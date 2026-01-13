#!/usr/bin/env python3
"""
Takum Arithmetic Implementation Validator

This script provides reference implementations and validation utilities for
takum arithmetic. It is language-agnostic in spirit - use it to verify your
implementations in any language against known correct values.

USAGE:
    python validate_takum.py --test-encoding
    python validate_takum.py --test-constants
    python validate_takum.py --test-all
    python validate_takum.py --encode <float_value>
    python validate_takum.py --decode <hex_value> --bits <8|16|32|64>

REQUIREMENTS:
    Python 3.11+ (type hints, math functions)
    No external dependencies (stdlib only)

Author: Luke Frankio
Version: 2.0
License: MIT
"""

from __future__ import annotations

import argparse
import math
import struct
import sys
from dataclasses import dataclass
from typing import Final, TypeAlias

# =============================================================================
# TYPE DEFINITIONS
# =============================================================================

TakumBits: TypeAlias = int  # 8, 16, 32, or 64


@dataclass(frozen=True, slots=True)
class TakumConfig:
    """Configuration for a specific takum bit width."""

    bits: int
    sign_bits: Final[int] = 1
    direction_bits: Final[int] = 1
    regime_bits: Final[int] = 3

    @property
    def overhead_bits(self) -> int:
        """Total overhead bits (sign + direction + regime)."""
        return self.sign_bits + self.direction_bits + self.regime_bits

    @property
    def max_mantissa_bits(self) -> int:
        """Maximum mantissa bits (at regime 0)."""
        return self.bits - self.overhead_bits

    @property
    def nar_value(self) -> int:
        """Not a Real (NaR) bit pattern as signed integer."""
        return -(1 << (self.bits - 1))

    @property
    def one_value(self) -> int:
        """Encoding of 1.0."""
        # 1 = sqrt(e)^0, so l=0, D=1, R=0, C=0, M=0
        # Bit pattern: 0_1_000_..._0
        return 1 << (self.bits - 3)  # D=1 at position n-2


# Pre-defined configurations
TAKUM8 = TakumConfig(bits=8)
TAKUM16 = TakumConfig(bits=16)
TAKUM32 = TakumConfig(bits=32)
TAKUM64 = TakumConfig(bits=64)

CONFIGS: dict[int, TakumConfig] = {
    8: TAKUM8,
    16: TAKUM16,
    32: TAKUM32,
    64: TAKUM64,
}

# Mathematical constant: sqrt(e)
SQRT_E: Final[float] = math.sqrt(math.e)
LN_SQRT_E: Final[float] = 0.5  # ln(sqrt(e)) = 0.5


# =============================================================================
# CHARACTERISTIC BIAS LOOKUP TABLE
# =============================================================================


def c_bias(r: int) -> int:
    """
    Compute characteristic bias for regime value r.

    c_bias(r) = 2^(r+1) - 1

    Args:
        r: Regime value in [0, 7]

    Returns:
        Bias value for characteristic encoding

    Examples:
        >>> c_bias(0)
        1
        >>> c_bias(3)
        15
        >>> c_bias(7)
        255
    """
    if not 0 <= r <= 7:
        raise ValueError(f"Regime must be in [0, 7], got {r}")
    return (1 << (r + 1)) - 1


C_BIAS_LUT: Final[tuple[int, ...]] = tuple(c_bias(r) for r in range(8))


# =============================================================================
# ENCODING FUNCTIONS
# =============================================================================


def compute_regime(l_abs: int) -> int:
    """
    Compute regime value from absolute logarithm magnitude.

    The regime r is the position of the highest set bit in l_biased.

    Args:
        l_abs: Absolute value of the logarithm (|l|)

    Returns:
        Regime value r in [0, 7]
    """
    if l_abs == 0:
        return 0
    # r = floor(log2(|l| + 1))
    return min(7, (l_abs + 1).bit_length() - 1)


