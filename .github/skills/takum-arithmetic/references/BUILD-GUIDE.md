# Building libtakum Reference Implementation

This guide covers building and using the libtakum reference implementation.

## Prerequisites

### Required Tools

| Tool                        | Version          | Purpose                 |
|-----------------------------|------------------|-------------------------|
| C Compiler (GCC/Clang/MSVC) | C99 support      | Compilation             |
| Make                        | POSIX-compatible | Build orchestration     |
| sh                          | POSIX shell      | Configure script        |
| ar                          | -                | Static library creation |
| ranlib                      | -                | Library indexing        |

### Optional Tools

| Tool         | Purpose                  |
|--------------|--------------------------|
| clang-format | Code formatting          |
| Doxygen      | Documentation generation |
| pkg-config   | Build integration        |

## Quick Start

### Standard Build

```bash
# Clone or extract source
cd libtakum-master

# Configure for your platform
./configure

# Build library (parallel)
make -j

# Run tests (parallel)
make -j test

# Install to system
sudo make install
```

### Verification

```bash
# Check library was built
ls -la libtakum.a libtakum.so*

# Verify tests passed
echo $?  # Should be 0

# Check installation
ls -la /usr/local/lib/libtakum.*
ls -la /usr/local/include/takum.h
```

## Detailed Build Process

### Step 1: Configure

The `configure` script detects your platform and sets appropriate variables:

```bash
./configure
```

This creates/modifies `config.mk` with:

- Library naming (`libtakum.a`, `libtakum.so.X.Y.Z`)
- Compiler flags
- Installation paths
- Platform-specific options

### Step 2: Build

```bash
# Build all targets (library, man pages)
make all

# Or just the library
make libtakum.a libtakum.so.2.0.0
```

Build artifacts:

- `libtakum.a` - Static library
- `libtakum.so.2.0.0` - Shared library (Linux naming)
- `*.o` files in `src/`

### Step 3: Test

```bash
# Run full test suite
make test

# Or equivalently
make check

# Test output shows pass/fail for each test
```

### Step 4: Install

```bash
# Install to default prefix (/usr/local)
sudo make install

# Install to custom prefix
make PREFIX=/opt/takum install

# Staged install for packaging
make DESTDIR=/tmp/package install
```

Installed files:

- `$(PREFIX)/lib/libtakum.a`
- `$(PREFIX)/lib/libtakum.so.X.Y.Z` (with symlinks)
- `$(PREFIX)/include/takum.h`
- `$(PREFIX)/share/man/man3/*.3`
- `$(PREFIX)/share/man/man7/libtakum.7`
- `$(PREFIX)/share/licenses/libtakum/LICENSE`

## Platform-Specific Notes

### Linux

Default configuration works out of the box:

```bash
./configure
make -j install
sudo ldconfig  # Update library cache
```

### macOS

Uses `.dylib` instead of `.so`:

```bash
./configure
make -j install
# Library will be libtakum.X.dylib
```

### Windows (MSYS2/MinGW)

```bash
./configure
make -j
# Library will be libtakum.lib and libtakum.dll
# Executables have .exe suffix
```

### FreeBSD/OpenBSD/NetBSD

Similar to Linux with minor differences:

```bash
./configure
gmake -j install  # Use gmake on BSD
```

## Build Targets Reference

| Target           | Description                           |
|------------------|---------------------------------------|
| `all`            | Build library and man pages (default) |
| `libtakum.a`     | Static library only                   |
| `libtakum.so.*`  | Shared library only                   |
| `example`        | Build example programs                |
| `test` / `check` | Build and run test suite              |
| `install`        | Install to system                     |
| `uninstall`      | Remove installed files                |
| `clean`          | Remove build artifacts                |
| `dist`           | Create distribution tarball           |
| `format`         | Run clang-format                      |

## Configuration Variables

### In config.mk

```makefile
# Installation paths
DESTDIR =                    # Staging directory
PREFIX = /usr/local          # Install prefix
INCPREFIX = $(PREFIX)/include
LIBPREFIX = $(PREFIX)/lib
MANPREFIX = $(PREFIX)/share/man
LICPREFIX = $(PREFIX)/share/licenses

# Library names
ANAME = libtakum.a           # Static archive
SONAME = libtakum.so.2.0.0   # Shared object

# Build flags
CC = cc
CFLAGS = -std=c99 -Os -Wall -Wextra -Wpedantic
LDFLAGS = -s
LDLIBS = -lm
```

