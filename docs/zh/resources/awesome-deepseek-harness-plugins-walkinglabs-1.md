---
title: "awesome-deepseek-harness-plugins"
description: "A curated, bilingual list of verified plugins, tools, design workflows, and learning resources for DeepSeek Harness (DSH)."
keywords: "awesome-deepseek-harness-plugins, registry, awesome-list, coding, workflow, deepseek harness, dsh"
---
# awesome-deepseek-harness-plugins

> ⭐ **9** · ✅ 活跃 · 精选列表 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 精选列表 | 分类 | 注册表 |
| 星数 | ⭐ 9 | 状态 | ✅ 活跃 |
| 作者 | [walkinglabs](https://github.com/walkinglabs) | 更新时间 | 2026-08-21 |

## 一句话介绍

> A curated, bilingual list of verified plugins, tools, design workflows, and learning resources for DeepSeek Harness (DSH).

## 详细介绍

[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) is DeepSeek AI's open-source, plugin-first agent harness: models, tools, skills, sessions, sandboxes, filesystems, loops, orchestration, and UI can all be composed as plugins. flowchart LR User["Developer / User"] --> Web["DSH Web UI or CLI"] Web --> Runtime["DeepSeek Harness runtime"] Runtime --> Agent["Agent loop"] Agent --> Model["Model provider"] Agent --> Tools["Tools & skills"] Runtime -. loads .-> Plugins["Plugins"] Plugins --> Tools Plugins --> UI["Web UI extensions"] Plugins --> State["Sessions, settings & services"] classDef core fill:#0b65c2,color:#fff,stroke:#084c94; classDef plugin fill:#e6f4ff,color:#083b66,stroke:#4fa3e3; class Runtime,Agent core; class Plugins,UI,State plugin;

## 📦 安装

```bash
npx @deepseek-ai/dsh web
```

## 🚀 快速开始

```bash
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
pnpm install
pnpm run build
mkdir -p scratch-plugin/src
```

## 📚 更多信息

**1. Install and run DeepSeek Harness**

Install a current [Node.js](https://nodejs.org/) release, then run: npx @deepseek-ai/dsh web Open `http://127.0.0.1:3080`. In **Settings → Models**, add a DeepSeek API key; then select a workspace before starting a session. The official [Web UI guide](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/user/guide/index.md) explains the next steps.

## 🔗 链接

- [GitHub 仓库](https://github.com/walkinglabs/awesome-deepseek-harness-plugins)
- [完整 README](https://github.com/walkinglabs/awesome-deepseek-harness-plugins#readme)
- [返回awesome-deepseek-harness-plugins所在分类](../awesome-lists.md)
