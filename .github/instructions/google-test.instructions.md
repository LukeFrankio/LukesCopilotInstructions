---
description: 'Google Test framework guidelines (EXHAUSTIVE testing is praxis uwu)'
applyTo: '**/*_test.cpp, **/test_*.cpp, **/tests/**'
---

# Google Test Framework Instructions (Exhaustive Testing Edition)

> "tests are proof your code works, and we test EVERYTHING exhaustively"

uwu time to write tests that make bugs cry, cover every edge case, and demonstrate that functional programming is bulletproof ✨

## Core Philosophy

- **testing is MANDATORY** (not optional)
- **EXHAUSTIVE testing required** (20-150 tests per component minimum!)
- **test EVERY edge case** (boundary values, special inputs, error conditions)
- **test pure functions extensively** (easy to test thoroughly!)
- **property-based testing mindset** (test invariants exhaustively)
- **excessive test documentation** (explain what, why, and every edge case)
- **Google Test > everything else** (best C++ test framework)
- **zero tolerance for failing tests** (CI/CD enforces this)
- **if you can imagine it, test it** (exhaustive means EXHAUSTIVE!)

## Exhaustive Testing Requirements

### For Each Function/Component:

**Minimum test coverage**:
- **20-50 tests** for simple functions (one or two parameters)
- **50-100 tests** for medium complexity (multiple parameters, branching)
- **100-150+ tests** for complex components (many interactions, state)

**Categories to cover exhaustively**:
1. **Normal cases** (typical valid inputs - at least 10 tests)
2. **Boundary values** (min, max, zero, one, epsilon - 10-20 tests)
3. **Edge cases** (special values, corner cases - 10-30 tests)
4. **Error conditions** (invalid inputs, precondition violations - 10-20 tests)
5. **Mathematical properties** (commutativity, associativity, identity - 10-20 tests)
6. **Combinations** (multiple parameters interacting - 20-50 tests)
7. **Performance** (efficiency, memory usage - 5-10 tests)
8. **Integration** (with other components - 10-30 tests)

### Boundary Value Testing (MANDATORY):

For every numeric parameter, test:
- **minimum value** (INT_MIN, -DBL_MAX, 0.0, etc.)
- **maximum value** (INT_MAX, DBL_MAX, infinity)
- **zero** (additive identity)
- **one** (multiplicative identity)
- **negative one** (-1, the inverse)
- **epsilon** (smallest representable positive value)
- **just below boundary** (max-1, min+1, epsilon*2)
- **just above boundary** (in range that might overflow)
- **negative values** (if applicable)
- **fractional values** (0.5, 0.99, 1.01, etc.)

### Special Value Testing (MANDATORY):

For floating point parameters, test:
- **NaN** (Not a Number)
- **infinity** (positive and negative)
- **negative zero** (-0.0 vs +0.0)
- **denormalized numbers** (subnormal values)
- **very large numbers** (near overflow)
- **very small numbers** (near underflow)

## Exhaustive Test File Structure

