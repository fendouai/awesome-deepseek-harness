---
title: "dsh-plugin-better-sidebar-plugin-office"
description: "为 better-sidebar 提供 Office 三件套预览（.docx/.xlsx/.pptx），独立瘦身 bundle。"
keywords: "dsh-plugin-better-sidebar-plugin-office, developer, plugin, files, ui, deepseek harness, dsh"
---
# dsh-plugin-better-sidebar-plugin-office

> ⭐ **23** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 23 | 状态 | ✅ 活跃 |
| 作者 | [HuanLinOTO](https://github.com/HuanLinOTO) | 更新时间 | 2026-08-15 |
| 子分类 | 🧪 代码·测试·审查 | 能力 | files, ui |

## 一句话介绍

> 为 better-sidebar 提供 Office 三件套预览（.docx/.xlsx/.pptx），独立瘦身 bundle。

## 详细介绍

DSH web 插件：为 better-sidebar 的编辑器提供 Office 三件套文件预览（`.docx` / `.xlsx` / `.pptx`）。

## ✨ 核心特性

- 通过 `ctx.betterSidebar.registerFileViewer` 注册 3 个 viewer（id 与内置一致）：
- viewer 描述符形状与原内置完全一致（`mediaUrl` 策略、priority 0、title/icon），因此：
- 客户端组件自包含：自带 locale（中/英）与 CSS，不依赖 better-sidebar 的 client 内部实现

## 📦 安装

```bash
pnpm install
pnpm run typecheck   # 类型门禁（需先构建 DSH-better-sidebar 的 lib/types）
pnpm test            # vitest（xlsx→Univer 转换 + 注册描述符）
pnpm run build       # tsdown 双产物（lib/index.js + lib/client.js）
```

## 🚀 快速开始

```bash
# 从 npm 安装（推荐）：
dsh plugin --profile web add @huanlin/dsh-plugin-better-sidebar-plugin-office

# 本地开发（link: 热更新）
dsh plugin --profile web add "link:D:/Projects/deepseek-harness/dsh-better-sidebar-plugin-office"
```

## 🔗 链接

- [GitHub 仓库](https://github.com/HuanLinOTO/dsh-plugin-better-sidebar-plugin-office)
- [完整 README](https://github.com/HuanLinOTO/dsh-plugin-better-sidebar-plugin-office#readme)
- [返回dsh-plugin-better-sidebar-plugin-office所在分类](../plugins.md)
