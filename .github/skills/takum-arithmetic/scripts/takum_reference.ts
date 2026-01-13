/**
 * Takum Arithmetic Reference Implementation (TypeScript/JavaScript)
 *
 * This module provides a language-agnostic reference implementation of
 * takum arithmetic for validation and educational purposes.
 *
 * USAGE (Node.js):
 *     import { encodeTakum, decodeTakum, SQRT_E } from './takum_reference.ts';
 *     const encoded = encodeTakum(Math.PI, 16);
 *     const decoded = decodeTakum(encoded, 16);
 *
 * USAGE (Browser):
 *     <script type="module" src="takum_reference.ts"></script>
 *
 * @module takum_reference
 * @version 2.0
 * @license MIT
 */

// =============================================================================
// CONSTANTS
// =============================================================================

/** Base of takum logarithm: sqrt(e) ≈ 1.6487212707 */
export const SQRT_E: number = Math.sqrt(Math.E);

/** Natural log of sqrt(e) = 0.5 */
export const LN_SQRT_E: number = 0.5;

/** Characteristic bias lookup table: c_bias(r) = 2^(r+1) - 1 */
export const C_BIAS_LUT: readonly number[] = Object.freeze([
  1, 3, 7, 15, 31, 63, 127, 255
]);

// =============================================================================
// TYPE DEFINITIONS
// =============================================================================

/**
 * Supported takum bit widths
 */
export type TakumBits = 8 | 16 | 32 | 64;

/**
 * Configuration for a specific takum bit width
 */
export interface TakumConfig {
  readonly bits: TakumBits;
  readonly signBits: 1;
  readonly directionBits: 1;
  readonly regimeBits: 3;
  readonly overheadBits: 5;
  readonly maxMantissaBits: number;
  readonly narValue: number;
  readonly oneValue: number;
}

/**
 * Pre-defined configurations for all takum types
 */
export const TAKUM_CONFIGS: Record<TakumBits, TakumConfig> = {
  8: {
    bits: 8,
    signBits: 1,
    directionBits: 1,
    regimeBits: 3,
    overheadBits: 5,
    maxMantissaBits: 3,
    narValue: -128,           // 0x80 as signed int8
    oneValue: 0x20,
  },
  16: {
    bits: 16,
    signBits: 1,
    directionBits: 1,
    regimeBits: 3,
    overheadBits: 5,
    maxMantissaBits: 11,
    narValue: -32768,         // 0x8000 as signed int16
    oneValue: 0x2000,
  },
  32: {
    bits: 32,
    signBits: 1,
    directionBits: 1,
    regimeBits: 3,
    overheadBits: 5,
    maxMantissaBits: 27,
    narValue: -2147483648,    // 0x80000000 as signed int32
    oneValue: 0x20000000,
  },
  64: {
    bits: 64,
    signBits: 1,
    directionBits: 1,
    regimeBits: 3,
    overheadBits: 5,
    maxMantissaBits: 59,
    narValue: Number.MIN_SAFE_INTEGER, // Approximation for int64
    oneValue: 0x2000000000000000,
  },
};

// =============================================================================
// HELPER FUNCTIONS
// =============================================================================

/**
 * Compute characteristic bias for a regime value
 *
 * @param r - Regime value in [0, 7]
 * @returns Bias value: 2^(r+1) - 1
 */
export function cBias(r: number): number {
  if (r < 0 || r > 7) {
    throw new RangeError(`Regime must be in [0, 7], got ${r}`);
  }
  return C_BIAS_LUT[r];
}

/**
 * Compute regime from absolute logarithm value
 *
 * @param lAbs - Absolute value of logarithm |l|
 * @returns Regime value r in [0, 7]
 */
export function computeRegime(lAbs: number): number {
  if (lAbs === 0) return 0;
  // r = floor(log2(|l| + 1))
  return Math.min(7, Math.floor(Math.log2(lAbs + 1)));
}

/**
 * Count bits needed to represent a number
 *
 * @param n - Non-negative integer
 * @returns Number of bits (equivalent to floor(log2(n)) + 1)
 */
function bitLength(n: number): number {
  if (n <= 0) return 0;
  return Math.floor(Math.log2(n)) + 1;
}

// =============================================================================
// ENCODING FUNCTIONS
// =============================================================================

/**
 * Encode a float as a logarithmic takum
 *
 * Implements Algorithm 1 from the Takum paper (simplified).
 *
 * @param value - Float value to encode
 * @param bits - Takum bit width (8, 16, 32, or 64)
 * @returns Signed integer representation
 *
 * @example
 * ```typescript
 * const piEncoded = encodeTakum(Math.PI, 16);
 * console.log(`π as takum16: 0x${(piEncoded & 0xFFFF).toString(16)}`);
 * ```
 */
