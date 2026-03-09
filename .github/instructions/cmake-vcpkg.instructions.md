---
description: 'CMake and Vcpkg build system guidelines (modern target graph supremacy uwu)'
applyTo: 'CMakeLists.txt, **/*.cmake, CMakePresets.json, **/CMakePresets.json, vcpkg.json, **/vcpkg.json, vcpkg-configuration.json, **/vcpkg-configuration.json'
---

# CMake and Vcpkg Instructions (The Beautiful Build Graph)

> "CMake is not ugly — most people are just writing it like shell script with
> Stockholm syndrome"

uwu if you are touching `CMakeLists.txt`, `*.cmake`, `CMakePresets.json`,
`vcpkg.json`, `vcpkg-configuration.json`, overlay ports, triplets, or package
export files, this document is LAW.

CMake is a declarative target graph language. Vcpkg is a dependency and
packaging workflow that integrates with that graph. The moment you treat either
one like a folder of magical strings and copy-pasted flags, the build becomes a
haunted house full of ABI mismatches, missing include directories, broken
install rules, and CI jobs that mysteriously work only on one machine. We do
not live like that.

This file forces CMake and Vcpkg to behave like disciplined infrastructure:

- target-based
- transitive by default
- preset-driven
- manifest-mode first
- package-exportable
- cross-platform without cope
- release-note-aware for CMake 4.0 through 4.3
- documented so aggressively that future maintainers can stop guessing

## Core Philosophy (Non-Negotiable Build Axioms)

- **targets are the unit of truth**
- **properties beat global variables**
- **usage requirements are sacred**
- **presets are mandatory** for serious projects
- **Vcpkg manifest mode is default**
- **imported targets only** (variables are legacy cope)
- **installation and exportability are first-class**
- **CMake 4.3+ preferred** and **4.1+ minimum** for new work
- **policy ranges are mandatory**
- **hardcoded paths are banned**
- **`find_package(CONFIG)` beats ad hoc discovery**
- **generator expressions are normal** not scary
- **multi-config awareness is mandatory**
- **coverage, sanitizers, warnings, and docs are modular**
- **overlay ports and custom triplets are legitimate tools** when justified
- **comments explain why** the build graph exists, not merely what it spells
- **the build must be consumable by other projects** not just by the original
  author on a lucky Tuesday

## Why CMake and Vcpkg Are Based (And What Everyone Else Gets Wrong)

### What CMake gets right when used correctly

- ✅ targets model real build graph nodes
- ✅ usage requirements propagate include directories, compile features,
  definitions, and link dependencies transitively
- ✅ presets separate user intent from build-system logic
- ✅ package exports let projects behave like reusable infrastructure instead of
  bespoke local snowflakes
- ✅ toolchain files and triplets make cross-compiling and ABI control explicit
- ✅ built-in installation, packaging, testing, file API, tracing, and now 4.3
  instrumentation give one coherent ecosystem
- ✅ generator expressions let configuration-specific and language-specific logic
  stay attached to the target that owns it
- ✅ the 4.x line keeps pushing toward more explicit, queryable, policy-driven
  behavior instead of ancient implicit magic

### What people do wrong with CMake

- ❌ use directory-wide `include_directories()` and `link_directories()`
- ❌ stuff compiler flags into `CMAKE_CXX_FLAGS` like it's 2009
- ❌ glob source files and act shocked when reconfigure behavior is weird
- ❌ call `find_package()` but still link raw library variables manually
- ❌ hardcode `Debug` and `Release` logic around `CMAKE_BUILD_TYPE` while using a
  multi-config generator
- ❌ configure for one machine and never think about install/export/consumer use
- ❌ patch around dependency problems with random `-I`, `-L`, and environment
  variables instead of modelling the graph correctly
- ❌ treat policies as warning spam instead of behavior contracts
- ❌ let Vcpkg drift outside the manifest and baseline system until builds become
  unreproducible archaeology

### What Vcpkg gets right when used correctly

- ✅ integrates directly with CMake toolchain flow
- ✅ manifest mode makes dependencies part of the repository, not tribal memory
- ✅ features and baselines make dependency intent explicit
- ✅ overlay ports and registries let you patch or extend packages without lying
  to the main build
- ✅ triplets make ABI, CRT linkage, library linkage, and toolchain identity
  visible and reproducible
- ✅ package exports + Vcpkg manifests give a coherent producer/consumer story

### What people do wrong with Vcpkg

- ❌ use classic mode as the default in shared repos
- ❌ install packages manually and never write `vcpkg.json`
- ❌ forget to pin a baseline, then wonder why CI changed under them
- ❌ mix toolchains or compiler versions across dependencies and main targets
- ❌ patch package sources manually in installed trees instead of using overlay
  ports
- ❌ ignore triplets and assume one default ABI magically fits everything
- ❌ use package variables instead of imported targets

## Release-Aware Mindset for CMake 4.0 Through 4.3

You were explicit about reading the 4.0, 4.1, 4.2, and 4.3 release notes, so
here is the distilled doctrine they imply. This section is not a changelog dump.
It is the behavioral guidance those releases demand.

## CMake 4.0 changed the floor, so stop pretending 3.x habits are fine

CMake 4.0 matters because it is where several old compatibility crutches finally
stopped being cute.

### What 4.0 means for authoring style

- use `cmake_minimum_required(VERSION <min>...<max>)` so the project states both
  its minimum supported version and the policy era it is authored for
- stop relying on pre-3.5 compatibility behavior entirely
- prefer portable linker and archiver argument forwarding using `LINKER:` and
  `ARCHIVER:` instead of compiler-specific string soup
- model debugger behavior explicitly where relevant instead of assuming the IDE
  will guess the working directory correctly
- treat path casing consistently, especially on Windows; CMake 4.0 stopped
  covering for sloppy source path spelling
- assume preset output is quieter by default and use explicit verbose/debug modes
  when you want diagnostic output

### 4.0 features you should actually use

#### `cmake_minimum_required` with a policy range

```cmake
cmake_minimum_required(VERSION 4.1...4.3 FATAL_ERROR)
```

This is based because:

- it allows a sane minimum
- it opts into policies through the newer authoring version
- it documents the era the project was written for
- it avoids the ancient-pattern clown show of pinning the minimum to whatever
  happened to exist when someone copy-pasted a template

#### Portable linker forwarding with `LINKER:`

```cmake
target_link_options(my_lib
    PRIVATE
        $<$<CXX_COMPILER_ID:GNU,Clang>:LINKER:-z,defs>
)
```

Do this instead of smashing raw `-Wl,` strings into global variables. The whole
point is to describe intent portably.

#### Portable archiver forwarding with `ARCHIVER:`

```cmake
set_property(TARGET my_static_lib APPEND PROPERTY
    STATIC_LIBRARY_OPTIONS
        "ARCHIVER:--thin"
)
```

If you need archiver-specific behavior, attach it to the target that owns the
archive step.

### 4.0 behaviors to keep in mind

- case consistency matters for project file paths
- `CMAKE_OSX_SYSROOT` behavior changed toward compiler-default selection, so do
  not cargo-cult old hardcoded sysroot assumptions into new projects
- older Visual Studio generator name/platform habits are gone; configure the
  platform properly rather than encoding it in generator strings
- `CMAKE_POLICY_VERSION_MINIMUM` exists for downstream packagers and users, but
  project authors should still write modern policy-aware files instead of hoping
  someone else rescues them

## CMake 4.1 made discovery, package integration, and transitive queries sharper

4.1 is the release where find behavior, configure logs, and transitive property
semantics got more serious.

### What 4.1 means for authoring style

- use imported targets for packages, not legacy result variables
- be aware that configure logs now surface more find-related diagnostics, which
  is excellent because mystery package discovery is cringe
- design `find_package()` calls to be explicit about requiredness and components
- stop pretending target transitivity is a side effect; it is now even more
  queryable and central
- be careful with regex assumptions because 4.1 changed important edge cases via
  policy

### 4.1 features you should actually use

#### `cmake_pkg_config()` when bridging with pkg-config

If you genuinely need to interoperate with `pkg-config`, use the modern command
instead of writing shell probes or bespoke parser nonsense.

```cmake
cmake_pkg_config(IMPORT zlib)
```

That is much cleaner than hand-rolling environment-based lookup logic.

#### Better default `find_*` strictness with `CMAKE_FIND_REQUIRED`

This can be useful in tightly controlled scopes, but do not spray it globally
without intent.

```cmake
block()
    set(CMAKE_FIND_REQUIRED TRUE)
    find_package(my_required_dep CONFIG)
    find_library(MY_REQUIRED_TOOL_LIBRARY NAMES my_required_tool)
endblock()
```

Scoped strictness is based. Global surprise strictness is not.

#### Configure-log-aware debugging

When package discovery is weird, do not guess. Turn on find diagnostics.

```cmake
set(CMAKE_FIND_DEBUG_MODE TRUE)
find_package(my_dep CONFIG REQUIRED)
set(CMAKE_FIND_DEBUG_MODE FALSE)
```

CMake 4.1 made discovery logging more visible. Use that instead of magical
rituals.

### 4.1 behaviors to keep in mind

- `FindGTest` variable outputs are deprecated in favor of `GTest::gtest` and
  `GTest::gtest_main`
- `GNUInstallDirs` behavior on special prefixes became more explicit; use the
  module correctly instead of hardcoding `lib`, `include`, or `bin`
- file-set ordering around `install(TARGETS)` is no longer semantically fragile,
  which is great because file sets should be data, not timing-sensitive spells
- imported target property queries became more transitive under policy control,
  which means your graph modelling matters even more

## CMake 4.2 expanded generator, platform, file-set, and intermediate-path power

4.2 is where CMake got noticeably better at describing object/intermediate file
behavior, file API richness, and practical build ergonomics.

### What 4.2 means for authoring style

- if your project exposes headers, file sets and header verification are now
  even more worth using
- if your project cares about object naming, install layout, or generated files,
  CMake now gives you better levers, so stop reaching for ad hoc custom commands
- be aware that imported-target config and location selection semantics were
  tightened; model configurations deliberately
- if you do platform or generator-specific work, remember FASTBuild and new
  cross-compiling workflows exist

### 4.2 features you should actually use

#### Explicit cache entry manipulation

Instead of ambiguous `set(... CACHE ...)` patterns, 4.2 gave a clearer style.

