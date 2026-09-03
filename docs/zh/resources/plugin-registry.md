---
title: "plugin-registry"
description: "DSH 插件生态基建：薄控制台管理官方 repository 插件（0 patch）+ make-dsh-plugin 技能。"
keywords: "plugin-registry, registry, awesome-list, workflow, ui, deepseek harness, dsh"
---
# plugin-registry

> ⭐ **57** · ✅ 活跃 · 精选列表 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 精选列表 | 分类 | 注册表 |
| 星数 | ⭐ 57 | 状态 | ✅ 活跃 |
| 作者 | [vlln](https://github.com/vlln) | 更新时间 | 2026-08-19 |

## 一句话介绍

> DSH 插件生态基建：薄控制台管理官方 repository 插件（0 patch）+ make-dsh-plugin 技能。

## 详细介绍

DeepSeek Harness's official mechanisms define "what a plugin is and how it runs"; this repository adds two things (panel structure: [console README](packages/plugin/console/README.md); guidance: below): 1. **Thin console** (`packages/plugin/console`) — browser panel managing a profile's plugin install state + 4 agent tools 2. **Development spec and guidance** — `make-dsh-plugin` skill + cookbook for creating official bundle/cordis plugins

## 📦 安装

```bash
dsh plugin --profile web add "github:vlln/plugin-registry#path:/packages/plugin/console"
```

## 🚀 快速开始

```bash
dsh plugin --profile web add @vlln/plugin-console@0.1.0
```

## 📚 更多信息

**Installation**

**Option 1: git source, direct install (recommended, one line)** dsh plugin --profile web add "github:vlln/plugin-registry#path:/packages/plugin/console" Build artifacts are committed (git source skips the build); one command installs directly (~15 s). > **Windows note**: this uses the `#path:` form (no `&`) on purpose — on win32 `dsh plugin` forwards > args through cmd.exe, where `&` is a command

## 🔗 链接

- [GitHub 仓库](https://github.com/vlln/plugin-registry)
- [完整 README](https://github.com/vlln/plugin-registry#readme)
- [返回plugin-registry所在分类](../awesome-lists.md)
