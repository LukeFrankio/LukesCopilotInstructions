# GPU First Architecture

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Alternative architecture 5: GPU-First Visualization Workbench Architecture

## Alternative architecture 5: GPU-First Visualization Workbench Architecture

this variant makes the **GPU lane** far more central than in the default model.

### Summary

- Slang becomes a first-class source of product capability, not just a side lane
- WebGPU is central to rendering or compute
- the C++ core may feed GPU pipelines or share layouts with them
- Electrobun can host desktop-grade GPU-heavy experiences cleanly
- Elysia and Drogon remain around the product, but they are not the star

### Use this when

- the product is a renderer, visualizer, editor, simulation viewer, CAD-like
  workbench, media tool, scientific tool, or GPU-accelerated analysis surface
- shader modularity and multi-target deployment matter
- there is real benefit to one shader source across targets

### Avoid this when

- the GPU path is speculative
- the product is mostly forms and coordination work
- Slang and WebGPU are being added because they are cool, not because they are
  needed

### Mandatory laws

1. **Slang is the authoring truth.**
   - WGSL is a generated or target form for the web path
2. **Capability checks are explicit.**
   - Slang's capability model exists for a reason
3. **Provide fallbacks.**
   - if a critical path needs CPU fallback, say so
   - if a feature is optional without GPU, say so
4. **Keep product logic out of shaders.**
5. **Keep shader module boundaries sane.**
   - do not treat shaders as one monolithic pastebin
6. **Own buffer layout strategy.**
   - if binary layouts matter across CPU, Wasm, and GPU, govern them on purpose

### Why this can be better than the default

because some products truly are visual or numeric systems first.
for them, the GPU is not a side quest.
it is the thing.

### Why this can be worse than the default

because GPU-first architecture can spread its worldview everywhere if nobody puts
up fences.
your billing rules do not need to be shader-adjacent, bestie.



