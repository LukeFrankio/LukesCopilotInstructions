# HTMX Constitution

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## HTMX constitution (the hypermedia lane)

## HTMX constitution (the hypermedia lane)

HTMX is **not** the fallback when people feel tired.
HTMX is a real architectural lane.

### What HTMX is for

- server-authored HTML fragments
- CRUD pages
- forms
- reports
- queues
- approval panels
- settings pages
- document-centric workflows
- progressive enhancement where it actually matters
- small islands of behavior driven by events and HTML semantics

### What HTMX is not for

- re-implementing a SPA badly
- becoming the secret default because nobody wanted to make a routing decision
- owning the same feature surface as Elm or Solid state logic
- shoving raw user HTML into the DOM without sanitation or `hx-disable`

### Laws

1. **HTMX territory must be named.**
2. **Server responses are HTML by default in HTMX land.**
3. **If you use pushed URLs, serve full pages for them.**
4. **Use `Vary: HX-Request` when full vs fragment rendering differs.**
5. **Treat `HX-Request`, `HX-Boosted`, `HX-Trigger`, and related headers as
   first-class part of the boundary.**
6. **Validation is server truth.**
7. **Progressive enhancement is a bonus, not a slogan.**
8. **If a non-HTMX library participates, integrate through events or bounded
   islands.**
9. **Use HTMX security tools when injecting risky content.**
   - `hx-disable`
   - CSP
   - same-origin request policy where appropriate
10. **Keep history and caching semantics explicit.**

### Important official-doc facts that should become laws

- HTMX expects **HTML** responses
- `hx-push-url` implies the route must be accessible as a full page
- `hx-sync` exists for request coordination; use it instead of pretending races do
  not exist
- progress indicators, response headers, and response code handling are all part
  of the formal tool, not hacks
- the docs strongly favor event-driven interop and island isolation
- the essay on hypermedia-friendly scripting explicitly argues for:
  - respecting HATEOAS
  - keeping purely client-only state client-only
  - using events between components
  - isolating non-hypermedia islands

### Good HTMX territory in this stack

- `/ops/*`
- `/admin/*`
- `/reports/*`
- `/review/*`
- `/settings/*`
- server-authored side panels, inspectors, and queue surfaces

### Bad HTMX territory in this stack

- the same route body that Elm thinks it owns
- deeply interactive simulation workbench canvas surrounds
- product surfaces that are mostly client-state machines

### Smells

- HTMX partials injected into an Elm-owned island
- Solid local state and HTMX fragments racing over the same DOM subtree
- using HTMX for a feature because "the reactive version was annoying"
- no full-page fallback for pushed URLs
- no caching strategy for `HX-Request` variation


---

### Source section: ## HTMX to Elysia seam

## HTMX to Elysia seam

### Good

- Elysia returns HTML fragments and full pages on purpose
- `HX-Request` and related headers are handled intentionally
- caching policy is explicit
- validation and error semantics are server-controlled

### Bad

- fragment vs full-page behavior left implicit
- 422 handling and form rerender semantics invented ad hoc
- no route ownership or full-page fallback

### Law

if HTMX is present, Elysia should know it is serving hypermedia, not just random
AJAX.


---

### Source section: ## Before touching HTMX, ask

## Before touching HTMX, ask

- is this truly a hypermedia-friendly surface?
- does the route have named territory?
- can the pushed URL return a full page?
- have we considered `HX-Request` caching variation?
- are we avoiding DOM warfare with client-owned islands?



