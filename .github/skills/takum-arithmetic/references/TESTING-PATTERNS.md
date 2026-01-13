# Takum Testing Patterns Reference

This document describes testing strategies for Takum arithmetic implementations based on the libtakum test suite.

## Testing Philosophy

The libtakum test framework follows these principles:

1. **Exhaustive for small types** - Full enumeration feasible for 8/16-bit
2. **Statistical for large types** - LFSR sampling for 32/64-bit
3. **Reference via long double** - Maximum precision for comparison
4. **LULP tolerance** - ±1 last unit for non-roundtrip tests
5. **Exact for roundtrips** - Bidirectional conversions must be exact

## Test Categories

### 1. Roundtrip Tests

Verify that conversions are lossless where expected:

```c
// Float → Takum → Float roundtrip
void test_roundtrip_float64(void) {
    for (takum_log16 t = MIN; t <= MAX; t++) {
        if (t == TAKUM_LOG16_NAR) continue;
        
        double f = takum_log16_to_float64(t);
        takum_log16 back = takum_log16_from_float64(f);
        
        assert(t == back);  // Must be exact
    }
}
```

### 2. Unary Function Tests

Test single-argument functions against reference implementations:

```c
// Reference implementation in long double
long double sin_reference(long double x) {
    if (!isfinite(x)) return NAN;
    return sinl(x);
}

// Test function
void test_sin(void) {
    for (takum_log16 t = MIN; t <= MAX; t++) {
        takum_log16 result = takum_log16_sin(t);
        takum_log16 expected = compute_reference(t, sin_reference);
        
        assert_within_lulp(result, expected, 1);
    }
}
```

### 3. Binary Function Tests

Test two-argument functions:

```c
void test_addition(void) {
    for (takum_log16 a = MIN; a <= MAX; a++) {
        for (takum_log16 b = MIN; b <= MAX; b++) {
            takum_log16 result = takum_log16_addition(a, b);
            takum_log16 expected = compute_reference_binary(a, b, add_ref);
            
            assert_within_lulp(result, expected, 1);
        }
    }
}
```

### 4. Constants Tests

Verify pre-computed constants:

```c
void test_constants(void) {
    // PI
    double pi_as_float = takum_log16_to_float64(TAKUM_LOG16_PI);
    assert(fabs(pi_as_float - M_PI) < EPSILON);
    
    // Check roundtrip
    takum_log16 pi_back = takum_log16_from_float64(M_PI);
    assert(pi_back == TAKUM_LOG16_PI);
}
```

### 5. Edge Case Tests

Specifically test boundary conditions:

```c
void test_edge_cases(void) {
    // NaR propagation
    assert(takum_log16_sin(TAKUM_LOG16_NAR) == TAKUM_LOG16_NAR);
    
    // Zero handling
    assert(takum_log16_sin(0) == 0);
    
    // Division by zero
    assert(takum_log16_division(TAKUM_LOG16_ONE, 0) == TAKUM_LOG16_NAR);
    
    // 0^0
    assert(takum_log16_integer_power(0, 0) == TAKUM_LOG16_NAR);
}
```

## Sampling Strategies

### Exhaustive Enumeration (Small Types)

For 8-bit and 16-bit types, test every possible value:

```c
// 8-bit: 256 values
// 16-bit: 65,536 values
// Unary: single loop
// Binary: nested loops (4 billion ops for 16-bit × 16-bit)

for (int32_t t = INT16_MIN; t <= INT16_MAX; t++) {
    test_unary_function((takum_log16)t);
}
```

### LFSR Random Sampling (Large Types)

For 32-bit and 64-bit, use maximal-length LFSR:

```c
// 32-bit LFSR: x³² + x²² + x² + x¹ + 1
uint32_t lfsr32_next(uint32_t state) {
    uint32_t bit = ((state >> 0) ^ (state >> 1) ^ 
                   (state >> 21) ^ (state >> 31)) & 1;
    return (state >> 1) | (bit << 31);
}

// Sample up to 4M values
#define MAX_SAMPLES (1 << 22)

void test_with_lfsr(void) {
    uint32_t lfsr = 1;  // Non-zero seed
    for (size_t i = 0; i < MAX_SAMPLES; i++) {
        takum_log32 t = (takum_log32)lfsr;
        test_unary_function(t);
        lfsr = lfsr32_next(lfsr);
    }
}
```