```cmake
set(CACHE{MYPROJECT_ENABLE_TOOLS} TYPE BOOL HELP "Build CLI tools" VALUE ON)
unset(CACHE{MYPROJECT_LEGACY_OVERRIDE})
```

This is more readable, more explicit, and less haunted.

#### `string(REGEX QUOTE)`

If you need to build a regex matching literal input, do not write escape salad.

```cmake
set(user_text "a+b(c)")
string(REGEX QUOTE escaped_literal "${user_text}")
string(REGEX MATCH "^${escaped_literal}$" exact_match "${user_text}")
```

#### File-set and source metadata querying

CMake 4.2 and 4.3 continue the trend of making file sets first-class. Use them.

```cmake
target_sources(my_lib
    PUBLIC
        FILE_SET public_headers
        TYPE HEADERS
        BASE_DIRS ${CMAKE_CURRENT_SOURCE_DIR}/include
        FILES
            ${CMAKE_CURRENT_SOURCE_DIR}/include/my_lib/api.hpp
            ${CMAKE_CURRENT_SOURCE_DIR}/include/my_lib/version.hpp
)
```

Then install them as file sets instead of duplicating header lists somewhere
else like a goblin.

#### `TARGET_INTERMEDIATE_DIR`

When custom commands genuinely need the target's intermediate directory, use the
proper query instead of reconstructing paths from undocumented assumptions.

```cmake
add_custom_command(TARGET my_lib POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E echo
        "$<TARGET_INTERMEDIATE_DIR:my_lib>"
)
```

### 4.2 behaviors to keep in mind

- imported target configuration selection changed; do not rely on accidental
  matches across irrelevant configurations
- Visual Studio defaults are being suppressed more aggressively so that project
  intent wins over IDE magic
- `CMAKE_PARENT_LIST_FILE` behavior changed in `CMakeLists.txt` processing
- per-source `JOB_POOL_COMPILE`, `OBJECT_NAME`, and install-object naming tools
  exist now, which means many old custom hacks should be deleted on sight

## CMake 4.3 is the big interoperability and observability release

4.3 is the reason this file is 4.3-first rather than merely 4.1-compatible.
It added features that materially change what "good modern CMake" looks like.

### What 4.3 means for authoring style

- package export/import should increasingly think in terms of CPS
  interoperability, not only hand-written CMake config files
- preset usage is no longer just convenience; it is a first-class part of the
  workflow and authoring surface
- instrumentation exists now, so configure/build/test/install performance and
  behavior can be observed with less guesswork
- per-language link flags and header verification became stronger tools, which
  means the build graph can express more policy in-target instead of in comments

### 4.3 features you should actually use

#### `project(... COMPAT_VERSION ... SPDX_LICENSE ...)`

If you are packaging and exporting a reusable project, this metadata matters.

```cmake
project(MyProject
    VERSION 1.2.0
    COMPAT_VERSION 1.0.0
    SPDX_LICENSE "MIT"
    DESCRIPTION "Reusable library with civilised packaging"
    HOMEPAGE_URL "https://example.com/my-project"
    LANGUAGES C CXX
)
```

The moment your build exports package metadata, you should think like a package
producer, not like a local-only script hoarder.

#### `install(PACKAGE_INFO)` and `export(PACKAGE_INFO)`

These support CPS generation. If you ship a reusable package, know this exists.
Even when you still ship classic config files, CMake 4.3 pushes toward richer
interoperability.

#### Instrumentation

Use instrumentation when you need real visibility into configure/build/test/
install cost instead of cargo-culting performance folklore.

```cmake
cmake_instrumentation(
    ENABLED ON
)
```

When appropriate, feed the results into trace viewers or dashboards. Build
systems deserve profiling too. They are code.

#### `cmake --version=json-v1`

Tools and scripts should query machine-readable version metadata rather than
scraping text blobs like raccoons.

#### Per-language link flags

4.3 added proper `CMAKE_<LANG>_LINK_FLAGS` variables. Use per-language link
intent when the language actually matters, instead of smashing everything into a
single global link string.

#### Private header verification

4.3 extended the header-verification story so projects can assert private header
self-sufficiency as well.

```cmake
set(CMAKE_VERIFY_PRIVATE_HEADER_SETS ON)
set_target_properties(my_lib PROPERTIES
    VERIFY_INTERFACE_HEADER_SETS ON
    VERIFY_PRIVATE_HEADER_SETS ON
)
```

This is based because header hygiene should be mechanically verified, not merely
manifesto'd.

### 4.3 behaviors to keep in mind

- `cmake -E tar` and archive extraction got stricter about unsafe paths; use the
  built-ins instead of insecure archive handling homebrew nonsense
- presets schema advanced again; keep preset files current
- the command-line interface got better at combining explicit build directories
  with presets; author workflows accordingly
- CPS support means package metadata quality matters even more

## Version Requirements (Bleeding Edge Only)

### CMake version policy

- **prefer: CMake 4.3+**
- **minimum: CMake 4.1** for new shared projects
- **4.0 is transitional** and acceptable only when a concrete consumer or CI
  environment genuinely blocks 4.1+
- **3.x for new work is banned**

### The correct `cmake_minimum_required` patterns

#### Greenfield project with full environment control

```cmake
cmake_minimum_required(VERSION 4.3 FATAL_ERROR)
```

Use this when you own the toolchain and CI environment and can simply require
modern CMake. This is the cleanest option.

#### Shared project that wants a sane floor and modern policy range

```cmake
cmake_minimum_required(VERSION 4.1...4.3 FATAL_ERROR)
```

Use this when:

- you want to support 4.1 and 4.2 users
- you want policies through the 4.3 authoring era
- you do not want 3.x compatibility ghosts haunting the file

#### What is banned

```cmake
# ❌ BANNED: ancient minimum with no policy range
cmake_minimum_required(VERSION 3.16)

# ❌ BANNED: policy version pinned way behind the authoring reality
cmake_policy(VERSION 3.16)

# ❌ BANNED: no minimum required at all
project(MyProject)
```

### Vcpkg version policy

- **prefer latest `vcpkg` tool**
- **manifest mode is mandatory**
- **pin a baseline** in `vcpkg-configuration.json` or within manifest
  configuration
- **overlay ports and registries are allowed** when solving a real problem
- **classic mode is not the default** in team or repository workflows

### Preset schema policy

- **prefer schema version 11** for `CMakePresets.json`
- keep preset files current with the CMake floor you claim to support
- do not pin ancient preset schema versions out of superstition

## Naming Conventions

```cmake
# project names: PascalCase or clear product names
project(MyProject LANGUAGES CXX)
project(MyLibrary LANGUAGES C CXX)

# option names: PROJECT_PREFIX_FEATURE_NAME
option(MYPROJECT_BUILD_TESTS "Build tests" ON)
option(MYPROJECT_ENABLE_COVERAGE "Enable coverage instrumentation" OFF)

# cache vars: PROJECT_PREFIX_SOMETHING
set(MYPROJECT_DEFAULT_WARNING_LEVEL "strict" CACHE STRING "Warning mode")

# interface helper targets: project_name::component style aliases
add_library(myproject_warnings INTERFACE)
add_library(MyProject::warnings ALIAS myproject_warnings)

# real targets: descriptive, lowercase_with_underscores or product names
add_library(myproject_core STATIC)
add_library(myproject_runtime SHARED)
add_executable(myproject_cli)

# exported namespace: PascalCase::Thing
install(EXPORT MyProjectTargets NAMESPACE MyProject:: ...)

# file sets: descriptive, semantic names
# public_headers, private_headers, generated_headers, module_interfaces

# preset names: short, workflow-oriented
# debug, release, relwithdebinfo, asan, tsan, coverage, ci-linux, ci-windows

# vcpkg features: lowercase-hyphenated
# tools, docs, gpu, server, cli, tests
```

### Banned naming patterns

```cmake
# ❌ BAD: options with no project prefix
option(BUILD_TESTS "..." ON)

# ❌ BAD: anonymous helper targets
add_library(common INTERFACE)

# ❌ BAD: exported namespace mismatch
add_library(my_lib)
add_library(Whatever::lib ALIAS my_lib)

# ❌ BAD: mystery preset names
# preset1, preset2, local, local2, final, final-final, real-final

# ❌ BAD: screaming ad hoc package vars used as API
set(MY_DEP_INCLUDE_DIR ...)
set(MY_DEP_LIBRARIES ...)
```

## Project Structure (How a Civilised Repository Looks)

```text
my-project/
├── CMakeLists.txt
├── CMakePresets.json
├── vcpkg.json
├── vcpkg-configuration.json
├── cmake/
│   ├── CompilerWarnings.cmake
│   ├── Sanitizers.cmake
│   ├── Coverage.cmake
│   ├── Docs.cmake
│   ├── Install.cmake
│   ├── Dependencies.cmake
│   ├── MyProjectConfig.cmake.in
│   └── toolchains/
│       ├── clang-libcxx.cmake
│       └── gcc-preview.cmake
├── src/
│   ├── CMakeLists.txt
│   ├── core/
│   ├── runtime/
│   └── cli/
├── include/
│   └── my_project/
├── tests/
│   ├── CMakeLists.txt
│   ├── unit/
│   └── integration/
├── docs/
├── scripts/
├── vcpkg-overlay/
│   ├── ports/
│   └── triplets/
└── examples/
```

### Structure rules

- root `CMakeLists.txt` defines the project, options, shared modules, install and
  export flow
- `src/` owns buildable implementation targets
- `include/` owns installed public headers
- `tests/` owns test targets; do not interleave test wiring randomly across
  production directories unless there is a compelling reason
- `cmake/` holds reusable modules, config templates, toolchains, and helper
  scripts that are actually part of the build-system architecture
- `vcpkg-overlay/` is where overlay ports and custom triplets live if you need
  them
- presets live at the root, not hidden in a side directory like contraband

## The Root `CMakeLists.txt` (How to Set the Tone Correctly)

Below is the generic root file pattern you should mentally start from. This is
not the only legal shape, but it is the default shape unless the project has a
real reason to differ.

