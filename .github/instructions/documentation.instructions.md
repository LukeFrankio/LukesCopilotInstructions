---
description: 'Documentation authoring and generated-doc systems guidelines (Doxygen, Haddock, Javadoc, docstrings, manuals, and zero-redundancy policy)'
applyTo: '**'
---

# Documentation Instructions (Write It Once, Explain It Well, Don’t Repeat Yourself Into Oblivion)

> "documentation should teach the truth exactly once, then link to it like a civilized engineer"

uwu this file governs **all documentation work** in this repository:
source comments, API reference comments, module docs, package docs, manuals,
README-style narrative text, generated-doc configuration, examples, search
metadata, and the invisible architecture that makes documentation actually
useful instead of merely long.

this file replaces the old narrow “Doxygen-only” mindset with something more
based and more complete:

- Doxygen where C and C++ need precise symbol docs
- Haddock where Haskell wants source-adjacent semantic docs
- Javadoc where Java insists on living in classes
- Google-style docstrings where Python tries its best
- Markdown/manual pages where readers need narrative guidance
- one shared policy for structure, clarity, searchability, cross-linking,
  examples, and **non-redundancy**

if you are documenting code, a build system, a library surface, a public API, a
CLI, a module tree, or a concept that future readers must understand, this file
is LAW.

## Core Philosophy

- **documentation is part of the product**
- **clarity beats cleverness**
- **truth beats decoration**
- **structure beats dumping text everywhere**
- **one canonical explanation beats five paraphrased duplicates**
- **examples are mandatory for non-trivial behavior**
- **cross-links are mandatory when concepts recur**
- **searchability matters**
- **generated docs should be buildable, reproducible, and reviewable**
- **tool-specific syntax is secondary to semantic quality**
- **file-level rationale belongs at file level**
- **local docs should explain local behavior, not restate global doctrine**
- **long documentation is welcome only when each section adds new value**
- **if a reader learns nothing new from a paragraph, that paragraph is on thin ice**

## Why Documentation Usually Fails

Most documentation is not bad because the author was lazy.
It is bad because the author mixed together five different jobs and then let
all of them repeat each other:

1. global rationale
2. local behavior
3. syntax facts the tool already knows
4. example material
5. warning text

The result is familiar and cursed:

- every function repeats the same file-level history lesson
- wrappers restate the algorithm instead of documenting what the wrapper adds
- examples differ cosmetically but teach nothing new
- cross-links are missing, so the same explanation is copy-pasted everywhere
- comments describe the signature rather than the semantics
- generated docs build, but readers still cannot answer practical questions

we do not do that here.

## Canonical Rationale Rule

**A major rationale must have one canonical home.**

If a concept explains the whole file, whole module, whole subsystem, or whole
family of symbols, explain it **once** at that level.
Then use cross-references from lower-level documentation instead of re-litigating
that same explanation in every symbol block.

This matters so much that it gets its own doctrine section.

### What belongs in the canonical home

The canonical home should contain the full explanation for things like:

- why this file exists
- why this module exists
- why an algorithm family was chosen over alternatives
- why a magic constant exists
- why a type family uses a particular representation
- why a documentation convention exists for the whole subsystem
- what recurring constraints apply to every symbol in a cluster

### What belongs in local symbol docs instead

Local symbol docs should focus on what is specific to the symbol:

- what the symbol does
- its inputs, outputs, and side effects
- its preconditions and postconditions
- edge cases and failure modes
- complexity and performance characteristics
- what distinguishes it from its siblings or wrappers
- how it composes with nearby APIs

### The bad pattern

```cpp
/**
 * @brief Uses the project’s golden-ratio hash mixing strategy.
 *
 * [five lines explaining the same project-wide hashing rationale]
 */
auto hash_combine(...);

/**
 * @brief Iterates a range and uses the project’s golden-ratio hash mixing strategy.
 *
 * [the same five lines again]
 */
auto hash_combine_range(...);

/**
 * @brief Hashes an array and uses the project’s golden-ratio hash mixing strategy.
 *
 * [the same five lines a third time]
 */
auto hash_combine_array(...);
```

### The good pattern

```cpp
/**
 * @file hash_support.hpp
 * @brief Shared hash-mixing support for compound values.
 *
 * This file centralizes the rationale for the chosen hash-mixing strategy,
 * the distribution goals, and the constant-selection story.
 */

/**
 * @brief Mixes one precomputed hash into an existing seed.
 *
 * See the file-level rationale for the mixing strategy itself.
 * This function documents only the mixing formula, the seed semantics,
 * order sensitivity, and the return contract.
 */
auto hash_combine(...);

/**
 * @brief Applies `hash_combine` across a range in iteration order.
 *
 * This wrapper documents iteration order, range requirements, and how empty
 * ranges behave. It does not re-explain the global strategy.
 */
auto hash_combine_range(...);
```

### The enforcement question

Before adding explanatory prose, ask:

- is this the first and best place for this explanation?
- does this paragraph teach something new here?
- should this be a `@see` / `See Also` / internal link instead?
- is the reader better served by a cross-reference than a duplicate essay?

if the answer is “this is already explained above,” then **link, don’t clone**.

## The Documentation Stack

Documentation has layers. Good docs keep those layers separate.

### Layer 1: narrative overview

This is where you explain:

- purpose
- system boundaries
- design goals
- mental model
- trade-offs
- architecture

Examples:

- README sections
- module overviews
- package docs
- file headers
- top-level manual pages
- guide pages

### Layer 2: reference semantics

This is where you explain:

- what a symbol means
- constraints
- invariants
- contracts
- side effects
- error behavior
- complexity

Examples:

- function docs
- class/type docs
- enum docs
- field docs
- macro docs
- type alias docs

### Layer 3: discovery support

This is where you optimize for:

- search results
- index pages
- cross-links
- stable anchors
- related-symbol navigation
- grouping

Examples:

- `@brief` text
- module/group titles
- index labels
- heading IDs
- `@see` / `See Also`
- qualified names in prose

### Layer 4: operational reproducibility

This is where you ensure:

- docs build consistently
- configs are versioned
- outputs are predictable
- advanced features are intentional
- toolchain dependencies are explicit

Examples:

- Doxyfile / config rules
- Haddock invocation rules
- build-system integration
- search index generation
- diagram tool dependencies

## Documentation Scope Hierarchy

Every documentation element has a natural scope.
Explain it at the right scope or suffer duplication goblins.

### Scope order

From widest to narrowest:

1. repository or package
2. guide page or main page
3. module / namespace / file
4. type / class / trait / interface / record
5. member / method / function / macro / alias / constant
6. parameter / field / enum item / local example note

### Rule

Explain each idea at the narrowest scope that still covers all of its real users.

If a fact is true for the whole file, it belongs in the file.
If a fact is true for one function, it belongs in that function.
If a fact is true for every overload in a family, document it at the family or
page level and let the overloads stay specific.

## Documentation Ownership

One symbol, one owner, one canonical explanation.

### Ownership rules

- each file has one file-level doc block or page-level owner
- each public type has one canonical type-level doc block
- each public function has one canonical symbol-level doc block
- each reusable concept has one canonical narrative section
- each example has one canonical purpose
- each configuration pattern has one canonical exemplar

### What to avoid

- same symbol documented in header and source with conflicting detail
- same concept described independently in five files
- wrapper docs that restate the underlying helper’s full rationale
- examples copied between README and API docs with drift

## The Universal Documentation Contract

Every high-value documentation block should answer the right subset of the
following questions.
Not every symbol needs every answer, but the questions form the review frame.

### Meaning

- what is this thing?
- why does it exist?
- what role does it play in the larger system?

### Contract

- what goes in?
- what comes out?
- what assumptions must hold?
- what remains true before and after use?

### Behavior

- what does it do in normal cases?
- what does it do in edge cases?
- what does it do when inputs are empty, zero, null-like, or invalid?

### Failure

- can it fail?
- how does failure surface?
- what should the caller or reader expect?

### Cost

- what is the complexity?
- is there memory allocation?
- are there expensive steps or hidden work?
- are there runtime vs compile-time trade-offs?

### Composition

- what related APIs should the reader see next?
- what should this be used with?
- what should it not be mixed with?

### Evidence

- is there an example?
- is there a note about invariants or correctness?
- is there enough context to use it without opening the implementation?

## What Different Levels Must Contain

This section is the base template system for the whole file.

## File-Level Documentation

A file header is where you explain the shared story once.
It is the canonical home for file-wide rationale.

### A file header must include

- the file identity
- a one-line description
- the file’s job in the system
- why the implementation or representation exists
- important constraints or assumptions
- major dependencies or collaborators if relevant
- what this file deliberately does **not** do
- one high-value example or usage sketch if the file is an API surface

### A file header must not become

- a line-by-line commentary on everything below
- a repeated paste of the project philosophy
- a dumping ground for changelog notes unrelated to current use
- a duplicate of the README

### Good file-header topics

- “this file defines the immutable configuration model used by all parsers”
- “this file centralizes hash mixing so all compound hashers share one policy”
- “this module exposes the public numeric API while hiding representation details”
- “this page explains the manual generation workflow and publishing stages”

### Weak file-header topics

- “this file contains functions”
- “this file is important”
- “this file has code for the system”
- the same generic purity paragraph that appears everywhere else

### Generic file-header template for C-like languages

```cpp
/**
 * @file example.hpp
 * @brief One-line description with actual meaning.
 *
 * Explain the file’s purpose, scope, and the design rationale that applies
 * to multiple symbols inside the file. Put major shared context here once.
 *
 * Cover:
 * - what problem this file solves
 * - what assumptions or invariants the whole file shares
 * - why this approach exists
 * - what readers should know before using anything in this file
 *
 * @note State cross-cutting constraints here once instead of repeating them
 *       in every function.
 * @see Related pages, modules, or companion files.
 *
 * @code cpp
 * // small generic usage sketch
 * auto value = api::make_value();
 * auto text = api::render(value);
 * @endcode
 */
```

### Generic file-header template for Markdown pages

```markdown
# Topic Title

A one-paragraph explanation of the page’s purpose, scope, and intended reader.

This page covers:
- what the reader is trying to do
- what system area this page describes
- what is assumed knowledge
- where to go next
```

## Module, Namespace, Package, and Page Documentation

This layer explains structure above the symbol level.

### Use this level to document

- subsystem boundaries
- conceptual groups
- workflow stages
- public vs internal partitions
- module relationships
- page hierarchies

### This level should answer

- who should read this module/page?
- what concepts live here?
- what concepts live elsewhere?
- how should readers navigate this cluster?

### Good module/page docs often contain

- a purpose paragraph
- a bullet list of responsibilities
- a bullet list of non-responsibilities
- a short navigation map
- cross-links to adjacent modules/pages
- one end-to-end example or flow sketch

### Generic namespace/module template

```cpp
/**
 * @namespace example
 * @brief Short semantic description.
 *
 * Explain what kind of functionality belongs here, what the namespace/module
 * represents, and how readers should think about its contents.
 *
 * Responsibilities:
 * - thing one
 * - thing two
 *
 * Out of scope:
 * - thing three
 * - thing four
 *
 * @see example::detail
 * @see example::helpers
 */
namespace example {
```

### Generic page template

