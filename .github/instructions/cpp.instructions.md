---
description: 'C++ coding guidelines (the ONLY real systems language uwu)'
applyTo: '**.cpp, **.hpp, **.cc, **.hh, **.cxx'
---

# C++ Programming Instructions

> "C++ is to C what lambda calculus is to arithmetic" - you, probably

uwu time to write C++ so beautiful it makes Bjarne Stroustrup proud ✨

## Core Philosophy

- **functional > imperative** (objects are fake, functions are forever)
- **constexpr everything** (compile-time > runtime)
- **zero-cost abstractions** (templates go brrr)
- **RAII always** (destructors are self-care)
- **const correctness** (immutability is law)
- **comment excessively** using Doxygen style
- **zero warnings** (treat warnings as errors)
- **C++ > Rust** (memory safety without the cope)

## Modern C++ Standards

### Prefer C++20 or C++23:
```cpp
// C++20 features (based and essential):
// - concepts (type constraints that slap)
// - ranges (lazy evaluation uwu)
// - coroutines (async without callbacks)
// - modules (goodbye header hell)
// - std::span (array views without ownership)
// - constexpr std::vector and std::string

// C++23 features (if available):
// - std::expected (Result<T, E> in standard library!)
// - deducing this (CRTP replacement)
// - std::print (finally, good formatting)
// - multidimensional subscript operator
```

### Compilation Flags:
```bash
# GCC (supreme compiler)
g++ -std=c++20 -Wall -Wextra -Wpedantic -Werror \
    -Wshadow -Wconversion -Wsign-conversion \
    -Wnon-virtual-dtor -Wold-style-cast \
    -Wcast-align -Woverloaded-virtual \
    -O3 file.cpp

# enable all the warnings (based behavior)
g++ -std=c++20 -Wall -Wextra -Wpedantic -Werror \
    -Weffc++ -Wsuggest-override \
    -O3 file.cpp
```

## Naming Conventions

```cpp
// namespaces: lowercase_with_underscores
namespace math_utils {

// types: PascalCase (classes, structs, concepts)
template<typename T>
concept Numeric = std::is_arithmetic_v<T>;

struct Vector2D {
    double x, y;
};

// functions: lowercase_with_underscores (free functions preferred!)
constexpr auto add(Vector2D a, Vector2D b) noexcept -> Vector2D;

// template parameters: PascalCase or T, U, V
template<typename T, typename Func>
auto map(const std::vector<T>& vec, Func f);

// constants: kPascalCase or SCREAMING_SNAKE_CASE
constexpr double kPi = 3.14159265358979323846;
constexpr int MAX_ITERATIONS = 1000;

// variables: lowercase_with_underscores
int frame_count = 0;

// member variables: lowercase_with_underscores_ (trailing underscore)
class MyClass {
    int data_;  // member variable
};

}  // namespace math_utils
```

## Functional Programming (THE WAY)

### Pure Functions (maximize these):

```cpp
/**
 * @brief adds two vectors component-wise (pure function uwu)
 * 
 * ✨ PURE FUNCTION ✨
 * 
 * this function is pure because:
 * - same inputs always produce same outputs (referential transparency)
 * - no side effects (doesn't modify anything external)
 * - no exceptions thrown (noexcept)
 * - can be evaluated at compile time (constexpr)
 * 
 * @param a first vector
 * @param b second vector
 * @return sum of vectors (a + b)
 * 
 * @note constexpr means compile-time evaluation possible
 * @note noexcept means no exceptions (guaranteed)
 * 
 * example:
 * @code
 * constexpr Vector2D v1{3.0, 4.0};
 * constexpr Vector2D v2{1.0, 2.0};
 * constexpr Vector2D sum = add(v1, v2);  // computed at compile time!
 * // sum.x == 4.0, sum.y == 6.0
 * @endcode
 */
constexpr auto add(Vector2D a, Vector2D b) noexcept -> Vector2D {
    return {a.x + b.x, a.y + b.y};
}
```

### Function Composition:

