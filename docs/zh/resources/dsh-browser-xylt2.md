---
title: "dsh-browser"
description: "Chrome 侧栏扩展：让 DSH 直接操控你的浏览器，无需视觉能力。"
keywords: "dsh-browser, browser, plugin, automation, deepseek harness, dsh"
---
# dsh-browser

> ⭐ **366** · ✅ 活跃 · 插件 · 近期 ⬆️ +21

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 浏览器控制 |
| 星数 | ⭐ 366 | 状态 | ✅ 活跃 |
| 作者 | [Lum1104](https://github.com/Lum1104) | 更新时间 | 2026-08-21 |

## 一句话介绍

> Chrome 侧栏扩展：让 DSH 直接操控你的浏览器，无需视觉能力。

## 详细介绍

Connect [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) to the Chrome or Firefox tab you are already using. The model can read page content, click controls, fill forms, scroll, and navigate while preserving your login state, session, and cookies. A side panel or sidebar provides the conversation UI. `dsh` is DeepSeek AI's open-source, plugin-based agent harness. This repository provides a companion browser bridge plugin and Chrome/Firefox MV3 extension as one standalone pnpm workspace. Browser operation remains text-only: pages become structured text with a numbered inventory of interactive elements, and the model addresses those elements by number. dsh 0.1.1 multimodal chat is separate from that page channel—the side panel accepts PNG, JPEG, WebP, and GIF attachments w

## 📦 安装

```bash
git clone https://github.com/Lum1104/dsh-browser.git
cd dsh-browser
./scripts/install.sh
```

## 🚀 快速开始

```bash
pnpm install
pnpm --filter dsh-browser-extension run build:firefox
```

## 📚 更多信息

**Quick install**

The standard `dsh plugin` command alone cannot install this project. The integration contains both a dsh bridge plugin and a browser extension. The one-line installer currently sets up the Chrome build. macOS and Linux: curl -fsSL https://raw.githubusercontent.com/Lum1104/dsh-browser/refs/heads/main/scripts/install.sh | bash Windows, in PowerShell: $s="$env:TEMP\dsh-install.ps1"; irm https://raw.g

**Detailed installation and usage**

Requirements: Node.js `^22.19` or `>=24`, Corepack/pnpm, and Chrome 116+ or Firefox 140+. Windows additionally needs Windows PowerShell 5.1, which ships with Windows, or PowerShell 7+.

**Install or update**

For a managed installation, run: curl -fsSL https://raw.githubusercontent.com/Lum1104/dsh-browser/refs/heads/main/scripts/install.sh | bash or, on Windows: $s="$env:TEMP\dsh-install.ps1"; irm https://raw.githubusercontent.com/Lum1104/dsh-browser/refs/heads/main/scripts/install.ps1 -OutFile $s; powershell -NoProfile -ExecutionPolicy Bypass -File $s The installer downloads `main`, builds and registe

## 🔗 链接

- [GitHub 仓库](https://github.com/Lum1104/dsh-browser)
- [完整 README](https://github.com/Lum1104/dsh-browser#readme)
- [返回dsh-browser所在分类](../plugins.md)
