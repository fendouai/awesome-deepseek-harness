---
title: "dsh-black-whale"
description: "DeepSeek Harness 黑鲸实验室主题：官网黑鲸 × 夕小瑶 IP，真实 profile 可安装的 Web UI 插件"
keywords: "dsh-black-whale, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-black-whale

> ⭐ **4** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [147228](https://github.com/147228) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, ui |

## One-liner

> DeepSeek Harness 黑鲸实验室主题：官网黑鲸 × 夕小瑶 IP，真实 profile 可安装的 Web UI 插件

## About

Black Whale Lab 是一个真实的 DeepSeek Harness Web 客户端插件。它通过 DSH 的 profile 与 Cordis 插件加载器进入官方 Web 应用，保留原生会话、模型、工具、沙箱、权限和设置能力，只接管浏览器表现层。 - **背景透传**：处理 DSH 嵌套的两层基础画布，让鲸鱼与小瑶真正进入主工作区。 - **局部承载**：侧栏、输入卡、菜单和弹窗仍保持可靠底色，文字不会落进复杂背景。 - **自动对比度保护**：运行时识别“浅底＋浅字”控件并自动切换深色文字，不依赖易变化的 CSS 哈希类名。 - **专注模式**：右上角一键压暗画布，适合长对话、代码和日志阅读。 - **完整回滚**：卸载时恢复标题、背景、DOM 与样式作用域，不污染 Harness 本身。 - **本地优先**：不读取会话，不发送提示词，不调用模型，不上传任何数据。

## ✨ Key Features

- **背景透传**：处理 DSH 嵌套的两层基础画布，让鲸鱼与小瑶真正进入主工作区。
- **局部承载**：侧栏、输入卡、菜单和弹窗仍保持可靠底色，文字不会落进复杂背景。
- **自动对比度保护**：运行时识别“浅底＋浅字”控件并自动切换深色文字，不依赖易变化的 CSS 哈希类名。
- **专注模式**：右上角一键压暗画布，适合长对话、代码和日志阅读。
- **完整回滚**：卸载时恢复标题、背景、DOM 与样式作用域，不污染 Harness 本身。
- **本地优先**：不读取会话，不发送提示词，不调用模型，不上传任何数据。

## 📦 Install

```bash
dsh plugin --profile web add \
  https://github.com/147228/dsh-black-whale/releases/download/v0.1.3/xiaoyao-ai-dsh-client-ui-skin-black-whale-0.1.3.tgz
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add github:147228/dsh-black-whale#v0.1.3
```

## 📚 Learn more

**安装**

要求：可正常运行的 DeepSeek Harness Web profile。当前版本在 DSH `0.1.0-rc.6`、Node.js 24 上完成真实验收。

**从 GitHub Release 安装（推荐）**

dsh plugin --profile web add \ https://github.com/147228/dsh-black-whale/releases/download/v0.1.3/xiaoyao-ai-dsh-client-ui-skin-black-whale-0.1.3.tgz 也可以直接安装固定 Git tag： dsh plugin --profile web add github:147228/dsh-black-whale#v0.1.3 安装后重启： dsh web > 全局皮肤会覆盖同一批主题变量。若已经安装其他 DSH 全局皮肤，请先移除旧皮肤，再安装 Black Whale Lab。

## 🔗 Links

- [GitHub Repository](https://github.com/147228/dsh-black-whale)
- [Full README](https://github.com/147228/dsh-black-whale#readme)
- [Back to the Plugins list](../plugins.md)
