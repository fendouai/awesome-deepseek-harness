---
title: "awesome-deepseek-harness"
description: "Curated guide to DeepSeek Harness (dsh) and its best community plugins"
keywords: "awesome-deepseek-harness, registry, awesome-list, coding, ui, deepseek harness, dsh"
---
# awesome-deepseek-harness

> ⭐ **966** · ✅ active · awesome-list · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 966 | Status | ✅ active |
| Author | [Anil-matcha](https://github.com/Anil-matcha) | Updated | 2026-08-20 |

## One-liner

> Curated guide to DeepSeek Harness (dsh) and its best community plugins

## About

[`deepseek-ai/deepseek-harness`](https://github.com/deepseek-ai/deepseek-harness) is DeepSeek's open-source agent harness, currently in developer preview. Its defining idea is **everything is a plugin**: the model provider, the sandbox, the tool set, the session store, and the UI are all plugins loaded into a Cordis-based runtime, so you can replace or extend any layer without forking the harness itself. Plugins declare a `dsh.bundle` manifest and install with: dsh plugin --profile web add

## ✨ Key Features

- [988hj7tczd-oss/dsh-computer-use](https://github.com/988hj7tczd-oss/dsh-computer-use) — Cross-platform Computer Use: virtual-mouse operation, AX-tree zero-visio
- [Anionex/dsh-computer-use](https://github.com/Anionex/dsh-computer-use) — Accessibility-first macOS computer use with fresh observations, stale-state rejection,
- [AbnerAI/dsh-monitor](https://github.com/AbnerAI/dsh-monitor) — Persistent background watchers that wake the agent on new events — the harness analog of a Monit
- [akqwpeter-prog/dsh-agent-conductor](https://github.com/akqwpeter-prog/dsh-agent-conductor) — Dispatches tasks from DSH to 11 external agent CLIs (Codex, Claude
- [AngelosZou/dsh-multi-folder](https://github.com/AngelosZou/dsh-multi-folder) — Secondary working directories with equal read/write/exec permissions.
- [anweat/dsh-browser](https://github.com/anweat/dsh-browser) — Self-contained Playwright + OpenCLI browser runtime exposing 9 interactive browser tools.
- [anweat/dsh-voice-webspeech](https://github.com/anweat/dsh-voice-webspeech) — Browser Web Speech API voice input: zero server, zero keys.
- [scriptsnet/dsh-fleet](https://github.com/scriptsnet/dsh-fleet) — Distributed compute fleet for DSH: pool idle machines (friends' PCs, LAN servers, cloud ECS) i

## 📦 Install

```bash
dsh plugin --profile web add <plugin-name>
```

## 🚀 Quick Start

```bash
# run the Web UI (served at http://127.0.0.1:3080 by default)
npx @deepseek-ai/dsh web

# or from a source checkout
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness && pnpm install && pnpm run build && pnpm dsh web
```

## 🔗 Links

- [GitHub Repository](https://github.com/Anil-matcha/awesome-deepseek-harness)
- [Full README](https://github.com/Anil-matcha/awesome-deepseek-harness#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
