---
title: "dsh-expert-mode"
description: "DSH (DeepSeek Harness) 专家模式 agent preset — 首席协调官 + 17位领域专家子代理 Expert-mode preset for DeepSeek Harness"
keywords: "dsh-expert-mode, vision, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-expert-mode

> ⭐ **11** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 11 | Status | ✅ active |
| Author | [Asher-2000](https://github.com/Asher-2000) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding, multi-agent |

## One-liner

> DSH (DeepSeek Harness) 专家模式 agent preset — 首席协调官 + 17位领域专家子代理 Expert-mode preset for DeepSeek Harness

## About

1 Coordinator + 17 Experts — Full-Stack Multi-Agent Team 首席协调官 + 17 位领域专家 — 全栈多智能体团队 中文 · English ---

## 📦 Install

```bash
# In DSH workspace — via plugin manager
dsh plugin add dsh-expert-mode

# ...or install the npm package directly
npm install dsh-expert-mode
```

## 🚀 Quick Start

```bash
User: 帮我设计一个用户认证系统

Coordinator:
  → 识别领域: 后端开发 + 安全
  → 委派 Backend Dev: API 设计、JWT 实现
  → 委派 Security: 安全审计、漏洞防护
  → 汇总输出完整方案
```

## 📚 Learn more

**🖼️ Demo**

<p align="center"> <br/> <em>Select the "Expert Mode" preset in DSH workspace to use</em> </p> <p align="center"> <br/> <em>5 expert subagents working in parallel, with real-time token usage and timing</em> </p> ---

**...or install the npm package directly**

npm install dsh-expert-mode > ℹ️ **How agent-presets work**: this is an **agent-preset plugin**, not a Cordis service plugin. Installing the npm package pulls all files into your `node_modules` — but the preset only **activates** once its files are mounted into DSH's preset discovery directory. The preset ships a copy step (below) that makes this one command.

**🚀 Quick Start**

1. Install the plugin 2. Select "专家模式" preset 3. Ask any question — the coordinator auto-delegates to the right expert

**Example**

User: 帮我设计一个用户认证系统 Coordinator: → 识别领域: 后端开发 + 安全 → 委派 Backend Dev: API 设计、JWT 实现 → 委派 Security: 安全审计、漏洞防护 → 汇总输出完整方案 ---

## 🔗 Links

- [GitHub Repository](https://github.com/Asher-2000/dsh-expert-mode)
- [Full README](https://github.com/Asher-2000/dsh-expert-mode#readme)
- [Back to the Plugins list](../plugins.md)
