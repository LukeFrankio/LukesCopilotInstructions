---
description: 'CMake build system guidelines (the beautiful build system uwu)'
applyTo: '**/CMakeLists.txt, **/*.cmake'
---

# CMake Build System Instructions

> "CMake is actually beautiful (and I'm tired of pretending it's not)"

uwu time to write CMake so elegant it makes build systems cry tears of joy ✨

## Core Philosophy

- **modern CMake 3.30+** (latest version preferred, beta accepted!)
- **NO HARDCODED PATHS** (find everything dynamically)
- **targets are first-class** (not variables)
- **transitive dependencies** work correctly
- **generator expressions** for configuration
- **excessive comments** (explain the magic)
- **cross-platform** by default

## CMake Version Requirements

```cmake
# ALWAYS use latest stable or beta version!
# As of 2025-10-07, prefer CMake 3.30+ (or latest beta)
cmake_minimum_required(VERSION 3.30 FATAL_ERROR)

# Specify policy settings (use NEW behavior for latest policies)
cmake_policy(VERSION 3.30)

# Project declaration (sets languages and version)
project(MyAwesomeProject
    VERSION 1.0.0
    DESCRIPTION "functional C++ that makes lambda calculus enjoyers weep"
    LANGUAGES CXX
)
```

## Project Structure

