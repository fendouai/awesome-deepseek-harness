---
title: "dsh-message-preview"
description: "Right-side user-message navigator for the DeepSeek Harness Web UI."
keywords: "dsh-message-preview, ide, integration, coding, ui, deepseek harness, dsh"
---
# dsh-message-preview

> ⭐ **7** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | IDE & editors |
| Stars | ⭐ 7 | Status | ✅ active |
| Author | [asukasec](https://github.com/asukasec) | Updated | — |

## One-liner

> Right-side user-message navigator for the DeepSeek Harness Web UI.

## About

DeepSeek Harness Web UI 的右侧消息导航条。它为当前会话中的每条用户消息生成一个导航块，可悬停预览、显示当前阅读位置，并点击跳转到对应消息。

## ✨ Key Features

- 只索引用户直接发送的消息，排除工具通知、后台任务和注入上下文。
- 当前阅读位置随会话滚动自动高亮。
- 悬停显示消息序号、相对时间和文本预览。
- 点击后自动加载较早的会话历史，平滑滚动并高亮目标消息。
- 导航块会根据消息数量和文本长度自适应排布；少于两条用户消息时自动隐藏。
- 默认仅显示当前位置指示，鼠标靠近会话右侧时展开完整导航条。
- 中英文界面文案随 DSH locale 自动切换。

## 📦 Install

```bash
dsh plugin --profile web add "github:asukasec/dsh-message-preview#main"
```

## 🚀 Quick Start

```bash
dsh web
```

## 📚 Learn more

**安装**

要求： 从 GitHub 安装： dsh plugin --profile web add "github:asukasec/dsh-message-preview#main" 安装完成后完整重启 Web UI： dsh web 也可以克隆仓库后从本地目录安装： git clone https://github.com/asukasec/dsh-message-preview.git cd dsh-message-preview dsh plugin --profile web add . Windows 用户还可以在克隆后的目录中双击 `install.cmd`。该脚本会定位 `DSH_HOME`、复制插件，并以幂等方式更新指定 profile 的 `cordis.patch.yml`： .\install.ps1 -Profile web -DshHome "D:\path\to\ds

**工作原理**

插件由宿主端和浏览器端两部分组成： 数据按以下优先级获取： 1. 宿主端 `dshMessagePreview` 投影，提供完整且轻量的消息索引。 2. 当前已加载的会话节点，用于首屏回退。 3. 投影尚未就绪时，通过 `loadOlder()` 补载更早的历史。 插件不会向第三方服务发送请求，也不会修改会话内容。消息预览只在本地 DSH 进程和浏览器之间传递，宿主端预览最多保留 80 个字符。

## 🔗 Links

- [GitHub Repository](https://github.com/asukasec/dsh-message-preview)
- [Full README](https://github.com/asukasec/dsh-message-preview#readme)
- [Back to the MCP & Integrations list](../integrations.md)
