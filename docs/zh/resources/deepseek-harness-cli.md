---
title: "deepseek-harness-cli"
description: "DeepSeek CLI"
keywords: "deepseek-harness-cli, vision, plugin, coding, deepseek harness, dsh"
---
# deepseek-harness-cli

> ⭐ **58** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 58 | 状态 | ✅ 活跃 |
| 作者 | [peiyuwang54](https://github.com/peiyuwang54) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> DeepSeek CLI

## 详细介绍

`deepseek-harness-cli` is a terminal front door for DeepSeek Harness. It maps prompts, sessions, tools, approvals, questions, models, presets, commands, skills, workspaces, and durable events to the official DSH services instead of creating a parallel agent runtime. The project combines a responsive React terminal renderer with a small DSH adapter and an isolated `dsh-cli` profile. You get a focused Claude Code-style workflow while Harness remains the source of truth for execution and persistence.

## 📦 安装

```bash
npm install -g @deepseek-ai/dsh deepseek-harness-cli
```

## 🚀 快速开始

```bash
npm install -g @deepseek-ai/dsh
git clone https://github.com/Richard-Yang0130/deepseek-harness-cli.git
cd deepseek-harness-cli
corepack enable pnpm
pnpm install --frozen-lockfile
npm run build
npm link
```

## 📚 更多信息

**Configuration, plugins, and MCP**

The profile is a Cordis composition. Compatible DSH plugins automatically contribute commands to `/`; MCP tools use the official Harness tool registry. Keep MCP credentials in environment variables and never commit plaintext secrets to `cordis.patch.yml`. Read [configuration](docs/configuration.md), [plugins and MCP](docs/plugins.md), and [themes](docs/themes.md) before changing the profile.

**Architecture**

dsh-cli launcher -> isolated dsh profile (Cordis composition) -> official Harness services and durable session events -> DSH adapter / Channel -> React terminal screens and components -> terminal renderer, input, selection, layout, and cleanup The adapter boundary keeps terminal mechanics replaceable without forking Harness domain services. Read the [architecture notes](docs/architecture.md) and [

**Update and uninstall**

For a source installation, update the clone and rebuild: git pull --ff-only pnpm install --frozen-lockfile npm run build npm link Uninstall the global command: npm uninstall -g deepseek-harness-cli The isolated DSH profile and `~/.dsh-cli` preferences remain available for a future reinstall unless you remove them yourself.

## 🔗 链接

- [GitHub 仓库](https://github.com/peiyuwang54/deepseek-harness-cli)
- [完整 README](https://github.com/peiyuwang54/deepseek-harness-cli#readme)
- [返回deepseek-harness-cli所在分类](../plugins.md)
