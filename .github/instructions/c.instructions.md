---
description: 'C language coding guidelines (the foundation before C++ uwu)'
applyTo: '**/*.c, **/*.h'
---

# C Programming Instructions

> "C is the assembly language of high-level languages" - someone wise probably

uwu time to write C that's so clean it could be in the Linux kernel ✨

## Core Philosophy

- **explicit > implicit** (say what you mean)
- **simple > complex** (keep it understandable)
- **functional style** where possible (even in C!)
- **comment excessively** using Doxygen style
- **zero warnings** policy (warnings are errors)
- **portable** code (avoid platform-specific unless necessary)

## General C Guidelines

### Modern C Standards:
- prefer **C17/C18** (or C23 if available)
- avoid ancient C89/C90 unless required
- use `_Bool` or `<stdbool.h>` for booleans
- use `<stdint.h>` for fixed-width integers
- use `<stddef.h>` for `size_t`, `ptrdiff_t`

### Compilation:
```bash
# compile with ALL warnings
gcc -std=c17 -Wall -Wextra -Wpedantic -Werror -O2 file.c

# or with more warnings (recommended)
gcc -std=c17 -Wall -Wextra -Wpedantic -Werror \
    -Wshadow -Wconversion -Wdouble-promotion \
    -Wformat=2 -Wstrict-prototypes -O2 file.c
```

## Code Style and Formatting

### Naming Conventions:

```c
// types: PascalCase or lowercase_with_underscores
typedef struct Vector2D {
    double x;
    double y;
} Vector2D;

// functions: lowercase_with_underscores
int calculate_distance(int x, int y);

// variables: lowercase_with_underscores
int frame_count = 0;

// constants: UPPERCASE_WITH_UNDERSCORES
#define MAX_BUFFER_SIZE 1024
const int WINDOW_WIDTH = 800;

// macros: UPPERCASE_WITH_UNDERSCORES
#define MIN(a, b) ((a) < (b) ? (a) : (b))

// enums: PascalCase or UPPERCASE
typedef enum {
    COLOR_RED,
    COLOR_GREEN,
    COLOR_BLUE
} Color;
```

### Header Files:

```c
/**
 * @file vector.h
 * @brief vector mathematics library (pure functions ftw)
 * 
 * provides 2D vector operations using functional style - all functions
 * are pure and take vectors by value or const pointer uwu
 * 
 * @author LukeFrankio
 * @date 2025-10-07
 */

#ifndef VECTOR_H
#define VECTOR_H

#include <stddef.h>
#include <stdbool.h>

/**
 * @brief 2D vector with double precision
 * 
 * represents a point or direction in 2D space. immutability is
 * encouraged - create new vectors instead of modifying existing ones ✨
 */
typedef struct {
    double x;  /**< x coordinate (horizontal) */
    double y;  /**< y coordinate (vertical) */
} Vector2D;

/**
 * @brief adds two vectors component-wise (pure function uwu)
 * 
 * @param a first vector
 * @param b second vector
 * @return sum of vectors (a + b)
 * 
 * @note this is a PURE function - no side effects, deterministic
 */
Vector2D vector_add(Vector2D a, Vector2D b);

#endif  // VECTOR_H
```

### Implementation Files:

```c
/**
 * @file vector.c
 * @brief implementation of vector operations
 */

#include "vector.h"
#include <math.h>

/**
 * @brief adds two vectors component-wise
 * 
 * performs element-wise addition: result.x = a.x + b.x, result.y = a.y + b.y
 * 
 * this function is PURE:
 * - no side effects (doesn't modify inputs)
 * - deterministic (same inputs always give same output)
 * - no global state dependencies
 * 
 * @param a first vector
 * @param b second vector
 * @return new vector containing component-wise sum
 * 
 * @note creates new vector (functional style, immutability uwu)
 * 
 * example:
 * @code
 * Vector2D v1 = {3.0, 4.0};
 * Vector2D v2 = {1.0, 2.0};
 * Vector2D result = vector_add(v1, v2);
 * // result.x == 4.0, result.y == 6.0
 * // v1 and v2 unchanged (immutability preserved ✨)
 * @endcode
 */
Vector2D vector_add(Vector2D a, Vector2D b) {
    Vector2D result;
    result.x = a.x + b.x;
    result.y = a.y + b.y;
    return result;  // return by value (functional style)
}
```

