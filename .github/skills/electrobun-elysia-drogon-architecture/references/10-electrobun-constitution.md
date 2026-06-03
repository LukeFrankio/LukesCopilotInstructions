# Electrobun Constitution

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Electrobun constitution (the shell sovereign)

## Electrobun constitution (the shell sovereign)

Electrobun is the **desktop host government**.

### What Electrobun is for

- window lifecycle
- system integration
- tray, menus, context menus
- BrowserWindow and BrowserView hosting
- app packaging and distribution
- updater orchestration
- native-feeling desktop affordances
- bundling views and resources
- desktop-specific bridge surfaces

### What Electrobun is not for

- becoming the main domain rules engine
- replacing Elysia as the public contract layer
- replacing Drogon as the compute service
- inventing random direct native bridges from every screen
- smearing native shell logic through all product code

### Laws

1. **Electrobun owns shell concerns.**
2. **Use system webview by default.**
   - the docs clearly position system webview as the default and CEF as optional
3. **Enable CEF only for actual browser-platform gaps.**
   - not for speculative comfort
4. **Keep the Bun worker / native wrapper split in mind.**
   - the official architecture uses the native GUI event loop on the main thread
     and app logic in a worker
5. **Bridge intentionally.**
   - postMessage, FFI, or approved APIs
   - not ad hoc side channels all over the place
6. **Exploit the updater if the product ships desktop updates often.**
   - tiny patches are one of Electrobun's real superpowers
7. **Respect distribution-time concerns.**
   - code signing
   - notarization
   - artifacts
   - static hosting of updates
8. **Treat Electrobun as a strategic dependency, not an untouchable identity.**
9. **Maintain shell escape seams.**

- isolate host APIs behind an adapter boundary
- keep renderer logic portable enough that a host swap is painful but possible

### Good Electrobun territory

- top-level shell state
- windows and multi-view orchestration
- desktop menus and accelerators
- file picker and local FS affordances
- updater lifecycle
- OS-specific integration
- native drag regions
- desktop-only WebGPU or view hosting concerns

### Smells

- business workflows depending on shell-specific APIs everywhere
- every feature getting its own special native bridge
- updater concerns leaking into product logic
- desktop packaging structure being treated like a domain abstraction

### Electrobun maturity and contingency law

Electrobun has compelling strengths, but it is also a younger ecosystem bet than
older desktop shells.

that does **not** mean "do not use Electrobun."
it means "use it with explicit contingency discipline."

required safeguards:

1. keep a host-adapter seam for native affordances
2. avoid scattering Electrobun-specific calls through domain code
3. keep route and feature logic shell-portable where practical
4. document what a host migration would touch first

if these safeguards are ignored, the shell choice stops being a tool decision and
becomes a lock-in event.

### Electrobun migration readiness checklist

keep this checklist green continuously, not only when panic starts:

- [ ] host-specific APIs are wrapped behind an internal adapter module
- [ ] renderer code avoids direct dependency on host internals except at adapter
  edges
- [ ] key workflows can run in a non-Electrobun dev surface for contingency
  testing
- [ ] packaging assumptions are documented separately from domain architecture
- [ ] update mechanism dependencies are isolated from product-domain logic

### Electrobun risk trigger thresholds

if two or more of the following persist across release cycles, open a formal
contingency ADR:

1. repeated breaking changes with no practical migration path
2. unresolved platform regressions on required OS targets
3. release velocity stalls against project roadmap needs
4. critical upstream issues blocking security or distribution requirements
5. team cannot execute shell upgrades within acceptable release windows

the goal is not to abandon Electrobun preemptively.
the goal is to avoid waking up with no realistic options.

### Electrobun packaging law

because the docs show real structure and update behavior, respect these truths:

- the desktop bundle is a real platform artifact, not just a JS folder
- the updater relies on hashes and patch chains
- distribution and dev builds differ materially
- non-dev builds produce artifacts with long-term operational consequences

if the product is desktop-first, release engineering is part of architecture,
not an afterthought.


---

### Source section: ## Electrobun security

## Electrobun security

- code signing and notarization are part of trust, not optional flavor text, when
  shipping real desktop builds
- keep secrets out of bundled client assets
- treat updater artifacts as part of supply-chain hygiene


---

### Source section: ## Electrobun observability

## Electrobun observability

- remember dev launcher output and native event visibility in development
- update hashes and artifact behavior are observable architecture, not just build
  trivia


---

### Source section: ## Before touching Electrobun, ask

## Before touching Electrobun, ask

- is this truly a shell concern?
- does this require desktop-native affordance?
- are we adding a clean bridge or a random shortcut?
- does this affect packaging, update flow, or code-signing assumptions?
- are we accidentally moving domain logic into the shell host?



