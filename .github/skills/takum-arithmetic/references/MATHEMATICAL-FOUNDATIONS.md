# Mathematical Foundations of Takum Arithmetic

This document provides the formal mathematical definitions and proofs underlying Takum arithmetic.

## Gustafson's Criteria for Number Systems

John Gustafson proposed 10 criteria for evaluating numerical formats. Takums satisfy all 10:

### Criterion 1: Total Ordering

All representable values form a total order (no incomparable elements like NaN comparisons in IEEE 754).

### Criterion 2: Projective Closure

Infinity is handled uniformly (NaR represents "not a real number").

### Criterion 3: Exact Zero

Zero has a unique representation (no +0/-0 distinction).

### Criterion 4: Signed Negation

Negation is exact and symmetric.

### Criterion 5: Bit-Efficient

Maximum information density per bit.

### Criterion 6: Tapered Precision

Precision varies smoothly with magnitude.

### Criterion 7: Exact Reciprocal

For logarithmic takums, 1/x is always exactly representable if x is.

### Criterion 8: Closed Operations

Arithmetic operations stay within the representable set.

### Criterion 9: Comparison by Integer

Values can be compared using standard integer comparison.

### Criterion 10: Smooth Transitions

No discontinuities in precision at regime boundaries.

## Formal Definitions

### Definition 1: Takum Alphabet

```text
T = {0, 1}  (binary alphabet)
```

### Definition 2: Takum Encoding (Logarithmic)

A logarithmic n-bit takum is a tuple `(S, D, R, C, M)` where:

- `S ∈ {0, 1}` is the sign bit
- `D ∈ {0, 1}` is the direction bit
- `R ∈ {0, 1, ..., 7}` is the 3-bit regime
- `C ∈ T^r` is the r-bit characteristic (r determined by R)
- `M ∈ T^p` is the p-bit mantissa where `p = n - 5 - r`

The decoded value is:

```text
τ((S, D, R, C, M)) = (-1)^S × √e^ℓ
```

where:

```text
ℓ = (-1)^S × (c + m)
c = c_bias(D, R) + value(C)
m = value(M) / 2^p
```

### Definition 3: Characteristic Bias Function

```text
c_bias(D, R) = {
    -2^(8-R) + 1   if D = 0
    2^R - 1        if D = 1
}
```

Expanded lookup table:

| D | R | c_bias |
|---|---|--------|
| 0 | 0 | -255   |
| 0 | 1 | -127   |
| 0 | 2 | -63    |
| 0 | 3 | -31    |
| 0 | 4 | -15    |
| 0 | 5 | -7     |
| 0 | 6 | -3     |
| 0 | 7 | -1     |
| 1 | 0 | 0      |
| 1 | 1 | 1      |
| 1 | 2 | 3      |
| 1 | 3 | 7      |
| 1 | 4 | 15     |
| 1 | 5 | 31     |
| 1 | 6 | 63     |
| 1 | 7 | 127    |

### Definition 4: NaR (Not a Real)

```text
NaR = (1, 0, 0, ε, ε)
```

where `ε` denotes the empty string. Numerically, NaR is the minimum signed integer.

### Definition 5: Zero

```text
0 = (0, 0, 0, ε, ε)
```

All bits zero.

### Definition 6: Dynamic Range

For n-bit logarithmic takums (n ≥ 12):

```text
D_n = [√e^(-255), √e^(255-2^(12-n))]
     ≈ [4.2 × 10^(-56), 2.4 × 10^55]
```

**Key property**: The dynamic range is constant for all n ≥ 12.

### Definition 7: Machine Precision

For logarithmic takum with logarithmic value ℓ:

```text
ε(ℓ) = √e^ℓ × (√e^(2^(-p)) - 1)
```

where p is the mantissa bit count.

### Definition 8: Linear Takum Encoding

Linear takums use the same bit structure but with linear significand:

```text
τ_linear((S, D, R, C, M)) = (-1)^S × (1 + m) × 2^h
```

where h is derived from the characteristic.

## Key Propositions

### Proposition 1: Uniqueness

Every finite real number in the representable range has a unique takum encoding.

**Proof sketch**: The encoding function is injective by construction. The regime uniquely determines the characteristic range, and the mantissa provides sub-interval precision.

### Proposition 2: Monotonicity

The takum encoding preserves order:

```text
For takums a, b: a < b ⟺ int(a) < int(b)
```

where int() interprets the bit pattern as a signed integer.

**Proof sketch**: The two's complement representation ensures sign ordering. Within each sign, the direction-regime-characteristic-mantissa ordering mirrors numerical ordering.

### Proposition 3: Negation Exactness

For any takum t ≠ NaR:

```text
-(-t) = t
```

**Proof**: Two's complement negation is its own inverse for all values except the minimum (which is NaR).

