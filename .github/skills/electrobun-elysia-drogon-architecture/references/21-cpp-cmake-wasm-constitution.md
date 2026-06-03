# CPP Cmake WASM Constitution

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## modern C++ constitution (the shared algorithmic center)

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


---

### Source section: ## CMake constitution (the native build truth)

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


---

### Source section: ## Emscripten and Embind constitution (the browser bridge)

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


---

### Source section: ## C++ WebAssembly constitution (one core, two embodiments)

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


---

### Source section: ## Before touching the C++ core, ask

## Before touching the C++ core, ask

- is this truly shared hot logic?
- should this live in the host wrapper instead?
- do native and Wasm both need this behavior?
- are we keeping the core free of shell or route concerns?
- are we deleting duplicated implementations elsewhere?


---

### Source section: ## Before touching CMake, ask

## Before touching CMake, ask

- is this the real native build truth?
- are we keeping Wasm and native targets aligned?
- should this be a formal target rather than a shell script?
- does Bun merely orchestrate this, or are we leaking ownership back to JS?
- are generated schemas, shaders, and artifacts wired into the graph honestly?


---

### Source section: ## Before touching Emscripten or Wasm bindings, ask

## Before touching Emscripten or Wasm bindings, ask

- is the boundary coarse enough?
- are browser-runtime constraints understood here?
- should this be Embind, a thinner ABI, or a binary contract?
- are we calling across the boundary too often?
- is the host still clearly responsible for DOM and shell behavior?



