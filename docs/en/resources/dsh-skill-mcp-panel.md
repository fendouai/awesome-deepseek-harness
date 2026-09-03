---
title: "dsh-skill-mcp-panel"
description: "DSH Web UI plugin: skill and MCP management（Web界面的skill/MCP管理工具）"
keywords: "dsh-skill-mcp-panel, mcp, integration, coding, ui, deepseek harness, dsh"
---
# dsh-skill-mcp-panel

> ⭐ **111** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | MCP |
| Stars | ⭐ 111 | Status | ✅ active |
| Author | [Fishquito7](https://github.com/Fishquito7) | Updated | — |

## One-liner

> DSH Web UI plugin: skill and MCP management（Web界面的skill/MCP管理工具）

## About

[English](README.en.md) | 简体中文 DSH 插件，在 Web 设置页同时提供「技能」与「MCP」两个管理面板，并随包提供统一终端命令 `dsh-panel`（`skill` / `mcp` 两个子命令族）。 注意：本项目提供的参考命令默认指定profile为默认的--profile web，需要更改profile的请自行注意。

## ✨ Key Features

- skill 卡片列表：预览已注册安装的 skill，点击卡片可展开查看完整内容
- skill 状态：启用、停用状态标签，与内置插件列表同款样式
- skill 管理：开关热启用/停用、删除；按名称搜索；进入页面自动刷新
- skill 添加（0.7.0 统一入口）：点“+”直接选文件（`.md` / `.zip`），或把文件、压缩包、
- **工作区分栏**（0.3.0）：技能实体直接存放在其所属位置里——全局在
- **批量迁移**：“+”号左侧的迁移按钮：源工作区、目标工作区（**可多选**）与技能都在

## 📦 Install

```bash
dsh plugin --profile web add https://github.com/Fishquito7/dsh-skill-mcp-panel/releases/download/v2.0.2/dsh-skill-mcp-panel-2.0.2.tgz
```

## 🚀 Quick Start

```bash
> dsh plugin --profile web add github:Fishquito7/dsh-skill-mcp-panel
   >
```

## 📚 Learn more

**安装**

1. 安装本包（bundle 层自动挂载，无需编辑配置文件） ```bash dsh plugin --profile web add https://github.com/Fishquito7/dsh-skill-mcp-panel/releases/download/v2.0.2/dsh-skill-mcp-panel-2.0.2.tgz ``` > 首选发行版 tarball：不走 Git，不受 pnpm v11 的构建脚本限制。 > 也可以从 Git 安装（Git 来源的依赖默认禁止运行 prepare 构建脚本；若报 > “git-hosted plugins build on install...”，把 pnpm 在上面打印的 key 加到 > profile 目录 `pnpm-workspace.yaml` 的 `allowBuilds` 下再重跑）： > > ```bash

## 🔗 Links

- [GitHub Repository](https://github.com/Fishquito7/dsh-skill-mcp-panel)
- [Full README](https://github.com/Fishquito7/dsh-skill-mcp-panel#readme)
- [Back to the MCP & Integrations list](../integrations.md)
