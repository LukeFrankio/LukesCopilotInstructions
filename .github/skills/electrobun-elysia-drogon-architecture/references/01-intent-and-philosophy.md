# Intent And Philosophy

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Core philosophy (non-negotiable axioms)

## Core philosophy (non-negotiable axioms)

- **roles > ingredients**
  - the key question is never "can these technologies coexist?"
  - the real question is "what does each one own, and what is forbidden?"
- **one stack, many architectures**
  - this stack supports multiple legitimate shapes
  - it is not required to express the same hierarchy in every product
- **defaults beat democracy**
  - every project needs a normal path for new work
  - if everything is equally primary, nothing is primary
- **specialization must stay specialized**
  - Elm, HTMX, Drogon, Turso Sync, FlatBuffers, Emscripten, and WebGPU all have
    real value
  - they are strongest when they stay in their lane instead of cosplaying as
    the whole product
- **human-readable edges, optimized hot paths**
  - HTML and JSON belong at product edges by default
  - FlatBuffers and other binary contracts belong on the internal hot path only
- **one owner per concern**
  - shell, interaction engine, hypermedia lane, public contract, compute,
    canonical truth, local sync, binary schema, and GPU lane all need owners
- **one source of truth per domain entity**
  - PostgreSQL and Turso may collaborate
  - they do not get to both wear the crown unless explicitly and narrowly
    declared
- **shared cores are based**
  - duplicated sibling implementations are cope
  - if the same algorithm matters in native and web contexts, write it once and
    compile it twice
- **weirdness must earn rent**
  - C++/WASM, FlatBuffers, Slang, WebGPU, and multi-runtime orchestration are
    powerful
  - they are justified by real product needs, not by aesthetic maximalism
- **latest versions always**
  - use the latest stable or beta line that the ecosystem actually supports
  - this stack moves fast; architectural guidance must acknowledge that reality
- **documentation and changelogs matter**
  - Elysia, Electrobun, Drizzle, Turso, and Slang are all active enough that
    stale assumptions rot quickly
- **no component has tenure**
  - every layer must keep re-earning its seat over time
- **platform bet risk is architecture risk**
  - young or fast-moving foundations (especially shell runtimes) need explicit
    contingency seams
  - "we can swap later" is only true if seams exist now


---

### Source section: ## What this stack actually is

## What this stack actually is

this stack is not one thing.
it is a federation of five major lanes:

1. **desktop and shell lane**
   - Electrobun
   - Bun
   - SolidJS
   - Tailwind CSS
2. **interaction and hypermedia lane**
   - Elm
   - HTMX
   - Elysia HTML or fragment rendering
3. **public contract and service composition lane**
   - Elysia
   - Drizzle ORM
   - Bun runtime and tooling
4. **native compute and portable core lane**
   - Drogon
   - modern C++
   - CMake
   - Emscripten / Embind
   - FlatBuffers
5. **GPU and accelerated rendering or compute lane**
   - Slang
   - WGSL
   - WebGPU

and all of those lanes sit on top of a data topology:

- **PostgreSQL** for canonical truth
- **Turso Sync** for local-first, offline, replicated, or edge-adjacent state

if you forget that this is a **lane stack** rather than a **single-framework
stack**, you will make bad decisions with frightening confidence.


---

### Source section: ## The hidden smell this stack attracts

## The hidden smell this stack attracts

this stack's signature temptation is:

> "surely every interesting component should remain involved forever"

that instinct is dangerous.

### Good interpretation

- each component has a real earned role
- each role is bounded
- each boundary exists because it solves a real problem
- not every component dominates every project

### Cursed interpretation

- we must find something for every tool to do
- removing or demoting a tool feels like betrayal
- a lane exists because it is interesting, not because it is necessary
- architecture becomes a celebration of inventory

this file supports **using the whole stack**.
it does **not** support worshipping the whole stack.



