# Workflow Constitutions Part 1

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Concrete workflow constitutions

## Concrete workflow constitutions

these mini-constitutions are useful when teams say "okay but what's the actual
flow?"


---

### Source section: ## Workflow constitution 1: local draft -> review -> publish

## Workflow constitution 1: local draft -> review -> publish

### Goal

let a desktop user work locally, potentially offline, then review and publish to
canonical truth.

### Recommended owners

- shell and local draft UI: Solid
- deep draft-state workflow if complex: Elm
- local storage: Turso
- publish API: Elysia
- canonical truth: PostgreSQL
- heavy validation or transforms: C++ core or Drogon if warranted

### Lawful sequence

1. user edits draft locally
2. draft writes land in Turso or local files first
3. shell exposes sync status and dirty state clearly
4. publish action goes through Elysia
5. Elysia validates public policy and auth
6. heavy transform or compile work delegates to C++ core or Drogon if needed
7. canonical durable record lands in PostgreSQL
8. Turso local state refreshes through explicit pull or local confirmation flow

### Common mistake

- directly treating the local draft as already-published truth and letting server
  reconciliation become vague


---

### Source section: ## Workflow constitution 2: compute job launch -> stream -> inspect

## Workflow constitution 2: compute job launch -> stream -> inspect

### Goal

run a heavy native task while keeping the product edge readable.

### Recommended owners

- launch contract: Elysia
- durable job metadata: PostgreSQL
- execution: C++ core + selected boundary (Drogon when isolation/service is
  warranted)
- status UI: Solid shell or HTMX route depending audience

### Lawful sequence

1. client starts job through Elysia
2. Elysia validates input and policy
3. Elysia records or coordinates job metadata in PostgreSQL
4. Elysia hands the heavy work to Drogon
5. Drogon runs C++ core work
6. progress is exposed through stream or websocket semantics
7. UI consumes progress through Elysia-owned product contract unless the
   architecture explicitly made Drogon public
8. results are shaped back into product semantics

### Common mistake

- letting job-launch response and compute status APIs fracture into separate
  public worlds with no single contract owner


---

### Source section: ## Workflow constitution 3: admin queue triage

## Workflow constitution 3: admin queue triage

### Goal

let operators review, filter, and act on records with low ceremony.

### Recommended owners

- route family: HTMX
- HTML and policy: Elysia
- typed SQL: Drizzle
- canonical truth: PostgreSQL

### Lawful sequence

1. operator opens queue page
2. Elysia renders full page or fragment HTML
3. HTMX issues targeted requests for filters, actions, and updates
4. Elysia validates permissions and shapes fragment responses
5. Drizzle performs TS-lane SQL access
6. PostgreSQL remains canonical

### Common mistake

- rebuilding an admin queue as a mini-SPA for no product reason at all



