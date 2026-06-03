---
name: electrobun-elysia-drogon-architecture
description: Use when designing, reviewing, critiquing, or refactoring architecture for stacks combining Electrobun, Bun, SolidJS, Elm, HTMX, Tailwind, Elysia, Drizzle, PostgreSQL, Turso Sync, Drogon, C++, CMake, Emscripten/Embind, FlatBuffers, Slang, WGSL, and WebGPU.
user-invocable: true
disable-model-invocation: false
---

# Electrobun Elysia Drogon Architecture

Companion skill for the constitutional mega-stack architecture guidance.

## Hard Rule

This skill is **additive** and does **not** replace the instruction file.
Authoritative baseline content is preserved in:

- [00-full-source-port.md](./references/00-full-source-port.md)

## When to Use

Use this skill when the task involves any of:

- lane ownership disputes (Solid vs Elm vs HTMX)
- public contract vs compute boundary decisions (Elysia vs Drogon)
- Bun FFI vs supervised process vs queue-backed worker vs Drogon service
  extraction
- Electrobun shell risk and contingency planning
- Turso vs PostgreSQL truth partitioning
- FlatBuffers hot-path boundary scoping
- Slang/WGSL/WebGPU lane governance

## Boundary ladder reminder

When compute placement is the real question, prefer the ladder in this order:

1. in-process FFI or thin host bridge
2. supervised local process
3. queue-backed worker for durable async work, retries, or fan-out
4. Drogon internal service only when service semantics are genuinely earned

That ladder is the core fix for the old "Drogon by default" mental model.

## Routing Table

## Core architecture
- [01-intent-and-philosophy.md](./references/01-intent-and-philosophy.md)
- [02-lane-model-and-roster.md](./references/02-lane-model-and-roster.md)
- [03-version-and-drift-policy.md](./references/03-version-and-drift-policy.md)

## Technology constitutions
- [10-electrobun-constitution.md](./references/10-electrobun-constitution.md)
- [11-bun-constitution.md](./references/11-bun-constitution.md)
- [12-solid-constitution.md](./references/12-solid-constitution.md)
- [13-tailwind-constitution.md](./references/13-tailwind-constitution.md)
- [14-elm-constitution.md](./references/14-elm-constitution.md)
- [15-htmx-constitution.md](./references/15-htmx-constitution.md)
- [16-elysia-constitution.md](./references/16-elysia-constitution.md)
- [17-drizzle-constitution.md](./references/17-drizzle-constitution.md)
- [18-drogon-constitution.md](./references/18-drogon-constitution.md)
- [19-postgres-constitution.md](./references/19-postgres-constitution.md)
- [20-turso-constitution.md](./references/20-turso-constitution.md)
- [21-cpp-cmake-wasm-constitution.md](./references/21-cpp-cmake-wasm-constitution.md)
- [22-flatbuffers-constitution.md](./references/22-flatbuffers-constitution.md)
- [23-slang-webgpu-constitution.md](./references/23-slang-webgpu-constitution.md)

## Architecture variants and seams
- [30-default-federation-architecture.md](./references/30-default-federation-architecture.md)
- [31-hypermedia-first-architecture.md](./references/31-hypermedia-first-architecture.md)
- [32-elm-centric-architecture.md](./references/32-elm-centric-architecture.md)
- [33-compute-first-architecture.md](./references/33-compute-first-architecture.md)
- [34-local-first-architecture.md](./references/34-local-first-architecture.md)
- [35-gpu-first-architecture.md](./references/35-gpu-first-architecture.md)
- [36-demotion-law-and-component-states.md](./references/36-demotion-law-and-component-states.md)
- [40-seam-laws.md](./references/40-seam-laws.md)
- [41-route-and-territory-map.md](./references/41-route-and-territory-map.md)
- [42-contract-style-laws.md](./references/42-contract-style-laws.md)
- [43-build-topology-templates.md](./references/43-build-topology-templates.md)