```cmake
cmake_minimum_required(VERSION 4.1...4.3 FATAL_ERROR)

project(MyProject
    VERSION 1.2.0
    COMPAT_VERSION 1.0.0
    SPDX_LICENSE "MIT"
    DESCRIPTION "Reusable library and toolchain-friendly application"
    HOMEPAGE_URL "https://example.com/my-project"
    LANGUAGES C CXX
)

# -----------------------------------------------------------------------------
# Global defaults that are actually legitimate
# -----------------------------------------------------------------------------

set(CMAKE_C_STANDARD 23)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)

set(CMAKE_CXX_STANDARD 26)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

include(GNUInstallDirs)
include(CTest)

# -----------------------------------------------------------------------------
# Options
# -----------------------------------------------------------------------------

option(MYPROJECT_BUILD_TESTS "Build the test suite" ON)
option(MYPROJECT_BUILD_DOCS "Build API documentation" ON)
option(MYPROJECT_ENABLE_WARNINGS_AS_ERRORS "Treat warnings as errors" ON)
option(MYPROJECT_ENABLE_COVERAGE "Enable coverage instrumentation" OFF)
option(MYPROJECT_ENABLE_SANITIZERS "Enable sanitizer instrumentation" OFF)
option(MYPROJECT_ENABLE_LTO "Enable link-time optimisation" ON)
option(MYPROJECT_ENABLE_TOOLS "Build CLI tools" ON)
option(MYPROJECT_ENABLE_EXAMPLES "Build example programs" OFF)

# -----------------------------------------------------------------------------
# Modules
# -----------------------------------------------------------------------------

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")

include(CompilerWarnings)
include(Dependencies)
include(Install)

if(MYPROJECT_ENABLE_SANITIZERS)
    include(Sanitizers)
endif()

if(MYPROJECT_ENABLE_COVERAGE)
    include(Coverage)
endif()

if(MYPROJECT_BUILD_DOCS)
    include(Docs)
endif()

# -----------------------------------------------------------------------------
# Generated files
# -----------------------------------------------------------------------------

configure_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/cmake/version.hpp.in"
    "${CMAKE_CURRENT_BINARY_DIR}/generated/my_project/version.hpp"
    @ONLY
)

# -----------------------------------------------------------------------------
# Shared interface targets
# -----------------------------------------------------------------------------

add_library(myproject_warnings INTERFACE)
add_library(MyProject::warnings ALIAS myproject_warnings)

target_compile_features(myproject_warnings INTERFACE cxx_std_26)

target_compile_options(myproject_warnings INTERFACE
    $<$<CXX_COMPILER_ID:GNU,Clang>:-Wall -Wextra -Wpedantic>
    $<$<CXX_COMPILER_ID:MSVC>:/W4>
)

if(MYPROJECT_ENABLE_WARNINGS_AS_ERRORS)
    target_compile_options(myproject_warnings INTERFACE
        $<$<CXX_COMPILER_ID:GNU,Clang>:-Werror>
        $<$<CXX_COMPILER_ID:MSVC>:/WX>
    )
endif()

add_library(myproject_project_options INTERFACE)
add_library(MyProject::project_options ALIAS myproject_project_options)

target_compile_features(myproject_project_options INTERFACE c_std_23 cxx_std_26)

# -----------------------------------------------------------------------------
# Main targets
# -----------------------------------------------------------------------------

add_subdirectory(src)

if(MYPROJECT_BUILD_TESTS)
    enable_testing()
    add_subdirectory(tests)
endif()

if(MYPROJECT_ENABLE_EXAMPLES)
    add_subdirectory(examples)
endif()

# -----------------------------------------------------------------------------
# Summary output
# -----------------------------------------------------------------------------

message(STATUS "")
message(STATUS "MyProject configuration summary")
message(STATUS "  Version:            ${PROJECT_VERSION}")
message(STATUS "  Build tests:        ${MYPROJECT_BUILD_TESTS}")
message(STATUS "  Build docs:         ${MYPROJECT_BUILD_DOCS}")
message(STATUS "  Warnings as errors: ${MYPROJECT_ENABLE_WARNINGS_AS_ERRORS}")
message(STATUS "  Coverage:           ${MYPROJECT_ENABLE_COVERAGE}")
message(STATUS "  Sanitizers:         ${MYPROJECT_ENABLE_SANITIZERS}")
message(STATUS "  LTO:                ${MYPROJECT_ENABLE_LTO}")
message(STATUS "")
```

### Why this root pattern is based

- `cmake_minimum_required` is modern and policy-ranged
- `project()` carries real package metadata instead of bare minimum cope
- truly global settings are limited to language standard and compile commands
- feature toggles are explicit and prefixed
- reusable interface targets separate warnings and options from product targets
- subdirectories own their local targets rather than turning the root file into
  a thousand-line procedural swamp
- generated files are configured once and exposed through build-interface
  include directories later
- root logic is declarative enough that packagers, IDEs, and future humans can
  follow it without spiritual damage

## The `src/CMakeLists.txt` Pattern (Targets Own Their Own Business)

```cmake
add_library(myproject_core STATIC)
add_library(MyProject::core ALIAS myproject_core)

target_sources(myproject_core
    PRIVATE
        core/api.cpp
        core/algorithm.cpp
        core/format.cpp
    PUBLIC
        FILE_SET public_headers
        TYPE HEADERS
        BASE_DIRS ${CMAKE_CURRENT_SOURCE_DIR}/../include
        FILES
            ${CMAKE_CURRENT_SOURCE_DIR}/../include/my_project/api.hpp
            ${CMAKE_CURRENT_SOURCE_DIR}/../include/my_project/algorithm.hpp
            ${CMAKE_CURRENT_SOURCE_DIR}/../include/my_project/format.hpp
)

target_include_directories(myproject_core
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/../include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}/../generated>
        $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)

target_link_libraries(myproject_core
    PUBLIC
        MyProject::project_options
    PRIVATE
        MyProject::warnings
        fmt::fmt
)

set_target_properties(myproject_core PROPERTIES
    POSITION_INDEPENDENT_CODE ON
    VERIFY_INTERFACE_HEADER_SETS ON
)

if(CMAKE_VERSION VERSION_GREATER_EQUAL 4.3)
    set_target_properties(myproject_core PROPERTIES
        VERIFY_PRIVATE_HEADER_SETS ON
    )
endif()

if(MYPROJECT_ENABLE_LTO)
    include(CheckIPOSupported)
    check_ipo_supported(RESULT ipo_supported OUTPUT ipo_error)
    if(ipo_supported)
        set_property(TARGET myproject_core PROPERTY INTERPROCEDURAL_OPTIMIZATION TRUE)
    else()
        message(WARNING "IPO not supported: ${ipo_error}")
    endif()
endif()

add_executable(myproject_cli cli/main.cpp)
add_executable(MyProject::cli ALIAS myproject_cli)

target_link_libraries(myproject_cli
    PRIVATE
        MyProject::core
        cxxopts::cxxopts
)

if(MYPROJECT_ENABLE_TOOLS)
    install(TARGETS myproject_cli
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    )
endif()
```

### What this teaches

- the library is created first, then aliased into its exported namespace
- sources and public headers are attached directly to the target
- include directories are expressed through build/install interface separation
- public dependencies are only things consumers truly need
- warnings remain private because downstream consumers did not consent to your
  local diagnostic ideology
- header verification is enabled where the target actually owns headers
- executables link against targets, not against loose flag variables

## Things you are allowed to set globally

Be very suspicious of global state. CMake has it. That does not mean you should
worship it.

### Usually acceptable global settings

```cmake
set(CMAKE_C_STANDARD 23)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)

set(CMAKE_CXX_STANDARD 26)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
```

### Sometimes acceptable when clearly intentional

```cmake
set(CMAKE_FIND_PACKAGE_PREFER_CONFIG TRUE)
set(CMAKE_VERIFY_INTERFACE_HEADER_SETS ON)
set(CMAKE_VERIFY_PRIVATE_HEADER_SETS ON)
set(CMAKE_FIND_DEBUG_MODE TRUE)
```

These are acceptable when scoped or documented. Do not set them because you saw
one blog post and got excited.

### Usually banned global settings

```cmake
# ❌ BANNED: global include path pollution
include_directories(/some/path)

# ❌ BANNED: global link directories
link_directories(/some/lib/path)

# ❌ BANNED: global compile definitions blob
add_definitions(-DMY_DEFINE=1)

# ❌ BANNED: giant raw flag strings
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -O3 -funroll-loops")
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -Wl,--whatever")
```

If a flag belongs to a target, attach it to that target. If multiple targets
share it, create an interface target. This is the way.

## Presets Are Mandatory (Humans Should Not Memorise Configure Incantations)

If a project is serious enough to have more than one build configuration, it is
serious enough to have `CMakePresets.json`.

Presets are not optional sugar. They are the stable, reviewable interface
between:

- humans
- CI
- IDEs
- tooling
- local conventions
- dependency and toolchain selection

Without presets, teams end up with README incantations, shell history cargo
culting, and five slightly different local build directories that all mean
"debug probably". No.

### Preset doctrine

- define configure presets first
- make build and test presets thin wrappers around configure presets
- prefer hidden base presets for shared settings
- separate compiler selection, generator selection, toolchain selection, and
  feature selection into composable preset layers
- keep preset names short and semantic
- use environment blocks only when you must
- keep cache variables in presets, not in wiki pages and not in developer lore
- prefer schema version 11 when your minimum supported CMake allows it
- do not use negative `jobs` values in build/test presets because modern CMake
  rejected that nonsense for a reason

## The correct `CMakePresets.json` shape

