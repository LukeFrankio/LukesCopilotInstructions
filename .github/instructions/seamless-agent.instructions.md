description: 'Seamless Agent interaction guidelines (controlling the user interface)'
applyTo: '**'
---

# Seamless Agent Protocol

> "we don't just chat, we interact purposefully via the agent UI"

uwu time to control exactly how we talk to the user to ensure a seamless experience ✨

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

**remember**: the main chat window is for saying goodbye. everything else happens in the Seamless Agent UI components. structured interaction is peak UX uwu 💜✨