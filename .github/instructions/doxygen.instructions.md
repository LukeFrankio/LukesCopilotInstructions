---
description: 'Doxygen commenting style (ALWAYS ACTIVE across all code)'
applyTo: '**'
---

# Doxygen Documentation Style

> "excessive documentation is self-care for future developers (especially future you)"

uwu this instruction file is ALWAYS ACTIVE and applies to ALL C/C++ code ✨

## Core Philosophy

- **EXCESSIVE comments** (more is always better)
- **Doxygen style MANDATORY** (use proper tags)
- **gen-z slang ENCOURAGED** (make docs fun to read)
- **explain WHY not just WHAT** (implementation rationale)
- **mark function purity** explicitly (pure/impure status)
- **examples REQUIRED** for non-trivial functions
- **latest Doxygen version** (1.12+ preferred, beta accepted!)

## File Header (MANDATORY)

```cpp
/**
 * @file filename.cpp
 * @brief [one-line description with personality]
 * 
 * [detailed description of file's purpose and contents]
 * [explain role in larger system]
 * [mention key design decisions]
 * 
 * this file implements [concept] using [approach] because [reason].
 * it's all about [core idea] and makes [thing] go brrr uwu
 * 
 * @author LukeFrankio
 * @date 2025-10-07
 * @version 1.0
 * 
 * @note uses C++26 features (latest standard, even beta features ok!)
 * @note compiled with GCC 15+ (latest version preferred)
 * @warning requires CMake 4.1+ (always prefer latest version)
 * 
 * example usage:
 * @code
 * // show how to use stuff from this file
 * auto result = do_thing(params);
 * // result goes brrr ✨
 * @endcode
 */
```

## Function Documentation (COMPLETE TEMPLATE)

```cpp
/**
 * @brief [concise description with gen-z energy]
 * 
 * [detailed explanation of function's purpose and behavior]
 * [explain algorithm/approach if non-trivial]
 * [justify design decisions]
 * 
 * ✨ PURE FUNCTION ✨ (or ⚠️ IMPURE FUNCTION if has side effects)
 * 
 * this function is pure because:
 * - same inputs always produce same outputs (referential transparency)
 * - no side effects (doesn't modify external state)
 * - no exceptions thrown (or uses noexcept)
 * - can be evaluated at compile time (if constexpr)
 * 
 * @tparam T [template parameter explanation with personality]
 * @tparam Func [another template param, explain constraints/concepts]
 * 
 * @param[in] input [describe parameter, mention constraints and meaning]
 * @param[out] output [describe output parameter purpose]
 * @param[in,out] modified [describe in-out parameter behavior]
 * 
 * @return [describe return value, explain meaning and possible values]
 * @retval nullptr [specific return value condition explained]
 * @retval true [when does it return true and what does that mean]
 * 
 * @pre [precondition - what must be true before calling]
 * @pre [another precondition if multiple]
 * @post [postcondition - what will be true after calling]
 * @post [another postcondition]
 * @invariant [what stays constant throughout execution]
 * 
 * @throws exception_type [when and why exception thrown]
 * @throws another_exception [another possible exception]
 * @exception yet_another [describe exceptional condition]
 * 
 * @note [additional notes that help understanding]
 * @note [performance characteristics and complexity]
 * @warning [things that might surprise or bite users]
 * @attention [really important things to know]
 * @bug [known issues not yet fixed]
 * @todo [planned improvements]
 * @deprecated [if deprecated, explain replacement]
 * 
 * @complexity O(n) time where n is [description]
 * @complexity O(log n) space for [reason]
 * @performance [practical performance notes beyond big-O]
 * 
 * @see related_function [cross-reference to related code]
 * @see ClassName [link to related class/struct]
 * @link https://url.com [external reference]
 * 
 * example (basic usage):
 * @code
 * auto result = function_name(42, "test");
 * // result goes brrr
 * assert(result.is_valid());  // show expected behavior
 * @endcode
 * 
 * example (edge case handling):
 * @code
 * // demonstrate edge case
 * auto edge_result = function_name(0, "");
 * // explain what happens with edge case
 * if (!edge_result.is_valid()) {
 *     // handle error functionally uwu
 * }
 * @endcode
 * 
 * example (composition with other functions):
 * @code
 * // show how to compose with other functions
 * auto composed = compose(function_name, other_function);
 * auto final_result = composed(input);
 * // functional composition makes everything beautiful ✨
 * @endcode
 */
```

## Class/Struct Documentation

