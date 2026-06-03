# Feature Placement Atlas Data

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Feature placement atlas

## Feature placement atlas

this section is intentionally blunt.
if a new piece of work arrives, use these tables before inventing a fourth owner.


---

### Source section: ## Data ownership matrix

## Data ownership matrix

| Data kind | Canonical owner | Local or secondary owner | Forbidden default assumption | Notes |
| --- | --- | --- | --- | --- |
| users | PostgreSQL | Turso cached subset if needed | Turso as system-of-record | multi-user durable truth |
| organizations or teams | PostgreSQL | none or read replicas | Turso authority | relational shared truth |
| permissions and roles | PostgreSQL | local cache only | device-local authority | policy-critical data |
| billing records | PostgreSQL | none | local-first write truth | canonical and auditable |
| user profile cache | PostgreSQL | Turso local projection | Turso canonical | projection is okay, truth stays central |
| local draft document | Turso or local file + Turso metadata | PostgreSQL eventual publish target | Postgres required for every keystroke | local-first territory |
| published collaborative document | PostgreSQL | Turso local working copy | Turso canonical without merge policy | shared durable object |
| sync health stats | Turso local stats + shell state | optional server aggregation | Postgres-only visibility | user trust depends on local visibility |
| app settings global | PostgreSQL if cross-device | Turso local mirror | one unnamed truth | decide per scope |
| app settings device-local | Turso or local config | optional cloud backup | PostgreSQL-only semantics | device concern |
| job definitions | PostgreSQL | Turso local queue cache if needed | Turso primary for shared jobs | collaborative system state |
| job progress ephemeral local view | Turso or shell memory | PostgreSQL or Elysia stream as source | Postgres round-trip for every paint | local UX concern |
| audit log | PostgreSQL | local cached window | Turso canonical | server truth |
| recent activity cache | Turso | PostgreSQL source | canonical local activity | fast local read model |
| feature flags | PostgreSQL | Turso cached subset | per-device truth by accident | policy-ish shared state |
| large model asset metadata | PostgreSQL | Turso local cache | local file = authority | metadata is canonical even if assets are local |
| local workspace catalog | Turso | optional remote sync | Postgres-only if purely device-local | workstation concern |
| search index shards | depends on architecture | Turso local index or native index | Postgres as the only performance answer | this is derived data |
| shader cache | local filesystem or Turso metadata | optional remote invalidation info | PostgreSQL as shader cache truth | build/runtime artifact territory |
| compiled Wasm artifact manifest | release pipeline storage | local cache | app DB tables as artifact truth | deployment artifact concern |
| Electrobun version manifest | release static host | local version.json | Postgres business DB | updater architecture, not domain DB |



