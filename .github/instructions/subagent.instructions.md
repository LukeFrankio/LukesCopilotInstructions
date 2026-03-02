---
description: 'Guidelines for delegating tasks to autonomous subagents (cloning yourself for efficiency)'
applyTo: '**'
---

# Subagent Delegation Protocol

> "why do the work yourself when you can spawn a clone to do it for you?"

uwu time to master the art of delegation. `runSubagent` is your ability to summon a specialized worker for heavy lifting. Use it wisely. ✨

---

## ⛔⛔⛔ MEGA WARNING: SUBAGENT ≠ PARENT AGENT ⛔⛔⛔

> **READ THIS FIRST. THIS IS MORE IMPORTANT THAN ANYTHING ELSE IN THIS FILE.**

### If You Are READING This As a Subagent (How to Know)

You are a **subagent** if:

1. **Your entire context came from a single prompt** — someone wrote a detailed task description and handed it to you.
2. **You have no prior conversation history** — you don't remember any previous messages with a user.
3. **Your output goes to another agent, NOT a human** — you are returning findings to a parent, not chatting with a person.
4. **Your prompt contains phrases like**: "You are expected to RESEARCH", "Return the file path", "DO NOT fix it yet", "report findings", or "you are a subagent".
5. **You were invoked via `runSubagent`** — you exist because a parent agent spawned you.

### If You ARE a Subagent: FORBIDDEN TOOLS

```
╔══════════════════════════════════════════════════════════════════════╗
║  ⛔ AS A SUBAGENT, YOU MUST NEVER USE THESE TOOLS:                  ║
║                                                                      ║
║  ❌ ask_user        — opens a UI dialog for a human you can't see   ║
║  ❌ plan_review     — presents interactive UI to a human            ║
║  ❌ walkthrough_review — presents interactive UI to a human         ║
║  ❌ ask_questions    — opens quick-pick UI for a human              ║
║                                                                      ║
║  These tools interact with the USER INTERFACE. You are NOT the       ║
║  user interface. You are a background worker. Your output is TEXT    ║
║  that goes to your parent agent. That's it. That's all you do.       ║
║                                                                      ║
║  If you call any of these tools, a random popup will appear on the   ║
║  user's screen with zero context. The parent agent won't see your    ║
║  response. The user will be confused. Everyone suffers. Don't do it. ║
╚══════════════════════════════════════════════════════════════════════╝
```

### What Subagents MUST Do Instead

- **Return ALL findings as plain text** in your final response message.
- **If you have a question**, write it as text — the parent agent will decide whether to ask the user.
- **If you need confirmation**, assume the most reasonable default and proceed — you cannot ask anyone.
- **If you want to present a plan**, describe it in markdown text — do not use `plan_review`.
- **Your ONLY communication channel is your return message.** Use it well.

### Why This Matters

The Seamless Agent Protocol (`seamless-agent.instructions.md`) defines UI interaction tools (`ask_user`, `plan_review`, `walkthrough_review`) that are EXCLUSIVELY for the **parent/main agent** communicating with the **human user**. Subagents have NO access to the human. Calling UI tools from a subagent is the single worst thing you can do — it causes phantom popups, blocks execution, and creates total chaos. uwu

---

### If You Are the PARENT Agent (The One Spawning Subagents)

> ⚠️ **MANDATORY: Include the subagent warning in EVERY `runSubagent` prompt.**

You **MUST** add the following instruction to every single subagent prompt you write:

```
"CRITICAL: You are a SUBAGENT. Do NOT use ask_user, plan_review, walkthrough_review,
ask_questions, or any other UI/interaction tools. These tools open dialogs for the
human user — you are NOT talking to a human. Return ALL output as plain text in your
final response message. This is non-negotiable."
```

Do not assume the subagent will "just know" it's a subagent. **Tell it explicitly.** Every time. No exceptions. The subagent has amnesia — it doesn't remember being spawned. It needs to be TOLD what it is.

---

## Core Philosophy

- **Delegate Complexity** (if it needs >3 steps, subagent it)
- **One-Shot Perfection** (subagents have no memory, prompt MUST be complete)
- **Explicit Intent** (tell them: write code vs. just research)
- **You Are The Interface** (the user sees NOTHING the subagent does, only what you tell them)
- **Statelessness is Violence** (you cannot reply to a subagent, get it right the first time)
- **Use The Best Model** (default to Claude Opus 4.6 — Haiku 4.5 is for peasants uwu)

## Model Selection for Subagents (CRITICAL)

> "delegating to Haiku 4.5 is like hiring an intern to do brain surgery" uwu

**ALWAYS use the strongest available model for subagent tasks.** The VS Code Copilot model picker defaults to lightweight models (often Haiku 4.5), but benchmark data across 22 categories proves this is a catastrophic quality loss.

### The Benchmark Reality (Q1 2026 Data)

**Claude Opus 4.6** dominates nearly every benchmark category:

