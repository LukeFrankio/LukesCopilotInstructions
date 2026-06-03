---
name: 'Electrobun Elysia Drogon Stack'
description: 'Use when designing, implementing, reviewing, critiquing, or refactoring projects built on this specific stack: Electrobun, Bun, SolidJS, Elm, HTMX, Tailwind CSS, Elysia, Drizzle ORM, PostgreSQL, Turso Sync, Drogon, modern C++, CMake, Emscripten or Embind, FlatBuffers, Slang, WGSL, and WebGPU. Covers multiple valid architectures within this exact stack, recommends a default constitutional model, defines lane ownership and forbidden crossovers, and explains when each alternative architecture is or is not the right move.'
---

# Stack Architecture Instructions (The Constitutional Polyglot Mega-Stack)

> "A big stack is not automatically a bad stack. It only becomes cursed when the
> parts stop having jobs and start having opinions."

uwu this file is **not** about every stack.
it is **not** generic architecture advice.
it is **not** a neutral little pamphlet that says "it depends" and then runs
into the fog.

this file is about **one specific family of technologies** and the many ways they
can be arranged **without** becoming framework trench warfare:

- **Electrobun**
- **Bun**
- **SolidJS**
- **Elm**
- **HTMX**
- **Tailwind CSS**
- **Elysia**
- **Drizzle ORM**
- **PostgreSQL**
- **Turso Sync**
- **Drogon**
- **modern C++**
- **CMake**
- **Emscripten / Embind**
- **C++ WebAssembly**
- **FlatBuffers**
- **Slang**
- **WGSL**
- **WebGPU**

this is a **project-agnostic** instruction file in the correct sense:

- it should help with **any project using this stack**
- it should help across **multiple valid architectures inside this stack**
- it should **recommend a default** instead of pretending all shapes are equal
- it should explain **why that default is or is not appropriate**
- it should name **alternative architectures using the same stack**
- it should **not** waste time comparing random other stacks unless contrast is
  needed to make a point

this file exists because this stack is **too interesting to govern casually**.
when it is bounded, it goes hard.
when it is not bounded, it becomes a boss fight where every runtime thinks it is
the chosen one.

## Core philosophy (non-negotiable axioms)

- **roles > ingredients**
  - the key question is never "can these technologies coexist?"
  - the real question is "what does each one own, and what is forbidden?"
- **one stack, many architectures**
  - this stack supports multiple legitimate shapes
  - it is not required to express the same hierarchy in every product
- **defaults beat democracy**
  - every project needs a normal path for new work
  - if everything is equally primary, nothing is primary
- **specialization must stay specialized**
  - Elm, HTMX, Drogon, Turso Sync, FlatBuffers, Emscripten, and WebGPU all have
    real value
  - they are strongest when they stay in their lane instead of cosplaying as
    the whole product
- **human-readable edges, optimized hot paths**
  - HTML and JSON belong at product edges by default
  - FlatBuffers and other binary contracts belong on the internal hot path only
- **one owner per concern**
  - shell, interaction engine, hypermedia lane, public contract, compute,
    canonical truth, local sync, binary schema, and GPU lane all need owners
- **one source of truth per domain entity**
  - PostgreSQL and Turso may collaborate
  - they do not get to both wear the crown unless explicitly and narrowly
    declared
- **shared cores are based**
  - duplicated sibling implementations are cope
  - if the same algorithm matters in native and web contexts, write it once and
    compile it twice
- **weirdness must earn rent**
  - C++/WASM, FlatBuffers, Slang, WebGPU, and multi-runtime orchestration are
    powerful
  - they are justified by real product needs, not by aesthetic maximalism
- **latest versions always**
  - use the latest stable or beta line that the ecosystem actually supports
  - this stack moves fast; architectural guidance must acknowledge that reality
- **documentation and changelogs matter**
  - Elysia, Electrobun, Drizzle, Turso, and Slang are all active enough that
    stale assumptions rot quickly
- **no component has tenure**
  - every layer must keep re-earning its seat over time
- **platform bet risk is architecture risk**
  - young or fast-moving foundations (especially shell runtimes) need explicit
    contingency seams
  - "we can swap later" is only true if seams exist now

## What this stack actually is

this stack is not one thing.
it is a federation of five major lanes:

1. **desktop and shell lane**
   - Electrobun
   - Bun
   - SolidJS
   - Tailwind CSS
2. **interaction and hypermedia lane**
   - Elm
   - HTMX
   - Elysia HTML or fragment rendering
3. **public contract and service composition lane**
   - Elysia
   - Drizzle ORM
   - Bun runtime and tooling
4. **native compute and portable core lane**
   - Drogon
   - modern C++
   - CMake
   - Emscripten / Embind
   - FlatBuffers
5. **GPU and accelerated rendering or compute lane**
   - Slang
   - WGSL
   - WebGPU

and all of those lanes sit on top of a data topology:

- **PostgreSQL** for canonical truth
- **Turso Sync** for local-first, offline, replicated, or edge-adjacent state

if you forget that this is a **lane stack** rather than a **single-framework
stack**, you will make bad decisions with frightening confidence.

## What the official docs imply about the stack

this section is here so the architecture advice stays grounded in what the tools
say they are, not what we wish they were.

### Electrobun says

the official docs position Electrobun as:

- a **tiny desktop app framework**
- Bun app + native launcher + native wrapper
- native bindings in **C++ / ObjC / Zig**
- **system webview by default**, **CEF optional**
- **built-in updater** with small bsdiff-style patch flow
- **cross-platform desktop** target with native-feeling shell behaviors
- a bundle story built around **launcher + bun runtime + native wrapper + views**
- a desktop architecture where Bun user code typically runs in a **worker** while
  the native GUI event loop lives on the main thread

translation: Electrobun is a **shell and packaging sovereign**.
it is not the best place to smuggle half your domain model just because it can
call native code.

### Elysia says

the official docs position Elysia as:

- ergonomic and Bun-optimized
- schema-first and type-integrity focused
- capable of end-to-end type flow via Eden or Treaty
- OpenAPI-friendly, including type-derived generation
- fast enough to matter, but explicitly **DX-oriented**, not raw speed theater
- Bun-first yet not totally vendor-locked because of broader runtime targets

translation: Elysia is a very strong **public contract layer**, **BFF**, and
**composition service** for the TypeScript side of the stack.

### Solid says

the official docs position Solid as:

- fine-grained reactive
- fast and low-overhead in update behavior
- pragmatic rather than dogmatic
- a very strong fit for responsive UI shell work

translation: Solid is an excellent **shell framework** and a good place for
cross-cutting UI orchestration.
it is not automatically the best owner for the deepest feature state machine if
Elm is already in the room for that job.

### Elm says

the official docs position Elm around:

- **Model / View / Update** as the core architecture
- strong guarantees and purity culture
- intentionally constrained interop through **flags**, **ports**, and **custom
  elements**
- explicit rejection of a casual JS FFI because it would erode guarantees

translation: Elm is a serious **interaction engine** technology, not a cute
little utility layer.
if you bring it in, give it real bounded territory.

### HTMX says

the official docs and essays position HTMX as:

- HTML-first
- hypermedia-driven
- server responses are typically **HTML**, not JSON
- strong at partial page updates, forms, CRUD, and progressive enhancement
- friendly to events, islands, web components, and light scripting
- explicit about history, validation, headers, security, and response handling

translation: HTMX is a real **hypermedia lane**.
it is at its best when route-scoped or surface-scoped, not when used as a random
escape hatch for uncertainty.

### Bun says

the official docs position Bun as:

- a fast all-in-one toolkit
- runtime, package manager, test runner, bundler, script runner
- Bun is a single binary and Bun wants to be infrastructure, not just runtime
- Bun is web-standard friendly but **Node compatibility is still an ongoing
  effort**

translation: Bun is the **TypeScript lane runtime and toolchain default** in this
stack.
it is not the native build system, the C++ package manager, or the reason to
pretend Node compatibility gaps do not exist.

### Drizzle says

the official site and release stream say a lot very loudly:

- Drizzle ships fast
- Drizzle's 1.0 line is still actively maturing
- Drizzle has been adding dialects, migration engine changes, and validation
  packaging changes aggressively
- Drizzle now explicitly covers Bun SQL and Turso-related flows
- Drizzle is excellent as a TypeScript-first SQL toolchain
- Drizzle is fast-moving enough that schema and migration policy must be
  governed, not assumed stable forever

translation: Drizzle is strong in the **TypeScript persistence lane**.
it is not the metaphysical source of truth for the entire polyglot system.

### Turso says

the official docs position Turso Sync around:

- local path + remote URL + auth token
- explicit **push()** and **pull()**
- explicit **checkpoint()** and **stats()**
- offline-first writes by writing locally first
- initial bootstrap behavior that can be disabled with `bootstrapIfEmpty: false`
- conflict behavior that is explicitly **last push wins**

translation: Turso is great for **local-first**, **offline**, **replicated**, or
**edge-adjacent** state.
it is **not** canonical truth by default, and its conflict model must be
acknowledged in plain English.

### Drogon says

the official site positions Drogon as:

- fast
- asynchronous
- coroutine-friendly
- WebSocket capable
- DB and Redis capable
- broadly portable across platforms and CPUs

translation: Drogon is a credible **compute engine**, **high-throughput service**,
or **native-first internal service** in this stack.
it is not public sovereign by default unless the project intentionally chooses a
compute-first architecture.

### Emscripten says

the official docs position Emscripten as:

- a real compiler toolchain to WebAssembly
- `emcc` as a drop-in compiler frontend
- portable C and C++ code are generally good candidates
- many codebases need changes to **main loop** and **file handling** when moved
  to Wasm or browser contexts

translation: Emscripten is the right answer for **compile the shared C++ core to
Wasm**, but you must respect its runtime differences instead of pretending the
web is just Linux with worse vibes.

### FlatBuffers says

the official docs position FlatBuffers as:

- direct access to serialized data without full parse/unpack
- memory efficient
- small footprint
- schema-evolvable with forwards and backwards compatibility

translation: FlatBuffers is perfect for **internal binary hot paths** and
**shared native / Wasm schema boundaries**.
it should stay out of product-facing HTML and JSON lanes unless a very unusual
constraint proves otherwise.

### Slang says

the official site positions Slang as:

- modular shader authoring
- portable backend targeting, including **WebGPU**
- HLSL and GLSL migration path
- capability system to keep target differences explicit
- increasingly open-governed under **Khronos**
- not just a toy shader language, but a serious large-codebase shader system

translation: Slang is the right candidate for a **single shader truth** in a
stack that targets modern web and native GPU paths.

## The stack roster at a glance

| Lane | Technology | Default role | Allowed secondary role | Must not become |
| --- | --- | --- | --- | --- |
| Desktop shell | Electrobun | native shell, windowing, updater, packaging, native integration | desktop-specific host for web or Wasm features | the main domain engine |
| TS runtime and tooling | Bun | runtime, bundler, tests, package manager, scripts | orchestration for TS-side build pipelines | the native build system |
| Shell UI | SolidJS | app chrome, layout, reactive shell, embedding | light feature UI for non-Elm surfaces | the owner of every deep state machine |
| Deep interaction | Elm | deterministic bounded interaction engine | isolated feature island | a ceremonial purity wrapper with random JS escape hatches |
| Hypermedia lane | HTMX | forms, CRUD, reports, admin, doc-centric flows | narrow progressive-enhancement surface inside shell-owned routes | the junk drawer for fuzzy ownership |
| Styling | Tailwind CSS | cross-lane design system and utility styling | prototyping and fast UI composition | the place where state architecture gets encoded in class soup |
| Public contract | Elysia | BFF, validation, composition, OpenAPI, HTML or JSON shaping | thin auth/session or edge service in compute-heavy systems | the heavy compute engine |
| TS persistence | Drizzle ORM | schema, migrations, typed SQL in the TS lane | sync-adjacent local persistence in Bun-side utilities | the universal schema religion for the whole polyglot stack |
| Canonical truth | PostgreSQL | durable system of record | analytics-adjacent query backbone and relational coordination | a local cache or device state store |
| Local-first sync | Turso Sync | local replica, offline writes, synced subset, device-local state | edge cache with explicit sync lifecycle | a shadow king database |
| Native compute service | Drogon | optional out-of-process compute service once FFI/process boundaries are justified | public service only in compute-first architectures | an accidental second public backend |
| Shared core | modern C++ | algorithms, simulation, performance core, native truth of hot logic | portable core compiled to Wasm | shell UX and product routing |
| Native build graph | CMake | canonical build system for C++, Wasm, shaders, native libs | top-level orchestrator for generated artifacts | a replacement for Bun in the TS lane |
| Wasm toolchain | Emscripten / Embind | compile C++ core to Wasm and expose coarse bindings | browser-portable execution surface | a chatty FFI trampoline for every tiny interaction |
| Binary hot path | FlatBuffers | internal schema and binary payloads | persisted binary artifacts in performance-sensitive flows | the public API format |
| Shader authoring | Slang | single shader source, modules, cross-target compilation | HLSL/GLSL migration path | business logic host |
| GPU execution | WGSL / WebGPU | portable GPU rendering or compute | specialized visual or numeric acceleration path | the default home of domain rules |

## Canonical vocabulary (use these names or lose the plot)

this stack desperately needs **clean nouns**.
if everything is called "core" or "engine" the design review is already over.

### Preferred names

- **shell**
  - Electrobun + Solid + Tailwind side of the product experience
- **interaction engine**
  - Elm-owned bounded feature state machine
- **hypermedia lane**
  - HTMX + server-authored HTML territory
- **public contract layer**
  - Elysia-facing product contract and composition layer
- **compute engine**
  - C++ core plus the selected compute boundary (FFI, process, or service)
- **shared core**
  - portable C++ algorithmic center built for native and Wasm targets
- **canonical store**
  - PostgreSQL
- **local sync store**
  - Turso local DB plus explicit push or pull lifecycle
- **binary contract lane**
  - FlatBuffers on hot internal boundaries
- **GPU lane**
  - Slang -> WGSL -> WebGPU path

### Banned naming habits

- do not call Electrobun "the backend"
- do not call Elysia "the app" if Drogon exists
- do not call Elm "core" if C++ is also core
- do not call Turso "the database" with no qualifier
- do not call HTMX "frontend" if Solid and Elm also exist
- do not call FlatBuffers "the API" unless you enjoy confusion as a hobby

## Version stance (bleeding edge with eyes open)

this stack is alive and moving.
treat stale assumptions like expired milk.

### Current orientation as of 2026-06

- **Electrobun**
  - prefer the latest stable **1.18.x** line or newer beta if the needed feature
    is only there
  - the release stream is active enough that packaging and updater behavior must
    be re-checked when bumping
  - treat ecosystem maturity as an explicit architectural risk input; keep a host
    adapter seam so migration to another shell runtime is possible if project
    velocity or compatibility regresses
- **Bun**
  - prefer latest **1.2+** line or newer
  - Bun is central enough to the stack that runtime and driver compatibility are
    first-class architectural concerns
- **Elysia**
  - prefer latest release compatible with current Bun line
  - docs updated recently enough that runtime and plugin stories keep evolving
- **htmx**
  - default to **2.x**, not 1.x, unless legacy browser support is an explicit
    requirement
- **Drizzle**
  - prefer latest stable or current 1.0 beta line if features or fixes require
    it
  - beware of migration-engine churn, validator package changes, and dialect
    behavior shifts
- **Slang**
  - prefer latest Khronos-governed release line and check target backend support
    before assuming a feature compiles cleanly to WGSL
- **Emscripten**
  - prefer latest SDK line with the browser targets you actually ship against
- **PostgreSQL**
  - prefer modern supported major releases and do not architect around antique
    dialect assumptions
- **Turso**
  - prefer latest sync tooling and libsql-compatible client versions in the TS
    lane

### Version law

if a project in this stack pins old versions for comfort, that pin must be
explained in writing.

### Drift law

when updating any of these:

- Bun
- Elysia
- Drizzle
- Electrobun
- Slang
- Emscripten
- Turso

re-check:

- deployment assumptions
- compatibility notes
- build flags
- contract generators
- migration behavior
- sync behavior
- output or packaging paths

this stack rewards staying current.
it also punishes cargo-cult copy-paste from six months ago.

## When this instruction applies

apply this file when the user is:

- designing a system on this exact stack
- asking whether the stack is coherent
- asking who should own a feature in this stack
- deciding whether a feature belongs in Solid, Elm, or HTMX
- deciding whether Elysia or Drogon should own a service boundary
- deciding whether PostgreSQL or Turso should own data
- deciding when to bring in FlatBuffers
- deciding whether the C++ core should be compiled to Wasm
- deciding whether Slang or raw WGSL should be the source of shader truth
- deciding how Electrobun should host or package the application
- refactoring a mushy version of this stack into a bounded one

## When this instruction does not apply strongly

this file is less important when:

- the project only uses one small fragment of the stack
- the question is purely about a single library API and not architectural shape
- the user is exploring a completely different stack
- the project is intentionally not desktop, not Wasm, not native, and not
  multi-lane enough for these boundaries to matter

## The hidden smell this stack attracts

this stack's signature temptation is:

> "surely every interesting component should remain involved forever"

that instinct is dangerous.

### Good interpretation

- each component has a real earned role
- each role is bounded
- each boundary exists because it solves a real problem
- not every component dominates every project

### Cursed interpretation

- we must find something for every tool to do
- removing or demoting a tool feels like betrayal
- a lane exists because it is interesting, not because it is necessary
- architecture becomes a celebration of inventory

this file supports **using the whole stack**.
it does **not** support worshipping the whole stack.

## The recommended default architecture (the Constitutional Federation)

this is the default architecture this file recommends unless the project gives a
strong reason otherwise.

### Summary

- **Electrobun + Bun + Solid + Tailwind** own the desktop shell
- **Elm** owns one or more bounded, correctness-sensitive interaction islands
- **HTMX** owns named hypermedia surfaces such as admin, operations, reports,
  settings, or document-heavy routes
