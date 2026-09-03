---
title: "awesome-dsh-plugin"
description: "A curated list of plugins for DeepSeek Harness (dsh) - DeepSeek Harness plugin ecosystem"
keywords: "awesome-dsh-plugin, registry, awesome-list, coding, deepseek harness, dsh"
---
# awesome-dsh-plugin

> ⭐ **966** · ✅ 活跃 · 精选列表 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 精选列表 | 分类 | 注册表 |
| 星数 | ⭐ 966 | 状态 | ✅ 活跃 |
| 作者 | [Anil-matcha](https://github.com/Anil-matcha) | 更新时间 | 2026-08-20 |

## 一句话介绍

> A curated list of plugins for DeepSeek Harness (dsh) - DeepSeek Harness plugin ecosystem

## 详细介绍

[`deepseek-ai/deepseek-harness`](https://github.com/deepseek-ai/deepseek-harness) is DeepSeek's open-source agent harness, currently in developer preview. Its defining idea is **everything is a plugin**: the model provider, the sandbox, the tool set, the session store, and the UI are all plugins loaded into a Cordis-based runtime, so you can replace or extend any layer without forking the harness itself. Plugins declare a `dsh.bundle` manifest and install with: dsh plugin --profile web add

## ✨ 核心特性

- [988hj7tczd-oss/dsh-computer-use](https://github.com/988hj7tczd-oss/dsh-computer-use) — Cross-platform Computer Use: virtual-mouse operation, AX-tree zero-visio
- [Anionex/dsh-computer-use](https://github.com/Anionex/dsh-computer-use) — Accessibility-first macOS computer use with fresh observations, stale-state rejection,
- [AbnerAI/dsh-monitor](https://github.com/AbnerAI/dsh-monitor) — Persistent background watchers that wake the agent on new events — the harness analog of a Monit
- [akqwpeter-prog/dsh-agent-conductor](https://github.com/akqwpeter-prog/dsh-agent-conductor) — Dispatches tasks from DSH to 11 external agent CLIs (Codex, Claude
- [AngelosZou/dsh-multi-folder](https://github.com/AngelosZou/dsh-multi-folder) — Secondary working directories with equal read/write/exec permissions.
- [anweat/dsh-browser](https://github.com/anweat/dsh-browser) — Self-contained Playwright + OpenCLI browser runtime exposing 9 interactive browser tools.
- [anweat/dsh-voice-webspeech](https://github.com/anweat/dsh-voice-webspeech) — Browser Web Speech API voice input: zero server, zero keys.
- [scriptsnet/dsh-fleet](https://github.com/scriptsnet/dsh-fleet) — Distributed compute fleet for DSH: pool idle machines (friends' PCs, LAN servers, cloud ECS) i

## 📦 安装

```bash
dsh plugin --profile web add <plugin-name>
```

## 🚀 快速开始

```bash
# run the Web UI (served at http://127.0.0.1:3080 by default)
npx @deepseek-ai/dsh web

# or from a source checkout
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness && pnpm install && pnpm run build && pnpm dsh web
```

## 🔗 链接

- [GitHub 仓库](https://github.com/Anil-matcha/awesome-dsh-plugin)
- [完整 README](https://github.com/Anil-matcha/awesome-dsh-plugin#readme)
- [返回awesome-dsh-plugin所在分类](../awesome-lists.md)
