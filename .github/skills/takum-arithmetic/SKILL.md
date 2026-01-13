---
name: takum-arithmetic
description: Implement and understand Takum arithmetic - a logarithmic tapered-precision number format using base √e. Use when working with numerical precision, floating-point alternatives, scientific computing, or implementing custom number systems. Covers encoding/decoding, arithmetic operations, transcendental functions, type conversions, and comparison with IEEE 754 and posits.
license: ISC
metadata:
  author: laslo-hunhold
  version: "2.0"
  paper: "arXiv:2404.18603v2"
  reference-implementation: "libtakum"
---

# Takum Arithmetic

Takum is a **logarithmic tapered-precision number format** that uses base √e instead of base 2.
It provides superior dynamic range while maintaining precision guarantees that IEEE 754 floats
and posits cannot match.

## When to Use This Skill

Activate this skill when:

- Implementing Takum numbers in any programming language
- Converting between Takum types and IEEE 754 floats
- Understanding bit-level encoding of Takum values
- Performing arithmetic operations (add, subtract, multiply, divide)
- Implementing transcendental functions (sin, cos, exp, log)
- Comparing Takum with IEEE 754 or posits
- Working with numerical precision requirements
- Designing scientific computing applications

## Core Concepts

### Two Takum Variants

| Variant                     | Types                 | Significand Domain | Best For                         |
| --------------------------- | --------------------- | ------------------ | ---------------------------------|
| **Logarithmic** (standard)  | `takum_log8/16/32/64` | Logarithmic        | Multiplication, division, powers |
| **Linear**                  | `takum8/16/32/64`     | Linear             | Addition, subtraction            |

**Recommendation**: Use logarithmic Takums unless your workload is addition-heavy.

### Dynamic Range (Constant for n≥12 bits)

```text
±(√e^-255, √e^255) ≈ ±(4.2×10^-56, 2.4×10^55)
```

This range is **identical** for takum16, takum32, and takum64.

### Bit Layout

```text
┌─────┬───────────┬─────────────────┬──────────────────────────┐
│  S  │  D │ R₂R₁R₀ │   Characteristic   │       Mantissa        │
│ 1b  │  1b│   3b   │     r bits         │    remaining bits     │
└─────┴───────────┴─────────────────┴──────────────────────────┘
```

- **S** (Sign): 0 = positive, 1 = negative
- **D** (Direction): 0 = magnitude < 1, 1 = magnitude ≥ 1
- **R** (Regime): Determines characteristic bit count (r = 0 to 7)
- **Characteristic**: Encodes exponent base √e
- **Mantissa**: Fractional precision bits

### Special Values

| Value              | Representation                       |
| ------------------ | ------------------------------------ |
| **Zero**           | All bits 0: `0b00000000…`            |
| **NaR** (Not a Real) | Sign=1, rest zeros: `0b10000000…`  |
| **One**            | Type-specific positive encoding      |

## Quick Reference

### Value Reconstruction

For logarithmic Takum with decoded value `l`:

```text
value = sign × √e^l = sign × e^(l/2)
```

### Characteristic Ranges

| Direction | Characteristic Range   |
| --------- | ---------------------- |
| D = 0     | c ∈ {-255, …, -1}      |
| D = 1     | c ∈ {0, …, 254}        |

### Regime to Mantissa Bits (takum16 example)

| Regime r | Mantissa bits p | Characteristic bits |
| -------- | --------------- | ------------------- |
| 0        | 11              | 0                   |
| 1        | 10              | 1                   |
| 2        | 9               | 2                   |
| …        | …               | …                   |
| 7        | 4               | 7                   |

**Minimum precision guarantee**: At least (n-12) mantissa bits for any value.

## Essential Operations

### Negation (Two's Complement)

```c
takum_neg(t) = -t  // Standard two's complement negation
```

### Inversion (Logarithmic Takums Only — O(1))

```c
// 1/x is just negating the logarithmic value!
takum_log_inversion(t) = (t ^ 0x7FFF...FF) + 1  // XOR non-sign bits, add 1
```

### Multiplication (Logarithmic — O(1))

```c
// In log domain: multiply = add exponents
l_result = l(a) + l(b)
sign = (a < 0) != (b < 0)
```

### Division (Logarithmic — O(1))

```c
// In log domain: divide = subtract exponents
l_result = l(a) - l(b)
sign = (a < 0) != (b < 0)
```

### Addition/Subtraction

Requires Gaussian logarithm computation — convert to linear domain, compute, convert back.

## Implementation Guide

### Step 1: Define Types

Use signed integers matching the bit width:

```c
typedef int8_t  takum_log8;
typedef int16_t takum_log16;
typedef int32_t takum_log32;
typedef int64_t takum_log64;
```

### Step 2: Define NaR Constants

