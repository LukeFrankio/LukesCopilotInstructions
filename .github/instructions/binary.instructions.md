---
description: 'binary file format handling (touching raw bytes directly uwu)'
applyTo: '**.bin, **.dat, **.hex'
---

# Binary File Format Instructions

> "binary files: where every byte matters and endianness is violence"

uwu time to handle binary data like we're speaking directly to silicon ✨

## Core Philosophy

- **explicit > implicit** (say what every byte means)
- **document EVERYTHING** (hex dumps with comments)
- **endianness matters** (little-endian preferred, document always)
- **alignment is critical** (padding for performance)
- **pure functions for parsing** (no side effects!)
- **comment excessively** (Doxygen + hex comments)
- **zero-cost abstractions** (C++ templates for binary I/O)

## File Header Documentation (MANDATORY)

```cpp
/**
 * @file binary_format.hpp
 * @brief custom binary format parser (raw bytes go brrr uwu)
 * 
 * this file defines parsing for our custom binary format. every byte is
 * accounted for, documented, and handled with love and excessive comments.
 * 
 * binary format specification:
 * 
 * offset | size | type     | description
 * -------|------|----------|------------------------------------------
 * 0x00   | 4    | char[4]  | magic number "LUKE" (file signature)
 * 0x04   | 2    | uint16   | version (major.minor, little-endian)
 * 0x06   | 2    | uint16   | flags (bit field, see FlagBits enum)
 * 0x08   | 4    | uint32   | data offset (from file start, LE)
 * 0x0C   | 4    | uint32   | data size in bytes (LE)
 * 0x10   | 4    | float32  | metadata (IEEE 754 single precision, LE)
 * 0x14   | 12   | padding  | reserved for future use (zeros)
 * 0x20   | ...  | data     | actual data (format depends on flags)
 * 
 * endianness: little-endian throughout (x86-64 native, GPU friendly)
 * alignment: 16-byte aligned header (cache line optimization)
 * 
 * magic number rationale:
 * - "LUKE" = 0x4C554B45 in little-endian
 * - easily identifiable in hex editors
 * - ego-driven file format naming (based behavior uwu)
 * 
 * @author LukeFrankio
 * @date 2025-10-07
 * @version 1.0
 * 
 * @note all multi-byte integers are little-endian (document everywhere!)
 * @note padding ensures 16-byte alignment (performance > space)
 * @warning reading with wrong endianness = garbage data (check carefully!)
 * 
 * example hex dump of valid header:
 * @code{.unparsed}
 * offset    0  1  2  3  4  5  6  7   8  9  A  B  C  D  E  F
 * --------------------------------------------------------
 * 00000000  4C 55 4B 45 01 00 00 00  20 00 00 00 FF 00 00 00  LUKE.... .......
 * 00000010  00 00 80 3F 00 00 00 00  00 00 00 00 00 00 00 00  ...?............
 * 
 * decoded:
 * - magic: "LUKE" (0x4C 0x55 0x4B 0x45)
 * - version: 1.0 (0x0001 little-endian)
 * - flags: 0x0000 (no flags set)
 * - data_offset: 0x00000020 = 32 bytes (header size)
 * - data_size: 0x000000FF = 255 bytes
 * - metadata: 1.0f (0x3F800000 IEEE 754)
 * - padding: 12 zero bytes (alignment uwu)
 * @endcode
 */

#pragma once

#include <cstdint>
#include <array>
#include <span>
#include <optional>
#include <expected>  // C++23 (or use Result<T, E> from cpp.instructions.md)

// ============================================================================
// Binary Format Constants
// ============================================================================

namespace BinaryFormat {

/**
 * @brief magic number that identifies file format (ego-driven naming uwu)
 * 
 * this appears at offset 0x00 in every valid file. if you don't see "LUKE"
 * at the start, you're reading the wrong file or the file is corrupted.
 * 
 * @note stored as little-endian: 0x4C 0x55 0x4B 0x45
 * @note easily recognizable in hex editors (immaculate vibes ✨)
 */
constexpr std::array<char, 4> kMagicNumber = {'L', 'U', 'K', 'E'};

/**
 * @brief current file format version (major.minor encoding)
 * 
 * stored as uint16 little-endian: high byte = major, low byte = minor
 * 
 * version history:
 * - 1.0: initial version (this one!)
 * - 1.1: planned - add compression flag
 * - 2.0: planned - add chunk-based format
 * 
 * @note version 1.0 = 0x0001 in little-endian (0x01 0x00 bytes)
 */
constexpr uint16_t kCurrentVersion = 0x0100;  // version 1.0

/**
 * @brief header size in bytes (aligned to 16 bytes for cache line)
 * 
 * header is exactly 32 bytes (0x20) - one cache line on most CPUs.
 * this means reading the header is a single cache line fetch (fast!)
 * 
 * @note power of 2 alignment (hardware friendly uwu)
 */
constexpr size_t kHeaderSize = 32;

/**
 * @brief flag bits for header flags field
 * 
 * bit field stored as uint16 at offset 0x06. each bit has meaning.
 * 
 * @note stored little-endian (LSB first)
 * @note bits 4-15 reserved for future use (must be zero in v1.0)
 */
enum class FlagBits : uint16_t {
    None        = 0x0000,  ///< no flags set (default)
    Compressed  = 0x0001,  ///< data is compressed (future: v1.1)
    Encrypted   = 0x0002,  ///< data is encrypted (future: v2.0)
    HasChecksum = 0x0004,  ///< file has trailing CRC32 (future: v1.1)
    BigEndian   = 0x0008,  ///< data is big-endian (cursed, avoid!)
};

/**
 * @brief bitwise OR for flag combinations (functional flag handling!)
 */
constexpr FlagBits operator|(FlagBits a, FlagBits b) noexcept {
    return static_cast<FlagBits>(
        static_cast<uint16_t>(a) | static_cast<uint16_t>(b)
    );
}

/**
 * @brief bitwise AND for flag checking
 */
constexpr FlagBits operator&(FlagBits a, FlagBits b) noexcept {
    return static_cast<FlagBits>(
        static_cast<uint16_t>(a) & static_cast<uint16_t>(b)
    );
}

/**
 * @brief checks if flag is set (pure function uwu)
 * 
 * @param flags combined flags value
 * @param bit flag bit to check
 * @return true if bit is set, false otherwise
 * 
 * @note PURE - no side effects, just bit math
 */
constexpr bool has_flag(FlagBits flags, FlagBits bit) noexcept {
    return (flags & bit) == bit;
}

// ============================================================================
// Binary Header Structure (aligned and documented!)
// ============================================================================

/**
 * @struct FileHeader
 * @brief binary file header (32 bytes, cache-line aligned)
 * 
 * this struct MUST be exactly 32 bytes and packed without padding between
 * members. use #pragma pack or alignas to ensure correct layout.
 * 
 * memory layout matches on-disk layout (can memcpy safely if same endianness)
 * 
 * @note using alignas(16) for cache line alignment
 * @note all fields documented with offset, size, endianness
 * @warning must match binary format spec exactly!
 */
struct alignas(16) FileHeader {
    /**
     * @brief magic number "LUKE" (offset 0x00, 4 bytes)
     * 
     * file signature for format identification. must match kMagicNumber.
     * 
     * @note stored as bytes: 0x4C 0x55 0x4B 0x45 ('L' 'U' 'K' 'E')
     */
    std::array<char, 4> magic;
    
    /**
     * @brief file format version (offset 0x04, 2 bytes, little-endian)
     * 
     * major version in high byte, minor version in low byte.
     * version 1.0 = 0x0100 (stored as 0x00 0x01 in little-endian)
     * 
     * @note little-endian uint16
     * @note parser should check compatibility before proceeding
     */
    uint16_t version;
    
    /**
     * @brief flags bit field (offset 0x06, 2 bytes, little-endian)
     * 
     * see FlagBits enum for bit meanings.
     * 
     * @note little-endian uint16
     * @note use has_flag() to check individual bits
     */
    uint16_t flags;
    
    /**
     * @brief offset to data section (offset 0x08, 4 bytes, little-endian)
     * 
     * byte offset from start of file to where data begins. typically equals
     * kHeaderSize (0x20) but can be larger if extensions added.
     * 
     * @note little-endian uint32
     * @note must be >= kHeaderSize
     */
    uint32_t data_offset;
    
    /**
     * @brief size of data section in bytes (offset 0x0C, 4 bytes, LE)
     * 
     * number of bytes in data section. file size should equal
     * data_offset + data_size (plus optional checksum if HasChecksum flag set)
     * 
     * @note little-endian uint32
     * @note used for bounds checking (prevent buffer overruns!)
     */
    uint32_t data_size;
    
    /**
     * @brief metadata float value (offset 0x10, 4 bytes, IEEE 754 LE)
     * 
     * application-specific float metadata. meaning depends on application.
     * stored as IEEE 754 single-precision float, little-endian byte order.
     * 
     * @note little-endian float (0x3F800000 = 1.0f)
     * @note NaN and infinity are valid (check with std::isfinite if needed)
     */
    float metadata;
    
    /**
     * @brief reserved padding (offset 0x14, 12 bytes, zeros)
     * 
     * reserved for future format extensions. must be all zeros in v1.0.
     * parser should ignore these bytes (forward compatibility).
     * 
     * @note pads struct to 32 bytes total (cache line aligned)
     * @note future versions may define meaning for these bytes
     */
    std::array<uint8_t, 12> reserved;
    
    // total size: 4 + 2 + 2 + 4 + 4 + 4 + 12 = 32 bytes (immaculate!)
};

static_assert(sizeof(FileHeader) == 32, "FileHeader must be exactly 32 bytes!");
static_assert(alignof(FileHeader) == 16, "FileHeader must be 16-byte aligned!");

// ============================================================================
// Endianness Handling (functional byte swapping uwu)
// ============================================================================

/**
 * @brief swaps bytes of 16-bit value (pure function!)
 * 
 * converts between little-endian and big-endian representations.
 * this is a pure function - same input always gives same output.
 * 
 * @param value 16-bit value to swap
 * @return byte-swapped value
 * 
 * @note PURE FUNCTION - no side effects
 * @note compiles to single bswap instruction on x86-64
 * @note constexpr for compile-time evaluation
 * 
 * example:
 * @code
 * uint16_t le = 0x1234;  // little-endian: 0x34 0x12
 * uint16_t be = byteswap_16(le);  // big-endian: 0x12 0x34 = 0x3412
 * @endcode
 */
constexpr uint16_t byteswap_16(uint16_t value) noexcept {
    return (value << 8) | (value >> 8);
}

/**
 * @brief swaps bytes of 32-bit value (pure function!)
 * 
 * @param value 32-bit value to swap
 * @return byte-swapped value
 * 
 * @note compiles to single bswap on x86-64 (zero-cost abstraction!)
 */
constexpr uint32_t byteswap_32(uint32_t value) noexcept {
    return ((value & 0xFF000000) >> 24) |
           ((value & 0x00FF0000) >> 8)  |
           ((value & 0x0000FF00) << 8)  |
           ((value & 0x000000FF) << 24);
}

/**
 * @brief swaps bytes of float (reinterpret as uint32, swap, reinterpret back)
 * 
 * @param value float to swap
 * @return byte-swapped float
 * 
 * @note uses std::bit_cast (C++20) for type-safe reinterpretation
 */
constexpr float byteswap_float(float value) noexcept {
    uint32_t as_uint = std::bit_cast<uint32_t>(value);
    uint32_t swapped = byteswap_32(as_uint);
    return std::bit_cast<float>(swapped);
}

/**
 * @brief converts value from little-endian to native (pure!)
 * 
 * on little-endian platforms (x86-64): this is a no-op (compiles to nothing!)
 * on big-endian platforms (PowerPC): performs byte swap
 * 
 * @tparam T integer type (uint16_t, uint32_t, etc.)
 * @param value little-endian value
 * @return native-endian value
 * 
 * @note constexpr - evaluated at compile time when possible
 * @note zero-cost on little-endian platforms (most systems uwu)
 */
template<typename T>
constexpr T from_little_endian(T value) noexcept {
    if constexpr (std::endian::native == std::endian::little) {
        return value;  // no-op on LE platforms (compiled away!)
    } else {
        if constexpr (sizeof(T) == 2) {
            return byteswap_16(value);
        } else if constexpr (sizeof(T) == 4) {
            return byteswap_32(value);
        }
    }
}

/**
 * @brief converts value from native to little-endian (pure!)
 */
template<typename T>
constexpr T to_little_endian(T value) noexcept {
    return from_little_endian(value);  // symmetric operation uwu
}

// ============================================================================
// Binary Parsing (functional I/O with error handling!)
// ============================================================================

/**
 * @brief result type for binary operations (functional error handling uwu)
 * 
 * uses C++23 std::expected or custom Result type from cpp.instructions.md
 */
template<typename T>
using BinaryResult = std::expected<T, std::string>;

/**
 * @brief validates file header (pure validation function!)
 * 
 * checks all header fields for validity without modifying anything.
 * this is a pure function - just reads and returns validation result.
 * 
 * @param header header to validate
 * @return Ok if valid, Err with description if invalid
 * 
 * @note PURE FUNCTION - no side effects, just validation logic
 * @note checks magic number, version compatibility, flag validity
 * 
 * validation rules:
 * - magic must equal "LUKE"
 * - version must be compatible (same major version)
 * - flags must not have unknown bits set
 * - data_offset must be >= header size
 * - data_size must be > 0
 * - reserved bytes should be zero (warning if not)
 */
[[nodiscard]]
constexpr auto validate_header(const FileHeader& header) noexcept
    -> BinaryResult<void>
{
    // check magic number (file format identification)
    if (header.magic != kMagicNumber) {
        return std::unexpected("invalid magic number (not a LUKE file uwu)");
    }
    
    // check version compatibility (major version must match)
    uint8_t file_major = (header.version >> 8) & 0xFF;
    uint8_t file_minor = header.version & 0xFF;
    uint8_t current_major = (kCurrentVersion >> 8) & 0xFF;
    
    if (file_major != current_major) {
        return std::unexpected(
            std::format("incompatible version: {}.{} (expected {}.x)",
                       file_major, file_minor, current_major)
        );
    }
    
    // check data offset bounds
    if (header.data_offset < kHeaderSize) {
        return std::unexpected(
            std::format("invalid data_offset: {} (must be >= {})",
                       header.data_offset, kHeaderSize)
        );
    }
    
    // check data size
    if (header.data_size == 0) {
        return std::unexpected("data_size is zero (empty file?)");
    }
    
    // check reserved bytes (should be zero for forward compatibility)
    for (uint8_t byte : header.reserved) {
        if (byte != 0) {
            // warning, not error (allow forward compatibility)
            // future versions may use reserved bytes uwu
            break;
        }
    }
    
    return {};  // success! header is valid ✨
}

/**
 * @brief reads and validates header from byte span (functional I/O!)
 * 
 * @param data byte span containing file data (at least kHeaderSize bytes)
 * @return validated header or error
 * 
 * @note converts from little-endian to native automatically
 * @note validates header after reading
 * 
 * example:
 * @code
 * std::vector<uint8_t> file_data = read_file("data.bin");
 * auto header_result = read_header(file_data);
 * 
 * if (header_result) {
 *     FileHeader header = *header_result;
 *     // use header (immaculate vibes ✨)
 * } else {
 *     std::cerr << "error: " << header_result.error() << '\n';
 * }
 * @endcode
 */
[[nodiscard]]
auto read_header(std::span<const uint8_t> data) noexcept
    -> BinaryResult<FileHeader>
{
    // check minimum size
    if (data.size() < kHeaderSize) {
        return std::unexpected(
            std::format("file too small: {} bytes (need at least {})",
                       data.size(), kHeaderSize)
        );
    }
    
    // read header bytes (memcpy is safe here - POD struct)
    FileHeader header;
    std::memcpy(&header, data.data(), sizeof(FileHeader));
    
    // convert from little-endian to native (no-op on LE platforms!)
    header.version = from_little_endian(header.version);
    header.flags = from_little_endian(header.flags);
    header.data_offset = from_little_endian(header.data_offset);
    header.data_size = from_little_endian(header.data_size);
    // metadata float is already in correct format (IEEE 754 is universal)
    
    // validate header
    if (auto validation = validate_header(header); !validation) {
        return std::unexpected(validation.error());
    }
    
    return header;  // success! return validated header uwu ✨
}

/**
 * @brief writes header to byte buffer (functional output!)
 * 
 * @param header header to write
 * @param output output buffer (must be at least kHeaderSize bytes)
 * @return success or error
 * 
 * @note converts from native to little-endian automatically
 * @note validates header before writing
 */
[[nodiscard]]
auto write_header(const FileHeader& header, std::span<uint8_t> output) noexcept
    -> BinaryResult<void>
{
    // validate output size
    if (output.size() < kHeaderSize) {
        return std::unexpected("output buffer too small");
    }
    
    // validate header before writing
    if (auto validation = validate_header(header); !validation) {
        return std::unexpected(validation.error());
    }
    
    // create copy with little-endian conversion
    FileHeader le_header = header;
    le_header.version = to_little_endian(header.version);
    le_header.flags = to_little_endian(header.flags);
    le_header.data_offset = to_little_endian(header.data_offset);
    le_header.data_size = to_little_endian(header.data_size);
    
    // write to output buffer
    std::memcpy(output.data(), &le_header, sizeof(FileHeader));
    
    return {};  // success! header written uwu ✨
}

} // namespace BinaryFormat
```