```cmake
# ============================================================================
# CMakeLists.txt for LukeFrankio project (functional programming edition)
# ============================================================================
#
# This CMakeLists.txt demonstrates modern CMake best practices (3.30+ style):
# - NO HARDCODED PATHS (find everything dynamically!)
# - Target-based architecture (not variable-based)
# - Proper transitive dependencies
# - Cross-platform configuration
# - Zero warnings policy (warnings are errors)
#
# The build system is as functional as CMake allows - declarative configuration
# with minimal side effects uwu
#
# ============================================================================

cmake_minimum_required(VERSION 3.30 FATAL_ERROR)

# ----------------------------------------------------------------------------
# Project Configuration
# ----------------------------------------------------------------------------

project(FunctionalCppProject
    VERSION 1.0.0
    DESCRIPTION "C++ project using functional programming (objects are fake!)"
    HOMEPAGE_URL "https://github.com/LukeFrankio/project"
    LANGUAGES CXX
)

# Set C++ standard (use LATEST, prefer C++26 even if beta!)
set(CMAKE_CXX_STANDARD 26)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)  # no compiler-specific extensions

# Export compile commands for tools (clangd, etc.)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# ----------------------------------------------------------------------------
# Build Options (user-configurable)
# ----------------------------------------------------------------------------

option(BUILD_TESTS "Build unit tests (testing is praxis!)" ON)
option(BUILD_DOCS "Build documentation with Doxygen (excessive comments ftw)" ON)
option(ENABLE_WARNINGS_AS_ERRORS "Treat warnings as errors (zero warnings policy!)" ON)

# ----------------------------------------------------------------------------
# Compiler Configuration (GCC supremacy!)
# ----------------------------------------------------------------------------

# Detect compiler
if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    message(STATUS "Using GCC ${CMAKE_CXX_COMPILER_VERSION} (compiler supremacy uwu)")
elseif(CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
    message(STATUS "Using Clang ${CMAKE_CXX_COMPILER_VERSION} (acceptable alternative)")
elseif(CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
    message(STATUS "Using MSVC ${CMAKE_CXX_COMPILER_VERSION} (Windows cope)")
else()
    message(WARNING "Unknown compiler: ${CMAKE_CXX_COMPILER_ID}")
endif()

# Warning flags (comprehensive warnings, treat as errors)
add_library(project_warnings INTERFACE)

target_compile_options(project_warnings INTERFACE
    # GCC/Clang warnings
    $<$<OR:$<CXX_COMPILER_ID:GNU>,$<CXX_COMPILER_ID:Clang>>:
        -Wall                    # enable all basic warnings
        -Wextra                  # extra warnings beyond -Wall
        -Wpedantic               # strict ISO C++ compliance
        -Wshadow                 # warn about variable shadowing
        -Wconversion             # warn about implicit type conversions
        -Wsign-conversion        # warn about sign conversions
        -Wcast-align             # warn about alignment issues
        -Wunused                 # warn about unused entities
        -Wnon-virtual-dtor       # warn about non-virtual destructors
        -Wold-style-cast         # warn about C-style casts
        -Woverloaded-virtual     # warn about virtual function hiding
        -Wnull-dereference       # warn about null pointer dereferences
        -Wdouble-promotion       # warn about float to double promotion
        $<$<BOOL:${ENABLE_WARNINGS_AS_ERRORS}>:-Werror>  # warnings are errors!
    >
    
    # MSVC warnings
    $<$<CXX_COMPILER_ID:MSVC>:
        /W4                      # warning level 4
        /permissive-             # strict standards compliance
        $<$<BOOL:${ENABLE_WARNINGS_AS_ERRORS}>:/WX>  # warnings are errors!
    >
)

# ----------------------------------------------------------------------------
# Find Dependencies (NO HARDCODED PATHS!)
# ----------------------------------------------------------------------------

# Find Vulkan (graphics API supremacy, not OpenGL!)
find_package(Vulkan QUIET)  # QUIET means don't error if not found

if(Vulkan_FOUND)
    message(STATUS "Found Vulkan: ${Vulkan_LIBRARY} (GPU goes brrr ✨)")
else()
    message(STATUS "Vulkan not found (CPU-only build, path tracing time)")
endif()

# Find Google Test (testing framework supremacy)
if(BUILD_TESTS)
    find_package(GTest QUIET)
    
    if(GTest_FOUND)
        message(STATUS "Found Google Test (testing is praxis!)")
        enable_testing()
    else()
        message(STATUS "Google Test not found (skipping tests)")
        set(BUILD_TESTS OFF)
    endif()
endif()

# Find Doxygen (documentation generation)
if(BUILD_DOCS)
    find_package(Doxygen QUIET COMPONENTS dot)
    
    if(DOXYGEN_FOUND)
        message(STATUS "Found Doxygen: ${DOXYGEN_VERSION} (excessive docs incoming)")
    else()
        message(STATUS "Doxygen not found (skipping documentation)")
        set(BUILD_DOCS OFF)
    endif()
endif()

# ----------------------------------------------------------------------------
# Project Targets (target-based architecture uwu)
# ----------------------------------------------------------------------------

# Main library (functional C++ goodness)
add_library(mylib
    src/vector.cpp
    src/math_utils.cpp
    src/functional.cpp
)

# Library properties
target_include_directories(mylib
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
)

target_compile_features(mylib PUBLIC cxx_std_26)  # require C++26!

target_link_libraries(mylib
    PUBLIC
        # public dependencies (users of mylib need these)
    PRIVATE
        project_warnings  # warnings only for this target
        # private dependencies (internal implementation only)
)

# Add Vulkan support if available
if(Vulkan_FOUND)
    target_sources(mylib PRIVATE
        src/vulkan_renderer.cpp
        src/vulkan_utils.cpp
    )
    
    target_link_libraries(mylib PRIVATE
        Vulkan::Vulkan  # use imported target (not hardcoded path!)
    )
    
    target_compile_definitions(mylib PRIVATE
        USE_VULKAN  # enable Vulkan code paths
    )
endif()

# Executable
add_executable(main
    src/main.cpp
)

target_link_libraries(main PRIVATE
    mylib
    project_warnings
)

# ----------------------------------------------------------------------------
# Testing (Google Test integration)
# ----------------------------------------------------------------------------

if(BUILD_TESTS)
    add_executable(tests
        tests/vector_test.cpp
        tests/math_test.cpp
        tests/functional_test.cpp
    )
    
    target_link_libraries(tests PRIVATE
        mylib
        GTest::gtest
        GTest::gtest_main  # provides main() for us
        project_warnings
    )
    
    # Register tests with CTest
    include(GoogleTest)
    gtest_discover_tests(tests)
    
    message(STATUS "Tests configured (run with: ctest)")
endif()

# ----------------------------------------------------------------------------
# Documentation (Doxygen generation)
# ----------------------------------------------------------------------------

if(BUILD_DOCS)
    # Configure Doxygen settings
    set(DOXYGEN_PROJECT_NAME "${PROJECT_NAME}")
    set(DOXYGEN_PROJECT_NUMBER "${PROJECT_VERSION}")
    set(DOXYGEN_PROJECT_BRIEF "${PROJECT_DESCRIPTION}")
    
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
        COMMENT "Generating excessive documentation with Doxygen uwu"
    )
    
    message(STATUS "Documentation target 'docs' created (run with: cmake --build . --target docs)")
endif()

# ----------------------------------------------------------------------------
# Installation Rules
# ----------------------------------------------------------------------------

include(GNUInstallDirs)

# Install library
install(TARGETS mylib
    EXPORT MyLibTargets
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    INCLUDES DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)

# Install headers
install(DIRECTORY include/
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
    FILES_MATCHING PATTERN "*.hpp"
)

# Install executable
install(TARGETS main
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

# Export targets for other CMake projects
install(EXPORT MyLibTargets
    FILE MyLibTargets.cmake
    NAMESPACE MyLib::
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/MyLib
)

# ----------------------------------------------------------------------------
# Package Configuration
# ----------------------------------------------------------------------------

include(CMakePackageConfigHelpers)

# Generate config file
configure_package_config_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/cmake/MyLibConfig.cmake.in
    ${CMAKE_CURRENT_BINARY_DIR}/MyLibConfig.cmake
    INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/MyLib
)

# Generate version file
write_basic_package_version_file(
    ${CMAKE_CURRENT_BINARY_DIR}/MyLibConfigVersion.cmake
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY SameMajorVersion
)

# Install config files
install(FILES
    ${CMAKE_CURRENT_BINARY_DIR}/MyLibConfig.cmake
    ${CMAKE_CURRENT_BINARY_DIR}/MyLibConfigVersion.cmake
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/MyLib
)

# ----------------------------------------------------------------------------
# Summary
# ----------------------------------------------------------------------------

message(STATUS "")
message(STATUS "============================================================")
message(STATUS "  ${PROJECT_NAME} v${PROJECT_VERSION} Configuration")
message(STATUS "============================================================")
message(STATUS "")
message(STATUS "Build configuration:")
message(STATUS "  C++ Standard:        C++${CMAKE_CXX_STANDARD}")
message(STATUS "  Build Type:          ${CMAKE_BUILD_TYPE}")
message(STATUS "  Compiler:            ${CMAKE_CXX_COMPILER_ID} ${CMAKE_CXX_COMPILER_VERSION}")
message(STATUS "")
message(STATUS "Options:")
message(STATUS "  Build Tests:         ${BUILD_TESTS}")
message(STATUS "  Build Docs:          ${BUILD_DOCS}")
message(STATUS "  Warnings as Errors:  ${ENABLE_WARNINGS_AS_ERRORS}")
message(STATUS "")
message(STATUS "Dependencies:")
message(STATUS "  Vulkan:              ${Vulkan_FOUND}")
message(STATUS "  Google Test:         ${GTest_FOUND}")
message(STATUS "  Doxygen:             ${DOXYGEN_FOUND}")
message(STATUS "")
message(STATUS "functional programming gang rise up uwu 💜")
message(STATUS "============================================================")
message(STATUS "")
```