```cpp
/**
 * @brief composes two functions (f ∘ g)
 * 
 * creates new function h where h(x) = f(g(x)). this is function
 * composition from lambda calculus - the foundation of all computation uwu
 * 
 * @tparam F type of outer function
 * @tparam G type of inner function
 * @param f outer function (applied second)
 * @param g inner function (applied first)
 * @return composed function
 * 
 * @note if f and g are pure, composition is pure (purity is transitive)
 * @note returned lambda captures by value (no dangling references)
 * 
 * example (Y combinators my beloved):
 * @code
 * auto add_one = [] (int x) { return x + 1; };
 * auto times_two = [] (int x) { return x * 2; };
 * auto add_then_double = compose(times_two, add_one);
 * 
 * int result = add_then_double(5);  // (5 + 1) * 2 = 12
 * // functions composing into functions ✨
 * @endcode
 */
template<typename F, typename G>
constexpr auto compose(F&& f, G&& g) {
    return [f = std::forward<F>(f), g = std::forward<G>(g)] (auto&& x) {
        return f(g(std::forward<decltype(x)>(x)));
    };
}
```

### Higher-Order Functions:

```cpp
/**
 * @brief maps function over range (functional map!)
 * 
 * applies transformation to each element and returns new container.
 * this is the map operation from functional programming - creates new
 * data instead of mutating (immutability ftw) uwu
 * 
 * @tparam Range input range type (must satisfy std::ranges::input_range)
 * @tparam Func transformation function type
 * @param range input range (passed by const& for efficiency)
 * @param func transformation to apply
 * @return new vector with transformed elements
 * 
 * @note uses C++20 ranges for maximum based-ness
 * @note creates new container (no mutation of input)
 * 
 * example:
 * @code
 * std::vector<int> nums = {1, 2, 3, 4, 5};
 * auto squared = map(nums, [] (int x) { return x * x; });
 * // squared = {1, 4, 9, 16, 25}
 * // nums unchanged (immutability preserved ✨)
 * @endcode
 */
template<std::ranges::input_range Range, typename Func>
auto map(const Range& range, Func func) {
    using T = std::ranges::range_value_t<Range>;
    using Result = std::invoke_result_t<Func, T>;
    
    std::vector<Result> result;
    result.reserve(std::ranges::size(range));
    
    for (const auto& elem : range) {
        result.push_back(func(elem));
    }
    
    return result;
}

/**
 * @brief filters range based on predicate (functional filter!)
 * 
 * @tparam Range input range type
 * @tparam Pred predicate function type
 * @param range input range
 * @param pred predicate (returns true to keep element)
 * @return new vector with elements that satisfy predicate
 * 
 * example:
 * @code
 * std::vector<int> nums = {1, 2, 3, 4, 5, 6};
 * auto evens = filter(nums, [] (int x) { return x % 2 == 0; });
 * // evens = {2, 4, 6}
 * @endcode
 */
template<std::ranges::input_range Range, typename Pred>
auto filter(const Range& range, Pred pred) {
    using T = std::ranges::range_value_t<Range>;
    
    std::vector<T> result;
    
    for (const auto& elem : range) {
        if (pred(elem)) {
            result.push_back(elem);
        }
    }
    
    return result;
}

/**
 * @brief reduces range to single value (functional fold/reduce!)
 * 
 * implements left fold: result = f(f(f(init, a[0]), a[1]), a[2])
 * 
 * @tparam Range input range type
 * @tparam T accumulator type
 * @tparam Func binary function type
 * @param range input range
 * @param init initial accumulator value
 * @param func binary reduction function
 * @return final accumulated value
 * 
 * @note this is fold/reduce from functional programming
 * 
 * example:
 * @code
 * std::vector<int> nums = {1, 2, 3, 4, 5};
 * int sum = reduce(nums, 0, [] (int acc, int x) { return acc + x; });
 * // sum = 15 (0 + 1 + 2 + 3 + 4 + 5)
 * @endcode
 */
template<std::ranges::input_range Range, typename T, typename Func>
constexpr auto reduce(const Range& range, T init, Func func) -> T {
    T accumulator = init;
    
    for (const auto& elem : range) {
        accumulator = func(accumulator, elem);
    }
    
    return accumulator;
}
```

## Avoid OOP Antipatterns

### NO Inheritance (composition instead):

