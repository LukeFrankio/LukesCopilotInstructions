# Hypermedia First Architecture

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Alternative architecture 1: Hypermedia-First Operations Architecture

## Alternative architecture 1: Hypermedia-First Operations Architecture

this is still the same stack.
this is **not** a different stack.
it is the same components arranged around a different center of gravity.

### Summary

- HTMX becomes much more prominent
- Solid remains the shell but thinner
- Elm becomes optional or very narrowly scoped
- Elysia becomes both public contract and HTML fragment engine for most surfaces
- Drogon remains the compute sidecar for heavy work
- Electrobun remains the desktop shell if a desktop form factor still matters

### Use this when

- most product value is in forms, workflows, queues, review interfaces, reports,
  settings, approvals, or document-like surfaces
- the product benefits more from server-authored HTML than from thick client
  reactive state
- many routes want progressive enhancement or simpler debugging
- the shell still matters, but the app is not interaction-engine-dominated

### Avoid this when

- the product has a few very deep state-machine-like interactions that really
  deserve Elm
- the app is heavily visual, animation-heavy, graphics-heavy, or local-state
  dominated
- the team will use HTMX as a cover story for route ownership confusion

### What changes from the default

| Concern | Default federation | Hypermedia-first variant |
| --- | --- | --- |
| shell | Solid-heavy shell | Solid still owns shell, but most route bodies are server-driven |
| primary feature lane | Solid + Elm mix | HTMX + Elysia HTML dominates most feature surfaces |
| Elm | important bounded engine | optional or limited to one advanced surface |
| Elysia | API + fragments | heavily HTML-oriented BFF and route composition engine |
| routing | more client-orchestrated shell | more server-authorized surface control |

### Mandatory laws

1. **HTMX routes must be named territory.**
   - `/ops/*`
   - `/admin/*`
   - `/reports/*`
   - `/settings/*`
   - or another clear partition
2. **Pushed URLs must be navigable as full pages.**
   - HTMX docs are explicit about this
   - do not push routes that only exist as partial fragments
3. **Use `Vary: HX-Request` when response shape differs for fragments vs full
   pages.**
4. **Set `historyRestoreAsHxRequest` thoughtfully.**
   - when using `HX-Request` to vary partials vs full pages, do not allow history
     restoration behavior to poison that assumption
5. **Server validation is truth.**
   - client validation is a convenience only
6. **HTMX is not your secret state manager.**
   - if a route needs rich local state, that is a signal for Solid or Elm island
     territory, not a reason to stretch fragments until they scream

### Why this can be better than the default

because many productivity and operations apps do **not** need the cost of a rich
client architecture everywhere.
HTML and HTTP are already powerful.
let them cook.

### Why this can be worse than the default

because if the product later grows a few ultra-rich interactions, teams often
start mixing HTMX, ad hoc JavaScript, Solid local state, and Elm-like logic with
no constitution.
that is how you invent a haunted DOM.



