# Staged Adoption Path

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Staged adoption path (how to grow into the full stack without becoming cursed)

## Staged adoption path (how to grow into the full stack without becoming cursed)

one of the nicest things about this stack is that you do **not** need to boot all
lanes at maximum power on day one.

### Stage 0: the lean viable core

start with:

- Bun
- Elysia
- Solid
- Tailwind
- PostgreSQL
- Electrobun if desktop is required now

skip for now:

- Elm
- HTMX
- Drogon
- Turso Sync
- FlatBuffers
- Slang / WebGPU
- Wasm

### Stage 1: add HTMX where HTML is honestly better

add HTMX when:

- forms or reports start multiplying
- admin or ops surfaces deserve server-authored HTML
- the shell does not need to own everything

### Stage 2: add Elm for one feature that truly deserves TEA

add Elm when:

- one feature is getting gnarly state transitions
- replayability, determinism, or correctness matters a lot
- you can give it a real island

### Stage 3: extract shared C++ core

add C++ when:

- a real hot path exists
- logic duplication across languages is becoming dangerous
- performance or portability justify one compiled core

### Stage 4: compile the core to Wasm

add Emscripten when:

- that core needs to run in browser or portable shell contexts too
- keeping one implementation is more valuable than maintaining sibling rewrites

### Stage 5: extract Drogon compute service

add Drogon when:

- in-process boundaries (including Bun FFI) have been proven insufficient for the
  current workload and lifecycle needs
- compute workloads deserve service isolation
- long-running jobs, async streaming, or native throughput become real concerns
- independent scaling, multi-caller access, or service-level lifecycle controls
  are required

### Stage 6: add Turso Sync for local-first workflows

add Turso when:

- offline matters
- local latency matters
- device-local durability matters
- you can explain conflict policy in a paragraph

### Stage 7: add FlatBuffers to the hot path

add FlatBuffers when:

- parse cost, memory layout, or payload volume prove it worth the complexity

### Stage 8: add Slang and WebGPU

add GPU lane when:

- rendering or compute really needs it
- the product is visibly limited without it
- you can own the fallback and capability story

### Growth law

only add the next lane when its **reason** is stronger than its **romance**.