- **Elysia** owns the public contract layer, BFF logic, auth boundary,
  validation, HTML fragment rendering for HTMX, and JSON or streaming APIs for
  interactive clients
- **modern C++** owns heavy compute logic, with **Bun FFI/in-process boundaries
  first** and **Drogon service extraction when justified**
- **modern C++ + CMake** own the shared performance core
- **Emscripten / Embind** compile the core into Wasm where browser or portable
  execution matters
- **PostgreSQL** owns canonical truth
- **Turso Sync** owns local-first or offline state near the client and syncs
  explicitly
- **FlatBuffers** stay on internal hot boundaries only
- **Slang -> WGSL -> WebGPU** own the GPU lane

### Why this default slaps

because it gives every major worldview a role without letting any of them
silently become sovereign over the others.

### Why this default might be wrong

it is wrong when:

- the project is far more hypermedia-centric than shell-centric
- Elm deserves to own most of the product surface, not just bounded islands
- the application is compute-first and Elysia would only proxy everything
- the product is truly local-first and cloud truth is secondary for long periods
- the product is GPU-first and most architecture should bend around the visual or
  compute pipeline

### The default ownership map

| Concern | Owner | Notes |
| --- | --- | --- |
| app shell | Electrobun + Solid | shell chrome, windowing, routing shell, menus, notifications |
| shared styling | Tailwind CSS | one visual dialect across Solid, Elm-rendered DOM, and HTMX surfaces |
| deepest feature state | Elm | only where the feature genuinely deserves TEA-level discipline |
| document or CRUD flows | HTMX + Elysia HTML | server-authored fragments, validation, forms, admin, reports |
| public API contract | Elysia | JSON, HTML fragments, streaming, auth-aware response shaping |
| TS database access | Drizzle ORM | Elysia lane, migrations, schema, typed SQL |
| canonical durable truth | PostgreSQL | relational invariants, authoritative writes |
| local and offline state | Turso Sync | explicit push/pull, device-local durability |
| heavy native compute | C++ core + selected transport (Bun FFI first, Drogon when warranted) | async execution, streaming, or isolated scaling when earned |
| shared algorithmic center | modern C++ | one implementation, many targets |
| browser-portable compute | Emscripten / Wasm | same core, different host |
| internal binary contracts | FlatBuffers | only for hot or high-volume paths |
| shader truth | Slang | modular source, cross-target pipeline |
| browser or desktop GPU execution | WebGPU | fed by Slang-generated WGSL on web target |

### The default constitutional laws

1. **Electrobun owns the shell, not the domain.**
2. **Solid owns app chrome and cross-cutting UI, not every deep feature brain.**
3. **Elm owns only bounded features that truly deserve deterministic state
   architecture.**
4. **HTMX gets named territory, not vibes-based escape-hatch privileges.**
5. **Elysia owns the public contract and product-facing composition.**
6. **Drogon is optional and internal by default; it computes rather than
  negotiating product semantics.**
7. **Start with the lightest valid compute boundary.**

- Bun FFI or in-process core calls first
- promote to Drogon only when isolation, scaling, multi-caller, or lifecycle
    pressure justifies a service

8. **PostgreSQL is the durable system of record unless a narrower exception is
   explicitly declared.**
9. **Turso is local-first and sync-explicit; it is not shadow sovereignty.**
10. **C++ is written once for shared hot logic and compiled to native and Wasm
   targets when needed.**
11. **FlatBuffers stay inside the hot path.**
12. **Slang is the shader source of truth; WGSL is a target artifact, not the
    authoring canon.**
13. **CMake owns native and Wasm build truth; Bun owns TS build truth.**

### What this architecture feels like in practice

- the user perceives a cohesive native app shell
- core interaction surfaces feel disciplined and predictable
- admin and ops surfaces ship fast with server-authored HTML
- the public contract stays legible
- the heavy work lives where native code belongs
- the local machine can stay useful offline
- the GPU lane can grow without swallowing the whole repo

that is what a bounded mega-stack looks like when it is being based instead of
performative.

## Alternative architecture 1: Hypermedia-First Operations Architecture

this is still the same stack.
this is **not** a different stack.
it is the same components arranged around a different center of gravity.

### Summary

- HTMX becomes much more prominent
- Solid remains the shell but thinner
- Elm becomes optional or very narrowly scoped
- Elysia becomes both public contract and HTML fragment engine for most surfaces
- Drogon remains the compute sidecar for heavy work
- Electrobun remains the desktop shell if a desktop form factor still matters

### Use this when

- most product value is in forms, workflows, queues, review interfaces, reports,
  settings, approvals, or document-like surfaces
- the product benefits more from server-authored HTML than from thick client
  reactive state
- many routes want progressive enhancement or simpler debugging
- the shell still matters, but the app is not interaction-engine-dominated

### Avoid this when

- the product has a few very deep state-machine-like interactions that really
  deserve Elm
- the app is heavily visual, animation-heavy, graphics-heavy, or local-state
  dominated
- the team will use HTMX as a cover story for route ownership confusion

### What changes from the default

| Concern | Default federation | Hypermedia-first variant |
| --- | --- | --- |
| shell | Solid-heavy shell | Solid still owns shell, but most route bodies are server-driven |
| primary feature lane | Solid + Elm mix | HTMX + Elysia HTML dominates most feature surfaces |
| Elm | important bounded engine | optional or limited to one advanced surface |
| Elysia | API + fragments | heavily HTML-oriented BFF and route composition engine |
| routing | more client-orchestrated shell | more server-authorized surface control |

### Mandatory laws

1. **HTMX routes must be named territory.**
   - `/ops/*`
   - `/admin/*`
   - `/reports/*`
   - `/settings/*`
   - or another clear partition
2. **Pushed URLs must be navigable as full pages.**
   - HTMX docs are explicit about this
   - do not push routes that only exist as partial fragments
3. **Use `Vary: HX-Request` when response shape differs for fragments vs full
   pages.**
4. **Set `historyRestoreAsHxRequest` thoughtfully.**
   - when using `HX-Request` to vary partials vs full pages, do not allow history
     restoration behavior to poison that assumption
5. **Server validation is truth.**
   - client validation is a convenience only
6. **HTMX is not your secret state manager.**
   - if a route needs rich local state, that is a signal for Solid or Elm island
     territory, not a reason to stretch fragments until they scream

### Why this can be better than the default

because many productivity and operations apps do **not** need the cost of a rich
client architecture everywhere.
HTML and HTTP are already powerful.
let them cook.

### Why this can be worse than the default

because if the product later grows a few ultra-rich interactions, teams often
start mixing HTMX, ad hoc JavaScript, Solid local state, and Elm-like logic with
no constitution.
that is how you invent a haunted DOM.

## Alternative architecture 2: Elm-Centric Deterministic Product Architecture

this variant promotes Elm from bounded interaction engine to **primary product
interaction architecture** for most important user-facing surfaces.

### Summary

- Electrobun + Solid still own the outer shell
- Elm owns much more of the actual product UI
- HTMX is demoted to admin or secondary ops surfaces
- Elysia still owns the public contract
- Drogon and C++ stay as compute layers

### Use this when

- the product's value lives in correctness-sensitive workflows
- the UI is effectively a state machine
- undo/redo, replayability, determinism, and explicit state transitions matter a
  lot
- the team is willing to respect Elm's interop limitations instead of fighting
  them with passive-aggressive port abuse

### Avoid this when

- the product is mostly document, CRUD, or admin flows
- the team actually wants casual JS interop everywhere
- the team is not prepared to think in bounded TEA surfaces
- the product spends more time rendering server-authored documents than it does
  driving deep state

### Mandatory laws

1. **Elm must own real territory.**
   - not just a tiny form
   - not just one tab because someone likes purity
2. **Ports stay coarse.**
   - command in
   - result out
   - event out
   - config in
   - avoid tiny chatty message spam across the boundary
3. **Do not treat Elm as a generic JS helper.**
4. **If a feature needs arbitrary browser or library access all day, maybe it is
   not an Elm feature.**
5. **Solid hosts; Elm governs.**
   - the shell may mount or unmount
   - the shell does not micromanage internal Elm state
6. **HTMX stays out of Elm-governed surfaces.**
   - the island boundary must be crisp

### Why this can be better than the default

because some products are just screaming for explicit state machines.
if the important surfaces look like editors, simulators, planners, or guided
workflow engines, Elm can reduce bug classes the rest of the stack cannot.

### Why this can be worse than the default

because Elm interop is intentionally constrained.
if the product wants constant direct entanglement with arbitrary JS widgets,
random browser APIs, or ad hoc framework glue, Elm becomes a pain tax instead of
a superpower.

## Alternative architecture 3: Compute-First Native Platform Architecture

this variant centers the product more heavily around **native C++ compute** and
usually promotes **Drogon (or equivalent service boundary)**, while treating
Elysia as a thinner contract or edge layer.

### Summary

- native compute service boundaries become closer to the product's operational
  heart (often Drogon in this stack)
- Elysia still exists, but may mostly shape sessions, auth, web or desktop edge
  concerns, and client-specific contracts
- the shared C++ core is not just a reusable library; it is the center of the
  system's value
- Electrobun remains a client shell
- Wasm may exist for previews, local simulations, or browser portability

### Use this when

- the product is fundamentally a native compute platform with a UI around it
- the hard problems are CPU-heavy, concurrency-heavy, simulation-heavy, or
  numerically intense
- performance and determinism of the native lane dominate over convenience of the
  TS lane
- the product might have multiple clients talking to the same compute engine

### Avoid this when

- the real product complexity is auth, forms, composition, and product UX
- the native layer would only be there for one small hot function
- Elysia would end up proxying 99% of traffic with zero value added

### Mandatory laws

1. **If Drogon becomes public, say so explicitly.**
   - do not keep pretending Elysia is the only public layer if clients now depend
     on Drogon contracts
2. **Elysia must either own the product contract or be consciously demoted.**
   - fake sovereignty is worse than honest thinness
3. **Keep auth and policy centralized.**
   - do not split product policy randomly between Elysia and Drogon
4. **C++ remains the algorithmic truth.**
   - not Elysia convenience rewrites
   - not one-off JS ports
5. **Use FlatBuffers only where the hot path really needs it.**

### Why this can be better than the default

because some products are honestly native systems with web or desktop clients,
not web apps pretending to do serious compute.
that distinction matters.

### Why this can be worse than the default

because teams often let compute-first architecture become an excuse for
public-contract chaos.
if every client starts speaking directly to the native monster, the product edge
becomes less governable.

## Alternative architecture 4: Local-First Synced Workstation Architecture

this variant makes **Turso Sync** much more central to user experience.

### Summary

- local reads and writes are primary during active usage
- cloud truth still exists, usually in PostgreSQL-backed server lanes
- sync is explicit, not magical
- Electrobun is very attractive here because local device semantics matter
- Elysia and Drogon remain important but do not own every interaction moment

### Use this when

- the app must stay useful offline
- users spend long periods disconnected or intermittently connected
- local durability, startup speed, and device-local workflows matter a lot
- conflict domains are narrow enough to make explicit sync rules viable

### Avoid this when

- many users are constantly contending on the same records
- conflict semantics are complex and the team has no merge strategy beyond hope
- the product does not actually benefit from offline or local-first workflows

### Mandatory laws

1. **Turso is local operational truth, not universal truth.**
2. **PostgreSQL remains canonical unless explicitly narrowed otherwise.**
3. **Sync timing is explicit.**
   - startup pull
   - manual sync
   - background sync
   - connectivity-event sync
   - conflict recovery
4. **Acknowledge Turso Sync conflict policy.**
   - official docs say last push wins
   - if that is dangerous for an entity class, do not use naïve sync there
5. **Use `bootstrapIfEmpty` intentionally.**
   - if offline-first startup matters, say so and configure it accordingly
6. **Observe sync health.**
   - checkpoint
   - stats
   - last pull time
   - last push time
   - WAL growth

### Why this can be better than the default

because some desktop and field apps live or die by local-first credibility.
latency, resiliency, and "works on the train" are not fake features.

### Why this can be worse than the default

because teams routinely underestimate sync semantics.
local-first done casually is just distributed systems pain wearing a cozy hat.

## Alternative architecture 5: GPU-First Visualization Workbench Architecture

this variant makes the **GPU lane** far more central than in the default model.

### Summary

- Slang becomes a first-class source of product capability, not just a side lane
- WebGPU is central to rendering or compute
- the C++ core may feed GPU pipelines or share layouts with them
- Electrobun can host desktop-grade GPU-heavy experiences cleanly
- Elysia and Drogon remain around the product, but they are not the star

### Use this when

- the product is a renderer, visualizer, editor, simulation viewer, CAD-like
  workbench, media tool, scientific tool, or GPU-accelerated analysis surface
- shader modularity and multi-target deployment matter
- there is real benefit to one shader source across targets

### Avoid this when

- the GPU path is speculative
- the product is mostly forms and coordination work
- Slang and WebGPU are being added because they are cool, not because they are
  needed

### Mandatory laws

1. **Slang is the authoring truth.**
   - WGSL is a generated or target form for the web path
2. **Capability checks are explicit.**
   - Slang's capability model exists for a reason
3. **Provide fallbacks.**
   - if a critical path needs CPU fallback, say so
   - if a feature is optional without GPU, say so
4. **Keep product logic out of shaders.**
5. **Keep shader module boundaries sane.**
   - do not treat shaders as one monolithic pastebin
6. **Own buffer layout strategy.**
   - if binary layouts matter across CPU, Wasm, and GPU, govern them on purpose

### Why this can be better than the default

because some products truly are visual or numeric systems first.
for them, the GPU is not a side quest.
it is the thing.

### Why this can be worse than the default

because GPU-first architecture can spread its worldview everywhere if nobody puts
up fences.
your billing rules do not need to be shader-adjacent, bestie.

## The demotion law

not every project on this stack needs every lane to dominate.
that is healthy.

### A component may be present in one of three states

- **primary**
  - this component is central to the architecture
- **bounded**
  - this component has named territory and real value
- **dormant**
  - this component exists in the toolbelt or roadmap but has no current
    sovereignty

### Good examples

- Elm is dormant in a hypermedia-heavy admin app
- HTMX is bounded to `/ops/*` in a Solid-heavy desktop workbench
- Drogon is dormant until compute extraction is justified
- Turso is bounded to local drafts and cached work queues
- WebGPU is bounded to one analysis view

### Bad examples

- Elm is "kinda around" but nobody can name its territory
- HTMX is used wherever Solid feels annoying
- Drogon exists because C++ should be somewhere
- FlatBuffers exist because binary is cool
- Turso is present "for future offline" with no policy

## The shell and UI constitutions

## Electrobun constitution (the shell sovereign)

Electrobun is the **desktop host government**.

### What Electrobun is for

- window lifecycle
- system integration
- tray, menus, context menus
- BrowserWindow and BrowserView hosting
- app packaging and distribution
- updater orchestration
- native-feeling desktop affordances
- bundling views and resources
- desktop-specific bridge surfaces

### What Electrobun is not for

- becoming the main domain rules engine
- replacing Elysia as the public contract layer
- replacing Drogon as the compute service
- inventing random direct native bridges from every screen
- smearing native shell logic through all product code

### Laws

1. **Electrobun owns shell concerns.**
2. **Use system webview by default.**
   - the docs clearly position system webview as the default and CEF as optional
3. **Enable CEF only for actual browser-platform gaps.**
   - not for speculative comfort
4. **Keep the Bun worker / native wrapper split in mind.**
   - the official architecture uses the native GUI event loop on the main thread
     and app logic in a worker
5. **Bridge intentionally.**
   - postMessage, FFI, or approved APIs
   - not ad hoc side channels all over the place
6. **Exploit the updater if the product ships desktop updates often.**
   - tiny patches are one of Electrobun's real superpowers
7. **Respect distribution-time concerns.**
   - code signing
   - notarization
   - artifacts
   - static hosting of updates
8. **Treat Electrobun as a strategic dependency, not an untouchable identity.**
9. **Maintain shell escape seams.**

- isolate host APIs behind an adapter boundary
- keep renderer logic portable enough that a host swap is painful but possible

### Good Electrobun territory

- top-level shell state
- windows and multi-view orchestration
- desktop menus and accelerators
- file picker and local FS affordances
- updater lifecycle
- OS-specific integration
- native drag regions
- desktop-only WebGPU or view hosting concerns

### Smells

- business workflows depending on shell-specific APIs everywhere
- every feature getting its own special native bridge
- updater concerns leaking into product logic
- desktop packaging structure being treated like a domain abstraction

### Electrobun maturity and contingency law

Electrobun has compelling strengths, but it is also a younger ecosystem bet than
older desktop shells.

that does **not** mean "do not use Electrobun."
it means "use it with explicit contingency discipline."

required safeguards:

1. keep a host-adapter seam for native affordances
2. avoid scattering Electrobun-specific calls through domain code
3. keep route and feature logic shell-portable where practical
4. document what a host migration would touch first

if these safeguards are ignored, the shell choice stops being a tool decision and
becomes a lock-in event.

### Electrobun migration readiness checklist

keep this checklist green continuously, not only when panic starts:

- [ ] host-specific APIs are wrapped behind an internal adapter module
- [ ] renderer code avoids direct dependency on host internals except at adapter
  edges
- [ ] key workflows can run in a non-Electrobun dev surface for contingency
  testing
- [ ] packaging assumptions are documented separately from domain architecture
- [ ] update mechanism dependencies are isolated from product-domain logic

### Electrobun risk trigger thresholds

if two or more of the following persist across release cycles, open a formal
contingency ADR:

1. repeated breaking changes with no practical migration path
2. unresolved platform regressions on required OS targets
3. release velocity stalls against project roadmap needs
4. critical upstream issues blocking security or distribution requirements
5. team cannot execute shell upgrades within acceptable release windows