### Overriding at Build Time

```bash
# Use different compiler
make CC=clang

# Use different flags
make CFLAGS="-std=c99 -O3 -march=native"

# Different install location
make PREFIX=/opt/local install
```

## Using the Library

### Linking

```bash
# With pkg-config (if installed)
gcc program.c $(pkg-config --cflags --libs takum)

# Manual linking
gcc program.c -I/usr/local/include -L/usr/local/lib -ltakum -lm
```

### Example Program

```c
#include <stdio.h>
#include <takum.h>

int main(void) {
    // Create takum values
    takum_log16 a = takum_log16_from_float64(3.14159);
    takum_log16 b = takum_log16_from_float64(2.71828);
    
    // Arithmetic
    takum_log16 sum = takum_log16_addition(a, b);
    takum_log16 product = takum_log16_multiplication(a, b);
    
    // Convert back to float
    printf("a = %.6f\n", takum_log16_to_float64(a));
    printf("b = %.6f\n", takum_log16_to_float64(b));
    printf("a + b = %.6f\n", takum_log16_to_float64(sum));
    printf("a × b = %.6f\n", takum_log16_to_float64(product));
    
    return 0;
}
```

### Compiling the Example

```bash
gcc example.c -o example -ltakum -lm
./example
```

## Running the Calculator Example

```bash
# Build example
make example

# Run calculator
./example/calculator

# Example session (RPN notation):
# > 3.14159
# [takum_log16] 3.141590118408203
# > 2
# [takum_log16] 2
# > *
# [takum_log16] 6.28318977355957
# > sin
# [takum_log16] 9.870529197695479e-06
```

## Troubleshooting

### Common Issues

**Error: `takum.h` not found**

```bash
# Ensure include path is correct
gcc -I/usr/local/include program.c ...

# Or set CPATH
export CPATH=/usr/local/include
```

**Error: `-ltakum` not found**

```bash
# Ensure library path is correct
gcc -L/usr/local/lib program.c -ltakum ...

# Or set LIBRARY_PATH
export LIBRARY_PATH=/usr/local/lib

# Run ldconfig after install (Linux)
sudo ldconfig
```

**Error: undefined reference to `log`**

```bash
# Link math library
gcc program.c -ltakum -lm
```

**Tests fail with precision errors?**

```bash
# May be platform-specific long double issues
# Check configure output for warnings
```

### Build Verification

```bash
# Check static library contents
ar -t libtakum.a | head -20

# Check shared library symbols
nm -D libtakum.so.* | grep takum | head -20

# Verify library loads
ldd ./example/calculator  # Linux
otool -L ./example/calculator  # macOS
```

## Integration with Build Systems

### CMake

```cmake
# FindTakum.cmake or direct linking
find_library(TAKUM_LIBRARY takum)
find_path(TAKUM_INCLUDE_DIR takum.h)

target_link_libraries(myapp ${TAKUM_LIBRARY} m)
target_include_directories(myapp PRIVATE ${TAKUM_INCLUDE_DIR})
```

### pkg-config

If `libtakum.pc` was installed:

```cmake
find_package(PkgConfig REQUIRED)
pkg_check_modules(TAKUM REQUIRED takum)

target_link_libraries(myapp ${TAKUM_LIBRARIES})
target_include_directories(myapp PRIVATE ${TAKUM_INCLUDE_DIRS})
```

### Meson

```meson
takum_dep = dependency('takum', required: true)
executable('myapp', 'main.c', dependencies: [takum_dep])
```

## Version Information

Current version: **2.0.0**

Check installed version:

```bash
# Via pkg-config
pkg-config --modversion takum

# Via man page
man libtakum
```

## Uninstallation

```bash
# Remove installed files
sudo make uninstall

# Manual removal
sudo rm /usr/local/lib/libtakum.*
sudo rm /usr/local/include/takum.h
sudo rm -rf /usr/local/share/man/man3/takum*
sudo rm /usr/local/share/man/man7/libtakum.7
sudo rm -rf /usr/local/share/licenses/libtakum
```
