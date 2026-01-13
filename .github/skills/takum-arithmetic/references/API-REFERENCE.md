# Takum API Reference

Complete function catalog for Takum arithmetic operations based on the libtakum reference implementation.

## Type Definitions

### Logarithmic Takums (Standard)

```c
typedef int8_t  takum_log8;   // 8-bit logarithmic takum
typedef int16_t takum_log16;  // 16-bit logarithmic takum
typedef int32_t takum_log32;  // 32-bit logarithmic takum
typedef int64_t takum_log64;  // 64-bit logarithmic takum
```

### Linear Takums

```c
typedef int8_t  takum8;   // 8-bit linear takum
typedef int16_t takum16;  // 16-bit linear takum
typedef int32_t takum32;  // 32-bit linear takum
typedef int64_t takum64;  // 64-bit linear takum
```

## Constants

### NaR (Not a Real)

```c
#define TAKUM8_NAR       (INT8_C(-127) - INT8_C(1))       // -128
#define TAKUM16_NAR      (INT16_C(-32767) - INT16_C(1))   // -32768
#define TAKUM32_NAR      (INT32_C(-2147483647) - INT32_C(1))
#define TAKUM64_NAR      (INT64_C(-9223372036854775807) - INT64_C(1))

#define TAKUM_LOG8_NAR   TAKUM8_NAR
#define TAKUM_LOG16_NAR  TAKUM16_NAR
#define TAKUM_LOG32_NAR  TAKUM32_NAR
#define TAKUM_LOG64_NAR  TAKUM64_NAR
```

### Unity (1.0)

```c
#define TAKUM8_ONE       0x20
#define TAKUM16_ONE      0x2000
#define TAKUM32_ONE      0x20000000
#define TAKUM64_ONE      0x2000000000000000

#define TAKUM_LOG8_ONE   TAKUM8_ONE
#define TAKUM_LOG16_ONE  TAKUM16_ONE
#define TAKUM_LOG32_ONE  TAKUM32_ONE
#define TAKUM_LOG64_ONE  TAKUM64_ONE
```

### Mathematical Constants

#### Pi Variants

```c
// π
takum8  TAKUM8_PI;
takum16 TAKUM16_PI;
takum32 TAKUM32_PI;
takum64 TAKUM64_PI;

// 2π
takum8  TAKUM8_2_PI;
takum16 TAKUM16_2_PI;
// ... etc

// 3π, π/2, π/3, π/4, π/5, π/6
// All available for each type
```

#### Roots

```c
// √2
takum8  TAKUM8_SQUARE_ROOT_2;
takum16 TAKUM16_SQUARE_ROOT_2;
// ...

// √3, √5, √6 also available
```

#### Logarithms

```c
// ln(2)
takum8  TAKUM8_LN_2;
takum16 TAKUM16_LN_2;
// ...

// ln(10), lb(e), lb(10), lg(2), lg(e)
// All available for each type
```

#### Special Numbers

```c
// φ (Golden ratio)
takum8  TAKUM8_PHI;
takum16 TAKUM16_PHI;
// ...

// γ (Euler-Mascheroni constant)
takum8  TAKUM8_GAMMA;
takum16 TAKUM16_GAMMA;
// ...
```

## Arithmetic Operations

### Addition

```c
takum8  takum8_addition(takum8 a, takum8 b);
takum16 takum16_addition(takum16 a, takum16 b);
takum32 takum32_addition(takum32 a, takum32 b);
takum64 takum64_addition(takum64 a, takum64 b);

takum_log8  takum_log8_addition(takum_log8 a, takum_log8 b);
takum_log16 takum_log16_addition(takum_log16 a, takum_log16 b);
takum_log32 takum_log32_addition(takum_log32 a, takum_log32 b);
takum_log64 takum_log64_addition(takum_log64 a, takum_log64 b);
```

**Behavior:**

- NaR + anything = NaR
- 0 + x = x
- Uses float-domain computation

### Subtraction

```c
takum8  takum8_subtraction(takum8 a, takum8 b);
takum16 takum16_subtraction(takum16 a, takum16 b);
takum32 takum32_subtraction(takum32 a, takum32 b);
takum64 takum64_subtraction(takum64 a, takum64 b);

takum_log8  takum_log8_subtraction(takum_log8 a, takum_log8 b);
takum_log16 takum_log16_subtraction(takum_log16 a, takum_log16 b);
takum_log32 takum_log32_subtraction(takum_log32 a, takum_log32 b);
takum_log64 takum_log64_subtraction(takum_log64 a, takum_log64 b);
```

### Multiplication