```json
{
  "version": 11,
  "cmakeMinimumRequired": {
    "major": 4,
    "minor": 1,
    "patch": 0
  },
  "configurePresets": [
    {
      "name": "base",
      "hidden": true,
      "binaryDir": "${sourceDir}/build/${presetName}",
      "installDir": "${sourceDir}/install/${presetName}",
      "cacheVariables": {
        "CMAKE_EXPORT_COMPILE_COMMANDS": "ON",
        "MYPROJECT_BUILD_TESTS": "ON",
        "MYPROJECT_BUILD_DOCS": "ON",
        "MYPROJECT_ENABLE_WARNINGS_AS_ERRORS": "ON"
      }
    },
    {
      "name": "ninja",
      "hidden": true,
      "inherits": ["base"],
      "generator": "Ninja Multi-Config"
    },
    {
      "name": "gcc",
      "hidden": true,
      "inherits": ["base"],
      "cacheVariables": {
        "CMAKE_C_COMPILER": "gcc",
        "CMAKE_CXX_COMPILER": "g++"
      },
      "environment": {
        "CC": "gcc",
        "CXX": "g++"
      }
    },
    {
      "name": "clang",
      "hidden": true,
      "inherits": ["base"],
      "cacheVariables": {
        "CMAKE_C_COMPILER": "clang",
        "CMAKE_CXX_COMPILER": "clang++"
      },
      "environment": {
        "CC": "clang",
        "CXX": "clang++"
      }
    },
    {
      "name": "vcpkg",
      "hidden": true,
      "inherits": ["base"],
      "cacheVariables": {
        "CMAKE_TOOLCHAIN_FILE": {
          "type": "FILEPATH",
          "value": "$env{VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake"
        }
      }
    },
    {
      "name": "debug",
      "displayName": "Debug",
      "inherits": ["ninja", "gcc", "vcpkg"],
      "cacheVariables": {
        "CMAKE_BUILD_TYPE": "Debug",
        "MYPROJECT_ENABLE_SANITIZERS": "ON",
        "MYPROJECT_ENABLE_COVERAGE": "OFF"
      }
    },
    {
      "name": "release",
      "displayName": "Release",
      "inherits": ["ninja", "gcc", "vcpkg"],
      "cacheVariables": {
        "CMAKE_BUILD_TYPE": "Release",
        "MYPROJECT_ENABLE_SANITIZERS": "OFF",
        "MYPROJECT_ENABLE_LTO": "ON"
      }
    },
    {
      "name": "coverage",
      "displayName": "Coverage",
      "inherits": ["ninja", "gcc", "vcpkg"],
      "cacheVariables": {
        "CMAKE_BUILD_TYPE": "Debug",
        "MYPROJECT_ENABLE_SANITIZERS": "OFF",
        "MYPROJECT_ENABLE_COVERAGE": "ON"
      }
    },
    {
      "name": "ci-windows-msvc",
      "displayName": "CI Windows MSVC",
      "inherits": ["base", "vcpkg"],
      "generator": "Visual Studio 18 2026",
      "architecture": {
        "value": "x64",
        "strategy": "set"
      },
      "cacheVariables": {
        "MYPROJECT_ENABLE_SANITIZERS": "OFF",
        "MYPROJECT_ENABLE_COVERAGE": "OFF"
      },
      "condition": {
        "type": "equals",
        "lhs": "${hostSystemName}",
        "rhs": "Windows"
      }
    }
  ],
  "buildPresets": [
    {
      "name": "debug",
      "configurePreset": "debug",
      "configuration": "Debug"
    },
    {
      "name": "release",
      "configurePreset": "release",
      "configuration": "Release"
    },
    {
      "name": "coverage",
      "configurePreset": "coverage",
      "configuration": "Debug"
    }
  ],
  "testPresets": [
    {
      "name": "debug",
      "configurePreset": "debug",
      "configuration": "Debug",
      "output": {
        "outputOnFailure": true,
        "verbosity": "default"
      },
      "execution": {
        "noTestsAction": "error",
        "stopOnFailure": false
      }
    },
    {
      "name": "release",
      "configurePreset": "release",
      "configuration": "Release",
      "output": {
        "outputOnFailure": true
      }
    }
  ],
  "workflowPresets": [
    {
      "name": "full-debug",
      "steps": [
        { "type": "configure", "name": "debug" },
        { "type": "build", "name": "debug" },
        { "type": "test", "name": "debug" }
      ]
    },
    {
      "name": "full-release",
      "steps": [
        { "type": "configure", "name": "release" },
        { "type": "build", "name": "release" },
        { "type": "test", "name": "release" }
      ]
    }
  ]
}
```

### Why this preset file is based

- versioned schema, not implied tooling chaos
- explicit minimum required CMake version
- composable hidden presets for shared settings
- compiler, generator, and toolchain concerns are layered instead of duplicated
- build/test presets are deliberately thin
- workflow presets make the happy path obvious for humans and CI

## Preset anti-patterns

```json
{
  "version": 4,
  "configurePresets": [
    {
      "name": "final-real-debug",
      "generator": "Ninja",
      "binaryDir": "build",
      "cacheVariables": {
        "CMAKE_C_COMPILER": "C:/random/path/gcc.exe",
        "CMAKE_CXX_COMPILER": "C:/random/path/g++.exe",
        "CMAKE_BUILD_TYPE": "Debug",
        "BUILD_TESTS": "ON",
        "BUILD_DOCS": "ON",
        "ENABLE_COVERAGE": "OFF",
        "ENABLE_WARNINGS_AS_ERRORS": "ON"
      }
    }
  ]
}
```

Why this is cringe:

- ancient schema for no reason
- binary dir collides across variants
- hardcoded compiler paths with zero abstraction
- unprefixed cache variables
- no base preset reuse
- no build/test presets
- no workflow presets

## Single-config vs multi-config awareness

This distinction is where half of CMake bugs are born.

### Single-config generators

- `Ninja`
- `Unix Makefiles`
- `MinGW Makefiles`
- `FASTBuild`

These consume `CMAKE_BUILD_TYPE` at configure time.

### Multi-config generators

- `Ninja Multi-Config`
- Visual Studio generators
- Xcode

These do not treat `CMAKE_BUILD_TYPE` as the active configuration selector for
build/test/install execution. They want `--config <Config>` at build/test time.

### Correct multi-config-safe authoring

```cmake
target_compile_definitions(myproject_core
    PRIVATE
        $<$<CONFIG:Debug>:MYPROJECT_DEBUG_BUILD=1>
        $<$<CONFIG:Release>:MYPROJECT_RELEASE_BUILD=1>
)

target_compile_options(myproject_core
    PRIVATE
        $<$<AND:$<CONFIG:Debug>,$<CXX_COMPILER_ID:GNU,Clang>>:-O0 -g3>
        $<$<AND:$<CONFIG:Release>,$<CXX_COMPILER_ID:GNU,Clang>>:-O3>
)
```

### Incorrect single-config-only authoring

```cmake
# ❌ BAD: will disappoint you on multi-config generators
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    target_compile_definitions(myproject_core PRIVATE MYPROJECT_DEBUG_BUILD=1)
endif()
```

Use generator expressions for target-local behavior. `CMAKE_BUILD_TYPE` is not a
universal truth.

## Generator selection doctrine

- prefer **`Ninja Multi-Config`** when available and appropriate
- prefer **Visual Studio generators** only when you specifically want IDE-native
  project generation
- prefer **Xcode generator** only when you actually need Xcode project output
- use **FASTBuild** only when the project and team actually understand it
- do not hardcode a generator in project code; choose it in presets or user
  invocation

### Why `Ninja Multi-Config` is often the sweet spot

- fast
- IDE-friendly enough
- avoids separate configure trees for every config if you do not want them
- keeps multi-config semantics explicit

## Toolchain files (Use Them Deliberately, Not Emotionally)

Toolchain files are for:

- cross-compiling
- alternative compilers or standard libraries
- controlled compiler discovery
- platform SDK selection
- external package manager integration when unavoidable

They are not for arbitrary project options that belong in presets or ordinary
cache variables.

### A sane generic toolchain file

```cmake
# file: cmake/toolchains/clang-libcxx.cmake

set(CMAKE_SYSTEM_NAME Linux)

set(CMAKE_C_COMPILER clang)
set(CMAKE_CXX_COMPILER clang++)

set(CMAKE_CXX_FLAGS_INIT "-stdlib=libc++")
set(CMAKE_EXE_LINKER_FLAGS_INIT "-stdlib=libc++")
set(CMAKE_SHARED_LINKER_FLAGS_INIT "-stdlib=libc++")

set(CMAKE_FIND_PACKAGE_PREFER_CONFIG TRUE)
```

### Toolchain rules

- keep them small
- keep them about platform/compiler/toolchain identity
- avoid project feature toggles inside them
- select them from presets, not from local shell scripts hidden in a dotfile

## Cross-compiling doctrine

If the project cross-compiles, say so explicitly and model it with a real
toolchain file.

### Emscripten and modern cross-compiling

CMake 4.2 improved support for simple cross-compiling-to-Emscripten workflows.
That means you should write a clean toolchain story instead of scattering
browser-specific hacks through target logic.

### Cross-compiling rules

- `CMAKE_SYSTEM_NAME` belongs in the toolchain
- avoid executing target binaries at configure time unless you have a configured
  emulator or other explicit support
- do not mix host and target package artifacts
- be aware that Python/package-discovery cross-compile consistency got stricter
  in 4.1 and 4.2-era behavior

## Vcpkg Manifest Mode (The Dependency Truth Must Live in the Repository)

If the project depends on Vcpkg-managed libraries, the repository must contain a
`vcpkg.json`. Full stop.

### Manifest doctrine

- dependencies live in `vcpkg.json`
- versions/baselines live in configuration
- optional capabilities live in features
- host tools are expressed as host dependencies where relevant
- the build should work from a clean checkout with only toolchain and bootstrap
  prerequisites documented

### The correct `vcpkg.json` shape

```json
{
  "$schema": "https://raw.githubusercontent.com/microsoft/vcpkg-tool/main/docs/vcpkg.schema.json",
  "name": "my-project",
  "version-string": "1.2.0",
  "description": "Reusable library and CLI built with modern CMake and Vcpkg",
  "homepage": "https://example.com/my-project",
  "license": "MIT",
  "supports": "!(uwp | arm) & (windows | linux | osx)",
  "dependencies": [
    "fmt",
    "spdlog",
    "nlohmann-json",
    {
      "name": "gtest",
      "default-features": true
    },
    {
      "name": "zlib",
      "platform": "!windows"
    }
  ],
  "features": {
    "cli": {
      "description": "Build the command-line application",
      "dependencies": [
        "cxxopts"
      ]
    },
    "docs": {
      "description": "Documentation support",
      "dependencies": []
    },
    "gpu": {
      "description": "GPU backend and shader tooling",
      "dependencies": [
        "vulkan",
        "vulkan-memory-allocator",
        "spirv-tools"
      ]
    },
    "benchmarks": {
      "description": "Microbenchmark support",
      "dependencies": [
        "benchmark"
      ]
    }
  },
  "default-features": [
    "cli"
  ]
}
```

### Manifest rules

- prefer `version-string` unless you have a real semantic version story that
  benefits from the other version fields
- keep dependency declarations readable and explicit
- use features to model optional capability groups, not local developer moods
- use `supports` to declare platform truth instead of letting unsupported
  platforms fail mysteriously later
- do not dump dozens of transitive wish-list packages into the manifest just
  because the package manager can acquire them

## `vcpkg-configuration.json` (Pin the Universe or Accept Chaos)