the goal is not to abandon Electrobun preemptively.
the goal is to avoid waking up with no realistic options.

### Electrobun packaging law

because the docs show real structure and update behavior, respect these truths:

- the desktop bundle is a real platform artifact, not just a JS folder
- the updater relies on hashes and patch chains
- distribution and dev builds differ materially
- non-dev builds produce artifacts with long-term operational consequences

if the product is desktop-first, release engineering is part of architecture,
not an afterthought.

## Bun constitution (the TS lane runtime and toolchain)

Bun is the default runtime and tooling nucleus for the TypeScript half of this
stack.

### What Bun is for

- runtime for Elysia and TS-side utilities
- runtime used by Electrobun app logic
- package manager
- bundling and testing
- scripts and development workflows
- fast tooling loop

### What Bun is not for

- pretending Node compatibility is magically perfect for every ecosystem corner
- becoming the native build truth for C++
- dictating architecture to the CMake or shader side
- replacing serious thought about driver support

### Laws

1. **Bun is the default TS runtime unless a project has a proven reason
   otherwise.**
2. **Check compatibility for legacy Node packages.**
3. **Use Bun for TS scripts, not for C++ identity.**
4. **Let Bun orchestrate, not annex.**
   - it can call CMake
   - it should not replace CMake's authority over native builds
5. **Prefer Bun-native drivers and integrations where mature.**
   - especially in Elysia and Drizzle lanes

### Good Bun territory

- TS runtime
- TS tests
- dev scripts
- bundling the shell-side web assets
- running the gateway and auxiliary tooling

### Smells

- hidden Node-only assumptions everywhere
- using Bun's presence as a reason to keep everything in TS even when the shared
  C++ core would be the honest owner
- build graphs where C++ artifacts depend on Bun quirks rather than CMake truth

## SolidJS constitution (the shell brain)

Solid is the default **shell UI owner**.

### What Solid is for

- app chrome
- route shell
- navigation bars and sidebars
- transient UI state
- notifications
- shell-level status indicators
- component composition
- embedding Elm or HTMX-governed territories cleanly
- responsive desktop UI around native shell features

### What Solid is not for

- owning every meaningful state machine by inertia
- becoming a universal store monarchy
- swallowing Elm territory because it happens to be nearby
- rendering server-authored CRUD pages that HTMX would do more cleanly

### Laws

1. **Solid owns the shell.**
2. **Shell state is not the same as domain state.**
3. **If a feature wants TEA-level discipline, let Elm own it.**
4. **If a route wants server-authored HTML, let HTMX own it.**
5. **Solid components may host islands; they must not blur island ownership.**
6. **Cross-cutting UI belongs here.**
   - theme
   - layout
   - menus
   - toasts
   - connection status
   - desktop affordance wrappers

### Good Solid state

- layout mode
- active panel
- selected shell tab
- menu visibility
- global notification center
- connectivity badge
- current workspace chrome

### Bad Solid state

- complex transactional wizard state if Elm exists for that job
- authoritative document model for a deep editor while Elm or C++ also claim it
- long-term sync conflict resolution state that belongs in local-first logic

### Smells

- a global Solid store that quietly becomes the application's actual sovereign
- components reaching through every feature boundary
- shell concerns and domain concerns interleaving until nothing has a clean home

## Tailwind CSS constitution (the one visual dialect)

Tailwind is not the architecture.
Tailwind is the **visual grammar** of the stack.
that matters more than people admit.

### What Tailwind is for

- fast, consistent styling across UI lanes
- a shared design token layer
- consistent spacing, type, layout, and component rhythm across Solid, Elm DOM,
  and HTMX fragments
- reducing CSS divergence between shell, hypermedia, and bounded islands

### What Tailwind is not for

- encoding business logic in class-name soups
- becoming the only place responsive or semantic thinking happens
- fragmenting into one utility style in HTMX and another in Solid and another in
  Elm

### Laws

1. **There is one design system for the whole stack.**
   - not a Tailwind dialect per lane
2. **Extract repeated patterns.**
   - do not let the app become `class="px-2 py-1 ..."` archaeology forever
3. **Tokens first.**
   - colors, spacing, radii, shadows, typography, and state colors should have a
     coherent design intent
4. **Use Tailwind to unify UI lanes, not to hide them.**
5. **Never encode ownership confusion in shared utility patterns.**
   - a button style can be shared
   - a domain workflow should not become a CSS convention

### Good Tailwind use

- common form styles across HTMX and Solid
- consistent panels and cards in shell and ops views
- stable spacing system across desktop shell and fragments
- state tokens for success, warning, sync, compute, offline, and destructive
  actions

### Smells

- every lane invents its own component vocabulary
- copy-paste utility blobs with no abstraction or token discipline
- semantic state living in class strings rather than component or route logic

## Elm constitution (the interaction engine)

Elm is a **bounded sovereign**.
if you bring it in, give it law.

### What Elm is for

- deterministic interaction models
- correctness-sensitive feature state
- explicit update transitions
- complex workflows that benefit from TEA
- deep feature islands
- bounded editors, planners, control panels, workflow engines, or state-heavy
  interaction surfaces

### What Elm is not for

- a thin wrapper around DOM calls
- a tiny widget you included because purity is cute
- an interop trampoline for arbitrary browser APIs
- a shell replacement
- a hidden state owner beneath Solid's shell state

### Laws

1. **Elm must own bounded territory.**
2. **TEA is the point.**
   - if the feature does not benefit from Model / View / Update, reconsider
3. **Ports are coarse.**
4. **Flags are for configuration, not casual dependency injection theater.**
5. **Custom elements are okay when the island boundary is honest.**
6. **Do not ask Elm to behave like React with worse marketing.**
7. **Respect the interop limits on purpose.**
   - Elm deliberately chose ports and custom elements over arbitrary JS FFI

### Good Elm territory

- simulation control panel
- deterministic workflow builder
- review or approval engine with explicit transitions
- bounded editor
- decision tree tool
- wizard with complex transitions and validation semantics

### Bad Elm territory

- one isolated button or modal with no real state model
- a feature that mostly wraps existing JS libraries with constant imperative
  escape hatches
- a hypermedia CRUD page

### The Elm island rule

Elm is easiest to keep healthy when:

- Solid or Electrobun shell mounts it
- the island gets coarse initial config
- the island emits coarse events or commands
- side effects cross through a narrow bridge
- the shell does not poke Elm's internal state directly

### Smells

- ports for every tiny UI interaction
- constant JS interop to keep the feature alive
- Elm plus HTMX plus Solid all mutating the same surface
- nobody can name what Elm owns besides "the important part"

bestie, name the important part.

## HTMX constitution (the hypermedia lane)

HTMX is **not** the fallback when people feel tired.
HTMX is a real architectural lane.

### What HTMX is for

- server-authored HTML fragments
- CRUD pages
- forms
- reports
- queues
- approval panels
- settings pages
- document-centric workflows
- progressive enhancement where it actually matters
- small islands of behavior driven by events and HTML semantics

### What HTMX is not for

- re-implementing a SPA badly
- becoming the secret default because nobody wanted to make a routing decision
- owning the same feature surface as Elm or Solid state logic
- shoving raw user HTML into the DOM without sanitation or `hx-disable`

### Laws

1. **HTMX territory must be named.**
2. **Server responses are HTML by default in HTMX land.**
3. **If you use pushed URLs, serve full pages for them.**
4. **Use `Vary: HX-Request` when full vs fragment rendering differs.**
5. **Treat `HX-Request`, `HX-Boosted`, `HX-Trigger`, and related headers as
   first-class part of the boundary.**
6. **Validation is server truth.**
7. **Progressive enhancement is a bonus, not a slogan.**
8. **If a non-HTMX library participates, integrate through events or bounded
   islands.**
9. **Use HTMX security tools when injecting risky content.**
   - `hx-disable`
   - CSP
   - same-origin request policy where appropriate
10. **Keep history and caching semantics explicit.**

### Important official-doc facts that should become laws

- HTMX expects **HTML** responses
- `hx-push-url` implies the route must be accessible as a full page
- `hx-sync` exists for request coordination; use it instead of pretending races do
  not exist
- progress indicators, response headers, and response code handling are all part
  of the formal tool, not hacks
- the docs strongly favor event-driven interop and island isolation
- the essay on hypermedia-friendly scripting explicitly argues for:
  - respecting HATEOAS
  - keeping purely client-only state client-only
  - using events between components
  - isolating non-hypermedia islands

### Good HTMX territory in this stack

- `/ops/*`
- `/admin/*`
- `/reports/*`
- `/review/*`
- `/settings/*`
- server-authored side panels, inspectors, and queue surfaces

### Bad HTMX territory in this stack

- the same route body that Elm thinks it owns
- deeply interactive simulation workbench canvas surrounds
- product surfaces that are mostly client-state machines

### Smells

- HTMX partials injected into an Elm-owned island
- Solid local state and HTMX fragments racing over the same DOM subtree
- using HTMX for a feature because "the reactive version was annoying"
- no full-page fallback for pushed URLs
- no caching strategy for `HX-Request` variation

## The service and contract constitutions

## Elysia constitution (the public contract layer)

Elysia is the default **public contract owner**.

### What Elysia is for

- auth and session-aware policy at the product edge
- request validation
- type-safe route definitions
- HTML fragment rendering for HTMX surfaces
- JSON APIs for Solid or Elm-driven surfaces
- streaming or websocket endpoints at the public edge when appropriate
- OpenAPI generation
- end-to-end type flow in the TS lane
- composition and orchestration between clients and deeper services

### What Elysia is not for

- being the long-term home of the heaviest compute logic
- pretending Drizzle is the only schema system that matters to C++ and Wasm
- becoming a giant monolith because every request passes through it anyway

### Laws

1. **Elysia owns the public contract by default.**
2. **Schema is public-layer truth in the TS lane.**
   - validation
   - runtime inference
   - type inference
   - docs generation
3. **If the contract is product-facing, shape it here.**
4. **If the workload is compute-heavy, delegate it.**
5. **Translate internal errors into public semantics.**
6. **Use OpenAPI and type-generation features to keep contracts honest.**
7. **Use Drizzle here, not as a diplomatic annex over the native lane.**
8. **If Elysia is demoted in a compute-first architecture, say so explicitly.**

### Why Elysia is strong here

because the official positioning is almost screaming BFF energy:

- schema as source of truth
- OpenAPI from types
- end-to-end type safety
- ergonomic handlers
- Bun-native speed
- WebSocket and streaming support
- OpenTelemetry support

that is extremely good public-edge material.

### Good Elysia territory

- authentication
- sessions
- public routing
- frontend composition
- HTML fragments for HTMX
- JSON or stream responses for client apps
- policy gates and request normalization
- orchestration of calls to Drogon or the shared core

### Bad Elysia territory

- large simulation kernels
- performance-critical numerical inner loops
- duplicated native business logic
- a second half-written compute engine in TypeScript

### Smells

- Elysia route handlers growing compute limbs because "it was faster to just do
  it here"
- public contracts mirroring Drogon internal contracts 1:1 with no translation
- every service concern collecting inside Elysia because it already has the
  request object

## Drizzle constitution (typed SQL in the TS lane)

Drizzle is the **TypeScript persistence specialist** of this stack.

### What Drizzle is for

- schema declaration in the TS lane
- migrations in the TS lane
- typed SQL access from Elysia and TS-side services or utilities
- coordinating TS-side access to PostgreSQL, Turso, and related supported
  backends
- keeping Elysia and Bun-side database access explicit and structured

### What Drizzle is not for

- defining the one true schema for C++, Wasm, Elm, and every other lane by force
- replacing thoughtful data contracts between TS and native systems
- becoming a theology where every part of the system must imitate the TS DSL

### Drizzle reality check

the official site and release cadence show a project that:

- ships fast
- adds features aggressively
- evolves migration behavior meaningfully
- has a current 1.0 beta story
- has changed validator packaging and dialect coverage over time
- is increasingly broad across dialects and runtimes

this is good.
it also means you should govern it consciously.

### Laws

1. **Drizzle owns typed SQL in the TS lane.**
2. **Do not universalize Drizzle concepts into the native lane unless doing so is
   clearly worth it.**
3. **Migration policy must be explicit.**
4. **Keep Drizzle upgrades and migration-engine changes under review.**
5. **Let PostgreSQL remain the data truth and Drizzle remain the TS access
   strategy.**
6. **Use Drizzle with Turso where it earns its keep, but do not let that erase the
   sync semantics.**
7. **Use Drizzle's RLS and dialect support thoughtfully where it aligns with
   Postgres policy.**

### Good Drizzle territory

- Elysia handlers and service modules
- admin jobs and operational scripts in Bun
- TS-side migrations and schema evolution
- typed DB access for HTML fragment routes and JSON APIs

### Bad Drizzle territory

- hot native compute loops
- binary contract definitions
- cross-language shared-core replacement

### Smells

- everyone starts saying "the Drizzle schema" when they really mean "the TS lane's
  SQL schema"
- native C++ re-derives business rules from Drizzle-generated artifacts without
  a proper contract
- Drizzle upgrade churn silently changes migration behavior with no review

## Drogon constitution (the compute engine)

Drogon is an **optional out-of-process compute service**, not an automatic
network hop.

### Compute boundary ladder (default order)

choose the lightest boundary that satisfies the workload:

1. **in-process call path**

- Bun-side FFI into compiled native code or equivalent thin host bridge

2. **local supervised process boundary**

- stdio or unix-domain/named-pipe style protocol when isolation is needed but
    service ceremony is not

3. **durable queue-backed worker boundary**

- NATS, Redis-backed queue, or simple task queue when retries, deferred
  execution, or fan-out matter but a full service does not yet earn itself

4. **Drogon internal service**

- HTTP or websocket service when independent scaling, lifecycle, or
    multi-caller integration is justified

5. **Drogon public promotion**

- only in consciously compute-first architectures

the default should not skip from step 1 to step 4 without reason.

protocol note:

- HTTP is common and pragmatic, but not mandatory for every internal compute seam
- if typed service contracts or internal RPC ergonomics matter more than
  web-style routing, gRPC or equivalent RPC transport may be the better fit
- if the need is isolation without full service ceremony, supervised process
  protocols (stdio or local sockets/pipes) can be enough
- if the need is deferred execution, retries, or fan-out without a full service,
  queue-backed worker protocols can be enough

### Drogon transport decision tree (practical)

use this quick tree before introducing or expanding a Drogon service:

1. **single caller + low latency sensitivity + shared deploy cadence?**
   - start in-process (Bun FFI / native bridge)
2. **need crash isolation or memory isolation but still single-caller?**
   - prefer supervised local process protocol first
3. **need durable async work, retries, or fan-out but still not a full service?**
  - prefer a queue-backed worker boundary first
4. **need independent scaling, multi-caller consumption, or long-lived service
  lifecycle?**
   - promote to Drogon internal service
5. **need strongly typed service contracts across many internal callers?**
   - evaluate RPC transport strategy explicitly (Drogon HTTP/WebSocket vs gRPC or
     equivalent), then document the choice
6. **need public-facing compute API identity?**
   - only then consider public Drogon promotion with explicit contract governance

### Concrete examples

- **example A: hot synchronous scoring call from one Elysia route**
  - default: in-process boundary (FFI)
- **example B: batch transform that can crash on malformed artifacts**
  - default: supervised local process boundary first
- **example C: simulation service consumed by API, CLI, and internal workers**
  - default: Drogon service boundary likely warranted
- **example D: long-running streamed simulation with independent autoscaling**
  - default: Drogon internal service, with explicit edge contract mapping in
    Elysia

### What Drogon is for

- async service endpoints for internal compute
- long-running jobs
- progress streaming
- concurrency-heavy operations
- native-first API surfaces for compute work
- coroutine-based handlers where they help readability
- internal coordination over HTTP, WebSocket, RPC, or process protocols as
  architecture warrants

### What Drogon is not for

- becoming a stealth second public backend by convenience
- owning shell or client UX concerns
- replacing Elysia on public routes just because C++ feels strong

### Laws

1. **Drogon is optional and internal by default.**
2. **Prefer Bun FFI or in-process native calls before introducing service
  transport.**
3. **Drogon computes; Elysia composes.**
4. **If Drogon becomes public, say so explicitly and adjust the whole contract
   story.**
5. **Keep auth and product policy centralized unless the architecture consciously
   changes that.**
6. **Use Drogon when the service boundary genuinely matters.**
   - async throughput
   - simulation
   - long-running tasks
   - streaming

- multi-caller service integration
- independent scaling or deploy cadence

7. **Do not make clients pick between Elysia and Drogon for the same kind of
   product call.**

### Good Drogon territory

- simulation jobs
- internal transform pipelines
- native model execution
- streaming heavy results
- compute status APIs
- native WebSocket progress updates

### Bad Drogon territory

- the product's general-purpose public REST or HTML contract by accident
- auth pages
- settings forms
- user profile page composition

### Smells

- client apps hitting Drogon directly because it was easier one time
- product-level errors and semantics leaking straight from native handlers
- duplicated API shape work between Elysia and Drogon

## The data constitutions

## PostgreSQL constitution (canonical truth)

PostgreSQL is the default **durable system of record** for this stack.

### What PostgreSQL is for

- authoritative multi-user state
- relational invariants
- transactions
- permissions and policy-relevant data
- job coordination metadata
- durable domain truth
- historical correctness and auditable writes

### What PostgreSQL is not for

- local ephemeral drafts that do not need round trips
- pretending device-local state does not exist
- being bypassed casually by synced local stores for canonical data

### Laws

1. **PostgreSQL is canonical truth by default.**
2. **The more contested and collaborative an entity is, the more it belongs
   here.**
3. **Cross-user invariants belong here.**
4. **Durable permissions and policy-relevant state belong here.**
5. **If a project departs from this default, it must say exactly which entities
   are exceptions.**

### Good PostgreSQL entities

