# Demotion Law And Component States

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## The demotion law

## The demotion law

not every project on this stack needs every lane to dominate.
that is healthy.

### A component may be present in one of three states

- **primary**
  - this component is central to the architecture
- **bounded**
  - this component has named territory and real value
- **dormant**
  - this component exists in the toolbelt or roadmap but has no current
    sovereignty

### Good examples

- Elm is dormant in a hypermedia-heavy admin app
- HTMX is bounded to `/ops/*` in a Solid-heavy desktop workbench
- Drogon is dormant until compute extraction is justified
- Turso is bounded to local drafts and cached work queues
- WebGPU is bounded to one analysis view

### Bad examples

- Elm is "kinda around" but nobody can name its territory
- HTMX is used wherever Solid feels annoying
- Drogon exists because C++ should be somewhere
- FlatBuffers exist because binary is cool
- Turso is present "for future offline" with no policy


---

### Source section: ## The keep / bounded / dormant framework

## The keep / bounded / dormant framework

when reviewing a project on this stack, classify components like this:

### Keep primary

- clearly owns a first-class lane
- delivers unique value
- no duplicate sovereignty

### Keep bounded

- useful in a specialized territory
- justified but not dominant
- requires explicit borders

### Keep dormant

- strategic future lane
- no current sovereignty
- present in build or package choice, but not in current architecture center

### Demote

- currently duplicating another lane
- role too fuzzy
- better kept available than active

### Remove or postpone

- all romance, no jurisdiction
- no real workload
- only there because it would be cool someday



