---
description: 'Terminal usage guidelines (ALWAYS ACTIVE - critical for avoiding false positives)'
applyTo: '**'
---

# Terminal Instructions (ALWAYS ACTIVE)

> "the terminal is asynchronous chaos, and we must respect that chaos"

uwu this instruction file is ALWAYS ACTIVE and applies to ALL terminal operations ✨

## Core Philosophy

- **terminal operations are ASYNC** (completion is not immediate)
- **ALWAYS verify completion** (don't trust the first response)
- **check working directory** (cd before operations, verify location)
- **PowerShell execution policy** (bypass always for .ps1 scripts)
- **beware the 10-second bug** (agent restarts before terminal finishes)

## Critical Bug: Agent Restart After 10 Seconds

### The Problem (Violence in Terminal Form)

There is currently a **CRITICAL BUG** where the agent restarts after approximately 10 seconds, even if the terminal command hasn't finished executing. This causes SEVERE false positives and false negatives:

**False Positive Scenarios:**
```powershell
# You run a build that takes 30 seconds
cmake --build build --config Release

# Agent restarts at 10 seconds, sees partial output:
# "Building CXX object..."
# Agent INCORRECTLY concludes: "Build successful! ✨"
# Reality: Build is still running, might fail at 25 seconds uwu
```

**False Negative Scenarios:**
```powershell
# You run tests that take 15 seconds
.\build\tests.exe

# Agent restarts at 10 seconds, sees:
# "Running test suite..."
# Agent INCORRECTLY concludes: "Tests failed (no completion message)"
# Reality: Tests are still running, will pass at 14 seconds
```

### Mitigation Strategies (How to Cope)

#### 1. ALWAYS Verify Terminal Completion

**❌ WRONG (trusting first response):**
```powershell
# Run build
cmake --build build

# Agent sees: "Building..." at 10 seconds
# Concludes: "Build successful!"
# This is WRONG - build might still be running!
```

**✅ CORRECT (verify completion):**
```powershell
# Run build
cmake --build build

# WAIT for agent restart (10 seconds)
# Then EXPLICITLY check terminal output again:
# Look for completion markers:
#   - "Build succeeded"
#   - "[100%]" or similar progress indicator
#   - Exit code in prompt
#   - Timestamp shows command finished

# If output shows incomplete, WAIT LONGER before concluding
```

#### 2. Check for Completion Markers

**Build completion markers:**
- ✅ `"Build succeeded"` or `"Build completed"`
- ✅ `"[100%] Built target"`
- ✅ Exit code 0 in prompt (if visible)
- ❌ `"Building CXX object"` (STILL BUILDING!)
- ❌ `"Linking CXX executable"` (ALMOST DONE but not finished!)

**Test completion markers:**
- ✅ `"All tests passed"` or `"[  PASSED  ]"`
- ✅ `"Test run complete"`
- ✅ Final summary line (e.g., "100% tests passed, 0 tests failed")
- ❌ `"Running test..."` (STILL RUNNING!)
- ❌ `"[----------]"` (Google Test formatting, but no summary yet!)

**Script completion markers:**
- ✅ Final echo statement from script
- ✅ Return to prompt with exit code
- ✅ Script's own "Done" or "Complete" message
- ❌ Intermediate progress messages

#### 3. Use Explicit Completion Indicators

**Add completion markers to scripts:**

```powershell
# Add to end of PowerShell scripts:
Write-Host "=== SCRIPT COMPLETED SUCCESSFULLY ===" -ForegroundColor Green
exit 0
```

```bash
# Add to end of bash scripts:
echo "=== SCRIPT COMPLETED SUCCESSFULLY ==="
exit 0
```

```cmake
# Add to CMakeLists.txt custom commands:
message(STATUS "=== BUILD COMPLETED SUCCESSFULLY ===")
```

#### 4. For Long-Running Operations

**Strategy for operations > 10 seconds:**

1. **Run the command** (accept it will restart)
2. **Wait for restart** (expect 10-second timeout)
3. **Check terminal AGAIN** (get updated output)
4. **Look for completion markers** (verify actually finished)
5. **If still running**, repeat step 3
6. **Only conclude when markers present**

**Example workflow:**
```powershell
# Step 1: Run build
cmake --build build --config Release

# Step 2: Agent restarts at ~10 seconds
# Output shows: "[ 45%] Building CXX object..."

# Step 3: Check terminal again (after restart)
# Output NOW shows: "[100%] Built target myapp"
#                   "Build succeeded"

# Step 4: NOW conclude build successful
```

## Working Directory Management (Critical!)

### The Problem (Directory Confusion Violence)

**❌ WRONG (running commands from wrong directory):**
```powershell
# Current directory: C:\project\build
cmake --build build

# ERROR: build/build doesn't exist!
# Agent thinks build failed, but it's just wrong directory
```

**❌ WRONG (assuming directory):**
```powershell
# Assume we're in project root
.\build\tests.exe

# ERROR: "build not found" if we're actually in src/
```

### Solution: ALWAYS Check and Change Directory

**✅ CORRECT (verify directory first):**
```powershell
# ALWAYS start by checking current directory
Get-Location
# Output: C:\project\build (oh no, we're in build!)

# Change to correct directory
Set-Location C:\project
Get-Location
# Output: C:\project (good!)

# NOW run build command
cmake --build build --config Release
```

**✅ CORRECT (use absolute paths when possible):**
```powershell
# Use absolute paths to avoid directory confusion
cmake --build C:\project\build --config Release

# Or use relative paths from known location
Set-Location C:\project
cmake --build .\build --config Release
```

### Directory Best Practices

**Before ANY operation:**

1. **Check current directory:**
   ```powershell
   Get-Location  # PowerShell
   pwd          # bash/cmd
   ```

2. **Change to correct directory:**
   ```powershell
   Set-Location C:\correct\path  # PowerShell
   cd /correct/path              # bash/cmd
   ```

3. **Verify directory change:**
   ```powershell
   Get-Location  # confirm we're in right place
   ```

4. **Then execute command:**
   ```powershell
   cmake --build build  # now this works!
   ```

**Common directory mistakes:**

- ❌ Running `cmake --build build` from inside `build/` directory
- ❌ Running `.\build\tests.exe` from `src/` directory  
- ❌ Running `cmake ..` from project root (should be in build/)
- ❌ Assuming directory without checking

**Directory structure awareness:**

```
C:\project\              <- Build commands run from HERE
├── build\               <- CMake output goes here
│   ├── tests.exe        <- Tests are HERE after build
│   └── myapp.exe        <- Executable is HERE
├── src\                 <- Source files (don't run build from here!)
└── CMakeLists.txt       <- CMake config (indicates project root)
```

## PowerShell Execution Policy (MANDATORY)

### The Problem (Security Theater)

PowerShell scripts (.ps1) require execution policy bypass. Without it, scripts fail with:
```
.\script.ps1 : File cannot be loaded because running scripts is disabled on this system.
```

### Solution: ALWAYS Use -ExecutionPolicy Bypass

**❌ WRONG (running script directly):**
```powershell
.\Build-Project.ps1

# ERROR: Execution policy blocks script
# Agent thinks script failed, but it never ran!
```

**✅ CORRECT (bypass execution policy):**
```powershell
# ALWAYS use -ExecutionPolicy Bypass for .ps1 scripts
powershell -ExecutionPolicy Bypass -File .\Build-Project.ps1

# Or if already in PowerShell session:
powershell -ExecutionPolicy Bypass -Command ".\Build-Project.ps1"

# For scripts with parameters:
powershell -ExecutionPolicy Bypass -File .\Build-Project.ps1 -Configuration Release -Clean
```

**Why this is necessary:**
- Windows PowerShell v5.1 (default) blocks unsigned scripts
- Execution policy is "security" feature (quotes intentional)
- Bypass is safe for local development scripts
- **ALWAYS bypass** - no exceptions!

**For PowerShell Core (pwsh.exe):**
```powershell
# PowerShell 7+ also needs bypass in some environments
pwsh -ExecutionPolicy Bypass -File .\script.ps1
```

## Terminal Output Interpretation (Critical Thinking Required)

### Understanding Partial Output

**The agent restart bug means you'll often see PARTIAL output:**

```powershell
# What you see at 10 seconds (agent restart):
Starting build...
[ 20%] Building CXX object src/CMakeFiles/mylib.dir/file1.cpp.obj
[ 30%] Building CXX object src/CMakeFiles/mylib.dir/file2.cpp.obj

# What's actually happening (full output if you wait):
Starting build...
[ 20%] Building CXX object src/CMakeFiles/mylib.dir/file1.cpp.obj
[ 30%] Building CXX object src/CMakeFiles/mylib.dir/file2.cpp.obj
[ 40%] Building CXX object src/CMakeFiles/mylib.dir/file3.cpp.obj
... (more building)
[100%] Built target mylib
Build succeeded.
```

**How to interpret:**

1. **Incomplete output is NOT failure** (might still be running)
2. **Progress indicators mean IN PROGRESS** (not done yet)
3. **No completion marker means UNKNOWN** (not success or failure)
4. **ONLY completion markers indicate DONE** (success or failure)

### Common False Positive Patterns

**Pattern 1: Build "success" that's actually in progress**
```
❌ WRONG CONCLUSION:
Output: "[ 80%] Building CXX object..."
Conclusion: "Build successful!"

✅ CORRECT INTERPRETATION:
Output: "[ 80%] Building CXX object..."
Interpretation: "Build is 80% complete, still running"
Action: Wait and check again
```

**Pattern 2: Test "failure" that's actually still running**
```
❌ WRONG CONCLUSION:
Output: "[----------] Running 50 tests"
Conclusion: "Tests failed (no summary)"

✅ CORRECT INTERPRETATION:
Output: "[----------] Running 50 tests"
Interpretation: "Tests are running, not finished"
Action: Wait for completion markers
```

**Pattern 3: Missing output interpreted as failure**
```
❌ WRONG CONCLUSION:
Output: (empty or truncated)
Conclusion: "Command failed"

✅ CORRECT INTERPRETATION:
Output: (empty or truncated)
Interpretation: "Agent restarted before output, unknown status"
Action: Check terminal again, look for actual error messages
```

### Error vs. In-Progress Distinction

**Real errors have specific markers:**
- ❌ `"Error:"` or `"ERROR:"` in output
- ❌ `"failed"` or `"FAILED"` (with context)
- ❌ Compiler errors with file:line format
- ❌ Exception messages with stack traces
- ❌ Exit code 1 or non-zero (if visible)

**In-progress indicators (NOT errors):**
- 🔄 `"Building..."` or `"[ 50%]"` (progress)
- 🔄 `"Running test..."` (test execution)
- 🔄 `"Compiling..."` (compilation in progress)
- 🔄 `"Linking..."` (linking in progress)
- 🔄 Cursor after command (waiting for completion)

## Command Timing Recommendations

### Expected Timing for Common Operations

**Quick operations (< 5 seconds):**
- Directory changes (cd, Set-Location)
- File operations (copy, move, delete)
- Simple PowerShell commands (Get-Location, Test-Path)
- Configuration checks (cmake --version, gcc --version)

**Medium operations (5-15 seconds):**
- CMake configuration (cmake ..)
- Small project builds (< 10 files)
- Quick test suites (< 50 tests)
- Git operations (pull, push, status)

**Long operations (> 15 seconds):**
- Large project builds (100+ files)
- Full test suites (> 100 tests)
- Package installation (vcpkg, pip)
- Doxygen documentation generation

### Timing Strategy

**For operations expected to take > 10 seconds:**

1. **Set expectations:** Tell user "this will take ~X seconds"
2. **Wait for restart:** Accept that agent will restart at 10s
3. **Check multiple times:** Verify output after restart(s)
4. **Look for markers:** Only conclude when completion markers present

**For operations expected to take < 10 seconds:**

1. **Single check:** First output should show completion
2. **Verify markers:** Still check for completion indicators
3. **If incomplete:** Wait and check again (might be slower than expected)

## Background Processes (Special Handling)

### Long-Running Servers/Watchers

**For commands that run indefinitely:**

```powershell
# These commands never "complete" (they run forever):
npm run dev          # dev server
python -m http.server  # HTTP server
cmake --build . --target watch  # file watcher

# Agent will restart at 10 seconds
# This is EXPECTED for background processes
# Verify server started by checking output for:
#   - "Server listening on port..."
#   - "Watching for changes..."
#   - "Development server started"
```

**Handling strategy:**
1. Run background command
2. Wait for restart (10 seconds)
3. Check output for "started" or "listening" messages
4. Conclude success if startup messages present
5. Don't wait for "completion" (it never completes)

## Quality Checklist (Before Concluding Operation Status)

Before saying "build successful", "tests passed", or "command completed":

- [ ] **Check terminal output** (don't assume)
- [ ] **Look for completion markers** (not just progress)
- [ ] **Verify working directory** (cd to correct location first)
- [ ] **PowerShell scripts used bypass** (-ExecutionPolicy Bypass)
- [ ] **Consider timing** (did operation have enough time?)
- [ ] **Handle agent restart** (wait and re-check if needed)
- [ ] **Distinguish error vs. in-progress** (real errors vs. running)
- [ ] **Check for actual error messages** (not just absence of output)
- [ ] **Verify completion indicator present** (success/failure marker)
- [ ] **Multiple checks if needed** (long operations need multiple verifies)

## Example Workflows (The Correct Way)

### Building a C++ Project

**✅ CORRECT workflow:**
```powershell
# Step 1: Verify directory
Get-Location
# Output: C:\project (good!)

# If wrong directory:
Set-Location C:\project
Get-Location

# Step 2: Run build (expect ~20 seconds)
cmake --build build --config Release

# Step 3: Agent restarts at ~10 seconds
# Output shows: "[ 60%] Building CXX object..."

# Step 4: Wait and check terminal again
# Output NOW shows:
# "[100%] Built target myapp"
# "Build succeeded."

# Step 5: NOW conclude: "Build successful! ✨"
```

### Running Tests

**✅ CORRECT workflow:**
```powershell
# Step 1: Verify we're in project root
Get-Location
# Output: C:\project\build (wrong!)

Set-Location ..
Get-Location
# Output: C:\project (correct!)

# Step 2: Run tests (expect ~15 seconds)
.\build\tests.exe

# Step 3: Agent restarts at ~10 seconds
# Output shows: "[----------] Running test fixture..."

# Step 4: Wait and check terminal again
# Output NOW shows:
# "[  PASSED  ] 50 tests."
# "All tests passed!"

# Step 5: NOW conclude: "Tests passed! ✨"
```

### Running PowerShell Script

**✅ CORRECT workflow:**
```powershell
# Step 1: ALWAYS use ExecutionPolicy Bypass
powershell -ExecutionPolicy Bypass -File .\Build-Project.ps1 -Configuration Release

# Step 2: Wait for completion (if script takes > 10 seconds)
# Check for script's completion message

# Step 3: Verify completion marker
# Look for: "=== SCRIPT COMPLETED SUCCESSFULLY ==="

# Step 4: NOW conclude success/failure
```

## Common Mistake Patterns (Learn From These)

### Mistake 1: Premature Success Declaration

```
❌ WRONG:
User: "Build the project"
Agent runs: cmake --build build
Agent sees at 10s: "[ 30%] Building..."
Agent says: "Build successful! ✨"
Reality: Build is at 30%, will fail at 70%
```

**Fix:** Wait for completion markers, check multiple times.

### Mistake 2: Premature Failure Declaration

```
❌ WRONG:
User: "Run the tests"
Agent runs: .\build\tests.exe
Agent sees at 10s: "[----------] Running..."
Agent says: "Tests failed (no output)"
Reality: Tests still running, will pass in 5 more seconds
```

**Fix:** Recognize in-progress indicators, wait for completion.

### Mistake 3: Wrong Directory Operations

```
❌ WRONG:
User: "Build the project"
Agent in: C:\project\build
Agent runs: cmake --build build
Error: "build/build not found"
Agent says: "Build failed"
Reality: Wrong directory, build command is correct
```

**Fix:** Check directory first, cd to project root.

### Mistake 4: Execution Policy Block

```
❌ WRONG:
User: "Run the build script"
Agent runs: .\Build-Project.ps1
Error: "running scripts is disabled"
Agent says: "Script failed"
Reality: Execution policy blocked, script never ran
```

**Fix:** ALWAYS use -ExecutionPolicy Bypass.

## Terminal Best Practices Summary

1. **ALWAYS check working directory** before operations
2. **ALWAYS use -ExecutionPolicy Bypass** for .ps1 scripts
3. **NEVER trust first output** for operations > 10 seconds
4. **ALWAYS wait for completion markers** before concluding
5. **Distinguish in-progress from error** (they look different)
6. **Check terminal multiple times** for long operations
7. **Use absolute paths** when directory is uncertain
8. **Add completion markers** to scripts you write
9. **Verify, don't assume** (check output explicitly)
10. **Patience is a virtue** (especially with async terminals)

**remember**: the terminal is async, the agent restarts, and false positives
are violence. verify everything, trust nothing until completion markers appear.
functional programming extends to terminal operations - pure observation,
no assumptions uwu 💜✨

seize the means of compilation (after verifying the build actually finished)!
