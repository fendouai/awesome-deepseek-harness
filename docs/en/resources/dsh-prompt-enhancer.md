---
title: "dsh-prompt-enhancer"
description: "DeepSeek Harness DSH 提示词增强插件：✨ 一键优化草稿，增强提示词。"
keywords: "dsh-prompt-enhancer, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-prompt-enhancer

> ⭐ **39** · ✅ active · plugin · ⬆️ +5 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 39 | Status | ✅ active |
| Author | [Fishsb](https://github.com/Fishsb) | Updated | 2026-08-21 |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> DeepSeek Harness DSH 提示词增强插件：✨ 一键优化草稿，增强提示词。

## About

DeepSeek Harness (DSH) 插件。**两大核心能力**： - ✨ **提示词增强** — 输入框草稿一键改写，不满意可撤回 - 💬 **语音识别** — 说完自动停，云端 / 本地双引擎离线可用，识别结果填入草稿 另附 🔁 **DSH 服务异常一键重启**（网页打不开也能命令行恢复）。

## ✨ Key Features

- ✨ **提示词增强** — 输入框草稿一键改写，不满意可撤回
- 💬 **语音识别** — 说完自动停，云端 / 本地双引擎离线可用，识别结果填入草稿

## 📦 Install

```bash
dsh plugin --profile web add github:Fishsb/dsh-prompt-enhancer#v3.3.3
```

## 🚀 Quick Start

```bash
dsh plugin --profile web update dsh-prompt-enhancer
dsh plugin --profile web remove dsh-prompt-enhancer
```

## 📚 Learn more

**🚀 安装**

dsh plugin --profile web add github:Fishsb/dsh-prompt-enhancer#v3.3.3 安装后重启 DSH（`dsh web`），输入框工具行出现 ✨ 按钮即安装成功。 > 需本机已装 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 且 `pnpm` 在 PATH 中。 > > **客户端兼容性（语音识别）**：🎤 语音输入依赖客户端注入 `inputActions.setDraft`（官方 web client 已满足）；第三方客户端若实现同一契约即可加载，能力集不同时语音输入自动**降级**（无插入能力 → 识别结果追加到草稿末尾；完全不注入 → 🎤 禁用并提示）。**本地离线引擎为「框架 + 可选下载」模式**：插件安装**不携带/不默认下载模型

**📦 库说明**

核心逻辑拆分为独立 Node 模块，可复用：`lib/shortcut-win.cjs`（Windows 快捷方式生成）、`lib/updater-host.cjs`（CLI 重启 / 更新执行器）、`lib/platform-service.cjs`（跨平台服务管理）、`lib/sys.cjs`（环境与路径）。详见各模块头注释。

**🎯 使用（提示词增强）**

1. 输入任意非空文本（斜杠命令保留前缀，只优化正文） 2. 点击 **✨** 按钮 3. 等待独立 LLM 调用完成，草稿被替换为增强版本 4. 不满意点击 **可撤回** 恢复原文

## 🔗 Links

- [GitHub Repository](https://github.com/Fishsb/dsh-prompt-enhancer)
- [Full README](https://github.com/Fishsb/dsh-prompt-enhancer#readme)
- [Back to the Plugins list](../plugins.md)