- users
- teams
- permissions
- subscriptions and billing-adjacent records
- shared documents or durable objects
- job metadata
- authoritative domain records

### Smells

- treating Postgres as merely the backup for what actually lives locally
- allowing multiple writers through different services without clear ownership
- confusing read-model copies with canonical ownership

## Turso Sync constitution (local-first truth with explicit humility)

Turso is a **local-first operational store**, not default universal truth.

### What Turso is for

- local reads and writes
- offline work
- device-local drafts
- synced projections
- cached subsets of canonical data
- field or desktop workflows that should not block on the network
- edge-adjacent or user-adjacent state

### What Turso is not for

- hidden multi-user canonical truth
- a casual replacement for PostgreSQL
- conflict-free magic when the official model is explicitly last-push-wins

### Laws

1. **Turso sync is explicit.**
   - `push()`
   - `pull()`
   - not telepathy
2. **Local writes are safe, but not magically canonical.**
3. **If offline-first startup matters, configure bootstrap behavior on purpose.**
4. **Checkpoint and stats matter.**
   - WAL growth is not a decorative metric
5. **Do not let contentious collaborative writes use naïve last-push-wins if that
   would hurt product semantics.**
6. **Partition what belongs in Turso carefully.**

### Good Turso entities

- local drafts
- cached work queues
- device-local settings
- replicated read models
- local notes and staging data
- offline task state
- local projections for speed

### Bad Turso entities by default

- financial truth
- cross-user permissions
- heavily contested collaborative objects
- canonical ledger-like state

### Smells

- no explicit sync schedule
- no user-visible sync health state
- no answer for conflict semantics
- treating local state as canonical because it is faster

## Postgres versus Turso decision law

for each entity, answer these questions explicitly:

- where is the authoritative durable record?
- can users edit it offline?
- is last-push-wins acceptable?
- who merges or rejects conflicts?
- is Turso storing a projection, a draft, a local-first canonical subset, or a
  cache?
- what happens after the first launch when the remote is unreachable?

if the answers are vague, the data topology is not done.

## The native, Wasm, and binary constitutions

## modern C++ constitution (the shared algorithmic center)

C++ is the **performance truth** of this stack when a shared core is warranted.

### What modern C++ is for

- core algorithms
- simulation logic
- numeric kernels
- performance-critical transforms
- memory-sensitive operations
- shared domain logic that deserves native and Wasm targets

### What modern C++ is not for

- shell routing
- casual product UI
- random HTML generation
- pretending all code should move native because native is cool

### Laws

1. **Write the hot logic once.**
2. **Keep the C++ core host-agnostic where practical.**
3. **Separate pure core from host wrappers.**
4. **Do not duplicate the same algorithm in TS and C++ just because the wrapper
   exists nearby.**
5. **Use C++ where the complexity is justified by real product value.**
6. **If a function matters in both native and browser execution, bias toward the
   shared core.**

### Good C++ territory

- simulation
- geometric or numeric kernels
- complex transforms
- performance-sensitive validation or compilation stages
- buffer packing or layout-sensitive logic
- GPU-adjacent data preparation

### Smells

- giant host wrappers becoming the true owner of logic
- parallel TS and C++ implementations drifting apart
- using native code for prestige, not value

## CMake constitution (the native build truth)

CMake is the canonical build system for the native lane.

### What CMake is for

- C++ compilation
- native library and executable graphs
- Emscripten target graphs
- generated headers or code from schemas or shader pipelines
- testing the native lane
- shader compilation orchestration where appropriate

### What CMake is not for

- being replaced by Bun scripts as the actual source of build truth
- owning the TS packaging and route build graph
- vague wrapper status beneath some `package.json` spellbook

### Laws

1. **CMake owns native build truth.**
2. **Bun may orchestrate CMake, but not supersede it.**
3. **Wasm builds should share as much CMake truth as possible with native builds.**
4. **Generated artifacts and output directories must be explicit.**
5. **Do not let shader, schema, and core code generation become shell scripts with
   no build graph governance.**

### Good CMake territory

- C++ targets
- Wasm targets
- unit tests
- codegen steps
- shared library packaging
- shader compilation helpers

### Smells

- native build steps hidden in JS scripts with no reproducible CMake target
- duplicated flags between native and Wasm builds
- no explicit dependency edges between generated schemas, shaders, and libraries

## Emscripten and Embind constitution (the browser bridge)

Emscripten is the right way to bring the shared core to the browser or webview
execution surface when native portability matters.

### What Emscripten is for

- compiling portable C++ to Wasm
- producing the JS glue needed for execution in browser or related runtimes
- reusing shared core logic without manual rewrite

### What Embind is for

- ergonomic JS bindings around C++ APIs
- exposing coarse, object-ish interfaces to JS when that ergonomics trade-off is
  actually worth it

### What they are not for

- pretending browser runtime constraints do not exist
- chatty cross-boundary micro-calls on every UI event
- replacing disciplined API design with "just bind the whole class graph"

### Laws

1. **Compile shared core to Wasm only when shared logic actually exists.**
2. **Respect browser-runtime differences.**
   - main loop
   - file handling
   - threading constraints
   - startup strategy
3. **Keep Wasm boundaries coarse.**
4. **Use Embind for ergonomics, not for every hot path.**
5. **If the boundary is hot, consider simpler ABI surfaces or binary contracts.**
6. **The browser host still owns DOM, navigation, and shell policy.**

### Good Wasm calls

- run simulation step
- compile or transform document
- evaluate planner state
- process batch geometry
- load or save binary model fragment
- execute long-lived worker-side core operations

### Bad Wasm calls

- read one field per keypress
- call across the boundary for trivial UI state
- use Wasm as a fashionable helper for things TS already does fine and cheaply

### Smells

- hundreds of tiny interop calls in a single interaction
- host logic and Wasm logic both owning the same validation semantics
- main-thread UI blocked by synchronous compute that should be isolated

## C++ WebAssembly constitution (one core, two embodiments)

when C++ is built to both native and Wasm targets, this stack becomes powerful in
a very specific way.

### The good version

- one core
- two or more targets
- thin wrappers
- explicit versioned boundary
- host-specific lifecycle kept out of the core

### The cursed version

- "native version"
- "Wasm version"
- "TS fallback"
- all roughly equivalent
- none actually shared

that is not portability.
that is a three-body maintenance problem.

### Laws

1. **The shared core contract must be versioned.**
2. **Behavior must match across targets unless divergence is explicitly justified.**
3. **Host wrappers must stay thin and obvious.**
4. **If one host needs different semantics, document the divergence.**

## FlatBuffers constitution (binary hot path only)

FlatBuffers are powerful.
FlatBuffers are also expensive in cognitive terms if sprayed across the repo.

### What FlatBuffers are for

- internal binary protocols
- low-overhead shared-core boundaries
- native/Wasm payloads where parse-free access matters
- layout-sensitive high-volume data
- stable schema evolution in hot internal paths

### What FlatBuffers are not for

- the public auth API
- ordinary CRUD payloads
- simple HTML fragment transport
- turning every contract into a binary ritual

### Laws

1. **FlatBuffers stay inside the hot path.**
2. **Public edges stay HTML or JSON by default.**
3. **Own schema evolution deliberately.**
4. **Treat FlatBuffers as a performance tool, not a general identity.**
5. **Keep decoding and translation boundaries explicit.**

### Good FlatBuffers territory

- C++ core to Wasm
- Drogon compute outputs to internal consumers
- GPU-adjacent layout preparation pipelines
- large binary model fragments
- high-frequency or large-volume internal payloads

### Bad FlatBuffers territory

- login form responses
- ordinary user settings pages
- admin panels
- public REST or hypermedia endpoints by default

### Smells

- developers cannot inspect product traffic without custom viewers
- binary payloads leaking into every feature because they were already there
- no named translation layer between human-readable and binary boundaries

## The GPU constitutions

## Slang constitution (shader source of truth)

Slang is the preferred authoring language for shader logic in this stack.

### What Slang is for

- one shader source across multiple target backends
- modular shader code organization
- HLSL and GLSL migration
- capability-aware shader authoring
- keeping large shader codebases sane
- enabling WebGPU without making WGSL the only source of truth

### What Slang is not for

- replacing application logic
- letting native graphics concerns bully every other layer
- becoming a shiny side quest with no real product need

### Laws

1. **Slang is authoring truth; WGSL is a target artifact.**
2. **Use modules.**
3. **Use the capability system honestly.**
4. **If a feature is target-specific, say so.**
5. **Do not fork shader truth per platform unless absolutely necessary.**
6. **Keep authoring and compilation policy centralized.**

### Good Slang territory

- shared shader library
- compute kernels
- rendering passes
- differentiable or ML-adjacent graphics experiments if the product truly needs
  them
- shader code that must target multiple backends

### Smells

- raw WGSL hand-maintained beside raw HLSL beside raw GLSL with no clear source
  of truth
- platform-specific shader drift nobody owns
- shader modules organized by accident instead of by rendering or compute domain

## WebGPU constitution (portable GPU execution)

WebGPU is the product-facing execution surface for portable GPU workloads.

### What WebGPU is for

- modern GPU rendering
- modern GPU compute
- portable accelerated execution in browser-like environments
- GPU-heavy views in shell or web surfaces

### What WebGPU is not for

- replacing the CPU core indiscriminately
- carrying business truth
- justifying GPU complexity before the bottleneck is known

### Laws

1. **The GPU lane must earn itself.**
2. **Critical user flows need a fallback story.**
3. **Buffer layouts and CPU or GPU contract shapes must be governed.**
4. **Rendering logic stays rendering logic.**
5. **Do not move business policy into compute kernels because the GPU exists.**

### Smells

- product correctness depending on a GPU feature not widely available
- no capability detection path
- buffer layout contracts defined in three places

## The seam laws (this is where stacks become either elegant or cursed)

## Shell to interaction engine seam (Solid <-> Elm)

### Good

- Solid hosts
- Elm governs bounded feature state
- messages are coarse
- mounting and unmounting are explicit
- ownership is obvious

### Bad

- Solid reaches into Elm state all day
- Elm requires constant shell intervention for routine behavior
- both think they own route or feature state

### Law

if both sides own the same meaningful state, the boundary is fake.
fix it.

## Shell to hypermedia seam (Solid <-> HTMX)

### Good

- route-scoped ownership
- HTMX surfaces live in named zones
- Solid shell contains them without pretending to own their local interaction
  model
- events are explicit

### Bad

- HTMX fragments injected into components that also own reactive state for the
  same subtree
- shell routing plus fragment routing plus browser history semantics fighting at
  once

### Law

HTMX may live inside the shell.
it may not erase shell-level ownership or create DOM civil war.

## HTMX to Elysia seam

### Good

- Elysia returns HTML fragments and full pages on purpose
- `HX-Request` and related headers are handled intentionally
- caching policy is explicit
- validation and error semantics are server-controlled

### Bad

- fragment vs full-page behavior left implicit
- 422 handling and form rerender semantics invented ad hoc
- no route ownership or full-page fallback

### Law

if HTMX is present, Elysia should know it is serving hypermedia, not just random
AJAX.

## Solid or Elm to Elysia seam

### Good

- Elysia owns contract shape
- auth, validation, and errors are consistent
- clients do not directly feel downstream weirdness

### Bad

- clients know too much about internal services
- raw compute errors bleed through
- clients hit multiple backends for equivalent product work

### Law

one obvious public contract is the default.

## Elysia to Drogon seam

### Good

- Elysia validates and composes
- Drogon computes
- public and internal contracts can differ
- streaming and job semantics are explicit

### Bad

- Elysia duplicates compute logic
- Drogon dictates public shape through inertia
- clients bypass Elysia for convenience

### Law

if Drogon feels public, either make that official or reassert Elysia ownership.
no fake borders.

## Drizzle to Postgres seam

### Good

- Drizzle models TS-lane access honestly
- Postgres remains authoritative
- migrations are governed and reviewed

### Bad

- application truth is treated as identical to generated TS schema metaphors
- native lane learns about truth only through Drizzle wrappers

### Law

Drizzle is access strategy, not metaphysical sovereignty.

## Turso to Postgres seam

### Good

- canonical truth is named
- local sync store role is named
- sync timing is explicit
- conflict policy is explicit

### Bad

- both are called truth in different docs
- last-push-wins is hand-waved away
- users can write anywhere and pray later

### Law

no shadow kings.

## C++ core to Wasm host seam

### Good

- coarse commands and responses
- predictable memory or schema boundary
- host retains shell and DOM ownership

### Bad

- one interop call per click, keystroke, or layout concern
- no versioned contract
- wrapper logic starts becoming the real implementation

### Law

Wasm is for meaningful work, not decorative indirection.

## C++ core to Drogon seam

### Good

- Drogon wraps the core with service semantics
- core stays reusable
- host-only concerns remain outside the core

### Bad

- Drogon handler logic quietly owns domain rules the core should own
- core contract becomes implicit through handler glue

### Law

Drogon should expose the core, not replace it.

## FlatBuffers to human-readable edge seam

### Good

- binary inside
- translation layer explicit
- HTML or JSON outside

### Bad

- internal performance contract leaks into public UX surface
- binary payloads are now everybody's problem

### Law

the public edge is for humans first.

## Slang to WebGPU seam

### Good

- Slang authoring centralized
- WGSL generated or governed as target output
- capability differences explicit

### Bad

- manual target edits causing drift
- no single compilation story

### Law

one shader truth if humanly possible.

## Bun to CMake seam

### Good

- Bun scripts orchestrate the native build when useful
- CMake retains authority over the native graph

### Bad

- package.json scripts become the real native build system
- nobody can build the core without JS-specific folklore

### Law

orchestration is not ownership.

## Default territory map for routes and surfaces

this is the default map unless the project consciously selects another
architecture variant.

### Recommended route ownership

- `/app/*`
  - Solid shell
  - may host Elm islands
- `/app/interactive/*`
  - Solid + Elm bounded features
- `/ops/*`
  - HTMX + Elysia HTML
- `/admin/*`
  - HTMX + Elysia HTML
- `/reports/*`
  - HTMX + Elysia HTML or hybrid shell-hosted surfaces
- `/api/*`
  - Elysia public API
- `/internal/compute/*`
  - Elysia -> Drogon or protected internal-only interfaces
- `/assets/shaders/*`
  - build output territory, not hand-edited runtime truth

### Recommended product ownership map

- shell navigation and app chrome
  - Solid + Electrobun
- deterministic editor or workflow surface
  - Elm
- admin queue, report, forms, settings
  - HTMX
- auth, policy, public contract, composition
  - Elysia
- heavy compute
  - C++ core + selected boundary (FFI first, Drogon when warranted)
- durable truth
  - Postgres
- offline and local-first operational state
  - Turso
- shader code
  - Slang

## Contract style laws

## HTML law

use **HTML** when:

- the server is authoring the UI fragment
- the surface is hypermedia-friendly
- the route is form-heavy or document-heavy
- progressive enhancement matters
- HTMX is the active lane

## JSON law

use **JSON** when:

- the client owns rendering
- the shell or interaction engine needs structured API data
- the contract is product-facing but not server-rendered UI
- Solid or Elm is the primary consumer

## FlatBuffers law

use **FlatBuffers** when:

- the internal boundary is hot enough to justify binary complexity
- C++ and Wasm need shared schema efficiency
- payload size or parse cost materially matters

## Forbidden roulette law

do not let one feature family use:

- HTML on Monday
- JSON on Tuesday
- FlatBuffers on Wednesday

without a named reason tied to ownership.
random protocol roulette is not flexibility.
it is organizational fog.

## Build and repo topology templates

these are examples, not holy scripture.
the point is to show **clean ownership**.

## Default federation topology

```text
repo/
├── apps/
│   ├── desktop-shell/
│   │   ├── electrobun.config.ts
│   │   ├── package.json
│   │   ├── src/
│   │   │   ├── main/                 <- Bun-side Electrobun entrypoints
│   │   │   ├── shell/                <- Solid shell and chrome
│   │   │   ├── interactive/          <- Elm host adapters and mount points
│   │   │   ├── ops/                  <- HTMX shell-hosted route wrappers if any
│   │   │   └── styles/               <- Tailwind entry and tokens
│   └── gateway/
│       ├── src/
│       │   ├── api/                  <- Elysia JSON routes
│       │   ├── hypermedia/           <- Elysia HTML fragment routes for HTMX
│       │   ├── auth/
│       │   ├── policies/
│       │   ├── services/
│       │   └── db/                   <- Drizzle access and migrations
├── services/
│   └── compute/
│       ├── src/
│       │   ├── handlers/             <- Drogon endpoints
│       │   ├── jobs/
│       │   ├── streaming/
│       │   └── adapters/             <- thin wrappers around shared C++ core
├── packages/
│   ├── elm-engine/
│   │   └── src/
│   ├── shared-core/
│   │   ├── CMakeLists.txt
│   │   ├── include/
│   │   ├── src/
│   │   ├── bindings/
│   │   ├── wasm/
│   │   └── tests/
│   ├── schemas/
│   │   ├── flatbuffers/
│   │   └── generated/
│   ├── shaders/
│   │   ├── slang/
│   │   └── generated/
│   └── design-system/
│       └── tailwind/
└── infra/
    ├── postgres/
    ├── turso/
    └── release/
```

## Hypermedia-first topology

```text
repo/
├── apps/
│   ├── desktop-shell/                <- thin Solid shell around mostly HTMX routes
│   └── gateway/
│       ├── src/
│       │   ├── hypermedia/           <- dominant surface layer
│       │   ├── partials/
│       │   ├── forms/
│       │   ├── reports/
│       │   └── admin/
├── services/
│   └── compute/
├── packages/
│   ├── shared-core/
│   ├── shaders/
│   └── design-system/
```

## Local-first workstation topology

```text
repo/
├── apps/
│   └── desktop-shell/
│       ├── src/
│       │   ├── local-db/             <- Turso sync wrappers and policies
│       │   ├── sync/                 <- explicit push/pull orchestration
│       │   ├── shell/
│       │   ├── interactive/
│       │   └── views/
├── apps/gateway/
├── services/compute/
├── packages/shared-core/
└── packages/schemas/
```

