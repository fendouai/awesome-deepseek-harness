---
title: "dsh-anchored-standard"
description: "Two-phase DeepSeek Harness preset: Minimal-aligned bootstrap, then full Standard tools (Project2 98/99)"
keywords: "dsh-anchored-standard, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-anchored-standard

> ⭐ **3,697** · ✅ 活跃 · 插件 · 近期 ⬆️ +28

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 3,697 | 状态 | ✅ 活跃 |
| 作者 | [xiaobright](https://github.com/xiaobright) | 更新时间 | 2026-08-17 |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Two-phase DeepSeek Harness preset: Minimal-aligned bootstrap, then full Standard tools (Project2 98/99)

## 详细介绍

[中文说明](./README.zh-CN.md) Experimental DeepSeek Harness agent presets — a base mode, two live-anchor variants, and one seeded prefab mode — that anchor a session's model trajectory on the Minimal condition (real Minimal tool schema, no auto-injected context), then promote to a small resident catalog once the session is durable, unlocking heavier Standard tools on demand. This is a community project. It is not an official DeepSeek preset and is not affiliated with or endorsed by DeepSeek. Feel free to submit feedback on the plugin in the form of Issues or PRs. For ideas for new plugins or useful findings, please submit them under the [repository](https://github.com/0liveiraaa/DeepseekCotexplorations).

## ✨ 核心特性

- [dsh-routing-suite](https://github.com/yjh051108/dsh-routing-suite) — a runtime injector
- [J-Space Cognition Suite](https://github.com/Tiger3807861189/J-Space-Cognition-Suite-V3.6)

## 🚀 快速开始

```bash
$target = Join-Path $env:USERPROFILE '.dsh\.agent-presets\anchored-standard'
if (Test-Path -LiteralPath $target) { throw "Preset already exists: $target" }
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $target) | Out-Null
Copy-Item -Recurse -LiteralPath '.\preset' -Destination $target
```

## 📚 更多信息

**Configuration reference**

All knobs are rows in each mode's `agent.cordis.yml`. Unknown keys fail at preset mount. `context-gate` (mounted FIRST in `preset/`, `zero-anchored-standard/`, and `whoami-standard/` — waterfall registration order makes the gate the outermost transform; the plugin lives in `shared/context-gate.mjs` and is reusable by any other composition that wants unified injection control alone): Injection cont

**Install**

For the prefab mode, the recommended path is AI-assisted one-command setup. Give your coding agent this repository and ask it to follow the [installation-agent contract](./prefab/AGENT_INSTALL.md). When it reports `INSTALL READY`, start DSH, select **Prefab Anchored Standard**, create a new session in the target workspace, and send the real task prompt. This installs the generic template; the Proj

## 🔗 链接

- [GitHub 仓库](https://github.com/xiaobright/dsh-anchored-standard)
- [完整 README](https://github.com/xiaobright/dsh-anchored-standard#readme)
- [返回dsh-anchored-standard所在分类](../plugins.md)