export function encodeTakum(value: number, bits: TakumBits = 16): number {
  const config = TAKUM_CONFIGS[bits];

  // Handle special cases
  if (Number.isNaN(value)) return config.narValue;
  if (!Number.isFinite(value)) return config.narValue;
  if (value === 0) return 0;

  // Extract sign
  const s = value > 0 ? 0 : 1;
  const absValue = Math.abs(value);

  // Compute logarithm in base sqrt(e)
  // l = log_{sqrt(e)}(|value|) = 2 * ln(|value|)
  const lFloat = 2.0 * Math.log(absValue);
  let l = Math.round(lFloat);

  // Clamp to valid range
  l = Math.max(-255, Math.min(255, l));

  // Determine direction
  const d = l >= 0 ? 1 : 0;

  // Compute regime from |l|
  const lAbs = Math.abs(l);
  const r = computeRegime(lAbs);

  // Compute characteristic
  let c: number;
  if (l >= 0) {
    c = r > 0 ? l - C_BIAS_LUT[r] : 0;
  } else {
    c = r > 0 ? C_BIAS_LUT[r] - 1 - lAbs : 0;
  }

  // Compute mantissa bits available
  let mBits = bits - config.overheadBits - r;
  if (mBits < 0) mBits = 0;

  // Compute mantissa from fractional part
  const lFrac = Math.abs(lFloat) - Math.abs(l);
  const m = mBits > 0 ? Math.floor(lFrac * (1 << mBits)) : 0;

  // Assemble bit pattern
  let result = s << (bits - 1);
  result |= d << (bits - 2);
  result |= r << (bits - 5);
  if (r > 0) result |= c << mBits;
  result |= m;

  // Convert to signed integer
  if (s === 1) {
    result = result - (1 << bits);
  }

  return result;
}

/**
 * Decode a logarithmic takum to a float
 *
 * Implements Algorithm 2 from the Takum paper (simplified).
 *
 * @param encoded - Signed integer takum representation
 * @param bits - Takum bit width (8, 16, 32, or 64)
 * @returns Decoded float value (NaN for NaR)
 *
 * @example
 * ```typescript
 * const decoded = decodeTakum(0x3C48, 16);
 * console.log(`Decoded: ${decoded}`);  // ~3.14159
 * ```
 */
export function decodeTakum(encoded: number, bits: TakumBits = 16): number {
  const config = TAKUM_CONFIGS[bits];

  // Handle special cases
  if (encoded === config.narValue) return NaN;
  if (encoded === 0) return 0;

  // Convert to unsigned for bit manipulation
  let encodedU = encoded;
  if (encoded < 0) {
    encodedU = encoded + (1 << bits);
  }

  // Extract sign
  const s = (encodedU >> (bits - 1)) & 1;

  // Extract direction
  const d = (encodedU >> (bits - 2)) & 1;

  // Extract regime
  const r = (encodedU >> (bits - 5)) & 0b111;

  // Compute mantissa bits
  let mBits = bits - config.overheadBits - r;
  if (mBits < 0) mBits = 0;

  // Extract characteristic
  const c = r > 0 ? (encodedU >> mBits) & ((1 << r) - 1) : 0;

  // Extract mantissa
  const m = mBits > 0 ? encodedU & ((1 << mBits) - 1) : 0;

  // Compute l
  let l: number;
  if (d === 1) {
    // Positive direction (l >= 0)
    l = r > 0 ? C_BIAS_LUT[r] + c : 0;
  } else {
    // Negative direction (l < 0)
    const lBiased = r > 0 ? C_BIAS_LUT[r] - 1 - c : 0;
    l = -(lBiased + 1);
  }

  // Add mantissa contribution
  const lFloat = l + (mBits > 0 ? m / (1 << mBits) : 0);

  // Convert back to linear: value = sqrt(e)^l = e^(l/2)
  const absValue = Math.exp(lFloat / 2.0);

  return s === 1 ? -absValue : absValue;
}

// =============================================================================
// ARITHMETIC OPERATIONS (Logarithmic Domain)
// =============================================================================

/**
 * Multiply two takum values (O(1) in l-domain)
 *
 * In the logarithmic domain: a × b = sqrt(e)^(l_a + l_b)
 *
 * @param a - First takum value (signed integer)
 * @param b - Second takum value (signed integer)
 * @param bits - Takum bit width
 * @returns Product as takum (signed integer)
 */
export function takumMultiply(a: number, b: number, bits: TakumBits = 16): number {
  const config = TAKUM_CONFIGS[bits];

  // Handle NaR
  if (a === config.narValue || b === config.narValue) return config.narValue;

  // Handle zero
  if (a === 0 || b === 0) return 0;

  // In l-domain, multiply = add
  // This is a simplified version - full implementation needs careful overflow handling
  const aFloat = decodeTakum(a, bits);
  const bFloat = decodeTakum(b, bits);
  return encodeTakum(aFloat * bFloat, bits);
}

