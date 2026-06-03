# Product Archetype Playbooks Part 2

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Product archetype playbooks

## Product archetype playbooks

these are example stack shapes that recur a lot.


---

### Source section: ## Archetype E: field data capture tool

## Archetype E: field data capture tool

### Recommended variant

- **local-first synced workstation architecture**

### Core lane map

- shell: Electrobun + Solid
- local data: Turso
- canonical cloud truth: PostgreSQL
- sync API: Elysia
- heavy media or model processing: C++ core or Drogon as needed

### Why it fits

- local-first is the actual product value
- sync semantics matter more than fashionable runtime choices

### Watch-outs

- last-push-wins may not be enough for some entities
- sync health must be visible to users


---

### Source section: ## Archetype F: native compute platform with client companions

## Archetype F: native compute platform with client companions

### Recommended variant

- **compute-first native platform architecture**

### Core lane map

- compute engine: C++ core with explicit boundary choice (often Drogon when
  promoted)
- public edge: Elysia, possibly thinner than default
- desktop client: Electrobun + Solid
- local cache and drafts: Turso if needed
- truth: PostgreSQL

### Why it fits

- native compute is the center of value
- multiple clients may consume the same native service lane

### Watch-outs

- public-contract sovereignty must still be explicit
- don't accidentally run two public backends with overlapping semantics


---

### Source section: ## Archetype G: creative desktop editor with occasional server sync

## Archetype G: creative desktop editor with occasional server sync

### Recommended variant

- **default federation** leaning local-first

### Core lane map

- shell: Electrobun + Solid
- deterministic editor state: Elm if the editor deserves it
- local project storage: Turso and files
- canonical publish state: Postgres
- heavy processing: C++ core
- web preview path: Wasm if needed

### Why it fits

- desktop affordances matter
- local state matters
- shared-core portability matters

### Watch-outs

- do not over-centralize ephemeral editor state in the backend
- do not let the shell own the editor's entire internal truth


---

### Source section: ## Archetype H: product shell with heavy internal admin console

## Archetype H: product shell with heavy internal admin console

### Recommended variant

- **default federation** with strong HTMX bounded lane

### Core lane map

- user-facing shell: Solid
- deep feature island(s): optional Elm
- internal staff tooling: HTMX + Elysia HTML
- contract and DB: Elysia + Drizzle + Postgres

### Why it fits

- one stack can serve both a polished shell and server-driven operations tooling

### Watch-outs

- make route ownership obvious
- do not let admin route idioms leak into the interactive product core



