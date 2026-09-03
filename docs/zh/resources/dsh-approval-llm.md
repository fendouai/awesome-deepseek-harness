---
title: "dsh-approval-llm"
description: "Model-based permission approval (approve-for-me) for DeepSeek Harness: an approval/request answerer backed by a separate reviewer model"
keywords: "dsh-approval-llm, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-approval-llm

> ⭐ **8** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 8 | 状态 | ✅ 活跃 |
| 作者 | [Letter2025](https://github.com/Letter2025) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Model-based permission approval (approve-for-me) for DeepSeek Harness: an approval/request answerer backed by a separate reviewer model

## 详细介绍

**Model-based permission approval (approve-for-me) for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness).** A community plugin that adds a **"model approval" permission mode** (approve-for-me) to DeepSeek Harness: in that mode, `approval/request` asks are answered by a **separate reviewer model** instead of a human — the reviewer decides `ALLOW / DENY / ESCALATE`, and the request only reaches a human when the reviewer cannot decide or fails. In every other permission mode the plugin stays silent, so human approval is never front-run by the model. It is the dsh equivalent of Codex's `approvals_reviewer=auto_review` (`--approve-for-me`), and it follows the review design of AGENTSCOPE-PLAN-058 / 062 / 063 (orthogonal reviewer dimension, three-way decision, routing policy, pr

## ✨ 核心特性

- **ALLOW / DENY / ESCALATE map 1:1 onto the dsh outcome vocabulary** (`allowed-once` / `rejected` / delegate). ESCALATE and model failures never fabricate a reje
- **The mode gate makes the modes exclusive.** In the `帮我批准` preset the reviewer answers; in `请求批准` (and every other preset) the plugin delegates, so human approv
- **One terminal answerer per deployment.** The dsh approval chain is not a priority list of competing judges — compose one answerer. To keep human override, put 
- **Arguments are read from the session log**, not from the approval request (the request deliberately carries no arguments to avoid a second rendering that could

## 📦 安装

```bash
dsh plugin --profile web add dsh-approval-llm   # installs the published npm package
```

## 🚀 快速开始

```bash
- insert:
    - id: approval-llm
      name: './src/index.ts'        # path to this package's entry, or an absolute path
      config:
        provider: deepseek-official
        model: deepseek-v4-flash
```

## 📚 更多信息

**Configuration**

All fields are validated by the Loader schema; defaults apply when omitted. Example overlay (`cordis.patch.yml` of your profile): config: provider: deepseek-official model: deepseek-v4-flash allowlist: [read, read_image, glob, grep] humanOnlyList: [delete, terminal_send] denyList: [job_kill] maxConsecutiveDenials: 3

**Install**

> **Copy-paste for an AI agent** — hand this one sentence to any AI coding agent to have it install the plugin for you: "Read https://github.com/Letter2025/dsh-approval-llm/blob/main/README.md and follow its `## Install` section to install the `dsh-approval-llm` bundle into the DeepSeek Harness web profile, restart the `dsh web` server, and verify that the permission selector shows the `model-appr

**As an installable bundle (recommended)**

This package declares `dsh.bundle.patch` in its `package.json`, so installing it activates a configuration layer that inserts the plugin row **and** adds the `model-approval` ("帮我批准") preset to the `permission` table — no manual preset config needed: dsh plugin --profile web add dsh-approval-llm # installs the published npm package Restart `dsh web`, then pick **帮我批准** in the permission selector (

**Bundled skill: configure the reviewer**

The package ships one bundled skill (`configure-approval-llm`, source `bundled`), so installing the plugin also puts a configuration guide in the skill catalog. Ask any agent to "configure the approval reviewer", or load the skill directly — it walks an **AI-proposes / user-confirms** flow: probe the current model and provider settings, write the `approval-llm` overlay into `~/.dsh/profiles/web/co

## 🔗 链接

- [GitHub 仓库](https://github.com/Letter2025/dsh-approval-llm)
- [完整 README](https://github.com/Letter2025/dsh-approval-llm#readme)
- [返回dsh-approval-llm所在分类](../plugins.md)
