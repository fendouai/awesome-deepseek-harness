---
title: "Deepseek-Harness-Desktop (ChisaAlter)"
description: "Electron desktop shell with theme and background-image customization."
keywords: "Deepseek-Harness-Desktop (ChisaAlter), desktop, client, ui, deepseek harness, dsh"
---
# Deepseek-Harness-Desktop (ChisaAlter)

> ⭐ **131** · ✅ active · client · ⬆️ +5 recently

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 131 | Status | ✅ active |
| Author | [ChisaAlter](https://github.com/ChisaAlter) | Updated | 2026-08-21 |

## One-liner

> Electron desktop shell with theme and background-image customization.

## About

到 [Releases](https://github.com/ChisaAlter/Deepseek-Harness-Desktop/releases/latest) 下载，装完不需要本机 Node。当前正式版是 **[0.2.7](https://github.com/ChisaAlter/Deepseek-Harness-Desktop/releases/tag/v0.2.7)**。 macOS 安装包未签名：下载后右键打开，或执行 `xattr -cr /Applications/Deepseek-Harness-Desktop.app`。校验见同页 `SHA512SUMS.txt`。 装完打开即是启动器，一般会自动进桌面；若桌面还没有会话、本机已有官方 `~/.dsh` 数据，会先停在导入。进主界面后选工作区，在设置里填 API 密钥即可对话。

## ✨ Key Features

- **官方界面** — 对话、工具调用、审批就是 `dsh web`，没有另做一套聊天页。
- **启动器** — 冷启动先开启动器（更新询问、导入、版本、插件问诊）；托盘可随时再打开。
- **Git** — 标题栏切分支、提交、推送、开变更请求。
- **远程** — 侧栏底部打开远程，扫码用手机浏览器接同一会话（默认关）。
- **文件与终端** — `Ctrl+\` 打开右栏（Files / Diff / Browser / Agents）；`` Ctrl+` `` 打开底栏终端，选区可送进对话。
- **模型** — 第三方思考强度、识图兜底；最新一条用户消息可改完再发。
- **外观** — 浅色 / 深色主题。壁纸在外观里选或点「浏览」打开图库（分类、搜索、收藏，确认后按窗口比例裁切）；毛玻璃和像素化也在外观里调。
- **扩展** — 设置里管理 MCP、技能和插件。市场是桌面自有的设置分区（内置精选目录与安装引擎，源自 [dsh-market](https://github.com/dsh-market/dsh-market) 的产品形态但已与上游分离），没有独立窗口。

## 📦 Install

```bash
git clone https://github.com/ChisaAlter/Deepseek-Harness-Desktop.git
cd Deepseek-Harness-Desktop
npm install
npm run setup:harness
npm start
```

## 🚀 Quick Start

```bash
npm test              # 桌面壳单测
npm run sync:harness -- --ref dsh-v0.1.2-alpha.4 --sha 4e84901e6471b79ec0338099867ebb4606d12bb5
npm run dist          # Windows 安装包
npm run dist:mac      # macOS 安装包（须在 macOS 上）
```

## 📚 Learn more

**安装**

到 [Releases](https://github.com/ChisaAlter/Deepseek-Harness-Desktop/releases/latest) 下载，装完不需要本机 Node。当前正式版是 **[0.2.7](https://github.com/ChisaAlter/Deepseek-Harness-Desktop/releases/tag/v0.2.7)**。 macOS 安装包未签名：下载后右键打开，或执行 `xattr -cr /Applications/Deepseek-Harness-Desktop.app`。校验见同页 `SHA512SUMS.txt`。 装完打开即是启动器，一般会自动进桌面；若桌面还没有会话、本机已有官方 `~/.dsh` 数据，会先停在导入。进主界面后选工作区，在设置里填 API 密钥即可对话。

## 🔗 Links

- [GitHub Repository](https://github.com/ChisaAlter/Deepseek-Harness-Desktop)
- [Full README](https://github.com/ChisaAlter/Deepseek-Harness-Desktop#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
