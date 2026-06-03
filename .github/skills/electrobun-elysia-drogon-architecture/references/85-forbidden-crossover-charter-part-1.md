# Forbidden Crossover Charter Part 1

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Forbidden crossover charter

## Forbidden crossover charter

this section exists because big stacks usually fail through **slow lane theft**,
not through one dramatic catastrophe.

every component below has a list of things it may collaborate with and things it
must not quietly annex.


---

### Source section: ## Electrobun forbidden crossovers

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


---

### Source section: ## Solid forbidden crossovers

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


---

### Source section: ## Elm forbidden crossovers

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


---

### Source section: ## HTMX forbidden crossovers

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


---

### Source section: ## Tailwind forbidden crossovers

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