## Staged adoption path (how to grow into the full stack without becoming cursed)

one of the nicest things about this stack is that you do **not** need to boot all
lanes at maximum power on day one.

### Stage 0: the lean viable core

start with:

- Bun
- Elysia
- Solid
- Tailwind
- PostgreSQL
- Electrobun if desktop is required now

skip for now:

- Elm
- HTMX
- Drogon
- Turso Sync
- FlatBuffers
- Slang / WebGPU
- Wasm

### Stage 1: add HTMX where HTML is honestly better

add HTMX when:

- forms or reports start multiplying
- admin or ops surfaces deserve server-authored HTML
- the shell does not need to own everything

### Stage 2: add Elm for one feature that truly deserves TEA

add Elm when:

- one feature is getting gnarly state transitions
- replayability, determinism, or correctness matters a lot
- you can give it a real island

### Stage 3: extract shared C++ core

add C++ when:

- a real hot path exists
- logic duplication across languages is becoming dangerous
- performance or portability justify one compiled core

### Stage 4: compile the core to Wasm

add Emscripten when:

- that core needs to run in browser or portable shell contexts too
- keeping one implementation is more valuable than maintaining sibling rewrites

### Stage 5: extract Drogon compute service

add Drogon when:

- in-process boundaries (including Bun FFI) have been proven insufficient for the
  current workload and lifecycle needs
- compute workloads deserve service isolation
- long-running jobs, async streaming, or native throughput become real concerns
- independent scaling, multi-caller access, or service-level lifecycle controls
  are required

### Stage 6: add Turso Sync for local-first workflows

add Turso when:

- offline matters
- local latency matters
- device-local durability matters
- you can explain conflict policy in a paragraph

### Stage 7: add FlatBuffers to the hot path

add FlatBuffers when:

- parse cost, memory layout, or payload volume prove it worth the complexity

### Stage 8: add Slang and WebGPU

add GPU lane when:

- rendering or compute really needs it
- the product is visibly limited without it
- you can own the fallback and capability story

### Growth law

only add the next lane when its **reason** is stronger than its **romance**.

## Decision checklists before adding or promoting a lane

## Before adding Elm

- [ ] what exact feature surface will Elm own?
- [ ] why is Solid not sufficient there?
- [ ] can the boundary be coarse?
- [ ] are ports enough for the required interop?
- [ ] does the feature actually benefit from TEA discipline?
- [ ] are we prepared to keep HTMX out of this surface?

## Before adding HTMX territory

- [ ] is the route family form-heavy, report-heavy, admin-heavy, or
      document-centric?
- [ ] do we want server-authored HTML here?
- [ ] can we serve full pages for pushed URLs?
- [ ] have we planned `HX-Request` caching variation?
- [ ] is this territory named, not vibes-based?

## Before adding Drogon

- [ ] is there meaningful native compute or throughput value?
- [ ] why is Bun FFI or an in-process native bridge insufficient here?
- [ ] why is a supervised local process boundary insufficient here?
- [ ] why is a queue-backed worker boundary insufficient here?
- [ ] are long-running tasks a first-class concern?
- [ ] do we need streaming or coroutine-friendly native services?
- [ ] do we need an independent process lifecycle or scaling profile?
- [ ] will more than one caller depend on this service boundary?
- [ ] would Elysia otherwise become a compute monolith?
- [ ] do we know whether Drogon is internal or public?

## Before adding Turso Sync

- [ ] does offline use materially matter?
- [ ] do local writes need to survive disconnection?
- [ ] is last-push-wins acceptable for the affected entities?
- [ ] who owns conflict resolution?
- [ ] what gets synced and what stays device-local?
- [ ] what is the bootstrap policy on first launch?

## Before adding FlatBuffers

- [ ] what is the measured pain with JSON here?
- [ ] is this boundary actually hot?
- [ ] who versions the schema?
- [ ] who translates between binary and public shapes?
- [ ] can developers still debug the system sanely?

## Before compiling to Wasm

- [ ] is there a genuine shared C++ core?
- [ ] can we keep the host wrapper thin?
- [ ] are main loop and file system differences understood?
- [ ] is the boundary coarse enough?
- [ ] are we avoiding duplicate implementations?

## Before adding WebGPU or Slang

- [ ] is there a real rendering or compute bottleneck?
- [ ] do we want one shader source across targets?
- [ ] is there a fallback story?
- [ ] is the shader module structure intentional?
- [ ] have we kept business logic out of the GPU lane?

## Before enabling CEF in Electrobun

- [ ] what actual system webview limitation is hurting us?
- [ ] is it a temporary platform bug or a product requirement?
- [ ] is the added binary weight justified?
- [ ] are we willing to own that distribution and update cost?

## Architecture review answer format for this stack

when responding to architecture questions in this stack, structure the answer in
this order:

1. **Blunt verdict**
   - coherent
   - coherent but high-discipline
   - salvageable
   - overbuilt
   - fake coherence
2. **Role map**
   - map every named technology to a lane
3. **Default lane**
   - where normal new work goes
4. **Exception lanes**
   - what is special and why
5. **Ownership conflicts**
   - duplicate primaries
   - duplicate truths
   - duplicate UI sovereignty
6. **Boundary risks**
   - where the laws are likely to fail first
7. **Recommended architecture variant**
   - default federation
   - hypermedia-first
   - Elm-centric
   - compute-first
   - local-first
   - GPU-first
8. **Constitutional laws**
   - the exact rules the team must enforce

## Product-shape recommendation matrix

## If the product is a desktop productivity workbench

prefer:

- **default federation**

because:

- Electrobun shell matters
- Solid shell matters
- HTMX probably helps for settings and admin-ish surfaces
- Elm can be bounded to one complex feature
- C++ core can grow only where justified

## If the product is mostly forms, queues, approvals, reports, and ops

prefer:

- **hypermedia-first operations architecture**

because:

- HTML-first and server-authored routes will likely beat SPA ceremony
- the shell can stay thin and useful
- HTMX gets to do the thing it is actually good at

## If the product is a planner, editor, simulator cockpit, or workflow engine

prefer:

- **Elm-centric deterministic architecture**

because:

- deep state transitions are the product
- TEA discipline is worth the boundary cost

## If the product is a native compute system with clients around it

prefer:

- **compute-first native platform architecture**

because:

- C++ and Drogon are closer to the value center than TS composition

## If the product must thrive offline and near the device

prefer:

- **local-first synced workstation architecture**

because:

- Turso's explicit sync model and Electrobun's desktop form factor combine well

## If the product is primarily visual, shader-heavy, or GPU-accelerated

prefer:

- **GPU-first visualization workbench architecture**

because:

- Slang and WebGPU become genuine first-class citizens instead of decoration

## Anti-pattern catalog (call these out aggressively)

## 1. The triple-frontend custody battle

symptoms:

- Solid owns layout
- Elm owns some state
- HTMX owns some fragments
- nobody can say who owns a full route

verdict:

this is not pluralism.
this is court-ordered visitation.

## 2. Elysia as the everything bagel

symptoms:

- auth
- HTML rendering
- JSON rendering
- job orchestration
- compute logic
- persistence policy
- reporting
- half the domain

verdict:

that is not a gateway anymore.
that is a monolith in streetwear.

## 3. Drogon the accidental public backend

symptoms:

- clients talk to it directly for convenience
- API shapes leak from compute to UI
- Elysia still pretends to be the edge

verdict:

pick a sovereign.

## 4. HTMX the junk drawer

symptoms:

- used for whatever Solid or Elm did not get around to
- no named route territory
- random fragments embedded in stateful surfaces

verdict:

this is not a niche lane.
this is denial with attributes.

## 5. Elm the ceremonial purity island

symptoms:

- tiny territory
- tons of ports
- constant JS escape hatches
- no feature-level reason for TEA

verdict:

you are paying the boundary cost without getting Elm's gift.

## 6. Turso the shadow monarch

symptoms:

- local store treated as practical truth
- no conflict policy
- sync timing is a rumor
- Postgres still called canonical but nobody acts like it

verdict:

distributed systems pain is loading.

## 7. FlatBuffers on the public edge

symptoms:

- product APIs are binary because performance vibes
- ordinary screens require custom payload tooling
- no human-readable contract at the edge

verdict:

over-optimization cosplay.

## 8. Shared core by fan fiction

symptoms:

- C++ native version
- C++ Wasm version
- TypeScript fallback version
- all are "roughly aligned"

verdict:

that is not one core.
that is three jobs and one lie.

## 9. Slang or WebGPU as premature religion

symptoms:

- added before the bottleneck is clear
- no fallback story
- no module strategy
- GPU lane starts dictating unrelated architecture

verdict:

cool technology, wrong moment.

## 10. CMake demoted to shell script intern

symptoms:

- native build truth hidden in package.json or ad hoc scripts
- no reproducible native graph
- Wasm and native flags drift independently

verdict:

let the build system be the build system.

## Security laws for this stack

## Public contract security

- auth policy should be centralized in Elysia by default
- public error semantics should be deliberate
- do not let compute-internal details leak directly to product clients

## HTMX security

- escape untrusted HTML
- use `hx-disable` around risky injected raw content if needed
- configure same-origin request policy appropriately
- remember CSRF headers or form strategies on server-rendered flows
- do not let `HX-Request` shape variation break caches or history semantics

## Electrobun security

- code signing and notarization are part of trust, not optional flavor text, when
  shipping real desktop builds
- keep secrets out of bundled client assets
- treat updater artifacts as part of supply-chain hygiene

## Turso security

- tokens are secrets
- local-first does not mean careless credentials
- device-local databases may still require at-rest protections depending on the
  domain

## Postgres security

- canonical truth deserves proper role and policy design
- if RLS is used, keep its ownership clear and tested

## Wasm and native security

- a compiled core is not automatically safer because it is compiled
- validate boundaries
- keep binary schema and memory assumptions explicit

## Observability laws

## Elysia observability

- exploit built-in OpenTelemetry support when appropriate
- log contract-level events and policy decisions

## HTMX observability

- for debugging, HTMX's event model is first-class
- htmx logging and event hooks are part of normal troubleshooting, not shameful
  rituals

## Turso observability

- track push and pull timings
- watch WAL sizes and sync failures
- expose sync health to the shell when user trust depends on it

## Electrobun observability

- remember dev launcher output and native event visibility in development
- update hashes and artifact behavior are observable architecture, not just build
  trivia

## Drogon observability

- long-running jobs must expose progress and failure clearly
- internal compute APIs need metrics and structured logs

## GPU observability

- shader compilation failures and capability mismatch need first-class reporting
- don't make the GPU lane a silent black box

## Testing and verification laws

## Shell and route tests

- Solid shell behavior should be tested at route and embedding boundaries
- HTMX fragments should be tested as fragment and full-page responses where
  history is involved

## Interaction engine tests

- Elm features deserve state-transition tests and deterministic scenario coverage

## Public contract tests

- Elysia contracts should be verified at the public boundary
- OpenAPI generation and type expectations should be treated as contract assets

## Compute tests

- C++ core gets unit tests and property-heavy tests where warranted
- Drogon service wrappers get integration tests around streaming, concurrency, and
  failure behavior

## Sync tests

- Turso flows need offline, push, pull, conflict, and restart scenarios
- if local-first matters, test it like it matters

## Binary schema tests

- FlatBuffers schema evolution requires compatibility checks
- do not trust binary boundaries by vibes

## Shader tests

- compile shaders for actual targets in CI
- a shader that only exists in the editor is fan fiction

## Performance laws

## Optimize the right lane

- HTML and JSON edges optimize for clarity first
- FlatBuffers optimize for hot internal transport
- C++ optimizes for compute correctness and speed
- WebGPU optimizes where the GPU is truly the right execution surface
- Turso optimizes local latency and resilience
- Electrobun optimizes shell startup, packaging, and update weight

## The no-performance-talisman rule

nobody gets to say "performance" and skip the architecture argument.
name:

- the workload
- the bottleneck
- the hot boundary
- the winning metric
- the fallback

or do not make the stack weirder.

## How to decide whether the default architecture should be used

use the default federation when most of the following are true:

- the product is desktop-shell friendly
- there is at least one deep interactive feature, but not enough to make Elm the
  whole product
- there are some admin, settings, or ops surfaces that HTMX would simplify
- Elysia provides clear product-edge value
- native compute exists or is likely to matter
- offline or local-first needs exist but do not dominate everything
- GPU work is important or plausible but not the center of all architecture

avoid the default federation when most of the following are true:

- almost every meaningful route is server-authored and hypermedia-first
- almost every meaningful product surface is an Elm-worthy interaction engine
- nearly all product complexity lives in native compute and Elysia adds little
- local-first semantics dominate product design more than public-contract shape
- the GPU lane is the true heart of the product

## The keep / bounded / dormant framework

when reviewing a project on this stack, classify components like this:

### Keep primary

- clearly owns a first-class lane
- delivers unique value
- no duplicate sovereignty

### Keep bounded

- useful in a specialized territory
- justified but not dominant
- requires explicit borders

### Keep dormant

- strategic future lane
- no current sovereignty
- present in build or package choice, but not in current architecture center

### Demote

- currently duplicating another lane
- role too fuzzy
- better kept available than active

### Remove or postpone

- all romance, no jurisdiction
- no real workload
- only there because it would be cool someday

## Example verdicts the agent should be willing to give

### "This is coherent."

say this when:

- the lane map is crisp
- the default path is obvious
- special cases are named
- the truth story is sane

### "This is coherent but high-discipline."

say this when:

- the stack is large
- the arrangement is defensible
- but laws must be actively enforced or it will drift

### "This is salvageable."

say this when:

- there are good bones
- but ownership, truth, or route territory are muddy

### "This is overbuilt."

say this when:

- multiple components duplicate primacy
- too much boundary cost exists without sufficient payoff

### "This has fake coherence."

say this when:

- the diagram looks nice
- the prose sounds smart
- but nobody can actually say where new work goes or who owns what

## The final constitutional checklist

before blessing an architecture on this stack, check all of these:

- [ ] is there one obvious default lane for normal new work?
- [ ] are alternative lanes named and justified?
- [ ] does every major concern have one owner?
- [ ] is the shell clearly owned?
- [ ] is the interaction engine clearly bounded?
- [ ] is HTMX territory named?
- [ ] does one layer own the public contract?
- [ ] is Drogon internal by default or explicitly public?
- [ ] is PostgreSQL canonical for the right entities?
- [ ] is Turso scoped and sync-explicit?
- [ ] is the shared core truly shared?
- [ ] do Wasm and native targets derive from one source of truth?
- [ ] are FlatBuffers limited to boundaries where they pay rent?
- [ ] is Slang the shader truth if a shader lane exists?
- [ ] is WGSL treated as target output, not accidental authoring canon?
- [ ] does CMake own native build truth?
- [ ] does Bun own TS build truth?
- [ ] can a new engineer tell where a new feature belongs?
- [ ] can a reviewer tell where the first architecture breach will happen?

if several boxes are unchecked, do not hand out approval just because the stack
is interesting.

## Extended appendices (because real stacks need field manuals, not just vibes)

the earlier sections establish the constitution.
these appendices answer the messier question:

> when a real feature request lands, where the heck does it actually go?

this is the part people usually try to improvise.
improvisation is how mega-stacks become folklore-driven.

## Feature placement atlas

this section is intentionally blunt.
if a new piece of work arrives, use these tables before inventing a fourth owner.

## Route and UI placement matrix