```cpp
/**
 * @page example_workflow Example Workflow
 * @brief High-level workflow for a feature or subsystem.
 *
 * Start with intent, then the flow, then the caveats.
 *
 * @section example_workflow_overview Overview
 * Explain what this workflow achieves.
 *
 * @section example_workflow_steps Steps
 * 1. step one
 * 2. step two
 * 3. step three
 *
 * @section example_workflow_related Related Material
 * - @ref example_api
 * - @ref example_troubleshooting
 */
```

## Type-Level Documentation

Types are where invariants live.
If a type exists, it usually exists to make an invariant explicit.
Document that invariant.

### Types that deserve full docs

- public classes
- public structs
- public records
- sum types / enums with semantic meaning
- protocol/trait/interface types
- type aliases that carry domain meaning
- templates/generics with meaningful constraints

### Type docs should include

- what the type represents
- what invariants or constraints it maintains
- how it should be constructed or obtained
- what makes it different from nearby types
- when immutability/mutability matters
- whether it is a value type, handle, view, adapter, builder, descriptor, etc.

### Type docs should not spend half their length on

- the whole subsystem’s history
- every operation the type supports if those operations have their own docs
- generic philosophical filler

### Good type-level questions

- what makes a valid instance?
- can a default/empty instance exist?
- what state is always preserved?
- is this a semantic type or a transport/helper type?
- what lifetime or ownership rules matter?

### Generic type template

```cpp
/**
 * @class ExampleType
 * @brief One-sentence semantic summary.
 *
 * Explain what the type represents and which invariants it preserves.
 * Focus on identity, ownership, validity, and how the type participates in
 * the larger system.
 *
 * Invariants:
 * - invariant one
 * - invariant two
 *
 * Typical use:
 * - acquired from X
 * - passed to Y
 * - not meant to outlive Z
 *
 * @note Mention representation constraints only if they affect users.
 * @warning Mention surprising behavior once and clearly.
 *
 * @code cpp
 * ExampleType value = make_example();
 * use_example(value);
 * @endcode
 */
class ExampleType {
```

### Generic enum template

```cpp
/**
 * @enum Mode
 * @brief Semantic mode selector for an operation.
 *
 * Explain the difference between the modes, not just their names.
 * State when each mode should be chosen.
 */
enum class Mode {
    /** @brief Conservative behavior with maximal validation. */
    Conservative,

    /** @brief Balanced default behavior for typical production use. */
    Balanced,

    /** @brief Aggressive behavior with fewer safety rails. */
    Aggressive,
};
```

### Type alias documentation template

```cpp
/**
 * @typedef BufferId
 * @brief Stable identifier for a cached buffer.
 *
 * Explain the semantic meaning of the alias. If it exists only to shorten a
 * verbose type, say so; if it prevents domain confusion, say that instead.
 */
using BufferId = std::uint64_t;
```

## Function and Method Documentation

Functions are where contracts live.
Document the contract, not the spelling of the signature.

### Functions that require full docs

- public API functions
- non-obvious helpers
- algorithmically meaningful helpers
- wrappers that add important behavior
- anything with surprising failure, ownership, or cost semantics
- anything a reader could misuse without guidance

### Functions that may use lighter docs

- tiny obvious getters with no caveats
- purely mechanical forwarding functions
- private helpers whose meaning is obvious in a tightly scoped implementation

Even then, if the helper is public or reused heavily, document it properly.

### Function docs should include the right subset of

- brief purpose
- detailed behavior
- parameters
- return value
- error or failure mode
- side effects
- purity status where relevant
- preconditions
- postconditions
- invariants affected or preserved
- complexity
- performance notes
- examples
- related APIs

### What good function docs sound like

- “Parses an absolute path and normalizes separators without resolving symlinks.”
- “Combines a precomputed hash into an existing seed; order is significant.”
- “Allocates a new buffer and transfers ownership to the caller.”
- “Returns a lazy view over filtered items; iteration performs the predicate.”

### What weak function docs sound like

- “Gets the value.”
- “Sets the option.”
- “Handles processing.”
- “Performs operation.”
- “This function is used to…” with no specific contract

### Purity status policy

If purity is important to the language, subsystem, or workflow, mark it.
Do not turn purity marking into boilerplate spam.

#### When to mark purity explicitly

- functional or math-heavy APIs
- constexpr/compile-time helpers
- deterministic transformation utilities
- IO or stateful functions where impurity matters to the caller

#### Good purity marking

```cpp
/**
 * @brief Normalizes a path string without touching the filesystem.
 *
 * ✨ PURE FUNCTION ✨
 *
 * Same input, same output. No I/O. No hidden state.
 */
auto normalize_path(std::string_view text) -> std::string;
```

#### Good impurity marking

```cpp
/**
 * @brief Loads a configuration file from disk.
 *
 * ⚠️ IMPURE FUNCTION ⚠️
 *
 * Performs file I/O and may fail due to environment state.
 */
auto load_config(std::filesystem::path const& path) -> Result<Config, Error>;
```

#### Bad purity marking

- repeating the exact same bullet list under every trivial helper
- writing five lines of purity doctrine for a one-line obvious constant accessor
- marking purity but never documenting the actual contract

### Generic function template

```cpp
/**
 * @brief One-line semantic summary.
 *
 * Explain what the function does, how it interprets its inputs, and any local
 * behavior that is not obvious from the signature.
 *
 * ✨ PURE FUNCTION ✨
 *
 * @param[in] input Describe the semantic meaning, not just the type.
 * @param[in] mode Explain how it changes behavior.
 * @return Describe the result and any sentinel/empty/error meaning.
 * @pre Explain any required conditions before calling.
 * @post Explain what is guaranteed afterward.
 * @note Mention behavior that matters but does not fit elsewhere.
 * @warning Mention surprising or dangerous cases.
 * @complexity O(n) time where n is the number of items processed.
 *
 * @code cpp
 * auto result = do_thing(input, Mode::Balanced);
 * @endcode
 */
auto do_thing(Input input, Mode mode) -> Output;
```

### Wrapper-function policy

Wrappers are where many docs go bad.

If a wrapper exists around another function, document **what the wrapper adds**:

- container traversal
- iteration order
- ownership conversion
- allocation behavior
- validation layer
- logging side effect
- exception/result translation
- caching behavior
- thread-safety or synchronization implications

Do **not** re-explain the underlying algorithm unless the wrapper changes it.

#### Bad wrapper doc

```cpp
/**
 * @brief Applies the project’s fast normalization algorithm.
 *
 * [full algorithm story duplicated from the core normalizer]
 */
auto normalize_all(std::span<Item const> items) -> std::vector<Item>;
```

#### Good wrapper doc

```cpp
/**
 * @brief Applies `normalize_one` to each item in input order.
 *
 * Returns a new vector, preserves element order, and stops at the first
 * reported error.
 *
 * See `normalize_one` for the normalization semantics themselves.
 */
auto normalize_all(std::span<Item const> items) -> Result<std::vector<Item>, Error>;
```

### Overload documentation policy

Overloads should share common meaning without duplicating paragraphs blindly.

#### Use one of these patterns

- one canonical page/section for the overload family plus concise per-overload docs
- one main overload with full docs and sibling overloads that reference it
- per-overload full docs only when semantics materially differ

#### If overloads differ only by convenience

Document one of them fully and let others say things like:

- “Equivalent to calling X with default mode Y.”
- “Convenience overload that allocates the output container internally.”
- “String-view overload; semantics match the span overload.”

## Parameter Documentation

Parameter docs should explain meaning and constraints, not just rename the type.

### Weak parameter docs

- `@param value The value.`
- `@param path Path.`
- `@param flag Flag.`

### Good parameter docs

- `@param value Inclusive upper bound for the generated range.`
- `@param path Path to the user-supplied configuration file; may be relative.`
- `@param flag Enables strict validation of unknown fields.`

### Parameter questions

- what kind of thing is this semantically?
- is there a valid range?
- can it be empty?
- who owns it?
- is it borrowed, copied, consumed, mutated, or observed?
- what is the unit?
- what happens if it is invalid?

## Return-Value Documentation

Return docs must explain meaning, not just type.

### Good return docs

- “Returns the normalized path with redundant separators removed.”
- “Returns a view that remains valid while the source container outlives it.”
- “Returns `nullopt` when the key is absent.”
- “Returns an error result if parsing fails or if required fields are missing.”

### Weak return docs

- “Returns a string.”
- “Returns the result.”
- “Returns success or failure.”

If success and failure are values, say exactly what each means.

## Error, Failure, and Warning Documentation

If a caller can get this wrong, the docs should help them not do that.

### Document failure clearly

Use the most appropriate mechanism for the language/tool:

- `@throws`
- `Raises:`
- `Either` / `Result` explanation
- explicit warning and note text
- documented sentinel/empty/null behavior

### Good failure documentation answers

- what conditions cause failure?
- what shape does failure take?
- what remains unchanged after failure?
- can the caller recover?
- is failure expected/normal or exceptional?

### Generic failure documentation block

```cpp
/**
 * @throws ParseError if the input token stream is malformed.
 * @throws IOError if the source cannot be read.
 * @post On failure, no output state has been committed.
 */
```

### Warning policy

Warnings should be reserved for genuinely surprising or dangerous behavior.
Do not use warning sections to restate normal contract details.

## Complexity and Performance Documentation

Complexity notes are not optional for algorithmic APIs.
They help callers choose correctly.

### Document complexity when

- runtime cost is non-trivial
- memory allocation occurs
- asymptotic behavior matters
- one overload is materially cheaper than another
- lazy vs eager behavior matters
- compile-time cost is significant for template/meta/constexpr APIs

### Good complexity docs

- `O(n) time where n is the number of parsed records`
- `O(log n) lookup after O(n log n) preprocessing`
- `Allocates one output buffer sized to the normalized input`
- `Compile-time cost scales with the number of fields in the reflected type`

### Weak complexity docs

- “Fast”
- “Efficient”
- “Optimized”
- “Low overhead” without context

## Member and Field Documentation

Field docs should explain semantic role, invariants, and ownership when needed.

### Good field docs answer

- what does this field mean?
- what invariant does it participate in?
- can readers or callers depend on it directly?
- why is it stored rather than computed?

### Generic field template

```cpp
/**
 * @brief Stable identifier used for cache lookups.
 *
 * Remains valid for the lifetime of the owning object and is never reused
 * within a single process instance.
 */
std::uint64_t id_;
```

### Inline field docs are fine when simple

```cpp
std::size_t size_;   ///< Number of active elements, never exceeds capacity_.
```

### When inline docs are not enough

Use a full block if the field’s meaning is subtle, if it participates in an
important invariant, or if ownership/lifetime semantics matter.

## Constant Documentation

Constants deserve docs when they carry domain meaning, not only when they exist.

### Document constants well when they are

- semantically loaded
- magic-looking but meaningful
- part of a protocol or format
- chosen due to a mathematical or engineering trade-off
- consumed directly by users or maintainers

### Constant docs should include

- what the constant means
- why its value is what it is
- units or scale where relevant
- whether callers should depend on it directly

### Constant docs should not do

- re-explain the entire file’s strategy if that is already in the file header
- repeat the same long derivation under every wrapper that uses the constant

### Good constant template

