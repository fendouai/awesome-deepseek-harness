---
title: "dsh-llm-inspector"
description: "Unified LLM request/response inspector: reasoning-effort tuning, external-think export, traffic & bundle analysis."
keywords: "dsh-llm-inspector, developer, plugin, observability, deepseek harness, dsh"
---
# dsh-llm-inspector

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [cdxiaodong](https://github.com/cdxiaodong) | Updated | 2026-08-15 |
| Subcategory | 🛡️ Security & ops | Capabilities | observability |

## One-liner

> Unified LLM request/response inspector: reasoning-effort tuning, external-think export, traffic & bundle analysis.

## About

一个插件收编四类能力，全部通过配置开关：reasoning 控制、外部思考（think）导出、流量/包分析、会话落盘审计。

## 📦 Install

```bash
dsh plugin --profile <你的profile> add github:cdxiaodong/dsh-llm-inspector
```

## 🚀 Quick Start

```bash
plugins:
  dsh-llm-inspector:
    reasoningEffort: 'none'      # 可选:'none' 关推理,或 adapter 支持的 'low'/'medium'/'high'
    externalThinking: true       # 是否启用 think 导出
    trafficAnalysis: true        # 是否做流量/包分析
    persistSession: true         # 是否落盘审计
    logDir: '.dsh-inspector'     # 落盘目录
    # thinkPrompt: '...'         # 可选,覆盖默认强制提示
```

## 📚 Learn more

**外部思考（external thinking）说明**

对**明文返回 reasoning 的模型**（DeepSeek 等开源模型），本插件直接从 `llm/stream` 抓 `reasoning` 块，零侵入。 对**加密推理的模型**（OpenAI / Anthropic / Gemini），原生推理被厂商加密藏起。本插件复刻 [oh-my-pi](https://github.com/can1357/oh-my-pi) 的 externalThinking 思路： 1. `reasoningEffort: 'none'` 关掉原生隐藏推理； 2. 注册一个 `think` 工具（description 为 "private scratchpad; not shown to user"），其 schema 经 `ctx.tools.register()` 自动进入发往 LLM 的请求体； 3. 通过 `systemPrompt.sect

**配置**

plugins: dsh-llm-inspector: reasoningEffort: 'none' # 可选:'none' 关推理,或 adapter 支持的 'low'/'medium'/'high' externalThinking: true # 是否启用 think 导出 trafficAnalysis: true # 是否做流量/包分析 persistSession: true # 是否落盘审计 logDir: '.dsh-inspector' # 落盘目录 # thinkPrompt: '...' # 可选,覆盖默认强制提示

## 🔗 Links

- [GitHub Repository](https://github.com/cdxiaodong/dsh-llm-inspector)
- [Full README](https://github.com/cdxiaodong/dsh-llm-inspector#readme)
- [Back to the Plugins list](../plugins.md)