### Integer Test Cases

For functions with integer parameters (power, root):

```c
static const int64_t INTEGER_TEST_CASES[] = {
    -100, -10, -2, -1, 0, 1, 2, 10, 100
};

void test_integer_power(void) {
    for (takum_log16 base = MIN; base <= MAX; base++) {
        for (size_t i = 0; i < ARRAY_SIZE(INTEGER_TEST_CASES); i++) {
            int64_t exp = INTEGER_TEST_CASES[i];
            takum_log16 result = takum_log16_integer_power(base, exp);
            // ... verify
        }
    }
}
```

## Reference Function Patterns

### Float-Domain Reference

```c
// Generic reference using long double
long double generic_reference(long double input, 
                             long double (*stdlib_func)(long double)) {
    if (!isfinite(input)) {
        return NAN;  // NaR propagation
    }
    
    long double result = stdlib_func(input);
    
    // Handle overflow/underflow
    if (fetestexcept(FE_OVERFLOW)) {
        return copysign(LDBL_MAX, result);
    }
    if (fetestexcept(FE_UNDERFLOW) && result == 0.0L) {
        return copysign(LDBL_MIN, result);
    }
    
    return result;
}
```

### Special Angle References

```c
long double sin_pi_times_reference(long double x) {
    long double mod = fmodl(x, 2.0L);
    
    // Exact values at special angles
    if (mod == 0.0L) return 0.0L;
    if (mod == 0.5L) return 1.0L;
    if (mod == 1.0L) return 0.0L;
    if (mod == 1.5L) return -1.0L;
    
    return sinl(M_PI * x);
}
```

## Tolerance Checking

### LULP (Last Unit in Last Place) Check

```c
bool within_lulp(takum_log16 actual, takum_log16 expected, int tolerance) {
    if (actual == expected) return true;
    if (expected == TAKUM_LOG16_NAR) return actual == TAKUM_LOG16_NAR;
    
    int16_t diff = (int16_t)actual - (int16_t)expected;
    return abs(diff) <= tolerance;
}
```

### Exact Match (Roundtrips)

```c
bool exact_match(takum_log16 actual, takum_log16 expected) {
    return actual == expected;
}
```

## Test Framework Structure

### Test Block Definition

```c
struct test_block {
    const char* name;
    enum test_type type;
    union {
        // Unary: takum → takum
        struct {
            takum_log16 (*func)(takum_log16);
            long double (*ref)(long double);
        } unary;
        
        // Binary: (takum, takum) → takum
        struct {
            takum_log16 (*func)(takum_log16, takum_log16);
            long double (*ref)(long double, long double);
        } binary;
        
        // Integer: (takum, int64) → takum
        struct {
            takum_log16 (*func)(takum_log16, int64_t);
            long double (*ref)(long double, int64_t);
            const int64_t* int_cases;
            size_t num_int_cases;
        } integer;
    } data;
};
```

### Test Runner

```c
int run_test_block(struct test_block* block) {
    size_t passed = 0;
    size_t failed = 0;
    
    switch (block->type) {
    case TEST_UNARY:
        for (int32_t t = INT16_MIN; t <= INT16_MAX; t++) {
            if (test_unary_case(block, (takum_log16)t)) {
                passed++;
            } else {
                failed++;
                log_failure(block, t);
            }
        }
        break;
    // ... other types
    }
    
    printf("%s: %zu passed, %zu failed\n", block->name, passed, failed);
    return failed == 0 ? 0 : 1;
}
```

## Error Reporting

### Detailed Failure Output

```c
void log_failure(struct test_block* block, takum_log16 input,
                 takum_log16 actual, takum_log16 expected) {
    fprintf(stderr,
        "FAIL: %s\n"
        "  Input:    0x%04X (%.15Le)\n"
        "  Expected: 0x%04X (%.15Le)\n"
        "  Actual:   0x%04X (%.15Le)\n"
        "  Diff:     %d LULP\n",
        block->name,
        (uint16_t)input, takum_log16_to_float64(input),
        (uint16_t)expected, takum_log16_to_float64(expected),
        (uint16_t)actual, takum_log16_to_float64(actual),
        (int)((int16_t)actual - (int16_t)expected));
}
```