NaR is the minimum signed value (two's complement minimum):

```c
#define TAKUM_LOG8_NAR  INT8_MIN   // -128
#define TAKUM_LOG16_NAR INT16_MIN  // -32768
#define TAKUM_LOG32_NAR INT32_MIN  // -2147483648
#define TAKUM_LOG64_NAR INT64_MIN  // -9223372036854775808
```

### Step 3: Create Lookup Tables

```c
// Maps (D|R₂|R₁|R₀) 4-bit index to characteristic bias
static const int16_t c_bias_lut[16] = {
    -255, -127, -63, -31, -15, -7, -3, -1,  // D=0
    0, 1, 3, 7, 15, 31, 63, 127             // D=1
};

// Maps (D|R₂|R₁|R₀) to mantissa bit count for takum16
static const uint8_t p_lut_16[16] = {
    11, 10, 9, 8, 7, 6, 5, 4,  // D=0 (r=0..7)
    11, 10, 9, 8, 7, 6, 5, 4   // D=1 (r=0..7)
};
```

### Step 4: Implement Decoding

```c
// Decode takum_log16 to logarithmic value l
double takum_log16_to_l(takum_log16 t) {
    if (t == TAKUM_LOG16_NAR) return NAN;
    if (t == 0) return -INFINITY;  // log(0) = -∞
    
    bool sign = t < 0;
    uint16_t bits = sign ? -t : t;
    
    uint8_t DR = (bits >> 11) & 0x0F;  // Extract D|R
    int16_t c = c_bias_lut[DR];
    uint8_t p = p_lut_16[DR];
    
    // Extract and add additional characteristic bits
    // Extract mantissa
    // Combine: l = c + m
    
    return sign ? -l : l;
}
```

### Step 5: Implement Encoding

```c
// Encode sign and logarithmic value to takum_log16
takum_log16 takum_log16_from_s_and_l(bool sign, double l) {
    if (isnan(l)) return TAKUM_LOG16_NAR;
    
    // Clamp to representable range
    l = clamp(l, -254.9375, 254.9375);
    
    // Separate into characteristic and mantissa
    int16_t c = (int16_t)floor(fabs(l));
    double m = fabs(l) - c;
    
    // Find DR from c using lookup table
    // Encode bits: S|D|R|C|M
    
    return sign ? -result : result;
}
```

## Conversion Examples

### Float64 to Takum

```c
takum_log16 from_float64(double f) {
    if (isnan(f)) return TAKUM_LOG16_NAR;
    if (f == 0.0) return 0;
    
    bool sign = f < 0;
    double l = 2.0 * log(fabs(f));  // l = 2·ln|f| = ln(|f|²)
    
    return takum_log16_from_s_and_l(sign, l);
}
```

### Takum to Float64

```c
double to_float64(takum_log16 t) {
    if (t == TAKUM_LOG16_NAR) return NAN;
    if (t == 0) return 0.0;
    
    double l = takum_log16_to_l(t);
    bool sign = t < 0;
    
    return (sign ? -1.0 : 1.0) * exp(l / 2.0);  // √e^l = e^(l/2)
}
```

## References

For detailed information, see:

- [BIT-ENCODING.md](references/BIT-ENCODING.md) — Complete bit layout specification
- [MATHEMATICAL-FOUNDATIONS.md](references/MATHEMATICAL-FOUNDATIONS.md) — Formal definitions and proofs
- [ALGORITHMS.md](references/ALGORITHMS.md) — Encoding/decoding algorithms
- [API-REFERENCE.md](references/API-REFERENCE.md) — Complete function catalog
- [CONVERSION-GUIDE.md](references/CONVERSION-GUIDE.md) — Type conversion patterns
- [EDGE-CASES.md](references/EDGE-CASES.md) — Special value handling
- [TESTING-PATTERNS.md](references/TESTING-PATTERNS.md) — Validation strategies
- [BUILD-GUIDE.md](references/BUILD-GUIDE.md) — Building the libtakum reference

## Key Advantages Over IEEE 754

| Property                    | IEEE 754                | Takum                    |
| --------------------------- | ----------------------- | ------------------------ |
| Dynamic range consistency   | Varies with precision   | **Constant** for n≥12    |
| Multiplication closure      | ~25% exact              | **40%+ exact**           |
| Inversion closure           | Rare                    | **100% exact** (log)     |
| Precision guarantee         | Variable                | **n-12 bits minimum**    |
| Zero representation         | +0 and -0               | **Single zero**          |
| Special values              | NaN, ±Inf, subnormals   | **Only NaR**             |

## Common Patterns

### Check for NaR

```c
bool is_nar(takum_log16 t) {
    return t == TAKUM_LOG16_NAR;
}
```

### Safe Division

```c
takum_log16 safe_divide(takum_log16 a, takum_log16 b) {
    if (is_nar(a) || is_nar(b) || b == 0) return TAKUM_LOG16_NAR;
    return takum_log16_division(a, b);
}
```

### Absolute Value (Branchless)

```c
takum_log16 takum_abs(takum_log16 t) {
    return (t < 0) * (-t) + (t >= 0) * t;
}
```

## Transcendental Functions

Use float-domain computation for transcendental functions:

```c
takum_log16 takum_sin(takum_log16 t) {
    double f = to_float64(t);
    double result = sin(f);
    return from_float64(result);
}
```

For `sinpi`, `cospi` variants, use exact values at special angles.

## Mathematical Constants

Pre-compute constants for each type:

| Constant | takum_log16 value |
| -------- | ----------------- |
| π        | `0x3C48`          |
| 2π       | `0x4648`          |
| √2       | `0x1684`          |
| e        | `0x2000`          |
| ln(2)    | `0xC91C`          |

See [constants.json](assets/constants.json) for all types.