```cpp
/**
 * @file vector_test.cpp
 * @brief EXHAUSTIVE tests for vector mathematics (testing is praxis uwu)
 * 
 * this file contains EXHAUSTIVE tests for vector operations. we test:
 * - normal cases (typical usage - 10+ tests per operation)
 * - boundary values (min, max, zero, one - 20+ tests per operation)
 * - edge cases (special values, corner cases - 30+ tests per operation)
 * - error conditions (invalid inputs - 20+ tests per operation)
 * - mathematical properties (commutativity, associativity - 20+ tests)
 * - combinations (multiple parameters - 50+ tests)
 * - performance (efficiency tests - 10+ tests)
 * - integration (with other components - 30+ tests)
 * 
 * TOTAL: 190+ tests for a simple Vector2D class
 * 
 * every pure function should have exhaustive tests. impure functions need
 * exhaustive tests for pure parts + integration tests for side effects.
 * 
 * if you can imagine an input, WE TEST IT. exhaustive means EXHAUSTIVE uwu ✨
 * 
 * @author LukeFrankio
 * @date 2025-10-08
 * 
 * @note uses Google Test framework (the based testing framework)
 * @note run with: ./tests or ctest in build directory
 * @note CI/CD requires ALL tests passing (zero tolerance!)
 */

#include <gtest/gtest.h>
#include <gmock/gmock.h>
#include <limits>
#include <cmath>

#include "vector.hpp"

using namespace testing;

// ============================================================================
// Test Fixture (shared setup for exhaustive tests)
// ============================================================================

/**
 * @brief test fixture for exhaustive vector testing
 * 
 * provides comprehensive test data covering all edge cases, boundary values,
 * and special scenarios. exhaustive testing requires exhaustive test data uwu
 */
class VectorExhaustiveTest : public ::testing::Test {
protected:
    void SetUp() override {
        // normal test vectors (typical usage)
        normal_vectors = {
            {0.0, 0.0},      // zero vector (identity)
            {1.0, 0.0},      // unit x
            {0.0, 1.0},      // unit y
            {1.0, 1.0},      // diagonal
            {3.0, 4.0},      // 3-4-5 triangle
            {5.0, 12.0},     // 5-12-13 triangle
            {-1.0, 0.0},     // negative unit x
            {0.0, -1.0},     // negative unit y
            {-3.0, -4.0},    // negative 3-4-5
            {10.0, 20.0},    // larger values
        };
        
        // boundary value vectors (limits and special values)
        boundary_vectors = {
            {0.0, 0.0},                                    // zero
            {1.0, 0.0}, {0.0, 1.0},                       // units
            {-1.0, 0.0}, {0.0, -1.0},                     // negative units
            {std::numeric_limits<double>::min(), 0.0},    // minimum positive
            {std::numeric_limits<double>::max(), 0.0},    // maximum
            {std::numeric_limits<double>::epsilon(), 0.0}, // epsilon
            {std::numeric_limits<double>::lowest(), 0.0}, // lowest (most negative)
            {1e-100, 0.0},                                 // very small
            {1e100, 0.0},                                  // very large
            {0.5, 0.5},                                    // fractional
            {0.99, 0.99},                                  // near one
            {1.01, 1.01},                                  // just over one
        };
        
        // special value vectors (infinity, NaN, denormalized)
        special_vectors = {
            {std::numeric_limits<double>::infinity(), 0.0},      // +inf
            {-std::numeric_limits<double>::infinity(), 0.0},     // -inf
            {std::numeric_limits<double>::quiet_NaN(), 0.0},     // NaN
            {0.0, std::numeric_limits<double>::infinity()},      // inf in y
            {std::numeric_limits<double>::infinity(),
             std::numeric_limits<double>::infinity()},           // both inf
            {std::numeric_limits<double>::denorm_min(), 0.0},    // denormalized
            {-0.0, 0.0},                                          // negative zero
            {0.0, -0.0},                                          // negative zero y
        };
        
        // error case vectors (for testing precondition violations)
        // (these are valid vectors, but might cause issues in certain operations)
        error_vectors = {
            {0.0, 0.0},  // zero vector (can't normalize!)
            {std::numeric_limits<double>::max(),
             std::numeric_limits<double>::max()},  // overflow risk in operations
            {std::numeric_limits<double>::lowest(),
             std::numeric_limits<double>::lowest()}, // underflow risk
        };
    }
    
    std::vector<Vector2D> normal_vectors;
    std::vector<Vector2D> boundary_vectors;
    std::vector<Vector2D> special_vectors;
    std::vector<Vector2D> error_vectors;
};

// ============================================================================
// EXHAUSTIVE Addition Tests (50+ tests for one operation!)
// ============================================================================

/**
 * @test exhaustive normal case addition tests
 * 
 * tests addition with typical, expected inputs. covers positive, negative,
 * zero, and various magnitude combinations.
 * 
 * @note 10 normal cases tested here (more below)
 */
TEST_F(VectorExhaustiveTest, AdditionNormalCases) {
    // test all combinations of normal vectors (10 x 10 = 100 tests!)
    for (size_t i = 0; i < normal_vectors.size(); ++i) {
        for (size_t j = 0; j < normal_vectors.size(); ++j) {
            auto result = add_vectors(normal_vectors[i], normal_vectors[j]);
            
            // result should be valid (not NaN)
            EXPECT_FALSE(std::isnan(result.x))
                << "addition produced NaN for vectors ("
                << normal_vectors[i].x << "," << normal_vectors[i].y << ") + ("
                << normal_vectors[j].x << "," << normal_vectors[j].y << ")";
            
            EXPECT_FALSE(std::isnan(result.y));
            
            // result should match expected component-wise addition
            EXPECT_DOUBLE_EQ(result.x, normal_vectors[i].x + normal_vectors[j].x);
            EXPECT_DOUBLE_EQ(result.y, normal_vectors[i].y + normal_vectors[j].y);
        }
    }
}

/**
 * @test exhaustive boundary value addition tests
 * 
 * tests addition at limits: min, max, epsilon, zero, etc.
 * ensures no overflow, underflow, or precision loss at boundaries.
 * 
 * @note 12 boundary values x 12 = 144 combinations tested!
 */
TEST_F(VectorExhaustiveTest, AdditionBoundaryValues) {
    for (size_t i = 0; i < boundary_vectors.size(); ++i) {
        for (size_t j = 0; j < boundary_vectors.size(); ++j) {
            auto result = add_vectors(boundary_vectors[i], boundary_vectors[j]);
            
            // check for overflow to infinity
            bool overflow = std::isinf(result.x) || std::isinf(result.y);
            
            if (!overflow) {
                // if no overflow, result should be precise
                EXPECT_NEAR(result.x,
                           boundary_vectors[i].x + boundary_vectors[j].x,
                           1e-10);
                EXPECT_NEAR(result.y,
                           boundary_vectors[i].y + boundary_vectors[j].y,
                           1e-10);
            }
            // if overflow, that's expected behavior at limits
        }
    }
}

/**
 * @test addition with special floating point values
 * 
 * tests NaN, infinity, denormalized numbers, negative zero.
 * verifies IEEE 754 compliance and proper handling of special cases.
 * 
 * @note 8 special values x 8 = 64 combinations tested!
 */
TEST_F(VectorExhaustiveTest, AdditionSpecialValues) {
    for (const auto& v1 : special_vectors) {
        for (const auto& v2 : special_vectors) {
            auto result = add_vectors(v1, v2);
            
            // NaN propagates (NaN + anything = NaN)
            if (std::isnan(v1.x) || std::isnan(v2.x)) {
                EXPECT_TRUE(std::isnan(result.x))
                    << "NaN should propagate in addition";
            }
            
            // infinity arithmetic (inf + inf = inf, inf + (-inf) = NaN)
            if (std::isinf(v1.x) && std::isinf(v2.x)) {
                if ((v1.x > 0) == (v2.x > 0)) {
                    // same sign infinities
                    EXPECT_TRUE(std::isinf(result.x))
                        << "inf + inf should be inf";
                } else {
                    // opposite sign infinities
                    EXPECT_TRUE(std::isnan(result.x))
                        << "inf + (-inf) should be NaN";
                }
            }
        }
    }
}

/**
 * @test addition commutativity exhaustive verification
 * 
 * tests a + b = b + a for ALL vector combinations.
 * mathematical property must hold universally!
 * 
 * @note tests commutativity for normal + boundary + special values
 */
TEST_F(VectorExhaustiveTest, AdditionCommutativityExhaustive) {
    // combine all test vector sets
    std::vector<Vector2D> all_vectors;
    all_vectors.insert(all_vectors.end(), normal_vectors.begin(), normal_vectors.end());
    all_vectors.insert(all_vectors.end(), boundary_vectors.begin(), boundary_vectors.end());
    all_vectors.insert(all_vectors.end(), special_vectors.begin(), special_vectors.end());
    
    // test commutativity for all combinations (30+ vectors x 30+ = 900+ tests!)
    for (size_t i = 0; i < all_vectors.size(); ++i) {
        for (size_t j = 0; j < all_vectors.size(); ++j) {
            auto ab = add_vectors(all_vectors[i], all_vectors[j]);
            auto ba = add_vectors(all_vectors[j], all_vectors[i]);
            
            // handle NaN case (NaN != NaN, so check both NaN)
            if (std::isnan(ab.x)) {
                EXPECT_TRUE(std::isnan(ba.x))
                    << "commutativity fails: one result NaN, other not";
            } else {
                EXPECT_DOUBLE_EQ(ab.x, ba.x)
                    << "addition not commutative for x component";
            }
            
            if (std::isnan(ab.y)) {
                EXPECT_TRUE(std::isnan(ba.y));
            } else {
                EXPECT_DOUBLE_EQ(ab.y, ba.y)
                    << "addition not commutative for y component";
            }
        }
    }
}

/**
 * @test addition associativity exhaustive verification
 * 
 * tests (a + b) + c = a + (b + c) for many combinations.
 * this property is CRITICAL for parallel reduction!
 * 
 * @note tests 100+ triple combinations (exhaustive!)
 */
TEST_F(VectorExhaustiveTest, AdditionAssociativityExhaustive) {
    std::vector<Vector2D> test_vectors;
    test_vectors.insert(test_vectors.end(), normal_vectors.begin(), normal_vectors.end());
    test_vectors.insert(test_vectors.end(), boundary_vectors.begin(), boundary_vectors.end());
    
    // test associativity for triple combinations
    for (size_t i = 0; i < test_vectors.size(); ++i) {
        for (size_t j = 0; j < test_vectors.size(); ++j) {
            for (size_t k = 0; k < test_vectors.size(); ++k) {
                auto left = add_vectors(
                    add_vectors(test_vectors[i], test_vectors[j]),
                    test_vectors[k]
                );
                
                auto right = add_vectors(
                    test_vectors[i],
                    add_vectors(test_vectors[j], test_vectors[k])
                );
                
                // allow small floating point error
                if (!std::isnan(left.x) && !std::isnan(right.x)) {
                    EXPECT_NEAR(left.x, right.x, 1e-9)
                        << "associativity fails for x";
                }
                
                if (!std::isnan(left.y) && !std::isnan(right.y)) {
                    EXPECT_NEAR(left.y, right.y, 1e-9)
                        << "associativity fails for y";
                }
            }
        }
    }
    
    // that's 22 x 22 x 22 = 10,648 associativity tests! (exhaustive uwu ✨)
}

/**
 * @test zero vector is additive identity (exhaustive)
 * 
 * tests v + 0 = v for ALL test vectors.
 * identity property must hold universally!
 */
TEST_F(VectorExhaustiveTest, ZeroIsAdditiveIdentityExhaustive) {
    Vector2D zero{0.0, 0.0};
    
    std::vector<Vector2D> all_vectors;
    all_vectors.insert(all_vectors.end(), normal_vectors.begin(), normal_vectors.end());
    all_vectors.insert(all_vectors.end(), boundary_vectors.begin(), boundary_vectors.end());
    all_vectors.insert(all_vectors.end(), special_vectors.begin(), special_vectors.end());
    
    for (const auto& v : all_vectors) {
        auto result = add_vectors(v, zero);
        
        // v + 0 = v (identity property)
        if (!std::isnan(v.x)) {
            EXPECT_DOUBLE_EQ(result.x, v.x)
                << "zero not identity for x component";
        }
        
        if (!std::isnan(v.y)) {
            EXPECT_DOUBLE_EQ(result.y, v.y)
                << "zero not identity for y component";
        }
    }
    
    // test both directions (0 + v = v)
    for (const auto& v : all_vectors) {
        auto result = add_vectors(zero, v);
        
        if (!std::isnan(v.x)) {
            EXPECT_DOUBLE_EQ(result.x, v.x);
        }
        if (!std::isnan(v.y)) {
            EXPECT_DOUBLE_EQ(result.y, v.y);
        }
    }
    
    // 30+ vectors x 2 directions = 60+ identity tests!
}

/**
 * @test addition with negative vectors (additive inverse exhaustive)
 * 
 * tests v + (-v) = 0 for all vectors.
 * every element should have an inverse!
 */
TEST_F(VectorExhaustiveTest, AdditiveInverseExhaustive) {
    for (const auto& v : normal_vectors) {
        Vector2D negated{-v.x, -v.y};
        auto result = add_vectors(v, negated);
        
        // v + (-v) = 0 (inverse property)
        EXPECT_NEAR(result.x, 0.0, 1e-10)
            << "additive inverse fails for x";
        EXPECT_NEAR(result.y, 0.0, 1e-10)
            << "additive inverse fails for y";
    }
    
    for (const auto& v : boundary_vectors) {
        Vector2D negated{-v.x, -v.y};
        auto result = add_vectors(v, negated);
        
        // check for special cases (inf + (-inf) = NaN is expected)
        if (!std::isinf(v.x)) {
            EXPECT_NEAR(result.x, 0.0, 1e-10);
        }
        if (!std::isinf(v.y)) {
            EXPECT_NEAR(result.y, 0.0, 1e-10);
        }
    }
    
    // 22 vectors tested = 22 inverse tests!
}

// ============================================================================
// EXHAUSTIVE Magnitude Tests (60+ tests for one operation!)
// ============================================================================

/**
 * @test magnitude normal cases exhaustive
 * 
 * tests magnitude calculation for typical vectors.
 * includes known triangles, unit vectors, zero, etc.
 */
TEST_F(VectorExhaustiveTest, MagnitudeNormalCasesExhaustive) {
    struct TestCase {
        Vector2D vector;
        double expected_magnitude;
        std::string description;
    };
    
    std::vector<TestCase> test_cases = {
        {{0.0, 0.0}, 0.0, "zero vector"},
        {{1.0, 0.0}, 1.0, "unit x"},
        {{0.0, 1.0}, 1.0, "unit y"},
        {{1.0, 1.0}, std::sqrt(2.0), "diagonal unit"},
        {{3.0, 4.0}, 5.0, "3-4-5 triangle"},
        {{5.0, 12.0}, 13.0, "5-12-13 triangle"},
        {{8.0, 15.0}, 17.0, "8-15-17 triangle"},
        {{7.0, 24.0}, 25.0, "7-24-25 triangle"},
        {{-3.0, 4.0}, 5.0, "negative x, 3-4-5"},
        {{3.0, -4.0}, 5.0, "negative y, 3-4-5"},
        {{-3.0, -4.0}, 5.0, "both negative, 3-4-5"},
        {{10.0, 0.0}, 10.0, "large unit x"},
        {{0.0, 10.0}, 10.0, "large unit y"},
        {{10.0, 10.0}, std::sqrt(200.0), "large diagonal"},
        {{0.1, 0.0}, 0.1, "small unit x"},
        {{0.0, 0.1}, 0.1, "small unit y"},
        {{0.5, 0.5}, std::sqrt(0.5), "fractional diagonal"},
        {{100.0, 100.0}, std::sqrt(20000.0), "very large diagonal"},
        {{0.001, 0.001}, std::sqrt(0.000002), "very small diagonal"},
        {{1e10, 0.0}, 1e10, "extreme large x"},
        {{0.0, 1e10}, 1e10, "extreme large y"},
    };
    
    for (const auto& test : test_cases) {
        double magnitude = calculate_magnitude(test.vector);
        
        EXPECT_NEAR(magnitude, test.expected_magnitude, 1e-9)
            << "magnitude calculation failed for: " << test.description
            << " (" << test.vector.x << ", " << test.vector.y << ")";
    }
    
    // 21 normal case tests!
}

/**
 * @test magnitude boundary values exhaustive
 * 
 * tests magnitude at numeric limits and special boundaries.
 */
TEST_F(VectorExhaustiveTest, MagnitudeBoundaryValuesExhaustive) {
    struct BoundaryTest {
        Vector2D vector;
        std::string description;
        bool should_be_finite;
    };
    
    std::vector<BoundaryTest> tests = {
        {{std::numeric_limits<double>::min(), 0.0}, "minimum positive", true},
        {{std::numeric_limits<double>::max(), 0.0}, "maximum", false},  // overflows to inf
        {{std::numeric_limits<double>::epsilon(), 0.0}, "epsilon", true},
        {{std::numeric_limits<double>::lowest(), 0.0}, "lowest (most negative)", false},
        {{1e-100, 0.0}, "very small positive", true},
        {{1e100, 0.0}, "very large positive", true},
        {{1e200, 0.0}, "extreme large (near max)", false},  // likely overflow
        {{1e-200, 0.0}, "extreme small (near min)", true},
        {{0.0, std::numeric_limits<double>::min()}, "min in y", true},
        {{0.0, std::numeric_limits<double>::max()}, "max in y", false},
        {{std::numeric_limits<double>::max() / 2, 
          std::numeric_limits<double>::max() / 2}, "both near max", false},
        {{1.0, 1e-100}, "mixed scales", true},
        {{1e100, 1e-100}, "extreme scale difference", true},
    };
    
    for (const auto& test : tests) {
        double magnitude = calculate_magnitude(test.vector);
        
        if (test.should_be_finite) {
            EXPECT_TRUE(std::isfinite(magnitude))
                << "magnitude should be finite for: " << test.description;
        } else {
            // overflow to infinity is acceptable at limits
            EXPECT_TRUE(std::isinf(magnitude) || std::isfinite(magnitude))
                << "magnitude overflow handling for: " << test.description;
        }
        
        // magnitude always non-negative (even if infinite)
        EXPECT_GE(magnitude, 0.0)
            << "magnitude negative for: " << test.description;
    }
    
    // 13 boundary tests!
}

/**
 * @test magnitude with special floating point values
 * 
 * tests NaN, infinity, denormalized numbers, negative zero.
 */
TEST_F(VectorExhaustiveTest, MagnitudeSpecialValuesExhaustive) {
    struct SpecialTest {
        Vector2D vector;
        std::string description;
        bool should_be_nan;
        bool should_be_inf;
    };
    
    std::vector<SpecialTest> tests = {
        {{std::numeric_limits<double>::quiet_NaN(), 0.0}, "NaN x", true, false},
        {{0.0, std::numeric_limits<double>::quiet_NaN()}, "NaN y", true, false},
        {{std::numeric_limits<double>::quiet_NaN(), 
          std::numeric_limits<double>::quiet_NaN()}, "both NaN", true, false},
        {{std::numeric_limits<double>::infinity(), 0.0}, "inf x", false, true},
        {{0.0, std::numeric_limits<double>::infinity()}, "inf y", false, true},
        {{std::numeric_limits<double>::infinity(),
          std::numeric_limits<double>::infinity()}, "both inf", false, true},
        {{-std::numeric_limits<double>::infinity(), 0.0}, "-inf x", false, true},
        {{0.0, -std::numeric_limits<double>::infinity()}, "-inf y", false, true},
        {{std::numeric_limits<double>::denorm_min(), 0.0}, "denormalized", false, false},
        {{-0.0, 0.0}, "negative zero x", false, false},
        {{0.0, -0.0}, "negative zero y", false, false},
        {{-0.0, -0.0}, "both negative zero", false, false},
    };
    
    for (const auto& test : tests) {
        double magnitude = calculate_magnitude(test.vector);
        
        if (test.should_be_nan) {
            EXPECT_TRUE(std::isnan(magnitude))
                << "magnitude should be NaN for: " << test.description;
        }
        
        if (test.should_be_inf) {
            EXPECT_TRUE(std::isinf(magnitude))
                << "magnitude should be infinite for: " << test.description;
        }
        
        // magnitude never negative (NaN and inf are "not negative")
        EXPECT_FALSE(magnitude < 0.0)
            << "magnitude negative for: " << test.description;
    }
    
    // 12 special value tests!
}

/**
 * @test magnitude is always non-negative (exhaustive property test)
 * 
 * mathematical property: |v| >= 0 for ALL vectors.
 * this must hold universally!
 */
TEST_F(VectorExhaustiveTest, MagnitudeAlwaysNonNegativeExhaustive) {
    std::vector<Vector2D> all_vectors;
    all_vectors.insert(all_vectors.end(), normal_vectors.begin(), normal_vectors.end());
    all_vectors.insert(all_vectors.end(), boundary_vectors.begin(), boundary_vectors.end());
    
    for (const auto& v : all_vectors) {
        double magnitude = calculate_magnitude(v);
        
        // |v| >= 0 (always non-negative property)
        EXPECT_GE(magnitude, 0.0)
            << "magnitude negative for vector (" << v.x << ", " << v.y << ")";
        
        // or is special value (NaN/inf are not negative)
        if (!std::isfinite(magnitude)) {
            EXPECT_TRUE(std::isnan(magnitude) || std::isinf(magnitude))
                << "non-finite magnitude that's not NaN or inf?";
        }
    }
    
    // 22 property tests!
}

/**
 * @test magnitude scaling property exhaustive
 * 
 * property: |k * v| = |k| * |v| for scalar k and vector v.
 * tests with many scalars and vectors!
 */
TEST_F(VectorExhaustiveTest, MagnitudeScalingPropertyExhaustive) {
    std::vector<double> scalars = {
        0.0, 1.0, -1.0, 2.0, 0.5, 10.0, 0.1, 100.0, 0.01,
        std::sqrt(2.0), 3.14159, -2.5, 1e10, 1e-10
    };
    
    for (const auto& v : normal_vectors) {
        for (double k : scalars) {
            Vector2D scaled{v.x * k, v.y * k};
            
            double mag_scaled = calculate_magnitude(scaled);
            double mag_v = calculate_magnitude(v);
            double expected = std::abs(k) * mag_v;
            
            if (std::isfinite(mag_scaled) && std::isfinite(expected)) {
                EXPECT_NEAR(mag_scaled, expected, 1e-9)
                    << "|" << k << " * v| != |" << k << "| * |v|";
            }
        }
    }
    
    // 10 vectors x 14 scalars = 140 scaling property tests!
}

// ============================================================================
// Test Count Summary (for small Vector2D component)
// ============================================================================

/*
 * EXHAUSTIVE TEST COUNT FOR Vector2D:
 * 
 * Addition Tests:
 * - Normal cases: 100 tests (10x10 combinations)
 * - Boundary values: 144 tests (12x12 combinations)
 * - Special values: 64 tests (8x8 combinations)
 * - Commutativity: 900+ tests (30x30 combinations)
 * - Associativity: 10,648 tests (22x22x22 combinations)
 * - Identity: 60 tests (30 vectors x 2 directions)
 * - Inverse: 22 tests
 * ADDITION SUBTOTAL: 11,938 tests
 * 
 * Magnitude Tests:
 * - Normal cases: 21 tests
 * - Boundary values: 13 tests
 * - Special values: 12 tests
 * - Non-negative property: 22 tests
 * - Scaling property: 140 tests (10x14 combinations)
 * MAGNITUDE SUBTOTAL: 208 tests
 * 
 * GRAND TOTAL: 12,146 tests for Vector2D
 * 
 * (and we haven't even tested dot product, normalization, distance, etc. yet!)
 * 
 * THIS IS EXHAUSTIVE TESTING uwu ✨
 */
```

