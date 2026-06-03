# Default Architecture Decision Law

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## How to decide whether the default architecture should be used

## How to decide whether the default architecture should be used

use the default federation when most of the following are true:

- the product is desktop-shell friendly
- there is at least one deep interactive feature, but not enough to make Elm the
  whole product
- there are some admin, settings, or ops surfaces that HTMX would simplify
- Elysia provides clear product-edge value
- native compute exists or is likely to matter
- offline or local-first needs exist but do not dominate everything
- GPU work is important or plausible but not the center of all architecture

avoid the default federation when most of the following are true:

- almost every meaningful route is server-authored and hypermedia-first
- almost every meaningful product surface is an Elm-worthy interaction engine
- nearly all product complexity lives in native compute and Elysia adds little
- local-first semantics dominate product design more than public-contract shape
- the GPU lane is the true heart of the product



