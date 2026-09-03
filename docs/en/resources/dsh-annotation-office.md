---
title: "dsh-plugin-better-sidebar-plugin-office"
description: "Office-suite preview (.docx/.xlsx/.pptx) for the Better Sidebar, as a standalone slim bundle."
keywords: "dsh-plugin-better-sidebar-plugin-office, developer, plugin, files, ui, deepseek harness, dsh"
---
# dsh-plugin-better-sidebar-plugin-office

> ⭐ **23** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 23 | Status | ✅ active |
| Author | [HuanLinOTO](https://github.com/HuanLinOTO) | Updated | 2026-08-15 |
| Subcategory | 🧪 Code, tests & review | Capabilities | files, ui |

## One-liner

> Office-suite preview (.docx/.xlsx/.pptx) for the Better Sidebar, as a standalone slim bundle.

## About

DSH web 插件：为 better-sidebar 的编辑器提供 Office 三件套文件预览（`.docx` / `.xlsx` / `.pptx`）。

## ✨ Key Features

- 通过 `ctx.betterSidebar.registerFileViewer` 注册 3 个 viewer（id 与内置一致）：
- viewer 描述符形状与原内置完全一致（`mediaUrl` 策略、priority 0、title/icon），因此：
- 客户端组件自包含：自带 locale（中/英）与 CSS，不依赖 better-sidebar 的 client 内部实现

## 📦 Install

```bash
pnpm install
pnpm run typecheck   # 类型门禁（需先构建 DSH-better-sidebar 的 lib/types）
pnpm test            # vitest（xlsx→Univer 转换 + 注册描述符）
pnpm run build       # tsdown 双产物（lib/index.js + lib/client.js）
```

## 🚀 Quick Start

```bash
# 从 npm 安装（推荐）：
dsh plugin --profile web add @huanlin/dsh-plugin-better-sidebar-plugin-office

# 本地开发（link: 热更新）
dsh plugin --profile web add "link:D:/Projects/deepseek-harness/dsh-better-sidebar-plugin-office"
```

## 🔗 Links

- [GitHub Repository](https://github.com/HuanLinOTO/dsh-plugin-better-sidebar-plugin-office)
- [Full README](https://github.com/HuanLinOTO/dsh-plugin-better-sidebar-plugin-office#readme)
- [Back to the Plugins list](../plugins.md)
