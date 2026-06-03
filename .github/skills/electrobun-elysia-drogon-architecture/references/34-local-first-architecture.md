# Local First Architecture

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Alternative architecture 4: Local-First Synced Workstation Architecture

## Alternative architecture 4: Local-First Synced Workstation Architecture

this variant makes **Turso Sync** much more central to user experience.

### Summary

- local reads and writes are primary during active usage
- cloud truth still exists, usually in PostgreSQL-backed server lanes
- sync is explicit, not magical
- Electrobun is very attractive here because local device semantics matter
- Elysia and Drogon remain important but do not own every interaction moment

### Use this when

- the app must stay useful offline
- users spend long periods disconnected or intermittently connected
- local durability, startup speed, and device-local workflows matter a lot
- conflict domains are narrow enough to make explicit sync rules viable

### Avoid this when

- many users are constantly contending on the same records
- conflict semantics are complex and the team has no merge strategy beyond hope
- the product does not actually benefit from offline or local-first workflows

### Mandatory laws

1. **Turso is local operational truth, not universal truth.**
2. **PostgreSQL remains canonical unless explicitly narrowed otherwise.**
3. **Sync timing is explicit.**
   - startup pull
   - manual sync
   - background sync
   - connectivity-event sync
   - conflict recovery
4. **Acknowledge Turso Sync conflict policy.**
   - official docs say last push wins
   - if that is dangerous for an entity class, do not use naïve sync there
5. **Use `bootstrapIfEmpty` intentionally.**
   - if offline-first startup matters, say so and configure it accordingly
6. **Observe sync health.**
   - checkpoint
   - stats
   - last pull time
   - last push time
   - WAL growth

### Why this can be better than the default

because some desktop and field apps live or die by local-first credibility.
latency, resiliency, and "works on the train" are not fake features.

### Why this can be worse than the default

because teams routinely underestimate sync semantics.
local-first done casually is just distributed systems pain wearing a cozy hat.



