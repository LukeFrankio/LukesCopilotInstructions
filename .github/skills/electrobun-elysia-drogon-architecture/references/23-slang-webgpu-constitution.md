# Slang Webgpu Constitution

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Slang constitution (shader source of truth)

## Slang constitution (shader source of truth)

Slang is the preferred authoring language for shader logic in this stack.

### What Slang is for

- one shader source across multiple target backends
- modular shader code organization
- HLSL and GLSL migration
- capability-aware shader authoring
- keeping large shader codebases sane
- enabling WebGPU without making WGSL the only source of truth

### What Slang is not for

- replacing application logic
- letting native graphics concerns bully every other layer
- becoming a shiny side quest with no real product need

### Laws

1. **Slang is authoring truth; WGSL is a target artifact.**
2. **Use modules.**
3. **Use the capability system honestly.**
4. **If a feature is target-specific, say so.**
5. **Do not fork shader truth per platform unless absolutely necessary.**
6. **Keep authoring and compilation policy centralized.**

### Good Slang territory

- shared shader library
- compute kernels
- rendering passes
- differentiable or ML-adjacent graphics experiments if the product truly needs
  them
- shader code that must target multiple backends

### Smells

- raw WGSL hand-maintained beside raw HLSL beside raw GLSL with no clear source
  of truth
- platform-specific shader drift nobody owns
- shader modules organized by accident instead of by rendering or compute domain


---

### Source section: ## WebGPU constitution (portable GPU execution)

## WebGPU constitution (portable GPU execution)

WebGPU is the product-facing execution surface for portable GPU workloads.

### What WebGPU is for

- modern GPU rendering
- modern GPU compute
- portable accelerated execution in browser-like environments
- GPU-heavy views in shell or web surfaces

### What WebGPU is not for

- replacing the CPU core indiscriminately
- carrying business truth
- justifying GPU complexity before the bottleneck is known

### Laws

1. **The GPU lane must earn itself.**
2. **Critical user flows need a fallback story.**
3. **Buffer layouts and CPU or GPU contract shapes must be governed.**
4. **Rendering logic stays rendering logic.**
5. **Do not move business policy into compute kernels because the GPU exists.**

### Smells

- product correctness depending on a GPU feature not widely available
- no capability detection path
- buffer layout contracts defined in three places


---

### Source section: ## Slang to WebGPU seam

## Slang to WebGPU seam

### Good

- Slang authoring centralized
- WGSL generated or governed as target output
- capability differences explicit

### Bad

- manual target edits causing drift
- no single compilation story

### Law

one shader truth if humanly possible.


---

### Source section: ## Before touching Slang, ask

## Before touching Slang, ask

- is Slang still the shader source of truth?
- does this belong in a module rather than another random file?
- are capability restrictions explicit?
- are we preserving portability rather than growing target forks?
- is there any sign of business logic creeping into shader code?


---

### Source section: ## Before touching WebGPU, ask

## Before touching WebGPU, ask

- is this really a GPU-worthy workload?
- what is the capability and fallback story?
- who owns the buffer layout contract?
- is the CPU-side product logic still in the right place?
- are we making the product better, or just more impressive on paper?



