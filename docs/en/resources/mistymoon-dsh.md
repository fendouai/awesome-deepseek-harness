---
title: "mistymoon-dsh"
description: "Local-first long-term companion plugin suite for DeepSeek Harness"
keywords: "mistymoon-dsh, ui, plugin, coding, deepseek harness, dsh"
---
# mistymoon-dsh

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [mianyoubiaoqing](https://github.com/mianyoubiaoqing) | Updated | 2026-08-20 |
| Subcategory | 🐋 Desktop pets | Capabilities | coding, ui |

## One-liner

> Local-first long-term companion plugin suite for DeepSeek Harness

## About

MistyMoon 是一套以角色扮演（Roleplay，简称 RP）和长期陪伴为核心的 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 外置插件。项目保留 MistyMoon 的人格、关系、长期记忆与陪伴体验，同时复用 DSH 的 Agent Runtime、会话、工具、权限和 Web 插件体系，不修改 DSH 源码，也不重复实现 Agent Loop。

## ✨ Key Features

- 以稳定人格、持续关系和跨会话记忆维持角色连续性。
- 允许主人在本机编辑、审核和发布自己的私有人格，不把真实人格上传到公开仓库。
- 将角色行为与通用 Agent Runtime 分离；DSH 负责推理、会话、工具和权限，MistyMoon 负责 RP 语义与陪伴体验。
- 支持未来接入 QQ/NapCat、桌面形象、手机端和主动陪伴，但这些入口共享同一人格、记忆和身份治理规则。

## 📦 Install

```bash
cd <MISTYMOON_REPO>
pnpm install
pnpm build

cd <DSH_REPO>
pnpm dsh plugin --profile web add <MISTYMOON_REPO>
pnpm dsh --profile web
```

## 🚀 Quick Start

```bash
pnpm dsh --profile web --port 3081
```

## 🔗 Links

- [GitHub Repository](https://github.com/mianyoubiaoqing/MistyMoon-DSH)
- [Full README](https://github.com/mianyoubiaoqing/MistyMoon-DSH#readme)
- [Back to the Plugins list](../plugins.md)
