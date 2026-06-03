# Elm Centric Architecture

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Alternative architecture 2: Elm-Centric Deterministic Product Architecture

## Alternative architecture 2: Elm-Centric Deterministic Product Architecture

this variant promotes Elm from bounded interaction engine to **primary product
interaction architecture** for most important user-facing surfaces.

### Summary

- Electrobun + Solid still own the outer shell
- Elm owns much more of the actual product UI
- HTMX is demoted to admin or secondary ops surfaces
- Elysia still owns the public contract
- Drogon and C++ stay as compute layers

### Use this when

- the product's value lives in correctness-sensitive workflows
- the UI is effectively a state machine
- undo/redo, replayability, determinism, and explicit state transitions matter a
  lot
- the team is willing to respect Elm's interop limitations instead of fighting
  them with passive-aggressive port abuse

### Avoid this when

- the product is mostly document, CRUD, or admin flows
- the team actually wants casual JS interop everywhere
- the team is not prepared to think in bounded TEA surfaces
- the product spends more time rendering server-authored documents than it does
  driving deep state

### Mandatory laws

1. **Elm must own real territory.**
   - not just a tiny form
   - not just one tab because someone likes purity
2. **Ports stay coarse.**
   - command in
   - result out
   - event out
   - config in
   - avoid tiny chatty message spam across the boundary
3. **Do not treat Elm as a generic JS helper.**
4. **If a feature needs arbitrary browser or library access all day, maybe it is
   not an Elm feature.**
5. **Solid hosts; Elm governs.**
   - the shell may mount or unmount
   - the shell does not micromanage internal Elm state
6. **HTMX stays out of Elm-governed surfaces.**
   - the island boundary must be crisp

### Why this can be better than the default

because some products are just screaming for explicit state machines.
if the important surfaces look like editors, simulators, planners, or guided
workflow engines, Elm can reduce bug classes the rest of the stack cannot.

### Why this can be worse than the default

because Elm interop is intentionally constrained.
if the product wants constant direct entanglement with arbitrary JS widgets,
random browser APIs, or ad hoc framework glue, Elm becomes a pain tax instead of
a superpower.



