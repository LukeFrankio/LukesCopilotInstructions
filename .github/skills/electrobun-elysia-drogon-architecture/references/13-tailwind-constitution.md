# Tailwind Constitution

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Tailwind CSS constitution (the one visual dialect)

## Tailwind CSS constitution (the one visual dialect)

Tailwind is not the architecture.
Tailwind is the **visual grammar** of the stack.
that matters more than people admit.

### What Tailwind is for

- fast, consistent styling across UI lanes
- a shared design token layer
- consistent spacing, type, layout, and component rhythm across Solid, Elm DOM,
  and HTMX fragments
- reducing CSS divergence between shell, hypermedia, and bounded islands

### What Tailwind is not for

- encoding business logic in class-name soups
- becoming the only place responsive or semantic thinking happens
- fragmenting into one utility style in HTMX and another in Solid and another in
  Elm

### Laws

1. **There is one design system for the whole stack.**
   - not a Tailwind dialect per lane
2. **Extract repeated patterns.**
   - do not let the app become `class="px-2 py-1 ..."` archaeology forever
3. **Tokens first.**
   - colors, spacing, radii, shadows, typography, and state colors should have a
     coherent design intent
4. **Use Tailwind to unify UI lanes, not to hide them.**
5. **Never encode ownership confusion in shared utility patterns.**
   - a button style can be shared
   - a domain workflow should not become a CSS convention

### Good Tailwind use

- common form styles across HTMX and Solid
- consistent panels and cards in shell and ops views
- stable spacing system across desktop shell and fragments
- state tokens for success, warning, sync, compute, offline, and destructive
  actions

### Smells

- every lane invents its own component vocabulary
- copy-paste utility blobs with no abstraction or token discipline
- semantic state living in class strings rather than component or route logic


---

### Source section: ## Before touching Tailwind, ask

## Before touching Tailwind, ask

- is this using the shared design token system?
- are we repeating a utility blob that should become an abstraction?
- are we accidentally encoding workflow semantics in class names?
- is the styling consistent across Solid, Elm, and HTMX surfaces?
- are we preserving accessibility and state clarity, not just visual neatness?



