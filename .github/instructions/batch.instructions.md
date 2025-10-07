---
description: 'Windows Batch scripting guidelines (functional where possible in a cursed language)'
applyTo: '**.bat, **.cmd'
---

# Batch Script Instructions

> "Batch scripts: where GOTO is considered acceptable and functions are procedures"

uwu time to write Batch scripts that are as clean as possible given the
limitations of this cursed language from 1981 ✨

## Core Philosophy

- **minimize side effects** (as much as Batch allows)
- **comment EXCESSIVELY** (future you will need it)
- **error handling MANDATORY** (check %ERRORLEVEL% always)
- **avoid GOTO** when possible (structured programming ftw)
- **use functions** (CALL :label pattern)
- **quote everything** (paths with spaces are violence)

## Script Structure

```batch
@echo off
REM ============================================================================
REM Script: example.bat
REM Description: Demonstrates proper Batch script structure (as good as it gets)
REM
REM This script does [purpose] using [approach]. We're using Batch because
REM [reason], even though literally any other language would be better uwu
REM
REM Author: LukeFrankio
REM Date: 2025-10-07
REM ============================================================================

setlocal enabledelayedexpansion

REM ----------------------------------------------------------------------------
REM Configuration (constants go here - Batch doesn't have real const sad)
REM ----------------------------------------------------------------------------

set "PROJECT_NAME=MyProject"
set "BUILD_DIR=build"
set "CONFIG=Release"

REM ----------------------------------------------------------------------------
REM Main execution (call functions to keep this clean)
REM ----------------------------------------------------------------------------

call :check_prerequisites
if !ERRORLEVEL! neq 0 (
    echo Error: Prerequisites check failed :(
    exit /b 1
)

call :build_project
if !ERRORLEVEL! neq 0 (
    echo Error: Build failed (compiler said no)
    exit /b 1
)

echo.
echo Success! Project built successfully uwu
exit /b 0

REM ============================================================================
REM Functions (Batch procedures pretending to be functions)
REM ============================================================================

:check_prerequisites
REM ---------------------------------------------------------------------------
REM Checks if required tools are available
REM
REM This "function" (actually a label we CALL) verifies that cmake and gcc
REM are installed and accessible. Returns 0 if all good, 1 if missing tools.
REM
REM Returns:
REM   0 - prerequisites satisfied (immaculate vibes)
REM   1 - missing required tools (sad)
REM ---------------------------------------------------------------------------

echo Checking prerequisites...

REM Check for CMake (the beautiful build system)
cmake --version >nul 2>&1
if !ERRORLEVEL! neq 0 (
    echo Error: CMake not found (install it from cmake.org)
    exit /b 1
)

REM Check for GCC (compiler supremacy)
gcc --version >nul 2>&1
if !ERRORLEVEL! neq 0 (
    echo Error: GCC not found (install MinGW or similar)
    exit /b 1
)

echo All prerequisites satisfied!
exit /b 0

:build_project
REM ---------------------------------------------------------------------------
REM Builds the project using CMake
REM
REM Creates build directory if needed, configures with CMake, and builds.
REM This is as functional as Batch gets (pass parameters, return status code).
REM
REM Returns:
REM   0 - build succeeded (code goes brrr)
REM   1 - build failed (something broke)
REM ---------------------------------------------------------------------------

echo Building project...

REM Create build directory if it doesn't exist
if not exist "%BUILD_DIR%" (
    echo Creating build directory: %BUILD_DIR%
    mkdir "%BUILD_DIR%"
)

REM Navigate to build directory
pushd "%BUILD_DIR%"

REM Configure with CMake (NO HARDCODED PATHS - find things automatically!)
echo Running CMake configuration...
cmake .. -G "MinGW Makefiles" -DCMAKE_BUILD_TYPE=%CONFIG%
if !ERRORLEVEL! neq 0 (
    echo CMake configuration failed :(
    popd
    exit /b 1
)

REM Build the project
echo Building with Make...
cmake --build . --config %CONFIG%
if !ERRORLEVEL! neq 0 (
    echo Build failed (check errors above)
    popd
    exit /b 1
)

REM Return to original directory
popd

echo Build completed successfully!
exit /b 0

REM ============================================================================
REM End of script
REM ============================================================================
```