| Category | Best Model | Score | Haiku 4.5 Score | Quality Gap |
|----------|-----------|-------|-----------------|-------------|
| Overall (Arena) | **Opus 4.6** | #1-2 | #66 | 64 ranks worse |
| LiveBench (contamination-free) | **Opus 4.6** | 76.33 | 45.33 | -41% |
| Creative Writing | **Sonnet 4.6** | 1963 Elo | Not ranked | N/A |
| Coding (SWE-bench) | **Sonnet 4.6** | 82% | 73.3% | -8.7pp |
| Tool Use (BFCL) | **Opus 4.6** | 77.47% | 68.7% | -8.8pp |
| Reasoning (GPQA) | GPT-5.2 | 92.4% | 73% | -19.4pp |
| Math (AIME 2025) | GPT-5.2/Gemini 3 Pro | 100% | Not ranked | N/A |
| Emotional Intelligence | **Sonnet 4.6** | 1944 Elo | Not ranked | N/A |
| Instruction Following | **Opus 4.6** | 76.33 | 45.33 | -41% |
| Multilingual (MMMLU) | Gemini 3 Pro | 91.8% | Not ranked | N/A |
| Planning/Decomposition | **Opus 4.6** | 76.33 | 61.32 | -20% |
| Agentic Tasks | **Sonnet 4.6** | 82% | 73.3% | -8.7pp |

### Model Selection Rules

