# Forbidden Crossover Charter Part 2

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Forbidden crossover charter

## Forbidden crossover charter

this section exists because big stacks usually fail through **slow lane theft**,
not through one dramatic catastrophe.

every component below has a list of things it may collaborate with and things it
must not quietly annex.


---

### Source section: ## Elysia forbidden crossovers

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


---

### Source section: ## Drizzle forbidden crossovers

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


---

### Source section: ## PostgreSQL forbidden crossovers

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


---

### Source section: ## Turso forbidden crossovers

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


---

### Source section: ## Drogon forbidden crossovers

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


---

### Source section: ## C++ core forbidden crossovers

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


---

### Source section: ## CMake forbidden crossovers

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


---

### Source section: ## Wasm forbidden crossovers

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



