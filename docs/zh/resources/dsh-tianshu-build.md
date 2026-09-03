---
title: "dsh-tianshu-build"
description: "DeepSeek X Tianshu  Harness build 是一款完全体开源 coding agent:在 dsh harness 基础之上带视觉、跨会话记忆、验证门、agent 路由、语义 + 图谱代码检索、文件回滚和全屏终端 UI——全部以插件组合。  它是 DeepSeek Harness(dsh)的友好 MIT fork, 它保留了上游一切皆插件的架构，并将以harness最佳形态和架构往下演进。"
keywords: "dsh-tianshu-build, multi-agent, agent, coding, ui, deepseek harness, dsh"
---
# dsh-tianshu-build

> ⭐ **36** · ✅ 活跃 · 智能体 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 智能体 | 分类 | 多智能体 |
| 星数 | ⭐ 36 | 状态 | ✅ 活跃 |
| 作者 | [huiliyi37](https://github.com/huiliyi37) | 更新时间 | 2026-08-20 |

## 一句话介绍

> DeepSeek X Tianshu  Harness build 是一款完全体开源 coding agent:在 dsh harness 基础之上带视觉、跨会话记忆、验证门、agent 路由、语义 + 图谱代码检索、文件回滚和全屏终端 UI——全部以插件组合。  它是 DeepSeek Harness(dsh)的友好 MIT fork, 它保留了上游一切皆插件的架构，并将以harness最佳形态和架构往下演进。

## 详细介绍

Tianshu Harness (`oh-my-tianshu`) is a full-capability open-source coding agent built on a plugin harness: models, tools, policies, memory, retrieval, and interfaces are all Cordis plugins a deployment can compose, replace, or extend without touching the agent loop. One distribution, four surfaces — full-screen terminal UI, browser UI, headless one-shot runs, and an ACP automation server — over a deep capability bench: a vision bridge plus an `ask_image` co-pilot so text-only primaries still work with images, cross-session project memory with a write-quality gate, an evidence gate enforcing RED→GREEN on bugfix edits, an agent router that moves from shadow to gradual dispatch over native subagents, semantic (BM25, CJK-aware, optional vector) and tree-sitter graph code retrieval, plan mode w

## 📦 安装

```bash
npm i -g @huiliyi37/oh-my-tianshu
oh-my-tianshu tui
```

## 🚀 快速开始

```bash
npm i -g --allow-scripts=koffi,node-pty,@huiliyi37/dsh-subprocess-local,@google/genai,protobufjs @huiliyi37/oh-my-tianshu
```

## 📚 更多信息

**Install**

Requirements: Node `^22.19 || >=24`, and a DeepSeek API key (`DEEPSEEK_API_KEY`). One-line installer (recommended — it auto-recovers the npm-mirror sync window, where a mirror already has the new entry package but not all of its dependencies and a plain install dies with `ETARGET`): curl -fsSL https://raw.githubusercontent.com/huiliyi37/oh-my-tianshu/main/scripts/install.sh | sh Windows PowerShell

**settings.yaml**

llm-deepseek: spark: enabled: true then switch with `/model spark-flash` or `/model spark-pro` (aliases for `deepseek-spark/deepseek-v4-flash` / `deepseek-spark/deepseek-v4-pro`). Spark shares the DeepSeek API key — no extra configuration. `dsh-spark-anchors` mounts with the `tui` bundle, so the anchor compensation is live once a session runs on the `deepseek-spark` route; a self-assembled profile

## 🔗 链接

- [GitHub 仓库](https://github.com/huiliyi37/dsh-tianshu-build)
- [完整 README](https://github.com/huiliyi37/dsh-tianshu-build#readme)
- [返回dsh-tianshu-build所在分类](../agents.md)