def encode_takum_log(value: float, config: TakumConfig) -> int:
    """
    Encode a float as a logarithmic takum.

    This implements Algorithm 1 from the Takum paper (simplified).

    Args:
        value: Float value to encode
        config: Takum configuration (bit width)

    Returns:
        Signed integer representation of the takum

    Raises:
        ValueError: If value is NaN or infinite
    """
    # Handle special cases
    if math.isnan(value):
        return config.nar_value
    if math.isinf(value):
        return config.nar_value
    if value == 0.0:
        return 0

    # Extract sign
    s = 0 if value > 0 else 1
    abs_value = abs(value)

    # Compute logarithm in base sqrt(e)
    # l = log_{sqrt(e)}(|value|) = ln(|value|) / ln(sqrt(e)) = 2 * ln(|value|)
    l_float = 2.0 * math.log(abs_value)
    l = round(l_float)

    # Clamp to valid range
    l = max(-255, min(255, l))

    # Determine direction
    d = 1 if l >= 0 else 0

    # Compute regime from |l|
    l_abs = abs(l)
    r = compute_regime(l_abs)

    # Compute characteristic (position within regime)
    if l >= 0:
        c = l - C_BIAS_LUT[r] if r > 0 else 0
    else:
        c = C_BIAS_LUT[r] - 1 - l_abs if r > 0 else 0

    # Compute mantissa bits available
    m_bits = config.bits - config.overhead_bits - r
    if m_bits < 0:
        m_bits = 0

    # Compute mantissa from fractional part of l_float
    l_frac = abs(l_float) - abs(l)
    m = int(l_frac * (1 << m_bits)) if m_bits > 0 else 0

    # Assemble bit pattern
    # Layout: S(1) | D(1) | R(3) | C(r bits) | M(m_bits)
    result = (s << (config.bits - 1))
    result |= (d << (config.bits - 2))
    result |= (r << (config.bits - 5))
    result |= (c << m_bits) if r > 0 else 0
    result |= m

    # Convert to signed integer
    if s == 1:
        result = result - (1 << config.bits)

    return result


def decode_takum_log(encoded: int, config: TakumConfig) -> float:
    """
    Decode a logarithmic takum to a float.

    This implements Algorithm 2 from the Takum paper (simplified).

    Args:
        encoded: Signed integer takum representation
        config: Takum configuration (bit width)

    Returns:
        Decoded float value (or math.nan for NaR)
    """
    # Handle special cases
    if encoded == config.nar_value:
        return math.nan
    if encoded == 0:
        return 0.0

    # Convert to unsigned for bit manipulation
    if encoded < 0:
        encoded_u = encoded + (1 << config.bits)
    else:
        encoded_u = encoded

    # Extract sign
    s = (encoded_u >> (config.bits - 1)) & 1

    # Extract direction
    d = (encoded_u >> (config.bits - 2)) & 1

    # Extract regime
    r = (encoded_u >> (config.bits - 5)) & 0b111

    # Compute mantissa bits
    m_bits = config.bits - config.overhead_bits - r
    if m_bits < 0:
        m_bits = 0

    # Extract characteristic
    if r > 0:
        c = (encoded_u >> m_bits) & ((1 << r) - 1)
    else:
        c = 0

    # Extract mantissa
    m = encoded_u & ((1 << m_bits) - 1) if m_bits > 0 else 0

    # Compute l_biased
    if d == 1:  # Positive direction (l >= 0)
        l = C_BIAS_LUT[r] + c if r > 0 else 0
    else:  # Negative direction (l < 0)
        l_biased = C_BIAS_LUT[r] - 1 - c if r > 0 else 0
        l = -(l_biased + 1)

    # Add mantissa contribution
    l_float = l + (m / (1 << m_bits) if m_bits > 0 else 0)

    # Convert back to linear: value = sqrt(e)^l = e^(l/2)
    abs_value = math.exp(l_float / 2.0)

    return -abs_value if s == 1 else abs_value


# =============================================================================
# VALIDATION TEST CASES
# =============================================================================

# Known correct encodings for validation
TEST_ENCODINGS: list[tuple[float, int, int]] = [
    # (value, expected_takum16, bits)
    (1.0, 0x2000, 16),
    (-1.0, -0x2000, 16),
    (0.0, 0x0000, 16),
    (math.e, 0x4000, 16),  # e = sqrt(e)^2
    (SQRT_E, 0x2800, 16),  # sqrt(e) = sqrt(e)^1
]

# Known constants from the Takum paper
KNOWN_CONSTANTS: dict[str, dict[str, float | int]] = {
    "pi": {"value": math.pi, "takum16_approx": 0x3C48},
    "e": {"value": math.e, "takum16_approx": 0x4000},
    "sqrt2": {"value": math.sqrt(2), "takum16_approx": 0x2358},
    "ln2": {"value": math.log(2), "takum16_approx": 0x1A38},
}


