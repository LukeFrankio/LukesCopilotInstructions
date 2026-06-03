# Lane Model And Roster

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## What this stack actually is

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


---

### Source section: ## The stack roster at a glance

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


---

### Source section: ## Canonical vocabulary (use these names or lose the plot)

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