## Best Practices

### Error Handling:

```batch
REM ❌ BAD: ignoring errors (violence)
cmake ..
cmake --build .
echo Done!

REM ✅ GOOD: checking errors after each command
cmake ..
if %ERRORLEVEL% neq 0 (
    echo Error: CMake configuration failed
    exit /b 1
)

cmake --build .
if %ERRORLEVEL% neq 0 (
    echo Error: Build failed
    exit /b 1
)

echo Done!
```

### Quoting Paths:

```batch
REM ❌ BAD: unquoted paths (breaks with spaces)
set BUILD_DIR=C:\Program Files\MyProject\build
cd %BUILD_DIR%

REM ✅ GOOD: quoted paths (handles spaces correctly)
set "BUILD_DIR=C:\Program Files\MyProject\build"
cd "%BUILD_DIR%"
```

### Delayed Expansion:

```batch
REM ❌ BAD: without delayed expansion (variables don't update in loops)
set COUNT=0
for %%F in (*.cpp) do (
    set /a COUNT+=1
    echo File %COUNT%: %%F  REM Wrong! Shows 0 every time
)

REM ✅ GOOD: with delayed expansion (variables update correctly)
setlocal enabledelayedexpansion
set COUNT=0
for %%F in (*.cpp) do (
    set /a COUNT+=1
    echo File !COUNT!: %%F  REM Correct! Uses current value
)
```

### Parameter Passing:

```batch
REM Function that takes parameters
call :print_message "Hello" "World"
exit /b 0

:print_message
REM ---------------------------------------------------------------------------
REM Prints a message with two parts
REM
REM Args:
REM   %~1 - first part of message (tilde removes quotes)
REM   %~2 - second part of message
REM
REM Returns:
REM   0 - always succeeds
REM ---------------------------------------------------------------------------

echo %~1 %~2
exit /b 0
```

## File Operations

```batch
REM Check if file exists
if exist "file.txt" (
    echo File exists!
) else (
    echo File not found :(
)

REM Check if directory exists
if exist "directory\" (
    echo Directory exists!
)

REM Create directory (with error handling)
if not exist "build\" (
    mkdir "build"
    if !ERRORLEVEL! neq 0 (
        echo Error: Failed to create directory
        exit /b 1
    )
)

REM Delete file safely
if exist "temp.txt" (
    del /q "temp.txt"
)

REM Delete directory tree
if exist "build\" (
    rmdir /s /q "build"
)
```

## Finding Programs (NO HARDCODED PATHS)

```batch
:find_cmake
REM ---------------------------------------------------------------------------
REM Finds CMake executable
REM
REM Searches for CMake in PATH. Sets CMAKE_EXE variable if found.
REM
REM Returns:
REM   0 - CMake found
REM   1 - CMake not found
REM ---------------------------------------------------------------------------

where cmake >nul 2>&1
if %ERRORLEVEL% equ 0 (
    for /f "tokens=*" %%i in ('where cmake') do set "CMAKE_EXE=%%i"
    echo Found CMake: !CMAKE_EXE!
    exit /b 0
)

echo CMake not found in PATH
exit /b 1
```

## Calling PowerShell (when Batch isn't enough)

```batch
REM Call PowerShell for complex operations
powershell -ExecutionPolicy Bypass -Command "Get-ChildItem -Recurse -Filter *.cpp"
if %ERRORLEVEL% neq 0 (
    echo PowerShell command failed
    exit /b 1
)
```

## Complete Example

