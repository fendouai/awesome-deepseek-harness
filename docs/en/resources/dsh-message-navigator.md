---
title: "dsh-message-navigator"
description: "消息导航条 Message Navigator: DeepSeek Harness 网页聊天界面右侧的垂直消息索引(动态 Cordis 插件)"
keywords: "dsh-message-navigator, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-message-navigator

> ⭐ **2** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [TableRogue](https://github.com/TableRogue) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> 消息导航条 Message Navigator: DeepSeek Harness 网页聊天界面右侧的垂直消息索引(动态 Cordis 插件)

## About

[English](README.en.md) | 中文 为 DeepSeek Harness Web UI 提供 Codex 风格的会话消息导航器。

## ✨ Key Features

- 只为普通用户消息和用户插话生成刻度；AI 回答、思考、工具和状态内容不计入。
- 每次用户发言只对应一条刻度，所有普通刻度等长，并以约 20px 的紧凑间距集中排布。
- 自动加载完整历史记录，不受 DeepSeek Harness 默认只渲染最新历史页的限制。
- 深色长刻度跟随当前阅读位置。
- 悬停或键盘聚焦时显示消息预览。
- 点击刻度或问题预览卡片均可平滑跳转；支持方向键、Home、End 和 Enter。
- 自动处理流式生成、新消息、加载较早记录、内容重排和会话切换。
- 少量刻度使用 Codex 式紧凑固定间距；超长会话才统一压缩间距。

## 📦 Install

```bash
dsh plugin --profile web add dsh-codex-message-navigator
cd ~/.dsh/profiles/web
pnpm ls dsh-codex-message-navigator --depth 0
```

## 🚀 Quick Start

```bash
pnpm install
pnpm check
pnpm pack
```

## 📚 Learn more

**给安装 Agent 的提示**

如果你是 AI Agent、脚本助手或正在替用户安装本插件，请遵守以下规则： 推荐的验证命令： dsh plugin --profile web add dsh-codex-message-navigator cd ~/.dsh/profiles/web pnpm ls dsh-codex-message-navigator --depth 0 如果桌面版使用自定义 `DSH_HOME`，请在对应 profile 目录执行最后一条验证命令。

**安装**

推荐直接从 npm 安装： dsh plugin --profile web add dsh-codex-message-navigator dsh --profile web --dump-config dsh --profile web 也可以先打包为 tarball 安装，避免安装期构建授权： pnpm pack dsh plugin --profile web add ./dsh-codex-message-navigator-0.1.4.tgz 如果使用其他 profile，请把 `web` 替换成对应名称。卸载： dsh plugin --profile web remove dsh-codex-message-navigator 如果此前只使用不带 profile 的 `dsh web` 快捷命令，需要先创建一个可扩展的 Web profile： dsh plugin --p

**本地源码安装**

dsh plugin --profile web add /absolute/path/to/deepseek-message-navigator 源码安装会执行 `prepare`。pnpm 10 可能要求在 profile 的 `pnpm-workspace.yaml` 中允许该包构建： allowBuilds: dsh-message-navigator: true 允许后重新执行安装命令。

## 🔗 Links

- [GitHub Repository](https://github.com/TableRogue/dsh-message-navigator)
- [Full README](https://github.com/TableRogue/dsh-message-navigator#readme)
- [Back to the Plugins list](../plugins.md)
