# Takum Edge Cases Reference

This document catalogs all edge cases and special value handling in Takum arithmetic.

## Special Values

### NaR (Not a Real)

**Representation**: Minimum signed integer

```c
TAKUM_LOG8_NAR  = -128          = 0x80
TAKUM_LOG16_NAR = -32768        = 0x8000
TAKUM_LOG32_NAR = -2147483648   = 0x80000000
TAKUM_LOG64_NAR = -9223372036854775808 = 0x8000000000000000
```

**When NaR is Produced**:

| Operation | Condition | Result |
|-----------|-----------|--------|
| Division | x / 0 | NaR |
| Division | 0 / 0 | NaR |
| Division | NaR / anything | NaR |
| Power | 0^0 | NaR |
| Square Root | √(negative) | NaR |
| N-th Root | root(negative, even n) | NaR |
| N-th Root | root(x, 0) | NaR |
| Inversion | 1/0 | NaR |
| Inversion | 1/NaR | NaR |
| Any | operation(NaR, ...) | NaR |
| Conversion | from NaN | NaR |

### Zero

**Representation**: All bits zero

```c
0 = 0x00 (8-bit)
0 = 0x0000 (16-bit)
0 = 0x00000000 (32-bit)
0 = 0x0000000000000000 (64-bit)
```

**Important**: Unlike IEEE 754, there is only ONE zero (no +0/-0 distinction).

**When Zero is Produced**:

| Operation | Condition | Result |
|-----------|-----------|--------|
| Any arithmetic | Underflow | 0 |
| Multiplication | x × 0 (x ≠ NaR) | 0 |
| Division | 0 / x (x ≠ 0, NaR) | 0 |
| Power | 0^n (n > 0) | 0 |
| Conversion | from 0.0 | 0 |

### One (Unity)

**Representation**: l = 0 encoded

```c
TAKUM_LOG8_ONE  = 0x20
TAKUM_LOG16_ONE = 0x2000
TAKUM_LOG32_ONE = 0x20000000
TAKUM_LOG64_ONE = 0x2000000000000000
```

**Properties**:

- `x × 1 = x`
- `x / 1 = x`
- `x^0 = 1` (for x ≠ 0, NaR)
- `√1 = 1`
- `1/1 = 1`

## Arithmetic Edge Cases

### Addition

```c
// NaR propagation
NaR + anything = NaR
anything + NaR = NaR

// Identity
0 + x = x
x + 0 = x

// Overflow
HUGE + HUGE = MAX_POSITIVE (saturates)

// Underflow
TINY + (-TINY) = 0 (may underflow)

// Sign handling
positive + positive = positive (or overflow)
negative + negative = negative (or underflow to max negative)
positive + negative = depends on magnitudes
```

### Subtraction

```c
// NaR propagation
NaR - anything = NaR
anything - NaR = NaR

// Identity
x - 0 = x

// Self-subtraction
x - x = 0 (for x ≠ NaR)

// Overflow/underflow
Same rules as addition with negated operand
```

### Multiplication

```c
// NaR propagation
NaR × anything = NaR
anything × NaR = NaR

// Zero rules
0 × x = 0 (for x ≠ NaR)
x × 0 = 0 (for x ≠ NaR)

// Identity
1 × x = x
x × 1 = x

// Overflow
HUGE × HUGE = MAX_POSITIVE (saturates)

// Underflow
TINY × TINY = 0 (underflows)

// Sign rules
positive × positive = positive
negative × negative = positive
positive × negative = negative
negative × positive = negative
```

### Division

```c
// NaR cases
NaR / anything = NaR
anything / NaR = NaR
x / 0 = NaR
0 / 0 = NaR

// Zero dividend
0 / x = 0 (for x ≠ 0, NaR)

// Identity
x / 1 = x

// Self-division
x / x = 1 (for x ≠ 0, NaR)

// Overflow
HUGE / TINY = MAX_POSITIVE (saturates)

// Underflow
TINY / HUGE = 0 (underflows)
```

### Power Operations

```c
// NaR cases
NaR^n = NaR
x^NaR = NaR (if base is takum)
0^0 = NaR (indeterminate)
0^(-n) = NaR (n > 0, division by zero)

// Zero base
0^n = 0 (for n > 0)

// Zero exponent
x^0 = 1 (for x ≠ 0, NaR)

// Negative base with fractional exponent
(-x)^(p/q) = NaR (for even q)
(-x)^(p/q) = -|x|^(p/q) (for odd q)

// Integer power sign rules
positive^n = positive (always)
negative^(even n) = positive
negative^(odd n) = negative

// Overflow
HUGE^2 = MAX_POSITIVE (saturates)

// Underflow
TINY^2 = 0 (underflows)
```

### Square Root

```c
// NaR cases
√NaR = NaR

// Negative input
√(negative) = NaR

// Zero
√0 = 0

// One
√1 = 1

// Normal positive
√positive = computed value
```

### N-th Root

```c
// NaR cases
root(NaR, n) = NaR
root(x, 0) = NaR (0th root undefined)

// Even root of negative
root(negative, even n) = NaR

// Odd root of negative
root(negative, odd n) = -root(|negative|, n)

// Zero
root(0, n) = 0 (for n ≠ 0)

// One
root(1, n) = 1 (for n ≠ 0)
```

### Inversion (1/x)

```c
// NaR cases
1/NaR = NaR
1/0 = NaR

// Identity
1/1 = 1

// Double inversion (logarithmic: always exact)
1/(1/x) = x (for x ≠ 0, NaR)

// Sign preservation
1/positive = positive
1/negative = negative

// Note: For logarithmic takums, inversion is ALWAYS exact
```

