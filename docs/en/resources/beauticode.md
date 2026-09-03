---
title: "beauticode"
description: "面向 AI 编程客户端的动态、可响应环境——视频背景、氛围场景与主题，适用于 DeepSeek Harness 与 Codex Desktop。"
keywords: "beauticode, desktop, client, coding, deepseek harness, dsh"
---
# beauticode

> ⭐ **51** · ✅ active · client · ⬆️ +10 recently

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 51 | Status | ✅ active |
| Author | [starsstreaming](https://github.com/starsstreaming) | Updated | 2026-08-20 |

## One-liner

> 面向 AI 编程客户端的动态、可响应环境——视频背景、氛围场景与主题，适用于 DeepSeek Harness 与 Codex Desktop。

## About

beautiCode 是一个本地背景工具，**主要面向 DeepSeek Harness和Codex**。 它不包含、不安装、也不启动 DSH。请先自行安装 DeepSeek Harness 并运行 `dsh web`。插件装好后，DSH 侧栏「设置」上方会出现「背景」，不必再开托盘。Codex Desktop 仍走 beautiCode 托盘。可以把电脑里的： * 图片 * 动态壁纸 * MP4 视频 * 番剧 直接设成 DeepSeek Harness 网页背后的背景。 它不会把工作窗口变成一个播放器，而是让画面安静地待在对话和工作区后面。 代码、输入框和按钮仍然可以正常使用。

## ✨ Key Features

- 图片
- 动态壁纸
- MP4 视频
- 番剧

## 📦 Install

```bash
npx @deepseek-ai/dsh plugin --profile web add beauticode-dsh
npx @deepseek-ai/dsh web
```

## 🚀 Quick Start

```bash
npx beauticode-dsh --remove
```

## 📚 Learn more

**一键安装插件（推荐）**

只要给 DeepSeek Harness 加背景，装插件即可，不必 fork 仓库、不必下 Windows 安装包，也不必开托盘。请先自己装好 DSH 和 Node.js。 npx beauticode-dsh `npx beauticode-dsh` 会从 npm 下载插件并写入你的 DSH profile，**不需要 pnpm，也不需要再执行 `dsh plugin add`**。已把 `dsh` 装到 PATH 时，第二行也可以写成 `dsh web`。 打开网页后，侧栏「设置」上方有「背景」：可从文件夹选图片或 MP4、清除、开关声音、切换已保存主题。已保存主题里自带「画窗」。网页控制台没有摸鱼。外观浅色/深色仍用 DSH 自己的设置。下次启动会恢复上次背景。 也可以用 `/bg`、`/bg-theme`、`/bg-clear`，或直接跟 AI 说把本机图片/视频设成背景。 已有 

**Windows 安装包**

需要 Codex Desktop、系统托盘或懒得留源码时，再下 [Windows 安装包](https://github.com/starsstreaming/beautiCode/releases/latest)。 然后自己启动： dsh web

## 🔗 Links

- [GitHub Repository](https://github.com/starsstreaming/beautiCode)
- [Full README](https://github.com/starsstreaming/beautiCode#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
