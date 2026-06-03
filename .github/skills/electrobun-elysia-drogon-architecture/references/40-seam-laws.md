# Seam Laws

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## The seam laws (this is where stacks become either elegant or cursed)

## The seam laws (this is where stacks become either elegant or cursed)


---

### Source section: ## Shell to interaction engine seam (Solid <-> Elm)

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


---

### Source section: ## Shell to hypermedia seam (Solid <-> HTMX)

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


---

### Source section: ## HTMX to Elysia seam

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


---

### Source section: ## Solid or Elm to Elysia seam

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


---

### Source section: ## Elysia to Drogon seam

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


---

### Source section: ## Drizzle to Postgres seam

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


---

### Source section: ## Turso to Postgres seam

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


---

### Source section: ## C++ core to Wasm host seam

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


---

### Source section: ## C++ core to Drogon seam

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


---

### Source section: ## FlatBuffers to human-readable edge seam

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


---

### Source section: ## Slang to WebGPU seam

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


---

### Source section: ## Bun to CMake seam

## Bun to CMake seam

### Good

- Bun scripts orchestrate the native build when useful
- CMake retains authority over the native graph

### Bad

- package.json scripts become the real native build system
- nobody can build the core without JS-specific folklore

### Law

orchestration is not ownership.



