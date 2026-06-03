# ADR Checklist And No Folklore Doctrine

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## ADR checklist for stack changes

## ADR checklist for stack changes

when introducing, promoting, or demoting a lane in this stack, write down these
answers.

### Problem statement

- what concrete pain exists right now?
- which existing lane failed to solve it?
- what measured or observed evidence exists?

### Lane decision

- which lane will now own the concern?
- what lane is being demoted or kept out?
- is this lane primary, bounded, or dormant?

### Boundary decision

- what format crosses the boundary?
- who versions the contract?
- who translates internal errors into public semantics?
- what are the timeout, retry, and failure behaviors?

### Truth decision

- where is canonical truth for affected entities?
- where is local or cached state?
- what sync or merge policy applies?

### Build and release decision

- does this change affect Bun build truth?
- does this change affect CMake build truth?
- does this change affect Electrobun packaging or updater flow?
- does this change affect shader generation or Wasm output?

### Observability decision

- how will developers debug failures here?
- what metrics or logs prove the boundary is healthy?
- what user-visible health state, if any, is required?

### Kill-switch decision

- if this lane disappoints, how do we back out?
- what is the simpler fallback architecture?


---

### Source section: ## The no-folklore doctrine

## The no-folklore doctrine

if the answer to any major architecture question is:

- "ask Alex"
- "check that old thread"
- "it depends on the feature"
- "you kind of just know"

then the architecture is under-governed.

this stack is powerful enough to deserve written law.
use this file to make the law real instead of relying on haunted oral tradition.