| Work item | Default owner | Escalate to | Keep away from | Why |
| --- | --- | --- | --- | --- |
| app chrome | Solid + Electrobun | none | HTMX, Elm, Drogon | this is literally shell territory |
| window menus and tray | Electrobun | none | Solid-only abstractions, Elm | desktop shell concern |
| theme switcher | Solid + Tailwind | HTMX if settings page is server-authored | Drogon, C++ | cross-cutting shell state |
| account settings page | HTMX + Elysia HTML | Solid if rich client behavior grows | Elm, Drogon | classic form and settings territory |
| admin queue page | HTMX + Elysia HTML | Solid shell wrapper | Elm | server-authored lists and forms are ideal here |
| report viewer | HTMX + Elysia HTML | Solid if charts become rich | Elm by default | document and report surfaces love hypermedia |
| notification center | Solid | HTMX for admin-rendered notification templates if needed | Elm | shell concern with transient state |
| onboarding flow | Solid by default | Elm if transitions become correctness-sensitive | HTMX if it becomes state-heavy | shell-adjacent, but can become a state machine |
| billing screen | HTMX + Elysia | Solid shell wrapper | Drogon direct, FlatBuffers | public edge, forms, policy, human-readable contract |
| profile page | HTMX or Solid | none | Drogon, Wasm | not a compute lane problem |
| desktop preferences dialog | Solid or HTMX | none | Elm unless genuinely state-machine-heavy | local UX or server-authored form work |
| import wizard | Solid | Elm if import states are complex and error-rich | HTMX fragments inside the core wizard | shell-hosted workflow that may justify TEA |
| export dialog | Solid | C++ core for actual export logic | HTMX route ownership conflict | shell modal with delegated heavy work |
| sync status center | Solid shell | HTMX detail pages for history or logs | Elm unless conflict resolution is deep | shell concern plus local-first insight |
| sync conflict resolution screen | Elm or Solid | HTMX for review pages if mostly document-like | random ad hoc JS | this can become a real interaction engine |
| admin audit log | HTMX + Elysia HTML | Solid shell framing | Elm | paged, filterable, server-authored list territory |
| interactive graph editor | Elm + WebGPU or Solid + WebGPU | C++ core if algorithmic model is shared | HTMX | this is not a fragment job |
| simulation control panel | Elm | Solid shell host | HTMX | deterministic bounded interaction territory |
| model browser | Solid | HTMX if it becomes mostly document navigation | Elm by default | browse and preview UI fits shell-side reactivity |
| document review workflow | HTMX or Elm depending state depth | Solid shell wrapper | raw FlatBuffers | if transitions matter deeply, Elm; otherwise HTMX |
| command palette | Solid + Electrobun | C++ core for ranking or search if hot | HTMX | shell-native interaction |
| feature flags console | HTMX + Elysia HTML | Solid shell wrapper | Drogon | admin and ops territory |
| internal support dashboard | HTMX + Elysia HTML | Solid charts or widgets as bounded islands | Elm as default | server-authored operations territory |
| offline drafts browser | Solid + Turso | HTMX for listing if mostly document-like | Postgres direct-only mental model | local-first user-side concern |
| job progress page | Solid shell + Elysia stream | HTMX for simple server-authored progress | Elm if the UI becomes a workflow engine | cross-cutting shell + compute coordination |
| shader inspector | Solid + WebGPU | Elm if it becomes deterministic tool state | HTMX | technical workstation surface, not hypermedia |
| log console | Solid | HTMX if mostly server-rendered pages | Elm | shell or tooling view |
| diagnostics page | HTMX or Solid | none | FlatBuffers public edge | human-readable ops surface |
| help docs page | HTMX | Solid shell wrapper | Elm, Drogon | document-oriented territory |
| collaborative permissions matrix | HTMX or Elm depending complexity | Solid shell wrapper | Turso-only truth | if edits are complex and correctness-heavy, Elm |
| review and approval queue | HTMX | Elm when transitions are deep and branched | Drogon | ideal hypermedia territory unless workflow logic explodes |
| file diff viewer | Solid | C++ core for diff computation | HTMX for the diff surface itself if very interactive | rendering-heavy client-side feature |
| local workspace chooser | Solid + Electrobun | Turso for backing data | HTMX by default | desktop shell and local state concern |
| search results page | HTMX or Solid | C++ or Drogon for heavy ranking logic | Elm by default | depends on interaction depth |
| visual node editor | Elm or Solid + WebGPU | C++ core for compute | HTMX | stateful visual tool, not hypermedia |
| simple CRUD table | HTMX | Solid only if local-only client interaction dominates | Elm | don't over-architect boring work |
| file upload form | HTMX + Elysia HTML | Solid if UX gets highly custom | Drogon public direct | form-heavy and server-mediated by default |
| background task launcher | HTMX or Solid | queue-backed worker or Drogon executes actual work | Elm only if the launcher itself is a workflow engine | human-readable edge over native compute |
| status badge in shell | Solid | none | HTMX, Elm | this is shell ambient state |

## Service and compute placement matrix

| Work item | Default owner | Secondary helper | Do not default to | Why |
| --- | --- | --- | --- | --- |
| login and session issuance | Elysia | PostgreSQL | Drogon | public contract and auth edge |
| role and policy checks | Elysia + PostgreSQL | Drizzle | Turso-only, Drogon-only | product edge policy should stay coherent |
| HTML fragment rendering | Elysia | HTMX | Drogon | public hypermedia lane |
| JSON API composition | Elysia | Drizzle, Postgres | Drogon direct | public contract layer territory |
| route validation | Elysia | schema definitions | C++ core | official Elysia strength |
| OpenAPI generation | Elysia | none | Drogon | Elysia is built for this |
| typed TS client contract | Elysia | Eden or Treaty | hand-maintained native shapes | keep product edge honest |
| simple DB-backed CRUD | Elysia + Drizzle | PostgreSQL | Drogon | don't use native compute for basic app semantics |
| report generation with trivial SQL | Elysia + Drizzle | HTMX | Drogon | no need to promote compute too early |
| heavy report generation | C++ core + selected boundary | Elysia shapes the output contract; Drogon if service extraction is warranted | HTMX direct to native | compute lane earns itself here |
| long-running simulation | C++ core + selected boundary | Elysia as public coordinator; queue-backed worker or Drogon when process/service isolation matters | Elysia-only implementation | classic compute-engine job |
| high-volume transform pipeline | C++ core + selected boundary | FlatBuffers if hot; queue-backed worker or Drogon when service lifecycle is required | Elysia monolith | compute-specific throughput concern |
| import parse and normalize small payload | Elysia | C++ core if shared parsing exists | Drogon by default | keep simple work simple |
| import parse and normalize huge binary model | C++ core + Drogon | FlatBuffers or native formats | Elysia-only path | heavy native work |
| progress streaming | Drogon or Elysia depending owner | Solid shell renders status | HTMX polling without reason if streaming exists | use the service that owns the work |
| websocket push for public clients | Elysia by default | Drogon underneath if needed | direct compute exposure | edge ownership still matters |
| internal native admin endpoint | Drogon or supervised local process | C++ core | public clients directly | bounded internal territory |
| local utility script with DB access | Bun + Drizzle | Postgres or Turso | Drogon | utility work belongs in the TS lane |
| full-text search ranking | C++ core or Postgres depending complexity | Elysia shapes response | Solid client ranking by default | put ranking where the real complexity is |
| file diff algorithm | C++ core | Elysia or shell host | HTMX | shareable algorithmic core candidate |
| image or model processing | C++ core + Drogon | Wasm for client preview | Elysia-only processing if hot | classic native lane value |
| compute result explanation for product UI | Elysia | Drogon as source | raw native response to clients | public contract and UX semantics stay at the edge |

## Data ownership matrix

| Data kind | Canonical owner | Local or secondary owner | Forbidden default assumption | Notes |
| --- | --- | --- | --- | --- |
| users | PostgreSQL | Turso cached subset if needed | Turso as system-of-record | multi-user durable truth |
| organizations or teams | PostgreSQL | none or read replicas | Turso authority | relational shared truth |
| permissions and roles | PostgreSQL | local cache only | device-local authority | policy-critical data |
| billing records | PostgreSQL | none | local-first write truth | canonical and auditable |
| user profile cache | PostgreSQL | Turso local projection | Turso canonical | projection is okay, truth stays central |
| local draft document | Turso or local file + Turso metadata | PostgreSQL eventual publish target | Postgres required for every keystroke | local-first territory |
| published collaborative document | PostgreSQL | Turso local working copy | Turso canonical without merge policy | shared durable object |
| sync health stats | Turso local stats + shell state | optional server aggregation | Postgres-only visibility | user trust depends on local visibility |
| app settings global | PostgreSQL if cross-device | Turso local mirror | one unnamed truth | decide per scope |
| app settings device-local | Turso or local config | optional cloud backup | PostgreSQL-only semantics | device concern |
| job definitions | PostgreSQL | Turso local queue cache if needed | Turso primary for shared jobs | collaborative system state |
| job progress ephemeral local view | Turso or shell memory | PostgreSQL or Elysia stream as source | Postgres round-trip for every paint | local UX concern |
| audit log | PostgreSQL | local cached window | Turso canonical | server truth |
| recent activity cache | Turso | PostgreSQL source | canonical local activity | fast local read model |
| feature flags | PostgreSQL | Turso cached subset | per-device truth by accident | policy-ish shared state |
| large model asset metadata | PostgreSQL | Turso local cache | local file = authority | metadata is canonical even if assets are local |
| local workspace catalog | Turso | optional remote sync | Postgres-only if purely device-local | workstation concern |
| search index shards | depends on architecture | Turso local index or native index | Postgres as the only performance answer | this is derived data |
| shader cache | local filesystem or Turso metadata | optional remote invalidation info | PostgreSQL as shader cache truth | build/runtime artifact territory |
| compiled Wasm artifact manifest | release pipeline storage | local cache | app DB tables as artifact truth | deployment artifact concern |
| Electrobun version manifest | release static host | local version.json | Postgres business DB | updater architecture, not domain DB |

## Transport and representation matrix

| Boundary | Preferred format | Upgrade to | Avoid | Why |
| --- | --- | --- | --- | --- |
| browser or shell route to Elysia HTMX surface | HTML | SSE or websocket extension for live fragments if truly needed | FlatBuffers | HTMX is HTML-first |
| Solid or Elm app to Elysia | JSON | stream or websocket as required | FlatBuffers by default | product edge clarity |
| Elysia to public docs tooling | OpenAPI + JSON schema story | generated TS types | native-only undocumented shapes | contract stewardship |
| Elysia to Drogon internal call | JSON by default | FlatBuffers if the path is hot or payload-heavy | raw ad hoc strings | keep simple things debuggable |
| Drogon to C++ core | native in-process calls | shared structs or FlatBuffers where needed | JSON if avoidable in hottest loops | internal native lane |
| Solid host to Wasm core | coarse typed bindings | FlatBuffers if payloads are large | tiny chatty getter calls | Wasm bridge cost matters |
| Wasm core to GPU prep | structured binary layout | FlatBuffers or direct typed buffer layout | hand-managed string protocols | this is performance-adjacent |
| Slang authoring to web target | Slang source -> WGSL output | capability-conditioned variants | dual-maintained raw WGSL and raw HLSL | one shader truth |
| updater static host to desktop client | Electrobun patch files and manifests | compressed full bundle fallback | business API route piggybacking | updater has its own architecture |

## Ownership-by-concern atlas

the following concerns often get smeared across layers in stack-heavy projects.
do not smear them.

### Authentication

- default owner: **Elysia**
- canonical data: **PostgreSQL**
- local cache: **Turso** only as projection where justified
- forbidden default: **Drogon** as separate auth universe

### Authorization and policy checks

- default owner: **Elysia** at the product edge
- canonical rules data: **PostgreSQL**
- native enforcement mirror: **Drogon** only when internal compute actions need
  policy verification and the contract is explicit

### Route ownership

- shell routes: **Solid + Electrobun**
- bounded interaction routes: **Solid host + Elm engine**
- hypermedia routes: **HTMX + Elysia HTML**
- public API routes: **Elysia**

### Background jobs

- public initiation: **Elysia**
- durable coordination: **PostgreSQL**
- heavy execution: **C++ core + selected boundary (Drogon when warranted)**
- local optimistic display: **Solid + Turso local state**

### Offline queueing

- local queue storage: **Turso**
- user-visible queue UX: **Solid shell**
- reconciliation: **Elysia** and server truth on reconnect

### Search and ranking

- shell results presentation: **Solid** or **HTMX** depending route family
- ranking implementation: **PostgreSQL**, **C++**, or **Drogon**, depending the
  true complexity

### Import and export

- UI flow: **Solid**, or **Elm** if workflow-heavy
- local file affordances: **Electrobun**
- heavy parsing or transforms: **C++ core**
- public status and progress: **Elysia** or **Drogon** depending owner

### Rendering and visualization

- shell and surrounding controls: **Solid**
- deterministic tool state if complex: **Elm**
- GPU shaders: **Slang**
- GPU execution: **WebGPU**
- numeric or layout-heavy precomputation: **C++ core**

### Schema evolution

- TS database schema: **Drizzle**
- canonical relational meaning: **PostgreSQL**
- internal binary schema: **FlatBuffers**
- shader module interfaces: **Slang**
- shared core ABI or bindings: **C++ core + CMake + Wasm bridge policy**

## Concrete scenario guide (40 common "where does this go?" calls)

### 1. "We need a settings screen."

- default answer: **HTMX + Elysia HTML**
- move to Solid only if:
  - it needs rich local-only shell behavior
  - it is part of the app chrome experience
- move to Elm only if:
  - it becomes a correctness-heavy state machine
- do not send this to Drogon

### 2. "We need a complex wizard with branching validation and undo."

- default answer: **Elm**
- host it in the Solid shell
- keep server calls through Elysia
- keep HTMX out unless separate supporting pages exist

### 3. "We need a boring admin CRUD list."

- default answer: **HTMX**
- Elysia serves fragments and pages
- Drizzle and Postgres back it
- do not reach for Elm because boredom is not a state machine

### 4. "We need a big batch transform pipeline."

- default answer: **C++ core + selected boundary**
- Elysia may start the job and shape public responses
- use FlatBuffers only if the boundary proves hot enough

### 5. "We need local drafts that survive offline."

- default answer: **Turso local-first**
- publish or sync through Elysia when connected
- keep canonical published truth in Postgres

### 6. "We need a lightweight profile page."

- default answer: **HTMX or Solid**
- pick HTMX if mostly forms and server-rendered details
- pick Solid if it sits naturally in shell navigation and client-side state
- do not over-promote this into Elm

### 7. "We need a node-graph editor."

- default answer: **Elm or Solid + WebGPU** depending state discipline needs
- use C++ core for heavy graph analysis if needed
- do not use HTMX for the interactive graph surface

### 8. "We need a report export button."

- default answer:
  - button UI in HTMX or Solid depending page owner
  - heavy export in C++ core or Drogon if justified
  - contract initiation in Elysia

### 9. "We need shell-wide connectivity and sync badges."

- default answer: **Solid shell**
- source status may come from Turso stats and Elysia health
- keep this out of HTMX route ownership

### 10. "We need live progress updates for a long-running native task."

- default answer:
  - task owner: **queue-backed worker or supervised process**
  - public contract owner: **Elysia** unless a compute-first architecture says
    otherwise
  - UI host: **Solid shell**
  - **Drogon** only when independent scaling, multi-caller integration, or a
    service lifecycle is actually earned

### 11. "We need one small fancy widget on an otherwise boring admin page."

- default answer: **HTMX page + bounded client island**
- the island can be Solid or a tiny JS helper
- do not let the one widget change page ownership

### 12. "We need a deterministic review workflow with 12 states."

- default answer: **Elm** if this is the center of the product value
- otherwise HTMX may still work if state depth is lower than it sounds

### 13. "We need to parse and preview huge files in the client."

- default answer: **C++ core + Wasm** for heavy parsing
- shell UI in Solid
- keep preview contract coarse

### 14. "We need to compile or inspect shaders in-app."

- default answer: **Slang-centered tooling path**
- present it in Solid shell
- use WebGPU where runtime preview matters

### 15. "We need a lightweight public JSON API for a mobile or web client."

- default answer: **Elysia**
- if compute-heavy, Elysia delegates to Drogon
- keep the public contract legible

### 16. "We need a machine-generated internal payload between native and Wasm."

- default answer: **FlatBuffers** if the path is hot enough
- otherwise plain structured boundary is fine

### 17. "We need a desktop-only local library browser with thumbnails and notes."

- default answer: **Solid + Electrobun + Turso**
- sync to server later if needed

### 18. "We need a fast text search over huge local content."

- default answer: local-first architecture
- UI in Solid
- index in Turso, native code, or both depending scale
- authoritative publish state still in Postgres if collaborative

### 19. "We need a metrics dashboard for internal ops."

- default answer: **HTMX + Elysia HTML**
- bounded client charts are okay inside that route family

### 20. "We need one route to act like a rich mini-application."

- default answer: **Elm island inside Solid shell**
- unless it is clearly a hypermedia report or forms page

### 21. "We need a login or account recovery flow."

- default answer: **Elysia + HTMX or Solid**
- this is public contract and product edge work, not compute-engine turf

### 22. "We need file drag-and-drop with immediate native affordances."

- default answer: **Electrobun shell + Solid UI**
- heavy processing can drop to C++ core or Drogon later

### 23. "We need to sync local edits later when online."

- default answer: **Turso push or pull orchestration**
- expose visible sync health in the shell

### 24. "We need an approvals queue with comments and side-by-side diffing."

- default answer: **HTMX page with Solid diff island**
- promote to Elm only if the internal transition logic gets truly gnarly

### 25. "We need durable collaborative permissions around shared assets."

- default answer: **PostgreSQL truth + Elysia policy edge**
- local mirrors are allowed, local sovereignty is not

### 26. "We need a shader-based preview canvas embedded in desktop UI."

- default answer: **Solid shell + WebGPU + Slang-generated shader path**
- keep tool state in Solid or Elm based on complexity

### 27. "We need a job retry and cancellation console."

- default answer: **HTMX or Solid UI**
- actual job control semantics remain Elysia + Drogon territory

### 28. "We need inline validation with friendly UX on a form."

- default answer: **HTMX + Elysia**
- use client-side affordances for comfort
- keep server validation authoritative

### 29. "We need local notes attached to shared objects."

- default answer: **Turso local state** if the notes are device-local
- **PostgreSQL** if they are shared collaboration artifacts
- decide on purpose, not later

### 30. "We need a reviewable audit trail of sync conflicts."

- default answer:
  - canonical record: **PostgreSQL**
  - local event visibility: **Turso stats or local history**
  - UI: **HTMX** or **Solid** depending route family

### 31. "We need a command-line maintenance tool."

- default answer: **Bun + Drizzle** for TS-side ops
- **C++ utility** only if it genuinely sits closer to shared-core behavior

### 32. "We need a portable compute preview in browser and desktop."

- default answer: **C++ shared core -> Emscripten/Wasm**
- shell or browser UI chooses how to display results

### 33. "We need a tiny binary patch update system."

- default answer: **Electrobun updater**
- do not invent your own updater just because infra engineers got bored

### 34. "We need a big static or semi-static documentation viewer inside the app."

- default answer: **HTMX** if dynamic but server-authored
- **Solid** if fully client-embedded and tightly shell-integrated

### 35. "We need role-aware HTML fragments."

- default answer: **Elysia hypermedia routes**
- this is product edge policy plus fragment shaping

### 36. "We need exportable binary model files for heavy scenes."

- default answer: **C++ core** for structure generation
- **FlatBuffers** if the format and workflow justify it
- not JSON if the volume is absurd

### 37. "We need a live status board for active compute sessions."

- default answer: **Solid shell or HTMX route depending audience**
- backend owner: **Elysia** or **Drogon** based on public vs internal audience

### 38. "We need a one-off support tool with lots of tables and actions."

- default answer: **HTMX**
- do not waste a perfect hypermedia use-case on SPA ceremony

### 39. "We need a polished desktop-first multi-panel workbench."

- default answer: **default federation**
- Solid shell
- optional Elm islands
- HTMX ops routes
- native compute behind Elysia