```c
takum8  takum8_multiplication(takum8 a, takum8 b);
takum16 takum16_multiplication(takum16 a, takum16 b);
takum32 takum32_multiplication(takum32 a, takum32 b);
takum64 takum64_multiplication(takum64 a, takum64 b);

takum_log8  takum_log8_multiplication(takum_log8 a, takum_log8 b);
takum_log16 takum_log16_multiplication(takum_log16 a, takum_log16 b);
takum_log32 takum_log32_multiplication(takum_log32 a, takum_log32 b);
takum_log64 takum_log64_multiplication(takum_log64 a, takum_log64 b);
```

**Behavior (logarithmic):**

- O(1) complexity via l-domain addition
- sign(result) = sign(a) XOR sign(b)
- l_result = l_a + l_b

### Division

```c
takum8  takum8_division(takum8 a, takum8 b);
takum16 takum16_division(takum16 a, takum16 b);
takum32 takum32_division(takum32 a, takum32 b);
takum64 takum64_division(takum64 a, takum64 b);

takum_log8  takum_log8_division(takum_log8 a, takum_log8 b);
takum_log16 takum_log16_division(takum_log16 a, takum_log16 b);
takum_log32 takum_log32_division(takum_log32 a, takum_log32 b);
takum_log64 takum_log64_division(takum_log64 a, takum_log64 b);
```

**Behavior:**

- x / 0 = NaR
- NaR / anything = NaR
- O(1) for logarithmic takums

## Power and Root Functions

### General Power

```c
takum8  takum8_power(takum8 base, takum8 exponent);
takum16 takum16_power(takum16 base, takum16 exponent);
takum32 takum32_power(takum32 base, takum32 exponent);
takum64 takum64_power(takum64 base, takum64 exponent);

takum_log8  takum_log8_power(takum_log8 base, takum_log8 exponent);
takum_log16 takum_log16_power(takum_log16 base, takum_log16 exponent);
takum_log32 takum_log32_power(takum_log32 base, takum_log32 exponent);
takum_log64 takum_log64_power(takum_log64 base, takum_log64 exponent);
```

### Integer Power

```c
takum8  takum8_integer_power(takum8 base, int64_t n);
takum16 takum16_integer_power(takum16 base, int64_t n);
takum32 takum32_integer_power(takum32 base, int64_t n);
takum64 takum64_integer_power(takum64 base, int64_t n);

takum_log8  takum_log8_integer_power(takum_log8 base, int64_t n);
takum_log16 takum_log16_integer_power(takum_log16 base, int64_t n);
takum_log32 takum_log32_integer_power(takum_log32 base, int64_t n);
takum_log64 takum_log64_integer_power(takum_log64 base, int64_t n);
```

**Behavior:**

- 0^0 = NaR
- x^0 = 1 for x ≠ 0
- O(1) for logarithmic: l_result = l_base × n

### Square Root

```c
takum8  takum8_square_root(takum8 t);
takum16 takum16_square_root(takum16 t);
takum32 takum32_square_root(takum32 t);
takum64 takum64_square_root(takum64 t);

takum_log8  takum_log8_square_root(takum_log8 t);
takum_log16 takum_log16_square_root(takum_log16 t);
takum_log32 takum_log32_square_root(takum_log32 t);
takum_log64 takum_log64_square_root(takum_log64 t);
```

**Behavior:**

- √(negative) = NaR
- O(1) for logarithmic: l_result = l / 2

### N-th Root

```c
takum8  takum8_root(takum8 t, int64_t n);
takum16 takum16_root(takum16 t, int64_t n);
takum32 takum32_root(takum32 t, int64_t n);
takum64 takum64_root(takum64 t, int64_t n);

takum_log8  takum_log8_root(takum_log8 t, int64_t n);
takum_log16 takum_log16_root(takum_log16 t, int64_t n);
takum_log32 takum_log32_root(takum_log32 t, int64_t n);
takum_log64 takum_log64_root(takum_log64 t, int64_t n);
```

**Behavior:**

- root(x, 0) = NaR
- root(negative, even n) = NaR

## Exponential Functions

### Natural Exponential

```c
takum8  takum8_exp(takum8 t);         // e^t
takum8  takum8_exp_minus_1(takum8 t); // e^t - 1 (accurate near 0)
// ... for all types
```

### Base-2 Exponential

```c
takum8  takum8_2_raised(takum8 t);          // 2^t
takum8  takum8_2_raised_minus_1(takum8 t);  // 2^t - 1
// ... for all types
```

### Base-10 Exponential

```c
takum8  takum8_10_raised(takum8 t);         // 10^t
takum8  takum8_10_raised_minus_1(takum8 t); // 10^t - 1
// ... for all types
```