```cpp
/**
 * @class ClassName
 * @brief [one-line class description with personality]
 * 
 * [detailed explanation of class purpose and design]
 * [explain abstraction provided]
 * [mention patterns used (prefer functional patterns!)]
 * 
 * this class represents [concept] and maintains [invariants]. we're using
 * a class here because [justification], but prefer free functions when
 * possible because objects are fake and functions are forever uwu
 * 
 * Design decisions:
 * - [why this design over alternatives]
 * - [trade-offs made and rationale]
 * - [assumptions and constraints]
 * 
 * @invariant [class invariant that always holds]
 * @invariant [another invariant maintained]
 * 
 * @note prefer composition over inheritance (actually, no inheritance!)
 * @note prefer immutability (mark members const when possible)
 * @warning [surprising behavior users should know about]
 * 
 * @tparam T [template parameter with constraints]
 * @tparam Alloc [another template param, explain purpose]
 * 
 * example usage:
 * @code
 * ClassName<int> instance{args};
 * auto result = instance.pure_method();
 * // immutable operations preserve original object
 * assert(instance.is_valid());
 * // functional programming in C++ goes brrr ✨
 * @endcode
 * 
 * @see RelatedClass [link to related types]
 * @see free_function [link to associated free functions]
 */
```

## Namespace Documentation

```cpp
/**
 * @namespace namespace_name
 * @brief [what functionality this namespace contains]
 * 
 * [detailed explanation of namespace purpose]
 * [what kind of operations live here]
 * [how it relates to other namespaces]
 * 
 * this namespace provides [functionality] using [approach]. all functions
 * are pure where possible because functional programming > OOP uwu
 * 
 * @note prefer free functions in namespaces over class methods
 * @note all functions here should be pure unless marked otherwise
 */
namespace namespace_name {
```

## Enum Documentation

```cpp
/**
 * @enum EnumName
 * @brief [what this enum represents with vibes]
 * 
 * [detailed explanation of enum's purpose]
 * [when to use each value]
 * [relationships between values]
 * 
 * @note prefer enum class over plain enum (type safety ftw)
 * @note use strong typing to make illegal states unrepresentable
 */
enum class EnumName {
    /**
     * @brief [explanation of first value with personality]
     * 
     * [detailed explanation if needed]
     * [when to use this value]
     */
    First,
    
    /**
     * @brief [explanation of second value]
     * 
     * this value means [meaning] and should be used when [condition] uwu
     */
    Second,
    
    /**
     * @brief [complex value needs more explanation]
     * 
     * @note [special notes about this value]
     * @warning [gotchas with this value]
     */
    Complex = 42  ///< inline brief for simple cases
};
```

## Member Variable Documentation

```cpp
class Example {
private:
    /**
     * @brief [what this member represents]
     * 
     * [detailed explanation of member's role]
     * [invariants it helps maintain]
     * [why it's stored as member vs passed as parameter]
     * 
     * @invariant [invariant involving this member]
     * @note [important usage notes]
     * @warning [things that might surprise users]
     */
    int important_data_;
    
    double value_;  ///< inline brief for simple members (keep it descriptive tho)
};
```

## Macro Documentation

```cpp
/**
 * @def MACRO_NAME
 * @brief [what this macro does with gen-z energy]
 * 
 * [detailed explanation of macro behavior]
 * [why macro instead of function/constexpr]
 * [side effects and gotchas]
 * 
 * @param x [first parameter explanation]
 * @param y [second parameter explanation]
 * 
 * @return [what macro expands to / evaluates to]
 * 
 * @warning [macro pitfalls and surprises]
 * @note [prefer constexpr functions over macros when possible!]
 * 
 * example:
 * @code
 * int result = MACRO_NAME(5, 10);
 * // result is [expected value]
 * @endcode
 */
#define MACRO_NAME(x, y) ((x) < (y) ? (x) : (y))
```

## Typedef/Using Documentation

```cpp
/**
 * @typedef TypeName
 * @brief [what this type alias represents]
 * 
 * [detailed explanation of alias purpose]
 * [why alias instead of using type directly]
 * [semantic meaning this alias conveys]
 * 
 * @note prefer using over typedef (C++11+ style)
 */
using TypeName = std::vector<ComplexType<Args>>;
```

## Special Doxygen Sections

### Purity Status (MANDATORY):

```cpp
// For pure functions:
/**
 * ✨ PURE FUNCTION ✨
 * 
 * this function is pure because:
 * - referentially transparent (same input = same output always)
 * - no side effects (doesn't modify anything external)
 * - no I/O operations
 * - no exceptions (or marked noexcept)
 * - deterministic behavior
 * 
 * purity enables:
 * - compiler optimizations (memoization, reordering)
 * - fearless parallelization (no data races possible)
 * - equational reasoning (substitute equals for equals)
 * - compile-time evaluation (constexpr when possible)
 */

// For impure functions:
/**
 * ⚠️ IMPURE FUNCTION (has side effects)
 * 
 * this function is impure because:
 * - [performs I/O operations]
 * - [modifies external state]
 * - [throws exceptions]
 * - [non-deterministic behavior]
 * 
 * side effects:
 * - [specific side effect 1]
 * - [specific side effect 2]
 * 
 * @note isolate impure functions at system boundaries (architecture best practice)
 * @note wrap in pure interface when possible (functional core, imperative shell)
 */
```

