---
title: "dsh-whale-report"
description: "深迹 DeepTrace — Your Agent, in numbers. DSH 插件：从会话事件日志生成日报/周报/月报/年报/自定义区间，确定性洞察与协作复盘，只读、不改写历史。"
keywords: "dsh-whale-report, ui, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-whale-report

> ⭐ **31** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 31 | Status | ✅ active |
| Author | [SenmuuuuW](https://github.com/SenmuuuuW) | Updated | — |
| Subcategory | 💡 Generative UI | Capabilities | coding, multi-agent |

## One-liner

> 深迹 DeepTrace — Your Agent, in numbers. DSH 插件：从会话事件日志生成日报/周报/月报/年报/自定义区间，确定性洞察与协作复盘，只读、不改写历史。

## About

Agent 跑完之后，真正难回答的问题不是"它做了什么"，而是： - 哪些 session 最贵？ - 为什么突然开始 retry？ - 哪些操作值得注意？ - 夜里到底跑了多少？ - 是哪次任务把成本拉高的？ - **这周有什么值得改的？** DeepTrace 不是 log viewer，也不是普通 dashboard——它把会话事件日志聚合成报告，让这些问题有答案。

## ✨ Key Features

- 哪些 session 最贵？
- 为什么突然开始 retry？
- 哪些操作值得注意？
- 夜里到底跑了多少？
- 是哪次任务把成本拉高的？
- **这周有什么值得改的？**

## 📦 Install

```bash
dsh plugin --profile web add "github:SenmuuuuW/dsh-whale-report"
# 重启 dsh web 使宿主代码生效；客户端 bundle 随插件自动更新
```

## 🚀 Quick Start

```bash
npm install dsh-whale-report@0.6.1
```

## 📚 Learn more

**示例**

PROBLEM Repeated Shell Timeouts EVIDENCE 6 次确定性 timeout / 3 个会话（0 硬失败） CHANGE shell.timeoutMs 60s → 120s EXPECTED shell_timeout_rate 下降 ROLLBACK 一键还原 60s（并发安全） 批准后进入 OBSERVING；满足最低证据后输出 **VERIFIED / NOT IMPROVED / INCONCLUSIVE**。NOT IMPROVED 只推荐 Revert，绝不自动回滚。

**Installation**

需要 DSH（DeepSeek Harness，web 端）环境。**v0.6.1 的官方兼容基线是 DSH 0.1.1-rc.2**（peer 范围 `>=0.1.1-rc.2 <0.2.0`；升级 dsh 后重启 web 实例即可，会话数据无需迁移）。两种安装方式，注意区分： **① DSH 插件安装（推荐，完整功能）** —— 注册进 dsh web： dsh plugin --profile web add "github:SenmuuuuW/dsh-whale-report"

**Architecture**

DSH session events（firehose + baseline + salvage） ↓ incremental ingest（seq 去重 / fingerprint reconcile；损坏会话 worker_threads 解压） canonical index（10 分钟分桶 + 精确边界行；coalesced checkpoints 落盘） ↓ query engine（PeriodSpec → 精确窗口 → 纯索引查询，零 session IO） Overview / Report / History（Web / HTML / PDF / PNG） 细节（数据流、存储结构、兼容性策略）见 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)。

## 🔗 Links

- [GitHub Repository](https://github.com/SenmuuuuW/dsh-whale-report)
- [Full README](https://github.com/SenmuuuuW/dsh-whale-report#readme)
- [Back to the Plugins list](../plugins.md)
