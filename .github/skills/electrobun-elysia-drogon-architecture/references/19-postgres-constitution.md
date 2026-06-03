# Postgres Constitution

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## PostgreSQL constitution (canonical truth)

## PostgreSQL constitution (canonical truth)

PostgreSQL is the default **durable system of record** for this stack.

### What PostgreSQL is for

- authoritative multi-user state
- relational invariants
- transactions
- permissions and policy-relevant data
- job coordination metadata
- durable domain truth
- historical correctness and auditable writes

### What PostgreSQL is not for

- local ephemeral drafts that do not need round trips
- pretending device-local state does not exist
- being bypassed casually by synced local stores for canonical data

### Laws

1. **PostgreSQL is canonical truth by default.**
2. **The more contested and collaborative an entity is, the more it belongs
   here.**
3. **Cross-user invariants belong here.**
4. **Durable permissions and policy-relevant state belong here.**
5. **If a project departs from this default, it must say exactly which entities
   are exceptions.**

### Good PostgreSQL entities

- users
- teams
- permissions
- subscriptions and billing-adjacent records
- shared documents or durable objects
- job metadata
- authoritative domain records

### Smells

- treating Postgres as merely the backup for what actually lives locally
- allowing multiple writers through different services without clear ownership
- confusing read-model copies with canonical ownership


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

### Source section: ## Postgres security

## Postgres security

- canonical truth deserves proper role and policy design
- if RLS is used, keep its ownership clear and tested


---

### Source section: ## Before touching PostgreSQL, ask

## Before touching PostgreSQL, ask

- is this entity truly canonical?
- is a local-first or cached representation also needed nearby?
- are permissions and invariants staying centralized?
- is this change going to hurt latency-sensitive shell flows unnecessarily?
- are we naming the difference between truth, cache, and projection?



