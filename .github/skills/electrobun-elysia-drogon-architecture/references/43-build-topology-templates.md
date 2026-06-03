# Build Topology Templates

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Build and repo topology templates

## Build and repo topology templates

these are examples, not holy scripture.
the point is to show **clean ownership**.


---

### Source section: ## Default federation topology

## Default federation topology

```text
repo/
├── apps/
│   ├── desktop-shell/
│   │   ├── electrobun.config.ts
│   │   ├── package.json
│   │   ├── src/
│   │   │   ├── main/                 <- Bun-side Electrobun entrypoints
│   │   │   ├── shell/                <- Solid shell and chrome
│   │   │   ├── interactive/          <- Elm host adapters and mount points
│   │   │   ├── ops/                  <- HTMX shell-hosted route wrappers if any
│   │   │   └── styles/               <- Tailwind entry and tokens
│   └── gateway/
│       ├── src/
│       │   ├── api/                  <- Elysia JSON routes
│       │   ├── hypermedia/           <- Elysia HTML fragment routes for HTMX
│       │   ├── auth/
│       │   ├── policies/
│       │   ├── services/
│       │   └── db/                   <- Drizzle access and migrations
├── services/
│   └── compute/
│       ├── src/
│       │   ├── handlers/             <- Drogon endpoints
│       │   ├── jobs/
│       │   ├── streaming/
│       │   └── adapters/             <- thin wrappers around shared C++ core
├── packages/
│   ├── elm-engine/
│   │   └── src/
│   ├── shared-core/
│   │   ├── CMakeLists.txt
│   │   ├── include/
│   │   ├── src/
│   │   ├── bindings/
│   │   ├── wasm/
│   │   └── tests/
│   ├── schemas/
│   │   ├── flatbuffers/
│   │   └── generated/
│   ├── shaders/
│   │   ├── slang/
│   │   └── generated/
│   └── design-system/
│       └── tailwind/
└── infra/
    ├── postgres/
    ├── turso/
    └── release/
```


---

### Source section: ## Hypermedia-first topology

## Hypermedia-first topology

```text
repo/
├── apps/
│   ├── desktop-shell/                <- thin Solid shell around mostly HTMX routes
│   └── gateway/
│       ├── src/
│       │   ├── hypermedia/           <- dominant surface layer
│       │   ├── partials/
│       │   ├── forms/
│       │   ├── reports/
│       │   └── admin/
├── services/
│   └── compute/
├── packages/
│   ├── shared-core/
│   ├── shaders/
│   └── design-system/
```


---

### Source section: ## Local-first workstation topology

## Local-first workstation topology

```text
repo/
├── apps/
│   └── desktop-shell/
│       ├── src/
│       │   ├── local-db/             <- Turso sync wrappers and policies
│       │   ├── sync/                 <- explicit push/pull orchestration
│       │   ├── shell/
│       │   ├── interactive/
│       │   └── views/
├── apps/gateway/
├── services/compute/
├── packages/shared-core/
└── packages/schemas/
```



