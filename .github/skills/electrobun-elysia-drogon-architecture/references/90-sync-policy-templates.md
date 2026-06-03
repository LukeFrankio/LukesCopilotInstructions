# Sync Policy Templates

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Sync policy templates

## Sync policy templates

the official Turso sync story is explicit enough that projects should also be
explicit.
do not improvise sync semantics in prose after the fact.


---

### Source section: ## Template A: local draft sync policy

## Template A: local draft sync policy

### Best for

- user-authored drafts
- offline-first desktop editing
- staged publish flows

### Ownership

- local working truth while editing: Turso
- canonical published truth: PostgreSQL

### Push policy

- on manual sync
- on explicit publish
- optionally on reconnect

### Pull policy

- on app launch if online
- on manual refresh
- after successful publish if needed

### Merge policy

- draft updates are local
- publish creates or updates canonical object through Elysia
- do not rely on blind last-push-wins for published collaborative fields

### UI obligations

- show dirty state
- show sync pending state
- show last successful sync time


---

### Source section: ## Template B: replicated read model policy

## Template B: replicated read model policy

### Best for

- read-mostly local mirrors
- cached dashboards
- locally searchable views of shared data

### Ownership

- canonical truth: PostgreSQL
- local mirror: Turso

### Push policy

- usually none or very limited

### Pull policy

- on launch
- on reconnect
- on explicit refresh
- optionally on timer

### Merge policy

- remote wins because the local copy is derived

### UI obligations

- show staleness when it matters


---

### Source section: ## Template C: field-capture offline policy

## Template C: field-capture offline policy

### Best for

- intermittent connectivity
- data collection at the edge

### Ownership

- local capture truth until upload succeeds: Turso
- central authoritative truth after ingest: PostgreSQL

### Push policy

- background on reconnect
- user-forced sync option available

### Pull policy

- limited; often reference data and assignment data only

### Merge policy

- submission IDs and ingest rules must prevent accidental duplicate authority

### UI obligations

- clearly show captured locally vs confirmed upstream


---

### Source section: ## Template D: contentious collaborative object policy

## Template D: contentious collaborative object policy

### Best for

- honestly, usually not for naïve last-push-wins

### Ownership

- PostgreSQL canonical
- Turso local cache or draft staging only

### Push policy

- explicit operations through Elysia

### Pull policy

- frequent refresh or subscription-based updates

### Merge policy

- application-defined, not blind sync default

### UI obligations

- conflict resolution UX must be real, not implied


---

### Source section: ## Template E: local queue policy

## Template E: local queue policy

### Best for

- pending uploads
- retryable actions
- local job staging

### Ownership

- Turso stores pending queue
- PostgreSQL stores accepted durable job truth after submission

### Push policy

- on connectivity
- on retry timer
- on user force sync

### Pull policy

- not always necessary beyond status refresh

### Merge policy

- queue item IDs must be idempotent enough to avoid duplicate server truth

### UI obligations

- show queued, retrying, failed, and sent states honestly



