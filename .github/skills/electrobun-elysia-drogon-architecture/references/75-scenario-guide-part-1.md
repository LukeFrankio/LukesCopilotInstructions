# Scenario Guide Part 1

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Concrete scenario guide (40 common "where does this go?" calls)

## Concrete scenario guide (40 common "where does this go?" calls)

### 1. "We need a settings screen."

- default answer: **HTMX + Elysia HTML**
- move to Solid only if:
  - it needs rich local-only shell behavior
  - it is part of the app chrome experience
- move to Elm only if:
  - it becomes a correctness-heavy state machine
- do not send this to Drogon

### 2. "We need a complex wizard with branching validation and undo."

- default answer: **Elm**
- host it in the Solid shell
- keep server calls through Elysia
- keep HTMX out unless separate supporting pages exist

### 3. "We need a boring admin CRUD list."

- default answer: **HTMX**
- Elysia serves fragments and pages
- Drizzle and Postgres back it
- do not reach for Elm because boredom is not a state machine

### 4. "We need a big batch transform pipeline."

- default answer: **C++ core + selected boundary**
- Elysia may start the job and shape public responses
- use FlatBuffers only if the boundary proves hot enough

### 5. "We need local drafts that survive offline."

- default answer: **Turso local-first**
- publish or sync through Elysia when connected
- keep canonical published truth in Postgres

### 6. "We need a lightweight profile page."

- default answer: **HTMX or Solid**
- pick HTMX if mostly forms and server-rendered details
- pick Solid if it sits naturally in shell navigation and client-side state
- do not over-promote this into Elm

### 7. "We need a node-graph editor."

- default answer: **Elm or Solid + WebGPU** depending state discipline needs
- use C++ core for heavy graph analysis if needed
- do not use HTMX for the interactive graph surface

### 8. "We need a report export button."

- default answer:
  - button UI in HTMX or Solid depending page owner
  - heavy export in C++ core or Drogon if justified
  - contract initiation in Elysia

### 9. "We need shell-wide connectivity and sync badges."

- default answer: **Solid shell**
- source status may come from Turso stats and Elysia health
- keep this out of HTMX route ownership

### 10. "We need live progress updates for a long-running native task."

- default answer:
  - task owner: **Drogon**
  - public contract owner: **Elysia** unless a compute-first architecture says
    otherwise
  - UI host: **Solid shell**

### 11. "We need one small fancy widget on an otherwise boring admin page."

- default answer: **HTMX page + bounded client island**
- the island can be Solid or a tiny JS helper
- do not let the one widget change page ownership

### 12. "We need a deterministic review workflow with 12 states."

- default answer: **Elm** if this is the center of the product value
- otherwise HTMX may still work if state depth is lower than it sounds

### 13. "We need to parse and preview huge files in the client."

- default answer: **C++ core + Wasm** for heavy parsing
- shell UI in Solid
- keep preview contract coarse

### 14. "We need to compile or inspect shaders in-app."

- default answer: **Slang-centered tooling path**
- present it in Solid shell
- use WebGPU where runtime preview matters

### 15. "We need a lightweight public JSON API for a mobile or web client."

- default answer: **Elysia**
- if compute-heavy, Elysia delegates to Drogon
- keep the public contract legible

### 16. "We need a machine-generated internal payload between native and Wasm."

- default answer: **FlatBuffers** if the path is hot enough
- otherwise plain structured boundary is fine

### 17. "We need a desktop-only local library browser with thumbnails and notes."

- default answer: **Solid + Electrobun + Turso**
- sync to server later if needed

### 18. "We need a fast text search over huge local content."

- default answer: local-first architecture
- UI in Solid
- index in Turso, native code, or both depending scale
- authoritative publish state still in Postgres if collaborative

### 19. "We need a metrics dashboard for internal ops."

- default answer: **HTMX + Elysia HTML**
- bounded client charts are okay inside that route family

### 20. "We need one route to act like a rich mini-application."

- default answer: **Elm island inside Solid shell**
- unless it is clearly a hypermedia report or forms page

### 21. "We need a login or account recovery flow."

- default answer: **Elysia + HTMX or Solid**
- this is public contract and product edge work, not compute-engine turf

### 22. "We need file drag-and-drop with immediate native affordances."

- default answer: **Electrobun shell + Solid UI**
- heavy processing can drop to C++ core or Drogon later

### 23. "We need to sync local edits later when online."

- default answer: **Turso push or pull orchestration**
- expose visible sync health in the shell

### 24. "We need an approvals queue with comments and side-by-side diffing."

- default answer: **HTMX page with Solid diff island**
- promote to Elm only if the internal transition logic gets truly gnarly

### 25. "We need durable collaborative permissions around shared assets."

- default answer: **PostgreSQL truth + Elysia policy edge**
- local mirrors are allowed, local sovereignty is not

### 26. "We need a shader-based preview canvas embedded in desktop UI."

- default answer: **Solid shell + WebGPU + Slang-generated shader path**
- keep tool state in Solid or Elm based on complexity

### 27. "We need a job retry and cancellation console."

- default answer: **HTMX or Solid UI**
- actual job control semantics remain Elysia + Drogon territory

### 28. "We need inline validation with friendly UX on a form."

- default answer: **HTMX + Elysia**
- use client-side affordances for comfort
- keep server validation authoritative

### 29. "We need local notes attached to shared objects."

- default answer: **Turso local state** if the notes are device-local
- **PostgreSQL** if they are shared collaboration artifacts
- decide on purpose, not later

### 30. "We need a reviewable audit trail of sync conflicts."

- default answer:
  - canonical record: **PostgreSQL**
  - local event visibility: **Turso stats or local history**
  - UI: **HTMX** or **Solid** depending route family

### 31. "We need a command-line maintenance tool."

- default answer: **Bun + Drizzle** for TS-side ops
- **C++ utility** only if it genuinely sits closer to shared-core behavior

### 32. "We need a portable compute preview in browser and desktop."

- default answer: **C++ shared core -> Emscripten/Wasm**
- shell or browser UI chooses how to display results

### 33. "We need a tiny binary patch update system."

- default answer: **Electrobun updater**
- do not invent your own updater just because infra engineers got bored

### 34. "We need a big static or semi-static documentation viewer inside the app."

- default answer: **HTMX** if dynamic but server-authored
- **Solid** if fully client-embedded and tightly shell-integrated

### 35. "We need role-aware HTML fragments."

- default answer: **Elysia hypermedia routes**
- this is product edge policy plus fragment shaping

### 36. "We need exportable binary model files for heavy scenes."

- default answer: **C++ core** for structure generation
- **FlatBuffers** if the format and workflow justify it
- not JSON if the volume is absurd

### 37. "We need a live status board for active compute sessions."

- default answer: **Solid shell or HTMX route depending audience**
- backend owner: **Elysia** or **Drogon** based on public vs internal audience

### 38. "We need a one-off support tool with lots of tables and actions."

- default answer: **HTMX**
- do not waste a perfect hypermedia use-case on SPA ceremony

### 39. "We need a polished desktop-first multi-panel workbench."

- default answer: **default federation**
- Solid shell
- optional Elm islands
- HTMX ops routes
- native compute behind Elysia

### 40. "We need a purely local technical tool that may sync later."

- default answer: **Electrobun + Solid + Turso**, with Postgres and Elysia added
  only when cloud truth becomes product-relevant



