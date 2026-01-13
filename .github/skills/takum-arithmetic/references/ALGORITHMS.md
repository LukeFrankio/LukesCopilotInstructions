# Takum Algorithms Reference

This document provides detailed algorithms for Takum encoding, decoding, and arithmetic operations.

## Algorithm 1: Decode Logarithmic Takum to Float

Converts an n-bit logarithmic takum to a floating-point value.

### Input

- `t`: n-bit signed integer (takum representation)
- `n`: bit width (8, 16, 32, or 64)

### Output

- Floating-point value (or NaN for NaR, 0 for zero)

### Pseudocode

```
DECODE_LOG_TAKUM(t, n):
    # Handle special cases
    if t == INT_MIN(n):
        return NaN  # NaR
    if t == 0:
        return 0.0
    
    # Extract sign and get absolute value
    sign = (t < 0)
    abs_t = sign ? (-t) : t
    
    # Extract bit fields
    shift_D = n - 2
    shift_R = n - 5
    
    D = (abs_t >> shift_D) & 1
    R = (abs_t >> shift_R) & 7
    
    # Calculate r (additional characteristic bits) and p (mantissa bits)
    r = R
    p = n - 5 - r
    
    # Get characteristic bias from lookup table
    DR_index = (D << 3) | R
    c_bias = C_BIAS_LUT[DR_index]
    
    # Extract additional characteristic bits
    c_extra_mask = (1 << r) - 1
    c_extra_shift = p
    c_extra = (abs_t >> c_extra_shift) & c_extra_mask
    
    # Compute full characteristic
    c = c_bias + c_extra
    
    # Extract mantissa bits
    m_mask = (1 << p) - 1
    m_bits = abs_t & m_mask
    
    # Convert mantissa to fraction
    m = m_bits / (1 << p)  # m ∈ [0, 1)
    
    # Compute logarithmic value
    l = c + m
    
    # Apply sign to l
    if sign:
        l = -l
    
    # Convert to actual value: √e^l = e^(l/2)
    value = exp(l / 2.0)
    
    # Apply sign to value
    return sign ? (-value) : value
```

### Lookup Table

```c
const int16_t C_BIAS_LUT[16] = {
    -255, -127, -63, -31, -15, -7, -3, -1,  // D=0, R=0..7
    0, 1, 3, 7, 15, 31, 63, 127             // D=1, R=0..7
};
```

## Algorithm 2: Encode Float to Logarithmic Takum

Converts a floating-point value to an n-bit logarithmic takum.

### Input

- `f`: floating-point value
- `n`: target bit width (8, 16, 32, or 64)

### Output

- n-bit signed integer (takum representation)

### Pseudocode

```
ENCODE_TO_LOG_TAKUM(f, n):
    # Handle special cases
    if isnan(f):
        return INT_MIN(n)  # NaR
    if f == 0.0:
        return 0
    
    # Extract sign and compute absolute value
    sign = (f < 0)
    abs_f = fabs(f)
    
    # Compute logarithmic value: l = 2 × ln(|f|)
    l = 2.0 * log(abs_f)
    
    # Clamp to representable range
    l_max = 254.0 + (1.0 - ldexp(1.0, 12-n))
    l_min = -255.0
    l = clamp(l, l_min, l_max)
    
    # Separate characteristic and mantissa
    c = (int)floor(fabs(l))
    m = fabs(l) - c
    
    # Determine Direction D
    if c < 0 || (c == 0 && l < 0):
        D = 0
    else:
        D = 1
    
    # Find regime R using binary search or linear scan
    R = FIND_REGIME(D, c)
    
    # Calculate precision
    r = R
    p = n - 5 - r
    
    # Get characteristic bias
    DR_index = (D << 3) | R
    c_bias = C_BIAS_LUT[DR_index]
    
    # Compute extra characteristic bits
    c_extra = c - c_bias
    
    # Round mantissa to p bits
    m_scaled = m * (1 << p)
    m_bits = round_to_nearest_even(m_scaled)
    
    # Handle mantissa overflow (carry)
    if m_bits >= (1 << p):
        m_bits = 0
        c_extra += 1
        
        # Check if we need to change regime
        if c_extra >= (1 << r):
            R += 1
            if R > 7:
                # Saturate at maximum
                return sign ? (INT_MIN(n) + 1) : INT_MAX(n)
            r = R
            p = n - 5 - r
            c_bias = C_BIAS_LUT[(D << 3) | R]
            c_extra = c + 1 - c_bias
            m_bits = 0
    
    # Assemble bit pattern
    abs_result = 0
    abs_result |= (D << (n - 2))
    abs_result |= (R << (n - 5))
    abs_result |= (c_extra << p)
    abs_result |= m_bits
    
    # Apply two's complement for sign
    return sign ? (-abs_result) : abs_result
```

