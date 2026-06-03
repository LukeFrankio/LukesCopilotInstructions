# Migration Playbooks Part 1

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Migration playbooks

## Migration playbooks

use these when the project grows or changes shape instead of pretending the first
architecture guess was eternal.


---

### Source section: ## Playbook 1: adding HTMX to a Solid-heavy app

## Playbook 1: adding HTMX to a Solid-heavy app

### Trigger

- too many forms and ops pages are being implemented with SPA ceremony

### Safe move

1. name HTMX territory explicitly
2. keep the shell in Solid
3. add Elysia fragment routes
4. ensure full-page responses exist for pushed URLs
5. standardize Tailwind tokens across the new route family

### Unsafe move

- sprinkling HTMX fragments into existing client-owned feature bodies without a
  route boundary


---

### Source section: ## Playbook 2: promoting one feature from Solid to Elm

## Playbook 2: promoting one feature from Solid to Elm

### Trigger

- one feature becomes state-machine-heavy, bug-prone, or correctness-sensitive

### Safe move

1. isolate the feature surface
2. define the Elm-owned model boundaries
3. keep ports coarse
4. keep server calls going through Elysia
5. remove duplicate state ownership from Solid

### Unsafe move

- embedding Elm while keeping the old Solid store as co-owner


---

### Source section: ## Playbook 3: extracting Drogon from Elysia compute bloat

## Playbook 3: extracting Drogon from Elysia compute bloat

### Trigger

- Elysia handlers are now doing serious heavy work

### Safe move

1. identify the compute kernels
2. move them into C++ core where shared value exists
3. expose them through Drogon
4. keep Elysia as public contract owner
5. translate internal errors and progress semantics back at the edge

### Unsafe move

- splitting handlers across Elysia and Drogon by whim rather than by workload


---

### Source section: ## Playbook 4: introducing local-first state with Turso

## Playbook 4: introducing local-first state with Turso

### Trigger

- users need to work offline or latency is hurting the product

### Safe move

1. classify which entities can be local-first
2. define canonical ownership in Postgres
3. implement explicit push and pull lifecycle
4. expose sync status in the shell
5. test bootstrap, conflict, reconnect, restart, and WAL behavior

### Unsafe move

- turning on sync and assuming semantics will sort themselves out later



