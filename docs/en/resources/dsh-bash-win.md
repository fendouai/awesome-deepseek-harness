---
title: "dsh-bash-win"
description: "在 Windows 环境中为 DeepSeek Harness 提供 Git Bash 与 WSL 2 bash 工具,含 bwrap 沙箱、审批模式、后台任务"
keywords: "dsh-bash-win, vision, plugin, coding, git, deepseek harness, dsh"
---
# dsh-bash-win

> ⭐ **9** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 9 | Status | ✅ active |
| Author | [zimzaza4](https://github.com/zimzaza4) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding, git |

## One-liner

> 在 Windows 环境中为 DeepSeek Harness 提供 Git Bash 与 WSL 2 bash 工具,含 bwrap 沙箱、审批模式、后台任务

## About

在 Windows 上为 DeepSeek Harness(DSH)提供 **Git Bash** 与 **WSL2** 两个 bash 工具的 Cordis 插件。

## ✨ Key Features

- DSH 在 Windows 上**禁用了官方 bash 工具**(只有 pwsh)

## 📦 Install

```bash
dsh plugin --profile web add @zimzaza4/dsh-bash-win
```

## 🚀 Quick Start

```bash
dsh plugin --profile web remove @zimzaza4/dsh-bash-win
```

## 📚 Learn more

**安装**

插件已发布到 npm。通过 DSH 官方 `dsh plugin` 命令安装进 **profile**(`dsh web` 对应 `web` profile)。

**从 npm 安装(推荐)**

dsh plugin --profile web add @zimzaza4/dsh-bash-win 装完**重启 `dsh web`** 生效。包内 `cordis.patch.yml`(经 `dsh.bundle.patch` 声明)自动挂载插件行，重启后即可在对话中使用 `git_bash` / `wsl_bash`。

## 🔗 Links

- [GitHub Repository](https://github.com/zimzaza4/dsh-bash-win)
- [Full README](https://github.com/zimzaza4/dsh-bash-win#readme)
- [Back to the Plugins list](../plugins.md)
