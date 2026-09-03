---
title: "billion-context-dsh"
description: "模型驱动的上下文管理（Active Context Pruning）：由模型决定何时压缩、压缩什么。"
keywords: "billion-context-dsh, memory, plugin, context, deepseek harness, dsh"
---
# billion-context-dsh

> ⭐ **33** · ✅ 活跃 · 插件 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 记忆与上下文 |
| 星数 | ⭐ 33 | 状态 | ✅ 活跃 |
| 作者 | [Tyan66666](https://github.com/Tyan66666) | 更新时间 | 2026-08-21 |
| 子分类 | 📦 上下文管理 | 能力 | context, memory |

## 一句话介绍

> 模型驱动的上下文管理（Active Context Pruning）：由模型决定何时压缩、压缩什么。

## 详细介绍

[中文](./README.md) | [English](./README.en.md) 衷心感谢以下项目——请给它们一个 ⭐： DeepSeek Harness · billion-context-pi · acp-kernel · opencode-acp Billion-Context for DeepSeek Harness 由模型决定何时压缩、压缩什么——而不是一个硬性上限。 --- npm install billion-context-dsh ---

## ✨ 核心特性

- **模型驱动** —— 摘要由模型自己书写，没有第二次 LLM 摘要调用
- **只建议、不强令** —— 自动策略只 *nudge*（提醒），是否压缩、何时压缩由模型决定
- **持久且可恢复** —— 压缩范围成为 checkpoint 节点，原文保留在 append-only 会话日志中；`decompress` 可恢复，`search_context` 可在块内查找
- **长任务稳得住** —— 每一步都接着前面的成果走，关键结论持续可用、不断叠加，超长任务更容易跑完
- **上下文始终精简** —— 每次请求都只用少量、精炼的上下文，只保留关键信息；不做大段统一压缩，细节不随之衰失，token 消耗自然更低

## 📦 安装

```bash
dsh plugin --profile web add billion-context-dsh
```

## 🚀 快速开始

```bash
npm install billion-context-dsh
```

## 📚 更多信息

**安装**

> 💡 **想让 DeepSeek Harness 帮你装？** 本仓库本身就运行在 DSH 上：把 > [docs/INSTALL.md](docs/INSTALL.md) 交给会话里的 agent，它会读取指南、解析 > 你的 profile、编辑组合配置并验证挂载。前提：① 配置写在 `~/.dsh` 下，需要 > 你批准一次文件权限；② 装完让它调用 `acp_status` 自证。 **方式一（推荐）：DSH 商店 / `dsh plugin` 一键装（bundle）——装完即全局生效，零配置。** 在 DSH 的插件商店里点安装，或命令行执行： dsh plugin --profile web add billion-context-dsh 命令内部会装包并把本包的 bundle 补丁（[cordis.patch.yml](cordis.patch.yml)）自动挂进该 pro

**provide `ctx.compaction` 会冲突。（bundle 安装已自动带上这两行。）**

disabled: true - id: compaction-acp name: 'billion-context-dsh' config: modelContextLimit: 128000 # 可选；省略时自动探测模型真实窗口（回退 128000） **（可选）自定义提示词文案 —— `config.prompts`。** 所有模型可见的提示词（普通/紧急 nudge 首句、上下文分解、增长行、批量提示、tier 蒸馏行、范围表、ACP system prompt 段、四个工具描述）默认**直接复用 acp-kernel 的 `renderNudgeText`**——效率提示、上下文分解、压缩规则、批量提示全部来自 kernel 原文，仅范围表换成 surface-seq 版（kernel 用 mNNNNN 引用，我们架构没有 `<acp>` 标签；seq 范围表同样携带 `[too

**工作原理**

DSH 的每个模型请求都派生自其 append-only 会话日志（*surface*）。ACP 语义直接映射到这一模型： 承载性的压缩指引（工具、哲学、摘要规则、tier 蒸馏/浓缩规则）注册为一次性系统提示段；每条 nudge 携带精简版（效率提示 + 哲学 + 上下文分解 + 压缩规则 + 范围表 + 批量提示）。刻意**不做自动摘要**：自动策略只 nudge 模型（`compactIfNeeded` 返回 null）。

## 🔗 链接

- [GitHub 仓库](https://github.com/Tyan66666/billion-context-dsh)
- [完整 README](https://github.com/Tyan66666/billion-context-dsh#readme)
- [返回billion-context-dsh所在分类](../plugins.md)