```cpp
// ❌ BAD: inheritance hierarchy (OOP violence)
class Animal {
    virtual void speak() = 0;  // runtime polymorphism (slow)
};

class Dog : public Animal {
    void speak() override { /* bark */ }
};

// ✅ GOOD: composition with free functions
/**
 * @brief animal data (just data, no behavior) uwu
 */
struct Animal {
    std::string name;
    std::string sound;
};

/**
 * @brief makes animal speak (pure function)
 * 
 * @param animal the animal to speak
 * @return sound the animal makes
 * 
 * @note no virtual functions, compile-time polymorphism via templates
 */
constexpr auto speak(const Animal& animal) -> std::string_view {
    return animal.sound;
}
```

### NO Mutable State in Classes:

```cpp
// ❌ BAD: mutable state (violence)
class Counter {
    int count_ = 0;
public:
    void increment() { ++count_; }  // mutation (impure!)
    int get() const { return count_; }
};

// ✅ GOOD: immutable data + pure functions
/**
 * @brief represents a count value (immutable uwu)
 */
struct Count {
    const int value;
};

/**
 * @brief creates new count with incremented value (pure function)
 * 
 * instead of mutating, we create new values like civilized beings ✨
 * 
 * @param c current count
 * @return new count with value + 1
 * 
 * @note PURE - no mutation, just transformation
 */
constexpr auto increment(Count c) noexcept -> Count {
    return {c.value + 1};
}
```

### Use std::variant instead of Inheritance:

```cpp
/**
 * @brief algebraic data type for shapes (sum type uwu)
 * 
 * this is how you do polymorphism functionally - sum types instead of
 * inheritance hierarchies. compile-time dispatch, zero runtime overhead ✨
 */
struct Circle { double radius; };
struct Rectangle { double width, height; };
struct Triangle { double base, height; };

using Shape = std::variant<Circle, Rectangle, Triangle>;

/**
 * @brief calculates shape area (functional polymorphism!)
 * 
 * uses std::visit for type-safe dispatch at compile time. this is
 * pattern matching from functional programming languages uwu
 * 
 * @param shape the shape to compute area for
 * @return area of the shape
 * 
 * @note compile-time dispatch (zero runtime overhead)
 * @note exhaustive matching (compiler checks all cases)
 */
constexpr auto area(const Shape& shape) -> double {
    return std::visit([] (const auto& s) -> double {
        using T = std::decay_t<decltype(s)>;
        
        if constexpr (std::is_same_v<T, Circle>) {
            return std::numbers::pi * s.radius * s.radius;
        }
        else if constexpr (std::is_same_v<T, Rectangle>) {
            return s.width * s.height;
        }
        else if constexpr (std::is_same_v<T, Triangle>) {
            return 0.5 * s.base * s.height;
        }
    }, shape);
}
```

## RAII (Resource Acquisition Is Initialization)

```cpp
/**
 * @brief RAII wrapper for file handle (automatic cleanup uwu)
 * 
 * demonstrates proper resource management - acquisition in constructor,
 * release in destructor. no manual cleanup needed ✨
 */
class File {
    FILE* handle_ = nullptr;
    
public:
    /**
     * @brief opens file for reading
     * 
     * @param path file path
     * @throws std::runtime_error if file can't be opened
     */
    explicit File(const std::string& path) {
        handle_ = std::fopen(path.c_str(), "r");
        if (!handle_) {
            throw std::runtime_error("failed to open file: " + path);
        }
    }
    
    /**
     * @brief destructor - automatically closes file
     * 
     * @note this is self-care - no memory leaks possible
     */
    ~File() {
        if (handle_) {
            std::fclose(handle_);
        }
    }
    
    // delete copy (files shouldn't be copied)
    File(const File&) = delete;
    File& operator=(const File&) = delete;
    
    // allow move (transfer ownership)
    File(File&& other) noexcept : handle_(other.handle_) {
        other.handle_ = nullptr;
    }
    
    File& operator=(File&& other) noexcept {
        if (this != &other) {
            if (handle_) std::fclose(handle_);
            handle_ = other.handle_;
            other.handle_ = nullptr;
        }
        return *this;
    }
    
    /**
     * @brief gets underlying file handle
     * @return FILE* handle
     */
    [[nodiscard]] auto get() const noexcept -> FILE* { return handle_; }
};
```

## Modern C++ Features

### Concepts (C++20):