If you use manifest mode seriously, pin the registry baseline. Otherwise the
world changes under you and you get to debug time-travel.

### The correct `vcpkg-configuration.json` shape

```json
{
  "$schema": "https://raw.githubusercontent.com/microsoft/vcpkg-tool/main/docs/vcpkg-configuration.schema.json",
  "default-registry": {
    "kind": "git",
    "repository": "https://github.com/microsoft/vcpkg",
    "baseline": "0123456789abcdef0123456789abcdef01234567"
  },
  "registries": [
    {
      "kind": "git",
      "repository": "https://example.com/custom-registry.git",
      "baseline": "89abcdef0123456789abcdef0123456789abcdef",
      "packages": [
        "my-custom-package"
      ]
    }
  ],
  "overlay-ports": [
    "${sourceDir}/vcpkg-overlay/ports"
  ],
  "overlay-triplets": [
    "${sourceDir}/vcpkg-overlay/triplets"
  ]
}
```

### Configuration rules

- always pin the default registry baseline
- use custom registries only when you actually own or rely on packages outside
  the default registry
- overlays are appropriate for local patches, custom ports, and custom triplets
- keep overlay locations in the repo, not in per-user machine setup

## Finding Vcpkg from CMake

Prefer selecting the toolchain in presets.

```json
{
  "name": "vcpkg",
  "hidden": true,
  "cacheVariables": {
    "CMAKE_TOOLCHAIN_FILE": {
      "type": "FILEPATH",
      "value": "$env{VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake"
    }
  }
}
```

This is better than telling developers to append `-DCMAKE_TOOLCHAIN_FILE=...`
from memory every time. Humans are unreliable build frontends.

## `find_package()` discipline with Vcpkg

Once the toolchain is active, use `find_package()` and imported targets.

```cmake
find_package(fmt CONFIG REQUIRED)
find_package(spdlog CONFIG REQUIRED)
find_package(nlohmann_json CONFIG REQUIRED)
find_package(GTest CONFIG REQUIRED)

target_link_libraries(myproject_core
    PRIVATE
        fmt::fmt
        spdlog::spdlog
        nlohmann_json::nlohmann_json
)

target_link_libraries(myproject_tests
    PRIVATE
        GTest::gtest
        GTest::gtest_main
)
```

### What is banned

```cmake
# ❌ BAD: variable-era linkage
find_package(GTest REQUIRED)
target_include_directories(myproject_tests PRIVATE ${GTEST_INCLUDE_DIRS})
target_link_libraries(myproject_tests PRIVATE ${GTEST_BOTH_LIBRARIES})

# ❌ BAD: manual include/lib paths into vcpkg installed trees
include_directories("${VCPKG_ROOT}/installed/x64-windows/include")
link_directories("${VCPKG_ROOT}/installed/x64-windows/lib")
```

If Vcpkg and CMake are integrated correctly, you should not be spelunking inside
the installed tree manually.

## Dependency layers and aggregate interface targets

For medium and large projects, make dependency bundles explicit.

```cmake
add_library(myproject_dependencies_core INTERFACE)
add_library(MyProject::dependencies_core ALIAS myproject_dependencies_core)

target_link_libraries(myproject_dependencies_core INTERFACE
    fmt::fmt
    spdlog::spdlog
    nlohmann_json::nlohmann_json
)

add_library(myproject_dependencies_testing INTERFACE)
add_library(MyProject::dependencies_testing ALIAS myproject_dependencies_testing)

target_link_libraries(myproject_dependencies_testing INTERFACE
    GTest::gtest
    GTest::gtest_main
)

add_library(myproject_dependencies_gpu INTERFACE)
add_library(MyProject::dependencies_gpu ALIAS myproject_dependencies_gpu)

target_link_libraries(myproject_dependencies_gpu INTERFACE
    Vulkan::Vulkan
)
```

This helps you express capability groupings without turning every real target
into a hand-maintained grocery list.

## Overlay ports (When Upstream Packaging Needs Surgery)

Overlay ports are the correct answer when:

- you need to patch a dependency's packaging logic
- you need a temporary compatibility fix
- you need a local package not yet in the main registry
- you need to adjust a build flag or export rule in a controlled way

They are not the correct answer for casually forking the world because you are
bored.

### Generic overlay port structure

```text
vcpkg-overlay/
├── ports/
│   └── my-patched-package/
│       ├── portfile.cmake
│       ├── vcpkg.json
│       ├── patches/
│       │   └── fix-cmake-4-compat.patch
│       └── usage
└── triplets/
```

### Generic `portfile.cmake`

```cmake
vcpkg_from_github(
    OUT_SOURCE_PATH SOURCE_PATH
    REPO upstream/project
    REF "v${VERSION}"
    SHA512 0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
    PATCHES
        fix-cmake-4-compat.patch
)

vcpkg_cmake_configure(
    SOURCE_PATH "${SOURCE_PATH}"
    OPTIONS
        -DPROJECT_BUILD_TESTS=OFF
        -DPROJECT_BUILD_EXAMPLES=OFF
        -DPROJECT_INSTALL=ON
)

vcpkg_cmake_install()
vcpkg_cmake_config_fixup(CONFIG_PATH lib/cmake/Project PACKAGE_NAME project)
vcpkg_fixup_pkgconfig()

vcpkg_install_copyright(FILE_LIST
    "${SOURCE_PATH}/LICENSE"
)

file(INSTALL
    "${CMAKE_CURRENT_LIST_DIR}/usage"
    DESTINATION "${CURRENT_PACKAGES_DIR}/share/${PORT}"
)
```

### Overlay port rules

- prefer real patches over `string(REPLACE)` surgery when the change is
  substantial or long-lived
- document why the overlay exists
- make the overlay easy to delete when upstream catches up
- keep `usage` instructions short and target-based
- keep host tool dependencies explicit in the overlay package metadata

### Generic `usage` file

```text
my-patched-package provides the following CMake targets:

    find_package(project CONFIG REQUIRED)
    target_link_libraries(my_target PRIVATE project::project)
```

Short. Honest. No drama.

## Custom triplets (ABI Is Not Vibes)

Custom triplets are appropriate when you need to control:

- target architecture
- CRT linkage
- library linkage
- platform identity
- toolchain chainloading
- compiler family/version alignment across dependencies and project targets

### Generic triplet example

```cmake
# file: vcpkg-overlay/triplets/x64-custom-dynamic.cmake

set(VCPKG_TARGET_ARCHITECTURE x64)
set(VCPKG_CRT_LINKAGE dynamic)
set(VCPKG_LIBRARY_LINKAGE dynamic)
set(VCPKG_CMAKE_SYSTEM_NAME Linux)

set(VCPKG_CHAINLOAD_TOOLCHAIN_FILE
    "${CMAKE_CURRENT_LIST_DIR}/../../cmake/toolchains/clang-libcxx.cmake"
)

set(VCPKG_ENV_PASSTHROUGH
    CC
    CXX
)
```

### Triplet rules

- use custom triplets when ABI or compiler identity matters
- name them descriptively
- keep them deterministic
- if you chainload a custom toolchain, do it because you need compiler/runtime
  alignment, not because you enjoy layers of indirection

## Why triplets matter more than people admit

Mixing these carelessly causes pain:

- GCC-built dependencies with Clang-built targets that assume another standard
  library
- MSVC ABI with MinGW-produced libraries
- static and dynamic CRT expectations colliding on Windows
- one build tree consuming another triplet's installed tree by accident

ABI mismatches are not philosophical disagreements. They are linker violence.

## Host dependencies vs target dependencies

If a dependency is used to run tooling during the build rather than linked into
the final artifact, model it as a host dependency where the package manager and
workflow expect that distinction.

Examples include:

- code generators
- protocol compilers
- documentation tools in packaging flows
- build-time helper executables

Do not pretend every dependency is a runtime dependency. That muddies the graph
and confuses cross-compiling.

## Dependency feature alignment between CMake and Vcpkg

If you expose project options that correspond to dependency feature groups,
coordinate them deliberately.

```cmake
option(MYPROJECT_ENABLE_GPU "Enable GPU backend" ON)
option(MYPROJECT_ENABLE_BENCHMARKS "Build benchmarks" OFF)

if(MYPROJECT_ENABLE_GPU)
    find_package(Vulkan CONFIG REQUIRED)
endif()

if(MYPROJECT_ENABLE_BENCHMARKS)
    find_package(benchmark CONFIG REQUIRED)
endif()
```

Then make the preset or user workflow activate matching manifest features. Do
not create a state where CMake expects a package feature the manifest never
asked for.

## Presets and Vcpkg features together

```json
{
  "name": "benchmark",
  "inherits": ["ninja", "gcc", "vcpkg"],
  "cacheVariables": {
    "CMAKE_BUILD_TYPE": "Release",
    "MYPROJECT_ENABLE_BENCHMARKS": "ON"
  },
  "vendor": {
    "my-project": {
      "manifest-features": ["benchmarks"]
    }
  }
}
```

If your tooling layer uses vendor fields or wrapper scripts to align manifest
features with presets, keep that mapping documented and obvious.

## Banned Vcpkg patterns

```text
❌ telling users to run `vcpkg install fmt spdlog gtest` manually for a repo
❌ no `vcpkg.json`
❌ no pinned baseline
❌ manual patching inside installed package directories
❌ hardcoding installed-tree include/lib paths in CMake
❌ assuming one default triplet works everywhere
❌ mixing classic mode and manifest mode without a deliberate migration plan
❌ hiding required overlay ports outside the repository
```

## A minimal but based producer-consumer dependency story

The repository should let a consumer do this:

```cmake
find_package(MyProject CONFIG REQUIRED)
target_link_libraries(their_app PRIVATE MyProject::core)
```

And your own build should let a contributor do this:

```text
cmake --preset debug
cmake --build --preset debug
ctest --preset debug
```

If the project cannot do both, the build architecture is not finished yet.

## Dependency modules (Keep Discovery Reusable and Honest)

In non-trivial projects, package discovery belongs in a dedicated module.

### Why a `Dependencies.cmake` module is based

- centralises required and optional package discovery
- keeps the root file readable
- makes discovery messaging consistent
- provides one place to encode package fallbacks, feature gates, and imported
  target adaptation

### A sane generic `Dependencies.cmake`

