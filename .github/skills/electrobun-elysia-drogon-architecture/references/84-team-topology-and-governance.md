# Team Topology And Governance

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Recommended team topology for this stack

## Recommended team topology for this stack

this is not mandatory, but it is often saner than pretending one undifferentiated
frontend-backend-fullstack blob will police itself.

### Shell owners

- Electrobun
- Solid
- Tailwind

### Product interaction owners

- Elm surfaces
- route-level client experience

### Hypermedia and ops owners

- HTMX
- Elysia HTML lanes

### Public contract owners

- Elysia JSON and stream APIs
- auth and policy edge

### Native compute owners

- C++ core
- compute boundary decisions (FFI, local process, or Drogon service)
- Drogon where service extraction is justified
- performance-critical algorithms

### Data owners

- PostgreSQL
- Drizzle migrations in TS lane
- Turso sync policies

### GPU owners

- Slang modules
- WGSL target pipeline
- WebGPU execution path

### Governance rule

you do not need isolated teams for every lane.
you **do** need named ownership for every lane.