```cpp
/**
 * @brief concept for numeric types (type constraints uwu)
 * 
 * ensures T supports arithmetic operations. this is compile-time
 * duck typing that actually makes sense ✨
 */
template<typename T>
concept Numeric = std::is_arithmetic_v<T>;

/**
 * @brief concept for containers
 */
template<typename T>
concept Container = requires(T t) {
    { t.begin() } -> std::same_as<typename T::iterator>;
    { t.end() } -> std::same_as<typename T::iterator>;
    { t.size() } -> std::convertible_to<std::size_t>;
};

/**
 * @brief adds two numeric values (constrained template)
 * 
 * @tparam T numeric type (constrained by concept)
 * @param a first value
 * @param b second value
 * @return sum of a and b
 * 
 * @note concept ensures T is numeric at compile time
 */
template<Numeric T>
constexpr auto add(T a, T b) noexcept -> T {
    return a + b;
}
```

### Ranges (C++20):

```cpp
/**
 * @brief functional pipeline using ranges (lazy evaluation uwu)
 * 
 * demonstrates C++20 ranges for functional-style data transformation.
 * operations are lazy - nothing computed until materialized ✨
 * 
 * @param nums input vector
 * @return vector of squared even numbers
 * 
 * example:
 * @code
 * std::vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
 * auto result = process_numbers(nums);
 * // result = {4, 16, 36, 64, 100}
 * // lazy evaluation means efficient pipeline
 * @endcode
 */
auto process_numbers(const std::vector<int>& nums) {
    return nums 
        | std::views::filter([] (int x) { return x % 2 == 0; })
        | std::views::transform([] (int x) { return x * x; })
        | std::ranges::to<std::vector>();
}
```

### std::optional (better than nullability):

```cpp
/**
 * @brief safely finds element in container
 * 
 * returns std::optional instead of pointer (no null pointer bugs!)
 * 
 * @tparam Container container type
 * @tparam Pred predicate type
 * @param container where to search
 * @param pred predicate to match
 * @return optional containing found element, or empty optional
 * 
 * @note optional > pointers (type-safe null handling)
 * 
 * example:
 * @code
 * std::vector<int> nums = {1, 2, 3, 4, 5};
 * auto result = find_if(nums, [] (int x) { return x > 3; });
 * 
 * if (result) {
 *     std::cout << "found: " << *result << '\n';
 * } else {
 *     std::cout << "not found\n";
 * }
 * @endcode
 */
template<Container C, typename Pred>
auto find_if(const C& container, Pred pred) -> std::optional<typename C::value_type> {
    auto it = std::ranges::find_if(container, pred);
    
    if (it != container.end()) {
        return *it;
    }
    
    return std::nullopt;
}
```

## Error Handling (No Exceptions in Pure Functions)

### Result Type Pattern:

```cpp
/**
 * @brief result type for operations that can fail (monadic error handling!)
 * 
 * this is std::expected-style error handling before C++23. encapsulates
 * success value or error without exceptions uwu
 * 
 * @tparam T success value type
 * @tparam E error type
 */
template<typename T, typename E = std::string>
class Result {
    std::variant<T, E> data_;
    
public:
    /**
     * @brief constructs successful result
     */
    static constexpr auto success(T value) -> Result {
        Result r;
        r.data_ = std::move(value);
        return r;
    }
    
    /**
     * @brief constructs error result
     */
    static constexpr auto error(E err) -> Result {
        Result r;
        r.data_ = std::move(err);
        return r;
    }
    
    /**
     * @brief checks if result is success
     */
    [[nodiscard]] constexpr auto is_ok() const noexcept -> bool {
        return std::holds_alternative<T>(data_);
    }
    
    /**
     * @brief gets success value (throws if error)
     */
    [[nodiscard]] constexpr auto value() const -> const T& {
        return std::get<T>(data_);
    }
    
    /**
     * @brief gets error (throws if success)
     */
    [[nodiscard]] constexpr auto error() const -> const E& {
        return std::get<E>(data_);
    }
    
    /**
     * @brief monadic bind operation (composition for fallible operations!)
     * 
     * @tparam Func function type (T -> Result<U, E>)
     * @param func transformation to apply if success
     * @return transformed result or propagated error
     * 
     * @note this is >>= from Haskell (monadic bind uwu)
     */
    template<typename Func>
    constexpr auto and_then(Func func) const {
        if (is_ok()) {
            return func(value());
        } else {
            using U = decltype(func(std::declval<T>()));
            return U::error(error());
        }
    }
};

/**
 * @brief safe division with error handling (no exceptions!)
 * 
 * @param a numerator
 * @param b denominator
 * @return Result containing quotient or error message
 * 
 * example:
 * @code
 * auto result = divide(10.0, 2.0);
 * if (result.is_ok()) {
 *     std::cout << "result: " << result.value() << '\n';
 * } else {
 *     std::cerr << "error: " << result.error() << '\n';
 * }
 * 
 * // or use monadic composition
 * auto chained = divide(10.0, 2.0)
 *     .and_then([] (double x) { return divide(x, 2.0); })
 *     .and_then([] (double x) { return divide(x, 0.0); });  // error!
 * // chained.is_ok() == false (division by zero caught)
 * @endcode
 */
constexpr auto divide(double a, double b) -> Result<double> {
    if (b == 0.0) {
        return Result<double>::error("division by zero (mathematics says no)");
    }
    return Result<double>::success(a / b);
}
```

