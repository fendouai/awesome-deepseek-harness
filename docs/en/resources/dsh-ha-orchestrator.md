---
title: "dsh-ha-orchestrator"
description: "DeepSeek Harness（dsh）动态 Cordis 插件：模型高可用回退 + 五种模式子智能体编排（fanout / pipeline / supervisor / map-reduce / router）"
keywords: "dsh-ha-orchestrator, multi-agent, agent, coding, deepseek harness, dsh"
---
# dsh-ha-orchestrator

> ⭐ **7** · ✅ active · agent

| | | | |
|---|---|---|---|
| Type | agent | Category | Multi-agent |
| Stars | ⭐ 7 | Status | ✅ active |
| Author | [Saktawdi](https://github.com/Saktawdi) | Updated | — |

## One-liner

> DeepSeek Harness（dsh）动态 Cordis 插件：模型高可用回退 + 五种模式子智能体编排（fanout / pipeline / supervisor / map-reduce / router）

## About

HA Orchestrator 是 [DeepSeek Harness](https://github.com/deepseek-ai/dsh)（dsh）的插件： - 模型调用中途出错时，自动改用备用模型重试，任务继续跑下去。 - 提供一个 `orchestrate` 工具，模型遇到适合的任务会自己调用它，把工作拆给多个子智能体并行执行（`fanout`）、分阶段执行（`pipeline`），或进行评审/归约（`supervisor`、`map-reduce`、`router`）。 配置页里还能定义自己的子智能体（也可以一句话让 AI 生成）；界面和提示词文案支持中英文，跟随 DSH 语言。 [English](README.en.md) **特别适合：** 深度调研、大型代码库阅读、批量审查、多方案对比和实现计划编排。

## ✨ Key Features

- 模型调用中途出错时，自动改用备用模型重试，任务继续跑下去。
- 提供一个 `orchestrate` 工具，模型遇到适合的任务会自己调用它，把工作拆给多个子智能体并行执行（`fanout`）、分阶段执行（`pipeline`），或进行评审/归约（`supervisor`、`map-reduce`、`router`）。

## 📦 Install

```bash
dsh plugin --profile web add dsh-ha-orchestrator
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add "file:<本仓库绝对路径>"
```

## 📚 Learn more

**安装**

需要：[DeepSeek Harness](https://github.com/deepseek-ai/dsh)（web profile）。发布包无需本地构建，运行时 peer 服务由 DSH 提供。

**方法一：npm 一条命令安装（推荐）**

本包已发布到 npm（包名 `dsh-ha-orchestrator`）： 1. 执行一条命令： ```sh dsh plugin --profile web add dsh-ha-orchestrator ``` 2. 因为本包声明了 `dsh.bundle.patch`，`dsh plugin add` 会自动把 **dsh-ha-orchestrator** 加进 `dsh.profile.bundles` 并应用 `cordis.patch.yml`，无需手写组合行。 3. 无需重启：bundle patch 层会被热加载（Cordis HMR），插件在运行中的进程里直接生效。刷新浏览器页面即可看到配置页。插件同样随进程启动自动加载，重启后依然生效。

**方法二：本地仓库安装（开发用）**

用于开发或测试未发布版本。需要 PATH 里有 pnpm： 1. 执行一条命令： ```sh dsh plugin --profile web add "file:<本仓库绝对路径>" ``` 2. 因为本包声明了 `dsh.bundle.patch`，`dsh plugin add` 会自动把 **dsh-ha-orchestrator** 加进 `dsh.profile.bundles` 并应用 `cordis.patch.yml`，无需手写组合行。 3. 无需重启：bundle patch 层会被热加载（Cordis HMR），插件在运行中的进程里直接生效。刷新浏览器页面即可看到配置页。插件同样随进程启动自动加载，重启后依然生效。

**方法三：手动安装（无需 pnpm）**

1. 把本仓库复制到 DSH profile 的 node_modules 下：`~/.dsh/profiles/web/node_modules/dsh-ha-orchestrator` 2. 在组合文件 `~/.dsh/profiles/web/cordis.patch.yml` 中加入： ```yaml - insert: - id: dsh-ha-orchestrator name: dsh-ha-orchestrator ``` 3. 无需重启：profile 的 patch 层会被热加载（Cordis HMR），插件在运行中的进程里直接生效。刷新浏览器页面即可看到配置页。插件同样随进程启动自动加载，重启后依然生效。 > **版本说明：** [v0.1.0](https://github.com/Saktawdi/dsh-ha-orchestrator/releases/tag/

## 🔗 Links

- [GitHub Repository](https://github.com/Saktawdi/dsh-ha-orchestrator)
- [Full README](https://github.com/Saktawdi/dsh-ha-orchestrator#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
