---
title: "dsh-desktop"
description: "An independent, open-source desktop wrapper for DeepSeek Harness. It starts the bundled @deepseek-ai/dsh Web UI locally and loads it in a hardened Electron window on Linux, macOS, and Windows."
keywords: "dsh-desktop, desktop, client, coding, ui, deepseek harness, dsh"
---
# dsh-desktop

> ⭐ **30** · ✅ active · client

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 30 | Status | ✅ active |
| Author | [liguobao](https://github.com/liguobao) | Updated | — |

## One-liner

> An independent, open-source desktop wrapper for DeepSeek Harness. It starts the bundled @deepseek-ai/dsh Web UI locally and loads it in a hardened Electron window on Linux, macOS, and Windows.

## About

[English](README.en.md) | 中文 DeepSeek Harness 的**桌面安装版**——下载安装即用，无需安装 Node.js、无需使用 npm、无需打开终端。安装后打开应用，在界面里填入你的 DeepSeek API Key，就能开始让 AI 帮你跑任务（读写文件、执行命令、写代码、自动化操作等）。 如果你在找「DeepSeek 桌面版」「DeepSeek 客户端下载」「DeepSeek Agent 电脑版」，这就是为你准备的。支持 macOS（Apple Silicon）和 Windows，安装包见下方 Releases。 📖 **文档站**：[foolgry.github.io/dsh-desktop/zh](https://foolgry.github.io/dsh-desktop/zh/) —— 遇到问题或有建议？欢迎到 [Issues](https://github.com/foolgry/dsh-desktop/issues) 反馈。

## ✨ Key Features

- **macOS（Apple Silicon / M 系列芯片）**：推荐用 Homebrew 安装，一条命令搞定（`xattr -cr` 清除未公证应用的隔离属性，避免「已损坏」提示；后续还能在 App 内一键更新，见下）：
- **Windows（64 位）**：下载 `DSH-Desktop-*-win-x64-setup.exe`
- **Windows**：后台自动下载，弹窗点「Restart and update」即重启完成更新；不点也会在下次退出应用时自动安装
- **macOS**（未签名，无法自我更新）：弹窗提示更新。如果是用 Homebrew 安装的，点「Update via Homebrew」会自动执行 `brew upgrade --cask dsh-desktop` + `xattr -cr` 并重启完成更新；否则点按钮跳转到 Releases 页手动下载

## 📦 Install

```bash
brew install --cask foolgry/tap/dsh-desktop && xattr -cr "/Applications/DSH Desktop.app"
```

## 🚀 Quick Start

```bash
curl -L -o "$(brew --cache --cask foolgry/tap/dsh-desktop)" \
  "https://ghfast.top/https://github.com/foolgry/dsh-desktop/releases/download/<tag>/DSH-Desktop-<版本>-mac-arm64.dmg"
brew install --cask foolgry/tap/dsh-desktop && xattr -cr "/Applications/DSH Desktop.app"
```

## 📚 Learn more

**下载安装**

到 [Releases](https://github.com/foolgry/dsh-desktop/releases) 页面下载最新版本： ```sh brew install --cask foolgry/tap/dsh-desktop && xattr -cr "/Applications/DSH Desktop.app" ``` 也可以下载 `DSH-Desktop-*-mac-arm64.dmg` 手动安装：未签名，首次打开如果提示"无法验证开发者"，**右键点应用 → 打开**；若提示「已损坏」，在终端执行一次上面的 `xattr` 命令即可。 - SmartScreen 会提示风险：点 **更多信息 → 仍要运行** 每个 Release 附带 `SHA256SUMS` 校验清单，可用于验证安装包完整性。 <details> <summary><strong>下载慢或无法访

**使用**

1. 安装后打开 **DSH Desktop** 2. 在界面的设置里填入你的 [DeepSeek API Key](https://platform.deepseek.com/)（和网页版操作一样） 3. 开始对话，让 AI 帮你完成任务 你的数据（对话、配置、会话）存在系统应用数据目录，不会污染你的用户目录。日志在同目录的 `logs/dsh.log`，日志和数据目录都可以从托盘菜单直接打开。

## 🔗 Links

- [GitHub Repository](https://github.com/liguobao/dsh-desktop)
- [Full README](https://github.com/liguobao/dsh-desktop#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
