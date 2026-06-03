# Ownership By Concern Atlas

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Ownership-by-concern atlas

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



