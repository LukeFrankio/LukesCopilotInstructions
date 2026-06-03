# Product Archetype Playbooks Part 1

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Product archetype playbooks

## Product archetype playbooks

these are example stack shapes that recur a lot.


---

### Source section: ## Archetype A: scientific visualization workbench

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


---

### Source section: ## Archetype B: regulated workflow desktop app

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


---

### Source section: ## Archetype C: internal operations platform with optional desktop shell

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


---

### Source section: ## Archetype D: collaborative modeling tool

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



