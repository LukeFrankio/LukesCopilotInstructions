# Compute First Architecture

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Alternative architecture 3: Compute-First Native Platform Architecture

## Alternative architecture 3: Compute-First Native Platform Architecture

this variant centers the product more heavily around **native C++ compute** and
usually promotes **Drogon (or equivalent service boundary)**, while treating
Elysia as a thinner contract or edge layer.

### Summary

- native compute service boundaries become closer to the product's operational
  heart (often Drogon in this stack)
- Elysia still exists, but may mostly shape sessions, auth, web or desktop edge
  concerns, and client-specific contracts
- the shared C++ core is not just a reusable library; it is the center of the
  system's value
- Electrobun remains a client shell
- Wasm may exist for previews, local simulations, or browser portability

### Use this when

- the product is fundamentally a native compute platform with a UI around it
- the hard problems are CPU-heavy, concurrency-heavy, simulation-heavy, or
  numerically intense
- performance and determinism of the native lane dominate over convenience of the
  TS lane
- the product might have multiple clients talking to the same compute engine

### Avoid this when

- the real product complexity is auth, forms, composition, and product UX
- the native layer would only be there for one small hot function
- Elysia would end up proxying 99% of traffic with zero value added

### Mandatory laws

1. **If Drogon becomes public, say so explicitly.**
   - do not keep pretending Elysia is the only public layer if clients now depend
     on Drogon contracts
2. **Elysia must either own the product contract or be consciously demoted.**
   - fake sovereignty is worse than honest thinness
3. **Keep auth and policy centralized.**
   - do not split product policy randomly between Elysia and Drogon
4. **C++ remains the algorithmic truth.**
   - not Elysia convenience rewrites
   - not one-off JS ports
5. **Use FlatBuffers only where the hot path really needs it.**

### Why this can be better than the default

because some products are honestly native systems with web or desktop clients,
not web apps pretending to do serious compute.
that distinction matters.

### Why this can be worse than the default

because teams often let compute-first architecture become an excuse for
public-contract chaos.
if every client starts speaking directly to the native monster, the product edge
becomes less governable.



