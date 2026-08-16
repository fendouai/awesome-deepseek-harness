---
title: "dsh-cost-plugin"
description: "DSH 费用/余额读数插件：在输入框统计行旁实时显示「本次 ≈¥x · 会话 ≈¥x · 余额 ¥x」，内置 DeepSeek 官方价目表，支持 2026-08-17 起生效的峰谷定价（按节点时间戳自动选档），余额经官方 /user/balance 实时查询，失败静默降级。"
keywords: "dsh-cost-plugin, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-cost-plugin

> ⭐ 5 · ✅ 活跃 · 插件

## 一句话介绍

DSH 费用/余额读数插件：在输入框统计行旁实时显示「本次 ≈¥x · 会话 ≈¥x · 余额 ¥x」，内置 DeepSeek 官方价目表，支持 2026-08-17 起生效的峰谷定价（按节点时间戳自动选档），余额经官方 /user/balance 实时查询，失败静默降级。

## 详细介绍

在 [DSH](https://github.com/deepseek-ai/dsh) Web 界面的输入框统计行（`3 轮 · 27 步 | …`）旁追加一行实时费用读数： 本次 ≈¥0.0123 | 会话 ≈¥1.2346 | 余额 ¥70.16 三个读数：**本次费用**（最新一轮 token 消耗 × 单价）、**会话费用**（会话累计 token × 单价）、**余额**（DeepSeek 官方账户余额，可选）。 这是一个 **DSH 动态 Cordis 插件**，由 Host（进程端）与 Client（浏览器端）两半组成，纯 JavaScript、无构建步骤。

## 作者
**[RoxsLee](https://github.com/RoxsLee)**

## 链接

- [GitHub 仓库](https://github.com/RoxsLee/dsh-cost-plugin)
- [完整 README](https://github.com/RoxsLee/dsh-cost-plugin#readme)
- [返回dsh-cost-plugin所在分类](../plugins.md)
