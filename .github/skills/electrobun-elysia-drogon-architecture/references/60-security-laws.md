# Security Laws

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Security laws for this stack

## Security laws for this stack


---

### Source section: ## Public contract security

## Public contract security

- auth policy should be centralized in Elysia by default
- public error semantics should be deliberate
- do not let compute-internal details leak directly to product clients


---

### Source section: ## HTMX security

## HTMX security

- escape untrusted HTML
- use `hx-disable` around risky injected raw content if needed
- configure same-origin request policy appropriately
- remember CSRF headers or form strategies on server-rendered flows
- do not let `HX-Request` shape variation break caches or history semantics


---

### Source section: ## Electrobun security

## Electrobun security

- code signing and notarization are part of trust, not optional flavor text, when
  shipping real desktop builds
- keep secrets out of bundled client assets
- treat updater artifacts as part of supply-chain hygiene


---

### Source section: ## Turso security

## Turso security

- tokens are secrets
- local-first does not mean careless credentials
- device-local databases may still require at-rest protections depending on the
  domain


---

### Source section: ## Postgres security

## Postgres security

- canonical truth deserves proper role and policy design
- if RLS is used, keep its ownership clear and tested


---

### Source section: ## Wasm and native security

## Wasm and native security

- a compiled core is not automatically safer because it is compiled
- validate boundaries
- keep binary schema and memory assumptions explicit