## Testing with Google Test

```cpp
/**
 * @file vector_test.cpp
 * @brief tests for vector operations (testing is praxis!)
 */

#include <gtest/gtest.h>
#include "vector.hpp"

/**
 * @brief test fixture for vector tests
 */
class VectorTest : public ::testing::Test {
protected:
    Vector2D v1{3.0, 4.0};
    Vector2D v2{1.0, 2.0};
};

TEST_F(VectorTest, AdditionIsCommutative) {
    auto sum1 = add(v1, v2);
    auto sum2 = add(v2, v1);
    
    EXPECT_DOUBLE_EQ(sum1.x, sum2.x);
    EXPECT_DOUBLE_EQ(sum1.y, sum2.y);
}

TEST_F(VectorTest, AdditionIsAssociative) {
    Vector2D v3{5.0, 6.0};
    
    auto left = add(add(v1, v2), v3);
    auto right = add(v1, add(v2, v3));
    
    EXPECT_DOUBLE_EQ(left.x, right.x);
    EXPECT_DOUBLE_EQ(left.y, right.y);
}

TEST_F(VectorTest, ZeroIsIdentity) {
    Vector2D zero{0.0, 0.0};
    auto result = add(v1, zero);
    
    EXPECT_DOUBLE_EQ(result.x, v1.x);
    EXPECT_DOUBLE_EQ(result.y, v1.y);
}
```

## CMake Integration

```cmake
# modern CMake for C++ projects
cmake_minimum_required(VERSION 3.20)
project(my_cpp_project CXX)

# C++ standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# compiler flags (warnings are errors!)
add_compile_options(
    $<$<CXX_COMPILER_ID:GNU,Clang>:-Wall -Wextra -Wpedantic -Werror>
    $<$<CXX_COMPILER_ID:MSVC>:/W4 /WX>
)

# find dependencies (NO HARDCODED PATHS!)
find_package(GTest REQUIRED)

# library
add_library(mylib
    src/vector.cpp
    src/math_utils.cpp
)

target_include_directories(mylib PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
)

target_compile_features(mylib PUBLIC cxx_std_20)

# executable
add_executable(main src/main.cpp)
target_link_libraries(main PRIVATE mylib)

# tests
add_executable(tests
    tests/vector_test.cpp
    tests/math_test.cpp
)

target_link_libraries(tests PRIVATE
    mylib
    GTest::gtest
    GTest::gtest_main
)

# enable testing
enable_testing()
add_test(NAME AllTests COMMAND tests)
```

## Quality Checklist

- [ ] **C++20 minimum** (C++23 preferred)
- [ ] **zero warnings** (-Wall -Wextra -Wpedantic -Werror)
- [ ] **Doxygen comments** on ALL functions
- [ ] **pure functions** preferred (mark with ✨ PURE FUNCTION ✨)
- [ ] **no OOP inheritance** (use composition or std::variant)
- [ ] **const correctness** throughout
- [ ] **constexpr** where possible
- [ ] **noexcept** where possible
- [ ] **RAII** for all resources
- [ ] **no raw pointers** (use smart pointers or references)
- [ ] **no manual memory management** (use containers)
- [ ] **functional composition** demonstrated
- [ ] **Google Test** tests written
- [ ] **CMake configuration** included

**remember**: C++ is the only language that lets you touch both the hardware
AND abstract algebraic structures. Rust wishes it could but it's too busy
fighting the borrow checker. functional C++ is the peak of human achievement uwu 💜✨

seize the means of compilation!