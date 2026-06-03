# Migration Playbooks Part 2

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Migration playbooks

## Migration playbooks

use these when the project grows or changes shape instead of pretending the first
architecture guess was eternal.


---

### Source section: ## Playbook 5: unifying duplicate native and web logic into a shared core

## Playbook 5: unifying duplicate native and web logic into a shared core

### Trigger

- TS and C++ versions of the same logic keep drifting

### Safe move

1. identify the truly shared logic
2. move it into modern C++ core
3. compile native and Wasm targets from the same source
4. define a coarse host boundary
5. delete duplicate sibling logic aggressively

### Unsafe move

- keeping the old duplicate implementations around "just in case"


---

### Source section: ## Playbook 6: adding FlatBuffers to an already-working JSON path

## Playbook 6: adding FlatBuffers to an already-working JSON path

### Trigger

- profiling proves the boundary is hot enough

### Safe move

1. scope FlatBuffers to the hot internal boundary only
2. create one translation layer
3. keep public JSON or HTML untouched
4. add compatibility tests

### Unsafe move

- converting every contract in sight to binary because one path got hot


---

### Source section: ## Playbook 7: centralizing shader truth under Slang

## Playbook 7: centralizing shader truth under Slang

### Trigger

- raw shader sources are diverging across targets

### Safe move

1. declare Slang authoring canon
2. define module boundaries
3. generate or validate WGSL as a target output
4. keep capability and fallback policy explicit

### Unsafe move

- keeping hand-edited WGSL and HLSL twins forever


---

### Source section: ## Playbook 8: reasserting Elysia as public edge after native creep

## Playbook 8: reasserting Elysia as public edge after native creep

### Trigger

- clients started consuming compute-native endpoints directly

### Safe move

1. audit client entry points
2. consolidate public contract in Elysia
3. keep Drogon internal unless a conscious public split is wanted
4. normalize auth and error policy at the edge

### Unsafe move

- letting legacy direct clients dictate permanent dual-sovereign architecture by
  inertia



