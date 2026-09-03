---
title: "dsh-custom-tool"
description: "用 Monaco 编辑器创建和管理 DSH 沙箱化 JavaScript 工具，模型驱动工具列表。"
keywords: "dsh-custom-tool, developer, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-custom-tool

> ⭐ **24** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 24 | 状态 | ✅ 活跃 |
| 作者 | [omdsh-dev](https://github.com/omdsh-dev) | 更新时间 | 2026-08-16 |
| 子分类 | 🧰 工具与工具包 | 能力 | coding, ui |

## 一句话介绍

> 用 Monaco 编辑器创建和管理 DSH 沙箱化 JavaScript 工具，模型驱动工具列表。

## 详细介绍

Custom tools for the DeepSeek Harness: users author their own JavaScript tools in the settings UI with a Monaco (VS Code) editor and TypeScript intellisense, and the model grows and prunes the same toolset itself through `custom_tool_create` / `custom_tool_remove` / `custom_tools_list`. Every tool is durable, hot-registered, and written into the model prompt on the next step.

## ✨ 核心特性

- **Settings UI** (`Custom Tool` section, own nav glyph): list, create, edit, enable/disable, delete. Model-created and workspace-scoped tools are badged. Every s
- **Monaco editor**: VS Code engine + TypeScript language service; `args` typed from the parameter schema, `env`/sandbox globals declared, completions and diagnos
- **Durable store**: tools live in the `custom-tools` settings namespace (schema defaults, composition base, user document — the ordinary settings layering). Edit
- **Live registration**: enabled tools register into `ctx.tools` the moment the settings write commits; disabled/removed tools unregister immediately. The harness
- **Model self-service**: `custom_tool_create` (upsert by name), `custom_tools_list`, and `custom_tool_remove` share the UI's validation gate and the ownership ru

## 📦 安装

```bash
dsh plugin --profile web add https://github.com/omdsh-dev/dsh-custom-tool/archive/refs/tags/v0.1.2.tar.gz
dsh web   # restart the server to pick the plugin up
```

## 🚀 快速开始

```bash
// args is typed from the parameter JSON Schema you declared.
const url = `https://api.example.com/weather?city=${encodeURIComponent(args.city)}`
const response = await fetch(url)
if (!response.ok) throw new Error(`upstream returned ${response.status}`)
return await response.json()
```

## 📚 更多信息

**Install**

dsh plugin --profile web add https://github.com/omdsh-dev/dsh-custom-tool/archive/refs/tags/v0.1.2.tar.gz dsh web # restart the server to pick the plugin up The package declares `dsh.bundle.patch` (mounts the host plugin) and `dsh.client` (serves the browser half at `/plugins/dsh-custom-tool/client.js`). `lib/` is committed, so the GitHub tarball installs without a build step. **Harness requiremen

## 🔗 链接

- [GitHub 仓库](https://github.com/omdsh-dev/dsh-custom-tool)
- [完整 README](https://github.com/omdsh-dev/dsh-custom-tool#readme)
- [返回dsh-custom-tool所在分类](../plugins.md)