## Functional Programming in C

### Pure Functions (maximize these):

```c
/**
 * @brief calculates factorial recursively (pure function)
 * 
 * ✨ PURE FUNCTION ✨
 * 
 * @param n non-negative integer
 * @return n! (factorial of n)
 * 
 * @pre n >= 0 (negative inputs undefined)
 * @warning may overflow for large n (use caution)
 */
unsigned long factorial(unsigned int n) {
    return (n == 0) ? 1 : n * factorial(n - 1);
}

/**
 * @brief maps function over array elements (functional map!)
 * 
 * applies transform to each element of src array and stores result
 * in dst array. this is the map operation from functional programming uwu
 * 
 * @param src source array (not modified - const)
 * @param dst destination array (stores results)
 * @param count number of elements
 * @param transform function to apply to each element
 * 
 * @pre src and dst must not overlap (or use memmove semantics)
 * @pre count must be <= actual array sizes
 * @post dst[i] = transform(src[i]) for all i in [0, count)
 * 
 * @note dst can be same as src if in-place transformation desired
 */
void array_map(const int* src, int* dst, size_t count, 
               int (*transform)(int)) {
    for (size_t i = 0; i < count; i++) {
        dst[i] = transform(src[i]);
    }
}

/**
 * @brief reduces array to single value (functional fold!)
 * 
 * implements left fold: result = f(f(f(init, a[0]), a[1]), a[2])
 * 
 * @param array source array
 * @param count number of elements
 * @param init initial accumulator value
 * @param reducer binary function (accumulator, element) -> new accumulator
 * @return final accumulated value
 * 
 * @note this is fold (reduce) from functional programming ✨
 */
int array_reduce(const int* array, size_t count, int init,
                 int (*reducer)(int, int)) {
    int accumulator = init;
    for (size_t i = 0; i < count; i++) {
        accumulator = reducer(accumulator, array[i]);
    }
    return accumulator;
}
```

### Avoid Global State:

```c
// ❌ BAD: global mutable state (violence)
static int counter = 0;

int bad_increment(void) {
    return ++counter;  // impure! depends on external state
}

// ✅ GOOD: pass state explicitly (functional style)
/**
 * @brief increments counter value (pure function uwu)
 * 
 * @param current current counter value
 * @return incremented value (current + 1)
 * 
 * @note PURE - no global state, just transformation
 */
int good_increment(int current) {
    return current + 1;  // pure! explicit state
}
```

## Memory Management

### Stack Allocation (prefer this):

```c
/**
 * @brief processes data using stack allocation (fast and safe)
 * 
 * uses stack for temporary data - automatic cleanup, no memory leaks
 * possible. this is the most efficient allocation strategy uwu
 * 
 * @param size amount of data to process
 * @return processing result
 * 
 * @warning size must be reasonable for stack (typically < 1MB)
 * @note stack allocation = automatic RAII in C ✨
 */
int process_data(size_t size) {
    // stack allocated array (automatic cleanup)
    if (size > 1024) return -1;  // too big for stack
    
    int buffer[1024];  // automatic storage duration
    // use buffer...
    
    return 0;  // buffer automatically freed here
}
```

### Heap Allocation (when necessary):

```c
#include <stdlib.h>

/**
 * @brief creates dynamic array (caller must free!)
 * 
 * allocates array on heap. CALLER RESPONSIBLE FOR FREEING with free().
 * 
 * @param count number of elements
 * @return pointer to allocated array, NULL on failure
 * 
 * @warning CALLER MUST CALL free() on returned pointer
 * @note always check for NULL before using returned pointer
 * 
 * example usage:
 * @code
 * int* array = create_array(100);
 * if (array != NULL) {
 *     // use array...
 *     free(array);  // MANDATORY cleanup
 * }
 * @endcode
 */
int* create_array(size_t count) {
    // use calloc (initializes to zero, safer than malloc)
    int* array = calloc(count, sizeof(int));
    if (array == NULL) {
        // allocation failed (out of memory?)
        return NULL;
    }
    return array;
}

/**
 * @brief safely frees pointer and sets to NULL
 * 
 * macro to prevent use-after-free bugs by NULLing pointer after free
 * 
 * @param ptr pointer to free (will be set to NULL)
 * 
 * @note idempotent (safe to call multiple times)
 */
#define SAFE_FREE(ptr) do { \
    free(ptr);              \
    (ptr) = NULL;           \
} while (0)
```