## Logarithmic Functions

### Natural Logarithm (ln)

```c
takum8  takum8_ln(takum8 t);         // ln(t)
takum8  takum8_ln_1_plus(takum8 t);  // ln(1 + t) (accurate near 0)
// ... for all types
```

### Binary Logarithm (lb = log₂)

```c
takum8  takum8_lb(takum8 t);         // log₂(t)
takum8  takum8_lb_1_plus(takum8 t);  // log₂(1 + t)
// ... for all types
```

### Decadic Logarithm (lg = log₁₀)

```c
takum8  takum8_lg(takum8 t);         // log₁₀(t)
takum8  takum8_lg_1_plus(takum8 t);  // log₁₀(1 + t)
// ... for all types
```

## Trigonometric Functions

### Sine

```c
takum8  takum8_sin(takum8 t);           // sin(t)
takum8  takum8_sin_pi_times(takum8 t);  // sin(π·t) with exact special values
// ... for all types
```

### Cosine

```c
takum8  takum8_cos(takum8 t);           // cos(t)
takum8  takum8_cos_pi_times(takum8 t);  // cos(π·t) with exact special values
// ... for all types
```

### Tangent

```c
takum8  takum8_tan(takum8 t);           // tan(t)
takum8  takum8_tan_pi_times(takum8 t);  // tan(π·t)
// ... for all types
```

### Cotangent

```c
takum8  takum8_cot(takum8 t);           // cot(t) = 1/tan(t)
takum8  takum8_cot_pi_times(takum8 t);  // cot(π·t)
// ... for all types
```

### Secant

```c
takum8  takum8_sec(takum8 t);           // sec(t) = 1/cos(t)
takum8  takum8_sec_pi_times(takum8 t);  // sec(π·t)
// ... for all types
```

### Cosecant

```c
takum8  takum8_csc(takum8 t);           // csc(t) = 1/sin(t)
takum8  takum8_csc_pi_times(takum8 t);  // csc(π·t)
// ... for all types
```

## Inverse Trigonometric Functions

### Arcsine

```c
takum8  takum8_arcsin(takum8 t);          // arcsin(t)
takum8  takum8_arcsin_over_pi(takum8 t);  // arcsin(t)/π
// ... for all types
```

### Arccosine

```c
takum8  takum8_arccos(takum8 t);          // arccos(t)
takum8  takum8_arccos_over_pi(takum8 t);  // arccos(t)/π
// ... for all types
```

### Arctangent

```c
takum8  takum8_arctan(takum8 t);           // arctan(t)
takum8  takum8_arctan_over_pi(takum8 t);   // arctan(t)/π
takum8  takum8_arctan2(takum8 y, takum8 x); // atan2(y, x)
takum8  takum8_arctan2_over_pi(takum8 y, takum8 x);
// ... for all types
```

### Arccotangent

```c
takum8  takum8_arccot(takum8 t);          // arccot(t)
takum8  takum8_arccot_over_pi(takum8 t);  // arccot(t)/π
// ... for all types
```

### Arcsecant

```c
takum8  takum8_arcsec(takum8 t);          // arcsec(t)
takum8  takum8_arcsec_over_pi(takum8 t);  // arcsec(t)/π
// ... for all types
```

### Arccosecant

```c
takum8  takum8_arccsc(takum8 t);          // arccsc(t)
takum8  takum8_arccsc_over_pi(takum8 t);  // arccsc(t)/π
// ... for all types
```

## Hyperbolic Functions

### Basic Hyperbolic

```c
takum8  takum8_sinh(takum8 t);  // sinh(t)
takum8  takum8_cosh(takum8 t);  // cosh(t)
takum8  takum8_tanh(takum8 t);  // tanh(t)
takum8  takum8_coth(takum8 t);  // coth(t) = 1/tanh(t)
takum8  takum8_sech(takum8 t);  // sech(t) = 1/cosh(t)
takum8  takum8_csch(takum8 t);  // csch(t) = 1/sinh(t)
// ... for all types
```

### Inverse Hyperbolic

```c
takum8  takum8_arsinh(takum8 t);  // arsinh(t)
takum8  takum8_arcosh(takum8 t);  // arcosh(t)
takum8  takum8_artanh(takum8 t);  // artanh(t)
takum8  takum8_arcoth(takum8 t);  // arcoth(t)
takum8  takum8_arsech(takum8 t);  // arsech(t)
takum8  takum8_arcsch(takum8 t);  // arcsch(t)
// ... for all types
```

## Utility Functions

### Absolute Value

