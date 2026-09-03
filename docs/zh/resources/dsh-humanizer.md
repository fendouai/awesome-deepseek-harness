---
title: "dsh-humanizer"
description: "写作工具：去除 AI 腔并贴合个人文风。8 个确定性工具扫描文本、从样本提取文风指纹，并返回改写 brief。"
keywords: "dsh-humanizer, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-humanizer

> ⭐ **1** · 🧪 实验性 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 1 | 状态 | 🧪 实验性 |
| 作者 | [lynote-ai](https://github.com/lynote-ai) | 更新时间 | 2026-08-20 |
| 子分类 | 🧰 工具与工具包 | 能力 | coding |

## 一句话介绍

> 写作工具：去除 AI 腔并贴合个人文风。8 个确定性工具扫描文本、从样本提取文风指纹，并返回改写 brief。

## 详细介绍

A writing skill for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`). The core idea is **not "write like a human", but "write like me"**: strip generic AI-sounding patterns on one side, learn your own writing fingerprint on the other, and turn any draft into something *you* wrote. This is a **skill for the agent**, not an LLM wrapper: it performs no model calls. It only produces rules, fingerprints, scores, and rewrite briefs — the agent does the actual rewriting itself.

## 📦 安装

```bash
# from GitHub (ships prebuilt lib/)
dsh plugin add github:lynote-ai/dsh-humanizer

# or, once published to npm:
# dsh plugin add dsh-humanizer
```

## 🚀 快速开始

```bash
- insert:
    - id: dsh-humanizer
      name: 'dsh-humanizer'
      config:
        strength: standard                          # light | standard | aggressive
        storagePath: ~/.dsh/voice-profiles.json
        maxExcerpts: 3
```

## 📚 更多信息

**Example (agent's point of view)**

User: I have a dozen tweets I wrote. Build me a "my voice" profile. Agent: 1. voice_import(name="me-x", samples=[...]) → extract & store fingerprint User: Rewrite this AI-written release post in my voice. Agent: 1. voice_score(text=draft, name="me-x") → 41/100 2. voice_rewrite(text=draft, name="me-x") → get brief (fingerprint + samples + issues) 3. agent rewrites following the brief 4. voice_score

**中文说明**

面向 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（`dsh`）的写作插件。核心理念是——**不是「像人写」，而是「像我写」**：一边去掉通用 AI 腔，一边学习你本人的写作指纹，把任意草稿改成「你写的」。 这是一个给 Agent 用的 **skill**，**不调模型**：只产出规则、指纹、打分和「改写 brief」，真正的改写由 Agent 自己完成。 规则库中英双语覆盖（参考 stop-slop / Humanizer-zh）。指纹提取与打分均为确定性计算，可复现、可单测；Profile 默认持久化到 `~/.dsh/voice-profiles.json`。 安装：`dsh plugin add github:lynote-ai/dsh-humanizer`

## 🔗 链接

- [GitHub 仓库](https://github.com/lynote-ai/dsh-humanizer)
- [完整 README](https://github.com/lynote-ai/dsh-humanizer#readme)
- [返回dsh-humanizer所在分类](../plugins.md)
