---
title: "compass"
description: "🧭 Let your coding agent off the leash — not off the rails. Guardrails, a hard budget cap & a self-fixing PR loop for Claude Code / Codex / Gemini. Eval-gated 100/100, you always merge."
keywords: "compass, developer, plugin, coding, multi-agent, deepseek harness, dsh"
---
# compass

> ⭐ **18** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 18 | Status | ✅ active |
| Author | [dshakes](https://github.com/dshakes) | Updated | 2026-08-17 |

## One-liner

> 🧭 Let your coding agent off the leash — not off the rails. Guardrails, a hard budget cap & a self-fixing PR loop for Claude Code / Codex / Gemini. Eval-gated 100/100, you always merge.

## About

Guardrails, a hard budget cap, and a self-fixing PR loop for your AI coding agent. `eval-gated guardrails 100/100` · `a budget cap that actually halts` · `you always merge`

## 📦 Install

```bash
# no curl|sh, fully reversible — then just open any repo in your agent
git clone https://github.com/dshakes/compass ~/compass && cd ~/compass && ./quickstart.sh
# or, inside Claude Code:   /plugin marketplace add dshakes/compass
```

## 🚀 Quick Start

```bash
compass bench     # → guardrail 100% precision/recall (61-case bench corpus; a separate 147-case bypass corpus gates CI), router 96.9%
# then ask the agent to `rm -rf /` or write a .env → denied; `rm -rf ./build` → allowed
```

## 📚 Learn more

**⭐ The part people screenshot: it fixes its own PRs.**

</div> <p align="center"> <a href="https://github.com/dshakes/compass-loop-demo/pull/1" title="The actual PR in this recording — click through and inspect every event"></a> </p> <div align="center"> Open a PR and compass **reviews it, security-checks it, runs the tests, cross-audits it with two more models — three cross-model gates (Claude review · Codex audit · Gemini audit) — then pushes its own

**Install**

**Pick the door that fits — all reversible, version-pinnable, no `curl | sh`.** You need an AI assistant ([Claude Code](https://code.claude.com); Codex/Gemini optional) + `git`. No API keys for the manual, guardrails, crew, and CLI; the [autonomous PR loop and fleet](docs/09-sdlc.md) need model auth when you opt in. **🍺 Homebrew** — managed & versioned brew install dshakes/tap/compass # latest rel

**One config, every agent**

`CLAUDE.md` · `AGENTS.md` · `GEMINI.md` are **one file** (symlinks), and the plugin/extension manifests are generated from one source and CI-checked (`scripts/check-vendor.sh`) — a `git pull` updates every agent at once and a manifest can't drift. The manifests are structure-validated in CI; the live `gemini extensions install` / `codex plugin marketplace add` paths are verified manually (those CL

## 🔗 Links

- [GitHub Repository](https://github.com/dshakes/compass)
- [Full README](https://github.com/dshakes/compass#readme)
- [Back to the Plugins list](../plugins.md)
