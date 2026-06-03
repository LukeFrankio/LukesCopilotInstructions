# Lane Quick Checklists Native GPU

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Lane quick-checklists (for when the team is tired and needs the short version)

## Lane quick-checklists (for when the team is tired and needs the short version)

these are the panic cards.
use them during implementation reviews, not just architecture summits.


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


---

### Source section: ## Before touching FlatBuffers, ask

## Before touching FlatBuffers, ask

- is this boundary hot enough to earn binary complexity?
- who versions this schema?
- where is the translation layer back to human-readable contracts?
- can engineers still inspect and debug the system sanely?
- are we keeping FlatBuffers away from boring public CRUD traffic?


---

### Source section: ## Before touching Slang, ask

## Before touching Slang, ask

- is Slang still the shader source of truth?
- does this belong in a module rather than another random file?
- are capability restrictions explicit?
- are we preserving portability rather than growing target forks?
- is there any sign of business logic creeping into shader code?


---

### Source section: ## Before touching WebGPU, ask

## Before touching WebGPU, ask

- is this really a GPU-worthy workload?
- what is the capability and fallback story?
- who owns the buffer layout contract?
- is the CPU-side product logic still in the right place?
- are we making the product better, or just more impressive on paper?



