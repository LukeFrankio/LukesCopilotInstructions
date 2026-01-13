# Takum Bit Encoding Reference

This document provides the complete specification for Takum bit-level encoding.

## Bit Field Structure

### General Layout (n-bit Takum)

```
MSB                                                              LSB
┌─────┬─────┬─────────────┬────────────────────┬────────────────────┐
│  S  │  D  │   R₂R₁R₀    │   Characteristic   │      Mantissa      │
│ 1b  │ 1b  │    3b       │      r bits        │    n-5-r bits      │
└─────┴─────┴─────────────┴────────────────────┴────────────────────┘
```

### Field Definitions

| Field | Bits | Range | Description |
|-------|------|-------|-------------|
| **S** (Sign) | 1 | {0, 1} | Sign bit: 0 = positive, 1 = negative |
| **D** (Direction) | 1 | {0, 1} | Direction: 0 = magnitude < 1, 1 = magnitude ≥ 1 |
| **R** (Regime) | 3 | {0, ..., 7} | Determines characteristic length |
| **C** (Characteristic) | r | Variable | Integer part of logarithmic exponent |
| **M** (Mantissa) | n-5-r | Variable | Fractional precision bits |

## Sign Field (S)

The sign bit determines the number's sign:

| S | Meaning | Effect on Value |
|---|---------|----------------|
| 0 | Positive | value > 0 |
| 1 | Negative | value < 0 (except NaR) |

**Important**: Takum uses **two's complement** representation. The entire n-bit value is treated as a signed integer.

### Two's Complement Encoding

```
Positive value t:    stored directly as signed integer
Negative value -t:   stored as two's complement of |t|
```

This means:

- Negation is standard two's complement negation: `-t` in the programming language
- Comparison uses signed integer comparison
- Zero is unique (no +0/-0 distinction)

## Direction Field (D)

The direction bit indicates whether the magnitude is less than or greater than 1:

| D | Characteristic Range | Magnitude |
|---|---------------------|-----------|
| 0 | c ∈ {-255, ..., -1} | |x| < 1 |
| 1 | c ∈ {0, ..., 254} | |x| ≥ 1 |

### Direction and Characteristic Relationship

The direction determines the characteristic bias:

```
D = 0:  c_min = -255, c_max = -1   (negative characteristics)
D = 1:  c_min = 0,    c_max = 254  (non-negative characteristics)
```

## Regime Field (R)

The 3-bit regime encodes the number of additional characteristic bits (r):

| R₂R₁R₀ | r (char bits) | Mantissa bits (n=16) | Mantissa bits (n=32) |
|--------|---------------|---------------------|---------------------|
| 000 | 0 | 11 | 27 |
| 001 | 1 | 10 | 26 |
| 010 | 2 | 9 | 25 |
| 011 | 3 | 8 | 24 |
| 100 | 4 | 7 | 23 |
| 101 | 5 | 6 | 22 |
| 110 | 6 | 5 | 21 |
| 111 | 7 | 4 | 20 |

### Regime Formula

```
r = R (direct value interpretation)
mantissa_bits = n - 5 - r
```

## Characteristic Field (C)

The characteristic encodes the integer part of the logarithmic exponent.

### Characteristic Encoding

The characteristic is encoded as an unsigned integer offset from a bias:

```
c = c_bias[D][R] + C_bits
```

### Characteristic Bias Lookup Table

| Index | D | R | c_bias | Representable c values |
|-------|---|---|--------|----------------------|
| 0 | 0 | 0 | -255 | {-255} |
| 1 | 0 | 1 | -127 | {-127, -126} |
| 2 | 0 | 2 | -63 | {-63, -62, -61, -60} |
| 3 | 0 | 3 | -31 | {-31, ..., -24} |
| 4 | 0 | 4 | -15 | {-15, ..., -8} |
| 5 | 0 | 5 | -7 | {-7, ..., 0} |
| 6 | 0 | 6 | -3 | {-3, ..., 4} |
| 7 | 0 | 7 | -1 | {-1, ..., 14} |
| 8 | 1 | 0 | 0 | {0} |
| 9 | 1 | 1 | 1 | {1, 2} |
| 10 | 1 | 2 | 3 | {3, 4, 5, 6} |
| 11 | 1 | 3 | 7 | {7, ..., 14} |
| 12 | 1 | 4 | 15 | {15, ..., 22} |
| 13 | 1 | 5 | 31 | {31, ..., 38} |
| 14 | 1 | 6 | 63 | {63, ..., 78} |
| 15 | 1 | 7 | 127 | {127, ..., 254} |