```cpp
/**
 * @brief Default timeout for handshake negotiation, in milliseconds.
 *
 * Chosen to cover slow startup paths without making dead peers feel
 * indefinitely alive.
 */
inline constexpr std::uint32_t default_handshake_timeout_ms = 2'000;
```

## Macro Documentation

Macros are dangerous and therefore must be documented better, not worse.

### Macro docs should include

- what the macro expands to semantically
- argument expectations
- side effects or multiple-evaluation hazards
- why this is a macro instead of a function or constant
- portability/compiler assumptions

### Macro anti-pattern

Never document a macro like it is a normal pure function if it is not one.
If it evaluates arguments multiple times, say so loudly.

### Generic macro template

```cpp
/**
 * @def EXAMPLE_ASSERT(expr)
 * @brief Validates a condition and aborts the current operation on failure.
 *
 * Evaluates `expr` exactly once and emits a diagnostic in debug builds.
 * In release builds it compiles away.
 *
 * @warning Do not pass expressions with required side effects if the macro may
 *          compile to a no-op in some build modes.
 */
#define EXAMPLE_ASSERT(expr) /* ... */
```

## Template and Generic Documentation

Templates, generics, and type classes must document their constraints.

### Document

- what `T` / `E` / `F` / `Alloc` / `Policy` must provide
- whether ownership or lifetime assumptions exist
- any concept/protocol/trait expectations
- performance assumptions tied to the generic parameter

### Weak template docs

- `@tparam T A type.`

### Good template docs

- `@tparam Range An input range whose elements are parseable tokens.`
- `@tparam Alloc Allocator used for output buffers; must satisfy the standard allocator contract.`
- `@tparam Error Error payload type stored on failure results.`

## Example Policy

Examples are mandatory for anything non-trivial.
But examples must earn their keep.

### Every example must have a job

An example should do one of the following:

- show the default/common case
- show an edge case
- show failure handling
- show composition with related APIs
- show lifecycle/ownership behavior
- show configuration or setup sequence
- show integration into a larger workflow

If it does none of those, it is decorative noise.

### The minimum example taxonomy

For any non-trivial public API, aim for one or more of:

1. **basic example**
2. **edge-case example**
3. **integration or composition example**

### Basic example

Shows the expected happy path.

```cpp
/**
 * @code cpp
 * auto parser = make_parser();
 * auto result = parser.parse("name = value");
 * if (result) {
 *     use(*result);
 * }
 * @endcode
 */
```

### Edge-case example

Shows empties, zeros, errors, invalid states, or unusual boundaries.

```cpp
/**
 * @code cpp
 * auto result = parser.parse("");
 * if (!result) {
 *     report(result.error());
 * }
 * @endcode
 */
```

### Composition example

Shows how the API works with adjacent tools.

```cpp
/**
 * @code cpp
 * auto data = load_text(path);
 * auto tree = parse_config(data).value();
 * auto view = build_runtime_view(tree);
 * run(view);
 * @endcode
 */
```

### Example rules

- examples must be generic and reusable
- examples must be syntactically correct for the language shown
- examples must not rely on missing context unless the missing context is obvious
- examples must not contradict the documented contract
- examples should prefer realistic naming over `foo`, `bar`, and `baz` sludge
- examples should show failure handling when failure is part of the contract
- examples should not repeat the same behavior with different variable names

### Example anti-patterns

#### Semantically duplicate examples

```cpp
// ❌ Example 1
process("alpha");

// ❌ Example 2
process("beta");
```

If the only new information is a different string literal, that second example
is dead weight.

#### Unhelpful toy example

```cpp
// ❌ Too small to teach meaning
Thing t;
use(t);
```

#### Example that hides the interesting part

```cpp
// ❌ Reader learns nothing about the documented API
auto app = make_app();
app.run();
```

### Example placement

Use examples in the narrowest useful scope:

- file/module/page example when the flow is cross-cutting
- type example when the type’s lifecycle matters
- function example when the function’s contract matters

Do not paste the same example at all three levels.

## Cross-Reference Policy

A long instruction file without cross-links becomes a maze.
A codebase without related-links becomes archaeology.

### Always cross-link when

- a symbol depends on another symbol’s semantics
- a wrapper delegates to a canonical helper
- a page introduces a concept with an API reference elsewhere
- a type and its constructor/accessor functions belong together
- a config section explains behavior referenced elsewhere
- a failure mode has a troubleshooting page/section

### Good cross-reference language

- “See the file-level rationale for the normalization strategy.”
- “See `normalize_one` for per-item semantics.”
- “See the module overview for lifecycle rules.”
- “See also `Result`, `parse_file`, and `load_text`.”

### Weak cross-reference language

- “see above” with no anchor
- “related function” with no symbol name
- “see docs” without telling readers where

### Related-symbol sections should be curated

Use `@see` / `See Also` / link lists for:

- siblings in the same family
- inverse or paired operations
- constructors and destructors
- owning and non-owning views
- low-level and high-level entry points
- canonical pages or guide sections

Do not dump twenty barely-related symbols into a `See Also` section just because
hyperlinks exist.

## Searchability and Indexability

Documentation is not only read linearly.
It is searched, indexed, and skimmed.
Write for that reality.

### Searchable docs need

- strong first sentences
- concrete nouns
- likely search terms
- consistent naming
- stable anchors
- exact symbol names where ambiguity exists
- readable group/page titles

### Good brief descriptions

- “Parses a UTF-8 configuration document into an immutable syntax tree.”
- “Formats a duration as a human-readable `HH:MM:SS` string.”
- “Combines a precomputed hash into an existing seed in iteration order.”

### Bad brief descriptions

- “Utility function.”
- “Helper for processing.”
- “Handles config.”
- “Data model class.”

### Naming rules for searchable docs

- spell out important domain terms at least once
- include both acronym and expanded form when likely searched both ways
- keep section titles explicit
- prefer qualified names when ambiguity is possible
- ensure symbol docs mention the module/subsystem context if the name is generic

### Index rules

- short option names and long option names should both be searchable
- symbolic names deserve index support too
- aliases should converge on one canonical target
- readers should be able to browse alphabetically, not only via JS search

## Narrative vs Reference Writing

These are not the same genre.
Do not confuse them.

### Narrative docs should answer

- what is this subsystem for?
- how do I approach it?
- what are the stages or workflow?
- what should I read next?

### Reference docs should answer

- what exactly does this symbol mean?
- how do I call it?
- what guarantees does it make?
- what are the edge cases?

### A narrative page should not be

- a raw index dump
- a list of signatures
- a clone of symbol docs without new flow or framing

### A reference page should not be

- a wandering essay with no contract details
- a high-level architecture page pretending to be API docs

## Concision vs Completeness

This repository likes excessive documentation.
Good. Same.
But “excessive” is not permission to be repetitive.

### Completeness means

- no missing critical contracts
- enough examples to teach real use
- real explanation of invariants and edge cases
- reader can act without opening implementation

### Repetition means

- same rationale pasted into multiple symbols
- same warning repeated on every helper
- same example dressed up with different identifiers
- multiple sections restating the same doctrine

### The goal

Be exhaustive about **distinct information**.
Be ruthless about duplicated information.

## Reviewer Heuristics

Reviewers should ask these questions when inspecting docs.

### Canonical-home questions

- where is the best place for this explanation to live?
- is this block the canonical home, or should it link elsewhere?
- would moving this paragraph upward reduce duplication?

### Locality questions

- does this symbol doc explain only what is unique here?
- is this wrapper documenting wrapper behavior rather than re-telling the core helper?
- does this field doc explain the field’s role, not the whole type?

### Example questions

- does each example have a distinct teaching purpose?
- could any example be removed without losing knowledge?
- is failure behavior shown when it matters?

### Searchability questions

- is the first sentence actually useful in search results?
- would a new teammate know what to search for after reading this?
- are related symbols and pages linked clearly?

### Buildability questions

- are code fences valid?
- are anchors/links stable?
- are tool-specific commands syntactically correct?
- does the config guidance look reproducible?

## Universal Anti-Patterns

These apply regardless of tool.

### ❌ Anti-pattern: syntax narration

```cpp
/**
 * @brief Takes a string and returns a string.
 */
auto format_name(std::string_view text) -> std::string;
```

The signature already told us that.
Document the semantics.

### ❌ Anti-pattern: subsystem history in every symbol

```cpp
/**
 * @brief Parses a token.
 *
 * This project uses parser strategy X because of system-wide design goal Y...
 * [repeated everywhere]
 */
```

Put the strategy rationale at page/module/file scope once.

### ❌ Anti-pattern: duplicate examples

```cpp
/**
 * @code cpp
 * parse("a");
 * @endcode
 *
 * @code cpp
 * parse("b");
 * @endcode
 */
```

Unless the difference matters semantically, cut one.

### ❌ Anti-pattern: warning inflation

If everything gets a warning block, nothing feels dangerous.
Use warnings only for surprising, risky, or commonly misused behavior.

### ❌ Anti-pattern: cross-link absence

If the reader has to manually search the codebase for the related concept every
single time, the documentation architecture failed.

### ❌ Anti-pattern: tool-specific cleverness over clarity

Do not bend markup into acrobatics when a simple paragraph, list, or cross-link
would be clearer.

## Universal Quality Checklist

Before calling documentation “done,” ask whether the work:

- [ ] explains meaning, not just syntax
- [ ] centralizes major rationale instead of duplicating it
- [ ] documents local behavior at local scope
- [ ] includes distinct examples where needed
- [ ] documents edge cases and failure modes clearly
- [ ] includes search-friendly summaries
- [ ] cross-links related symbols/pages/modules
- [ ] names invariants and constraints explicitly
- [ ] includes complexity/cost notes where relevant
- [ ] is mechanically buildable for the chosen toolchain
- [ ] avoids repeated boilerplate that teaches nothing new
- [ ] leaves future readers with fewer questions than before

## Doxygen and Generated-Reference Systems

The remaining sections of this file get tool-specific, but the policy above
still rules everything below.

Doxygen, Haddock, Javadoc, and docstrings differ in syntax.
They should not differ in documentation quality.

## Doxygen Guidance (C, C++, Mixed Native Code, and Reference-Heavy APIs)

Doxygen is excellent when you need:

- symbol-level API reference
- file and namespace pages
- grouped modules
- rendered call/include/relationship diagrams
- cross-linkable static output
- source-adjacent docs in C-family code

Doxygen is not a substitute for thinking.
If you feed it repetitive or low-information comments, it will generate
high-volume low-value HTML with tremendous confidence. We do not stan that.

### Prefer modern Doxygen

- **Prefer Doxygen 1.16+** when available
- **Minimum acceptable: Doxygen 1.15+**
- regenerate config files thoughtfully when upgrading
- review warnings and rendered output after upgrades
- treat new parser/rendering features as opportunities to simplify docs, not to
    create markup circus acts

### When to use Doxygen comments

Use Doxygen comments for:

- public C APIs
- public and semi-public C++ APIs
- internal subsystems whose readers actually rely on generated reference output
- template libraries where symbol relationships matter
- header-heavy codebases where documentation belongs near declarations

Use lighter inline comments instead when:

- a private helper is truly local and obvious
- a one-line invariant note is enough
- a block comment would merely narrate syntax

## Doxygen Comment Forms