## Trigonometric Edge Cases

### sin(x)

```c
sin(NaR) = NaR
sin(0) = 0

// Special angles (sin_pi_times)
sin(π × 0) = 0
sin(π × 0.5) = 1
sin(π × 1.0) = 0
sin(π × 1.5) = -1
sin(π × 2.0) = 0
```

### cos(x)

```c
cos(NaR) = NaR
cos(0) = 1

// Special angles (cos_pi_times)
cos(π × 0) = 1
cos(π × 0.5) = 0
cos(π × 1.0) = -1
cos(π × 1.5) = 0
cos(π × 2.0) = 1
```

### tan(x)

```c
tan(NaR) = NaR
tan(0) = 0

// Poles (tan_pi_times)
tan(π × 0.5) = NaR (undefined)
tan(π × 1.5) = NaR (undefined)
```

### arcsin(x)

```c
arcsin(NaR) = NaR
arcsin(0) = 0

// Domain restriction
arcsin(x) where |x| > 1 = NaR
```

### arctan2(y, x)

```c
arctan2(NaR, x) = NaR
arctan2(y, NaR) = NaR

// Special cases
arctan2(0, positive) = 0
arctan2(0, negative) = π
arctan2(positive, 0) = π/2
arctan2(negative, 0) = -π/2
arctan2(0, 0) = NaR or 0 (implementation-defined)
```

## Exponential/Logarithmic Edge Cases

### exp(x)

```c
exp(NaR) = NaR

// Overflow
exp(HUGE) = MAX_POSITIVE (saturates)

// Underflow
exp(-HUGE) = 0 (underflows)

// Identity
exp(0) = 1
```

### ln(x)

```c
ln(NaR) = NaR
ln(0) = NaR (or -∞ depending on convention)
ln(negative) = NaR

// Identity
ln(1) = 0
```

### ln_1_plus(x) = ln(1+x)

```c
ln_1_plus(NaR) = NaR
ln_1_plus(-1) = NaR (ln(0) undefined)
ln_1_plus(x < -1) = NaR (ln of negative)

// Accurate near zero
ln_1_plus(TINY) ≈ TINY (avoids precision loss)
```

## Hyperbolic Edge Cases

### sinh(x)

```c
sinh(NaR) = NaR
sinh(0) = 0

// Overflow
sinh(HUGE) = MAX_POSITIVE (saturates)
```

### cosh(x)

```c
cosh(NaR) = NaR
cosh(0) = 1

// Overflow
cosh(HUGE) = MAX_POSITIVE (saturates)

// Note: cosh(x) ≥ 1 always
```

### tanh(x)

```c
tanh(NaR) = NaR
tanh(0) = 0

// Limits (no overflow possible)
tanh(HUGE) → 1
tanh(-HUGE) → -1
```

### artanh(x)

```c
artanh(NaR) = NaR

// Domain restriction
artanh(1) = +∞ (NaR in practice)
artanh(-1) = -∞ (NaR in practice)
artanh(x) where |x| > 1 = NaR
```

## Type Conversion Edge Cases

### Float → Takum

```c
// NaN handling
from_float(NaN) = NaR

// Infinity handling
from_float(+∞) = MAX_POSITIVE (saturates)
from_float(-∞) = MIN_NEGATIVE (saturates)

// Zero handling
from_float(0.0) = 0
from_float(-0.0) = 0 (takum has single zero)

// Overflow
from_float(HUGE_FLOAT) = MAX_POSITIVE
from_float(-HUGE_FLOAT) = MIN_NEGATIVE

// Underflow
from_float(TINY_FLOAT) = 0 or MIN_POSITIVE
```

### Takum → Float

```c
// NaR handling
to_float(NaR) = NaN

// Zero handling
to_float(0) = 0.0

// Range (takum fits in float64)
All takum values fit in float64 without overflow
```

### Takum → Takum (Reduction)

```c
// NaR handling
reduce(NaR) = NaR

// Saturation (avoid creating NaR from valid value)
If reduction would produce NaR pattern from non-NaR:
  result = MAX_POSITIVE or MIN_NEGATIVE (saturate)

// Rounding
Round-to-nearest-even is standard
```

## Comparison Edge Cases

```c
// NaR comparison
NaR is "less than" all other values (as signed integer)
NaR == NaR is true (as integer comparison)

// Zero comparison
0 > negative (for non-NaR negative)
0 < positive

// Sign comparison
All negative < 0 < all positive

// Monotonicity
If a > b (as values), then a > b (as integers)
```

## Precision Edge Cases

### Minimum Precision

For n-bit takum (n ≥ 12):

- Minimum mantissa bits = n - 12
- This occurs at extreme characteristic values (near ±255)

### Maximum Precision

- Maximum mantissa bits = n - 5
- This occurs when characteristic fits in 0 extra bits (r = 0)

### Precision at Unity

| Type | Precision at 1.0 |
|------|-----------------|
| takum_log8 | 3 bits |
| takum_log16 | 11 bits |
| takum_log32 | 27 bits |
| takum_log64 | 59 bits |

## Implementation Edge Case Checklist

When implementing Takum arithmetic, ensure handling for:

- [ ] NaR input detection
- [ ] Zero input detection
- [ ] Overflow saturation (don't create NaR from overflow)
- [ ] Underflow to zero
- [ ] Domain restrictions (sqrt of negative, etc.)
- [ ] Exact special values (sin_pi_times at 0, 0.5, 1, 1.5)
- [ ] 0^0 returns NaR
- [ ] Division by zero returns NaR
- [ ] Double inversion exactness (logarithmic)
- [ ] Rounding mode (round-to-nearest-even)
- [ ] Type reduction saturation
