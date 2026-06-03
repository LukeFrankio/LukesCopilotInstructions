# Default Federation Architecture

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## The recommended default architecture (the Constitutional Federation)

## The recommended default architecture (the Constitutional Federation)

this is the default architecture this file recommends unless the project gives a
strong reason otherwise.

### Summary

- **Electrobun + Bun + Solid + Tailwind** own the desktop shell
- **Elm** owns one or more bounded, correctness-sensitive interaction islands
- **HTMX** owns named hypermedia surfaces such as admin, operations, reports,
  settings, or document-heavy routes
- **Elysia** owns the public contract layer, BFF logic, auth boundary,
  validation, HTML fragment rendering for HTMX, and JSON or streaming APIs for
  interactive clients
- **modern C++** owns heavy compute logic, with **Bun FFI/in-process boundaries
  first** and **Drogon service extraction when justified**
- **modern C++ + CMake** own the shared performance core
- **Emscripten / Embind** compile the core into Wasm where browser or portable
  execution matters
- **PostgreSQL** owns canonical truth
- **Turso Sync** owns local-first or offline state near the client and syncs
  explicitly
- **FlatBuffers** stay on internal hot boundaries only
- **Slang -> WGSL -> WebGPU** own the GPU lane

### Why this default slaps

because it gives every major worldview a role without letting any of them
silently become sovereign over the others.

### Why this default might be wrong

it is wrong when:

- the project is far more hypermedia-centric than shell-centric
- Elm deserves to own most of the product surface, not just bounded islands
- the application is compute-first and Elysia would only proxy everything
- the product is truly local-first and cloud truth is secondary for long periods
- the product is GPU-first and most architecture should bend around the visual or
  compute pipeline

### The default ownership map

| Concern | Owner | Notes |
| --- | --- | --- |
| app shell | Electrobun + Solid | shell chrome, windowing, routing shell, menus, notifications |
| shared styling | Tailwind CSS | one visual dialect across Solid, Elm-rendered DOM, and HTMX surfaces |
| deepest feature state | Elm | only where the feature genuinely deserves TEA-level discipline |
| document or CRUD flows | HTMX + Elysia HTML | server-authored fragments, validation, forms, admin, reports |
| public API contract | Elysia | JSON, HTML fragments, streaming, auth-aware response shaping |
| TS database access | Drizzle ORM | Elysia lane, migrations, schema, typed SQL |
| canonical durable truth | PostgreSQL | relational invariants, authoritative writes |
| local and offline state | Turso Sync | explicit push/pull, device-local durability |
| heavy native compute | C++ core + selected transport (Bun FFI first, Drogon when warranted) | async execution, streaming, or isolated scaling when earned |
| shared algorithmic center | modern C++ | one implementation, many targets |
| browser-portable compute | Emscripten / Wasm | same core, different host |
| internal binary contracts | FlatBuffers | only for hot or high-volume paths |
| shader truth | Slang | modular source, cross-target pipeline |
| browser or desktop GPU execution | WebGPU | fed by Slang-generated WGSL on web target |

### The default constitutional laws

1. **Electrobun owns the shell, not the domain.**
2. **Solid owns app chrome and cross-cutting UI, not every deep feature brain.**
3. **Elm owns only bounded features that truly deserve deterministic state
   architecture.**
4. **HTMX gets named territory, not vibes-based escape-hatch privileges.**
5. **Elysia owns the public contract and product-facing composition.**
6. **Drogon is optional and internal by default; it computes rather than
  negotiating product semantics.**
7. **Start with the lightest valid compute boundary.**

- Bun FFI or in-process core calls first
- promote to Drogon only when isolation, scaling, multi-caller, or lifecycle
    pressure justifies a service

8. **PostgreSQL is the durable system of record unless a narrower exception is
   explicitly declared.**
2. **Turso is local-first and sync-explicit; it is not shadow sovereignty.**
3. **C++ is written once for shared hot logic and compiled to native and Wasm
   targets when needed.**
4. **FlatBuffers stay inside the hot path.**
5. **Slang is the shader source of truth; WGSL is a target artifact, not the
    authoring canon.**
6. **CMake owns native and Wasm build truth; Bun owns TS build truth.**

### What this architecture feels like in practice

- the user perceives a cohesive native app shell
- core interaction surfaces feel disciplined and predictable
- admin and ops surfaces ship fast with server-authored HTML
- the public contract stays legible
- the heavy work lives where native code belongs
- the local machine can stay useful offline
- the GPU lane can grow without swallowing the whole repo

that is what a bounded mega-stack looks like when it is being based instead of
performative.



