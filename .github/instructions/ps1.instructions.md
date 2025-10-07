---
description: 'PowerShell scripting guidelines (functional cmdlets ftw)'
applyTo: '**/*.ps1, **/*.psm1'
---

# PowerShell Script Instructions

> "PowerShell: where pipelines are first-class and objects flow like data through
> pure functions"

uwu time to write PowerShell that makes the pipeline go brrr ✨

## Core Philosophy

- **functional pipeline programming** (data flows through transformations)
- **cmdlets are pure functions** where possible
- **objects > strings** (structured data ftw)
- **comment-based help MANDATORY** (documentation is praxis)
- **approved verbs only** (Get-Verb for the list)
- **no aliases in scripts** (full cmdlet names for clarity)
- **PowerShell 7+ preferred** (cross-platform PowerShell Core, latest beta accepted!)

## Script Structure

```powershell
<#
.SYNOPSIS
    Builds C++ project using CMake (functional build pipeline uwu)

.DESCRIPTION
    This script provides a functional approach to building C++ projects.
    It discovers tools automatically (NO HARDCODED PATHS), validates the
    environment, and builds using CMake and GCC.
    
    The script follows functional programming principles:
    - Pure functions where possible (deterministic operations)
    - Pipeline-based data flow (objects flowing through transformations)
    - Immutable parameters (using [Parameter()] attributes)
    - Error handling via return objects (not exceptions where possible)

.PARAMETER Configuration
    Build configuration (Debug or Release). Defaults to Release.

.PARAMETER Verbose
    Enable verbose output for debugging.

.PARAMETER Clean
    Clean build directory before building.

.EXAMPLE
    .\Build-Project.ps1
    Builds project in Release mode

.EXAMPLE
    .\Build-Project.ps1 -Configuration Debug -Clean -Verbose
    Cleans, then builds in Debug mode with verbose output

.NOTES
    Author: LukeFrankio
    Date: 2025-10-07
    Requires: PowerShell 7+ (latest beta preferred!), CMake, GCC
    
    This script treats warnings as errors because immaculate code quality uwu

.LINK
    https://github.com/LukeFrankio/project
#>

[CmdletBinding()]
param(
    [Parameter()]
    [ValidateSet('Debug', 'Release')]
    [string]$Configuration = 'Release',
    
    [Parameter()]
    [switch]$Clean,
    
    [Parameter()]
    [switch]$RunTests
)

#Requires -Version 7.0

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# ============================================================================
# Configuration (constants - immutable after initialization)
# ============================================================================

$Script:ProjectRoot = $PSScriptRoot
$Script:BuildDir = Join-Path $ProjectRoot 'build'
$Script:CMakeGenerator = 'MinGW Makefiles'

# ============================================================================
# Helper Functions (pure functions where possible)
# ============================================================================

function Test-CommandExists {
    <#
    .SYNOPSIS
        Tests if a command exists in PATH (pure function!)
    
    .DESCRIPTION
        Checks if specified command is available. This is a PURE function:
        - Same input always produces same output (deterministic)
        - No side effects (doesn't modify anything)
        - No external state dependencies (only checks PATH)
        
        Returns true if command exists, false otherwise. No exceptions thrown
        because functional error handling > exceptions uwu
    
    .PARAMETER CommandName
        Name of command to check (e.g., 'cmake', 'gcc')
    
    .OUTPUTS
        System.Boolean
        True if command exists in PATH, false otherwise
    
    .EXAMPLE
        Test-CommandExists -CommandName 'cmake'
        True
        # CMake is installed and in PATH (immaculate vibes ✨)
    
    .EXAMPLE
        Test-CommandExists -CommandName 'rustc'
        False
        # Rust not installed (as it should be, Rust is cope)
    
    .NOTES
        ✨ PURE FUNCTION ✨
        This is referentially transparent and has no side effects.
    #>
    [CmdletBinding()]
    [OutputType([bool])]
    param(
        [Parameter(Mandatory = $true)]
        [ValidateNotNullOrEmpty()]
        [string]$CommandName
    )
    
    $null -ne (Get-Command -Name $CommandName -ErrorAction SilentlyContinue)
}

function Get-ToolPath {
    <#
    .SYNOPSIS
        Finds tool in PATH and returns full path (pure function!)
    
    .DESCRIPTION
        Searches for tool in PATH and returns full path if found, $null if not.
        This is functional error handling - return optional value instead of
        throwing exceptions. Like Option<T> in Rust but we don't talk about Rust.
    
    .PARAMETER ToolName
        Name of tool to find (e.g., 'cmake.exe', 'g++.exe')
    
    .OUTPUTS
        System.String or $null
        Full path to tool if found, $null otherwise
    
    .EXAMPLE
        $cmakePath = Get-ToolPath -ToolName 'cmake'
        if ($cmakePath) {
            Write-Host "Found CMake: $cmakePath"
        } else {
            Write-Error "CMake not found (the beautiful build system is missing!)"
        }
    
    .NOTES
        ✨ PURE FUNCTION ✨
        No side effects, deterministic output.
    #>
    [CmdletBinding()]
    [OutputType([string])]
    param(
        [Parameter(Mandatory = $true)]
        [ValidateNotNullOrEmpty()]
        [string]$ToolName
    )
    
    $command = Get-Command -Name $ToolName -ErrorAction SilentlyContinue
    if ($command) {
        return $command.Source
    }
    
    return $null
}

function Test-BuildEnvironment {
    <#
    .SYNOPSIS
        Validates build environment has required tools
    
    .DESCRIPTION
        Checks that CMake and GCC are installed and accessible. Returns
        custom object with validation results - functional error handling
        that provides structured data instead of just throwing uwu
    
    .OUTPUTS
        PSCustomObject with properties:
        - IsValid (bool): true if all tools found
        - CMakePath (string): path to CMake or $null
        - GccPath (string): path to GCC or $null
        - MissingTools (string[]): array of missing tool names
    
    .EXAMPLE
        $env = Test-BuildEnvironment
        if ($env.IsValid) {
            Write-Host "Environment valid! Using CMake: $($env.CMakePath)"
        } else {
            Write-Error "Missing tools: $($env.MissingTools -join ', ')"
        }
    
    .NOTES
        ✨ PURE FUNCTION ✨
        Only reads environment, doesn't modify anything.
    #>
    [CmdletBinding()]
    [OutputType([PSCustomObject])]
    param()
    
    Write-Verbose 'Validating build environment...'
    
    # find required tools (NO HARDCODED PATHS!)
    $cmakePath = Get-ToolPath -ToolName 'cmake'
    $gccPath = Get-ToolPath -ToolName 'g++'
    
    # collect missing tools
    $missingTools = @()
    if (-not $cmakePath) { $missingTools += 'CMake' }
    if (-not $gccPath) { $missingTools += 'GCC' }
    
    # return structured result object
    return [PSCustomObject]@{
        IsValid = ($missingTools.Count -eq 0)
        CMakePath = $cmakePath
        GccPath = $gccPath
        MissingTools = $missingTools
    }
}

function Invoke-CleanBuildDirectory {
    <#
    .SYNOPSIS
        Cleans and recreates build directory
    
    .DESCRIPTION
        Removes existing build directory and creates fresh one. This has
        side effects (file I/O) so it's not pure, but we isolate impure
        operations at boundaries (functional architecture uwu)
    
    .PARAMETER Path
        Path to build directory
    
    .OUTPUTS
        PSCustomObject with properties:
        - Success (bool): true if operation succeeded
        - Message (string): status message
    
    .EXAMPLE
        $result = Invoke-CleanBuildDirectory -Path './build'
        if ($result.Success) {
            Write-Host $result.Message
        }
    
    .NOTES
        ⚠️ IMPURE FUNCTION (has side effects)
        This function modifies the file system.
    #>
    [CmdletBinding(SupportsShouldProcess)]
    [OutputType([PSCustomObject])]
    param(
        [Parameter(Mandatory = $true)]
        [ValidateNotNullOrEmpty()]
        [string]$Path
    )
    
    try {
        if (Test-Path -Path $Path) {
            if ($PSCmdlet.ShouldProcess($Path, 'Remove build directory')) {
                Write-Verbose "Removing existing build directory: $Path"
                Remove-Item -Path $Path -Recurse -Force -ErrorAction Stop
            }
        }
        
        if ($PSCmdlet.ShouldProcess($Path, 'Create build directory')) {
            Write-Verbose "Creating build directory: $Path"
            New-Item -Path $Path -ItemType Directory -Force | Out-Null
        }
        
        return [PSCustomObject]@{
            Success = $true
            Message = "Build directory ready: $Path"
        }
    }
    catch {
        return [PSCustomObject]@{
            Success = $false
            Message = "Failed to prepare build directory: $_"
        }
    }
}

function Invoke-CMakeConfigure {
    <#
    .SYNOPSIS
        Configures project with CMake
    
    .DESCRIPTION
        Runs CMake configuration step. Returns structured result object
        for functional error handling instead of exceptions uwu
    
    .PARAMETER SourcePath
        Path to source directory (where CMakeLists.txt is)
    
    .PARAMETER BuildPath
        Path to build directory
    
    .PARAMETER Configuration
        Build configuration (Debug or Release)
    
    .PARAMETER Generator
        CMake generator to use (e.g., 'MinGW Makefiles')
    
    .OUTPUTS
        PSCustomObject with properties:
        - Success (bool): true if configuration succeeded
        - Message (string): status message
        - Output (string): CMake output
    
    .EXAMPLE
        $result = Invoke-CMakeConfigure `
            -SourcePath '.' `
            -BuildPath './build' `
            -Configuration 'Release' `
            -Generator 'MinGW Makefiles'
    
    .NOTES
        ⚠️ IMPURE FUNCTION (runs external process)
        Has side effects (creates files, runs CMake).
    #>
    [CmdletBinding()]
    [OutputType([PSCustomObject])]
    param(
        [Parameter(Mandatory = $true)]
        [string]$SourcePath,
        
        [Parameter(Mandatory = $true)]
        [string]$BuildPath,
        
        [Parameter(Mandatory = $true)]
        [ValidateSet('Debug', 'Release')]
        [string]$Configuration,
        
        [Parameter(Mandatory = $true)]
        [string]$Generator
    )
    
    Write-Verbose 'Configuring project with CMake...'
    
    Push-Location -Path $BuildPath
    
    try {
        $cmakeArgs = @(
            $SourcePath
            '-G', $Generator
            "-DCMAKE_BUILD_TYPE=$Configuration"
        )
        
        Write-Verbose "Running: cmake $($cmakeArgs -join ' ')"
        
        $output = & cmake @cmakeArgs 2>&1 | Out-String
        
        if ($LASTEXITCODE -eq 0) {
            return [PSCustomObject]@{
                Success = $true
                Message = 'CMake configuration successful (immaculate vibes ✨)'
                Output = $output
            }
        }
        else {
            return [PSCustomObject]@{
                Success = $false
                Message = 'CMake configuration failed (sad)'
                Output = $output
            }
        }
    }
    finally {
        Pop-Location
    }
}

function Invoke-CMakeBuild {
    <#
    .SYNOPSIS
        Builds project with CMake
    
    .DESCRIPTION
        Runs CMake build step. Returns structured result for functional
        error handling (no exceptions thrown, just return status).
    
    .PARAMETER BuildPath
        Path to build directory
    
    .PARAMETER Configuration
        Build configuration (Debug or Release)
    
    .OUTPUTS
        PSCustomObject with properties:
        - Success (bool): true if build succeeded
        - Message (string): status message
        - Output (string): build output
    
    .EXAMPLE
        $result = Invoke-CMakeBuild -BuildPath './build' -Configuration 'Release'
        if (-not $result.Success) {
            Write-Error $result.Message
        }
    
    .NOTES
        ⚠️ IMPURE FUNCTION (runs external process)
        Has side effects (compiles code, creates binaries).
    #>
    [CmdletBinding()]
    [OutputType([PSCustomObject])]
    param(
        [Parameter(Mandatory = $true)]
        [string]$BuildPath,
        
        [Parameter(Mandatory = $true)]
        [ValidateSet('Debug', 'Release')]
        [string]$Configuration
    )
    
    Write-Verbose 'Building project...'
    
    try {
        $buildArgs = @(
            '--build', $BuildPath
            '--config', $Configuration
        )
        
        Write-Verbose "Running: cmake $($buildArgs -join ' ')"
        
        $output = & cmake @buildArgs 2>&1 | Out-String
        
        if ($LASTEXITCODE -eq 0) {
            return [PSCustomObject]@{
                Success = $true
                Message = 'Build successful (code goes brrr 🚀)'
                Output = $output
            }
        }
        else {
            return [PSCustomObject]@{
                Success = $false
                Message = 'Build failed (compiler said no)'
                Output = $output
            }
        }
    }
    catch {
        return [PSCustomObject]@{
            Success = $false
            Message = "Build error: $_"
            Output = $_.Exception.Message
        }
    }
}

function Invoke-Tests {
    <#
    .SYNOPSIS
        Runs test executable if it exists
    
    .DESCRIPTION
        Searches for test executable and runs it. Returns structured result
        with test output and status (functional error handling uwu).
    
    .PARAMETER BuildPath
        Path to build directory
    
    .OUTPUTS
        PSCustomObject with properties:
        - Success (bool): true if tests passed (or no tests found)
        - TestsRun (bool): true if tests were actually run
        - Message (string): status message
        - Output (string): test output
    
    .EXAMPLE
        $result = Invoke-Tests -BuildPath './build'
        if ($result.TestsRun) {
            Write-Host "Tests: $($result.Success ? 'PASSED' : 'FAILED')"
        }
    
    .NOTES
        ⚠️ IMPURE FUNCTION (runs external process)
        Has side effects (runs tests).
    #>
    [CmdletBinding()]
    [OutputType([PSCustomObject])]
    param(
        [Parameter(Mandatory = $true)]
        [string]$BuildPath
    )
    
    Write-Verbose 'Looking for test executable...'
    
    # find test executable (common names)
    $testPaths = @(
        (Join-Path $BuildPath 'tests.exe')
        (Join-Path $BuildPath 'tests')
        (Join-Path $BuildPath 'test.exe')
        (Join-Path $BuildPath 'test')
    )
    
    $testExe = $testPaths | Where-Object { Test-Path $_ } | Select-Object -First 1
    
    if (-not $testExe) {
        return [PSCustomObject]@{
            Success = $true
            TestsRun = $false
            Message = 'No test executable found (skipping tests)'
            Output = ''
        }
    }
    
    Write-Verbose "Running tests: $testExe"
    
    try {
        $output = & $testExe 2>&1 | Out-String
        
        if ($LASTEXITCODE -eq 0) {
            return [PSCustomObject]@{
                Success = $true
                TestsRun = $true
                Message = 'Tests passed! (immaculate vibes ✨)'
                Output = $output
            }
        }
        else {
            return [PSCustomObject]@{
                Success = $false
                TestsRun = $true
                Message = 'Tests failed (some tests did not pass)'
                Output = $output
            }
        }
    }
    catch {
        return [PSCustomObject]@{
            Success = $false
            TestsRun = $true
            Message = "Test execution error: $_"
            Output = $_.Exception.Message
        }
    }
}

# ============================================================================
# Main Script Logic (functional pipeline!)
# ============================================================================

Write-Host '============================================================' -ForegroundColor Cyan
Write-Host " Building C++ Project (functional programming edition uwu)" -ForegroundColor Cyan
Write-Host '============================================================' -ForegroundColor Cyan
Write-Host ''

# Step 1: Validate environment (pure function - just reads)
$environment = Test-BuildEnvironment

if (-not $environment.IsValid) {
    Write-Error "Missing required tools: $($environment.MissingTools -join ', ')"
    Write-Host ''
    Write-Host 'Please install:' -ForegroundColor Yellow
    if ($environment.MissingTools -contains 'CMake') {
        Write-Host '  - CMake: https://cmake.org/download/ (the beautiful build system!)' -ForegroundColor Yellow
    }
    if ($environment.MissingTools -contains 'GCC') {
        Write-Host '  - GCC: https://gcc.gnu.org/ (compiler supremacy, not Rust)' -ForegroundColor Yellow
    }
    exit 1
}

Write-Host '✓ Environment validated' -ForegroundColor Green
Write-Host "  CMake: $($environment.CMakePath)" -ForegroundColor Gray
Write-Host "  GCC:   $($environment.GccPath)" -ForegroundColor Gray
Write-Host ''

# Step 2: Clean build directory if requested (impure - file I/O)
if ($Clean) {
    $cleanResult = Invoke-CleanBuildDirectory -Path $BuildDir
    
    if (-not $cleanResult.Success) {
        Write-Error $cleanResult.Message
        exit 1
    }
    
    Write-Host '✓ Build directory cleaned' -ForegroundColor Green
    Write-Host ''
}
else {
    # create build directory if it doesn't exist
    if (-not (Test-Path -Path $BuildDir)) {
        New-Item -Path $BuildDir -ItemType Directory -Force | Out-Null
    }
}

# Step 3: Configure with CMake (impure - runs CMake)
$configResult = Invoke-CMakeConfigure `
    -SourcePath $ProjectRoot `
    -BuildPath $BuildDir `
    -Configuration $Configuration `
    -Generator $CMakeGenerator

if ($PSCmdlet.MyInvocation.BoundParameters['Verbose']) {
    Write-Host $configResult.Output -ForegroundColor Gray
}

if (-not $configResult.Success) {
    Write-Error $configResult.Message
    Write-Host $configResult.Output -ForegroundColor Red
    exit 1
}

Write-Host '✓ CMake configuration complete' -ForegroundColor Green
Write-Host ''

# Step 4: Build project (impure - runs compiler)
$buildResult = Invoke-CMakeBuild `
    -BuildPath $BuildDir `
    -Configuration $Configuration

if ($PSCmdlet.MyInvocation.BoundParameters['Verbose']) {
    Write-Host $buildResult.Output -ForegroundColor Gray
}

if (-not $buildResult.Success) {
    Write-Error $buildResult.Message
    Write-Host $buildResult.Output -ForegroundColor Red
    exit 1
}

Write-Host '✓ Build complete' -ForegroundColor Green
Write-Host ''

# Step 5: Run tests if requested (impure - runs tests)
if ($RunTests) {
    $testResult = Invoke-Tests -BuildPath $BuildDir
    
    if ($testResult.TestsRun) {
        if ($PSCmdlet.MyInvocation.BoundParameters['Verbose']) {
            Write-Host $testResult.Output -ForegroundColor Gray
        }
        
        if ($testResult.Success) {
            Write-Host '✓ Tests passed' -ForegroundColor Green
        }
        else {
            Write-Error $testResult.Message
            Write-Host $testResult.Output -ForegroundColor Red
            exit 1
        }
    }
    else {
        Write-Host '- No tests found' -ForegroundColor Yellow
    }
    Write-Host ''
}

# Success! (functional pipeline completed uwu)
Write-Host '============================================================' -ForegroundColor Cyan
Write-Host ' Build completed successfully! ✨' -ForegroundColor Cyan
Write-Host '============================================================' -ForegroundColor Cyan
Write-Host ''
Write-Host "Configuration: $Configuration" -ForegroundColor Gray
Write-Host "Build directory: $BuildDir" -ForegroundColor Gray
Write-Host ''
Write-Host 'functional programming gang rise up uwu 💜' -ForegroundColor Magenta
```

## Quality Checklist

- [ ] **PowerShell 7+ required** (latest version/beta preferred!)
- [ ] **comment-based help** on ALL functions
- [ ] **approved verbs** only (Get-Verb)
- [ ] **no aliases** in scripts (Write-Host not echo)
- [ ] **pure functions** where possible (mark purity status)
- [ ] **structured return objects** (not exceptions for business logic)
- [ ] **pipeline support** (accept from pipeline where appropriate)
- [ ] **ShouldProcess** for destructive operations
- [ ] **NO HARDCODED PATHS** (find tools dynamically)
- [ ] **parameter validation** (ValidateSet, ValidateNotNullOrEmpty)
- [ ] **Set-StrictMode** enabled
- [ ] **$ErrorActionPreference = 'Stop'** for errors
- [ ] **excessive comments** (document everything!)

**remember**: PowerShell is the functional scripting language Microsoft
accidentally created. Use the pipeline, embrace objects over strings, and
make those cmdlets as pure as possible uwu 💜✨

seize the means of compilation (and automation)!