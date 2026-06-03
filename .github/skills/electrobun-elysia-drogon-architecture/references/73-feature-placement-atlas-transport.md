# Feature Placement Atlas Transport

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Feature placement atlas

## Feature placement atlas

this section is intentionally blunt.
if a new piece of work arrives, use these tables before inventing a fourth owner.


---

### Source section: ## Transport and representation matrix

## Transport and representation matrix

| Boundary | Preferred format | Upgrade to | Avoid | Why |
| --- | --- | --- | --- | --- |
| browser or shell route to Elysia HTMX surface | HTML | SSE or websocket extension for live fragments if truly needed | FlatBuffers | HTMX is HTML-first |
| Solid or Elm app to Elysia | JSON | stream or websocket as required | FlatBuffers by default | product edge clarity |
| Elysia to public docs tooling | OpenAPI + JSON schema story | generated TS types | native-only undocumented shapes | contract stewardship |
| Elysia to Drogon internal call | JSON by default | FlatBuffers if the path is hot or payload-heavy | raw ad hoc strings | keep simple things debuggable |
| Drogon to C++ core | native in-process calls | shared structs or FlatBuffers where needed | JSON if avoidable in hottest loops | internal native lane |
| Solid host to Wasm core | coarse typed bindings | FlatBuffers if payloads are large | tiny chatty getter calls | Wasm bridge cost matters |
| Wasm core to GPU prep | structured binary layout | FlatBuffers or direct typed buffer layout | hand-managed string protocols | this is performance-adjacent |
| Slang authoring to web target | Slang source -> WGSL output | capability-conditioned variants | dual-maintained raw WGSL and raw HLSL | one shader truth |
| updater static host to desktop client | Electrobun patch files and manifests | compressed full bundle fallback | business API route piggybacking | updater has its own architecture |



