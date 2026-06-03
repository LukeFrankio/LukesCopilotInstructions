# Version And Drift Policy

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Version stance (bleeding edge with eyes open)

## Version stance (bleeding edge with eyes open)

this stack is alive and moving.
treat stale assumptions like expired milk.

### Current orientation as of 2026-06

- **Electrobun**
  - prefer the latest stable **1.18.x** line or newer beta if the needed feature
    is only there
  - the release stream is active enough that packaging and updater behavior must
    be re-checked when bumping
  - treat ecosystem maturity as an explicit architectural risk input; keep a host
    adapter seam so migration to another shell runtime is possible if project
    velocity or compatibility regresses
- **Bun**
  - prefer latest **1.2+** line or newer
  - Bun is central enough to the stack that runtime and driver compatibility are
    first-class architectural concerns
- **Elysia**
  - prefer latest release compatible with current Bun line
  - docs updated recently enough that runtime and plugin stories keep evolving
- **htmx**
  - default to **2.x**, not 1.x, unless legacy browser support is an explicit
    requirement
- **Drizzle**
  - prefer latest stable or current 1.0 beta line if features or fixes require
    it
  - beware of migration-engine churn, validator package changes, and dialect
    behavior shifts
- **Slang**
  - prefer latest Khronos-governed release line and check target backend support
    before assuming a feature compiles cleanly to WGSL
- **Emscripten**
  - prefer latest SDK line with the browser targets you actually ship against
- **PostgreSQL**
  - prefer modern supported major releases and do not architect around antique
    dialect assumptions
- **Turso**
  - prefer latest sync tooling and libsql-compatible client versions in the TS
    lane

### Version law

if a project in this stack pins old versions for comfort, that pin must be
explained in writing.

### Drift law

when updating any of these:

- Bun
- Elysia
- Drizzle
- Electrobun
- Slang
- Emscripten
- Turso

re-check:

- deployment assumptions
- compatibility notes
- build flags
- contract generators
- migration behavior
- sync behavior
- output or packaging paths

this stack rewards staying current.
it also punishes cargo-cult copy-paste from six months ago.