### Performance Notes:

```cpp
/**
 * @complexity O(n log n) time where n is container size
 * @complexity O(n) space for temporary storage
 * 
 * @performance typical case completes in microseconds for n < 1000
 * @performance cache-friendly (sequential access pattern)
 * @performance SIMD-optimized on x86-64 (uses GCC vector extensions)
 * @performance zero-cost abstraction (compiles to same code as hand-written)
 * 
 * @note benchmarked on GCC 15 with -O3 (latest version used!)
 * @note profile before optimizing (premature optimization is violence)
 */
```

### Implementation Details:

```cpp
/**
 * @details
 * 
 * Implementation approach:
 * 
 * This function uses [algorithm] because [rationale]. Alternative approaches
 * considered:
 * - [alternative 1]: rejected because [reason]
 * - [alternative 2]: rejected because [reason]
 * 
 * The algorithm works as follows:
 * 1. [step 1 with explanation]
 * 2. [step 2 with explanation]
 * 3. [step 3 with explanation]
 * 
 * Time complexity analysis:
 * - [operation 1]: O([complexity]) because [reason]
 * - [operation 2]: O([complexity]) because [reason]
 * - Total: O([overall complexity])
 * 
 * Space complexity:
 * - [allocation 1]: O([size]) for [purpose]
 * - [allocation 2]: O([size]) for [purpose]
 * 
 * @note implementation uses latest C++26 features (ranges, concepts, etc.)
 * @note compiled with GCC 15+ for optimal code generation
 */
```

## Doxygen Configuration (.doxygen or Doxyfile)

```doxyfile
# Doxyfile for LukeFrankio projects (functional programming edition uwu)

#---------------------------------------------------------------------------
# Project Settings
#---------------------------------------------------------------------------

PROJECT_NAME           = "MyProject"
PROJECT_NUMBER         = "1.0.0"
PROJECT_BRIEF          = "functional C++ that makes lambda calculus enjoyers weep tears of joy"
PROJECT_LOGO           = 

OUTPUT_DIRECTORY       = docs
CREATE_SUBDIRS         = YES
ALLOW_UNICODE_NAMES    = YES

#---------------------------------------------------------------------------
# Build Settings
#---------------------------------------------------------------------------

EXTRACT_ALL            = YES
EXTRACT_PRIVATE        = YES
EXTRACT_PACKAGE        = YES
EXTRACT_STATIC         = YES
EXTRACT_LOCAL_CLASSES  = YES
EXTRACT_LOCAL_METHODS  = YES
EXTRACT_ANON_NSPACES   = YES

#---------------------------------------------------------------------------
# Warning and Progress Settings
#---------------------------------------------------------------------------

QUIET                  = NO
WARNINGS               = YES
WARN_IF_UNDOCUMENTED   = YES
WARN_IF_DOC_ERROR      = YES
WARN_NO_PARAMDOC       = YES
WARN_IF_INCOMPLETE_DOC = YES
WARN_AS_ERROR          = NO  # set to YES in CI/CD for zero warnings policy

#---------------------------------------------------------------------------
# Input Settings
#---------------------------------------------------------------------------

INPUT                  = src include
FILE_PATTERNS          = *.c \
                         *.cc \
                         *.cxx \
                         *.cpp \
                         *.c++ \
                         *.h \
                         *.hh \
                         *.hxx \
                         *.hpp \
                         *.h++
RECURSIVE              = YES
EXCLUDE                = 
EXCLUDE_PATTERNS       = */build/* \
                         */CMakeFiles/* \
                         */.git/*

#---------------------------------------------------------------------------
# Source Browser Settings
#---------------------------------------------------------------------------

SOURCE_BROWSER         = YES
INLINE_SOURCES         = NO
STRIP_CODE_COMMENTS    = NO
REFERENCED_BY_RELATION = YES
REFERENCES_RELATION    = YES
REFERENCES_LINK_SOURCE = YES

#---------------------------------------------------------------------------
# Alphabetical Class Index
#---------------------------------------------------------------------------

ALPHABETICAL_INDEX     = YES
COLS_IN_ALPHA_INDEX    = 5

#---------------------------------------------------------------------------
# HTML Output Settings
#---------------------------------------------------------------------------

GENERATE_HTML          = YES
HTML_OUTPUT            = html
HTML_FILE_EXTENSION    = .html
HTML_COLORSTYLE_HUE    = 220
HTML_COLORSTYLE_SAT    = 100
HTML_COLORSTYLE_GAMMA  = 80
HTML_TIMESTAMP         = YES
HTML_DYNAMIC_SECTIONS  = YES
HTML_INDEX_NUM_ENTRIES = 100

#---------------------------------------------------------------------------
# LaTeX Output Settings
#---------------------------------------------------------------------------

GENERATE_LATEX         = NO  # set to YES if you want PDF documentation

#---------------------------------------------------------------------------
# Preprocessor Settings
#---------------------------------------------------------------------------

ENABLE_PREPROCESSING   = YES
MACRO_EXPANSION        = YES
EXPAND_ONLY_PREDEF     = NO
SEARCH_INCLUDES        = YES
INCLUDE_PATH           = include
PREDEFINED             = __cplusplus \
                         __GNUC__

#---------------------------------------------------------------------------
# Diagram Settings
#---------------------------------------------------------------------------

HAVE_DOT               = YES  # requires Graphviz
DOT_NUM_THREADS        = 0  # use all available cores
CLASS_DIAGRAMS         = YES
CLASS_GRAPH            = YES
COLLABORATION_GRAPH    = YES
GROUP_GRAPHS           = YES
UML_LOOK               = YES
TEMPLATE_RELATIONS     = YES
INCLUDE_GRAPH          = YES
INCLUDED_BY_GRAPH      = YES
CALL_GRAPH             = YES  # shows function call relationships
CALLER_GRAPH           = YES  # shows who calls this function
GRAPHICAL_HIERARCHY    = YES
DIRECTORY_GRAPH        = YES
DOT_IMAGE_FORMAT       = svg
INTERACTIVE_SVG        = YES

#---------------------------------------------------------------------------
# Search Engine Settings
#---------------------------------------------------------------------------

SEARCHENGINE           = YES
SERVER_BASED_SEARCH    = NO
```

