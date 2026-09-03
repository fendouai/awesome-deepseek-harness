---
title: "dsh-usage-stats"
description: "Token usage heatmap, per-model breakdowns, and DeepSeek account balance for the DeepSeek Harness Web GUI (dsh web)."
keywords: "dsh-usage-stats, developer, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-usage-stats

> ⭐ **98** · ✅ 活跃 · 插件 · 近期 ⬆️ +5

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 98 | 状态 | ✅ 活跃 |
| 作者 | [Ychris12138](https://github.com/Ychris12138) | 更新时间 | 2026-08-20 |
| 子分类 | 💰 费用与统计 | 能力 | coding, ui |

## 一句话介绍

> Token usage heatmap, per-model breakdowns, and DeepSeek account balance for the DeepSeek Harness Web GUI (dsh web).

## 详细介绍

为 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 网页端提供多供应商账户监测与 Token 用量分析。 Provider balances, subscription quotas, and token-usage analytics for the DeepSeek Harness Web GUI (`dsh web`).

## 📦 安装

```bash
dsh plugin --profile web add "@ychris12138/dsh-usage-stats@0.3.2"
```

## 🚀 快速开始

```bash
dsh plugin --profile web update "@ychris12138/dsh-usage-stats"
dsh plugin --profile web remove "@ychris12138/dsh-usage-stats"
```

## 📚 更多信息

**dsh-usage-stats**

为 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 网页端提供多供应商账户监测与 Token 用量分析。 Provider balances, subscription quotas, and token-usage analytics for the DeepSeek Harness Web GUI (`dsh web`). > 展示图使用脱敏演示数据；插件不会把 API Key、Cookie、管理 PAT 或上游原始响应发送到浏览器。  > 🐋 OrcaRouter sponsors this project and is available as an optional OpenAI-compatible provider. [Learn more](https://www.orcarouter.

**快速安装 / Quick start**

需要 DeepSeek Harness `web` profile（`@deepseek-ai/dsh >= 0.1.0-rc.6`）。 稳定版优先安装 npm 上的精确版本；这也是 DSH Desktop Market 使用的同一个包： dsh plugin --profile web add "@ychris12138/dsh-usage-stats@0.3.2" 只有测试尚未发布的 source/RC 时才使用 `dsh plugin --profile web add "github:Ychris12138/dsh-usage-stats"`。GitHub `main` 可能领先 npm stable，不应把 source 安装当作市场安装验收。 然后重启已经运行的 `dsh web`，并在浏览器中硬刷新。侧边栏底部会出现“用量/余额”（Usage/Balance）入口。

**插件市场 GUI 安装（DSH Community Market，Path A 标准来源）**

本仓库按 [DSH Community Market 目录 adapter 指南](https://github.com/anywhere-labs/deepseek-harness-desktop/blob/master/dsh-community-market/docs/catalog-adapter-guide.zh.md) 的**标准来源（Path A）** 接入，无需修改 Market 代码。内置两份目录数据： **使用前提（重要）**：市场托管安装只接受 npm registry 的精确稳定版本，git 条目仅可浏览。`dsh-usage-stats` 这个 npm 名已被其他项目占用，因此目录条目身份使用 `@ychris12138/dsh-usage-stats`。当前 stable/catalog 版本是 `0.3.2`；每个新版本都按以下顺序发布： 1. 运行 `npm

**安装但不修改 Cordis patch**

npx --yes github:Ychris12138/dsh-usage-stats --no-enable 无法使用 `npx` 时可从源码运行 `node scripts/install.mjs`。 </details>

## 🔗 链接

- [GitHub 仓库](https://github.com/Ychris12138/dsh-usage-stats)
- [完整 README](https://github.com/Ychris12138/dsh-usage-stats#readme)
- [返回dsh-usage-stats所在分类](../plugins.md)
