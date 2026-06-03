# Pr Review Rubrics By Lane

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Pull request review rubric by lane

## Pull request review rubric by lane

use these review questions so the stack does not drift one "quick fix" at a
time.


---

### Source section: ## Shell PRs (Electrobun, Solid, Tailwind)

## Shell PRs (Electrobun, Solid, Tailwind)

- did this change stay in shell territory?
- did it accidentally absorb domain rules?
- is Tailwind usage consistent with shared design tokens?
- does a new desktop bridge belong in Electrobun, or is it a one-off shortcut?
- did the PR preserve route or island ownership clarity?


---

### Source section: ## Elm PRs

## Elm PRs

- does the feature still clearly justify Elm?
- are ports coarse and intentional?
- did shell state remain outside Elm internals unless explicitly bridged?
- did the PR avoid HTMX or Solid ownership conflicts on the same surface?
- are state transitions still explicit and testable?


---

### Source section: ## HTMX PRs

## HTMX PRs

- is the route family named territory?
- are full-page responses valid where history or pushed URLs are used?
- did the PR handle `HX-Request` or caching variation correctly?
- is server validation authoritative?
- did the PR avoid embedding fragments into client-owned state zones?


---

### Source section: ## Elysia PRs

## Elysia PRs

- is this public contract work or compute creep?
- are schema and validation changes explicit?
- does the API shape stay product-friendly instead of reflecting internal quirks?
- if HTMX is involved, are fragment and full-page semantics both handled?
- if Drogon is called, is the boundary still clean and observable?


---

### Source section: ## Drizzle and Postgres PRs

## Drizzle and Postgres PRs

- is the migration strategy explicit?
- did the change accidentally alter canonical data ownership?
- is this TS-lane access logic, not native-lane theology?
- if RLS or roles are touched, are policy implications reviewed?
- if Turso sync is involved, are conflict implications documented?


---

### Source section: ## Turso PRs

## Turso PRs

- what entities are local-first now?
- what is the sync lifecycle?
- what does last-push-wins mean here?
- are stats and checkpoint behavior still considered?
- does the shell surface sync health honestly?


---

### Source section: ## Drogon and C++ PRs

## Drogon and C++ PRs

- is this truly compute or shared-core work?
- could this logic belong in the C++ core rather than Drogon glue?
- is the public contract still owned by Elysia unless consciously changed?
- are concurrency and streaming behaviors observable and testable?
- did we accidentally duplicate logic already present elsewhere?


---

### Source section: ## Wasm and FlatBuffers PRs

## Wasm and FlatBuffers PRs

- is the boundary coarse enough?
- is the binary format justified by heat or volume?
- are compatibility tests present?
- did the PR avoid leaking binary complexity to public clients?
- is the shared-core story stronger after this change, or weaker?


---

### Source section: ## GPU PRs

## GPU PRs

- is Slang still source truth?
- are WGSL or other target artifacts generated or governed properly?
- are capability restrictions explicit?
- is there a fallback story?
- did the PR keep product logic out of the GPU lane?