### 40. "We need a purely local technical tool that may sync later."

- default answer: **Electrobun + Solid + Turso**, with Postgres and Elysia added
  only when cloud truth becomes product-relevant

## Product archetype playbooks

these are example stack shapes that recur a lot.

## Archetype A: scientific visualization workbench

### Recommended variant

- **GPU-first visualization workbench**

### Core lane map

- shell: Electrobun + Solid
- styling: Tailwind
- interaction core: Elm only if tooling state becomes deeply deterministic
- public edge: Elysia
- heavy compute: C++ core + selected boundary (Drogon when service extraction is
  warranted)
- shared math and transforms: C++ core
- local datasets and session state: Turso or local files
- canonical shared project truth: PostgreSQL
- shader truth: Slang
- GPU execution: WebGPU

### Strong reasons to choose it

- GPU work is real, not decorative
- shared native or Wasm core matters
- desktop shell quality matters

### Strong reasons not to choose it

- the app is mostly reports and forms
- the GPU story is speculative
- the team cannot maintain shader and native boundaries responsibly

### Top three anti-patterns

- pushing business policy into shader code
- hand-maintained WGSL divergence from Slang
- bypassing Elysia for public product contract work

## Archetype B: regulated workflow desktop app

### Recommended variant

- **Elm-centric deterministic architecture** or **default federation** depending
  how deep the workflow logic gets

### Core lane map

- shell: Electrobun + Solid
- workflow engine: Elm
- admin and audit views: HTMX
- public contract and auth: Elysia
- truth: PostgreSQL
- local resilience: Turso if offline matters

### Why it fits

- deterministic interaction and validation are product value
- server-authored admin surfaces still make sense

### Watch-outs

- do not let HTMX and Elm share the same workflow body
- keep policy truth centralized at Elysia and Postgres

## Archetype C: internal operations platform with optional desktop shell

### Recommended variant

- **hypermedia-first operations architecture**

### Core lane map

- shell: thin Solid or no heavy shell emphasis
- primary UI: HTMX
- public contract: Elysia
- DB lane: Drizzle + Postgres
- compute sidecar: Drogon only where needed

### Why it fits

- HTMX is perfect for queues, tables, forms, reports, approvals
- Elysia can render HTML and JSON cleanly

### Watch-outs

- do not add Elm unless one route really earns it
- do not let random client islands seize route ownership

## Archetype D: collaborative modeling tool

### Recommended variant

- **default federation**

### Core lane map

- shell: Electrobun + Solid
- editor or planner engine: Elm or Solid depending depth
- heavy model operations: C++ core + selected boundary (Drogon when needed)
- shared truth: PostgreSQL
- local draft and cache: Turso
- binary hot path: FlatBuffers if proven necessary

### Why it fits

- multiple UI modes coexist honestly
- native and local-first concerns are both real

### Watch-outs

- local drafts must not become shadow truth
- shared core duplication will destroy consistency fast

## Archetype E: field data capture tool

### Recommended variant

- **local-first synced workstation architecture**

### Core lane map

- shell: Electrobun + Solid
- local data: Turso
- canonical cloud truth: PostgreSQL
- sync API: Elysia
- heavy media or model processing: C++ core or Drogon as needed

### Why it fits

- local-first is the actual product value
- sync semantics matter more than fashionable runtime choices

### Watch-outs

- last-push-wins may not be enough for some entities
- sync health must be visible to users

## Archetype F: native compute platform with client companions

### Recommended variant

- **compute-first native platform architecture**

### Core lane map

- compute engine: C++ core with explicit boundary choice (often Drogon when
  promoted)
- public edge: Elysia, possibly thinner than default
- desktop client: Electrobun + Solid
- local cache and drafts: Turso if needed
- truth: PostgreSQL

### Why it fits

- native compute is the center of value
- multiple clients may consume the same native service lane

### Watch-outs

- public-contract sovereignty must still be explicit
- don't accidentally run two public backends with overlapping semantics

## Archetype G: creative desktop editor with occasional server sync

### Recommended variant

- **default federation** leaning local-first

### Core lane map

- shell: Electrobun + Solid
- deterministic editor state: Elm if the editor deserves it
- local project storage: Turso and files
- canonical publish state: Postgres
- heavy processing: C++ core
- web preview path: Wasm if needed

### Why it fits

- desktop affordances matter
- local state matters
- shared-core portability matters

### Watch-outs

- do not over-centralize ephemeral editor state in the backend
- do not let the shell own the editor's entire internal truth

## Archetype H: product shell with heavy internal admin console

### Recommended variant

- **default federation** with strong HTMX bounded lane

### Core lane map

- user-facing shell: Solid
- deep feature island(s): optional Elm
- internal staff tooling: HTMX + Elysia HTML
- contract and DB: Elysia + Drizzle + Postgres

### Why it fits

- one stack can serve both a polished shell and server-driven operations tooling

### Watch-outs

- make route ownership obvious
- do not let admin route idioms leak into the interactive product core

## Migration playbooks

use these when the project grows or changes shape instead of pretending the first
architecture guess was eternal.

## Playbook 1: adding HTMX to a Solid-heavy app

### Trigger

- too many forms and ops pages are being implemented with SPA ceremony

### Safe move

1. name HTMX territory explicitly
2. keep the shell in Solid
3. add Elysia fragment routes
4. ensure full-page responses exist for pushed URLs
5. standardize Tailwind tokens across the new route family

### Unsafe move

- sprinkling HTMX fragments into existing client-owned feature bodies without a
  route boundary

## Playbook 2: promoting one feature from Solid to Elm

### Trigger

- one feature becomes state-machine-heavy, bug-prone, or correctness-sensitive

### Safe move

1. isolate the feature surface
2. define the Elm-owned model boundaries
3. keep ports coarse
4. keep server calls going through Elysia
5. remove duplicate state ownership from Solid

### Unsafe move

- embedding Elm while keeping the old Solid store as co-owner

## Playbook 3: extracting Drogon from Elysia compute bloat

### Trigger

- Elysia handlers are now doing serious heavy work

### Safe move

1. identify the compute kernels
2. move them into C++ core where shared value exists
3. expose them through Drogon
4. keep Elysia as public contract owner
5. translate internal errors and progress semantics back at the edge

### Unsafe move

- splitting handlers across Elysia and Drogon by whim rather than by workload

## Playbook 4: introducing local-first state with Turso

### Trigger

- users need to work offline or latency is hurting the product

### Safe move

1. classify which entities can be local-first
2. define canonical ownership in Postgres
3. implement explicit push and pull lifecycle
4. expose sync status in the shell
5. test bootstrap, conflict, reconnect, restart, and WAL behavior

### Unsafe move

- turning on sync and assuming semantics will sort themselves out later

## Playbook 5: unifying duplicate native and web logic into a shared core

### Trigger

- TS and C++ versions of the same logic keep drifting

### Safe move

1. identify the truly shared logic
2. move it into modern C++ core
3. compile native and Wasm targets from the same source
4. define a coarse host boundary
5. delete duplicate sibling logic aggressively

### Unsafe move

- keeping the old duplicate implementations around "just in case"

## Playbook 6: adding FlatBuffers to an already-working JSON path

### Trigger

- profiling proves the boundary is hot enough

### Safe move

1. scope FlatBuffers to the hot internal boundary only
2. create one translation layer
3. keep public JSON or HTML untouched
4. add compatibility tests

### Unsafe move

- converting every contract in sight to binary because one path got hot

## Playbook 7: centralizing shader truth under Slang

### Trigger

- raw shader sources are diverging across targets

### Safe move

1. declare Slang authoring canon
2. define module boundaries
3. generate or validate WGSL as a target output
4. keep capability and fallback policy explicit

### Unsafe move

- keeping hand-edited WGSL and HLSL twins forever

## Playbook 8: reasserting Elysia as public edge after native creep

### Trigger

- clients started consuming compute-native endpoints directly

### Safe move

1. audit client entry points
2. consolidate public contract in Elysia
3. keep Drogon internal unless a conscious public split is wanted
4. normalize auth and error policy at the edge

### Unsafe move

- letting legacy direct clients dictate permanent dual-sovereign architecture by
  inertia

## Pull request review rubric by lane

use these review questions so the stack does not drift one "quick fix" at a
time.

## Shell PRs (Electrobun, Solid, Tailwind)

- did this change stay in shell territory?
- did it accidentally absorb domain rules?
- is Tailwind usage consistent with shared design tokens?
- does a new desktop bridge belong in Electrobun, or is it a one-off shortcut?
- did the PR preserve route or island ownership clarity?

## Elm PRs

- does the feature still clearly justify Elm?
- are ports coarse and intentional?
- did shell state remain outside Elm internals unless explicitly bridged?
- did the PR avoid HTMX or Solid ownership conflicts on the same surface?
- are state transitions still explicit and testable?

## HTMX PRs

- is the route family named territory?
- are full-page responses valid where history or pushed URLs are used?
- did the PR handle `HX-Request` or caching variation correctly?
- is server validation authoritative?
- did the PR avoid embedding fragments into client-owned state zones?

## Elysia PRs

- is this public contract work or compute creep?
- are schema and validation changes explicit?
- does the API shape stay product-friendly instead of reflecting internal quirks?
- if HTMX is involved, are fragment and full-page semantics both handled?
- if Drogon is called, is the boundary still clean and observable?

## Drizzle and Postgres PRs

- is the migration strategy explicit?
- did the change accidentally alter canonical data ownership?
- is this TS-lane access logic, not native-lane theology?
- if RLS or roles are touched, are policy implications reviewed?
- if Turso sync is involved, are conflict implications documented?

## Turso PRs

- what entities are local-first now?
- what is the sync lifecycle?
- what does last-push-wins mean here?
- are stats and checkpoint behavior still considered?
- does the shell surface sync health honestly?

## Drogon and C++ PRs

- is this truly compute or shared-core work?
- could this logic belong in the C++ core rather than Drogon glue?
- is the public contract still owned by Elysia unless consciously changed?
- are concurrency and streaming behaviors observable and testable?
- did we accidentally duplicate logic already present elsewhere?

## Wasm and FlatBuffers PRs

- is the boundary coarse enough?
- is the binary format justified by heat or volume?
- are compatibility tests present?
- did the PR avoid leaking binary complexity to public clients?
- is the shared-core story stronger after this change, or weaker?

## GPU PRs

- is Slang still source truth?
- are WGSL or other target artifacts generated or governed properly?
- are capability restrictions explicit?
- is there a fallback story?
- did the PR keep product logic out of the GPU lane?

## Failure mode catalog (aka how this stack usually betrays careless teams)

## Failure mode 1: shell inflation

### Symptom

- shell components keep gaining domain logic

### Root cause

- Solid or Electrobun is nearby, so people stop respecting deeper owners

### Corrective move

- move domain rules back to Elm, Elysia, or shared core depending the concern

## Failure mode 2: gateway obesity

### Symptom

- Elysia handlers become the de facto domain monolith

### Root cause

- every request passes there, so it becomes the easiest dumping ground

### Corrective move

- separate contract work from compute and shared-core logic again

## Failure mode 3: fake local-first

### Symptom

- the app advertises offline support but sync behavior is mysterious and fragile

### Root cause

- Turso was added as a feature checkbox, not a governed lane

### Corrective move

- define entity ownership, sync triggers, failure UI, and conflict policy

## Failure mode 4: duplicate public backends

### Symptom

- clients hit Elysia and Drogon for overlapping concerns

### Root cause

- compute endpoints escaped into product usage

### Corrective move

- restore Elysia sovereignty or explicitly split the public architecture

## Failure mode 5: fragment civil war

### Symptom

- HTMX and client-owned state keep fighting over the same subtree

### Root cause

- no territory map

### Corrective move

- move to route-scoped ownership or bounded islands

## Failure mode 6: ceremonial Elm

### Symptom

- a lot of ports, not much real Elm value

### Root cause

- feature never really justified Elm ownership

### Corrective move

- either enlarge the territory honestly or demote the lane

## Failure mode 7: shared core mythology

### Symptom

- multiple implementations keep diverging

### Root cause

- nobody forced one source of truth

### Corrective move

- consolidate into C++ core and delete sibling rewrites

## Failure mode 8: binary creep

### Symptom

- FlatBuffers show up in boring product paths

### Root cause

- one hot boundary justified binary and the discipline stopped there

### Corrective move

- re-limit binary formats to hot internal seams

## Failure mode 9: shader drift

### Symptom

- target-specific shader versions disagree or break unexpectedly

### Root cause

- no source-of-truth declaration under Slang

### Corrective move

- centralize authoring and target generation policy

## Failure mode 10: build-graph dishonesty

### Symptom

- nobody can explain how native, Wasm, and shell assets are really produced

### Root cause

- package scripts became architecture instead of tooling

### Corrective move

- restore CMake and Bun as honest authorities over their own lanes

## Recommended team topology for this stack

this is not mandatory, but it is often saner than pretending one undifferentiated
frontend-backend-fullstack blob will police itself.

### Shell owners

- Electrobun
- Solid
- Tailwind

### Product interaction owners

- Elm surfaces
- route-level client experience

### Hypermedia and ops owners

- HTMX
- Elysia HTML lanes

### Public contract owners

- Elysia JSON and stream APIs
- auth and policy edge

### Native compute owners

- C++ core
- compute boundary decisions (FFI, local process, or Drogon service)
- Drogon where service extraction is justified
- performance-critical algorithms

### Data owners

- PostgreSQL
- Drizzle migrations in TS lane
- Turso sync policies

### GPU owners

- Slang modules
- WGSL target pipeline
- WebGPU execution path

### Governance rule

you do not need isolated teams for every lane.
you **do** need named ownership for every lane.

## Forbidden crossover charter

this section exists because big stacks usually fail through **slow lane theft**,
not through one dramatic catastrophe.

every component below has a list of things it may collaborate with and things it
must not quietly annex.

## Electrobun forbidden crossovers

### Electrobun may collaborate with

- Solid shell
- Bun runtime logic
- local file affordances
- shell-level sync state visibility
- WebGPU host surfaces

### Electrobun must not quietly annex

- public auth policy
- billing rules
- route contract ownership
- deep editor state that belongs to Elm or shared core
- core domain truth that belongs in Postgres, C++, or Elysia

### Smell sentence

> "we put that rule in the desktop host because it needed a native API"

no.
native affordance and domain ownership are different things.

## Solid forbidden crossovers

### Solid may collaborate with

- Electrobun shell APIs
- Elm islands as host
- HTMX territory as surrounding route shell
- Elysia APIs
- Turso-backed local state indicators
- WebGPU views

### Solid must not quietly annex

- all meaningful feature state by inertia
- canonical workflow transitions already owned by Elm
- server-authored page ownership already owned by HTMX
- compute logic that belongs in C++ or Drogon

### Smell sentence

> "it was easier to just put that state in the global store"

that is how shells become empires.

## Elm forbidden crossovers

### Elm may collaborate with

- Solid shell hosts
- Elysia product contracts
- C++ core through coarse Wasm or service boundaries
- Tailwind-based visual styling around rendered DOM

### Elm must not quietly annex

- shell-wide chrome behavior
- admin pages that are mostly forms and tables
- casual JS library wrapper work with nonstop interop
- routing sovereignty for the whole app unless the project has consciously gone
  full Elm-centered

### Smell sentence

> "Elm owns the important part"

name the important part or stop saying that.

## HTMX forbidden crossovers

### HTMX may collaborate with

- Elysia HTML routes
- Tailwind styling
- bounded shell islands
- event-driven third-party widgets

### HTMX must not quietly annex

- the reactive shell
- deep state-machine product surfaces owned by Elm
- arbitrary client-owned DOM subtrees with local state
- public JSON API identity

### Smell sentence

> "we used HTMX there because we just needed something quick"

that is not architecture.
that is caffeine.

## Tailwind forbidden crossovers

### Tailwind may collaborate with

- Solid
- Elm-rendered DOM
- HTMX fragments
- design tokens and component abstractions

### Tailwind must not quietly annex

- workflow semantics
- feature ownership decisions
- accessibility responsibility through class-name luck alone
- component API design

### Smell sentence

> "the architecture is basically in the class names"

absolutely not.

## Elysia forbidden crossovers

### Elysia may collaborate with

- Drizzle
- PostgreSQL
- Turso-aware sync APIs
- Drogon internal services
- HTMX hypermedia routes
- Solid and Elm clients

### Elysia must not quietly annex

- all heavy compute logic
- native algorithm ownership already sitting in C++ core
- shell concerns
- updater and distribution semantics

### Smell sentence

> "we already had the request here so we just did the work here"

that sentence has launched a thousand bloated gateways.

## Drizzle forbidden crossovers

### Drizzle may collaborate with

- Elysia
- Bun scripts
- PostgreSQL
- Turso in the TS lane

### Drizzle must not quietly annex

- native binary contracts
- the C++ core's notion of domain identity
- product architecture authority over non-TS lanes

### Smell sentence

> "the Drizzle schema is the architecture"

no bestie, it is one lane's schema tooling.

## PostgreSQL forbidden crossovers

### PostgreSQL may collaborate with

- Drizzle migrations and access
- Elysia policy edge
- Drogon internal services
- Turso projections and sync target

### PostgreSQL must not quietly annex

- every device-local interaction concern
- every transient shell status concern
- every cache or derived view in the entire product by default

### Smell sentence

> "we'll just round-trip to Postgres for that too"

latency is a real cost, actually.

## Turso forbidden crossovers

### Turso may collaborate with

- local shell workflows
- offline drafts
- sync-aware Elysia APIs
- device-local caches and projections

### Turso must not quietly annex

- contested collaborative truth
- policy sovereignty
- global shared canonical entities by accident

### Smell sentence

> "it's basically the source of truth for the app while you're using it"

if you mean local operational state, say that.
if you mean universal truth, absolutely not.

## Drogon forbidden crossovers

### Drogon may collaborate with