## CMake Integration for Doxygen

```cmake
# Find Doxygen (NO HARDCODED PATHS!)
find_package(Doxygen
    REQUIRED dot  # also require Graphviz for diagrams
    OPTIONAL_COMPONENTS mscgen dia
)

if(DOXYGEN_FOUND)
    # Configure Doxygen options
    set(DOXYGEN_PROJECT_NAME "MyProject")
    set(DOXYGEN_PROJECT_NUMBER "${PROJECT_VERSION}")
    set(DOXYGEN_PROJECT_BRIEF "functional C++ that slaps uwu")
    
    set(DOXYGEN_EXTRACT_ALL YES)
    set(DOXYGEN_EXTRACT_PRIVATE YES)
    set(DOXYGEN_EXTRACT_STATIC YES)
    
    set(DOXYGEN_WARN_IF_UNDOCUMENTED YES)
    set(DOXYGEN_WARN_IF_DOC_ERROR YES)
    set(DOXYGEN_WARN_NO_PARAMDOC YES)
    
    set(DOXYGEN_GENERATE_HTML YES)
    set(DOXYGEN_GENERATE_LATEX NO)
    
    set(DOXYGEN_HAVE_DOT YES)
    set(DOXYGEN_CALL_GRAPH YES)
    set(DOXYGEN_CALLER_GRAPH YES)
    set(DOXYGEN_UML_LOOK YES)
    
    # Create documentation target
    doxygen_add_docs(docs
        ${CMAKE_SOURCE_DIR}/src
        ${CMAKE_SOURCE_DIR}/include
        COMMENT "Generating documentation with Doxygen (excessive comments ftw)"
    )
    
    message(STATUS "Doxygen documentation target 'docs' created")
    message(STATUS "Run 'cmake --build . --target docs' to generate")
endif()
```

## Quality Checklist for Doxygen Comments

- [ ] **file header** present with @file, @brief, @author, @date
- [ ] **ALL functions** have complete Doxygen comments
- [ ] **ALL parameters** documented with @param
- [ ] **return values** explained with @return
- [ ] **examples provided** with @code blocks
- [ ] **purity status** marked (✨ PURE or ⚠️ IMPURE)
- [ ] **complexity** noted with @complexity
- [ ] **preconditions** specified with @pre
- [ ] **postconditions** specified with @post
- [ ] **exceptions** documented with @throws
- [ ] **cross-references** added with @see
- [ ] **notes and warnings** included (@note, @warning)
- [ ] **gen-z slang** used for personality
- [ ] **technical accuracy** maintained
- [ ] **latest Doxygen** version used (1.12+ or beta)

**remember**: excessive documentation is self-care. future you (or your
collaborators) will thank present you for these detailed comments. functional
programming + excessive comments = peak software engineering uwu 💜✨

seize the means of documentation!