```c
takum8  takum8_absolute(takum8 t);
takum16 takum16_absolute(takum16 t);
takum32 takum32_absolute(takum32 t);
takum64 takum64_absolute(takum64 t);
// ... and log variants
```

**Implementation:**

```c
// Branchless
return (t < 0) * (-t) + (t >= 0) * t;
```

### Sign Function

```c
takum8  takum8_sign(takum8 t);  // Returns -1, 0, or 1 (as takum)
// ... for all types
```

### Inversion (Reciprocal)

```c
takum8  takum8_inversion(takum8 t);  // 1/t
// ... for all types
```

**Behavior (logarithmic):**

- O(1) via bit manipulation
- NaR or 0 → NaR
- Always exact (no rounding)

### Precision Query

```c
uint8_t takum8_precision(takum8 t);   // Returns mantissa bit count
uint8_t takum16_precision(takum16 t);
uint8_t takum32_precision(takum32 t);
uint8_t takum64_precision(takum64 t);
// ... and log variants
```

### Hypotenuse

```c
takum8  takum8_hypotenuse(takum8 a, takum8 b);  // √(a² + b²)
// ... for all types
```

## Type Conversions

### Float to Takum

```c
// From float32
takum8  takum8_from_float32(float f);
takum16 takum16_from_float32(float f);
takum32 takum32_from_float32(float f);
takum64 takum64_from_float32(float f);
// ... and log variants

// From float64
takum8  takum8_from_float64(double f);
takum16 takum16_from_float64(double f);
takum32 takum32_from_float64(double f);
takum64 takum64_from_float64(double f);
// ... and log variants

// From extended float (long double)
takum8  takum8_from_extended_float(long double f);
takum16 takum16_from_extended_float(long double f);
takum32 takum32_from_extended_float(long double f);
takum64 takum64_from_extended_float(long double f);
// ... and log variants
```

### Takum to Float

```c
// To float32
float takum8_to_float32(takum8 t);
float takum16_to_float32(takum16 t);
float takum32_to_float32(takum32 t);
float takum64_to_float32(takum64 t);
// ... and log variants

// To float64
double takum8_to_float64(takum8 t);
double takum16_to_float64(takum16 t);
double takum32_to_float64(takum32 t);
double takum64_to_float64(takum64 t);
// ... and log variants

// To extended float
long double takum8_to_extended_float(takum8 t);
long double takum16_to_extended_float(takum16 t);
long double takum32_to_extended_float(takum32 t);
long double takum64_to_extended_float(takum64 t);
// ... and log variants
```

### Between Takum Types

```c
// Linear ↔ Logarithmic (same width)
takum8  takum8_from_takum_log8(takum_log8 t);
takum_log8 takum_log8_from_takum8(takum8 t);
// ... for all widths

// Width conversions (expansion - lossless)
takum16 takum16_from_takum8(takum8 t);
takum32 takum32_from_takum8(takum8 t);
takum32 takum32_from_takum16(takum16 t);
takum64 takum64_from_takum8(takum8 t);
takum64 takum64_from_takum16(takum16 t);
takum64 takum64_from_takum32(takum32 t);
// ... and log variants

// Width conversions (reduction - may lose precision)
takum8  takum8_from_takum16(takum16 t);
takum8  takum8_from_takum32(takum32 t);
takum8  takum8_from_takum64(takum64 t);
takum16 takum16_from_takum32(takum32 t);
takum16 takum16_from_takum64(takum64 t);
takum32 takum32_from_takum64(takum64 t);
// ... and log variants
```

## Function Summary Table

| Category | Functions | Count |
|----------|-----------|-------|
| Arithmetic | addition, subtraction, multiplication, division | 32 |
| Power/Root | power, integer_power, square_root, root | 32 |
| Exponential | exp, exp_minus_1, 2_raised, 2_raised_minus_1, 10_raised, 10_raised_minus_1 | 48 |
| Logarithmic | ln, ln_1_plus, lb, lb_1_plus, lg, lg_1_plus | 48 |
| Trigonometric | sin, cos, tan, cot, sec, csc (+ pi_times variants) | 96 |
| Inverse Trig | arcsin, arccos, arctan, arccot, arcsec, arccsc (+ over_pi, arctan2) | 112 |
| Hyperbolic | sinh, cosh, tanh, coth, sech, csch | 48 |
| Inverse Hyperbolic | arsinh, arcosh, artanh, arcoth, arsech, arcsch | 48 |
| Utility | absolute, sign, inversion, precision, hypotenuse | 40 |
| Conversion | float ↔ takum, takum ↔ takum | ~100 |
| **Total** | | **~600** |