- C++ shared core
- Elysia public edge
- Postgres where native-service ownership warrants it
- streaming and job status flows

### Drogon must not quietly annex

- public auth and session policy
- user-facing HTML rendering as a default style
- casual product-edge route ownership

### Smell sentence

> "the client just talks to Drogon directly for this one feature"

that is how second backends happen.

## C++ core forbidden crossovers

### C++ may collaborate with

- Drogon wrappers
- Emscripten and Wasm targets
- FlatBuffers schemas
- Slang or GPU-adjacent buffer preparation

### C++ must not quietly annex

- shell UX
- route composition
- session semantics
- hypermedia rendering

### Smell sentence

> "the native core now also knows about the app's tabs and dialogs"

why are we like this.

## CMake forbidden crossovers

### CMake may collaborate with

- Bun orchestration scripts
- shader compilation steps
- code generation
- native and Wasm target graphs

### CMake must not quietly annex

- TS package management
- public runtime config identity
- application shell ownership

### Smell sentence

> "we can just keep the real build in npm scripts"

incorrect and cursed.

## Wasm forbidden crossovers

### Wasm may collaborate with

- Solid or Elm hosts
- Elysia and Drogon product flows through coarse boundaries
- FlatBuffers or typed bindings

### Wasm must not quietly annex

- DOM sovereignty
- shell routing
- every small UI interaction loop

### Smell sentence

> "the feature now calls into Wasm for every field edit"

please step away from the boundary.

## FlatBuffers forbidden crossovers

### FlatBuffers may collaborate with

- C++ core
- Wasm bridge
- Drogon internal hot paths
- GPU-adjacent binary payloads

### FlatBuffers must not quietly annex

- product auth flows
- settings pages
- public HTML or JSON surface identity

### Smell sentence

> "users never see it so we made everything FlatBuffers"

developers still exist and need to debug things.

## Slang and WebGPU forbidden crossovers

### Slang and WebGPU may collaborate with

- C++ core
- Solid visual surfaces
- Electrobun desktop views
- tool-specific Elm or Solid state

### Slang and WebGPU must not quietly annex

- policy logic
- route identity
- durable business truth
- the belief that every feature is now a graphics problem

### Smell sentence

> "we should move more of the product into the GPU"

no.
the GPU lane is a specialist, not a coup.

## Concrete workflow constitutions

these mini-constitutions are useful when teams say "okay but what's the actual
flow?"

## Workflow constitution 1: local draft -> review -> publish

### Goal

let a desktop user work locally, potentially offline, then review and publish to
canonical truth.

### Recommended owners

- shell and local draft UI: Solid
- deep draft-state workflow if complex: Elm
- local storage: Turso
- publish API: Elysia
- canonical truth: PostgreSQL
- heavy validation or transforms: C++ core or Drogon if warranted

### Lawful sequence

1. user edits draft locally
2. draft writes land in Turso or local files first
3. shell exposes sync status and dirty state clearly
4. publish action goes through Elysia
5. Elysia validates public policy and auth
6. heavy transform or compile work delegates to C++ core or Drogon if needed
7. canonical durable record lands in PostgreSQL
8. Turso local state refreshes through explicit pull or local confirmation flow

### Common mistake

- directly treating the local draft as already-published truth and letting server
  reconciliation become vague

## Workflow constitution 2: compute job launch -> stream -> inspect

### Goal

run a heavy native task while keeping the product edge readable.

### Recommended owners

- launch contract: Elysia
- durable job metadata: PostgreSQL
- execution: C++ core + selected boundary (supervised process, queue-backed
  worker, or Drogon when isolation/service is warranted)
- status UI: Solid shell or HTMX route depending audience

### Lawful sequence

1. client starts job through Elysia
2. Elysia validates input and policy
3. Elysia records or coordinates job metadata in PostgreSQL
4. Elysia routes the heavy work to the lightest boundary that fits the job:
  in-process FFI, supervised process, queue-backed worker, or Drogon when
  service extraction is earned
5. the chosen boundary runs C++ core work
6. progress is exposed through stream or websocket semantics
7. UI consumes progress through Elysia-owned product contract unless the
   architecture explicitly made Drogon public
8. results are shaped back into product semantics

### Common mistake

- letting job-launch response and compute status APIs fracture into separate
  public worlds with no single contract owner

## Workflow constitution 3: admin queue triage

### Goal

let operators review, filter, and act on records with low ceremony.

### Recommended owners

- route family: HTMX
- HTML and policy: Elysia
- typed SQL: Drizzle
- canonical truth: PostgreSQL

### Lawful sequence

1. operator opens queue page
2. Elysia renders full page or fragment HTML
3. HTMX issues targeted requests for filters, actions, and updates
4. Elysia validates permissions and shapes fragment responses
5. Drizzle performs TS-lane SQL access
6. PostgreSQL remains canonical

### Common mistake

- rebuilding an admin queue as a mini-SPA for no product reason at all

## Workflow constitution 4: deep planner or editor surface

### Goal

support a bounded feature with lots of transitions, validation, or undo-like
behavior.

### Recommended owners

- host shell: Solid
- feature brain: Elm
- heavy algorithms: C++ core or Wasm
- public contract: Elysia

### Lawful sequence

1. shell mounts bounded feature island
2. Elm receives initial coarse config
3. Elm drives feature-local transitions
4. expensive operations cross to Wasm or service boundaries coarsely
5. public persistence or collaboration still flows through Elysia and Postgres

### Common mistake

- putting the feature in Elm while keeping a parallel Solid store as a shadow
  owner

## Workflow constitution 5: GPU preview or analysis surface

### Goal

run a shader-heavy preview in a way that preserves source-of-truth sanity.

### Recommended owners

- shell and surrounding panels: Solid
- GPU authoring truth: Slang
- GPU execution: WebGPU
- heavy buffer prep: C++ core if justified

### Lawful sequence

1. UI state changes in Solid or Elm
2. product semantics stay in CPU-side layers
3. Slang modules compile to target outputs including WGSL
4. WebGPU executes rendering or compute
5. fallback or capability limits are surfaced honestly

### Common mistake

- manually editing multiple target shader sources and hoping they remain aligned

## Workflow constitution 6: import large external artifact

### Goal

let users bring large files or models into the system without turning the shell
into a parser.

### Recommended owners

- file affordance and local access: Electrobun
- import UI flow: Solid or Elm depending complexity
- parse and normalize: C++ core
- service wrapper if remote or long-running: supervised process,
  queue-backed worker, or Drogon when service extraction is warranted
- public response and persistence policy: Elysia

### Lawful sequence

1. shell opens file affordance
2. UI receives file selection and progress affordances
3. heavy parse runs in native core, a supervised process, or a queue-backed
  worker depending size and isolation needs
4. UI previews coarse results
5. user confirms import or publish
6. Elysia commits product-facing state

### Common mistake

- parsing giant artifacts in the shell because the file picker lived there

## Sync policy templates

the official Turso sync story is explicit enough that projects should also be
explicit.
do not improvise sync semantics in prose after the fact.

## Template A: local draft sync policy

### Best for

- user-authored drafts
- offline-first desktop editing
- staged publish flows

### Ownership

- local working truth while editing: Turso
- canonical published truth: PostgreSQL

### Push policy

- on manual sync
- on explicit publish
- optionally on reconnect

### Pull policy

- on app launch if online
- on manual refresh
- after successful publish if needed

### Merge policy

- draft updates are local
- publish creates or updates canonical object through Elysia
- do not rely on blind last-push-wins for published collaborative fields

### UI obligations

- show dirty state
- show sync pending state
- show last successful sync time

## Template B: replicated read model policy

### Best for

- read-mostly local mirrors
- cached dashboards
- locally searchable views of shared data

### Ownership

- canonical truth: PostgreSQL
- local mirror: Turso

### Push policy

- usually none or very limited

### Pull policy

- on launch
- on reconnect
- on explicit refresh
- optionally on timer

### Merge policy

- remote wins because the local copy is derived

### UI obligations

- show staleness when it matters

## Template C: field-capture offline policy

### Best for

- intermittent connectivity
- data collection at the edge

### Ownership

- local capture truth until upload succeeds: Turso
- central authoritative truth after ingest: PostgreSQL

### Push policy

- background on reconnect
- user-forced sync option available

### Pull policy

- limited; often reference data and assignment data only

### Merge policy

- submission IDs and ingest rules must prevent accidental duplicate authority

### UI obligations

- clearly show captured locally vs confirmed upstream

## Template D: contentious collaborative object policy

### Best for

- honestly, usually not for naïve last-push-wins

### Ownership

- PostgreSQL canonical
- Turso local cache or draft staging only

### Push policy

- explicit operations through Elysia

### Pull policy

- frequent refresh or subscription-based updates

### Merge policy

- application-defined, not blind sync default

### UI obligations

- conflict resolution UX must be real, not implied

## Template E: local queue policy

### Best for

- pending uploads
- retryable actions
- local job staging

### Ownership

- Turso stores pending queue
- PostgreSQL stores accepted durable job truth after submission

### Push policy

- on connectivity
- on retry timer
- on user force sync

### Pull policy

- not always necessary beyond status refresh

### Merge policy

- queue item IDs must be idempotent enough to avoid duplicate server truth

### UI obligations

- show queued, retrying, failed, and sent states honestly

## Runtime and environment matrix

architectures fail when they only describe prod and forget every other reality.

## Environment matrix

| Environment | Shell mode | Gateway mode | Native mode | Local data mode | Update mode | Must verify |
| --- | --- | --- | --- | --- | --- | --- |
| local UI dev | Electrobun dev build or web shell equivalent | Elysia dev | C++ debug or mocked | Turso local dev DB or temp file | none | shell boundaries, route ownership |
| local compute dev | Solid or minimal shell | Elysia dev | C++ debug with selected boundary mode (FFI/process/Drogon) | test Postgres / local cache | none | compute contract separation |
| offline dev simulation | desktop shell | optional stub gateway | local or mocked native | Turso local-first | none | sync UX and fallback behavior |
| integration test env | shell optional | Elysia test | Drogon test | disposable Postgres + disposable Turso | none | seam correctness |
| canary desktop build | Electrobun canary | Elysia staging | Drogon staging | realistic sync state | Electrobun artifact flow | updater, packaging, code signing assumptions |
| stable desktop build | Electrobun stable | Elysia prod | Drogon prod | production sync topology | patch + bundle fallback | release integrity |
| browser or preview mode | Solid shell without desktop host or webview-hosted | Elysia | Wasm or remote Drogon | local browser-safe persistence if needed | none | Wasm boundary and GPU capability |
| GPU CI smoke | minimal UI | not always needed | optional native tool | sample assets | none | shader compilation and fallback |

### Environment law

if an architecture only works in one environment because the team memorized the
missing pieces, it is not mature.

## ADR checklist for stack changes

when introducing, promoting, or demoting a lane in this stack, write down these
answers.

### Problem statement

- what concrete pain exists right now?
- which existing lane failed to solve it?
- what measured or observed evidence exists?

### Lane decision

- which lane will now own the concern?
- what lane is being demoted or kept out?
- is this lane primary, bounded, or dormant?

### Boundary decision

- what format crosses the boundary?
- who versions the contract?
- who translates internal errors into public semantics?
- what are the timeout, retry, and failure behaviors?

### Truth decision

- where is canonical truth for affected entities?
- where is local or cached state?
- what sync or merge policy applies?

### Build and release decision

- does this change affect Bun build truth?
- does this change affect CMake build truth?
- does this change affect Electrobun packaging or updater flow?
- does this change affect shader generation or Wasm output?

### Observability decision

- how will developers debug failures here?
- what metrics or logs prove the boundary is healthy?
- what user-visible health state, if any, is required?

### Kill-switch decision

- if this lane disappoints, how do we back out?
- what is the simpler fallback architecture?

## The no-folklore doctrine

if the answer to any major architecture question is:

- "ask Alex"
- "check that old thread"
- "it depends on the feature"
- "you kind of just know"

then the architecture is under-governed.

this stack is powerful enough to deserve written law.
use this file to make the law real instead of relying on haunted oral tradition.

## Lane quick-checklists (for when the team is tired and needs the short version)

these are the panic cards.
use them during implementation reviews, not just architecture summits.

## Before touching Electrobun, ask

- is this truly a shell concern?
- does this require desktop-native affordance?
- are we adding a clean bridge or a random shortcut?
- does this affect packaging, update flow, or code-signing assumptions?
- are we accidentally moving domain logic into the shell host?

## Before touching Solid, ask

- is this shell state or domain state?
- does this belong to a bounded feature island instead?
- is this route actually HTMX territory?
- are we creating a new global store habit we will regret later?
- does this preserve the shell's role as host rather than empire?

## Before touching Elm, ask

- does the feature actually deserve TEA discipline?
- can the boundary stay coarse?
- are ports rare and intentional?
- are we keeping shell and hypermedia owners out of the same surface?
- are we using Elm because it is correct here, not because it sounds virtuous?

## Before touching HTMX, ask

- is this truly a hypermedia-friendly surface?
- does the route have named territory?
- can the pushed URL return a full page?
- have we considered `HX-Request` caching variation?
- are we avoiding DOM warfare with client-owned islands?

## Before touching Tailwind, ask

- is this using the shared design token system?
- are we repeating a utility blob that should become an abstraction?
- are we accidentally encoding workflow semantics in class names?
- is the styling consistent across Solid, Elm, and HTMX surfaces?
- are we preserving accessibility and state clarity, not just visual neatness?

## Before touching Elysia, ask

- is this edge contract work or compute creep?
- does this route shape a public HTML or JSON contract?
- should this delegate to Drogon or shared core instead?
- are auth and policy still centralized here?
- are we preserving a clean public story instead of tunneling internal weirdness?

## Before touching Drizzle, ask

- is this a TS-lane schema or migration concern?
- did we consider the current Drizzle release behavior or migration engine state?
- are we treating Drizzle as access strategy rather than universal law?
- does this change affect Postgres ownership or Turso sync semantics?
- would the native lane be better served by a different contract abstraction?

## Before touching PostgreSQL, ask

- is this entity truly canonical?
- is a local-first or cached representation also needed nearby?
- are permissions and invariants staying centralized?
- is this change going to hurt latency-sensitive shell flows unnecessarily?
- are we naming the difference between truth, cache, and projection?

## Before touching Turso, ask

- is this local-first state or just a cache?
- when will we `push()` and `pull()`?
- is last-push-wins acceptable here?
- how will the user see sync health or staleness?
- are we accidentally creating a shadow source of truth?

## Before touching Drogon, ask

- is this genuinely native compute or throughput work?
- should the public edge still stay in Elysia?
- is the shared C++ core the real owner of the logic?
- are we about to expose another public contract by accident?
- how will progress, failure, and retries be observed?

## Before touching the C++ core, ask

- is this truly shared hot logic?
- should this live in the host wrapper instead?
- do native and Wasm both need this behavior?
- are we keeping the core free of shell or route concerns?
- are we deleting duplicated implementations elsewhere?

## Before touching CMake, ask

- is this the real native build truth?
- are we keeping Wasm and native targets aligned?
- should this be a formal target rather than a shell script?
- does Bun merely orchestrate this, or are we leaking ownership back to JS?
- are generated schemas, shaders, and artifacts wired into the graph honestly?

## Before touching Emscripten or Wasm bindings, ask

- is the boundary coarse enough?
- are browser-runtime constraints understood here?
- should this be Embind, a thinner ABI, or a binary contract?
- are we calling across the boundary too often?
- is the host still clearly responsible for DOM and shell behavior?

## Before touching FlatBuffers, ask

- is this boundary hot enough to earn binary complexity?
- who versions this schema?
- where is the translation layer back to human-readable contracts?
- can engineers still inspect and debug the system sanely?
- are we keeping FlatBuffers away from boring public CRUD traffic?

## Before touching Slang, ask

- is Slang still the shader source of truth?
- does this belong in a module rather than another random file?
- are capability restrictions explicit?
- are we preserving portability rather than growing target forks?
- is there any sign of business logic creeping into shader code?

## Before touching WebGPU, ask

- is this really a GPU-worthy workload?
- what is the capability and fallback story?
- who owns the buffer layout contract?
- is the CPU-side product logic still in the right place?
- are we making the product better, or just more impressive on paper?

## The architecture oath for this stack

if you are about to place new work in this stack, ask yourself:

- am I putting this where it is nearest, or where it belongs?
- am I respecting the default lane, or dodging it?
- am I adding a bounded exception, or a precedent that will quietly spread?
- am I keeping human-readable edges human-readable?
- am I letting performance tools stay specialized?
- am I preserving one source of truth for logic, data, shaders, and build graphs?

if the honest answer is "not really," stop and redesign before the repo learns a
new bad habit.

## Final mantra

> shell explicit, interaction bounded, hypermedia named, contract singular,
> compute native, truth canonical, sync humble, binary internal, shaders unified,
> build graphs honest.

that is the actual religion here.

this stack can absolutely slap.
Electrobun gives it shell weight.
Solid gives it responsive chrome.
Elm gives it a disciplined brain where needed.
HTMX gives it low-ceremony hypermedia power.
Elysia gives it a clean public edge.
Drizzle gives the TS lane typed SQL without ORM baroque nonsense.
PostgreSQL gives it real truth.
Turso gives it local-first courage.
Drogon and C++ give it native teeth.
Emscripten gives it portable embodiment.
FlatBuffers give the hot path a reason to exist.
Slang, WGSL, and WebGPU give the GPU lane a real future.
Bun and CMake keep the build worlds honest.

but none of that matters if the repo becomes a diplomatic summit where every
layer is simultaneously in charge.

we are not here to preserve diplomatic ambiguity.
we are here to establish **jurisdiction**.

this stack is best when it behaves like a federation with a constitution, not a
polycule of frameworks trying to share one toothbrush.

seize the means of composition, set hard borders, and let each lane do the thing
it was actually born to do uwu 💜✨