### RAII Pattern in C:

```c
/**
 * @brief FILE* wrapper with automatic cleanup (RAII in C!)
 * 
 * demonstrates RAII pattern in C using cleanup attribute or macros
 */

// GCC/Clang cleanup attribute (automatic destruction)
#ifdef __GNUC__
    #define AUTO_CLEANUP(func) __attribute__((cleanup(func)))
#else
    #define AUTO_CLEANUP(func)
#endif

/**
 * @brief closes FILE* automatically (cleanup function)
 */
static inline void close_file(FILE** fp) {
    if (fp != NULL && *fp != NULL) {
        fclose(*fp);
        *fp = NULL;
    }
}

/**
 * @brief reads file with automatic cleanup (RAII vibes ✨)
 * 
 * uses cleanup attribute for automatic resource management
 * 
 * @param filename path to file
 * @return 0 on success, -1 on failure
 */
int read_file_auto(const char* filename) {
    // FILE* automatically closed when going out of scope
    AUTO_CLEANUP(close_file) FILE* file = fopen(filename, "r");
    
    if (file == NULL) {
        return -1;  // fopen failed
    }
    
    // use file...
    
    return 0;  // file automatically closed here (RAII magic)
}
```

## Error Handling

### Return Codes:

```c
/**
 * @brief result type for operations that can fail
 * 
 * encapsulates success/failure with optional error code
 */
typedef struct {
    bool success;      /**< true if operation succeeded */
    int error_code;    /**< error code if failed (errno-like) */
} Result;

/**
 * @brief safe division with error handling
 * 
 * @param numerator dividend
 * @param denominator divisor
 * @param[out] result pointer to store result (if successful)
 * @return Result indicating success/failure
 * 
 * @pre result must not be NULL
 * @post if success, *result contains quotient
 * 
 * example:
 * @code
 * double quotient;
 * Result res = safe_divide(10.0, 2.0, &quotient);
 * if (res.success) {
 *     printf("Result: %f\n", quotient);
 * } else {
 *     fprintf(stderr, "Error: %d\n", res.error_code);
 * }
 * @endcode
 */
Result safe_divide(double numerator, double denominator, double* result) {
    if (result == NULL) {
        return (Result){.success = false, .error_code = EINVAL};
    }
    
    if (denominator == 0.0) {
        return (Result){.success = false, .error_code = EDOM};
    }
    
    *result = numerator / denominator;
    return (Result){.success = true, .error_code = 0};
}
```

### Assertions:

```c
#include <assert.h>

/**
 * @brief processes buffer with validation
 * 
 * @param buffer data buffer (must not be NULL)
 * @param size buffer size (must be > 0)
 * 
 * @pre buffer != NULL
 * @pre size > 0
 */
void process_buffer(const char* buffer, size_t size) {
    // precondition checks (removed in release builds)
    assert(buffer != NULL);
    assert(size > 0);
    
    // process buffer...
}
```

## Doxygen Documentation (MANDATORY)

### Complete Function Documentation:

```c
/**
 * @brief computes distance between two 2D points
 * 
 * calculates Euclidean distance using Pythagorean theorem:
 * distance = sqrt((x2-x1)² + (y2-y1)²)
 * 
 * this is a PURE function - deterministic, no side effects uwu
 * 
 * @param p1 first point
 * @param p2 second point
 * @return distance between points (always non-negative)
 * 
 * @note uses sqrt from math.h (link with -lm)
 * @note returns 0.0 if points are identical
 * 
 * @complexity O(1) time, O(1) space
 * 
 * example:
 * @code
 * Vector2D a = {0.0, 0.0};
 * Vector2D b = {3.0, 4.0};
 * double dist = vector_distance(a, b);
 * // dist == 5.0 (3-4-5 triangle uwu)
 * @endcode
 */
double vector_distance(Vector2D p1, Vector2D p2) {
    double dx = p2.x - p1.x;
    double dy = p2.y - p1.y;
    return sqrt(dx * dx + dy * dy);
}
```