## Complete Test Suite Organization

### By Function Category

```structure
tests/
├── arithmetic/
│   ├── addition_test.c
│   ├── subtraction_test.c
│   ├── multiplication_test.c
│   └── division_test.c
├── power/
│   ├── power_test.c
│   ├── integer_power_test.c
│   ├── square_root_test.c
│   └── root_test.c
├── exponential/
│   ├── exp_test.c
│   ├── exp_minus_1_test.c
│   ├── 2_raised_test.c
│   └── 10_raised_test.c
├── logarithmic/
│   ├── ln_test.c
│   ├── lb_test.c
│   └── lg_test.c
├── trigonometric/
│   ├── sin_test.c
│   ├── cos_test.c
│   ├── tan_test.c
│   └── ...
├── hyperbolic/
│   ├── sinh_test.c
│   ├── cosh_test.c
│   └── ...
├── conversion/
│   ├── float_roundtrip_test.c
│   ├── type_conversion_test.c
│   └── codec_test.c
└── utility/
    ├── absolute_test.c
    ├── sign_test.c
    ├── inversion_test.c
    └── precision_test.c
```

### Test Execution

```bash
# Build all tests
make test

# Run individual test
./tests/arithmetic/addition_test

# Parallel execution
make -j test
```

## Property-Based Testing

### Commutativity

```c
void test_addition_commutative(void) {
    for (takum_log16 a = MIN; a <= MAX; a++) {
        for (takum_log16 b = MIN; b <= MAX; b++) {
            takum_log16 ab = takum_log16_addition(a, b);
            takum_log16 ba = takum_log16_addition(b, a);
            assert(ab == ba);  // a + b == b + a
        }
    }
}
```

### Associativity (Approximate)

```c
void test_addition_associative_approx(void) {
    // Due to rounding, can't guarantee exact associativity
    // Check that results are within tolerance
    for (takum_log16 a : sample_set) {
        for (takum_log16 b : sample_set) {
            for (takum_log16 c : sample_set) {
                takum_log16 ab_c = add(add(a, b), c);
                takum_log16 a_bc = add(a, add(b, c));
                assert_within_lulp(ab_c, a_bc, 2);
            }
        }
    }
}
```

### Identity Elements

```c
void test_identities(void) {
    for (takum_log16 x = MIN; x <= MAX; x++) {
        if (x == TAKUM_LOG16_NAR) continue;
        
        // Additive identity
        assert(takum_log16_addition(x, 0) == x);
        assert(takum_log16_addition(0, x) == x);
        
        // Multiplicative identity
        assert(takum_log16_multiplication(x, TAKUM_LOG16_ONE) == x);
        assert(takum_log16_multiplication(TAKUM_LOG16_ONE, x) == x);
        
        // Division by self
        if (x != 0) {
            assert(takum_log16_division(x, x) == TAKUM_LOG16_ONE);
        }
    }
}
```

### Double Inversion (Logarithmic)

```c
void test_double_inversion(void) {
    for (takum_log16 x = MIN; x <= MAX; x++) {
        if (x == TAKUM_LOG16_NAR || x == 0) continue;
        
        takum_log16 inv = takum_log16_inversion(x);
        takum_log16 back = takum_log16_inversion(inv);
        
        // For logarithmic takums, this MUST be exact
        assert(x == back);
    }
}
```

## Coverage Metrics

### Target Coverage

| Category | 8-bit | 16-bit | 32-bit | 64-bit   |
|----------|-------|--------|--------|----------|
| Unary    | 100%  | 100%   | ~6%    | <1%      |
| Binary   | 100%  | ~6%    | <0.01% | <0.0001% |
| Integer  | 100%  | 100%   | ~6%    | <1%      |

### Minimum Sample Recommendations

| Type   | Unary Tests   | Binary Tests       |
|--------|---------------|--------------------|
| 8-bit  | 256 (full)    | 65,536 (full)      |
| 16-bit | 65,536 (full) | 4M (sampled)       |
| 32-bit | 4M (sampled)  | 4M (sampled pairs) |
| 64-bit | 4M (sampled)  | 4M (sampled pairs) |
