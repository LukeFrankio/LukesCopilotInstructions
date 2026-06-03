# Environment Matrix And Runtime Modes

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Runtime and environment matrix

## Runtime and environment matrix

architectures fail when they only describe prod and forget every other reality.


---

### Source section: ## Environment matrix

## Environment matrix

| Environment | Shell mode | Gateway mode | Native mode | Local data mode | Update mode | Must verify |
| --- | --- | --- | --- | --- | --- | --- |
| local UI dev | Electrobun dev build or web shell equivalent | Elysia dev | C++ debug or mocked | Turso local dev DB or temp file | none | shell boundaries, route ownership |
| local compute dev | Solid or minimal shell | Elysia dev | C++ debug with selected boundary mode (FFI/process/Drogon) | test Postgres / local cache | none | compute contract separation |
| offline dev simulation | desktop shell | optional stub gateway | local or mocked native | Turso local-first | none | sync UX and fallback behavior |
| integration test env | shell optional | Elysia test | Drogon test | disposable Postgres + disposable Turso | none | seam correctness |
| canary desktop build | Electrobun canary | Elysia staging | Drogon staging | realistic sync state | Electrobun artifact flow | updater, packaging, code signing assumptions |
| stable desktop build | Electrobun stable | Elysia prod | Drogon prod | production sync topology | patch + bundle fallback | release integrity |
| browser or preview mode | Solid shell without desktop host or webview-hosted | Elysia | Wasm or remote Drogon | local browser-safe persistence if needed | none | Wasm boundary and GPU capability |
| GPU CI smoke | minimal UI | not always needed | optional native tool | sample assets | none | shader compilation and fallback |

### Environment law

if an architecture only works in one environment because the team memorized the
missing pieces, it is not mature.



