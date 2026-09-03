---
title: "dsh-side-panel"
description: "Compact side panel with a file browser, terminal and Git review."
keywords: "dsh-side-panel, ui, plugin, files, terminal, git, deepseek harness, dsh"
---
# dsh-side-panel

> ⭐ **16** · 💤 inactive · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 16 | Status | 💤 inactive |
| Author | [ccq1](https://github.com/ccq1) | Updated | 2026-08-14 |
| Subcategory | 🖥️ Sidebars & panels | Capabilities | ui, files, terminal, git |

## One-liner

> Compact side panel with a file browser, terminal and Git review.

## About

DSH Web 的右侧工作区面板，在当前会话旁集中提供 Git 审查、终端和文件操作。 可以点击dsh会话区弹出的文件链接，会自动打开相应的文件以供审阅。

## 📦 Install

```bash
dsh plugin --profile web add github:dsh-external/dsh-side-panel
dsh web
```

## 🚀 Quick Start

```bash
git clone git@github.com:dsh-external/dsh-side-panel.git
cd dsh-side-panel
npm install
npm run build
dsh plugin --profile web add .
```

## 📚 Learn more

**安装**

从 github-dsh-external仓库安装 dsh plugin --profile web add github:dsh-external/dsh-side-panel dsh web 或者可以先从git clone 到本地，然后从本地目录安装 git clone git@github.com:dsh-external/dsh-side-panel.git cd dsh-side-panel npm install npm run build dsh plugin --profile web add .

**配置**

组合包默认启用以下配置： - id: side-panel name: '@dsh-external/dsh-side-panel' config: maxTextBytes: 2097152 maxImageBytes: 10485760 searchMaxResults: 200

## 🔗 Links

- [GitHub Repository](https://github.com/ccq1/dsh-side-panel)
- [Full README](https://github.com/ccq1/dsh-side-panel#readme)
- [Back to the Plugins list](../plugins.md)
