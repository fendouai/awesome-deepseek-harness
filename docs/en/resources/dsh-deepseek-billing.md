---
title: "DeepSeek-Harness-billing-plugin"
description: "Account balance plus per-model remaining-task estimator with a session cost ledger."
keywords: "DeepSeek-Harness-billing-plugin, developer, plugin, observability, deepseek harness, dsh"
---
# DeepSeek-Harness-billing-plugin

> ⭐ **9** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 9 | Status | ✅ active |
| Author | [WilliamLIiii](https://github.com/WilliamLIiii) | Updated | 2026-08-14 |
| Subcategory | 💰 Cost & billing | Capabilities | observability |

## One-liner

> Account balance plus per-model remaining-task estimator with a session cost ledger.

## About

一个 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 插件，在 Web 会话头部直接显示你的 **DeepSeek 账户余额**，以及**大概还能跑多少个任务**。

## ✨ Key Features

- **会话头部徽标** —— 剩余余额（`剩余额度：¥X`）加上「按当前模型预计还能跑多少任务」。
- **详情面板** —— 每个模型一行：还能跑多少任务，或「暂无消耗记录」/「按消耗能跑不足 1 个任务，该充钱了」。
- **刷新** —— 按需重新拉取余额并重新折叠用量。

## 📦 Install

```bash
dsh plugin --profile web add @deepseek-ai/dsh-llm-billing @deepseek-ai/dsh-client-ui-billing
```

## 🚀 Quick Start

```bash
- insert:
    - id: llm-billing
      name: '@deepseek-ai/dsh-llm-billing'
    - id: ui-billing
      name: '@deepseek-ai/dsh-client-ui-billing'
```

## 📚 Learn more

**1. 安装包**

dsh plugin --profile web add @deepseek-ai/dsh-llm-billing @deepseek-ai/dsh-client-ui-billing > 这两个包位于本仓库的 `packages/` 工作区内；需要先把它们发布到 npm > （`@deepseek-ai` 或你自己的 scope），`dsh plugin add` 才能从 registry 解析。

**3. 配置你的 DeepSeek API key**

二选一：在网页「模型」页填入（会把 `DEEPSEEK_API_KEY` 写入 `~/.dsh/.credentials.yaml`），或导出环境变量： export DEEPSEEK_API_KEY=sk-...

## 🔗 Links

- [GitHub Repository](https://github.com/WilliamLIiii/DeepSeek-Harness-billing-plugin)
- [Full README](https://github.com/WilliamLIiii/DeepSeek-Harness-billing-plugin#readme)
- [Back to the Plugins list](../plugins.md)
