# Elm Constitution

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Elm constitution (the interaction engine)

## Elm constitution (the interaction engine)

Elm is a **bounded sovereign**.
if you bring it in, give it law.

### What Elm is for

- deterministic interaction models
- correctness-sensitive feature state
- explicit update transitions
- complex workflows that benefit from TEA
- deep feature islands
- bounded editors, planners, control panels, workflow engines, or state-heavy
  interaction surfaces

### What Elm is not for

- a thin wrapper around DOM calls
- a tiny widget you included because purity is cute
- an interop trampoline for arbitrary browser APIs
- a shell replacement
- a hidden state owner beneath Solid's shell state

### Laws

1. **Elm must own bounded territory.**
2. **TEA is the point.**
   - if the feature does not benefit from Model / View / Update, reconsider
3. **Ports are coarse.**
4. **Flags are for configuration, not casual dependency injection theater.**
5. **Custom elements are okay when the island boundary is honest.**
6. **Do not ask Elm to behave like React with worse marketing.**
7. **Respect the interop limits on purpose.**
   - Elm deliberately chose ports and custom elements over arbitrary JS FFI

### Good Elm territory

- simulation control panel
- deterministic workflow builder
- review or approval engine with explicit transitions
- bounded editor
- decision tree tool
- wizard with complex transitions and validation semantics

### Bad Elm territory

- one isolated button or modal with no real state model
- a feature that mostly wraps existing JS libraries with constant imperative
  escape hatches
- a hypermedia CRUD page

### The Elm island rule

Elm is easiest to keep healthy when:

- Solid or Electrobun shell mounts it
- the island gets coarse initial config
- the island emits coarse events or commands
- side effects cross through a narrow bridge
- the shell does not poke Elm's internal state directly

### Smells

- ports for every tiny UI interaction
- constant JS interop to keep the feature alive
- Elm plus HTMX plus Solid all mutating the same surface
- nobody can name what Elm owns besides "the important part"

bestie, name the important part.


---

### Source section: ## Before touching Elm, ask

## Before touching Elm, ask

- does the feature actually deserve TEA discipline?
- can the boundary stay coarse?
- are ports rare and intentional?
- are we keeping shell and hypermedia owners out of the same surface?
- are we using Elm because it is correct here, not because it sounds virtuous?



