# Product Shape Recommendation Matrix

## Imported baseline content`r`n`r`nSource: [00-full-source-port.md](./00-full-source-port.md)

---

### Source section: ## Product-shape recommendation matrix

## Product-shape recommendation matrix


---

### Source section: ## If the product is a desktop productivity workbench

## If the product is a desktop productivity workbench

prefer:

- **default federation**

because:

- Electrobun shell matters
- Solid shell matters
- HTMX probably helps for settings and admin-ish surfaces
- Elm can be bounded to one complex feature
- C++ core can grow only where justified


---

### Source section: ## If the product is mostly forms, queues, approvals, reports, and ops

## If the product is mostly forms, queues, approvals, reports, and ops

prefer:

- **hypermedia-first operations architecture**

because:

- HTML-first and server-authored routes will likely beat SPA ceremony
- the shell can stay thin and useful
- HTMX gets to do the thing it is actually good at


---

### Source section: ## If the product is a planner, editor, simulator cockpit, or workflow engine

## If the product is a planner, editor, simulator cockpit, or workflow engine

prefer:

- **Elm-centric deterministic architecture**

because:

- deep state transitions are the product
- TEA discipline is worth the boundary cost


---

### Source section: ## If the product is a native compute system with clients around it

## If the product is a native compute system with clients around it

prefer:

- **compute-first native platform architecture**

because:

- C++ and Drogon are closer to the value center than TS composition


---

### Source section: ## If the product is primarily visual, shader-heavy, or GPU-accelerated

## If the product is primarily visual, shader-heavy, or GPU-accelerated

prefer:

- **GPU-first visualization workbench architecture**

because:

- Slang and WebGPU become genuine first-class citizens instead of decoration