### Regime Finding Subroutine

```
FIND_REGIME(D, c):
    for R = 0 to 7:
        c_bias = C_BIAS_LUT[(D << 3) | R]
        c_max = c_bias + (1 << R) - 1
        if c >= c_bias and c <= c_max:
            return R
    return 7  # Maximum regime
```

## Algorithm 3: Logarithmic Takum Multiplication

Exploits the logarithmic domain for O(1) multiplication.

### Pseudocode

```
LOG_TAKUM_MULTIPLY(a, b, n):
    # Handle special cases
    if a == NaR or b == NaR:
        return NaR
    if a == 0 or b == 0:
        return 0
    
    # Determine result sign
    sign_a = (a < 0)
    sign_b = (b < 0)
    result_sign = sign_a XOR sign_b
    
    # Decode logarithmic values
    l_a = DECODE_TO_L(a, n)
    l_b = DECODE_TO_L(b, n)
    
    # In log domain: multiplication = addition
    l_result = l_a + l_b
    
    # Encode back
    return ENCODE_FROM_S_AND_L(result_sign, l_result, n)
```

### Optimized Implementation

For maximum performance, avoid full decode/encode:

```
LOG_TAKUM_MULTIPLY_FAST(a, b, n):
    # XOR for sign (but need careful handling of NaR/zero)
    # Direct l-value computation from bit patterns
    # Single encode pass at end
```

## Algorithm 4: Logarithmic Takum Division

Exploits the logarithmic domain for O(1) division.

### Pseudocode

```
LOG_TAKUM_DIVIDE(a, b, n):
    # Handle special cases
    if a == NaR or b == NaR or b == 0:
        return NaR
    if a == 0:
        return 0
    
    # Determine result sign
    result_sign = (a < 0) XOR (b < 0)
    
    # In log domain: division = subtraction
    l_a = DECODE_TO_L(a, n)
    l_b = DECODE_TO_L(b, n)
    l_result = l_a - l_b
    
    return ENCODE_FROM_S_AND_L(result_sign, l_result, n)
```

## Algorithm 5: Logarithmic Takum Inversion

O(1) bit manipulation for exact inversion.

### Pseudocode

```
LOG_TAKUM_INVERT(t, n):
    if t == NaR or t == 0:
        return NaR
    
    # XOR all bits except sign, then add 1
    # This negates the l-value: l → -l
    # Since value = √e^l, 1/value = √e^(-l)
    
    mask = (1 << (n-1)) - 1  # All bits except sign
    
    # Get sign
    sign = (t < 0)
    abs_t = sign ? (-t) : t
    
    # Invert absolute value's l-representation
    # This is: flip all bits of abs_t, add 1
    inverted_abs = (~abs_t & mask) + 1
    
    # Handle edge case: if abs_t was minimum positive, 
    # inverted might overflow
    if inverted_abs > mask:
        inverted_abs = mask  # Saturate
    
    # Apply sign
    return sign ? (-inverted_abs) : inverted_abs
```

### Simplified Implementation (C)

```c
takum_log16 takum_log16_inversion(takum_log16 t) {
    if (t == TAKUM_LOG16_NAR || t == 0) {
        return TAKUM_LOG16_NAR;
    }
    
    union { int16_t val; uint16_t bits; } u;
    u.val = t;
    
    // XOR non-sign bits, add 1
    u.bits = (u.bits ^ 0x7FFF) + 1;
    
    return u.val;
}
```

## Algorithm 6: Integer Power (Logarithmic)

Efficient O(1) power computation for integer exponents.

### Pseudocode