### Proposition 4: Inversion Exactness (Logarithmic Only)

For any logarithmic takum t ≠ 0, NaR:

```text
1/(1/t) = t
```

**Proof**: In logarithmic representation:

```text
value(t) = √e^ℓ
1/value(t) = √e^(-ℓ)
```

The negation of ℓ is exact due to the two's complement-like bit manipulation.

### Proposition 5: Machine Precision Bound

For an n-bit logarithmic takum:

```text
max precision error ≤ (2/3) × 2^(-(n-12))
```

This bound is tighter than IEEE 754 floats of comparable bit width.

### Proposition 6: Characteristic Bound

For any n-bit takum (n ≥ 12):

```text
-255 ≤ c ≤ 254
```

The characteristic never exceeds 255 in absolute value, regardless of bit width.

### Proposition 7: Mantissa Bit Guarantee

For any n-bit takum (n ≥ 12):

```text
p ≥ n - 12
```

There are always at least (n-12) mantissa bits.

## Gaussian Logarithms

### Definition: Gaussian Addition Logarithm

```text
Φ_b^+(q) = log_b(1 + b^q)
```

### Definition: Gaussian Subtraction Logarithm

```text
Φ_b^-(q) = log_b(1 - b^q)  for q < 0
```

### Base Conversion for √e

```text
Φ_√e^±(q) = 2 × Φ_e^±(q/2)
```

This allows using standard natural logarithm tables.

### Application to Addition

For logarithmic takums with values √e^a and √e^b (assuming a ≥ b):

```text
√e^a + √e^b = √e^a × (1 + √e^(b-a))
            = √e^(a + Φ_√e^+(b-a))
```

### Application to Subtraction

```text
√e^a - √e^b = √e^a × (1 - √e^(b-a))
            = √e^(a + Φ_√e^-(b-a))  for a > b
```

## Closure Analysis

### Multiplication Closure

For n-bit logarithmic takums, multiplication is closed under:

```text
P(exact mult) ≈ 40% for random operands
```

This significantly exceeds IEEE 754 floats (~25%).

### Division Closure

For logarithmic takums:

```text
P(exact div) ≈ 40% for random operands
```

### Inversion Closure

For logarithmic takums:

```text
P(exact inversion) = 100%
```

Every non-zero takum has an exactly representable inverse.

### Addition/Subtraction Closure

```text
P(exact add/sub) < 5%
```

Addition and subtraction are rarely exact (require Gaussian logarithm computation).

## Comparison with IEEE 754

### Dynamic Range Comparison

| Format       | Dynamic Range (decades) |
|--------------|-------------------------|
| IEEE float32 | ~83                     |
| IEEE float64 | ~616                    |
| takum16      | ~111                    |
| takum32      | ~111                    |
| takum64      | ~111                    |

Takum has constant dynamic range regardless of bit width.

### Precision Comparison at Unity

| Format       | Precision at 1.0 |
|--------------|------------------|
| IEEE float32 | 24 bits          |
| IEEE float64 | 53 bits          |
| takum16      | 11 bits          |
| takum32      | 27 bits          |
| takum64      | 59 bits          |

### Special Value Comparison

| Property            | IEEE 754      | Takum             |
|---------------------|---------------|-------------------|
| Zeros               | +0, -0        | Single 0          |
| Infinities          | +∞, -∞        | None (saturates)  |
| NaN                 | Many patterns | Single NaR        |
| Subnormals          | Yes           | No (smooth taper) |

## Rounding

### Algorithm: Round to Nearest Even

For encoding a real number r as an n-bit takum:

1. Compute the ideal logarithmic value: `ℓ = 2 × ln(|r|)`
2. Determine the regime from ℓ
3. Round mantissa to available bits using round-to-nearest-even
4. Handle overflow (carry to characteristic) if needed
5. Saturate at boundaries (avoid NaR)

### Saturation Rules

| Condition           | Result                 |
|---------------------|------------------------|
| Overflow to +∞      | Maximum positive takum |
| Underflow to 0      | Minimum positive takum |
| Invalid input (NaN) | NaR                    |

## Transcendental Functions

### Exponential

```text
exp(√e^ℓ) = √e^(ℓ × √e^ℓ)
```

Must be computed in extended precision, then rounded.

### Natural Logarithm

```text
ln(√e^ℓ) = ℓ / 2
```

Simple scaling in logarithmic domain.

### Trigonometric

Standard float-domain computation with careful handling of special angles for `sinpi`, `cospi` variants.

## References

1. Hunhold, L. (2024). "Takum Arithmetic" arXiv:2404.18603v2
2. Gustafson, J. (2017). "Posit Arithmetic"
3. Goldberg, D. (1991). "What Every Computer Scientist Should Know About Floating-Point Arithmetic"
