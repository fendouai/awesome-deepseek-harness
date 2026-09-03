---
title: "dsh-browser"
description: "Chrome sidebar extension that lets DSH operate your browser directly, no vision capabilities required."
keywords: "dsh-browser, browser, plugin, automation, deepseek harness, dsh"
---
# dsh-browser

> ⭐ **366** · ✅ active · plugin · ⬆️ +21 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Browser control |
| Stars | ⭐ 366 | Status | ✅ active |
| Author | [Lum1104](https://github.com/Lum1104) | Updated | 2026-08-21 |

## One-liner

> Chrome sidebar extension that lets DSH operate your browser directly, no vision capabilities required.

## About

Connect [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) to the Chrome or Firefox tab you are already using. The model can read page content, click controls, fill forms, scroll, and navigate while preserving your login state, session, and cookies. A side panel or sidebar provides the conversation UI. `dsh` is DeepSeek AI's open-source, plugin-based agent harness. This repository provides a companion browser bridge plugin and Chrome/Firefox MV3 extension as one standalone pnpm workspace. Browser operation remains text-only: pages become structured text with a numbered inventory of interactive elements, and the model addresses those elements by number. dsh 0.1.1 multimodal chat is separate from that page channel—the side panel accepts PNG, JPEG, WebP, and GIF attachments w

## 📦 Install

```bash
git clone https://github.com/Lum1104/dsh-browser.git
cd dsh-browser
./scripts/install.sh
```

## 🚀 Quick Start

```bash
pnpm install
pnpm --filter dsh-browser-extension run build:firefox
```

## 📚 Learn more

**Quick install**

The standard `dsh plugin` command alone cannot install this project. The integration contains both a dsh bridge plugin and a browser extension. The one-line installer currently sets up the Chrome build. macOS and Linux: curl -fsSL https://raw.githubusercontent.com/Lum1104/dsh-browser/refs/heads/main/scripts/install.sh | bash Windows, in PowerShell: $s="$env:TEMP\dsh-install.ps1"; irm https://raw.g

**Detailed installation and usage**

Requirements: Node.js `^22.19` or `>=24`, Corepack/pnpm, and Chrome 116+ or Firefox 140+. Windows additionally needs Windows PowerShell 5.1, which ships with Windows, or PowerShell 7+.

**Install or update**

For a managed installation, run: curl -fsSL https://raw.githubusercontent.com/Lum1104/dsh-browser/refs/heads/main/scripts/install.sh | bash or, on Windows: $s="$env:TEMP\dsh-install.ps1"; irm https://raw.githubusercontent.com/Lum1104/dsh-browser/refs/heads/main/scripts/install.ps1 -OutFile $s; powershell -NoProfile -ExecutionPolicy Bypass -File $s The installer downloads `main`, builds and registe

## 🔗 Links

- [GitHub Repository](https://github.com/Lum1104/dsh-browser)
- [Full README](https://github.com/Lum1104/dsh-browser#readme)
- [Back to the Plugins list](../plugins.md)
