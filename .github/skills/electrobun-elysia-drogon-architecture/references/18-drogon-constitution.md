# Drogon Constitution

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Drogon constitution (the compute engine)

## Drogon constitution (the compute engine)

Drogon is an **optional out-of-process compute service**, not an automatic
network hop.

### Compute boundary ladder (default order)

choose the lightest boundary that satisfies the workload:

1. **in-process call path**

- Bun-side FFI into compiled native code or equivalent thin host bridge

2. **local supervised process boundary**

- stdio or unix-domain/named-pipe style protocol when isolation is needed but
    service ceremony is not

3. **Drogon internal service**

- HTTP or websocket service when independent scaling, lifecycle, or
    multi-caller integration is justified

4. **Drogon public promotion**

- only in consciously compute-first architectures

the default should not skip from step 1 to step 3 without reason.

protocol note:

- HTTP is common and pragmatic, but not mandatory for every internal compute seam
- if typed service contracts or internal RPC ergonomics matter more than
  web-style routing, gRPC or equivalent RPC transport may be the better fit
- if the need is isolation without full service ceremony, supervised process
  protocols (stdio or local sockets/pipes) can be enough

### Drogon transport decision tree (practical)

use this quick tree before introducing or expanding a Drogon service:

1. **single caller + low latency sensitivity + shared deploy cadence?**
   - start in-process (Bun FFI / native bridge)
2. **need crash isolation or memory isolation but still single-caller?**
   - prefer supervised local process protocol first
3. **need independent scaling, multi-caller consumption, or long-lived service
   lifecycle?**
   - promote to Drogon internal service
4. **need strongly typed service contracts across many internal callers?**
   - evaluate RPC transport strategy explicitly (Drogon HTTP/WebSocket vs gRPC or
     equivalent), then document the choice
5. **need public-facing compute API identity?**
   - only then consider public Drogon promotion with explicit contract governance

### Concrete examples

- **example A: hot synchronous scoring call from one Elysia route**
  - default: in-process boundary (FFI)
- **example B: batch transform that can crash on malformed artifacts**
  - default: supervised local process boundary first
- **example C: simulation service consumed by API, CLI, and internal workers**
  - default: Drogon service boundary likely warranted
- **example D: long-running streamed simulation with independent autoscaling**
  - default: Drogon internal service, with explicit edge contract mapping in
    Elysia

### What Drogon is for

- async service endpoints for internal compute
- long-running jobs
- progress streaming
- concurrency-heavy operations
- native-first API surfaces for compute work
- coroutine-based handlers where they help readability
- internal coordination over HTTP, WebSocket, RPC, or process protocols as
  architecture warrants

### What Drogon is not for

- becoming a stealth second public backend by convenience
- owning shell or client UX concerns
- replacing Elysia on public routes just because C++ feels strong

### Laws

1. **Drogon is optional and internal by default.**
2. **Prefer Bun FFI or in-process native calls before introducing service
  transport.**
3. **Drogon computes; Elysia composes.**
4. **If Drogon becomes public, say so explicitly and adjust the whole contract
   story.**
5. **Keep auth and product policy centralized unless the architecture consciously
   changes that.**
6. **Use Drogon when the service boundary genuinely matters.**
   - async throughput
   - simulation
   - long-running tasks
   - streaming

- multi-caller service integration
- independent scaling or deploy cadence

7. **Do not make clients pick between Elysia and Drogon for the same kind of
   product call.**

### Good Drogon territory

- simulation jobs
- internal transform pipelines
- native model execution
- streaming heavy results
- compute status APIs
- native WebSocket progress updates

### Bad Drogon territory

- the product's general-purpose public REST or HTML contract by accident
- auth pages
- settings forms
- user profile page composition

### Smells

- client apps hitting Drogon directly because it was easier one time
- product-level errors and semantics leaking straight from native handlers
- duplicated API shape work between Elysia and Drogon


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

### Source section: ## Drogon observability

## Drogon observability

- long-running jobs must expose progress and failure clearly
- internal compute APIs need metrics and structured logs


---

### Source section: ## Before touching Drogon, ask

## Before touching Drogon, ask

- is this genuinely native compute or throughput work?
- should the public edge still stay in Elysia?
- is the shared C++ core the real owner of the logic?
- are we about to expose another public contract by accident?
- how will progress, failure, and retries be observed?