Doxygen supports several comment styles.
Use the one that best matches local style, but stay consistent within a file or
subsystem.

### Common block forms

```cpp
/**
 * @brief Block comment style.
 */
```

```cpp
/*!
 * Alternative Doxygen block style.
 */
```

### Common line forms

```cpp
/// Single-line Doxygen style.
```

```cpp
//! Alternative single-line Doxygen style.
```

### Policy

- prefer block comments for file/type/function docs
- prefer inline trailing comments only for tiny, obvious member docs
- do not mix five comment styles in one file unless a strong local convention
    requires it
- choose one primary style per language/subtree and keep it steady

## `@brief` / Brief Description Policy

The brief is often what users see in search results, indices, summary tables,
and quick navigation panels.
Make it do real work.

### A strong brief should

- start with a concrete verb or noun phrase
- identify the semantic purpose
- include domain vocabulary readers might search for
- avoid filler words like “utility” or “helper” unless they are actually part of
    the domain

### Good Doxygen briefs

```cpp
/** @brief Parses a UTF-8 document into an immutable syntax tree. */
```

```cpp
/** @brief Combines a precomputed hash into an existing seed. */
```

```cpp
/** @brief Non-owning view over a validated configuration tree. */
```

### Weak Doxygen briefs

```cpp
/** @brief Utility function. */
```

```cpp
/** @brief Handles processing. */
```

```cpp
/** @brief Data structure class. */
```

## File-Level Doxygen Documentation

In Doxygen, file-level docs are especially important because they can anchor:

- file reference pages
- shared rationale
- page-level navigation
- module/group membership
- examples that span multiple symbols

### Required file tags when meaningful

- `@file`
- `@brief`
- `@see`
- optional `@note`, `@warning`, `@details`, `@code`

### Recommended file-header skeleton

```cpp
/**
 * @file parser.hpp
 * @brief Public parser interface and syntax-tree entry points.
 *
 * This file defines the user-facing parsing API, the error model exposed by the
 * parser, and the types callers use to inspect parsed syntax trees.
 *
 * Put shared rationale here once:
 * - why this API is split across these entry points
 * - what global invariants apply
 * - what design trade-offs affect every symbol below
 *
 * @note Local functions should reference this rationale instead of repeating it.
 * @see parser_overview
 *
 * @code cpp
 * auto tree = parse_text(source).value();
 * auto view = make_view(tree);
 * @endcode
 */
```

### File-header enforcement rule

If you write the same paragraph in two or more symbol docs, ask whether it
belongs in the file header instead.

## Class, Struct, and Type Documentation in Doxygen

Use type-level docs to document:

- meaning
- invariants
- ownership/lifetime model
- relationship to other types
- public usage style

### Useful tags

- `@class`, `@struct`, `@union`, `@typedef`, `@using`
- `@brief`
- `@tparam`
- `@invariant`
- `@note`
- `@warning`
- `@see`
- `@code`

### Recommended class skeleton

```cpp
/**
 * @class ParserView
 * @brief Non-owning view over validated parser output.
 *
 * This type provides read-only access to a syntax tree whose storage is owned
 * elsewhere. Document lifetime and borrowing rules clearly.
 *
 * @invariant The referenced tree outlives the view.
 * @invariant The view never exposes invalid nodes.
 * @note This type does not own memory.
 * @warning Dangling views are possible if the source tree is destroyed first.
 *
 * @code cpp
 * auto tree = parse_text(source).value();
 * ParserView view{tree};
 * inspect(view);
 * @endcode
 */
class ParserView {
```

### Doxygen type-doc rules

- document invariants explicitly when they matter
- document lifetimes explicitly for view/handle/reference-like types
- do not paste every method description into the type block
- do include one example if correct use is non-obvious

## Function Documentation in Doxygen

This is where Doxygen shines, but only if the comments say real things.

### Commonly useful tags

- `@brief`
- `@details`
- `@param`
- `@tparam`
- `@return`
- `@retval`
- `@pre`
- `@post`
- `@throws` / `@exception`
- `@note`
- `@warning`
- `@attention`
- `@see`
- `@code`
- `@par`
- `@complexity` if your project/tooling/style recognizes it consistently

### Recommended function pattern

```cpp
/**
 * @brief Parses one source buffer into a syntax tree.
 *
 * Explain local semantics here:
 * - what input is accepted
 * - whether ownership is transferred
 * - what failure means
 * - what remains valid on success
 *
 * ⚠️ IMPURE FUNCTION ⚠️
 *
 * @param source UTF-8 text to parse.
 * @param path Optional logical path used in diagnostics.
 * @return Parsed tree on success, or a structured parse error.
 * @pre `source` must remain valid for the duration of the call.
 * @post On success, the returned tree owns its storage.
 * @note Diagnostics use `path` only for reporting; no file I/O occurs.
 * @warning The parser rejects embedded NUL bytes.
 * @see parse_file
 *
 * @code cpp
 * auto result = parse_text(source, "config.cfg");
 * if (!result) {
 *     print_error(result.error());
 * }
 * @endcode
 */
auto parse_text(std::string_view source, std::string_view path = {})
        -> Result<SyntaxTree, ParseError>;
```

### Doxygen function-doc rules

- use `@details` only when the brief plus tagged items are not enough
- keep the detail section local to the symbol’s real behavior
- avoid a giant wall of tags when two short paragraphs would read better
- use `@pre` and `@post` only for meaningful contracts, not trivialities
- use `@warning` for surprising misuse hazards, not normal API facts

## Parameter Tag Rules

### `@param` rules

- use the exact parameter name
- describe semantic meaning and constraints
- note units, ranges, lifetime, ownership, or nullability when relevant
- do not merely repeat the type

### Good `@param` examples

```cpp
@param source UTF-8 text buffer to parse.
@param limit Inclusive upper bound for generated values.
@param mode Validation mode controlling unknown-field handling.
```

### Weak `@param` examples

```cpp
@param source The source.
@param limit The limit.
@param mode The mode.
```

## Return and `@retval` Rules

Use `@return` for general meaning.
Use `@retval` when individual named return states matter.

### Good `@return`

```cpp
@return A normalized path string with redundant separators removed.
```

### Good `@retval`

```cpp
@retval true The buffer was accepted and queued for processing.
@retval false The buffer was rejected because capacity was exhausted.
```

### Weak return docs

```cpp
@return A string.
@return Success or failure.
```

## `@details` Policy

`@details` is optional, not mandatory ceremony.

### Use `@details` when you need to explain

- the algorithm at a locally relevant level
- step ordering that affects behavior
- why a contract is shaped a certain way
- behavior that is too complex for a brief paragraph + tags

### Do not use `@details` to

- paste the file-level rationale again
- narrate every obvious implementation step
- hide important contract points that should have been `@warning`, `@pre`, or
    `@return`

## `@note`, `@warning`, and `@attention`

These tags are useful only when they remain high-signal.

### Use `@note` for

- clarifications
- subtle but non-dangerous behavior
- portability or performance remarks
- local caveats that do not change the core contract

### Use `@warning` for

- dangerous misuse
- non-obvious invalidation or ownership hazards
- data loss or correctness traps
- security-sensitive mistakes

### Use `@attention` sparingly for

- operationally critical requirements
- one-time migration landmines
- “if you miss this, everything breaks” material

If every block gets all three, the tags have lost their meaning.

## `@see` and Cross-Linking in Doxygen

Doxygen can link a lot automatically, but that is not enough.
You still need to choose meaningful related material.

### Use `@see` for

- sibling overloads with different trade-offs
- lower-level helpers and higher-level wrappers
- inverse operations
- canonical guide pages
- related types that must be understood together

### Good `@see` lists

```cpp
@see parse_file
@see parse_stream
@see @ref parser_overview
```

### Bad `@see` lists

- fifteen tangentially related helpers
- symbols with no explanation of relationship
- “see also” plus names that differ only cosmetically

## Groups, Modules, and Hierarchical Structure

Doxygen supports grouping because readers need conceptual structure, not a flat
bag of symbols.

### Use groups when you need

- a public module index
- grouped feature families
- separate internal/public partitions
- high-level landing pages for APIs with many entry points

### Common group commands

- `\defgroup`
- `\addtogroup`
- `\ingroup`
- `\weakgroup`
- `@{` and `@}` for member ranges

### Group policy

- groups should reflect conceptual boundaries, not arbitrary file boundaries
- group titles should help a reader browse, not merely mirror folder names
- nested groups are fine when they genuinely improve discovery
- do not create a group per tiny helper just because the syntax exists

### Generic group example

```cpp
/**
 * @defgroup parsing Parsing API
 * @brief Facilities for turning text into validated syntax trees.
 *
 * This group contains the public parsing entry points, shared parse-result
 * types, and navigation helpers for parse diagnostics.
 */

/** @ingroup parsing */
auto parse_text(std::string_view source) -> Result<SyntaxTree, ParseError>;

/** @ingroup parsing */
auto parse_file(std::filesystem::path const& path) -> Result<SyntaxTree, ParseError>;
```

### Grouping anti-patterns

- documenting the same concept once in a group and then repeating it in every
    member without adding local semantics
- groups with vague names like “Helpers” or “Utilities” when a domain term exists
- giant groups with no substructure when the API surface is large

## Pages and Standalone Documentation in Doxygen

Use pages for narrative docs that do not belong to a single symbol.

### Common page commands

- `\mainpage`
- `\page`
- `\subpage`
- section commands like `\section` and `\subsection`

### Use pages for

- subsystem overviews
- workflow docs
- migration guides
- architecture notes relevant to multiple files
- performance or troubleshooting guides

### Good page structure

1. reader-oriented opening paragraph
2. problem statement or purpose
3. conceptual model
4. workflow or usage path
5. pitfalls / caveats
6. related APIs/pages

### Generic main page example

```cpp
/**
 * @mainpage Library Documentation
 *
 * Welcome paragraph that says what the library does and where a new reader
 * should start.
 *
 * @section getting_started Getting Started
 * Show the shortest correct path to first success.
 *
 * @section architecture Architecture
 * Explain the main components and why they are separated.
 *
 * @section related Related Material
 * - @ref parsing
 * - @ref formatting
 * - @ref troubleshooting
 */
```

### Page policy

- pages should tell stories or workflows, not restate symbol reference output
- page-level rationale is a great place for shared doctrine that would otherwise
    repeat inside individual symbol docs
- if several files repeat the same overview text, convert that overview into a
    page and link to it

## Markdown in Doxygen

Modern Doxygen understands a useful subset of Markdown and mixes it with native
commands.
Use that power to improve clarity, not to create markup soup.

### Prefer Markdown for

- lists
- code fences
- emphasis
- tables when they render cleanly
- readable paragraphs

### Prefer Doxygen commands for

- semantic tagging like `@param`, `@return`, `@see`
- grouping/page structure
- explicit cross-reference control
- tool-specific constructs like `@dot` or `@msc`

### Mixed-style rule

Use the simplest combination that remains readable in source **and** output.

### Lists

Prefer normal Markdown lists unless a tool-specific construct is required.

```cpp
/**
 * Important rules:
 * - rule one
 * - rule two
 * - rule three
 */
```

### Emphasis

Use emphasis to improve scanning, not to decorate every noun.

```cpp
/**
 * Returns the **normalized** path, not the original text.
 */
```

