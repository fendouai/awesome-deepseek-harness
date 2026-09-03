---
title: "DeepSeek-Harness-billing-plugin"
description: "账户余额 + 按模型剩余任务估算，带会话费用台账。"
keywords: "DeepSeek-Harness-billing-plugin, developer, plugin, observability, deepseek harness, dsh"
---
# DeepSeek-Harness-billing-plugin

> ⭐ **9** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 9 | 状态 | ✅ 活跃 |
| 作者 | [WilliamLIiii](https://github.com/WilliamLIiii) | 更新时间 | 2026-08-14 |
| 子分类 | 💰 费用与统计 | 能力 | observability |

## 一句话介绍

> 账户余额 + 按模型剩余任务估算，带会话费用台账。

## 详细介绍

一个 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 插件，在 Web 会话头部直接显示你的 **DeepSeek 账户余额**，以及**大概还能跑多少个任务**。

## ✨ 核心特性

- **会话头部徽标** —— 剩余余额（`剩余额度：¥X`）加上「按当前模型预计还能跑多少任务」。
- **详情面板** —— 每个模型一行：还能跑多少任务，或「暂无消耗记录」/「按消耗能跑不足 1 个任务，该充钱了」。
- **刷新** —— 按需重新拉取余额并重新折叠用量。

## 📦 安装

```bash
dsh plugin --profile web add @deepseek-ai/dsh-llm-billing @deepseek-ai/dsh-client-ui-billing
```

## 🚀 快速开始

```bash
- insert:
    - id: llm-billing
      name: '@deepseek-ai/dsh-llm-billing'
    - id: ui-billing
      name: '@deepseek-ai/dsh-client-ui-billing'
```

## 📚 更多信息

**1. 安装包**

dsh plugin --profile web add @deepseek-ai/dsh-llm-billing @deepseek-ai/dsh-client-ui-billing > 这两个包位于本仓库的 `packages/` 工作区内；需要先把它们发布到 npm > （`@deepseek-ai` 或你自己的 scope），`dsh plugin add` 才能从 registry 解析。

**3. 配置你的 DeepSeek API key**

二选一：在网页「模型」页填入（会把 `DEEPSEEK_API_KEY` 写入 `~/.dsh/.credentials.yaml`），或导出环境变量： export DEEPSEEK_API_KEY=sk-...

## 🔗 链接

- [GitHub 仓库](https://github.com/WilliamLIiii/DeepSeek-Harness-billing-plugin)
- [完整 README](https://github.com/WilliamLIiii/DeepSeek-Harness-billing-plugin#readme)
- [返回DeepSeek-Harness-billing-plugin所在分类](../plugins.md)
