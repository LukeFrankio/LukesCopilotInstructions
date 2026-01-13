# Takum Type Conversion Guide

This document provides comprehensive patterns for converting between Takum types and other numeric formats.

## Conversion Overview

```
                    ┌─────────────────┐
                    │  float32/64/ld  │
                    └────────┬────────┘
                             │
            ┌────────────────┼────────────────┐
            │                │                │
            ▼                ▼                ▼
    ┌───────────┐    ┌───────────┐    ┌───────────┐
    │ takum8/16 │◄──►│ takum32   │◄──►│ takum64   │
    │ /32/64    │    │           │    │           │
    └─────┬─────┘    └───────────┘    └───────────┘
          │
          │ linear ↔ log
          ▼
    ┌───────────┐
    │takum_log* │
    └───────────┘
```

## Float to Takum Conversion

### Algorithm Overview

```
1. Handle special cases (NaN, ±Inf, 0)
2. Extract sign
3. Compute logarithmic value: l = 2 × ln(|f|)
4. Encode l as takum
```

### Detailed Implementation (Float64 → takum_log16)

```c
takum_log16 takum_log16_from_float64(double f) {
    // Step 1: Special cases
    if (isnan(f)) {
        return TAKUM_LOG16_NAR;
    }
    if (f == 0.0) {
        return 0;
    }
    if (isinf(f)) {
        return (f > 0) ? INT16_MAX : (INT16_MIN + 1);
    }
    
    // Step 2: Extract sign
    bool sign = (f < 0);
    double abs_f = fabs(f);
    
    // Step 3: Compute logarithmic value
    // l = 2 × ln(|f|) = ln(|f|²)
    double l = 2.0 * log(abs_f);
    
    // Step 4: Encode to takum
    return encode_takum_log16_from_l(sign, l);
}
```

### Float32 Conversion

```c
takum_log16 takum_log16_from_float32(float f) {
    // Promote to double for precision
    return takum_log16_from_float64((double)f);
}
```

### Extended Float Conversion

```c
takum_log16 takum_log16_from_extended_float(long double f) {
    if (isnanl(f)) {
        return TAKUM_LOG16_NAR;
    }
    if (f == 0.0L) {
        return 0;
    }
    
    bool sign = (f < 0);
    long double l = 2.0L * logl(fabsl(f));
    
    return encode_takum_log16_from_l(sign, (double)l);
}
```

## Takum to Float Conversion

### Algorithm Overview

```
1. Handle special cases (NaR, 0)
2. Decode to logarithmic value l
3. Compute: value = √e^l = e^(l/2)
4. Apply sign
```

### Detailed Implementation (takum_log16 → Float64)

```c
double takum_log16_to_float64(takum_log16 t) {
    // Step 1: Special cases
    if (t == TAKUM_LOG16_NAR) {
        return NAN;
    }
    if (t == 0) {
        return 0.0;
    }
    
    // Step 2: Decode to l
    double l = decode_takum_log16_to_l(t);
    
    // Step 3: Compute value
    // √e^l = e^(l/2)
    double value = exp(l / 2.0);
    
    // Step 4: Apply sign
    return (t < 0) ? -value : value;
}
```

### To Float32 (with precision consideration)

```c
float takum_log16_to_float32(takum_log16 t) {
    // Convert via double then narrow
    double d = takum_log16_to_float64(t);
    return (float)d;
}
```

## Between Takum Widths

### Expansion (Lossless)

Converting from smaller to larger bit width preserves all information.

```c
// takum_log16 → takum_log32
takum_log32 takum_log32_from_takum_log16(takum_log16 t) {
    // Simply left-shift to fill larger type
    return ((int32_t)t) << 16;
}

// takum_log8 → takum_log64
takum_log64 takum_log64_from_takum_log8(takum_log8 t) {
    return ((int64_t)t) << 56;
}
```

### Reduction (May Lose Precision)

Converting from larger to smaller requires rounding.

```c
// takum_log32 → takum_log16
takum_log16 takum_log16_from_takum_log32(takum_log32 t) {
    if (t == TAKUM_LOG32_NAR) {
        return TAKUM_LOG16_NAR;
    }
    
    // Round using bits that will be discarded
    uint32_t abs_t = (t < 0) ? -t : t;
    
    // Round to nearest even
    uint32_t round_bit = (abs_t >> 15) & 1;
    uint32_t sticky_bits = abs_t & 0x7FFF;
    uint16_t truncated = (uint16_t)(abs_t >> 16);
    
    // Apply rounding
    if (round_bit && (sticky_bits || (truncated & 1))) {
        truncated++;
    }
    
    // Handle saturation (don't create NaR from valid value)
    if (truncated == 0x8000 && t != TAKUM_LOG32_NAR) {
        truncated = 0x7FFF;  // Saturate to max positive
    }
    
    return (t < 0) ? -truncated : truncated;
}
```

## Linear ↔ Logarithmic Conversion

### Logarithmic to Linear (Same Width)

```c
takum16 takum16_from_takum_log16(takum_log16 t) {
    if (t == TAKUM_LOG16_NAR) {
        return TAKUM16_NAR;
    }
    if (t == 0) {
        return 0;
    }
    
    // Convert via float
    double f = takum_log16_to_float64(t);
    return takum16_from_float64(f);
}
```

### Linear to Logarithmic (Same Width)

```c
takum_log16 takum_log16_from_takum16(takum16 t) {
    if (t == TAKUM16_NAR) {
        return TAKUM_LOG16_NAR;
    }
    if (t == 0) {
        return 0;
    }
    
    // Convert via float
    double f = takum16_to_float64(t);
    return takum_log16_from_float64(f);
}
```

## Special Value Handling

### NaR Propagation