### C Code for Bias LUT

```c
static const int16_t c_bias_lut[16] = {
    // D=0, R=0..7
    -255, -127, -63, -31, -15, -7, -3, -1,
    // D=1, R=0..7
    0, 1, 3, 7, 15, 31, 63, 127
};
```

## Mantissa Field (M)

The mantissa provides fractional precision within the characteristic interval.

### Mantissa Interpretation

```
mantissa_value = M / 2^p
```

Where:

- `M` is the raw mantissa bits as unsigned integer
- `p` is the number of mantissa bits (n - 5 - r)

### Precision Guarantee

**Key property**: For any n-bit takum (n ≥ 12):

```
minimum_mantissa_bits = n - 5 - 7 = n - 12
```

Examples:

| Type | n | Min mantissa bits |
|------|---|-------------------|
| takum8 | 8 | -4 (N/A) |
| takum16 | 16 | 4 |
| takum32 | 32 | 20 |
| takum64 | 64 | 52 |

## Complete Encoding Examples

### Example 1: takum_log16 = 1.0

Value: 1.0 = √e^0

```
l = 0  (logarithmic value)
c = 0  (characteristic)
m = 0  (mantissa)
D = 1  (magnitude ≥ 1)
R = 0  (c=0 uses D=1,R=0)
C_bits = 0 (c - c_bias = 0 - 0 = 0)
M = 0

Bit pattern: 0|1|000|00000000000 = 0x2000
```

### Example 2: takum_log16 = 2.0

Value: 2.0 = √e^(2·ln(2)) ≈ √e^1.386

```
l ≈ 1.386
c = 1
m ≈ 0.386
D = 1  (magnitude ≥ 1)
R = 1  (c=1 uses D=1,R=1, c_bias=1)
C_bits = 0 (c - c_bias = 1 - 1 = 0)
M = round(0.386 × 2^10) = 395

Bit pattern: 0|1|001|0|1100001011 = 0x260B (approximate)
```

### Example 3: takum_log16 = 0.5

Value: 0.5 = √e^(2·ln(0.5)) = √e^(-1.386...)

```
l ≈ -1.386
c = -2 (floor)
m ≈ 0.614
D = 0  (magnitude < 1)
R = 6  (c=-2 fits in D=0,R=6, c_bias=-3)
C_bits = 1 (c - c_bias = -2 - (-3) = 1)
M = round(0.614 × 2^5) = 20

Bit pattern: 0|0|110|1|10100 = 0x0D94 (approximate)
```

### Example 4: NaR

```
Bit pattern: 1|0|000|00000000000 = 0x8000 (INT16_MIN)
```

### Example 5: Zero

```
Bit pattern: 0|0|000|00000000000 = 0x0000
```

## Decoding Algorithm

### Pseudocode

```
DECODE(bits, n):
    if bits == NaR_PATTERN:
        return NaR
    if bits == 0:
        return 0
    
    sign = (bits < 0)
    abs_bits = sign ? -bits : bits
    
    # Extract fields
    D = (abs_bits >> (n-2)) & 1
    R = (abs_bits >> (n-5)) & 7
    
    # Calculate precision
    r = R
    p = n - 5 - r
    
    # Get characteristic
    DR_index = (D << 3) | R
    c_bias = C_BIAS_LUT[DR_index]
    
    # Extract additional characteristic bits
    c_extra_mask = (1 << r) - 1
    c_extra = (abs_bits >> p) & c_extra_mask
    c = c_bias + c_extra
    
    # Extract mantissa
    m_mask = (1 << p) - 1
    m_bits = abs_bits & m_mask
    m = m_bits / (1 << p)
    
    # Compute logarithmic value
    l = c + m
    if sign:
        l = -l
    
    return l
```

## Encoding Algorithm

### Pseudocode