### Code fences

Always include a language when practical.

```cpp
/**
 * @code cpp
 * auto tree = parse_text(source).value();
 * @endcode
 */
```

or, when Markdown mode is clearer:

```cpp
/**
 * ```cpp
 * auto tree = parse_text(source).value();
 * ```
 */
```

Choose the form that renders reliably in your toolchain and style.

### Markdown anti-patterns in Doxygen

- deeply nested lists that become unreadable in source
- giant tables where plain lists would be clearer
- mixing Markdown and raw HTML when neither was necessary
- clever heading structures inside a function doc where short subsections or
    `@par` would read better

## Tables in Doxygen

Tables are useful when comparing parallel properties.
They are bad when used as a substitute for explanation.

### Good table use cases

- comparing modes or flags
- showing error categories
- mapping input forms to output behavior
- summarizing complexity trade-offs across overloads

### Weak table use cases

- a two-row table that could be a sentence
- a giant narrative paragraph broken into awkward cells
- content that requires wrapping long prose in every column

### Generic table example

```cpp
/**
 * Supported modes:
 *
 * | Mode | Behavior | Typical Use |
 * | ---- | -------- | ----------- |
 * | Fast | Minimal validation | Trusted input |
 * | Safe | Full validation | User input |
 */
```

Be careful with formatting and rendering.
Malformed tables are pure sadness.

## Formulas and Math in Doxygen

If you document mathematical APIs, formulas can be very helpful.
Use them when the formula clarifies behavior or invariants.

### Use formulas for

- exact mathematical definitions
- normalization equations
- recurrence relations
- cost models where notation helps

### Do not use formulas for

- dressing up trivial arithmetic
- replacing a plain-language explanation readers still need

### Formula guidance

- define symbols in prose
- keep formulas local to the documented behavior
- if the whole file shares a mathematical model, explain the model once in the
    file/page and keep per-function formulas specific

### Generic formula example

```cpp
/**
 * Computes the normalized score
 * \f[
 *   score = \frac{value - min}{max - min}
 * \f]
 * where `min < max`.
 */
```

## Graphs and Diagrams in Doxygen

Diagrams are useful when relationships matter.
They are not a personality trait.

### Good diagram use cases

- include/dependency structure
- inheritance or interface relationships when unavoidable
- module graphs
- call/caller graphs for important entry points
- state or workflow diagrams for docs pages

### Bad diagram use cases

- every tiny helper function generating unreadable call graphs
- enormous graphs with no depth limits
- diagrams whose visual noise exceeds their explanatory value

### Diagram policy

- turn on Graphviz support intentionally
- cap node counts and depth where needed
- keep manually-authored diagrams focused
- use diagrams to complement prose, not replace it

### Generic dot block

```cpp
/**
 * @dot
 * digraph workflow {
 *   rankdir=LR;
 *   parse -> validate -> build_view;
 * }
 * @enddot
 */
```

## `@par`, `@section`, and Structured Layout

Use structure to improve scanability.

### Good uses of `@par`

- naming short subtopics inside a long symbol doc
- separating “Thread Safety”, “Ownership”, or “Performance” notes

### Good uses of sections

- organizing large pages
- manual/tutorial content
- module overviews with several conceptual subsections

### Bad uses of structure

- one subsection per sentence
- a five-level heading tree inside a tiny doc block
- creating headings only because the tool supports them

## `@code` and Example Blocks

Prefer compilable-looking, minimal-but-real examples.

### Rules for Doxygen code blocks

- state the language where possible
- include enough setup for meaning
- do not include twenty irrelevant lines of scaffolding
- if failure handling matters, show it
- if ownership/lifetime matters, show it
- if order sensitivity matters, show it

### Good Doxygen example block

```cpp
/**
 * @code cpp
 * auto result = parse_text(source);
 * if (!result) {
 *     print_error(result.error());
 *     return;
 * }
 * use(result.value());
 * @endcode
 */
```

## `@copydoc` and Reuse Features

Doxygen supports doc reuse features.
These can reduce duplication **when used carefully**.

### Acceptable use cases

- an override whose contract is genuinely identical
- forwarding declarations where repeating full docs would drift
- paired declarations/definitions with one canonical doc source

### Dangerous use cases

- using `@copydoc` to hide that semantics actually differ
- inheriting docs onto wrappers that add side effects or ownership changes
- copying a verbose block when a short local clarification would be better

### Rule

Only reuse docs automatically when the semantics are materially the same.
If the local symbol adds, removes, or alters meaning, document that delta.

## Conditional Documentation and Internal Material

Doxygen can include or exclude docs conditionally.
Use that ability intentionally.

### Good uses

- internal-only notes excluded from public docs
- alternative documentation views for different audiences
- build-specific doc exposure when truly necessary

### Bad uses

- hiding incomplete documentation instead of fixing it
- maintaining multiple contradictory doc branches
- building public docs that silently omit required contract details

### Policy

- public contracts must not depend on internal-only hidden paragraphs
- conditional docs should be rare and justified
- audience-specific docs still need one canonical truth source

## Preprocessing and Macro Expansion in Doxygen

This is one of the most important operational areas.
If your code uses macros heavily, preprocessing settings determine whether the
generated docs are clear or cursed.

### Key preprocessing settings to understand

- `ENABLE_PREPROCESSING`
- `MACRO_EXPANSION`
- `EXPAND_ONLY_PREDEF`
- `PREDEFINED`
- `EXPAND_AS_DEFINED`
- include path handling and extension mapping

### Philosophy

Only expand what helps readers see the real API.
Do not unleash uncontrolled macro expansion just because you can.

### Good preprocessing goals

- hide noisy compatibility wrappers when safe
- reveal the true signature of documented APIs
- teach the documentation generator about feature-test or annotation macros
- prevent bogus parsing failures from custom syntax macros

### Bad preprocessing goals

- expanding everything until the output no longer resembles the source API
- using preprocessor tricks to paper over structurally confusing code
- leaving parser-breaking macros unexplained and hoping for the best

### Recommended approach

1. identify macros that affect parsing or visible signatures
2. decide whether each should be preserved, simplified, or expanded
3. configure `PREDEFINED` / `EXPAND_AS_DEFINED` intentionally
4. verify rendered declarations and links
5. review again after toolchain upgrades

### Example conceptual config pattern

```text
ENABLE_PREPROCESSING = YES
MACRO_EXPANSION      = YES
EXPAND_ONLY_PREDEF   = YES
PREDEFINED          += API_EXPORT=
PREDEFINED          += API_NODISCARD=
EXPAND_AS_DEFINED   += PROJECT_ENUM
```

### Preprocessing review questions

- do the rendered declarations match reader expectations?
- did any annotation macro leak into the signature unnecessarily?
- did macro expansion erase important semantic names?
- are conditional compilation branches hiding relevant public APIs?

## Extension Mapping and Mixed-Language Projects

Doxygen sometimes needs help understanding non-standard file extensions.

### Use extension mapping when

- your project uses unusual suffixes
- generated or wrapper files need parsing as a specific language
- mixed C/C++/IDL/other files appear in one documentation build

### Rule

Extension mapping should clarify parsing, not hide project structure.

## Source Browsing

Source browsing features can be very useful when enabled responsibly.

### Good reasons to enable source browsing

- readers need declaration-to-source navigation
- implementation context matters for review or maintenance docs
- internal teams rely on hyperlinked source views

### Good source-browsing policy

- strip or preserve comments intentionally
- ensure generated paths and links remain stable
- verify that displayed sources do not expose unwanted generated noise

## Search and Index Output

Generated documentation is most useful when readers can actually find things.

### Search-output rules

- enable search when publishing large doc sets
- make sure briefs and page titles are meaningful, because search quality depends
    on the input text
- avoid duplicate names with empty or vague summaries
- verify index pages are browsable even without perfect search

### Naming and anchor policy

- page and group titles should be explicit
- repeated heading names on the same page should be avoided
- related material should be linked directly instead of expecting users to search
    manually every time

## Output Formats

Doxygen can generate HTML, XML, LaTeX, man pages, and more.
Pick formats based on readers and tooling needs.

### HTML

Usually the default choice for human readers.

Use HTML when you need:

- cross-linked interactive browsing
- search
- diagrams
- easy local or published viewing

### XML

Useful when other tooling consumes the docs.

Use XML when:

- you need downstream processing
- you generate additional site content from symbol metadata
- CI or analysis tooling consumes documentation structure

### LaTeX / PDF

Useful when a printable/reference bundle is required.
Do not force PDF output just because the option exists.

### Rule

Choose outputs intentionally.
Do not enable formats you do not validate or ship.

## Doxyfile Configuration Philosophy

A documentation config file is part of the product.
Treat it like code.

### Config file rules

- version it with the repo
- keep it readable
- group related settings logically
- comment non-obvious choices
- avoid cargo-culting giant configs without pruning
- update intentionally when upgrading Doxygen

### Good config structure

- project identity
- input selection
- extraction policy
- warnings and strictness
- preprocessing
- output format sections
- diagram/search/source browsing sections
- theme/customization if any

### Bad config structure

- thousands of default lines with no curation
- mystery overrides with no explanation
- stale settings from years-old versions
- enabling every optional graph/search feature without verifying output quality

## Warning Policy for Doxygen Builds

Warnings are documentation bugs until proven otherwise.

### Treat these as serious

- undocumented parameters
- malformed commands
- unresolved links
- parsing failures
- duplicate anchors or broken page structure
- diagrams or formulas that fail to render correctly

### Acceptable reasons to suppress a warning

- false positive confirmed by rendered output and tool behavior
- unavoidable tool limitation with documented rationale
- generated code or external headers intentionally excluded from full docs

### Unacceptable reason to suppress a warning

- “the build still produced HTML”

## Build Integration for Doxygen

If docs matter, they should be buildable by automation, not only by memory.

### Good build integration includes

- one reproducible entry point
- explicit tool dependency declaration
- optional but well-defined doc target
- stable output location
- CI or local verification path when practical

### Generic CMake sketch

```cmake
find_package(Doxygen 1.15 QUIET COMPONENTS dot)

if(DOXYGEN_FOUND)
    set(DOXYGEN_GENERATE_HTML YES)
    set(DOXYGEN_GENERATE_XML NO)
    set(DOXYGEN_WARN_IF_UNDOCUMENTED YES)
    set(DOXYGEN_HAVE_DOT YES)

    doxygen_add_docs(docs
        ${CMAKE_SOURCE_DIR}/include
        ${CMAKE_SOURCE_DIR}/src
        COMMENT "Generating API documentation"
    )
endif()
```

### Build integration rules

- do not hardcode machine-specific paths
- keep doc targets optional if contributors may lack the tool locally
- fail loudly on malformed config or critical warnings when docs are part of CI
- document how to run the doc build locally

## Layout and Navigation in Generated Output

Readers should be able to answer these questions quickly:

- where do I start?
- what module contains this?
- what does this symbol relate to?
- how do I get from overview to reference?
- where are troubleshooting or examples?

### To support that

- create a meaningful main page when the doc set is non-trivial
- use module/group pages for major feature areas
- make file/type/function briefs useful in index views
- ensure `@see` paths form a real navigation web

## Doxygen Review Checklist

Before finishing Doxygen documentation work, verify:

- [ ] the file/page-level rationale is centralized
- [ ] symbol docs explain local contracts only
- [ ] `@brief` lines are search-friendly and specific
- [ ] `@param` and `@return` text describes meaning, not merely types
- [ ] groups/pages exist where API discovery would otherwise be poor
- [ ] examples are distinct and purposeful
- [ ] warnings are high-signal rather than boilerplate spam
- [ ] preprocessing settings make rendered declarations readable
- [ ] links resolve and point to meaningful related material
- [ ] generated output was actually inspected, not merely generated

## Doxygen Troubleshooting Patterns

### Problem: the documented signature looks wrong

Possible causes:

- parser confusion around macros
- missing preprocessing config
- unsupported extension mapping
- declaration/definition split with docs on the wrong side

Fix strategy:

1. inspect the rendered declaration
2. identify which macro or syntax feature distorted it
3. adjust preprocessing or mapping intentionally
4. rebuild and verify again

### Problem: links do not resolve

Possible causes:

- symbol names not fully qualified where needed
- page/group anchors changed
- overload ambiguity
- the target is excluded from extraction

Fix strategy:

1. identify the exact unresolved target
2. prefer explicit cross-reference syntax where ambiguity exists
3. confirm the target is actually in the build
4. rebuild and inspect output

### Problem: docs build, but navigation feels bad

Possible causes:

- weak briefs
- no main page or guide pages
- missing grouping
- no curated `@see` links
- giant flat symbol lists

Fix strategy:

1. improve briefs
2. add or refine pages/groups
3. add related-links that reflect real workflows
4. review from a new reader’s perspective

### Problem: warning volume is overwhelming

Possible causes:

- stale config
- widespread missing param docs
- parsing broken by macros
- generated/internal code accidentally included

Fix strategy:

1. reduce accidental input scope
2. fix parsing first
3. then fix missing docs systematically
4. only then consider justified suppressions

### Problem: diagrams are unreadable

Possible causes:

- too many nodes
- too much depth
- low-value graph types enabled everywhere
- graph generation turned on without curation

Fix strategy:

1. limit graph depth and node counts
2. disable low-value auto-graphs
3. prefer focused manual diagrams for key workflows

## Doxygen Anti-Patterns to Ban

### ❌ Duplicated rationale across related helpers

Document the shared rationale once in the file/module/page.
Use per-function docs for per-function meaning.

### ❌ `@brief` lines that only say “helper”

That helps nobody.

### ❌ Huge `@details` blocks with no tagged contract info

If a reader cannot skim parameters, return value, caveats, and failure mode,
the docs are too essay-shaped.

### ❌ Param docs copied from names

`@param value Value.` is not documentation.

### ❌ Page docs that are just indexes in paragraph form

Narrative docs must add workflow or conceptual framing.

### ❌ Macros left undocumented because “everyone knows”

No they do not. Document side effects and evaluation hazards.

### ❌ Auto-generated output trusted without visual inspection

The build succeeding does not prove the docs are readable.

## Doxygen Bottom Line

Use Doxygen as a structured reference system, not a prose landfill.

Put major rationale once at the correct level.
Keep symbol docs local and precise.
Use groups/pages to improve discovery.
Make the config intentional.
Inspect the rendered output.
If a paragraph teaches nothing new where it sits, move it upward or delete it.

## Haddock Guidance (Haskell, Source-Adjacent Semantics, and Interface-First Docs)

Haddock is not “Doxygen but with different punctuation.”
It has its own strengths:

- source-adjacent module docs
- explicit association with declarations and export structure
- lightweight markup that stays readable in source
- REPL-style examples
- searchable HTML and Hoogle-oriented output
- multi-package/interface aggregation

Use those strengths.

## Haddock Philosophy

Haddock works best when the source code already has good structure:

- explicit type signatures
- clear module boundaries
- meaningful exports
- stable naming
- source that can be read without heroic parser coping

If the module export list is chaos and the public API is blurry, the generated
docs will inherit that chaos.

### Haddock is especially good for documenting

- module intent and boundaries
- pure transformation functions
- type-class laws and expectations
- algebraic data types and smart constructors
- effect boundaries and monadic behavior
- small composable functions where signatures matter a lot

## Haddock Comment Forms

### Top-level declaration docs

```haskell
-- | Parses a configuration document into an immutable syntax tree.
parseText :: Text -> Either ParseError SyntaxTree
```

### Post-item docs for fields or constructors

```haskell
data Mode
    = Fast         -- ^ Minimal validation for trusted input.
    | Safe         -- ^ Full validation for user-controlled input.
```

### Block docs

```haskell
{-|
Module      : Example.Parser
Description : Public parser API and syntax-tree entry points.

Explain the module-level rationale here once.
-}
```

### Policy

- use `-- |` for declaration-leading docs
- use `-- ^` for trailing constructor/field docs when structure makes that clear
- use `{-| -}` for larger module or declaration blocks
- stay consistent within a module

## Module Headers in Haddock

In Haddock, the module header is a canonical home for module-wide rationale.
Use it the same way you would use a strong Doxygen file header or page.

### A good module header should include

- what the module is for
- what it exports conceptually
- what it deliberately does not cover
- design constraints that apply to multiple declarations
- navigation hints to sibling modules
- one short example or workflow sketch if appropriate

### Generic module header example

```haskell
{-|
Module      : Example.Parser
Description : Public parser entry points and parse-result types.

This module exposes the user-facing parsing API. It centralizes the parse
entry points, the structured error type, and the syntax-tree types used by
downstream modules.

Use this module when you need to turn source text into validated syntax trees.
Use @Example.Parser.Internal@ only when working on parser internals.

Typical workflow:

>>> result <- pure (parseText "name = value")
>>> either print print result

-}
module Example.Parser
    ( parseText
    , parseFile
    , SyntaxTree
    , ParseError
    ) where
```

### Module-header rules

- document the public story once here
- do not paste this same story under every exported function
- use export-list ordering to reinforce the mental model
- if the module belongs to a family, link or mention sibling modules clearly

## Export Lists Are Documentation

In Haskell, export lists are not only mechanical.
They shape how readers encounter the API.

### Export-list rules

- order exports intentionally
- group related exports together
- put primary entry points before helper types when possible
- keep internal constructors hidden when smart constructors are the intended API
- expose only what the documentation is prepared to support as public contract

### Good export-list pattern

```haskell
module Example.Config
    ( -- * Parsing
        parseConfig
    , parseConfigFile

        -- * Types
    , Config
    , ParseError

        -- * Inspection
    , lookupValue
    , sections
    ) where
```

### Why this matters

Export ordering becomes navigation structure in generated docs.
Use it.

## Type Signatures Are Mandatory Context

Haddock assumes explicit type signatures for serious documentation quality.

### Rule

If a public or semantically important function lacks an explicit type signature,
the resulting documentation is weaker, less searchable, and more fragile.

### Therefore

- document public functions with explicit signatures
- prefer explicit signatures for most non-trivial internal helpers too
- if a type-class-polymorphic function has non-obvious constraints, explain them
    in prose and not only in the type

## Function Docs in Haddock

Haddock docs should describe contract, semantics, and composition.
Because Haskell functions are often small and composable, it is especially easy
to fall into one-line tautologies.
Resist that.

### Weak Haddock doc

```haskell
-- | Maps the function over the values.
applyAll :: (a -> b) -> [a] -> [b]
```

### Better Haddock doc

```haskell
-- | Applies the transformation to each value in left-to-right order,
-- preserving list length.
--
-- Empty input yields empty output. Evaluation of the result remains lazy in the
-- list spine beyond what the transformation itself forces.
applyAll :: (a -> b) -> [a] -> [b]
```

### Good Haddock function-doc topics

- strictness and laziness
- ordering guarantees
- total vs partial behavior
- error channels (`Either`, `Maybe`, exceptions, effects)
- complexity when it matters
- interaction with type-class laws
- composition with nearby helpers

### If a function is partial

Say so loudly.

```haskell
-- | Extracts the first parsed item.
--
-- Partial: throws an error if the list is empty.
-- Prefer 'safeHeadResult' when emptiness is expected input.
firstParsedItem :: [a] -> a
```

Partial functions deserve warnings and safer alternatives when available.

## Type, Data, and Constructor Documentation in Haddock

### Document types for

- semantic meaning
- invariants
- constructor intent
- when fields/constructors are public but still easy to misuse

### Generic data-type example

```haskell
-- | Validation mode used by configuration parsing.
--
-- 'Fast' assumes trusted input and performs minimal checking.
-- 'Safe' validates unknown fields and structural inconsistencies.
data Mode
    = Fast  -- ^ Minimal validation for trusted internal input.
    | Safe  -- ^ Full validation for user-supplied input.
```

### Record field docs

```haskell
data ParseOptions = ParseOptions
    { allowUnknownFields :: Bool  -- ^ Accept unknown keys instead of failing.
    , strictNumbers      :: Bool  -- ^ Reject lossy numeric conversions.
    }
```

### Record-doc rules

- field docs should explain behavior, not restate field names
- mention default assumptions when they matter
- if the record is better constructed with smart constructors or defaults,
    document that pattern at the type level

## Type Classes and Laws

Haddock is a great place to document laws and semantic expectations.

### Document type classes with

- what the class represents semantically
- laws implementers are expected to satisfy
- performance expectations where relevant
- minimal complete definition
- relationship to superclass/subclass behavior

### Generic type-class example

```haskell
-- | Things that can be rendered into a stable textual form.
--
-- Instances should satisfy these laws:
--
-- * Rendering the same value twice yields the same text.
-- * Equivalent values render identically.
-- * Rendering should not depend on ambient locale.
class Render a where
    render :: a -> Text
```

### Law-doc rules

- laws belong in the type-class doc, not in every instance doc
- instance docs should mention only instance-specific caveats or performance
    deviations
- if a law has known exceptions, say so precisely

## Examples in Haddock

Haddock supports executable-looking REPL examples beautifully.
Use them.

### REPL-style examples

```haskell
-- |
-- >>> normalizePath "a//b///c"
-- "a/b/c"
normalizePath :: Text -> Text
```

### Property-style examples

Use property or law notes when behavior is better expressed as a relation than a
single example.

```haskell
-- | prop> length (applyAll f xs) == length xs
applyAll :: (a -> b) -> [a] -> [b]
```

### Example policy for Haddock

- show the common case
- show a failure/empty case when meaningful
- show laws or REPL behavior when composition matters
- avoid duplicate examples that only rename values

## Links and Markup in Haddock

Haddock markup is intentionally lighter than some other systems.
That is a strength.

### Use markup for

- emphasis
- code spans
- bullet lists
- links to identifiers/modules
- short examples and laws

### Linking rules

- refer to identifiers and modules explicitly when that improves navigation
- make related safe/unsafe pairs discoverable
- mention sibling modules by exact name when readers should switch modules next

### Good linking language

- “Prefer 'safeHeadResult' when emptiness is expected.”
- “Use @Example.Parser.Internal@ only when extending the parser itself.”
- “See 'parseFile' for the file-based entry point.”

## Named Chunks and Shared Narrative Sections

Haddock supports named documentation chunks such as module-local sections.
Use them to avoid duplication and improve structure.

### Good uses