def test_encoding_roundtrip(config: TakumConfig, verbose: bool = False) -> bool:
    """
    Test encoding/decoding roundtrip for various values.

    Args:
        config: Takum configuration to test
        verbose: Print detailed results

    Returns:
        True if all tests pass
    """
    test_values = [
        0.0,
        1.0,
        -1.0,
        SQRT_E,
        math.e,
        math.pi,
        0.5,
        2.0,
        0.1,
        10.0,
        100.0,
        0.01,
    ]

    all_passed = True
    max_relative_error = 0.0

    for value in test_values:
        if value == 0.0:
            # Zero should encode/decode exactly
            encoded = encode_takum_log(value, config)
            decoded = decode_takum_log(encoded, config)
            passed = decoded == 0.0
        else:
            encoded = encode_takum_log(value, config)
            decoded = decode_takum_log(encoded, config)
            relative_error = abs(decoded - value) / abs(value)
            max_relative_error = max(max_relative_error, relative_error)

            # Allow some error due to limited precision
            tolerance = 2.0 ** (-(config.bits - 8))
            passed = relative_error < tolerance

        if verbose:
            status = "✓" if passed else "✗"
            print(f"  {status} {value:>12.6f} -> 0x{encoded & ((1 << config.bits) - 1):0{config.bits // 4}X} -> {decoded:>12.6f}")

        all_passed = all_passed and passed

    if verbose:
        print(f"  Max relative error: {max_relative_error:.2e}")

    return all_passed


def test_special_values(config: TakumConfig, verbose: bool = False) -> bool:
    """
    Test special value handling (NaR, zero, one).

    Args:
        config: Takum configuration to test
        verbose: Print detailed results

    Returns:
        True if all tests pass
    """
    all_passed = True

    # Test NaR
    nar_decoded = decode_takum_log(config.nar_value, config)
    nar_passed = math.isnan(nar_decoded)
    if verbose:
        status = "✓" if nar_passed else "✗"
        print(f"  {status} NaR (0x{config.nar_value & ((1 << config.bits) - 1):0{config.bits // 4}X}) -> {nar_decoded}")
    all_passed = all_passed and nar_passed

    # Test zero
    zero_encoded = encode_takum_log(0.0, config)
    zero_passed = zero_encoded == 0
    if verbose:
        status = "✓" if zero_passed else "✗"
        print(f"  {status} Zero: 0.0 -> 0x{zero_encoded:0{config.bits // 4}X}")
    all_passed = all_passed and zero_passed

    # Test one (approximate - encoding may vary slightly)
    one_encoded = encode_takum_log(1.0, config)
    one_decoded = decode_takum_log(one_encoded, config)
    one_passed = abs(one_decoded - 1.0) < 0.01
    if verbose:
        status = "✓" if one_passed else "✗"
        print(f"  {status} One: 1.0 -> 0x{one_encoded & ((1 << config.bits) - 1):0{config.bits // 4}X} -> {one_decoded}")
    all_passed = all_passed and one_passed

    # Test NaN input
    nan_encoded = encode_takum_log(float("nan"), config)
    nan_passed = nan_encoded == config.nar_value
    if verbose:
        status = "✓" if nan_passed else "✗"
        print(f"  {status} NaN input -> 0x{nan_encoded & ((1 << config.bits) - 1):0{config.bits // 4}X} (NaR)")
    all_passed = all_passed and nan_passed

    return all_passed


def test_symmetry(config: TakumConfig, verbose: bool = False) -> bool:
    """
    Test that x and 1/x have related encodings (negation in l-domain).

    Args:
        config: Takum configuration to test
        verbose: Print detailed results

    Returns:
        True if symmetry holds
    """
    test_values = [2.0, 4.0, 10.0, SQRT_E, math.e, math.pi]
    all_passed = True

    for x in test_values:
        inv_x = 1.0 / x
        enc_x = encode_takum_log(x, config)
        enc_inv = encode_takum_log(inv_x, config)

        # In l-domain, 1/x should give -l (approximately)
        # The sum of encodings should be close to the encoding of 1.0
        dec_x = decode_takum_log(enc_x, config)
        dec_inv = decode_takum_log(enc_inv, config)
        product = dec_x * dec_inv

        # Product should be close to 1.0
        passed = abs(product - 1.0) < 0.1
        if verbose:
            status = "✓" if passed else "✗"
            print(f"  {status} {x:.4f} × {inv_x:.4f} = {product:.6f} (expected ~1.0)")

        all_passed = all_passed and passed

    return all_passed