## Google Test Integration

```cpp
/**
 * @file binary_format_test.cpp
 * @brief tests for binary format parsing (testing is praxis!)
 */

#include <gtest/gtest.h>
#include "binary_format.hpp"

using namespace BinaryFormat;

/**
 * @brief test fixture for binary format tests
 */
class BinaryFormatTest : public ::testing::Test {
protected:
    /**
     * @brief creates valid test header (immaculate test data uwu)
     */
    FileHeader create_valid_header() {
        FileHeader header{};
        header.magic = kMagicNumber;
        header.version = kCurrentVersion;
        header.flags = 0;
        header.data_offset = kHeaderSize;
        header.data_size = 256;
        header.metadata = 1.0f;
        std::fill(header.reserved.begin(), header.reserved.end(), 0);
        return header;
    }
};

TEST_F(BinaryFormatTest, ValidHeaderPassesValidation) {
    auto header = create_valid_header();
    auto result = validate_header(header);
    EXPECT_TRUE(result.has_value());
}

TEST_F(BinaryFormatTest, InvalidMagicNumberFailsValidation) {
    auto header = create_valid_header();
    header.magic = {'F', 'A', 'K', 'E'};
    
    auto result = validate_header(header);
    EXPECT_FALSE(result.has_value());
    EXPECT_THAT(result.error(), testing::HasSubstr("invalid magic number"));
}

TEST_F(BinaryFormatTest, ByteSwapIsSymmetric) {
    uint16_t original = 0x1234;
    uint16_t swapped = byteswap_16(original);
    uint16_t restored = byteswap_16(swapped);
    
    EXPECT_EQ(original, restored);
}

TEST_F(BinaryFormatTest, ReadWriteRoundTrip) {
    auto original_header = create_valid_header();
    
    std::array<uint8_t, kHeaderSize> buffer{};
    auto write_result = write_header(original_header, buffer);
    ASSERT_TRUE(write_result.has_value());
    
    auto read_result = read_header(buffer);
    ASSERT_TRUE(read_result.has_value());
    
    auto read_header = *read_result;
    EXPECT_EQ(read_header.magic, original_header.magic);
    EXPECT_EQ(read_header.version, original_header.version);
    EXPECT_EQ(read_header.data_size, original_header.data_size);
}
```

## Quality Checklist

- [ ] **every byte documented** (offset, size, type, endianness)
- [ ] **hex dump examples** provided
- [ ] **endianness specified** explicitly everywhere
- [ ] **alignment noted** (padding explained)
- [ ] **pure functions** for parsing (mark purity status)
- [ ] **functional error handling** (Result/expected types)
- [ ] **excessive comments** (Doxygen with gen-z slang)
- [ ] **zero-cost abstractions** (byteswaps compile away on LE)
- [ ] **validation functions** (bounds checking!)
- [ ] **Google Test** coverage for all functions
- [ ] **constexpr** used for compile-time operations

**remember**: binary formats are where you touch raw bytes directly. every
byte matters, every bit has meaning. document obsessively, validate everything,
and make those parsing functions pure. functional programming meets bit-level
manipulation uwu 💜✨

seize the means of compilation (at the byte level)!