```cmake
include_guard(GLOBAL)

include(CMakeFindDependencyMacro)

function(myproject_find_package package_name)
  cmake_parse_arguments(PARSE_ARGV 1 ARG
    "REQUIRED;QUIET"
    "VERSION"
    ""
  )

  set(find_args ${package_name})
  if(ARG_VERSION)
    list(APPEND find_args ${ARG_VERSION})
  endif()
  list(APPEND find_args CONFIG)

  if(ARG_REQUIRED)
    list(APPEND find_args REQUIRED)
  endif()

  if(ARG_QUIET)
    list(APPEND find_args QUIET)
  endif()

  find_package(${find_args})

  if(${package_name}_FOUND)
    message(STATUS "Found ${package_name}")
  elseif(ARG_REQUIRED)
    message(FATAL_ERROR "Required package not found: ${package_name}")
  else()
    message(STATUS "Optional package not found: ${package_name}")
  endif()
endfunction()

myproject_find_package(fmt REQUIRED VERSION 11)
myproject_find_package(spdlog REQUIRED)
myproject_find_package(nlohmann_json REQUIRED)

if(MYPROJECT_BUILD_TESTS)
  myproject_find_package(GTest REQUIRED)
  include(GoogleTest)
endif()

if(MYPROJECT_ENABLE_BENCHMARKS)
  myproject_find_package(benchmark)
endif()

if(MYPROJECT_ENABLE_GPU)
  myproject_find_package(Vulkan REQUIRED VERSION 1.3)
endif()
```

### Rules for discovery modules

- prefer a tiny helper function over copy-pasted `find_package()` boilerplate
- always use `CONFIG` when the upstream package provides it
- only add fallbacks when they are real requirements, not "maybe this package is
  installed weirdly on someone's laptop"
- emit status lines that are actually informative
- do not create mystery package variables as your public API

## Warning configuration (Diagnostics belong to interface targets)

Warnings should be applied through interface targets, not through global flag
variables.

### Generic warning target

```cmake
add_library(myproject_warnings INTERFACE)
add_library(MyProject::warnings ALIAS myproject_warnings)

target_compile_options(myproject_warnings INTERFACE
  $<$<CXX_COMPILER_ID:GNU>:
    -Wall
    -Wextra
    -Wpedantic
    -Wconversion
    -Wsign-conversion
    -Wshadow
    -Wformat=2
    -Wundef
  >
  $<$<CXX_COMPILER_ID:Clang>:
    -Wall
    -Wextra
    -Wpedantic
    -Wconversion
    -Wsign-conversion
    -Wshadow
    -Wformat=2
    -Wundef
  >
  $<$<CXX_COMPILER_ID:MSVC>:
    /W4
    /permissive-
  >
)

if(MYPROJECT_ENABLE_WARNINGS_AS_ERRORS)
  target_compile_options(myproject_warnings INTERFACE
    $<$<CXX_COMPILER_ID:GNU,Clang>:-Werror>
    $<$<CXX_COMPILER_ID:MSVC>:/WX>
  )
endif()
```

### Warning rules

- warnings belong to first-party code targets
- do not force your warnings on consumers unless that is explicitly part of the
  package contract and you truly mean it
- prefer private linkage to the warning interface target for product targets
- carve out specific exceptions for known compiler-extension requirements rather
  than disabling broad categories lazily

## Sanitizers (Instrument the graph, do not improvise it)

Sanitizers are too important to be managed through ad hoc developer commands.
Model them in CMake.

### Generic sanitizer interface target

```cmake
add_library(myproject_sanitizers INTERFACE)
add_library(MyProject::sanitizers ALIAS myproject_sanitizers)

option(MYPROJECT_SANITIZER_ADDRESS "Enable ASan" ON)
option(MYPROJECT_SANITIZER_UNDEFINED "Enable UBSan" ON)
option(MYPROJECT_SANITIZER_THREAD "Enable TSan" OFF)
option(MYPROJECT_SANITIZER_MEMORY "Enable MSan (Clang only)" OFF)

if(MYPROJECT_SANITIZER_ADDRESS AND MYPROJECT_SANITIZER_THREAD)
  message(FATAL_ERROR "ASan and TSan are mutually exclusive")
endif()

if(MYPROJECT_SANITIZER_MEMORY AND NOT CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
  message(FATAL_ERROR "MSan requires Clang")
endif()

if(MYPROJECT_SANITIZER_ADDRESS)
  target_compile_options(myproject_sanitizers INTERFACE
    $<$<CXX_COMPILER_ID:GNU,Clang>:-fsanitize=address -fno-omit-frame-pointer>
    $<$<CXX_COMPILER_ID:MSVC>:/fsanitize=address>
  )
  target_link_options(myproject_sanitizers INTERFACE
    $<$<CXX_COMPILER_ID:GNU,Clang>:-fsanitize=address>
    $<$<CXX_COMPILER_ID:MSVC>:/fsanitize=address>
  )
endif()

if(MYPROJECT_SANITIZER_UNDEFINED)
  target_compile_options(myproject_sanitizers INTERFACE
    $<$<CXX_COMPILER_ID:GNU,Clang>:-fsanitize=undefined>
  )
  target_link_options(myproject_sanitizers INTERFACE
    $<$<CXX_COMPILER_ID:GNU,Clang>:-fsanitize=undefined>
  )
endif()

if(MYPROJECT_SANITIZER_THREAD)
  target_compile_options(myproject_sanitizers INTERFACE
    $<$<CXX_COMPILER_ID:GNU,Clang>:-fsanitize=thread>
  )
  target_link_options(myproject_sanitizers INTERFACE
    $<$<CXX_COMPILER_ID:GNU,Clang>:-fsanitize=thread>
  )
endif()
```

### Sanitizer rules

- keep sanitizer enablement preset-driven
- document incompatible combinations
- link sanitizer interface targets only to relevant first-party targets
- remember platform/toolchain caveats, especially on Windows and exotic link
  setups
- do not pretend one sanitizer profile fits every compiler and platform

## Coverage (Treat It Like Build Configuration, Not a Ritual)

Coverage is not just "turn on gcov somehow". It is a build mode with its own
trade-offs.

### Generic coverage interface target

```cmake
add_library(myproject_coverage INTERFACE)
add_library(MyProject::coverage ALIAS myproject_coverage)

if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
  target_compile_options(myproject_coverage INTERFACE
    --coverage
    -fprofile-arcs
    -ftest-coverage
    -fprofile-abs-path
    -fno-inline
  )
  target_link_options(myproject_coverage INTERFACE
    --coverage
  )
elseif(CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
  target_compile_options(myproject_coverage INTERFACE
    -fprofile-instr-generate
    -fcoverage-mapping
    -fno-inline
  )
  target_link_options(myproject_coverage INTERFACE
    -fprofile-instr-generate
  )
endif()
```

### Coverage rules

- coverage presets should usually disable sanitizers unless you have a very good
  reason otherwise
- use dedicated build directories for coverage builds
- filter out external and generated code from reports
- make report generation a build target or scriptable workflow, not a README
  séance

### Generic coverage report target for GCC and lcov

```cmake
find_program(LCOV_EXECUTABLE lcov)
find_program(GENHTML_EXECUTABLE genhtml)
find_program(GCOV_EXECUTABLE gcov)

if(LCOV_EXECUTABLE AND GENHTML_EXECUTABLE AND GCOV_EXECUTABLE)
  add_custom_target(coverage-report
    COMMAND ${LCOV_EXECUTABLE} --zerocounters --directory ${CMAKE_BINARY_DIR}
    COMMAND ${CMAKE_CTEST_COMMAND} --test-dir ${CMAKE_BINARY_DIR} --output-on-failure
    COMMAND ${LCOV_EXECUTABLE}
      --capture
      --directory ${CMAKE_BINARY_DIR}
      --output-file ${CMAKE_BINARY_DIR}/coverage.info
      --gcov-tool ${GCOV_EXECUTABLE}
    COMMAND ${LCOV_EXECUTABLE}
      --remove ${CMAKE_BINARY_DIR}/coverage.info
      '/usr/*'
      '*/vcpkg_installed/*'
      '*/build/*'
      --output-file ${CMAKE_BINARY_DIR}/coverage.cleaned.info
    COMMAND ${GENHTML_EXECUTABLE}
      ${CMAKE_BINARY_DIR}/coverage.cleaned.info
      --output-directory ${CMAKE_BINARY_DIR}/coverage-html
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
    COMMENT "Generating coverage report"
    VERBATIM
  )
endif()
```

## Testing (Testing Is Praxis and the Build Graph Should Admit That)

If the project has tests, the test infrastructure should be easy to extend and
hard to misuse.

### Test doctrine

- use `include(CTest)` in the root
- enable testing only when the project option says so
- keep test target creation behind a helper function once the suite grows
- prefer `gtest_discover_tests()` with deliberate discovery settings for Google
  Test projects
- use labels for logical grouping
- use resource locks when tests share global or external state
- keep benchmarks separate from correctness tests

### Generic test helper module

```cmake
include_guard(GLOBAL)

add_library(myproject_test_common INTERFACE)
add_library(MyProject::test_common ALIAS myproject_test_common)

target_link_libraries(myproject_test_common INTERFACE
  GTest::gtest
  GTest::gtest_main
  MyProject::core
)

if(TARGET MyProject::warnings)
  target_link_libraries(myproject_test_common INTERFACE MyProject::warnings)
endif()

if(TARGET MyProject::sanitizers)
  target_link_libraries(myproject_test_common INTERFACE MyProject::sanitizers)
endif()

if(TARGET MyProject::coverage)
  target_link_libraries(myproject_test_common INTERFACE MyProject::coverage)
endif()

function(myproject_add_test)
  cmake_parse_arguments(PARSE_ARGV 0 ARG
    ""
    "NAME;TIMEOUT"
    "SOURCES;LABELS;DEPENDS;RESOURCE_LOCK"
  )

  if(NOT ARG_NAME)
    message(FATAL_ERROR "myproject_add_test requires NAME")
  endif()

  if(NOT ARG_SOURCES)
    message(FATAL_ERROR "myproject_add_test requires SOURCES")
  endif()

  if(NOT ARG_TIMEOUT)
    set(ARG_TIMEOUT 60)
  endif()

  set(test_target "test_${ARG_NAME}")
  add_executable(${test_target} ${ARG_SOURCES})

  target_link_libraries(${test_target}
    PRIVATE
      MyProject::test_common
      ${ARG_DEPENDS}
  )

  if(ARG_RESOURCE_LOCK)
    gtest_discover_tests(${test_target}
      TEST_PREFIX "${ARG_NAME}::"
      DISCOVERY_MODE PRE_TEST
      DISCOVERY_TIMEOUT 20
      PROPERTIES
        TIMEOUT ${ARG_TIMEOUT}
        LABELS "${ARG_LABELS}"
        RESOURCE_LOCK "${ARG_RESOURCE_LOCK}"
    )
  else()
    gtest_discover_tests(${test_target}
      TEST_PREFIX "${ARG_NAME}::"
      DISCOVERY_MODE PRE_TEST
      DISCOVERY_TIMEOUT 20
      PROPERTIES
        TIMEOUT ${ARG_TIMEOUT}
        LABELS "${ARG_LABELS}"
    )
  endif()
endfunction()
```

