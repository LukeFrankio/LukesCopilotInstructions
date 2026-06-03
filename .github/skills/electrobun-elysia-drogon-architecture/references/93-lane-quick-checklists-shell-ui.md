# Lane Quick Checklists Shell UI

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Lane quick-checklists (for when the team is tired and needs the short version)

## Lane quick-checklists (for when the team is tired and needs the short version)

these are the panic cards.
use them during implementation reviews, not just architecture summits.


---

### Source section: ## Before touching Electrobun, ask

## Before touching Electrobun, ask

- is this truly a shell concern?
- does this require desktop-native affordance?
- are we adding a clean bridge or a random shortcut?
- does this affect packaging, update flow, or code-signing assumptions?
- are we accidentally moving domain logic into the shell host?


---

### Source section: ## Before touching Solid, ask

## Before touching Solid, ask

- is this shell state or domain state?
- does this belong to a bounded feature island instead?
- is this route actually HTMX territory?
- are we creating a new global store habit we will regret later?
- does this preserve the shell's role as host rather than empire?


---

### Source section: ## Before touching Elm, ask

## Before touching Elm, ask

- does the feature actually deserve TEA discipline?
- can the boundary stay coarse?
- are ports rare and intentional?
- are we keeping shell and hypermedia owners out of the same surface?
- are we using Elm because it is correct here, not because it sounds virtuous?


---

### Source section: ## Before touching HTMX, ask

## Before touching HTMX, ask

- is this truly a hypermedia-friendly surface?
- does the route have named territory?
- can the pushed URL return a full page?
- have we considered `HX-Request` caching variation?
- are we avoiding DOM warfare with client-owned islands?


---

### Source section: ## Before touching Tailwind, ask

## Before touching Tailwind, ask

- is this using the shared design token system?
- are we repeating a utility blob that should become an abstraction?
- are we accidentally encoding workflow semantics in class names?
- is the styling consistent across Solid, Elm, and HTMX surfaces?
- are we preserving accessibility and state clarity, not just visual neatness?