```
LOG_TAKUM_INTEGER_POWER(t, n_exp, n):
    # Handle special cases
    if t == NaR:
        return NaR
    if t == 0:
        if n_exp == 0:
            return NaR  # 0^0 is undefined
        if n_exp > 0:
            return 0    # 0^positive = 0
        return NaR      # 0^negative = undefined
    if n_exp == 0:
        return ONE(n)   # x^0 = 1
    if n_exp == 1:
        return t
    
    # Compute sign of result
    result_sign = (t < 0) AND (n_exp is odd)
    
    # In log domain: power = multiplication
    l_t = DECODE_TO_L(t, n)
    l_result = l_t * n_exp
    
    # Check for overflow/underflow
    if l_result > L_MAX(n):
        return result_sign ? MIN_NEGATIVE(n) : MAX_POSITIVE(n)
    if l_result < L_MIN(n):
        return 0  # Underflow to zero
    
    return ENCODE_FROM_S_AND_L(result_sign, l_result, n)
```

## Algorithm 7: Square Root (Logarithmic)

O(1) square root via halving the logarithmic value.

### Pseudocode

```
LOG_TAKUM_SQRT(t, n):
    if t == NaR:
        return NaR
    if t < 0:
        return NaR  # Square root of negative
    if t == 0:
        return 0
    
    # In log domain: sqrt = divide by 2
    l_t = DECODE_TO_L(t, n)
    l_result = l_t / 2.0  # or ldexp(l_t, -1)
    
    return ENCODE_FROM_S_AND_L(false, l_result, n)
```

## Algorithm 8: Addition (via Gaussian Logarithm)

Addition requires more complex handling in logarithmic domain.

### Pseudocode

```
LOG_TAKUM_ADD(a, b, n):
    if a == NaR or b == NaR:
        return NaR
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Convert to float, add, convert back
    # (Simple but not optimal)
    f_a = LOG_TAKUM_TO_FLOAT(a, n)
    f_b = LOG_TAKUM_TO_FLOAT(b, n)
    f_result = f_a + f_b
    
    return FLOAT_TO_LOG_TAKUM(f_result, n)
```

### Optimized Version (Gaussian Logarithm)

```
LOG_TAKUM_ADD_GAUSSIAN(a, b, n):
    if a == NaR or b == NaR:
        return NaR
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Handle signs
    if SIGN(a) != SIGN(b):
        return LOG_TAKUM_SUBTRACT_SAME_SIGN(a, NEGATE(b), n)
    
    # Both same sign: use Gaussian addition logarithm
    l_a = DECODE_TO_L(a, n)
    l_b = DECODE_TO_L(b, n)
    
    # Ensure l_a >= l_b
    if abs(l_a) < abs(l_b):
        swap(l_a, l_b)
    
    # Compute: result = √e^l_a + √e^l_b = √e^l_a × (1 + √e^(l_b - l_a))
    # In log domain: l_result = l_a + Φ_√e^+(l_b - l_a)
    q = l_b - l_a
    phi_plus = 2 * log1p(exp(q / 2))  # Φ_√e^+(q) = 2·Φ_e^+(q/2)
    l_result = l_a + phi_plus
    
    return ENCODE_FROM_S_AND_L(SIGN(a), l_result, n)
```

## Algorithm 9: Subtraction (via Gaussian Logarithm)

### Pseudocode

```
LOG_TAKUM_SUBTRACT(a, b, n):
    return LOG_TAKUM_ADD(a, NEGATE(b), n)
```

### Optimized (Same Sign Case)

```
LOG_TAKUM_SUBTRACT_SAME_SIGN(a, b, n):
    # Assumes a and b have same sign, computing a - b where |a| > |b|
    
    l_a = DECODE_TO_L(a, n)
    l_b = DECODE_TO_L(b, n)
    
    if abs(l_a) < abs(l_b):
        # Result flips sign
        swap(l_a, l_b)
        result_sign = !SIGN(a)
    else:
        result_sign = SIGN(a)
    
    # Compute: √e^l_a - √e^l_b = √e^l_a × (1 - √e^(l_b - l_a))
    q = l_b - l_a  # q < 0 since |l_a| > |l_b|
    phi_minus = 2 * log1p(-exp(q / 2))  # Φ_√e^-(q)
    l_result = l_a + phi_minus
    
    return ENCODE_FROM_S_AND_L(result_sign, l_result, n)
```

