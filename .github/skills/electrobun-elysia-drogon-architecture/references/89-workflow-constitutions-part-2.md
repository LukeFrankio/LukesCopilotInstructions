# Workflow Constitutions Part 2

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Concrete workflow constitutions

## Concrete workflow constitutions

these mini-constitutions are useful when teams say "okay but what's the actual
flow?"


---

### Source section: ## Workflow constitution 4: deep planner or editor surface

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


---

### Source section: ## Workflow constitution 5: GPU preview or analysis surface

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


---

### Source section: ## Workflow constitution 6: import large external artifact

## Workflow constitution 6: import large external artifact

### Goal

let users bring large files or models into the system without turning the shell
into a parser.

### Recommended owners

- file affordance and local access: Electrobun
- import UI flow: Solid or Elm depending complexity
- parse and normalize: C++ core
- service wrapper if remote or long-running: Drogon
- public response and persistence policy: Elysia

### Lawful sequence

1. shell opens file affordance
2. UI receives file selection and progress affordances
3. heavy parse runs in native core or compute service
4. UI previews coarse results
5. user confirms import or publish
6. Elysia commits product-facing state

### Common mistake

- parsing giant artifacts in the shell because the file picker lived there



