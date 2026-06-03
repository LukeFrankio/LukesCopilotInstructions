# Failure Mode Catalog

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Failure mode catalog (aka how this stack usually betrays careless teams)

## Failure mode catalog (aka how this stack usually betrays careless teams)


---

### Source section: ## Failure mode 1: shell inflation

## Failure mode 1: shell inflation

### Symptom

- shell components keep gaining domain logic

### Root cause

- Solid or Electrobun is nearby, so people stop respecting deeper owners

### Corrective move

- move domain rules back to Elm, Elysia, or shared core depending the concern


---

### Source section: ## Failure mode 2: gateway obesity

## Failure mode 2: gateway obesity

### Symptom

- Elysia handlers become the de facto domain monolith

### Root cause

- every request passes there, so it becomes the easiest dumping ground

### Corrective move

- separate contract work from compute and shared-core logic again


---

### Source section: ## Failure mode 3: fake local-first

## Failure mode 3: fake local-first

### Symptom

- the app advertises offline support but sync behavior is mysterious and fragile

### Root cause

- Turso was added as a feature checkbox, not a governed lane

### Corrective move

- define entity ownership, sync triggers, failure UI, and conflict policy


---

### Source section: ## Failure mode 4: duplicate public backends

## Failure mode 4: duplicate public backends

### Symptom

- clients hit Elysia and Drogon for overlapping concerns

### Root cause

- compute endpoints escaped into product usage

### Corrective move

- restore Elysia sovereignty or explicitly split the public architecture


---

### Source section: ## Failure mode 5: fragment civil war

## Failure mode 5: fragment civil war

### Symptom

- HTMX and client-owned state keep fighting over the same subtree

### Root cause

- no territory map

### Corrective move

- move to route-scoped ownership or bounded islands


---

### Source section: ## Failure mode 6: ceremonial Elm

## Failure mode 6: ceremonial Elm

### Symptom

- a lot of ports, not much real Elm value

### Root cause

- feature never really justified Elm ownership

### Corrective move

- either enlarge the territory honestly or demote the lane


---

### Source section: ## Failure mode 7: shared core mythology

## Failure mode 7: shared core mythology

### Symptom

- multiple implementations keep diverging

### Root cause

- nobody forced one source of truth

### Corrective move

- consolidate into C++ core and delete sibling rewrites


---

### Source section: ## Failure mode 8: binary creep

## Failure mode 8: binary creep

### Symptom

- FlatBuffers show up in boring product paths

### Root cause

- one hot boundary justified binary and the discipline stopped there

### Corrective move

- re-limit binary formats to hot internal seams


---

### Source section: ## Failure mode 9: shader drift

## Failure mode 9: shader drift

### Symptom

- target-specific shader versions disagree or break unexpectedly

### Root cause

- no source-of-truth declaration under Slang

### Corrective move

- centralize authoring and target generation policy


---

### Source section: ## Failure mode 10: build-graph dishonesty

## Failure mode 10: build-graph dishonesty

### Symptom

- nobody can explain how native, Wasm, and shell assets are really produced

### Root cause

- package scripts became architecture instead of tooling

### Corrective move

- restore CMake and Bun as honest authorities over their own lanes