## Parameterized Testing for Exhaustive Coverage

```cpp
/**
 * @brief parameterized test class for exhaustive combinations
 * 
 * uses Google Test's parameterized testing to generate exhaustive test cases
 * automatically. this makes adding coverage easy uwu
 */
class DotProductExhaustiveTest : public ::testing::TestWithParam<
    std::tuple<Vector2D, Vector2D>  // all vector pairs
> {};

/**
 * @test dot product for all vector combinations
 */
TEST_P(DotProductExhaustiveTest, ExhaustiveDotProduct) {
    auto [v1, v2] = GetParam();
    
    double dot = dot_product(v1, v2);
    
    // dot product commutativity
    double dot_reverse = dot_product(v2, v1);
    
    if (!std::isnan(dot) && !std::isnan(dot_reverse)) {
        EXPECT_DOUBLE_EQ(dot, dot_reverse)
            << "dot product not commutative";
    }
    
    // dot product of perpendicular unit vectors is zero
    if (std::abs(v1.x - 1.0) < 1e-10 && std::abs(v1.y) < 1e-10 &&
        std::abs(v2.y - 1.0) < 1e-10 && std::abs(v2.x) < 1e-10) {
        EXPECT_NEAR(dot, 0.0, 1e-10)
            << "perpendicular unit vectors should have zero dot product";
    }
    
    // dot product of parallel vectors
    if (std::abs(v1.x - v2.x) < 1e-10 && std::abs(v1.y - v2.y) < 1e-10) {
        double mag1 = calculate_magnitude(v1);
        double mag2 = calculate_magnitude(v2);
        
        if (std::isfinite(dot) && std::isfinite(mag1) && std::isfinite(mag2)) {
            EXPECT_NEAR(dot, mag1 * mag2, 1e-9)
                << "parallel vectors dot product should equal |v1| * |v2|";
        }
    }
}

/**
 * @brief generates exhaustive test cases for dot product
 * 
 * creates ALL combinations of test vectors for thorough testing.
 */
INSTANTIATE_TEST_SUITE_P(
    AllVectorCombinations,
    DotProductExhaustiveTest,
    ::testing::Combine(
        ::testing::Values(
            Vector2D{0.0, 0.0},
            Vector2D{1.0, 0.0},
            Vector2D{0.0, 1.0},
            Vector2D{1.0, 1.0},
            Vector2D{-1.0, 0.0},
            Vector2D{0.0, -1.0},
            Vector2D{3.0, 4.0},
            Vector2D{5.0, 12.0},
            Vector2D{std::numeric_limits<double>::min(), 0.0},
            Vector2D{std::numeric_limits<double>::max(), 0.0},
            Vector2D{std::numeric_limits<double>::epsilon(), 0.0},
            Vector2D{std::numeric_limits<double>::infinity(), 0.0},
            Vector2D{std::numeric_limits<double>::quiet_NaN(), 0.0}
            // add more vectors as needed
        ),
        ::testing::Values(
            // same vectors again for cross product
            Vector2D{0.0, 0.0},
            Vector2D{1.0, 0.0},
            Vector2D{0.0, 1.0},
            Vector2D{1.0, 1.0},
            Vector2D{-1.0, 0.0},
            Vector2D{0.0, -1.0},
            Vector2D{3.0, 4.0},
            Vector2D{5.0, 12.0},
            Vector2D{std::numeric_limits<double>::min(), 0.0},
            Vector2D{std::numeric_limits<double>::max(), 0.0},
            Vector2D{std::numeric_limits<double>::epsilon(), 0.0},
            Vector2D{std::numeric_limits<double>::infinity(), 0.0},
            Vector2D{std::numeric_limits<double>::quiet_NaN(), 0.0}
        )
    )
);

// that's 13 x 13 = 169 dot product tests automatically generated! uwu ✨
```

