# Turso Constitution

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Turso Sync constitution (local-first truth with explicit humility)

## Turso Sync constitution (local-first truth with explicit humility)

Turso is a **local-first operational store**, not default universal truth.

### What Turso is for

- local reads and writes
- offline work
- device-local drafts
- synced projections
- cached subsets of canonical data
- field or desktop workflows that should not block on the network
- edge-adjacent or user-adjacent state

### What Turso is not for

- hidden multi-user canonical truth
- a casual replacement for PostgreSQL
- conflict-free magic when the official model is explicitly last-push-wins

### Laws

1. **Turso sync is explicit.**
   - `push()`
   - `pull()`
   - not telepathy
2. **Local writes are safe, but not magically canonical.**
3. **If offline-first startup matters, configure bootstrap behavior on purpose.**
4. **Checkpoint and stats matter.**
   - WAL growth is not a decorative metric
5. **Do not let contentious collaborative writes use naïve last-push-wins if that
   would hurt product semantics.**
6. **Partition what belongs in Turso carefully.**

### Good Turso entities

- local drafts
- cached work queues
- device-local settings
- replicated read models
- local notes and staging data
- offline task state
- local projections for speed

### Bad Turso entities by default

- financial truth
- cross-user permissions
- heavily contested collaborative objects
- canonical ledger-like state

### Smells

- no explicit sync schedule
- no user-visible sync health state
- no answer for conflict semantics
- treating local state as canonical because it is faster


---

### Source section: ## Postgres versus Turso decision law

## Postgres versus Turso decision law

for each entity, answer these questions explicitly:

- where is the authoritative durable record?
- can users edit it offline?
- is last-push-wins acceptable?
- who merges or rejects conflicts?
- is Turso storing a projection, a draft, a local-first canonical subset, or a
  cache?
- what happens after the first launch when the remote is unreachable?

if the answers are vague, the data topology is not done.


---

### Source section: ## Turso observability

## Turso observability

- track push and pull timings
- watch WAL sizes and sync failures
- expose sync health to the shell when user trust depends on it


---

### Source section: ## Before touching Turso, ask

## Before touching Turso, ask

- is this local-first state or just a cache?
- when will we `push()` and `pull()`?
- is last-push-wins acceptable here?
- how will the user see sync health or staleness?
- are we accidentally creating a shadow source of truth?



