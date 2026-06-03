# Flatbuffers Constitution

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## FlatBuffers constitution (binary hot path only)

## FlatBuffers constitution (binary hot path only)

FlatBuffers are powerful.
FlatBuffers are also expensive in cognitive terms if sprayed across the repo.

### What FlatBuffers are for

- internal binary protocols
- low-overhead shared-core boundaries
- native/Wasm payloads where parse-free access matters
- layout-sensitive high-volume data
- stable schema evolution in hot internal paths

### What FlatBuffers are not for

- the public auth API
- ordinary CRUD payloads
- simple HTML fragment transport
- turning every contract into a binary ritual

### Laws

1. **FlatBuffers stay inside the hot path.**
2. **Public edges stay HTML or JSON by default.**
3. **Own schema evolution deliberately.**
4. **Treat FlatBuffers as a performance tool, not a general identity.**
5. **Keep decoding and translation boundaries explicit.**

### Good FlatBuffers territory

- C++ core to Wasm
- Drogon compute outputs to internal consumers
- GPU-adjacent layout preparation pipelines
- large binary model fragments
- high-frequency or large-volume internal payloads

### Bad FlatBuffers territory

- login form responses
- ordinary user settings pages
- admin panels
- public REST or hypermedia endpoints by default

### Smells

- developers cannot inspect product traffic without custom viewers
- binary payloads leaking into every feature because they were already there
- no named translation layer between human-readable and binary boundaries


---

### Source section: ## FlatBuffers to human-readable edge seam

## FlatBuffers to human-readable edge seam

### Good

- binary inside
- translation layer explicit
- HTML or JSON outside

### Bad

- internal performance contract leaks into public UX surface
- binary payloads are now everybody's problem

### Law

the public edge is for humans first.


---

### Source section: ## Before touching FlatBuffers, ask

## Before touching FlatBuffers, ask

- is this boundary hot enough to earn binary complexity?
- who versions this schema?
- where is the translation layer back to human-readable contracts?
- can engineers still inspect and debug the system sanely?
- are we keeping FlatBuffers away from boring public CRUD traffic?