```
ENCODE(l, n):
    if isnan(l):
        return NaR_PATTERN
    if l == -INFINITY:
        return 0  # log(0) = -∞
    
    sign = (l < 0)
    l_abs = abs(l)
    
    # Clamp to representable range
    l_max = 254 + (1 - 2^(-(n-12)))
    l_abs = min(l_abs, l_max)
    
    # Separate characteristic and mantissa
    c = floor(l_abs)
    m = l_abs - c
    
    # Determine D and R
    if c < 0:
        D = 0
        # Find R such that c_bias[0][R] <= c < c_bias[0][R] + 2^R
    else:
        D = 1
        # Find R such that c_bias[1][R] <= c < c_bias[1][R] + 2^R
    
    # Calculate field values
    r = R
    p = n - 5 - r
    DR_index = (D << 3) | R
    c_extra = c - C_BIAS_LUT[DR_index]
    m_bits = round(m * (1 << p))
    
    # Handle rounding overflow
    if m_bits >= (1 << p):
        # Carry to characteristic
        c_extra += 1
        m_bits = 0
        # May need to adjust R
    
    # Assemble bits
    abs_bits = (D << (n-2)) | (R << (n-5)) | (c_extra << p) | m_bits
    
    # Apply sign (two's complement)
    bits = sign ? -abs_bits : abs_bits
    
    return bits
```

## Precision Bit Count by (D, R)

### takum_log16 (n=16)

| D | R | r | p | Total fixed | c range |
|---|---|---|---|-------------|---------|
| 0 | 0 | 0 | 11 | 5 | {-255} |
| 0 | 1 | 1 | 10 | 6 | {-127, -126} |
| 0 | 2 | 2 | 9 | 7 | {-63...-60} |
| 0 | 3 | 3 | 8 | 8 | {-31...-24} |
| 0 | 4 | 4 | 7 | 9 | {-15...-8} |
| 0 | 5 | 5 | 6 | 10 | {-7...0} |
| 0 | 6 | 6 | 5 | 11 | {-3...4} |
| 0 | 7 | 7 | 4 | 12 | {-1...14} |
| 1 | 0 | 0 | 11 | 5 | {0} |
| 1 | 1 | 1 | 10 | 6 | {1, 2} |
| 1 | 2 | 2 | 9 | 7 | {3...6} |
| 1 | 3 | 3 | 8 | 8 | {7...14} |
| 1 | 4 | 4 | 7 | 9 | {15...22} |
| 1 | 5 | 5 | 6 | 10 | {31...38} |
| 1 | 6 | 6 | 5 | 11 | {63...78} |
| 1 | 7 | 7 | 4 | 12 | {127...254} |

## Value Range Summary

### Positive Values

| Type | Min Positive | Max Positive |
|------|--------------|--------------|
| takum_log8 | √e^-15 ≈ 5.53×10^-4 | √e^14.875 ≈ 1.69×10^3 |
| takum_log16 | √e^-255 ≈ 4.20×10^-56 | √e^254.9375 ≈ 2.38×10^55 |
| takum_log32 | √e^-255 ≈ 4.20×10^-56 | √e^254.99999... ≈ 2.38×10^55 |
| takum_log64 | √e^-255 ≈ 4.20×10^-56 | √e^254.99999... ≈ 2.38×10^55 |

### Dynamic Range (in decades)

```
For n ≥ 16: ~111 decades (from 10^-56 to 10^55)
```

## Monotonicity Property

**Theorem**: The takum encoding is **monotonic** with respect to the underlying signed integer representation.

This means:

- If `a > b` (as takum values), then `a > b` (as signed integers)
- Comparison can use standard signed integer comparison
- Sorting requires no special handling

## Implementation Notes

### Type Punning

Safe type punning via unions:

```c
union takum_log16_union {
    int16_t value;   // Signed interpretation
    uint16_t bits;   // Unsigned for bit manipulation
};
```

### NaR Detection

```c
#define IS_NAR_16(t) ((t) == INT16_MIN)
```

### Zero Detection

```c
#define IS_ZERO(t) ((t) == 0)
```

### Sign Extraction

```c
#define SIGN(t) ((t) < 0)
```