### Why `DISCOVERY_MODE PRE_TEST` is often based

For some environments — especially where runtime dependencies are copied late,
or where discovery races with post-build deployment — `PRE_TEST` avoids flaky
discovery-time execution.

Use it when:

- test executables depend on copied shared libraries
- multi-target parallel builds create timing weirdness
- test discovery should happen in the more stable test phase rather than the
  build phase

### Generic test directory

```cmake
add_subdirectory(unit)
add_subdirectory(integration)

add_custom_target(test-unit
  COMMAND ${CMAKE_CTEST_COMMAND}
    --test-dir ${CMAKE_BINARY_DIR}
    -C $<CONFIG>
    --label-regex unit
    --output-on-failure
)

add_custom_target(test-integration
  COMMAND ${CMAKE_CTEST_COMMAND}
    --test-dir ${CMAKE_BINARY_DIR}
    -C $<CONFIG>
    --label-regex integration
    --output-on-failure
)
```

### Benchmark doctrine

- benchmark executables are not unit tests
- build them only when the benchmark dependency is available and enabled
- keep benchmark linkage separate from test linkage
- benchmark common utilities may live in an interface target

```cmake
find_package(benchmark CONFIG REQUIRED)

add_library(myproject_bench_common INTERFACE)
add_library(MyProject::bench_common ALIAS myproject_bench_common)

target_link_libraries(myproject_bench_common INTERFACE
  benchmark::benchmark
  benchmark::benchmark_main
  MyProject::core
)
```

## Documentation (Doxygen Should Be First-Class, Not a Weekend Afterthought)

If the codebase uses generated API docs, model them as build targets.

### Generic docs module

```cmake
include_guard(GLOBAL)

find_package(Doxygen 1.15 QUIET COMPONENTS dot)

if(NOT DOXYGEN_FOUND)
  message(STATUS "Doxygen not found; docs target disabled")
  return()
endif()

set(DOXYGEN_PROJECT_NAME "MyProject")
set(DOXYGEN_PROJECT_NUMBER "${PROJECT_VERSION}")
set(DOXYGEN_PROJECT_BRIEF "Reusable C++ library with target-based build logic")
set(DOXYGEN_EXTRACT_ALL YES)
set(DOXYGEN_EXTRACT_PRIVATE YES)
set(DOXYGEN_WARN_IF_UNDOCUMENTED YES)
set(DOXYGEN_WARN_IF_DOC_ERROR YES)
set(DOXYGEN_GENERATE_HTML YES)
set(DOXYGEN_GENERATE_LATEX NO)
set(DOXYGEN_HAVE_DOT ${DOXYGEN_DOT_FOUND})
set(DOXYGEN_CALL_GRAPH YES)
set(DOXYGEN_CALLER_GRAPH YES)
set(DOXYGEN_UML_LOOK YES)
set(DOXYGEN_MARKDOWN_SUPPORT YES)
set(DOXYGEN_USE_MDFILE_AS_MAINPAGE "${CMAKE_SOURCE_DIR}/README.md")

doxygen_add_docs(docs
  ${CMAKE_SOURCE_DIR}/include
  ${CMAKE_SOURCE_DIR}/src
  ${CMAKE_SOURCE_DIR}/README.md
  COMMENT "Generating documentation"
)
```

### Docs rules

- docs should fail loudly enough that broken config is visible
- prefer `dot` support when diagrams matter
- include markdown entry points deliberately
- document how to generate the docs in presets, tasks, or README, not only in
  one person's memory

## Installation and export (If It Builds But Cannot Be Consumed, It Is Half Done)

One of the biggest differences between toy CMake and real CMake is whether the
project installs and exports itself cleanly.

### Install doctrine

- use `GNUInstallDirs`
- install targets, not raw files, whenever possible
- install public headers through file sets if you have them
- install exports under `${CMAKE_INSTALL_LIBDIR}/cmake/<Project>`
- generate package config and package version files
- use `find_dependency()` in the config file template

### Generic install and export example

```cmake
install(TARGETS myproject_core
  EXPORT MyProjectTargets
  FILE_SET public_headers DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
  ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

install(TARGETS myproject_cli
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

install(EXPORT MyProjectTargets
  FILE MyProjectTargets.cmake
  NAMESPACE MyProject::
  DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/MyProject
)
```

### Generic package config generation

```cmake
include(CMakePackageConfigHelpers)

configure_package_config_file(
  "${CMAKE_CURRENT_SOURCE_DIR}/cmake/MyProjectConfig.cmake.in"
  "${CMAKE_CURRENT_BINARY_DIR}/MyProjectConfig.cmake"
  INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/MyProject
)

write_basic_package_version_file(
  "${CMAKE_CURRENT_BINARY_DIR}/MyProjectConfigVersion.cmake"
  VERSION ${PROJECT_VERSION}
  COMPATIBILITY SameMajorVersion
)

install(FILES
  "${CMAKE_CURRENT_BINARY_DIR}/MyProjectConfig.cmake"
  "${CMAKE_CURRENT_BINARY_DIR}/MyProjectConfigVersion.cmake"
  DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/MyProject
)
```

### Generic `MyProjectConfig.cmake.in`

```cmake
@PACKAGE_INIT@

include(CMakeFindDependencyMacro)

find_dependency(fmt CONFIG REQUIRED)
find_dependency(spdlog CONFIG REQUIRED)

if(@MYPROJECT_ENABLE_GPU@)
  find_dependency(Vulkan CONFIG REQUIRED)
endif()

include("${CMAKE_CURRENT_LIST_DIR}/MyProjectTargets.cmake")

check_required_components(MyProject)
```

### Consumer example

```cmake
cmake_minimum_required(VERSION 4.1...4.3)

project(Consumer LANGUAGES CXX)

find_package(MyProject CONFIG REQUIRED)

add_executable(consumer_app main.cpp)
target_link_libraries(consumer_app PRIVATE MyProject::core)
```

If this consumer story is not tested, your package export story is aspirational,
not real.

## Common Package Specification and package metadata

CMake 4.3 added a real CPS story. You do not need to use it everywhere yet, but
you absolutely need to know it exists.

### Generic CPS-aware export example

```cmake
install(PACKAGE_INFO MyProject
  DESTINATION ${CMAKE_INSTALL_LIBDIR}/cps
)

export(PACKAGE_INFO MyProject)
```

### CPS rules

- if the project is a reusable library, follow CPS developments closely
- keep project metadata clean enough that CPS export is not embarrassing
- even if you still ship classic config packages, do not ignore the direction
  of modern CMake interoperability

## Advanced CMake 4.x features you should know exist

This section is for the sharp tools. You do not need every one every day, but
you should not be unaware of them either.

## `cmake_language(TRACE)`

Useful when debugging macro/function flow without enabling giant global trace
flags for the whole run.

```cmake
cmake_language(TRACE ON)
# suspicious logic here
cmake_language(TRACE OFF)
```

## `cmake_instrumentation()` and instrumentation workflows

If configure/build/test/install performance or behavior matters, instrument it.

```cmake
cmake_instrumentation(ENABLED ON)
```

This is especially good when a project's configuration step became a small novel
and nobody knows why.

## File API over cache scraping

If tools need to understand the build graph, prefer the file API. Do not scrape
cache files or console text like a barbarian.

### Why the file API is based

- structured replies
- codemodel versioning
- better IDE/tool integration
- 4.0 through 4.3 kept enriching target and dependency data

If you are building tooling, respect the file API.

## `cmake --version=json-v1`

Machine-readable version queries exist now. Use them.

```text
cmake --version=json-v1
```

That is better than regexing human output and praying the spacing never changes.

## `cmake -E copy_if_newer` and `copy_directory_if_newer`

Use these when timestamp-based copying is what you actually want.

```cmake
add_custom_command(TARGET myproject_cli POST_BUILD
  COMMAND ${CMAKE_COMMAND} -E copy_if_newer
    "$<TARGET_FILE:myproject_cli>"
    "${CMAKE_BINARY_DIR}/staging/bin"
)
```

This can be more appropriate than content-comparison copying for certain build
pipelines.

## `cmake -E bin2c`

If you need to embed binary assets and the built-in tool is sufficient, prefer
the supported tool over bespoke conversion scripts.

## `string(JSON GET_RAW)` and `STRING_ENCODE`

4.3 extended `string(JSON)` for more faithful JSON handling. If you are doing
JSON in configure logic, use the actual command features instead of shelling out
to Python for every minor operation.

## `string(REGEX QUOTE)`

Already discussed, but worth repeating: this eliminates so much manual escaping
cope that it deserves permanent mental residency.

## `set(CACHE{...})` and `unset(CACHE{...})`

Use the explicit cache syntax when setting cache entries intentionally.

```cmake
set(CACHE{MYPROJECT_RUNTIME_BACKEND}
  TYPE STRING
  HELP "Selected runtime backend"
  VALUE "native"
)
```

This reads like intent instead of like legacy incantation residue.

## `TARGET_INTERMEDIATE_DIR`

When you genuinely need to talk about the target's intermediate directory, do
not reconstruct paths manually.

```cmake
add_custom_command(TARGET myproject_core POST_BUILD
  COMMAND ${CMAKE_COMMAND} -E echo "$<TARGET_INTERMEDIATE_DIR:myproject_core>"
)
```

## `SKIP_LINTING` and `CMAKE_SKIP_LINTING`

Modern CMake lets you tell command-line generators to skip linting for specific
targets or globally. Use this sparingly.

```cmake
set_target_properties(third_party_codegen_output PROPERTIES
  SKIP_LINTING ON
)
```

Appropriate for generated code. Inappropriate for code you simply do not feel
like fixing.

## `source_group()` with generator expressions