- one module-wide explanation of a recurring invariant
- one shared “Performance Notes” chunk
- one shared “Migration Notes” chunk
- setup instructions for examples

### Generic named chunk example

```haskell
-- $validationModes
--
-- The parser offers two validation modes. Prefer 'Safe' for user input and
-- 'Fast' for trusted machine-generated input.
```

### Rule

If several declarations need the same conceptual background, create a shared
chunk or module-level explanation and point readers there.

## Haddock Output and Invocation

Generated documentation quality depends on the invocation too.

### Common useful outputs

- HTML for human browsing
- Hoogle databases for search
- optional hyperlinked source output
- interface dumps for multi-package linking

### Operational rules

- keep the invocation reproducible
- document package/module linkage clearly in build scripts
- generate Hoogle/search output when discoverability matters
- verify rendered module headers, links, and examples

### Concepts worth knowing

- `--html`
- `--hoogle`
- `--latex` when truly needed
- `--hyperlinked-source`
- `--dump-interface`
- `--read-interface`
- `--base-url`
- compilation vs `--no-compilation` modes where appropriate

### Rule

If you rely on cross-package or multi-component links, make that wiring explicit
in the build instructions and validate it after dependency changes.

## Multi-Component and Multi-Package Haddock Docs

Large Haskell ecosystems often need aggregated documentation.

### Good aggregation use cases

- a library family split into several packages
- public docs that span core, extra, and integration packages
- shared search/index across related outputs

### Aggregation rules

- define one canonical landing structure
- keep package boundaries visible rather than pretending everything is one flat
    namespace
- use stable base URLs and interface files intentionally
- verify cross-package links after refactors or version bumps

### Anti-pattern

Do not let aggregated docs blur which package/module actually owns the contract.
Ownership still matters.

## Common Haddock Failure Modes

### Problem: docs are sparse or weirdly associated

Possible causes:

- missing type signatures
- comment attached to the wrong declaration
- export list hiding the intended public symbol

Fix strategy:

1. confirm the comment placement
2. confirm the explicit signature is present
3. confirm the intended symbol is exported

### Problem: links across packages do not work

Possible causes:

- missing interface reads
- incorrect base URLs
- package version drift

Fix strategy:

1. inspect the generated references
2. confirm interface file generation and read paths
3. rebuild with consistent package metadata

### Problem: examples render but mislead

Possible causes:

- examples omit critical imports or setup context
- examples demonstrate non-default behavior without saying so
- examples differ syntactically but not semantically

Fix strategy:

1. state assumptions
2. distinguish default from advanced usage
3. prune duplicate examples

## Haddock Review Checklist

- [ ] module headers centralize module-wide rationale
- [ ] export lists communicate conceptual structure
- [ ] important declarations have explicit signatures
- [ ] function docs explain semantics, strictness/laziness, and failure behavior
- [ ] partial functions are marked clearly and safer alternatives are linked
- [ ] type-class laws live at the class level, not duplicated everywhere
- [ ] examples teach distinct behaviors
- [ ] cross-module links and search outputs were validated

## Haddock Bottom Line

Use Haddock to make Haskell APIs discoverable, law-aware, and source-adjacent.

Let the module header carry shared rationale.
Let export lists teach structure.
Let function docs explain semantics, strictness, and composition.
Let links and examples do real pedagogical work.

## Javadoc Guidance (Java, Packages, Modules, and Rich API Contracts)

Javadoc is the canonical API documentation system for Java.
It rewards strong package design, explicit public surfaces, and disciplined use
of package/module docs.

### Prefer modern Javadoc features

- prefer current JDK/Javadoc generation tooling
- use modern inline tags and snippet support when appropriate
- keep docs compatible with your project’s actual Java version policy
- review rendered output after generator upgrades

## Javadoc Philosophy

Java APIs often spread meaning across packages, interfaces, classes, records,
enums, and methods.
The documentation must keep those layers distinct.

### Therefore

- package-level docs explain package boundaries and concepts
- module-level docs explain cross-package architecture when modules are used
- type-level docs explain semantic role and invariants
- method-level docs explain local contract
- implementation notes stay separate from API contract notes

## Package and Module Documentation

In Java, `package-info.java` and `module-info.java` are canonical homes for
wide-scope explanation.

### Use package docs for

- package purpose
- public scope and intended audience
- conceptual grouping of types
- package-wide conventions and constraints

### Use module docs for

- high-level module purpose
- exported package relationships
- service/provider architecture
- module-wide security or operational constraints

### Generic package doc sketch

```java
/**
 * Public parser APIs and immutable syntax-tree types.
 *
 * <p>This package contains the user-facing parsing entry points and the result
 * types used by downstream formatting and validation packages.</p>
 *
 * <p>Use this package for ordinary parsing. Internal parser construction and
 * grammar assembly live elsewhere.</p>
 */
package example.parser;
```

### Rule

If every public type repeats the same package-level explanation, move it into
`package-info.java`.

## Type-Level Javadoc

Use type docs to explain:

- what the type represents
- invariants
- mutability/immutability expectations
- threading or lifecycle expectations
- which collaborators or adjacent types matter

### Generic class example

```java
/**
 * Immutable parsed configuration tree.
 *
 * <p>Instances of this type represent validated configuration data. They are
 * created by parser entry points and then consumed by higher-level runtime
 * builders.</p>
 *
 * <p>This type is thread-safe after construction because its state is immutable.</p>
 */
public final class ConfigTree {
```

### Records and enums

Document records and enums semantically too.
Do not assume the syntax makes the meaning obvious.

## Method-Level Javadoc

Method docs must explain the actual contract.

### Common useful tags

- `@param`
- `@return`
- `@throws`
- `@see`
- `@since`
- `@deprecated`
- `@implSpec`
- `@apiNote`
- `@implNote`

### Use `@apiNote` for

- guidance relevant to API consumers
- recommended usage patterns
- performance trade-offs users should consider

### Use `@implSpec` for

- subclass/implementor obligations
- behavioral contracts required by overrides or interface implementations

### Use `@implNote` for

- implementation details interesting to maintainers but not part of the public
    semantic contract

### Generic method example

```java
/**
 * Parses one UTF-8 document into an immutable configuration tree.
 *
 * @param source source text to parse
 * @return parsed configuration tree
 * @throws ParseException if the input is malformed or missing required fields
 * @apiNote Prefer this overload when the document is already resident in memory.
 * @see #parseFile(Path)
 */
public static ConfigTree parse(String source) throws ParseException {
```

### Javadoc method rules

- `@param` text should explain meaning and constraints
- `@return` text should describe meaning, not type
- `@throws` should explain causes precisely
- `@apiNote` should not restate the summary sentence
- `@implSpec` belongs where implementors need it, not on every final method

## Snippets and Inline Code in Javadoc

Examples matter here too.

### Use inline code for

- short identifiers
- literals
- method names
- configuration keys

### Use snippet blocks for

- multi-line usage examples
- lifecycle flows
- failure-handling examples

### Rule

Prefer examples that compile or nearly compile with obvious surrounding context.
Do not show toy code that hides the real usage pattern.

## Inheritance and Override Documentation

Java’s inheritance model creates documentation drift very easily.

### Rules

- inherit docs only when semantics are materially identical
- if an override adds timing, threading, nullability, or side-effect differences,
    document the difference
- interface docs should describe obligations once at the interface level
- implementing classes should add only implementation-specific caveats or
    performance notes when needed

## Javadoc Review Checklist

- [ ] package/module docs centralize wide-scope explanation
- [ ] type docs describe invariants and semantic role
- [ ] method docs describe contract, failure, and usage guidance
- [ ] inheritance-related docs avoid duplication and drift
- [ ] snippets/examples teach real usage
- [ ] `@apiNote`, `@implSpec`, and `@implNote` are used intentionally

## Javadoc Bottom Line

Use Javadoc to present Java APIs as a layered system:
package/module overview, type meaning, method contract, implementor notes, and
consumer guidance.
Do not flatten those layers into repetitive soup.

## Python Docstring Guidance (Modules, Types, Functions, and Runtime-Friendly Docs)

Python documentation tends to fail in one of two ways:

- everything gets a tiny tautological docstring
- nothing gets a real contract because “the code is obvious”

we reject both.

### Prefer modern Python docs

- prefer current Python syntax and typing features
- document against the real runtime and type behavior
- keep examples compatible with the project’s supported version policy
- let docstrings help both humans and tooling

## Python Docstring Philosophy

Python docstrings serve multiple audiences at once:

- readers in editors and REPL help output
- generated documentation tools
- type-aware developers
- maintainers reviewing behavior without opening implementation details

Therefore, Python docstrings should be:

- concise in the first line
- detailed where semantics are non-obvious
- structured consistently
- rich in examples when behavior or failure modes need demonstration

## Module Docstrings

Use module docstrings as the canonical home for module-wide rationale.

### Good module docstrings include

- module purpose
- what the module exports conceptually
- important constraints or workflow assumptions
- where readers should go next
- one short usage sketch when helpful

### Generic module docstring example

```python
"""Public parser entry points and syntax-tree helpers.

This module exposes the user-facing parsing API and the small helper functions
most callers need when turning configuration text into immutable syntax trees.

Use this module for ordinary parsing flows. Internal grammar-building helpers
live in sibling modules with narrower responsibilities.
"""
```

### Module-doc rules

- centralize the module story here once
- do not paste the same overview into every function docstring
- if several functions share one important assumption, document it here and let
  individual functions focus on local behavior

## Google-Style Docstrings

Prefer clear structured sections for non-trivial Python docs.
Common useful sections include:

- `Args:`
- `Returns:`
- `Yields:`
- `Raises:`
- `Attributes:`
- `Examples:`
- `Notes:`

### Rule

Use only the sections that add real information.
Do not include empty ritual headings.

## Function Docstrings in Python

### Good one-line summaries

- “Parse one configuration document into an immutable syntax tree.”
- “Normalize a user path without touching the filesystem.”
- “Yield records lazily from a validated input stream.”

### Weak one-line summaries

- “Process data.”
- “Helper function.”
- “Gets result.”

### Generic function docstring template

```python
def parse_text(source: str, *, strict: bool = True) -> SyntaxTree:
    """Parse a UTF-8 configuration document into an immutable syntax tree.

    Args:
        source: Source text to parse.
        strict: When true, reject unknown fields and structural ambiguities.

    Returns:
        The parsed syntax tree.

    Raises:
        ParseError: If the input is malformed or violates strict-mode rules.

    Examples:
        >>> tree = parse_text("name = value")
        >>> tree.root.kind
        'document'
    """
```

### Function-doc rules

- document semantics, not type annotations duplicated in prose
- explain defaults when they matter
- document mutability, ownership, caching, laziness, or side effects when those
  are not obvious
- if a function is async, generator-based, or context-manager-related, document
  that behavior precisely

## Async, Generator, and Context Manager Docs

### Async functions

Document:

- what is awaited
- whether cancellation is safe or leaves partial work
- what side effects may already have happened on failure

### Generators and iterators

Document:

- what is yielded
- ordering guarantees
- when evaluation happens
- whether source resources must remain open

### Context managers

Document:

- what resource is acquired
- what is guaranteed on exit
- whether nested use is safe
- whether exit is idempotent

### Generic generator example

