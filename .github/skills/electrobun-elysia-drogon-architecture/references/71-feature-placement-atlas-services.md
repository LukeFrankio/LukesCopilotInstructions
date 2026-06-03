# Feature Placement Atlas Services

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Feature placement atlas

## Feature placement atlas

this section is intentionally blunt.
if a new piece of work arrives, use these tables before inventing a fourth owner.


---

### Source section: ## Service and compute placement matrix

## Service and compute placement matrix

| Work item | Default owner | Secondary helper | Do not default to | Why |
| --- | --- | --- | --- | --- |
| login and session issuance | Elysia | PostgreSQL | Drogon | public contract and auth edge |
| role and policy checks | Elysia + PostgreSQL | Drizzle | Turso-only, Drogon-only | product edge policy should stay coherent |
| HTML fragment rendering | Elysia | HTMX | Drogon | public hypermedia lane |
| JSON API composition | Elysia | Drizzle, Postgres | Drogon direct | public contract layer territory |
| route validation | Elysia | schema definitions | C++ core | official Elysia strength |
| OpenAPI generation | Elysia | none | Drogon | Elysia is built for this |
| typed TS client contract | Elysia | Eden or Treaty | hand-maintained native shapes | keep product edge honest |
| simple DB-backed CRUD | Elysia + Drizzle | PostgreSQL | Drogon | don't use native compute for basic app semantics |
| report generation with trivial SQL | Elysia + Drizzle | HTMX | Drogon | no need to promote compute too early |
| heavy report generation | C++ core + selected boundary | Elysia shapes the output contract; Drogon if service extraction is warranted | HTMX direct to native | compute lane earns itself here |
| long-running simulation | C++ core + selected boundary | Elysia as public coordinator; Drogon when process/service isolation matters | Elysia-only implementation | classic compute-engine job |
| high-volume transform pipeline | C++ core + selected boundary | FlatBuffers if hot; Drogon when service lifecycle is required | Elysia monolith | compute-specific throughput concern |
| import parse and normalize small payload | Elysia | C++ core if shared parsing exists | Drogon by default | keep simple work simple |
| import parse and normalize huge binary model | C++ core + Drogon | FlatBuffers or native formats | Elysia-only path | heavy native work |
| progress streaming | Drogon or Elysia depending owner | Solid shell renders status | HTMX polling without reason if streaming exists | use the service that owns the work |
| websocket push for public clients | Elysia by default | Drogon underneath if needed | direct compute exposure | edge ownership still matters |
| internal native admin endpoint | Drogon or supervised local process | C++ core | public clients directly | bounded internal territory |
| local utility script with DB access | Bun + Drizzle | Postgres or Turso | Drogon | utility work belongs in the TS lane |
| full-text search ranking | C++ core or Postgres depending complexity | Elysia shapes response | Solid client ranking by default | put ranking where the real complexity is |
| file diff algorithm | C++ core | Elysia or shell host | HTMX | shareable algorithmic core candidate |
| image or model processing | C++ core + Drogon | Wasm for client preview | Elysia-only processing if hot | classic native lane value |
| compute result explanation for product UI | Elysia | Drogon as source | raw native response to clients | public contract and UX semantics stay at the edge |