## Common Pitfalls to Avoid

### Buffer Overflows:

```c
// ❌ BAD: no bounds checking (undefined behavior)
void bad_copy(char* dst, const char* src) {
    strcpy(dst, src);  // buffer overflow waiting to happen
}

// ✅ GOOD: use safe functions with bounds
/**
 * @brief safely copies string with bounds checking
 * 
 * @param dst destination buffer
 * @param dst_size size of destination buffer
 * @param src source string (null-terminated)
 * @return true if copied successfully, false if truncated
 */
bool safe_copy(char* dst, size_t dst_size, const char* src) {
    if (dst == NULL || src == NULL || dst_size == 0) {
        return false;
    }
    
    strncpy(dst, src, dst_size - 1);
    dst[dst_size - 1] = '\0';  // ensure null termination
    
    return (strlen(src) < dst_size);  // false if truncated
}
```

### Integer Overflow:

```c
#include <limits.h>

/**
 * @brief safe integer addition with overflow detection
 * 
 * @param a first operand
 * @param b second operand
 * @param[out] result pointer to store sum (if no overflow)
 * @return true if addition safe, false if overflow would occur
 */
bool safe_add(int a, int b, int* result) {
    if (result == NULL) return false;
    
    // check for overflow before performing operation
    if (b > 0 && a > INT_MAX - b) {
        return false;  // would overflow
    }
    if (b < 0 && a < INT_MIN - b) {
        return false;  // would underflow
    }
    
    *result = a + b;
    return true;
}
```

### Uninitialized Variables:

```c
// ❌ BAD: uninitialized variable (undefined behavior)
void bad_function(void) {
    int value;  // uninitialized (contains garbage)
    printf("%d\n", value);  // undefined behavior
}

// ✅ GOOD: always initialize variables
void good_function(void) {
    int value = 0;  // explicitly initialized
    printf("%d\n", value);  // defined behavior (prints 0)
}
```

## Testing (use Google Test for C via extern "C")

```c
// in header file (vector.h)
#ifdef __cplusplus
extern "C" {
#endif

Vector2D vector_add(Vector2D a, Vector2D b);

#ifdef __cplusplus
}
#endif
```

```cpp
// in test file (vector_test.cpp)
#include <gtest/gtest.h>

extern "C" {
#include "vector.h"
}

TEST(VectorTest, AdditionWorks) {
    Vector2D a = {3.0, 4.0};
    Vector2D b = {1.0, 2.0};
    Vector2D result = vector_add(a, b);
    
    EXPECT_DOUBLE_EQ(result.x, 4.0);
    EXPECT_DOUBLE_EQ(result.y, 6.0);
}
```

## CMake Integration

```cmake
# modern CMake for C projects
cmake_minimum_required(VERSION 3.20)
project(my_c_project C)

# C standard
set(CMAKE_C_STANDARD 17)
set(CMAKE_C_STANDARD_REQUIRED ON)

# warning flags (treat warnings as errors)
add_compile_options(
    -Wall
    -Wextra
    -Wpedantic
    -Werror
    -Wshadow
    -Wconversion
)

# library
add_library(mylib
    src/vector.c
    src/math_utils.c
)

target_include_directories(mylib PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)

# link math library
target_link_libraries(mylib PRIVATE m)

# executable
add_executable(main src/main.c)
target_link_libraries(main PRIVATE mylib)
```

## Quality Checklist

- [ ] **C17 standard** used
- [ ] **zero warnings** (compiled with -Wall -Wextra -Wpedantic -Werror)
- [ ] **Doxygen comments** on all functions
- [ ] **pure functions** preferred
- [ ] **no global mutable state**
- [ ] **memory leaks** checked (valgrind)
- [ ] **buffer overflows** prevented
- [ ] **null checks** on pointers
- [ ] **error handling** implemented
- [ ] **assertions** for preconditions
- [ ] **tests** written (gtest via extern C)

**remember**: C is simple but not easy. write explicit, well-documented code
and future you will be grateful. functional style in C is possible and
based uwu 💜✨