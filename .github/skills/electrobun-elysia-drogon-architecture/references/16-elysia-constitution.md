# Elysia Constitution

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Elysia constitution (the public contract layer)

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


---

### Source section: ## Public contract security

## Public contract security

- auth policy should be centralized in Elysia by default
- public error semantics should be deliberate
- do not let compute-internal details leak directly to product clients


---

### Source section: ## Elysia observability

## Elysia observability

- exploit built-in OpenTelemetry support when appropriate
- log contract-level events and policy decisions


---

### Source section: ## Before touching Elysia, ask

## Before touching Elysia, ask

- is this edge contract work or compute creep?
- does this route shape a public HTML or JSON contract?
- should this delegate to Drogon or shared core instead?
- are auth and policy still centralized here?
- are we preserving a clean public story instead of tunneling internal weirdness?



