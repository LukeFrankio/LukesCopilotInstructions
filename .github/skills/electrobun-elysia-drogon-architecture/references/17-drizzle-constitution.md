# Drizzle Constitution

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Drizzle constitution (typed SQL in the TS lane)

## Drizzle constitution (typed SQL in the TS lane)

Drizzle is the **TypeScript persistence specialist** of this stack.

### What Drizzle is for

- schema declaration in the TS lane
- migrations in the TS lane
- typed SQL access from Elysia and TS-side services or utilities
- coordinating TS-side access to PostgreSQL, Turso, and related supported
  backends
- keeping Elysia and Bun-side database access explicit and structured

### What Drizzle is not for

- defining the one true schema for C++, Wasm, Elm, and every other lane by force
- replacing thoughtful data contracts between TS and native systems
- becoming a theology where every part of the system must imitate the TS DSL

### Drizzle reality check

the official site and release cadence show a project that:

- ships fast
- adds features aggressively
- evolves migration behavior meaningfully
- has a current 1.0 beta story
- has changed validator packaging and dialect coverage over time
- is increasingly broad across dialects and runtimes

this is good.
it also means you should govern it consciously.

### Laws

1. **Drizzle owns typed SQL in the TS lane.**
2. **Do not universalize Drizzle concepts into the native lane unless doing so is
   clearly worth it.**
3. **Migration policy must be explicit.**
4. **Keep Drizzle upgrades and migration-engine changes under review.**
5. **Let PostgreSQL remain the data truth and Drizzle remain the TS access
   strategy.**
6. **Use Drizzle with Turso where it earns its keep, but do not let that erase the
   sync semantics.**
7. **Use Drizzle's RLS and dialect support thoughtfully where it aligns with
   Postgres policy.**

### Good Drizzle territory

- Elysia handlers and service modules
- admin jobs and operational scripts in Bun
- TS-side migrations and schema evolution
- typed DB access for HTML fragment routes and JSON APIs

### Bad Drizzle territory

- hot native compute loops
- binary contract definitions
- cross-language shared-core replacement

### Smells

- everyone starts saying "the Drizzle schema" when they really mean "the TS lane's
  SQL schema"
- native C++ re-derives business rules from Drizzle-generated artifacts without
  a proper contract
- Drizzle upgrade churn silently changes migration behavior with no review


---

### Source section: ## Drizzle to Postgres seam

## Drizzle to Postgres seam

### Good

- Drizzle models TS-lane access honestly
- Postgres remains authoritative
- migrations are governed and reviewed

### Bad

- application truth is treated as identical to generated TS schema metaphors
- native lane learns about truth only through Drizzle wrappers

### Law

Drizzle is access strategy, not metaphysical sovereignty.


---

### Source section: ## Before touching Drizzle, ask

## Before touching Drizzle, ask

- is this a TS-lane schema or migration concern?
- did we consider the current Drizzle release behavior or migration engine state?
- are we treating Drizzle as access strategy rather than universal law?
- does this change affect Postgres ownership or Turso sync semantics?
- would the native lane be better served by a different contract abstraction?



