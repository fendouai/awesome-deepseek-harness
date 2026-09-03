---
title: "dsh-sidechain"
description: "Side sessions: persistent /side sessions (Codex style) and one-off /btw questions (Claude style) in temporary forks."
keywords: "dsh-sidechain, multi-agent, agent, context, deepseek harness, dsh"
---
# dsh-sidechain

> ⭐ **10** · ✅ active · agent · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | agent | Category | Multi-agent |
| Stars | ⭐ 10 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | 2026-08-21 |

## One-liner

> Side sessions: persistent /side sessions (Codex style) and one-off /btw questions (Claude style) in temporary forks.

## About

DSH 侧会话插件。它通过 fork 当前会话创建隔离子会话，让用户在不中断主线程的情况下发起一次性问题或持续对话。 当前版本适配公开版 DSH npm `0.0.1-rc.5`、`0.1.0-rc.6`、`0.1.0-rc.7`、`0.1.0-rc.8`、`0.1.1-rc.1` 和 `0.1.1-rc.2`。在已验证的 `0.1.1-rc.2` 中，`/side` 与 `/btw` 会转发命令输入中的图片附件，并在侧栏显示持久化图片。 侧会话继承主会话已经完成的回合作为参考上下文，但拥有独立的消息记录和执行过程。侧会话的提示、思考、工具调用和回答不会进入主会话的模型上下文。

## ✨ Key Features

- `/btw` 在后台完成单轮问答，主会话可以继续使用。
- `/side` 创建可续聊线程，可直接在侧栏中发送后续消息。
- 右侧面板显示用户消息、上下文、思考、工具调用与回答。
- 运行中的会话实时更新，并在列表中显示活动摘要。
- 子会话历史持久化，重启 DSH 后仍可查看。
- 面板支持拖拽调宽、展开、手动刷新和 `Ctrl/Cmd+Shift+E` 快捷开关。

## 📦 Install

```bash
dsh plugin --profile web add github:omdsh-dev/dsh-sidechain
```

## 🚀 Quick Start

```bash
- insert:
    - id: dsh-sidechain
      name: '@dsh-external/dsh-sidechain'
```

## 📚 Learn more

**安装与卸载**

依赖 DSH 提供的 `@deepseek-ai/dsh-subagent`、`@deepseek-ai/dsh-subagent-fork-in-process` 和 `@deepseek-ai/dsh-commands`。默认 Web profile 已包含这些依赖。

**安装**

dsh plugin --profile web add github:omdsh-dev/dsh-sidechain pnpm 10 及以上首次安装会提示允许 Git 依赖执行 `prepare`。按命令输出把插件键加入 Web profile 的 `pnpm-workspace.yaml`，然后重新执行安装命令。 插件会向 Web profile 添加以下配置： - id: dsh-sidechain name: '@dsh-external/dsh-sidechain' 安装或更新插件代码后，重启 `dsh web` 并刷新页面。

**配置**

配置示例： - id: dsh-sidechain name: '@dsh-external/dsh-sidechain' config: providerName: fork readOnlyTools: - read - grep - glob

**使用**

一次性侧问： /btw 这个目录下哪个文件最大？ 命令立即返回，侧链面板自动打开并显示执行过程和答案。`/btw` 只运行一轮，不能继续追问。 持续侧会话： /side 分析一下当前插件的事件流 侧链面板会打开新线程。在线程底部输入消息并按 Enter，即可继续对话。 查看子代理列表： /side list `/side` 和 `/btw` 都必须提供问题。

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-sidechain)
- [Full README](https://github.com/omdsh-dev/dsh-sidechain#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