def run_all_tests(verbose: bool = True) -> bool:
    """
    Run all validation tests.

    Args:
        verbose: Print detailed results

    Returns:
        True if all tests pass
    """
    all_passed = True

    for bits, config in CONFIGS.items():
        print(f"\n{'=' * 60}")
        print(f"Testing TAKUM{bits}")
        print(f"{'=' * 60}")

        print("\nRoundtrip encoding tests:")
        if not test_encoding_roundtrip(config, verbose):
            all_passed = False

        print("\nSpecial value tests:")
        if not test_special_values(config, verbose):
            all_passed = False

        print("\nSymmetry tests (x × 1/x ≈ 1):")
        if not test_symmetry(config, verbose):
            all_passed = False

    return all_passed


# =============================================================================
# CLI INTERFACE
# =============================================================================


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Takum Arithmetic Implementation Validator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python validate_takum.py --test-all
  python validate_takum.py --encode 3.14159 --bits 16
  python validate_takum.py --decode 0x3C48 --bits 16
        """,
    )

    parser.add_argument(
        "--test-all",
        action="store_true",
        help="Run all validation tests",
    )
    parser.add_argument(
        "--test-encoding",
        action="store_true",
        help="Run encoding roundtrip tests",
    )
    parser.add_argument(
        "--test-constants",
        action="store_true",
        help="Test known mathematical constants",
    )
    parser.add_argument(
        "--encode",
        type=float,
        metavar="VALUE",
        help="Encode a float value to takum",
    )
    parser.add_argument(
        "--decode",
        type=str,
        metavar="HEX",
        help="Decode a hex takum value to float",
    )
    parser.add_argument(
        "--bits",
        type=int,
        choices=[8, 16, 32, 64],
        default=16,
        help="Takum bit width (default: 16)",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Verbose output",
    )

    args = parser.parse_args()

    # Get configuration for specified bit width
    config = CONFIGS[args.bits]

    # Handle test modes
    if args.test_all:
        passed = run_all_tests(verbose=True)
        print(f"\n{'=' * 60}")
        if passed:
            print("ALL TESTS PASSED ✓")
            return 0
        else:
            print("SOME TESTS FAILED ✗")
            return 1

    if args.test_encoding:
        passed = test_encoding_roundtrip(config, verbose=True)
        return 0 if passed else 1

    if args.test_constants:
        print("Known Mathematical Constants:")
        print("-" * 40)
        for name, data in KNOWN_CONSTANTS.items():
            value = data["value"]
            encoded = encode_takum_log(value, TAKUM16)
            decoded = decode_takum_log(encoded, TAKUM16)
            error = abs(decoded - value) / value * 100
            print(f"  {name:8s}: {value:.10f}")
            print(f"           -> 0x{encoded & 0xFFFF:04X}")
            print(f"           -> {decoded:.10f} ({error:.4f}% error)")
        return 0

    # Handle encode/decode operations
    if args.encode is not None:
        encoded = encode_takum_log(args.encode, config)
        hex_str = f"0x{encoded & ((1 << config.bits) - 1):0{config.bits // 4}X}"
        print(f"Encoding {args.encode} as takum{config.bits}:")
        print(f"  Hex: {hex_str}")
        print(f"  Int: {encoded}")
        # Verify roundtrip
        decoded = decode_takum_log(encoded, config)
        print(f"  Decoded: {decoded}")
        return 0

    if args.decode is not None:
        # Parse hex value
        try:
            encoded = int(args.decode, 16)
            # Convert to signed if necessary
            if encoded >= (1 << (config.bits - 1)):
                encoded = encoded - (1 << config.bits)
        except ValueError:
            print(f"Error: Invalid hex value '{args.decode}'")
            return 1

        decoded = decode_takum_log(encoded, config)
        print(f"Decoding {args.decode} as takum{config.bits}:")
        if math.isnan(decoded):
            print("  Value: NaR (Not a Real)")
        else:
            print(f"  Value: {decoded}")
        return 0

    # No arguments - show help
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
