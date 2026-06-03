# Lane Decision Checklists

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Decision checklists before adding or promoting a lane

## Decision checklists before adding or promoting a lane


---

### Source section: ## Before adding Elm

## Before adding Elm

- [ ] what exact feature surface will Elm own?
- [ ] why is Solid not sufficient there?
- [ ] can the boundary be coarse?
- [ ] are ports enough for the required interop?
- [ ] does the feature actually benefit from TEA discipline?
- [ ] are we prepared to keep HTMX out of this surface?


---

### Source section: ## Before adding HTMX territory

## Before adding HTMX territory

- [ ] is the route family form-heavy, report-heavy, admin-heavy, or
      document-centric?
- [ ] do we want server-authored HTML here?
- [ ] can we serve full pages for pushed URLs?
- [ ] have we planned `HX-Request` caching variation?
- [ ] is this territory named, not vibes-based?


---

### Source section: ## Before adding Drogon

## Before adding Drogon

- [ ] is there meaningful native compute or throughput value?
- [ ] why is Bun FFI or an in-process native bridge insufficient here?
- [ ] are long-running tasks a first-class concern?
- [ ] do we need streaming or coroutine-friendly native services?
- [ ] do we need an independent process lifecycle or scaling profile?
- [ ] will more than one caller depend on this service boundary?
- [ ] would Elysia otherwise become a compute monolith?
- [ ] do we know whether Drogon is internal or public?


---

### Source section: ## Before adding Turso Sync

## Before adding Turso Sync

- [ ] does offline use materially matter?
- [ ] do local writes need to survive disconnection?
- [ ] is last-push-wins acceptable for the affected entities?
- [ ] who owns conflict resolution?
- [ ] what gets synced and what stays device-local?
- [ ] what is the bootstrap policy on first launch?


---

### Source section: ## Before adding FlatBuffers

## Before adding FlatBuffers

- [ ] what is the measured pain with JSON here?
- [ ] is this boundary actually hot?
- [ ] who versions the schema?
- [ ] who translates between binary and public shapes?
- [ ] can developers still debug the system sanely?


---

### Source section: ## Before compiling to Wasm

## Before compiling to Wasm

- [ ] is there a genuine shared C++ core?
- [ ] can we keep the host wrapper thin?
- [ ] are main loop and file system differences understood?
- [ ] is the boundary coarse enough?
- [ ] are we avoiding duplicate implementations?


---

### Source section: ## Before adding WebGPU or Slang

## Before adding WebGPU or Slang

- [ ] is there a real rendering or compute bottleneck?
- [ ] do we want one shader source across targets?
- [ ] is there a fallback story?
- [ ] is the shader module structure intentional?
- [ ] have we kept business logic out of the GPU lane?


---

### Source section: ## Before enabling CEF in Electrobun

## Before enabling CEF in Electrobun

- [ ] what actual system webview limitation is hurting us?
- [ ] is it a temporary platform bug or a product requirement?
- [ ] is the added binary weight justified?
- [ ] are we willing to own that distribution and update cost?