```c
// Input NaN or invalid → Output NaR
if (isnan(input)) return TAKUM_NAR;

// Input infinity → Saturate
if (isinf(input)) {
    return (input > 0) ? MAX_POSITIVE : MIN_NEGATIVE;
}
```

### Zero Handling

```c
// Exact zero conversion
if (input == 0.0) return 0;

// Underflow to zero
if (fabs(input) < MIN_POSITIVE_FLOAT) {
    return 0;  // Or MIN_POSITIVE_TAKUM for some implementations
}
```

### Overflow Handling

```c
// Saturate at maximum representable
if (fabs(input) > MAX_REPRESENTABLE) {
    return (input > 0) ? MAX_POSITIVE_TAKUM : MIN_NEGATIVE_TAKUM;
}
```

## Cross-Type Conversion Matrix

### Expansion Paths (Lossless)

| From | To | Method |
|------|-----|--------|
| takum_log8 | takum_log16 | `<< 8` |
| takum_log8 | takum_log32 | `<< 24` |
| takum_log8 | takum_log64 | `<< 56` |
| takum_log16 | takum_log32 | `<< 16` |
| takum_log16 | takum_log64 | `<< 48` |
| takum_log32 | takum_log64 | `<< 32` |

### Reduction Paths (Round + Saturate)

| From | To | Method |
|------|-----|--------|
| takum_log64 | takum_log32 | Round `>> 32` |
| takum_log64 | takum_log16 | Round `>> 48` |
| takum_log64 | takum_log8 | Round `>> 56` |
| takum_log32 | takum_log16 | Round `>> 16` |
| takum_log32 | takum_log8 | Round `>> 24` |
| takum_log16 | takum_log8 | Round `>> 8` |

## Type Punning Patterns

### Union-Based Safe Punning

```c
union takum_log16_union {
    int16_t value;    // Signed interpretation
    uint16_t bits;    // Unsigned for bit manipulation
};

// Usage
union takum_log16_union u;
u.value = t;
uint16_t raw_bits = u.bits;
```

### Bit Field Extraction

```c
// Extract direction bit
bool D = (abs_t >> 14) & 1;

// Extract regime
uint8_t R = (abs_t >> 11) & 7;

// Extract characteristic extra bits
uint16_t c_extra = (abs_t >> p) & ((1 << r) - 1);

// Extract mantissa
uint16_t m_bits = abs_t & ((1 << p) - 1);
```

## Platform Considerations

### Endianness

Takum encoding is endian-neutral at the logical level. However, when serializing:

```c
// Big-endian serialization
void serialize_takum_log16_be(takum_log16 t, uint8_t* buf) {
    buf[0] = (t >> 8) & 0xFF;
    buf[1] = t & 0xFF;
}

// Little-endian serialization
void serialize_takum_log16_le(takum_log16 t, uint8_t* buf) {
    buf[0] = t & 0xFF;
    buf[1] = (t >> 8) & 0xFF;
}
```

### Floating-Point Precision

For maximum accuracy in conversions:

```c
// Use long double for intermediate calculations when available
long double l = 2.0L * logl(fabsl((long double)f));

// Fall back to double where long double is not distinct
double l = 2.0 * log(fabs(f));
```

## Conversion Function Template (Generic)

### C Macro Pattern

```c
#define TAKUM_LOG_FROM_FLOAT(TYPE, BITS, NAR) \
TYPE TYPE##_from_float64(double f) { \
    if (isnan(f)) return NAR; \
    if (f == 0.0) return 0; \
    bool sign = (f < 0); \
    double l = 2.0 * log(fabs(f)); \
    return encode_##TYPE##_from_l(sign, l); \
}

// Usage
TAKUM_LOG_FROM_FLOAT(takum_log8, 8, TAKUM_LOG8_NAR)
TAKUM_LOG_FROM_FLOAT(takum_log16, 16, TAKUM_LOG16_NAR)
TAKUM_LOG_FROM_FLOAT(takum_log32, 32, TAKUM_LOG32_NAR)
TAKUM_LOG_FROM_FLOAT(takum_log64, 64, TAKUM_LOG64_NAR)
```

## Common Conversion Errors

### Error 1: Forgetting NaR Check

```c
// WRONG
double takum_to_float(takum_log16 t) {
    return exp(decode_l(t) / 2.0);  // Crashes on NaR!
}

// CORRECT
double takum_to_float(takum_log16 t) {
    if (t == TAKUM_LOG16_NAR) return NAN;
    return exp(decode_l(t) / 2.0);
}
```

### Error 2: Creating NaR from Reduction

```c
// WRONG - reduction might accidentally create NaR
takum_log8 result = (int8_t)(t32 >> 24);

// CORRECT - saturate instead of creating NaR
int8_t result = (int8_t)(t32 >> 24);
if (result == INT8_MIN && t32 != TAKUM_LOG32_NAR) {
    result = INT8_MIN + 1;  // Saturate
}
```

### Error 3: Precision Loss in Float Conversion

```c
// WRONG - loses precision for takum64
float f = takum_log64_to_float32(t);
takum_log64 back = takum_log64_from_float32(f);  // Different!

// CORRECT - use matching precision
double f = takum_log64_to_float64(t);
// Still may lose precision for extreme values
```

## Roundtrip Guarantees

### Lossless Roundtrips

- `takum_log8` → `float64` → `takum_log8` (exact)
- `takum_log16` → `float64` → `takum_log16` (exact)
- `takum_log8` → `takum_log32` → `takum_log8` (exact with proper reduction)

### Potentially Lossy Roundtrips

- `takum_log32` → `float32` → `takum_log32` (may lose precision)
- `float64` → `takum_log16` → `float64` (may lose precision)
- Any reduction path (may lose precision)