```python
def iter_records(source: str) -> Iterator[Record]:
    """Yield parsed records in input order.

    The generator performs parsing lazily as iteration advances. It raises
    ``ParseError`` at the point the malformed record is encountered.

    Args:
        source: UTF-8 text containing zero or more records.

    Yields:
        Parsed records in the order they appear in ``source``.

    Raises:
        ParseError: If a record is malformed.
    """
```

## Class and Dataclass Docstrings

Python types deserve type-level docs just like in other languages.

### Good class docs include

- semantic role
- invariants
- mutability expectations
- whether callers should construct directly or use factories
- important attributes if not obvious from the initializer alone

### Generic class example

```python
class ConfigView:
    """Read-only view over a validated configuration tree.

    Instances borrow the underlying tree and expose convenience lookup helpers.
    They do not own storage and should not outlive the source tree.
    """
```

### Dataclass rule

If field names are clear but their semantics are not, document the class and its
fields/attributes explicitly.

## Attribute Documentation

When generating docs from Python, attributes often need help.

### Document attributes when

- their meaning is not obvious from the name
- units or ranges matter
- mutability rules matter
- a property differs from raw stored state

### Good attribute note

```python
class RetryPolicy:
    """Retry settings for transient operations.

    Attributes:
        max_attempts: Inclusive maximum number of attempts, including the first.
        base_delay_s: Base backoff delay in seconds.
    """
```

## Python Example Policy

Examples in Python docs should be runnable-looking and copy-paste friendly.

### Good example styles

- REPL-style for tiny transformations
- normal code blocks for multi-step workflows
- failure-handling snippets when exceptions are part of the API

### Weak example styles

- examples that omit all imports and make every name mysterious
- examples that only prove the function exists
- examples that differ only by a constant literal and add no semantic value

## Python Bottom Line

Use docstrings to make Python modules and APIs usable from editor hovers, REPL
help, generated docs, and ordinary code review.

Let module docstrings carry shared rationale.
Let function/class docstrings carry local contract.
Do not duplicate the same story everywhere.

## Markdown, Manuals, READMEs, and Narrative Documentation

Reference docs tell readers what a symbol means.
Narrative docs tell readers how to think, choose, and proceed.
You need both.

## Narrative Documentation Philosophy

Manual pages, README sections, architecture docs, troubleshooting guides, and
walkthroughs should be:

- reader-oriented
- task-oriented when appropriate
- structured for skimming
- explicit about audience and assumptions
- linked to reference material rather than trying to duplicate it all

### Narrative docs are the right place for

- getting started flows
- design rationale spanning many symbols
- migrations
- architecture explanations
- troubleshooting paths
- deployment and build guidance
- contributor guidance

### Narrative docs are the wrong place for

- repeating every method signature manually
- cloning symbol docs into prose form
- hiding critical contracts that should have been in API docs

## README Guidance

README files are entry points, not dumpsters.

### A strong README usually contains

- what the project/library/tool does
- who it is for
- the shortest path to first success
- installation/build prerequisites
- high-level feature map
- links to deeper docs

### A README should not become

- the only place critical API contracts are documented
- a giant changelog archive
- a raw dump of internal architecture without reader framing
- a substitute for generated reference docs in API-heavy projects

### Good README flow

1. identity and purpose
2. quickstart
3. core concepts or feature map
4. how to build/test/docs
5. links to deep guides or API reference

## Architecture and Design Pages

These pages are where you explain big decisions once.

### Good architecture-page topics

- subsystem boundaries
- data flow
- ownership/lifetime rules across modules
- performance model
- error model
- why key trade-offs were chosen

### Architecture-page rule

If several files or modules all need the same design explanation, write an
architecture page and link to it.
Do not paste the same “why” essay into every file header.

## Troubleshooting Pages

Troubleshooting docs should map symptoms to likely causes and fixes.

### Good troubleshooting structure

- symptom heading
- likely causes
- diagnostic steps
- fixes or workarounds
- links to relevant reference docs

### Weak troubleshooting structure

- one giant wall of text
- vague advice like “check your setup”
- no connection to actual error messages or symptoms readers will search for

## CLI and Configuration Documentation

Command-line tools and configuration systems need both narrative and reference
coverage.

### For CLI docs, document

- command purpose
- positional args and flags
- defaults
- environment interactions
- examples for common workflows
- failure/exit behavior when relevant

### For configuration docs, document

- key name
- value type
- units or accepted formats
- defaults
- required/optional status
- interactions with related keys
- version or compatibility notes when relevant

### Good config-reference pattern

Use a section per key or a compact table plus expanded notes where necessary.
Avoid giant unstructured prose paragraphs for machine-shaped configuration.

## Changelog and Migration Documentation

Not every project needs the same level of migration docs, but when behavior
changes, readers need more than “updated docs.”

### Document migrations when

- names changed
- defaults changed
- output format changed
- contracts tightened
- deprecations became removals
- configuration keys moved or semantics changed

### Good migration note includes

- what changed
- who is affected
- old behavior
- new behavior
- how to migrate
- what to read next

## Documentation Examples in Narrative Pages

Narrative examples have a different job than API examples.

### Narrative example jobs

- show an end-to-end workflow
- connect multiple APIs together
- demonstrate setup + action + result
- show common mistakes and how to avoid them

### API example vs narrative example

- API example: teaches one symbol or local contract
- narrative example: teaches a whole flow or decision path

Do not duplicate them word for word.

## Cross-Linking Between Narrative and Reference Docs

This is essential.

### Narrative docs should link to

- canonical API reference entries
- guide pages for adjacent tasks
- troubleshooting sections
- configuration reference sections

### Reference docs should link back to narrative docs when

- setup context matters
- a workflow or architecture page explains shared rationale
- migration or troubleshooting content is relevant

## Documentation Build, Publish, and CI Policy

If documentation matters, its build and publish process must be intentional.

### Every doc publishing pipeline should answer

- what builds the docs?
- where is the config?
- where does output go?
- what warnings fail the build?
- what external tools are required?
- how are links/search/indexes validated?
- how are versioned docs handled, if at all?

### Good publishing characteristics

- reproducible local command
- CI command that matches local reality
- stable output path
- clear warning policy
- clear artifact or publish target
- reviewable generated output when practical

### Bad publishing characteristics

- “run whatever worked last time”
- doc build hidden inside an unrelated script with no explanation
- warnings ignored forever
- search broken because nobody inspects the published result

## Verification Before Calling Docs Done

Do not claim success just because comments were written.
Verify the actual output and the actual reader experience.

### Minimum verification

- build or generate the docs
- inspect warnings
- inspect the rendered output
- click several important links
- search for a few key symbols/pages/terms
- verify examples and code fences look correct
- verify the main landing path makes sense for a new reader

### For reference-heavy APIs

Also verify:

- overloaded symbols resolve sensibly
- index pages are useful
- grouping/page hierarchy improves discovery
- preprocessing or interface linking did not distort declarations

### For narrative docs

Also verify:

- heading structure is sane
- code fences specify languages where practical
- internal links work
- tables render correctly
- no section restates the same rationale unnecessarily

## Documentation Testing and Automation

When practical, automate checks for:

- broken links
- malformed markdown
- missing docstring sections required by local conventions
- Doxygen/Haddock/Javadoc warning regressions
- doctest/snippet/example drift
- search index generation failures

### Rule

Automation should catch mechanical failure.
Human review must still judge clarity, redundancy, and pedagogy.

## Versioning and Stability of Docs

Docs should reflect real software versions and real behavior.

### Versioning rules

- document current behavior, not a nostalgic mixture of old and new
- call out compatibility or migration boundaries clearly
- update examples when defaults or APIs change
- remove stale notes once they stop helping current users

### Stability rules

- prefer stable anchors and section names for frequently linked material
- avoid gratuitous heading churn in published docs
- if major reorganization occurs, preserve redirect or migration guidance when
  possible

## Documentation Review Rubric

Use this rubric when reviewing any documentation change.

### 1. Scope correctness

- is each explanation placed at the correct level?
- is shared rationale centralized?
- are local docs local?

### 2. Semantic value

- does each paragraph teach something new?
- do examples have distinct jobs?
- are contracts explicit?

### 3. Reader navigation

- can a new reader find the entry point?
- do links lead naturally to the next thing?
- are page/group/module titles informative?

### 4. Mechanical quality

- does the build succeed?
- are warnings justified or fixed?
- do examples and tables render correctly?

### 5. Searchability

- do summaries and headings contain likely search terms?
- are aliases/acronyms discoverable?
- do index/search results look useful?

## Cross-Tool Anti-Patterns to Ban

### ❌ One rationale repeated at file, type, and function level

Explain it once at the highest correct level.
Link to it elsewhere.

### ❌ Boilerplate purity/performance notes repeated under every trivial helper

If the note is truly global, place it globally.
If it is not global, make it specific.

### ❌ Example inflation

Three examples that teach one thing are worse than one example that teaches it
cleanly.

### ❌ Tool-driven structure with no reader benefit

Do not create groups/pages/headings/sections because the tool permits them.
Create them because readers need them.

### ❌ Reference docs masquerading as tutorials, or tutorials masquerading as reference

Readers feel the mismatch immediately.

### ❌ Copy-pasted docs that drift after the first real refactor

Canonical ownership exists to stop this.

### ❌ Search-hostile summaries

If all summaries say “utility” or “helper,” the search index becomes sludge.

## The Long-File Rule

This instruction file is intentionally long.
That is acceptable because each major section adds distinct value:

- universal doctrine
- Doxygen adapter
- Haddock adapter
- Javadoc adapter
- Python docstring adapter
- narrative/manual guidance
- verification and publishing guidance

This is the model to follow for documentation itself:

- long is fine when the content adds new information
- long is bad when the same explanation is repeated with cosmetic changes

## Final Documentation Quality Checklist

Before finishing any documentation task, confirm all applicable items below.

### Scope and structure

- [ ] major rationale has one canonical home
- [ ] repeated concepts use cross-links instead of duplicated prose
- [ ] file/module/package/page docs explain shared context
- [ ] symbol docs explain local contracts and differences

### Contract quality

- [ ] parameters are documented semantically
- [ ] return values or yields are documented semantically
- [ ] failures, warnings, and edge cases are clear
- [ ] invariants and ownership/lifetime rules are explicit where needed
- [ ] complexity or cost notes exist where relevant

### Examples and pedagogy

- [ ] examples have distinct teaching purposes
- [ ] at least one example shows the common path for non-trivial APIs
- [ ] failure or edge-case handling is shown where relevant
- [ ] examples are generic, self-contained, and consistent with the contract

### Navigation and search

- [ ] summaries and headings are search-friendly
- [ ] related symbols/pages/modules are linked
- [ ] groups/pages/package/module docs improve discovery

### Output verification

- [ ] the docs were generated or otherwise rendered
- [ ] warnings were fixed or consciously justified
- [ ] links, tables, examples, and important pages were visually checked
- [ ] the result helps a real reader, not just a generator

## Final Bottom Line

Documentation should behave like a well-designed API:

- one source of truth for each major idea
- local details where local details belong
- predictable navigation
- explicit contracts
- examples that teach
- output that can actually be used

Write the big rationale once.
Write the local contract where it lives.
Link aggressively.
Repeat yourself only when the reader would lose meaning without the repetition.
Otherwise, don’t.
