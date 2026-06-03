# Solid Constitution

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## SolidJS constitution (the shell brain)

## SolidJS constitution (the shell brain)

Solid is the default **shell UI owner**.

### What Solid is for

- app chrome
- route shell
- navigation bars and sidebars
- transient UI state
- notifications
- shell-level status indicators
- component composition
- embedding Elm or HTMX-governed territories cleanly
- responsive desktop UI around native shell features

### What Solid is not for

- owning every meaningful state machine by inertia
- becoming a universal store monarchy
- swallowing Elm territory because it happens to be nearby
- rendering server-authored CRUD pages that HTMX would do more cleanly

### Laws

1. **Solid owns the shell.**
2. **Shell state is not the same as domain state.**
3. **If a feature wants TEA-level discipline, let Elm own it.**
4. **If a route wants server-authored HTML, let HTMX own it.**
5. **Solid components may host islands; they must not blur island ownership.**
6. **Cross-cutting UI belongs here.**
   - theme
   - layout
   - menus
   - toasts
   - connection status
   - desktop affordance wrappers

### Good Solid state

- layout mode
- active panel
- selected shell tab
- menu visibility
- global notification center
- connectivity badge
- current workspace chrome

### Bad Solid state

- complex transactional wizard state if Elm exists for that job
- authoritative document model for a deep editor while Elm or C++ also claim it
- long-term sync conflict resolution state that belongs in local-first logic

### Smells

- a global Solid store that quietly becomes the application's actual sovereign
- components reaching through every feature boundary
- shell concerns and domain concerns interleaving until nothing has a clean home


---

### Source section: ## Before touching Solid, ask

## Before touching Solid, ask

- is this shell state or domain state?
- does this belong to a bounded feature island instead?
- is this route actually HTMX territory?
- are we creating a new global store habit we will regret later?
- does this preserve the shell's role as host rather than empire?



