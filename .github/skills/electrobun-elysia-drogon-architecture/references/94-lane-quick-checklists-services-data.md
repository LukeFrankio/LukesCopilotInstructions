# Lane Quick Checklists Services Data

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Lane quick-checklists (for when the team is tired and needs the short version)

## Lane quick-checklists (for when the team is tired and needs the short version)

these are the panic cards.
use them during implementation reviews, not just architecture summits.


---

### Source section: ## Before touching Elysia, ask

## Before touching Elysia, ask

- is this edge contract work or compute creep?
- does this route shape a public HTML or JSON contract?
- should this delegate to Drogon or shared core instead?
- are auth and policy still centralized here?
- are we preserving a clean public story instead of tunneling internal weirdness?


---

### Source section: ## Before touching Drizzle, ask

## Before touching Drizzle, ask

- is this a TS-lane schema or migration concern?
- did we consider the current Drizzle release behavior or migration engine state?
- are we treating Drizzle as access strategy rather than universal law?
- does this change affect Postgres ownership or Turso sync semantics?
- would the native lane be better served by a different contract abstraction?


---

### Source section: ## Before touching PostgreSQL, ask

## Before touching PostgreSQL, ask

- is this entity truly canonical?
- is a local-first or cached representation also needed nearby?
- are permissions and invariants staying centralized?
- is this change going to hurt latency-sensitive shell flows unnecessarily?
- are we naming the difference between truth, cache, and projection?


---

### Source section: ## Before touching Turso, ask

## Before touching Turso, ask

- is this local-first state or just a cache?
- when will we `push()` and `pull()`?
- is last-push-wins acceptable here?
- how will the user see sync health or staleness?
- are we accidentally creating a shadow source of truth?


---

### Source section: ## Before touching Drogon, ask

## Before touching Drogon, ask

- is this genuinely native compute or throughput work?
- should the public edge still stay in Elysia?
- is the shared C++ core the real owner of the logic?
- are we about to expose another public contract by accident?
- how will progress, failure, and retries be observed?