## Adoption and governance
- [50-staged-adoption-path.md](./references/50-staged-adoption-path.md)
- [51-lane-decision-checklists.md](./references/51-lane-decision-checklists.md)
- [52-product-shape-recommendation-matrix.md](./references/52-product-shape-recommendation-matrix.md)
- [53-anti-pattern-catalog.md](./references/53-anti-pattern-catalog.md)
- [60-security-laws.md](./references/60-security-laws.md)
- [61-observability-laws.md](./references/61-observability-laws.md)
- [62-testing-verification-laws.md](./references/62-testing-verification-laws.md)
- [63-performance-laws.md](./references/63-performance-laws.md)
- [64-default-architecture-decision-law.md](./references/64-default-architecture-decision-law.md)
- [65-keep-bounded-dormant-framework.md](./references/65-keep-bounded-dormant-framework.md)
- [66-verdict-language-and-final-checklist.md](./references/66-verdict-language-and-final-checklist.md)

## Expanded appendices (post-3000 content split)
- [70-feature-placement-atlas-ui-routes.md](./references/70-feature-placement-atlas-ui-routes.md)
- [71-feature-placement-atlas-services.md](./references/71-feature-placement-atlas-services.md)
- [72-feature-placement-atlas-data.md](./references/72-feature-placement-atlas-data.md)
- [73-feature-placement-atlas-transport.md](./references/73-feature-placement-atlas-transport.md)
- [74-ownership-by-concern-atlas.md](./references/74-ownership-by-concern-atlas.md)
- [75-scenario-guide-part-1.md](./references/75-scenario-guide-part-1.md)
- [76-scenario-guide-part-2.md](./references/76-scenario-guide-part-2.md)
- [77-scenario-guide-part-3.md](./references/77-scenario-guide-part-3.md)
- [78-product-archetype-playbooks-part-1.md](./references/78-product-archetype-playbooks-part-1.md)
- [79-product-archetype-playbooks-part-2.md](./references/79-product-archetype-playbooks-part-2.md)
- [80-migration-playbooks-part-1.md](./references/80-migration-playbooks-part-1.md)
- [81-migration-playbooks-part-2.md](./references/81-migration-playbooks-part-2.md)
- [82-pr-review-rubrics-by-lane.md](./references/82-pr-review-rubrics-by-lane.md)
- [83-failure-mode-catalog.md](./references/83-failure-mode-catalog.md)
- [84-team-topology-and-governance.md](./references/84-team-topology-and-governance.md)
- [85-forbidden-crossover-charter-part-1.md](./references/85-forbidden-crossover-charter-part-1.md)
- [86-forbidden-crossover-charter-part-2.md](./references/86-forbidden-crossover-charter-part-2.md)
- [87-forbidden-crossover-charter-part-3.md](./references/87-forbidden-crossover-charter-part-3.md)
- [88-workflow-constitutions-part-1.md](./references/88-workflow-constitutions-part-1.md)
- [89-workflow-constitutions-part-2.md](./references/89-workflow-constitutions-part-2.md)
- [90-sync-policy-templates.md](./references/90-sync-policy-templates.md)
- [91-environment-matrix-and-runtime-modes.md](./references/91-environment-matrix-and-runtime-modes.md)
- [92-adr-checklist-and-no-folklore-doctrine.md](./references/92-adr-checklist-and-no-folklore-doctrine.md)
- [93-lane-quick-checklists-shell-ui.md](./references/93-lane-quick-checklists-shell-ui.md)
- [94-lane-quick-checklists-services-data.md](./references/94-lane-quick-checklists-services-data.md)
- [95-lane-quick-checklists-native-gpu.md](./references/95-lane-quick-checklists-native-gpu.md)
- [96-architecture-oath-and-mantra.md](./references/96-architecture-oath-and-mantra.md)

## Companion templates

- [architecture-review-template.md](./assets/architecture-review-template.md)
- [lane-ownership-audit-template.md](./assets/lane-ownership-audit-template.md)
- [compute-boundary-decision-record-template.md](./assets/compute-boundary-decision-record-template.md)
- [electrobun-contingency-audit-template.md](./assets/electrobun-contingency-audit-template.md)

## Verification Procedure

1. Use this router to load only relevant modules for the current architecture question.
2. Prefer module guidance over ad hoc “it depends” answers.
3. For deep historical parity or line-by-line source verification, consult full source port.
4. Keep instruction and skill guidance semantically aligned when either evolves.
