---
title: "dsh-token-usage"
description: "Persistent token usage records and dashboard for DeepSeek Harness"
keywords: "dsh-token-usage, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-token-usage

> ⭐ **13** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 13 | Status | ✅ active |
| Author | [LeemanCheung](https://github.com/LeemanCheung) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Persistent token usage records and dashboard for DeepSeek Harness

## About

面向 DeepSeek Harness 的本地优先 Token 可观测性、预算与轨迹审计插件。 持久统计四类 provider Token bucket，提供趋势、预算、公开费率估算、聚合导出，并通过模型目录当前选中的已接入路由按需生成用量和会话轨迹报告。 功能全景 · 功能截图 · 安装 · AI 用量分析 · 轨迹分析 · 已知限制 · 贡献与社区 · 安全

## ✨ Key Features

- **被动账本，不拦截请求**：Host 侧观察普通模型请求、重试和压缩事件，构建可恢复的会话统计 projection；预算、异常和建议只展示证据，不会阻止模型调用或改写路由。
- **按需 AI，不是后台画像**：聚合用量分析和单会话轨迹报告都必须由用户显式启动；前者只发送有界聚合 DTO，后者只发送白名单事件元数据。提示词、回复、标题、路径、工具参数和原始 provider/model 不会进入模型证据。
- **估算不等于账单或合规结论**：USD 数字只按本地静态公开费率计算，报告中的审批统计也只陈述观测到的事件与证据缺口；两者都不替代 provider 账单、策略执行或认证审计。

## 📦 Install

```bash
dsh plugin --profile web add github:LeemanCheung/dsh-token-usage
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add ./dsh-token-usage
```

## 📚 Learn more

**dsh-token-usage**

<p align="center"> <a href="https://awesome.re"></a> <a href="https://awesome-dsh-plugin.com"></a> <a href="https://github.com/deepseek-ai/deepseek-harness"></a>     <a href="LICENSE"></a> </p> <p align="center"> <strong>面向 <a href="https://github.com/deepseek-ai/deepseek-harness">DeepSeek Harness</a> 的本地优先 Token 可观测性、预算与轨迹审计插件。</strong><br> 持久统计四类 provider Token bucket，提供趋势、预算、公开费率估算、聚合导出，并通过模型目录

**🚀 安装**

dsh plugin --profile web add github:LeemanCheung/dsh-token-usage 安装后重启当前 `dsh web` 进程并刷新 [http://127.0.0.1:3080](http://127.0.0.1:3080)，再打开 **设置 → Token 用量**。 <details> <summary>本地源码开发安装</summary> 在本目录的上一级运行： dsh plugin --profile web add ./dsh-token-usage </details>

**🔎 设计参考与取舍**

本插件吸收了主流 Agent 可观测性产品对 Token、成本、缓存和聚合趋势的做法，例如 [LangSmith cost tracking](https://docs.langchain.com/langsmith/cost-tracking)、[OpenAI Agents SDK usage](https://openai.github.io/openai-agents-python/usage/)、[Langfuse token/cost tracking](https://python-sdk-v2.docs-snapshot.langfuse.com/docs/observability/features/token-and-cost-tracking/) 和 [Phoenix LLM metrics](https://arize.com/docs/phoenix/tracing

## 🔗 Links

- [GitHub Repository](https://github.com/LeemanCheung/dsh-token-usage)
- [Full README](https://github.com/LeemanCheung/dsh-token-usage#readme)
- [Back to the Plugins list](../plugins.md)
