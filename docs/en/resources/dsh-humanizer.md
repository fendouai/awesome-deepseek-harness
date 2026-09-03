---
title: "dsh-humanizer"
description: "Writing tool for the agent: removes AI-sounding patterns and clones your personal voice. 8 deterministic tools scan text, build a style fingerprint from your samples, and return rewrite briefs."
keywords: "dsh-humanizer, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-humanizer

> ⭐ **1** · 🧪 experimental · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 1 | Status | 🧪 experimental |
| Author | [lynote-ai](https://github.com/lynote-ai) | Updated | 2026-08-20 |
| Subcategory | 🧰 Toolkits | Capabilities | coding |

## One-liner

> Writing tool for the agent: removes AI-sounding patterns and clones your personal voice. 8 deterministic tools scan text, build a style fingerprint from your samples, and return rewrite briefs.

## About

A writing skill for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`). The core idea is **not "write like a human", but "write like me"**: strip generic AI-sounding patterns on one side, learn your own writing fingerprint on the other, and turn any draft into something *you* wrote. This is a **skill for the agent**, not an LLM wrapper: it performs no model calls. It only produces rules, fingerprints, scores, and rewrite briefs — the agent does the actual rewriting itself.

## 📦 Install

```bash
# from GitHub (ships prebuilt lib/)
dsh plugin add github:lynote-ai/dsh-humanizer

# or, once published to npm:
# dsh plugin add dsh-humanizer
```

## 🚀 Quick Start

```bash
- insert:
    - id: dsh-humanizer
      name: 'dsh-humanizer'
      config:
        strength: standard                          # light | standard | aggressive
        storagePath: ~/.dsh/voice-profiles.json
        maxExcerpts: 3
```

## 📚 Learn more

**Example (agent's point of view)**

User: I have a dozen tweets I wrote. Build me a "my voice" profile. Agent: 1. voice_import(name="me-x", samples=[...]) → extract & store fingerprint User: Rewrite this AI-written release post in my voice. Agent: 1. voice_score(text=draft, name="me-x") → 41/100 2. voice_rewrite(text=draft, name="me-x") → get brief (fingerprint + samples + issues) 3. agent rewrites following the brief 4. voice_score

**中文说明**

面向 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（`dsh`）的写作插件。核心理念是——**不是「像人写」，而是「像我写」**：一边去掉通用 AI 腔，一边学习你本人的写作指纹，把任意草稿改成「你写的」。 这是一个给 Agent 用的 **skill**，**不调模型**：只产出规则、指纹、打分和「改写 brief」，真正的改写由 Agent 自己完成。 规则库中英双语覆盖（参考 stop-slop / Humanizer-zh）。指纹提取与打分均为确定性计算，可复现、可单测；Profile 默认持久化到 `~/.dsh/voice-profiles.json`。 安装：`dsh plugin add github:lynote-ai/dsh-humanizer`

## 🔗 Links

- [GitHub Repository](https://github.com/lynote-ai/dsh-humanizer)
- [Full README](https://github.com/lynote-ai/dsh-humanizer#readme)
- [Back to the Plugins list](../plugins.md)