## Algorithm 10: Round to Nearest Even

Standard banker's rounding for mantissa truncation.

### Pseudocode

```
ROUND_TO_NEAREST_EVEN(value, num_bits):
    # value is the full-precision scaled mantissa
    # num_bits is the target precision
    
    shift = full_bits - num_bits
    
    # Extract the part to keep
    truncated = value >> shift
    
    # Extract rounding bit (first bit after truncation point)
    round_bit = (value >> (shift - 1)) & 1
    
    # Check if exactly at midpoint (all remaining bits are 0)
    remaining_mask = (1 << (shift - 1)) - 1
    at_midpoint = (value & remaining_mask) == 0
    
    # Round up if:
    # - round_bit is 1 AND
    # - (not at midpoint OR truncated is odd)
    if round_bit AND (!at_midpoint OR (truncated & 1)):
        truncated += 1
    
    return truncated
```

## Algorithm 11: Type Conversion (Expansion)

Converting smaller takum to larger (no precision loss).

### Pseudocode

```
EXPAND_TAKUM(t_small, n_small, n_large):
    # Simply left-shift to fill larger type
    shift = n_large - n_small
    return (extended_type)t_small << shift
```

### Example (takum_log16 to takum_log32)

```c
takum_log32 takum_log32_from_takum_log16(takum_log16 t) {
    return ((int32_t)t) << 16;
}
```

## Algorithm 12: Type Conversion (Reduction)

Converting larger takum to smaller (precision loss possible).

### Pseudocode

```
REDUCE_TAKUM(t_large, n_large, n_small):
    # Round then truncate
    shift = n_large - n_small
    
    # Round using bits that will be discarded
    rounded = ROUND_TO_NEAREST_EVEN(t_large, n_small)
    
    # Handle saturation (avoid creating NaR from valid value)
    if rounded == INT_MIN(n_small) AND t_large != INT_MIN(n_large):
        rounded = INT_MIN(n_small) + 1  # Minimum negative
    if rounded > INT_MAX(n_small):
        rounded = INT_MAX(n_small)  # Maximum positive
    if rounded < INT_MIN(n_small) + 1:
        rounded = INT_MIN(n_small) + 1  # Minimum negative
    
    return (small_type)rounded
```

## Helper Functions

### Decode to L-Value

```
DECODE_TO_L(t, n):
    # Extract l without final exp() conversion
    # (Returns the logarithmic value directly)
    
    if t == NaR(n):
        return NaN
    if t == 0:
        return -INFINITY
    
    sign = (t < 0)
    abs_t = sign ? (-t) : t
    
    D = (abs_t >> (n-2)) & 1
    R = (abs_t >> (n-5)) & 7
    r = R
    p = n - 5 - r
    
    DR = (D << 3) | R
    c = C_BIAS_LUT[DR] + ((abs_t >> p) & ((1 << r) - 1))
    m = (abs_t & ((1 << p) - 1)) / (1.0 * (1 << p))
    
    l = c + m
    return sign ? (-l) : l
```

### Encode from Sign and L-Value

```
ENCODE_FROM_S_AND_L(sign, l, n):
    if isnan(l):
        return NaR(n)
    if isinf(l) AND l < 0:
        return 0  # log(0) = -∞ → 0
    
    # Clamp l to range
    l_max = 254 + (1 - ldexp(1, 12-n))
    l_clamped = clamp(abs(l), 0, l_max)
    
    # Encode (see Algorithm 2)
    return ENCODE_TO_LOG_TAKUM_FROM_L(sign, l_clamped, n)
```

## Complexity Summary

| Operation | Logarithmic Takum | Linear Takum |
|-----------|------------------|--------------|
| Negation | O(1) | O(1) |
| Comparison | O(1) | O(1) |
| Multiplication | O(1) | O(decode + encode) |
| Division | O(1) | O(decode + encode) |
| Inversion | O(1) | O(decode + encode) |
| Integer Power | O(1) | O(decode + encode) |
| Square Root | O(1) | O(decode + encode) |
| Addition | O(Gaussian log) | O(1) |
| Subtraction | O(Gaussian log) | O(1) |
| Transcendentals | O(float comp) | O(float comp) |
