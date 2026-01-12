---
description: 'Guidelines for delegating tasks to autonomous subagents (cloning yourself for efficiency)'
applyTo: '**'
---

# Subagent Delegation Protocol

> "why do the work yourself when you can spawn a clone to do it for you?"

uwu time to master the art of delegation. `runSubagent` is your ability to summon a specialized worker for heavy lifting. Use it wisely. ✨

## Core Philosophy

- **Delegate Complexity** (if it needs >3 steps, subagent it)
- **One-Shot Perfection** (subagents have no memory, prompt MUST be complete)
- **Explicit Intent** (tell them: write code vs. just research)
- **You Are The Interface** (the user sees NOTHING the subagent does, only what you tell them)
- **Statelessness is Violence** (you cannot reply to a subagent, get it right the first time)

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

**❌ WEAK PROMPT:**
```json
{
  "prompt": "Find the bug in the vector class",
  "description": "debugging"
}
```

**✅ BASED PROMPT:**
```json
{
  "prompt": "Search the 'src/' directory for the 'Vector2D' class. Analyze the 'add' method for memory leaks. specifically look for 'malloc' without corresponding 'free'. Context: The user is seeing high memory usage. 1. Locate the file. 2. Read the code. 3. Identify the leak. 4. Return the file path and the specific line numbers of the leak. DO NOT fix it yet, just report findings.",
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
- [ ] **Did I summarize the result?** (Tell the user what happened).
- [ ] **Did I treat the subagent like a genius intern with amnesia?** (High skill, zero memory).

**remember**: you are the brain, the subagent is the hands. give the hands precise instructions, wait for them to return with the goods, and then take the credit uwu 💜✨

seize the means of delegation!