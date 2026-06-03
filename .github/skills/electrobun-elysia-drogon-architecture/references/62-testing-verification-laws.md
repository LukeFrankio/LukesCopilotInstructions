# Testing Verification Laws

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Testing and verification laws

## Testing and verification laws


---

### Source section: ## Shell and route tests

## Shell and route tests

- Solid shell behavior should be tested at route and embedding boundaries
- HTMX fragments should be tested as fragment and full-page responses where
  history is involved


---

### Source section: ## Interaction engine tests

## Interaction engine tests

- Elm features deserve state-transition tests and deterministic scenario coverage


---

### Source section: ## Public contract tests

## Public contract tests

- Elysia contracts should be verified at the public boundary
- OpenAPI generation and type expectations should be treated as contract assets


---

### Source section: ## Compute tests

## Compute tests

- C++ core gets unit tests and property-heavy tests where warranted
- Drogon service wrappers get integration tests around streaming, concurrency, and
  failure behavior


---

### Source section: ## Sync tests

## Sync tests

- Turso flows need offline, push, pull, conflict, and restart scenarios
- if local-first matters, test it like it matters


---

### Source section: ## Binary schema tests

## Binary schema tests

- FlatBuffers schema evolution requires compatibility checks
- do not trust binary boundaries by vibes


---

### Source section: ## Shader tests

## Shader tests

- compile shaders for actual targets in CI
- a shader that only exists in the editor is fan fiction



