---
title: "dsh-side-chat"
description: "一个 DSH 网页插件，Codex 式侧边聊天的强化版本： 在右侧面板提供按主会话隔离的独立聊天，具备 Codex 式的智能体能力——继承主会话的 工具集、模型、思考难度与权限预设，能感知所在工作目录；选中对话内容即可提问，AI 回复 也能带回主会话（直接带回或摘要后带回，写入草稿或注入为折叠提示行）。  在 Codex 式能力之上，它额外支持：当主会话的智能体弹出问题弹框向你提问时，可以 把问题与各个选项带入侧边聊天、让 AI 帮你分析，不必打断当前流程——想清楚后把答案 带回，再回答弹框即可。"
keywords: "dsh-side-chat, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-side-chat

> ⭐ **12** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 12 | Status | ✅ active |
| Author | [heartmove](https://github.com/heartmove) | Updated | — |
| Subcategory | 🧰 Toolkits | Capabilities | coding |

## One-liner

> 一个 DSH 网页插件，Codex 式侧边聊天的强化版本： 在右侧面板提供按主会话隔离的独立聊天，具备 Codex 式的智能体能力——继承主会话的 工具集、模型、思考难度与权限预设，能感知所在工作目录；选中对话内容即可提问，AI 回复 也能带回主会话（直接带回或摘要后带回，写入草稿或注入为折叠提示行）。  在 Codex 式能力之上，它额外支持：当主会话的智能体弹出问题弹框向你提问时，可以 把问题与各个选项带入侧边聊天、让 AI 帮你分析，不必打断当前流程——想清楚后把答案 带回，再回答弹框即可。

## About

An **enhanced version of a Codex-style side chat** for [DSH](https://www.deepseek.com): a dedicated, agentic chat in a right-side panel, scoped to the conversation it was started from and aware of its workspace. Select part of a conversation and ask about it in the side chat; the side chat inherits the main conversation's toolset, model, and permission preset, and its AI replies can be **brought back to the main conversation** (directly or as a summary, into the composer draft or as a collapsed context row). On top of the Codex-style base, it adds one extra capability: when the main agent asks you a **question dialog**, you can side-chat about the question and its options **without interrupting the flow** — let the AI help you think it through first, then bring the answer back and answer t

## ✨ Key Features

- **Select text → ask in a side chat.** Select any part of a message and a
- **Per-conversation isolation.** Each side chat is a hidden ordinary DSH
- **Inherits main-conversation context.** The side chat is aware of the
- **Model / effort / permission are adjustable.** A two-level model menu
- **"Look up workspace / parent when needed" switch** (default off). When on,
- **Normal conversation capabilities.** Markdown replies, thinking/reasoning
- **Bring AI replies back to the main conversation.** Every assistant reply in
- **Ask about the current question dialog — without interrupting the flow.**

## 📦 Install

```bash
pnpm install
pnpm build
```

## 🚀 Quick Start

```bash
npx -p @deepseek-ai/dsh dsh plugin --profile web add dsh-side-chat-plus
```

## 📚 Learn more

**Install from npm**

The built package is published to npm as [`dsh-side-chat-plus`](https://www.npmjs.com/package/dsh-side-chat-plus). Installed from the registry, the tarball ships the prebuilt `lib/` (plus `cordis.patch.yml` and `dsh.plugin.json`), so no source build is needed: npx -p @deepseek-ai/dsh dsh plugin --profile web add dsh-side-chat-plus `dsh plugin` reconciles the bundle into the profile's `dsh.profile.

**Install from GitHub**

npx -p @deepseek-ai/dsh dsh plugin --profile web add github:heartmove/dsh-side-chat-plus `dsh plugin` forwards to pnpm inside `~/.dsh/profiles/web/`, then reconciles the bundle into the profile's `dsh.profile.bundles` layer list. A git install fetches sources, so pnpm runs the package's `prepare` script (`tsdown`) to build `lib/` from `src/` after checkout. pnpm ≥ 10 refuses to run a git dependenc

**Install from a local checkout**

From the directory that contains this checkout: npx -p @deepseek-ai/dsh dsh plugin --profile web add ./dsh-side-chat-plus pnpm links the checkout and `dsh` activates the bundle the same way.

**Usage**

1. Select part of any message in the main conversation. 2. A floating **"Ask in side chat"** button appears — click it. - If a side chat already exists for this conversation, you'll also see **"Continue active side chat"**. 3. The right-side panel opens (or expands) with the selected text staged in the composer. 4. Adjust **model / effort** and **permission**, and toggle **"Look up workspace / par

## 🔗 Links

- [GitHub Repository](https://github.com/heartmove/dsh-side-chat)
- [Full README](https://github.com/heartmove/dsh-side-chat#readme)
- [Back to the Plugins list](../plugins.md)
