---
title: "dsh-doctor"
description: "DSH 插件：flutter-doctor 风格诊断与修复（安装级 + harness 内检查，安全自动修复）。官方 repository-plugin（.dsh-plugin 格式）"
keywords: "dsh-doctor, discovery, plugin, coding, deepseek harness, dsh"
---
# dsh-doctor

> ⭐ **6** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 插件发现 |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [coppynight](https://github.com/coppynight) | 更新时间 | — |

## 一句话介绍

> DSH 插件：flutter-doctor 风格诊断与修复（安装级 + harness 内检查，安全自动修复）。官方 repository-plugin（.dsh-plugin 格式）

## 详细介绍

**Your dsh config has settings that silently stopped applying. This tells you which ones.** npx github:asdf17128/dsh-doctor One command, ten seconds, read-only. No config, no signup, no dependencies. ---

## ✨ 核心特性

- fallbackMaxBytes: 40 ← gone, silently
- maxTitleBytes: 80 ← gone, silently

## 📦 安装

```bash
dsh plugin --profile web add dsh-doctor
```

## 🚀 快速开始

```bash
Your harness: 130 entries, 103 active, 25 disabled, 2 conditional

  Web UI                  32
  Tools                   18  (16 off)
  Sessions & history      11
  Agent loop               5  (1 off)
  ...

Conditional (2) — enablement is decided at mount time, not here
  bash-sandbox             !!js process.platform === 'win32'
  pwsh-sandbox             !!js process.platform !== 'win32'
```

## 📚 更多信息

**Why your setting isn't taking effect**

Two dsh behaviours boot cleanly with exit code 0, so nothing tells you: **A patch replaces an entry's whole `config`.** You change one field; every sibling field you did not restate disappears from the tree that boots. The plugin then runs on defaults you never chose. config: fallbackMaxWords: 12 **A typo in an entry id is inert.** Write `agent-defualt-model` and dsh prints one stderr line, then b

**Usage**

npx dsh-doctor # check the web profile npx dsh-doctor --explain # describe the tree instead of checking it npx dsh-doctor --profile headless # another profile npx dsh-doctor --verbose # include informational notes npx dsh-doctor --json # machine-readable npx dsh-doctor --fix # restate the dropped fields for you npx dsh-doctor --offline # skip npm registry lookups npx dsh-doctor --quiet # print onl

**Install and uninstall**

As a CLI, nothing to install — `npx dsh-doctor` runs it. As a plugin: dsh plugin --profile web add github:asdf17128/dsh-doctor # install dsh plugin --profile web remove dsh-doctor # uninstall Removing it drops the `config_doctor` tool and leaves nothing behind: the plugin never writes to your Harness home.

## 🔗 链接

- [GitHub 仓库](https://github.com/coppynight/dsh-doctor)
- [完整 README](https://github.com/coppynight/dsh-doctor#readme)
- [返回dsh-doctor所在分类](../plugins.md)