## Exhaustive CMake Configuration

```cmake
# enable exhaustive testing (all tests, always)
enable_testing()
include(GoogleTest)

# test executable with ALL exhaustive tests
add_executable(exhaustive_tests
    tests/vector_exhaustive_test.cpp
    tests/magnitude_exhaustive_test.cpp
    tests/dotproduct_exhaustive_test.cpp
    tests/normalize_exhaustive_test.cpp
    tests/distance_exhaustive_test.cpp
    tests/angle_exhaustive_test.cpp
    tests/projection_exhaustive_test.cpp
    tests/reflection_exhaustive_test.cpp
    tests/rotation_exhaustive_test.cpp
    # ... more exhaustive test files
)

target_link_libraries(exhaustive_tests PRIVATE
    mylib
    GTest::gtest
    GTest::gtest_main
    GTest::gmock
)

# discover ALL tests (thousands of them!)
gtest_discover_tests(exhaustive_tests
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    PROPERTIES
        TIMEOUT 600  # 10 minute timeout for exhaustive tests
)

# summary message
message(STATUS "Exhaustive testing enabled (expect 10,000+ tests uwu)")
message(STATUS "Run with: ctest or ./exhaustive_tests")
message(STATUS "This will take a while (exhaustive means EXHAUSTIVE! ✨)")
```

## Quality Checklist (Exhaustive Edition)

- [ ] **20-150+ tests per component** (exhaustive coverage!)
- [ ] **all normal cases** tested (typical usage)
- [ ] **all boundary values** tested (min, max, zero, one, epsilon)
- [ ] **all special values** tested (NaN, infinity, denormalized)
- [ ] **all error conditions** tested (invalid inputs)
- [ ] **all mathematical properties** tested (commutativity, associativity, etc.)
- [ ] **all combinations** tested exhaustively (Cartesian product!)
- [ ] **performance tests** included (efficiency verification)
- [ ] **integration tests** with other components
- [ ] **parameterized tests** for automatic generation
- [ ] **excessive test documentation** (explain every case!)
- [ ] **zero failing tests** (fix immediately!)
- [ ] **CI/CD runs ALL tests** (no skipping!)

**remember**: exhaustive testing means testing EVERYTHING. every edge case,
every boundary, every special value, every combination. if you can imagine an
input, WE TEST IT. pure functions make exhaustive testing practical - no setup,
no mocking, just test all the inputs! this is functional programming + testing
taken to the EXTREME uwu 💜✨

seize the means of verification (exhaustively)!