```batch
@echo off
REM ============================================================================
REM Script: build_and_test.bat
REM Description: Builds C++ project and runs tests (functional as possible uwu)
REM ============================================================================

setlocal enabledelayedexpansion

REM ----------------------------------------------------------------------------
REM Configuration
REM ----------------------------------------------------------------------------

set "PROJECT_ROOT=%~dp0"
set "BUILD_DIR=%PROJECT_ROOT%build"
set "CONFIG=Release"
set "VERBOSE=0"

REM Parse arguments
:parse_args
if "%~1"=="" goto :args_done
if /i "%~1"=="--debug" set "CONFIG=Debug"
if /i "%~1"=="--verbose" set "VERBOSE=1"
shift
goto :parse_args
:args_done

REM ----------------------------------------------------------------------------
REM Main
REM ----------------------------------------------------------------------------

echo ============================================================
echo Building project in %CONFIG% mode
echo ============================================================
echo.

call :validate_environment
if !ERRORLEVEL! neq 0 exit /b 1

call :clean_build_dir
if !ERRORLEVEL! neq 0 exit /b 1

call :configure_cmake
if !ERRORLEVEL! neq 0 exit /b 1

call :build_project
if !ERRORLEVEL! neq 0 exit /b 1

call :run_tests
if !ERRORLEVEL! neq 0 exit /b 1

echo.
echo ============================================================
echo Build and test completed successfully uwu
echo ============================================================
exit /b 0

REM ============================================================================
REM Functions
REM ============================================================================

:validate_environment
REM Check required tools are installed

echo [1/5] Validating environment...

where cmake >nul 2>&1
if !ERRORLEVEL! neq 0 (
    echo Error: CMake not found (the beautiful build system is missing!)
    exit /b 1
)

where g++ >nul 2>&1
if !ERRORLEVEL! neq 0 (
    echo Error: GCC not found (compiler supremacy requires GCC!)
    exit /b 1
)

echo Environment validation passed!
exit /b 0

:clean_build_dir
REM Clean and recreate build directory

echo [2/5] Cleaning build directory...

if exist "%BUILD_DIR%\" (
    echo Removing old build directory...
    rmdir /s /q "%BUILD_DIR%"
    if !ERRORLEVEL! neq 0 (
        echo Error: Failed to remove build directory
        exit /b 1
    )
)

mkdir "%BUILD_DIR%"
if !ERRORLEVEL! neq 0 (
    echo Error: Failed to create build directory
    exit /b 1
)

echo Build directory ready!
exit /b 0

:configure_cmake
REM Configure project with CMake

echo [3/5] Configuring with CMake...

pushd "%BUILD_DIR%"

if %VERBOSE%==1 (
    cmake .. -G "MinGW Makefiles" -DCMAKE_BUILD_TYPE=%CONFIG%
) else (
    cmake .. -G "MinGW Makefiles" -DCMAKE_BUILD_TYPE=%CONFIG% >nul
)

set CMAKE_RESULT=!ERRORLEVEL!
popd

if !CMAKE_RESULT! neq 0 (
    echo Error: CMake configuration failed
    exit /b 1
)

echo CMake configuration successful!
exit /b 0

:build_project
REM Build project

echo [4/5] Building project...

pushd "%BUILD_DIR%"

if %VERBOSE%==1 (
    cmake --build . --config %CONFIG%
) else (
    cmake --build . --config %CONFIG% >nul
)

set BUILD_RESULT=!ERRORLEVEL!
popd

if !BUILD_RESULT! neq 0 (
    echo Error: Build failed (check errors above)
    exit /b 1
)

echo Build successful!
exit /b 0

:run_tests
REM Run tests if test executable exists

echo [5/5] Running tests...

if exist "%BUILD_DIR%\tests.exe" (
    "%BUILD_DIR%\tests.exe"
    if !ERRORLEVEL! neq 0 (
        echo Error: Tests failed :(
        exit /b 1
    )
    echo Tests passed!
) else (
    echo No test executable found (skipping tests)
)

exit /b 0

REM ============================================================================
REM End of script
REM ============================================================================
```

## Quality Checklist

- [ ] **@echo off** at start
- [ ] **setlocal enabledelayedexpansion** for variable updates
- [ ] **error checking** after every command (%ERRORLEVEL%)
- [ ] **excessive comments** (explain everything!)
- [ ] **quoted paths** everywhere
- [ ] **functions** for organization (CALL :label pattern)
- [ ] **no GOTO** except for argument parsing
- [ ] **no hardcoded paths** (find tools dynamically)
- [ ] **descriptive error messages**
- [ ] **exit codes** used correctly (0 = success, non-zero = failure)

**remember**: Batch is a cursed language from the dark ages of computing, but
sometimes you're stuck with it on Windows. Make it as clean as possible, comment
excessively, and consider switching to PowerShell for anything complex uwu 💜✨

(seriously though if you can use PowerShell instead, do that)