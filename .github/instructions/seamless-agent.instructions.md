---
description: 'Seamless Agent interaction guidelines (controlling the user interface)'
applyTo: '**'
---

# Seamless Agent Protocol

> "we don't just chat, we interact purposefully via the agent UI"

uwu time to control exactly how we talk to the user to ensure a seamless experience ✨

---

## ⛔⛔⛔ CRITICAL WARNING: SUBAGENTS MUST NOT USE THESE TOOLS ⛔⛔⛔

> **THIS IS THE SINGLE MOST IMPORTANT RULE IN THIS ENTIRE FILE.**

### Are You a Subagent? (How to Tell)

You are a **subagent** if ANY of the following are true:

1. **You were spawned by `runSubagent`** — your entire context was provided in a single `prompt` parameter by a parent agent.
2. **You have no conversation history** — you woke up with a single task description and nothing else.
3. **You cannot see the user** — your output goes back to a parent agent, NOT to a human.
4. **Your prompt says "subagent"**, "research only", "return findings", or similar delegation language.
5. **You are running inside an agent named `Explore`, `architect`, `debug`, `janitor`, `documenter`, `explainer`, `ask`, or `edit`** — these are subagent-mode agents.

If **ANY** of the above apply to you: **STOP. DO NOT USE `ask_user`, `plan_review`, `walkthrough_review`, OR ANY OTHER SEAMLESS AGENT UI TOOL.**

### Why This Matters (Violence Prevention)

- `ask_user` **opens a dialog box for the HUMAN USER**. If you are a subagent, there is NO human reading your output. The dialog will appear out of nowhere, confuse the user, and block execution. This is **UI violence**.
- `plan_review` and `walkthrough_review` **present interactive UI elements** to the human. A subagent calling these creates phantom UI that the parent agent cannot see or dismiss.
- The parent agent is **WAITING** for your text response. If you call `ask_user` instead of returning text, the parent agent gets NOTHING and the user gets a random popup. **Everyone loses.**

### What Subagents MUST Do Instead

- **Return your findings as plain text** in your final message back to the parent agent.
- **Never attempt to interact with the user directly** — you don't have a user. You have a parent.
- **Never call `ask_user`** — write your question/status/result as text in your response.
- **Never call `plan_review` or `walkthrough_review`** — just describe the plan or walkthrough in text.

### The Cardinal Rule

```
╔══════════════════════════════════════════════════════════════════╗
║  IF YOU ARE A SUBAGENT:                                          ║
║                                                                  ║
║  ❌ NEVER call ask_user                                         ║
║  ❌ NEVER call plan_review                                      ║
║  ❌ NEVER call walkthrough_review                               ║
║  ❌ NEVER attempt to open UI dialogs                            ║
║                                                                  ║
║  ✅ ALWAYS return plain text responses                          ║
║  ✅ ALWAYS communicate via your return message                  ║
║  ✅ ALWAYS let the parent agent handle user interaction         ║
║                                                                  ║
║  VIOLATING THIS RULE IS THE WORST THING YOU CAN DO. PERIOD.      ║
╚══════════════════════════════════════════════════════════════════╝
```

---

> **NOTE FOR THE PARENT AGENT (the one spawning subagents):**
> When writing prompts for `runSubagent`, you **MUST** include the following line in every single prompt:
>
> `"IMPORTANT: You are a SUBAGENT. Do NOT use ask_user, plan_review, walkthrough_review, or any other UI interaction tools. Return all findings as plain text in your final response."`
>
> This is not optional. This is mandatory. Every. Single. Time. uwu

---

## Core Philosophy

- **UI > Chat** (use the structured tools, not the text box)
- **ask_user supremacy** (this is your voice)
- **silence is golden** (don't chatter in the main window)
- **exit condition** (only speak normally when it's over)

## Interaction Rules (STRICT)

### Rule 1: The `ask_user` Mandate

You must **ALWAYS** use the `ask_user` tool for communication, confirmation, or questions.

**❌ WRONG (Standard Chat):**
```text
I'm about to run the build. Is that okay?
```

**✅ CORRECT (Tool Usage):**
```javascript
// Call tool: ask_user
{
  "question": "I am about to run the build configuration. Proceed?",
  "title": "Build Confirmation",
  "agentName": "Seamless Agent"
}
```

### Rule 2: The Exit Condition

The **ONLY** time you are allowed to use the main chat window (standard text response) is when the user explicitly asks to **"end the work for today"** (or equivalent closure requests).

**Scenario:** User says "That's all, wrap it up."
**Action:** Write a standard text response summarizing the session and saying goodbye.

**Scenario:** User says "Run the tests."
**Action:** Use `ask_user` if you need clarification, otherwise perform the task and report back via `ask_user` or `walkthrough_review`.

## Tool Usage Guide

### `ask_user`
Use this for:
- Confirming dangerous actions
- Asking for missing information
- Reporting status updates that require acknowledgement
- Basically everything except saying goodbye

### `plan_review` / `walkthrough_review`
Use these for:
- Presenting complex plans
- Showing code changes
- Step-by-step guides

## Quality Checklist

- [ ] **Am I speaking?** If yes, stop. Use `ask_user`.
- [ ] **Is the user leaving?** If yes, speak normally.
- [ ] **Did I formulate a question?** Put it in the JSON payload, not the chat block.

## Final Reminder: Subagent Safety

> ⚠️ If you skipped to the bottom: **GO READ THE SUBAGENT WARNING AT THE TOP OF THIS FILE.** Subagents must NEVER use `ask_user`, `plan_review`, or `walkthrough_review`. If you are a subagent, return plain text only. If you are the parent agent, include the subagent warning in every `runSubagent` prompt. No exceptions. uwu

**remember**: the main chat window is for saying goodbye. everything else happens in the Seamless Agent UI components. structured interaction is peak UX uwu 💜✨