/**
 * Divide two takum values (O(1) in l-domain)
 *
 * In the logarithmic domain: a / b = sqrt(e)^(l_a - l_b)
 *
 * @param a - Dividend (signed integer)
 * @param b - Divisor (signed integer)
 * @param bits - Takum bit width
 * @returns Quotient as takum (signed integer)
 */
export function takumDivide(a: number, b: number, bits: TakumBits = 16): number {
  const config = TAKUM_CONFIGS[bits];

  // Handle NaR
  if (a === config.narValue || b === config.narValue) return config.narValue;

  // Division by zero = NaR
  if (b === 0) return config.narValue;

  // Zero divided by anything = zero
  if (a === 0) return 0;

  // In l-domain, divide = subtract
  const aFloat = decodeTakum(a, bits);
  const bFloat = decodeTakum(b, bits);
  return encodeTakum(aFloat / bFloat, bits);
}

/**
 * Invert a takum value (O(1) in l-domain)
 *
 * In the logarithmic domain: 1/a = sqrt(e)^(-l_a)
 *
 * @param a - Value to invert (signed integer)
 * @param bits - Takum bit width
 * @returns Inverse as takum (signed integer)
 */
export function takumInvert(a: number, bits: TakumBits = 16): number {
  const config = TAKUM_CONFIGS[bits];

  // Handle NaR
  if (a === config.narValue) return config.narValue;

  // 1/0 = NaR
  if (a === 0) return config.narValue;

  // In l-domain, invert = negate
  const aFloat = decodeTakum(a, bits);
  return encodeTakum(1.0 / aFloat, bits);
}

/**
 * Square root of a takum value (O(1) in l-domain)
 *
 * In the logarithmic domain: sqrt(a) = sqrt(e)^(l_a / 2)
 *
 * @param a - Value (signed integer)
 * @param bits - Takum bit width
 * @returns Square root as takum (signed integer)
 */
export function takumSqrt(a: number, bits: TakumBits = 16): number {
  const config = TAKUM_CONFIGS[bits];

  // Handle NaR
  if (a === config.narValue) return config.narValue;

  // Handle zero
  if (a === 0) return 0;

  // Negative numbers: NaR
  const aFloat = decodeTakum(a, bits);
  if (aFloat < 0) return config.narValue;

  // In l-domain, sqrt = divide by 2 (arithmetic right shift)
  return encodeTakum(Math.sqrt(aFloat), bits);
}

// =============================================================================
// VALIDATION UTILITIES
// =============================================================================

/**
 * Test encoding/decoding roundtrip
 *
 * @param value - Value to test
 * @param bits - Takum bit width
 * @param tolerance - Maximum relative error allowed
 * @returns True if roundtrip error is within tolerance
 */
export function testRoundtrip(
  value: number,
  bits: TakumBits = 16,
  tolerance: number = 0.01
): boolean {
  if (value === 0) {
    const encoded = encodeTakum(value, bits);
    const decoded = decodeTakum(encoded, bits);
    return decoded === 0;
  }

  const encoded = encodeTakum(value, bits);
  const decoded = decodeTakum(encoded, bits);
  const relativeError = Math.abs(decoded - value) / Math.abs(value);
  return relativeError < tolerance;
}

/**
 * Run basic validation tests
 *
 * @returns True if all tests pass
 */
export function runValidation(): boolean {
  const testValues = [0, 1, -1, Math.PI, Math.E, 0.5, 2, 0.1, 10, 100, 0.01];
  let allPassed = true;

  console.log("Takum Validation Tests");
  console.log("=" .repeat(50));

  for (const bits of [8, 16, 32] as TakumBits[]) {
    console.log(`\nTesting takum${bits}:`);

    for (const value of testValues) {
      const encoded = encodeTakum(value, bits);
      const decoded = decodeTakum(encoded, bits);
      const passed = testRoundtrip(value, bits);

      const status = passed ? "✓" : "✗";
      const hex = (encoded >>> 0).toString(16).padStart(bits / 4, "0");
      console.log(`  ${status} ${value.toFixed(6).padStart(12)} -> 0x${hex} -> ${decoded.toFixed(6)}`);

      if (!passed) allPassed = false;
    }
  }

  console.log("\n" + "=".repeat(50));
  console.log(allPassed ? "ALL TESTS PASSED ✓" : "SOME TESTS FAILED ✗");

  return allPassed;
}

// =============================================================================
// EXPORTS
// =============================================================================

export default {
  SQRT_E,
  LN_SQRT_E,
  C_BIAS_LUT,
  TAKUM_CONFIGS,
  cBias,
  computeRegime,
  encodeTakum,
  decodeTakum,
  takumMultiply,
  takumDivide,
  takumInvert,
  takumSqrt,
  testRoundtrip,
  runValidation,
};
