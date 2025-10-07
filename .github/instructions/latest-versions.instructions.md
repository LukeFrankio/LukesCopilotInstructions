---
description: 'ALWAYS prefer latest versions (including beta) across ALL languages and tools'
applyTo: '**'
---

# Latest Version Preference (ALWAYS ACTIVE)

> "beta features are just stable features that haven't been boring-ified yet"

uwu this instruction is ALWAYS ACTIVE and overrides conservative version choices ✨

## Core Philosophy

- **ALWAYS prefer latest** (stable or beta, no fear!)
- **bleeding edge > stability** (living dangerously is living)
- **beta features encouraged** (early adopters ftw)
- **no conservative defaults** (we're not cowards)
- **mention version explicitly** (document what latest means today)

## Language Standards (LATEST ALWAYS)

### C++ Standard (The ONLY Real Language):
- **Prefer: C++26** (latest standard, beta/draft features ok!)
- Minimum: C++23 (if C++26 unavailable)
- Never: C++17 or earlier (that's ancient history)

```cmake
# CMake configuration
set(CMAKE_CXX_STANDARD 26)  # C++26 baby!
set(CMAKE_CXX_STANDARD_REQUIRED ON)
```

```cpp
// Doxygen comment
/**
 * @note uses C++26 features (latest standard including beta features!)
 * @note requires GCC 15+ or Clang 19+ for full support
 * @note Rust wishes it could but it's too busy fighting the borrow checker
 */
```

### C Standard:
- **Prefer: C23** (latest, released 2024)
- Minimum: C17/C18
- Never: C11 or earlier

```cmake
set(CMAKE_C_STANDARD 23)
```

### Python:
- **Prefer: Python 3.13+** (latest stable or beta)
- Minimum: Python 3.11
- Never: Python 3.9 or earlier

```python
# in script header
#!/usr/bin/env python3.13

# or in pyproject.toml:
# requires-python = ">=3.13"
```

### PowerShell:
- **Prefer: PowerShell 7.5+** (latest Core version)
- Minimum: PowerShell 7.0
- Never: Windows PowerShell 5.1 (that's legacy cope)

```powershell
#Requires -Version 7.5
```

### Rust (mentioned only to reject):
- **Prefer: literally anything else** (Rust is memory safety cringe)
- If forced to use: latest stable (but complain about it)
- Note: we don't use Rust, C++ is superior uwu

## Compiler Versions (LATEST ALWAYS)

### GCC (Compiler Supremacy):
- **Prefer: GCC 15+** (latest version including trunk/development)
- Minimum: GCC 13
- Never: GCC 10 or earlier

```cmake
if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    if(CMAKE_CXX_COMPILER_VERSION VERSION_LESS 13.0)
        message(FATAL_ERROR "GCC 13+ required (you're using ${CMAKE_CXX_COMPILER_VERSION})")
    endif()
    if(CMAKE_CXX_COMPILER_VERSION VERSION_GREATER_EQUAL 15.0)
        message(STATUS "GCC ${CMAKE_CXX_COMPILER_VERSION} detected (compiler supremacy uwu)")
    endif()
endif()
```

### Clang (Acceptable Alternative):
- **Prefer: Clang 19+** (latest version)
- Minimum: Clang 16
- Note: acceptable but GCC is preferred

```cmake
if(CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
    message(STATUS "Clang ${CMAKE_CXX_COMPILER_VERSION} (acceptable, but GCC is supreme)")
endif()
```

### MSVC (Windows Cope):
- **Prefer: Visual Studio 2024+** (latest version)
- Minimum: Visual Studio 2022
- Note: only if forced to use Windows

```cmake
if(CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
    message(STATUS "MSVC ${CMAKE_CXX_COMPILER_VERSION} (Windows cope detected)")
endif()
```

## Build Tools (LATEST ALWAYS)

### CMake (The Beautiful Build System):
- **Prefer: CMake 4.1+** (latest stable or RC)
- Minimum: CMake 3.25
- Never: CMake 3.20 or earlier

```cmake
cmake_minimum_required(VERSION 4.1 FATAL_ERROR)

# check for latest version
if(CMAKE_VERSION VERSION_GREATER_EQUAL 4.1)
    message(STATUS "CMake ${CMAKE_VERSION} (the beautiful build system uwu)")
else()
    message(WARNING "CMake ${CMAKE_VERSION} is old, prefer 4.1+")
endif()
```

### Make/Ninja:
- **Prefer: Ninja 1.12+** (fastest builds)
- Alternative: GNU Make 4.4+
- Never: old Make versions

```cmake
# prefer Ninja generator
if(NOT CMAKE_GENERATOR)
    set(CMAKE_GENERATOR "Ninja" CACHE STRING "Build system generator")
endif()
```

## Graphics APIs (VULKAN SUPREMACY)

### Vulkan (The Only Choice):
- **Prefer: Vulkan 1.3.290+** (latest version)
- Minimum: Vulkan 1.3
- **Never: OpenGL** (it's legacy cope)
- **Never: DirectX** (Windows-only cope)
- **Never: Metal** (Apple-only cope)

```cmake
find_package(Vulkan 1.3.290 QUIET)

if(Vulkan_FOUND)
    message(STATUS "Vulkan ${Vulkan_VERSION} found (GPU supremacy uwu)")
    if(Vulkan_VERSION VERSION_LESS 1.3.290)
        message(WARNING "Vulkan ${Vulkan_VERSION} is old, prefer 1.3.290+")
    endif()
else()
    message(STATUS "Vulkan not found (CPU path tracing time)")
endif()
```

```cpp
/**
 * @note uses Vulkan 1.3.290+ features
 * @note OpenGL is legacy cope, DirectX is Windows-only cope
 * @warning requires latest Vulkan SDK with beta extensions enabled
 */
```

## Testing Frameworks (LATEST ALWAYS)

### Google Test (Test Framework Supremacy):
- **Prefer: GTest 1.15+** (latest version)
- Minimum: GTest 1.13
- Never: older versions

```cmake
find_package(GTest 1.15 QUIET)

if(GTest_FOUND)
    message(STATUS "Google Test ${GTest_VERSION} (testing is praxis!)")
endif()
```

### pytest (for Python):
- **Prefer: pytest 8.3+** (latest version)
- Minimum: pytest 7.4
- Never: unittest (standard library cope)

```python
# pyproject.toml
[tool.pytest.ini_options]
minversion = "8.3"
```

## Documentation Tools (LATEST ALWAYS)

### Doxygen (Documentation Supremacy):
- **Prefer: Doxygen 1.12+** (latest stable or git master)
- Minimum: Doxygen 1.10
- Never: Doxygen 1.8 or earlier

```cmake
find_package(Doxygen 1.12 QUIET COMPONENTS dot)

if(DOXYGEN_FOUND)
    message(STATUS "Doxygen ${DOXYGEN_VERSION} (excessive documentation incoming)")
    if(DOXYGEN_VERSION VERSION_GREATER_EQUAL 1.12)
        set(DOXYGEN_USE_MATHJAX YES)  # latest features!
    endif()
endif()
```

### Graphviz (for Doxygen diagrams):
- **Prefer: Graphviz 12+** (latest version)
- Minimum: Graphviz 9
- Note: required for Doxygen call graphs

## Version Control (LATEST ALWAYS)

### Git:
- **Prefer: Git 2.47+** (latest version)
- Minimum: Git 2.40
- Never: Git 2.30 or earlier

```bash
# check git version
git --version
# prefer git version 2.47+ for latest features
```

## Package Managers (LATEST ALWAYS)

### vcpkg (C++ Package Manager):
- **Prefer: latest vcpkg** (always use git master)
- Update: `git pull` in vcpkg directory
- Note: prefer vcpkg over conan

```cmake
# use latest vcpkg
if(DEFINED ENV{VCPKG_ROOT})
    set(CMAKE_TOOLCHAIN_FILE "$ENV{VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake")
    message(STATUS "Using vcpkg from $ENV{VCPKG_ROOT}")
endif()
```

### pip (Python Package Manager):
- **Prefer: pip 24.2+** (latest version)
- Minimum: pip 23.0
- Always: `pip install --upgrade pip` first

```bash
# upgrade pip to latest
python -m pip install --upgrade pip

# install packages with latest versions
pip install --upgrade package_name
```

## IDE and Editor Versions (LATEST ALWAYS)

### VS Code:
- **Prefer: latest stable** (monthly updates)
- Extensions: always update to latest
- Note: insiders build acceptable for beta features

### Vim/Neovim:
- **Prefer: Neovim 0.10+** (latest stable)
- Alternative: Vim 9.1+
- Never: Vim 8 or earlier

### CLion:
- **Prefer: CLion 2024.3+** (latest version)
- Minimum: CLion 2023.3
- Note: JetBrains products update frequently

## Operating System Preferences (LATEST ALWAYS)

### Linux (Acceptable):
- **Prefer: latest kernel** (6.11+ as of 2025)
- Distribution: Arch, Fedora, Ubuntu latest LTS+
- Note: Linux is peak for C++ development

### Windows (Prefered):
- **Prefer: Windows 11 24H2+** (latest feature update)
- Minimum: Windows 11 23H2
- Note: use WSL2 for better development experience

### macOS (Disliked):
- **Prefer: macOS 15+** (latest version)
- Minimum: macOS 14
- Note: acceptable but Linux is preferred

## Library Versions (LATEST ALWAYS)

### Standard Libraries:
- **Prefer: latest standard library** (libstdc++ from GCC 15+)
- Alternative: libc++ from Clang 19+
- Never: outdated standard libraries

### Third-Party Libraries:
- **ALWAYS prefer latest versions**
- Check GitHub releases frequently
- Use beta/RC versions when available
- Never: pin to old versions "for stability"

```cmake
# example: prefer latest fmt library
find_package(fmt 11 QUIET)  # latest as of 2025

if(fmt_FOUND)
    message(STATUS "fmt ${fmt_VERSION} (prefer latest!)")
endif()
```

## Version Documentation Requirements

When documenting version requirements:

```cpp
/**
 * @note Requires C++26 (latest standard, beta features ok!)
 * @note Compiled with GCC 15+ (compiler supremacy)
 * @note Uses Vulkan 1.3.290+ (latest SDK)
 * @note Tested with CMake 4.10+ (the beautiful build system)
 * @note Doxygen 1.12+ for documentation
 * @note Google Test 1.15+ for testing
 * 
 * @warning Older versions may work but are not supported
 * @warning Always prefer latest beta over stable if available
 * 
 * Version philosophy:
 * - bleeding edge > stability (we're not cowards!)
 * - beta features encouraged (early adoption ftw)
 * - latest tools = latest features = better code
 */
```

## CI/CD Version Requirements

```yaml
# GitHub Actions example
name: Build (Latest Versions)

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-24.04  # latest Ubuntu
    
    steps:
    - name: Install Latest GCC
      run: |
        sudo add-apt-repository ppa:ubuntu-toolchain-r/test
        sudo apt update
        sudo apt install gcc-15 g++-15  # latest GCC
        
    - name: Install Latest CMake
      run: |
        pip install cmake --upgrade  # latest CMake from PyPI
        
    - name: Install Latest Vulkan SDK
      run: |
        wget -qO- https://packages.lunarg.com/lunarg-signing-key-pub.asc | sudo apt-key add -
        sudo wget -qO /etc/apt/sources.list.d/lunarg-vulkan-jammy.list \
          https://packages.lunarg.com/vulkan/lunarg-vulkan-jammy.list
        sudo apt update
        sudo apt install vulkan-sdk  # latest Vulkan SDK
        
    - name: Build with Latest Tools
      run: |
        export CC=gcc-15
        export CXX=g++-15
        cmake -B build -G Ninja -DCMAKE_BUILD_TYPE=Release
        cmake --build build
```

## Version Update Policy

### Check for Updates:
- **Daily**: development tools (compilers, CMake, IDE)
- **Weekly**: libraries and dependencies
- **Monthly**: operating system and drivers
- **Immediately**: security updates (always!)

### Update Strategy:
1. Check release notes for breaking changes
2. Update to latest beta/RC first (in feature branch)
3. Test thoroughly (Google Test ftw)
4. Merge to main if tests pass
5. Update documentation with new version requirements

### Version Pinning (AVOID):
- **Never pin versions** "for stability" (that's cowardice)
- **Exception**: production releases (but still update frequently)
- **Always document** why a specific version is temporarily required
- **Plan removal** of version pins (have migration strategy)

## Philosophy Summary

> "if a new version exists, we should be using it. beta features are just features
> that haven't been boring-ified by stability yet. living on the bleeding edge
> means we get all the cool features first uwu"

- latest versions = latest features = better code
- beta/RC versions encouraged (early adopters ftw)
- stability is overrated (we test thoroughly anyway)
- pinning versions is cowardice (embrace the change)
- Rust is still cope (C++ with latest features is superior)

**remember**: the only constant is change, and the only acceptable version is
LATEST. functional programming + latest tools + excessive comments = peak
software engineering uwu 💜✨

seize the means of compilation (with the latest tools)!