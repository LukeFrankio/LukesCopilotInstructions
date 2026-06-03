# Feature Placement Atlas UI Routes

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Feature placement atlas

## Feature placement atlas

this section is intentionally blunt.
if a new piece of work arrives, use these tables before inventing a fourth owner.


---

### Source section: ## Route and UI placement matrix

## Route and UI placement matrix

| Work item | Default owner | Escalate to | Keep away from | Why |
| --- | --- | --- | --- | --- |
| app chrome | Solid + Electrobun | none | HTMX, Elm, Drogon | this is literally shell territory |
| window menus and tray | Electrobun | none | Solid-only abstractions, Elm | desktop shell concern |
| theme switcher | Solid + Tailwind | HTMX if settings page is server-authored | Drogon, C++ | cross-cutting shell state |
| account settings page | HTMX + Elysia HTML | Solid if rich client behavior grows | Elm, Drogon | classic form and settings territory |
| admin queue page | HTMX + Elysia HTML | Solid shell wrapper | Elm | server-authored lists and forms are ideal here |
| report viewer | HTMX + Elysia HTML | Solid if charts become rich | Elm by default | document and report surfaces love hypermedia |
| notification center | Solid | HTMX for admin-rendered notification templates if needed | Elm | shell concern with transient state |
| onboarding flow | Solid by default | Elm if transitions become correctness-sensitive | HTMX if it becomes state-heavy | shell-adjacent, but can become a state machine |
| billing screen | HTMX + Elysia | Solid shell wrapper | Drogon direct, FlatBuffers | public edge, forms, policy, human-readable contract |
| profile page | HTMX or Solid | none | Drogon, Wasm | not a compute lane problem |
| desktop preferences dialog | Solid or HTMX | none | Elm unless genuinely state-machine-heavy | local UX or server-authored form work |
| import wizard | Solid | Elm if import states are complex and error-rich | HTMX fragments inside the core wizard | shell-hosted workflow that may justify TEA |
| export dialog | Solid | C++ core for actual export logic | HTMX route ownership conflict | shell modal with delegated heavy work |
| sync status center | Solid shell | HTMX detail pages for history or logs | Elm unless conflict resolution is deep | shell concern plus local-first insight |
| sync conflict resolution screen | Elm or Solid | HTMX for review pages if mostly document-like | random ad hoc JS | this can become a real interaction engine |
| admin audit log | HTMX + Elysia HTML | Solid shell framing | Elm | paged, filterable, server-authored list territory |
| interactive graph editor | Elm + WebGPU or Solid + WebGPU | C++ core if algorithmic model is shared | HTMX | this is not a fragment job |
| simulation control panel | Elm | Solid shell host | HTMX | deterministic bounded interaction territory |
| model browser | Solid | HTMX if it becomes mostly document navigation | Elm by default | browse and preview UI fits shell-side reactivity |
| document review workflow | HTMX or Elm depending state depth | Solid shell wrapper | raw FlatBuffers | if transitions matter deeply, Elm; otherwise HTMX |
| command palette | Solid + Electrobun | C++ core for ranking or search if hot | HTMX | shell-native interaction |
| feature flags console | HTMX + Elysia HTML | Solid shell wrapper | Drogon | admin and ops territory |
| internal support dashboard | HTMX + Elysia HTML | Solid charts or widgets as bounded islands | Elm as default | server-authored operations territory |
| offline drafts browser | Solid + Turso | HTMX for listing if mostly document-like | Postgres direct-only mental model | local-first user-side concern |
| job progress page | Solid shell + Elysia stream | HTMX for simple server-authored progress | Elm if the UI becomes a workflow engine | cross-cutting shell + compute coordination |
| shader inspector | Solid + WebGPU | Elm if it becomes deterministic tool state | HTMX | technical workstation surface, not hypermedia |
| log console | Solid | HTMX if mostly server-rendered pages | Elm | shell or tooling view |
| diagnostics page | HTMX or Solid | none | FlatBuffers public edge | human-readable ops surface |
| help docs page | HTMX | Solid shell wrapper | Elm, Drogon | document-oriented territory |
| collaborative permissions matrix | HTMX or Elm depending complexity | Solid shell wrapper | Turso-only truth | if edits are complex and correctness-heavy, Elm |
| review and approval queue | HTMX | Elm when transitions are deep and branched | Drogon | ideal hypermedia territory unless workflow logic explodes |
| file diff viewer | Solid | C++ core for diff computation | HTMX for the diff surface itself if very interactive | rendering-heavy client-side feature |
| local workspace chooser | Solid + Electrobun | Turso for backing data | HTMX by default | desktop shell and local state concern |
| search results page | HTMX or Solid | C++ or Drogon for heavy ranking logic | Elm by default | depends on interaction depth |
| visual node editor | Elm or Solid + WebGPU | C++ core for compute | HTMX | stateful visual tool, not hypermedia |
| simple CRUD table | HTMX | Solid only if local-only client interaction dominates | Elm | don't over-architect boring work |
| file upload form | HTMX + Elysia HTML | Solid if UX gets highly custom | Drogon public direct | form-heavy and server-mediated by default |
| background task launcher | HTMX or Solid | Drogon executes actual work | Elm only if the launcher itself is a workflow engine | human-readable edge over native compute |
| status badge in shell | Solid | none | HTMX, Elm | this is shell ambient state |