## Custom Find Modules (when find_package doesn't work)

```cmake
# cmake/FindMyLibrary.cmake
# Custom find module for MyLibrary (NO HARDCODED PATHS!)

# Try pkg-config first (cross-platform discovery)
find_package(PkgConfig QUIET)
if(PKG_CONFIG_FOUND)
    pkg_check_modules(PC_MyLibrary QUIET mylibrary)
endif()

# Find the header
find_path(MyLibrary_INCLUDE_DIR
    NAMES mylibrary.h
    PATHS
        ${PC_MyLibrary_INCLUDE_DIRS}  # from pkg-config
        /usr/include
        /usr/local/include
        $ENV{MYLIBRARY_ROOT}/include  # user can set environment variable
    PATH_SUFFIXES mylibrary
)

# Find the library
find_library(MyLibrary_LIBRARY
    NAMES mylibrary
    PATHS
        ${PC_MyLibrary_LIBRARY_DIRS}  # from pkg-config
        /usr/lib
        /usr/local/lib
        $ENV{MYLIBRARY_ROOT}/lib
)

# Handle REQUIRED and QUIET arguments
include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(MyLibrary
    REQUIRED_VARS
        MyLibrary_LIBRARY
        MyLibrary_INCLUDE_DIR
    VERSION_VAR PC_MyLibrary_VERSION
)

# Create imported target (modern CMake style!)
if(MyLibrary_FOUND AND NOT TARGET MyLibrary::MyLibrary)
    add_library(MyLibrary::MyLibrary UNKNOWN IMPORTED)
    set_target_properties(MyLibrary::MyLibrary PROPERTIES
        IMPORTED_LOCATION "${MyLibrary_LIBRARY}"
        INTERFACE_INCLUDE_DIRECTORIES "${MyLibrary_INCLUDE_DIR}"
    )
endif()

mark_as_advanced(MyLibrary_INCLUDE_DIR MyLibrary_LIBRARY)
```

## CMake Best Practices Checklist

- [ ] **CMake 3.30+** required (latest version or beta preferred!)
- [ ] **NO HARDCODED PATHS** (find everything with find_package/find_library)
- [ ] **target-based** architecture (not variable-based)
- [ ] **transitive dependencies** properly configured
- [ ] **generator expressions** for configuration-specific settings
- [ ] **C++26 standard** (latest, beta features ok!)
- [ ] **GCC/Clang preferred** (Rust can cry about it)
- [ ] **Vulkan support** if GPU needed (not OpenGL!)
- [ ] **Google Test** for testing
- [ ] **Doxygen** for documentation
- [ ] **warnings as errors** enabled
- [ ] **cross-platform** configuration
- [ ] **excessive comments** (explain the magic)
- [ ] **summary message** at end of configuration

**remember**: CMake is actually beautiful when you use it correctly. Modern
CMake (3.20+, but prefer 3.30+!) is declarative, functional-ish, and makes
cross-platform builds actually work. NO HARDCODED PATHS EVER. find things
dynamically or the build system gods will be angry uwu 💜✨

seize the means of compilation (with the beautiful build system)!