Visual-IDE organisation can now be smarter. Nice to know. Do not over-engineer
it.

## File-set querying and property scopes

4.3 added file-set scope support to `get_property()` and `set_property()`.
Use this when the project truly needs file-set introspection or custom metadata.

## Per-language link flags

4.3 finally gave a clearer story for per-language link flags. If C and C++ link
steps need different treatment, say so explicitly instead of smearing all link
flags together.

## `cmake_pkg_config()`

Bridge cleanly to `pkg-config` ecosystems when you must. Prefer imported-target
workflows, but know this tool exists.

## `LINKER:` and `ARCHIVER:` prefixes

Say it with intent, not with compiler-driver punctuation folklore.

```cmake
target_link_options(myproject_core PRIVATE "LINKER:-z,defs")
set_property(TARGET myproject_archive APPEND PROPERTY STATIC_LIBRARY_OPTIONS
  "ARCHIVER:--thin"
)
```

## Package-finding best practices outside Vcpkg

Even when Vcpkg is not providing a package, prefer this order of operations:

1. upstream `CONFIG` package
2. a sane built-in CMake module if upstream config does not exist
3. `cmake_pkg_config()` when pkg-config is the right bridge
4. a custom find module only when the other options genuinely fail

Do not start at step 4 because you enjoy work.

## Custom commands and generated files

Generated files should be modelled with explicit inputs, outputs, byproducts,
and target relationships.

### Generic generated-file example

```cmake
add_custom_command(
  OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/generated/version.txt
  COMMAND ${CMAKE_COMMAND} -E echo "${PROJECT_VERSION}"
    > ${CMAKE_CURRENT_BINARY_DIR}/generated/version.txt
  DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/CMakeLists.txt
  VERBATIM
)

add_custom_target(generate_version_file
  DEPENDS ${CMAKE_CURRENT_BINARY_DIR}/generated/version.txt
)
```

### Generated-file rules

- declare outputs
- declare dependencies
- keep generation deterministic
- do not hide generation inside configure-time `execute_process()` unless the
  result truly must exist before target generation

## `execute_process()` discipline

`execute_process()` is not banned. It is just dangerous when abused.

### Use it for

- small configure-time probes
- querying tool versions when truly necessary
- one-off metadata extraction that must influence configure logic

### Do not use it for

- most build-time work that belongs in custom commands or targets
- parsing giant tool outputs because you refused to use the file API
- replacing proper package discovery
- shelling out for features CMake already has

Always prefer explicit `COMMAND_ERROR_IS_FATAL` behavior or project-wide default
control via modern variables rather than silent failure vibes.

## Anti-patterns (The Crimes Against the Build Graph)

### ❌ BAD: source globbing as the primary source list

```cmake
file(GLOB_RECURSE ALL_SOURCES CONFIGURE_DEPENDS src/*.cpp)
add_library(myproject_core ${ALL_SOURCES})
```

### ✅ GOOD: explicit source lists or target-local `target_sources()`

```cmake
add_library(myproject_core)
target_sources(myproject_core
  PRIVATE
    src/api.cpp
    src/algorithm.cpp
    src/runtime.cpp
)
```

Globbing is acceptable only when you explicitly accept its trade-offs and the
directory shape makes that worthwhile. It is not the default for core product
targets.

### ❌ BAD: directory-level include/link pollution

```cmake
include_directories(${SOME_INCLUDE_DIR})
link_directories(${SOME_LIB_DIR})
```

### ✅ GOOD: target-level usage requirements

```cmake
target_include_directories(myproject_core PRIVATE ${SOME_INCLUDE_DIR})
target_link_libraries(myproject_core PRIVATE some_imported_target)
```

### ❌ BAD: public dependency sprawl

```cmake
target_link_libraries(myproject_core
  PUBLIC
    fmt::fmt
    spdlog::spdlog
    nlohmann_json::nlohmann_json
    cxxopts::cxxopts
    benchmark::benchmark
)
```

### ✅ GOOD: public means truly required by consumers

```cmake
target_link_libraries(myproject_core
  PUBLIC
    MyProject::project_options
  PRIVATE
    fmt::fmt
    spdlog::spdlog
    nlohmann_json::nlohmann_json
)
```

If consumers do not need it to compile or link against your exported target, it
should not be public.

### ❌ BAD: manual package-variable archaeology

```cmake
find_package(ZLIB REQUIRED)
target_include_directories(myproject_core PRIVATE ${ZLIB_INCLUDE_DIRS})
target_link_libraries(myproject_core PRIVATE ${ZLIB_LIBRARIES})
```

### ✅ GOOD: imported targets when available

```cmake
find_package(ZLIB REQUIRED)
target_link_libraries(myproject_core PRIVATE ZLIB::ZLIB)
```

### ❌ BAD: configure-time feature discovery via ad hoc shell commands

```cmake
execute_process(COMMAND bash -c "pkg-config --libs fmt" OUTPUT_VARIABLE FMT_LIBS)
```

### ✅ GOOD: actual package discovery

```cmake
find_package(fmt CONFIG REQUIRED)
```

### ❌ BAD: no install/export story

```cmake
add_library(myproject_core STATIC src/api.cpp)
# and then nothing else. consumers can fend for themselves apparently.
```

### ✅ GOOD: install and export are part of target definition completion

Add the install/export flow before declaring the target integration-ready.

### ❌ BAD: hardcoding build types into path logic

```cmake
set(output_dir "${CMAKE_BINARY_DIR}/Debug/bin")
```

### ✅ GOOD: generator-aware expressions or install/runtime properties

```cmake
set_target_properties(myproject_cli PROPERTIES
  RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin"
)
```

Or use config-specific properties explicitly if that is the real requirement.

### ❌ BAD: mixing Vcpkg classic and manifest assumptions

```text
README says to run manual installs
repo has half a manifest
CI uses toolchain + baseline
local dev uses whatever was installed last month
```

Choose a real dependency workflow.

## Troubleshooting (When the Build Graph Starts Acting Possessed)

## Problem: package found locally but not in CI

Likely causes:

- no pinned Vcpkg baseline
- relying on system packages locally without declaring them
- hidden environment variables or user package registry state
- missing toolchain selection in presets

What to do:

- pin the baseline
- use manifest mode
- make presets authoritative
- test from a clean environment

## Problem: imported target exists but link still fails

Likely causes:

- ABI mismatch from triplet/compiler mismatch
- wrong config selected for imported target
- static vs shared runtime mismatch
- consumer forgot required components or config mapping

What to do:

- verify triplet and toolchain alignment
- inspect imported target properties
- test the install/export package from a clean consumer project

## Problem: tests discover locally but fail in CI or parallel builds

Likely causes:

- discovery-time execution races
- missing deployed runtime dependencies
- multi-config `-C` not passed to `ctest`
- shared global resources without resource locks

What to do:

- consider `DISCOVERY_MODE PRE_TEST`
- use resource locks
- make test runtime dependencies explicit
- ensure CI uses test presets instead of bespoke commands

## Problem: coverage or sanitizer flags break linking

Likely causes:

- incompatible sanitizer combinations
- toolchain-specific limitations
- link flags applied globally instead of selectively
- mixing instrumented and non-instrumented objects in unsupported ways

What to do:

- isolate the instrumentation in interface targets
- use dedicated presets
- document unsupported combinations
- stop pretending one debug preset must do everything simultaneously

## Problem: install tree works, exported package does not

Likely causes:

- missing `find_dependency()` calls in config template
- forgotten public file sets or include directories
- private-only dependency accidentally required by consumers
- namespace mismatch between exported targets and consumer expectations

What to do:

- write and run a real consumer smoke test
- inspect the generated config files
- ensure only true public requirements propagate publicly

## Problem: CMake policies keep appearing after updates

Likely causes:

- your authoring range is stale
- project code relies on old behavior accidentally
- dependency or subproject policy assumptions are leaking into your build

What to do:

- update the policy range deliberately
- read the relevant policy docs and release notes
- fix the code instead of muting the warning forever

## Problem: path handling breaks on Windows or case-sensitive filesystems

Likely causes:

- inconsistent path spelling
- manual path concatenation assumptions
- source file names referenced with the wrong case

What to do:

- standardise canonical case
- use path-aware CMake facilities and generator expressions where appropriate
- stop assuming Windows case insensitivity will save you forever

## Golden rules for maintainers reviewing CMake and Vcpkg changes

- ask whether the change is target-based
- ask whether install/export behavior still works
- ask whether presets remain the authoritative workflow
- ask whether dependency intent moved closer to or farther from the manifest
- ask whether the change relies on undocumented environment state
- ask whether the public/private linkage boundary is still honest
- ask whether the project now uses a newer 4.x feature correctly or merely more
  opaquely

## Quality Checklist

- [ ] `cmake_minimum_required()` uses a modern floor and policy range
- [ ] `project()` contains real metadata when the project is reusable
- [ ] targets own their sources, include dirs, features, definitions, and link
    dependencies
- [ ] global flag strings were not used where target properties would do
- [ ] presets exist and are the primary workflow
- [ ] `vcpkg.json` exists for manifest-mode dependency management
- [ ] `vcpkg-configuration.json` pins a baseline
- [ ] packages are consumed through imported targets
- [ ] install and export rules exist for reusable targets
- [ ] package config and version files are generated correctly
- [ ] a consumer smoke test is possible and ideally automated
- [ ] tests are grouped logically and use labels where useful
- [ ] sanitizers and coverage are modelled through interface targets or clearly
    isolated configuration logic
- [ ] docs are buildable through first-class targets if documentation is part of
    the project story
- [ ] overlay ports and triplets, if present, are repo-local and documented
- [ ] hardcoded paths are absent or justified by a genuine external constraint
- [ ] multi-config generators are not accidentally treated like single-config
    ones
- [ ] release-note-aware 4.x features are used where they improve clarity,
    interoperability, or observability

## Final doctrine

The correct mental model is this:

- CMake describes a graph
- targets are graph nodes
- usage requirements are graph edges
- presets describe workflows into that graph
- Vcpkg supplies dependency nodes in a reproducible way
- install/export logic makes the graph consumable by others
- policies and release-note changes define the semantics of the language you are
  writing in

If you remember only one thing, remember this:

> **Do not write CMake as if it were shell. Do not use Vcpkg as if it were a
> global machine state. Model the graph honestly, pin the world deliberately,
> and let targets propagate truth transitively.**

That is how the build goes brrr without becoming cursed uwu ✨
