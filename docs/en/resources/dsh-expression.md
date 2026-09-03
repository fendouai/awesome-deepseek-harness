---
title: "dsh-expression"
description: "DeepSeek Harness 的表情包插件——找得到、发得出、学得会"
keywords: "dsh-expression, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-expression

> ⭐ **36** · ✅ active · plugin · ⬆️ +6 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 36 | Status | ✅ active |
| Author | [yyh-001](https://github.com/yyh-001) | Updated | 2026-08-20 |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> DeepSeek Harness 的表情包插件——找得到、发得出、学得会

## About

已发布到 **npm**（`dsh-meme`），一行装进任意 DSH profile（如 `~/.dsh/profiles/web/`）： dsh plugin --profile web add dsh-meme

## ✨ Key Features

- **纯文本也能斗图**：界面显示表情图片，模型收到的是 `[表情: 描述]`，无需图片输入能力
- **AI 自动学图**：用户说「入库」时，`learn_meme` 收录最近一张用户附件（不必填附件 id），自动识别分类/描述
- **情绪主动发图**：先选情绪桶，系统随机抽若干张 caption，模型挑一张贴进回复
- **像 QQ/微信 一样发图**：输入框 😊 悬浮面板点选表情直接发出
- **零第三方依赖**：仅 node:sqlite，装完即用

## 📦 Install

```bash
dsh plugin --profile web add dsh-meme
# 等价于:
pnpm add dsh-meme
```

## 🚀 Quick Start

```bash
pnpm add github:yyh-001/dsh-meme   # 或
pnpm add file:/path/to/dsh-meme
```

## 📚 Learn more

**安装**

已发布到 **npm**（`dsh-meme`），一行装进任意 DSH profile（如 `~/.dsh/profiles/web/`）： dsh plugin --profile web add dsh-meme

**配置**

默认内置两套图库：`official-001`（官方表情包 1 号，92 张）和 `dafeiyu-001`（大肥鱼，49 张），开箱用官方包，**无需任何配置**。 设置页「当前图库」下拉即可切换。插件会扫描内置 `memes/*` 以及「扫描目录」（默认 `~/.dsh/meme-packs`）下带 `index.db` 的子文件夹。导入 ZIP 也会放进扫描目录并立刻切过去。设置存在 `~/.dsh/dsh-expression.json`，升级插件不丢。

## 🔗 Links

- [GitHub Repository](https://github.com/yyh-001/dsh-expression)
- [Full README](https://github.com/yyh-001/dsh-expression#readme)
- [Back to the Plugins list](../plugins.md)