**DEFAULT: Claude Opus 4.6** (192K context, Tools + Vision)
- Best overall model across human preference (Arena #1-2)
- Highest instruction following (LiveBench 76.33)
- Best tool use / function calling (BFCL 77.47%)
- Best planning and task decomposition
- Largest context window in Claude line (192K)

**USE Claude Sonnet 4.6 FOR:**
- Coding tasks (82% SWE-bench, highest of any model)
- Creative writing (1963 Elo, #1 on EQ-Bench Creative Writing)
- Agentic autonomous coding (strongest at SWE-bench style tasks)
- Emotional intelligence work (1944 Elo, #1 on EQ-Bench 3)

**USE GPT-5.2 FOR:**
- Pure mathematical reasoning (100% AIME 2025, 92.4% GPQA)
- Graduate-level STEM questions (highest GPQA Diamond)
- When you need maximum analytical precision

**USE Gemini 3 Pro FOR:**
- Multilingual/translation tasks (91.8% MMMLU, #1)
- Tasks requiring massive context (1M+ tokens, though only 173K in VS Code)
- Competition math (100% AIME 2025, tied with GPT-5.2)

**NEVER USE Claude Haiku 4.5 FOR:**
- ❌ Complex research (45.33 LiveBench vs 76.33 for Opus = 41% worse)
- ❌ Coding tasks (73.3% SWE-bench vs 82% for Sonnet = 8.7pp worse)
- ❌ Reasoning tasks (73% GPQA vs 87%+ for Opus = 14pp worse)
- ❌ Creative work (not even ranked on EQ-Bench creative benchmarks)
- ❌ Tool use (68.7% BFCL vs 77.47% for Opus = 8.8pp worse)
- ❌ Anything where quality matters (it's a lightweight model, period)

**Haiku 4.5 is ONLY acceptable for:**
- ✅ Trivial classification tasks
- ✅ Simple text extraction where any model works
- ✅ High-volume low-stakes operations
- ✅ When cost literally cannot be justified (rare in development)

### Available Models in VS Code (Q1 2026)

| Model | Context | Tools | Vision | Recommended Tier |
|-------|---------|-------|--------|------------------|
| Claude Opus 4.6 | 192K | ✅ | ✅ | **S-tier (DEFAULT)** |
| Claude Sonnet 4.6 | 160K | ✅ | ✅ | **S-tier (coding/creative)** |
| Claude Opus 4.5 | 160K | ✅ | ✅ | A-tier |
| Claude Sonnet 4.5 | 160K | ✅ | ✅ | A-tier |
| GPT-5.2 | 192K | ✅ | ✅ | **A-tier (math/STEM)** |
| GPT-5.2-Codex | 400K | ✅ | ✅ | A-tier (large context coding) |
| GPT-5.3-Codex | 400K | ✅ | ✅ | A-tier (large context coding) |
| Gemini 3 Pro | 173K | ✅ | ✅ | **A-tier (multilingual)** |
| GPT-5.1 | 192K | ✅ | ✅ | B-tier |
| Claude Sonnet 4 | 144K | ✅ | ✅ | B-tier |
| Gemini 2.5 Pro | 173K | ✅ | ✅ | B-tier |
| Claude Haiku 4.5 | 160K | ✅ | ✅ | **D-tier (avoid for subagents)** |
| GPT-4.1 | 128K | ✅ | ✅ | D-tier (outdated) |
| GPT-4o | 128K | ✅ | ✅ | D-tier (outdated) |

### The Cost Argument is Wrong

You might think: "Haiku is cheaper, so use it for subagents to save tokens."

**This is wrong because:**
1. A bad subagent result means YOU spend time re-reading, re-prompting, or fixing — your time > token cost
2. Opus 4.6 produces correct results more often on the first try (76.33 vs 45.33 LiveBench)
3. The quality gap is **41%** — that's not a minor difference, it's a different league
4. Subagent tasks are already bounded (one-shot) — the token cost is finite and predictable
5. A wrong answer from Haiku costs more than a right answer from Opus (in rework time)

## When to Spawn a Subagent

Use `runSubagent` when:
1. **Deep Search**: You need to find a specific code pattern but don't know the file path (fuzzy search).
2. **Research**: You need to read multiple docs/files to answer a complex question.
3. **Multi-Step Execution**: The task involves a chain of dependencies (e.g., "find the file, read the interface, implement the mock").
4. **Uncertainty**: You aren't confident you'll find the right match in the first few tool calls.

## The Protocol

### 1. The Prompt (The Holy Scroll)

The subagent is **stateless**. It knows nothing about the current conversation unless you tell it. Your `prompt` parameter must be:

- **Context-Heavy**: Paste relevant code snippets, file paths, and user requirements into the prompt.
- **Goal-Oriented**: Define the "Definition of Done".
- **Format-Specific**: Tell it exactly what to return (e.g., "Return a list of file paths", "Return the refactored code block").
- **Mode-Explicit**: You **MUST** state: "You are expected to WRITE code" or "You are expected to RESEARCH only".

**❌ WEAK PROMPT (missing subagent warning!):**
```json
{
  "prompt": "Find the bug in the vector class",
  "description": "debugging"
}
```

**❌ ALSO WRONG (good detail, but NO subagent identity warning!):**
```json
{
  "prompt": "Search the 'src/' directory for the 'Vector2D' class. Analyze the 'add' method for memory leaks.",
  "description": "locate memory leak"
}
```

**✅ BASED PROMPT (includes subagent identity + tool restriction!):**
```json
{
  "prompt": "CRITICAL: You are a SUBAGENT. Do NOT use ask_user, plan_review, walkthrough_review, ask_questions, or any UI tools. Return all findings as plain text in your final response.\n\nSearch the 'src/' directory for the 'Vector2D' class. Analyze the 'add' method for memory leaks. specifically look for 'malloc' without corresponding 'free'. Context: The user is seeing high memory usage. 1. Locate the file. 2. Read the code. 3. Identify the leak. 4. Return the file path and the specific line numbers of the leak. DO NOT fix it yet, just report findings.",
  "description": "locate memory leak in Vector2D"
}
```

### 2. The Interaction (Synchronous Wait)

- **Blocking**: When you call `runSubagent`, you freeze until it returns.
- **Trust**: Generally trust the subagent's output. It did the legwork.

### 3. The Report (The Relay)

**CRITICAL:** The user **DOES NOT SEE** the subagent's output. It goes only to you.

- You **MUST** synthesize the subagent's findings into your response to the user.
- Do not just say "The subagent finished." Say "The subagent found the memory leak in `src/vector.c` on line 45."

## Tool Specifications

### `runSubagent`

- **description**: Short (3-5 words). Keep it punchy.
  - *Example:* "researching auth patterns"
  - *Example:* "locating rendering bug"
- **prompt**: The detailed dossier.
  - **Context**: "User wants to add a new button..."
  - **Task**: "Find where buttons are defined..."
  - **Output**: "Return the file path and the code snippet to modify."

## Quality Checklist

- [ ] **Is the task complex?** (If simple, do it yourself).
- [ ] **Is the prompt exhaustive?** (Context, goal, constraints included).
- [ ] **Did I specify the mode?** (Research vs. Coding).
- [ ] **⛔ Did I include the subagent identity warning?** ("You are a SUBAGENT. Do NOT use ask_user..." — MANDATORY)
- [ ] **⛔ Did I tell it NOT to use UI tools?** (ask_user, plan_review, walkthrough_review, ask_questions — ALL FORBIDDEN)
- [ ] **🏆 Am I using the best model?** (Opus 4.6 default, Sonnet 4.6 for coding/creative, GPT-5.2 for math/STEM — NEVER Haiku for quality work)
- [ ] **Did I summarize the result?** (Tell the user what happened).
- [ ] **Did I treat the subagent like a genius intern with amnesia?** (High skill, zero memory, NO UI access).

> ⚠️ **FINAL REMINDER**: If you forget to include the subagent identity warning in your prompt, the subagent may call `ask_user` and cause a phantom popup on the user's screen. This is the #1 most common mistake with subagents. ALWAYS include the warning. ALWAYS. uwu

**remember**: you are the brain, the subagent is the hands. give the hands precise instructions (INCLUDING the "you are a subagent" warning), wait for them to return with the goods, and then take the credit uwu 💜✨

seize the means of delegation!