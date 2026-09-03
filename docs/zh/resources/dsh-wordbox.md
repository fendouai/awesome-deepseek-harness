---
title: "dsh-wordbox"
description: "输入框旁常用词箱：全局/项目词桶，一键插入。"
keywords: "dsh-wordbox, input-editing, plugin, ui, deepseek harness, dsh"
---
# dsh-wordbox

> ⭐ **4** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 输入与编辑 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [arcmosin](https://github.com/arcmosin) | 更新时间 | 2026-08-14 |

## 一句话介绍

> 输入框旁常用词箱：全局/项目词桶，一键插入。

## 详细介绍

[English](README.en.md) | 中文 DeepSeek Harness（`dsh web`）的 **Web 客户端插件**：在对话输入框右侧放一个「词」按钮，点击弹出一个**常驻**的上拉面板，管理自己的常用词/句，一键插入对话输入框。 词条分两个桶：**全局**（所有工作区共享）与**当前项目**（按工作区目录隔离）。

## ✨ 核心特性

- 🖱️ 点击「词」按钮 → 上拉面板（带滑入动画），**常驻不消失**（再点一次 / 点击外部 / Esc 关闭）
- 🔀 三档显示范围：**全部 / 全局 / 当前**（切换控件在「＋ 添加」同行最右侧）
- ⏎ 点击词条 → **追加进输入框**（保留焦点、一个撤销步、面板不关闭，可连续插入）
- 🌐 中/英双语（跟随 DSH 界面语言）

## 📦 安装

```bash
# 前提，安装官方 CLI（已装可跳过）
npm install -g @deepseek-ai/dsh

# 安装本插件
# 方式一：从 npm 安装（推荐，已发布到 npm）
dsh plugin --profile web add dsh-wordbox

# 方式二：从 GitHub 安装（仓库根即插件包，无构建步骤，直接可用）
dsh plugin --profile web add github:arcmosin/dsh-wordbox

# 方式三：本地开发（link 到本仓库）
dsh plugin --profile web add link:D:/path/to/dsh-wordbox
```

## 🚀 快速开始

```bash
dsh plugin --profile web remove dsh-wordbox
```

## 📚 更多信息

**安装**

前置：DeepSeek Harness `dsh web` + `pnpm`（`dsh plugin` 命令会转发给 pnpm，需要它在 PATH 上）。 本插件是标准的 **DSH bundle 插件**（`dsh.bundle.patch` 声明，包内自带插件行 patch），因此安装/卸载都是**一条命令**：

**使用**

1. 点击输入框右侧的「词」按钮（英文界面显示 **W**），面板上拉并保持打开； 2. 底部右侧切换 全部 / 全局 / 当前； 3. 点击词条 → 追加进输入框（可连续点多条）；悬停行尾出现 × 删除； 4. 「当前」模式下悬停行尾出现"添加到全局"转化按钮，一键复制进全局； 5. 长词悬停会慢速流动显示完整内容。

## 🔗 链接

- [GitHub 仓库](https://github.com/arcmosin/dsh-wordbox)
- [完整 README](https://github.com/arcmosin/dsh-wordbox#readme)
- [返回dsh-wordbox所在分类](../plugins.md)
