---
title: "dsh_workflow"
description: "Brings Claude Code's UltraCode mode to DSH: upgrade one-shot multi-agent dispatch into a generatable, saveable, governable, observable, recoverable workflow layer."
keywords: "dsh_workflow, workflow, multi-agent, deepseek harness, dsh"
---
# dsh_workflow

> ⭐ **92** · ✅ active · workflow · ⬆️ +3 recently

| | | | |
|---|---|---|---|
| Type | workflow | Category | Workflows |
| Stars | ⭐ 92 | Status | ✅ active |
| Author | [icetomoyo](https://github.com/icetomoyo) | Updated | 2026-08-13 |

## One-liner

> Brings Claude Code's UltraCode mode to DSH: upgrade one-shot multi-agent dispatch into a generatable, saveable, governable, observable, recoverable workflow layer.

## About

DSH 已经有很强的 Harness 基础设施：模型路由、子 Agent provider、工具权限、审批、Session 日志、后台 jobs 与 UI 事件。但仅有这些“执行原语”，团队仍需在每次会话里重新描述如何拆解、并发、验证和汇总。 对 DSH 项目本身，这个插件的价值是把已有 Harness 能力串成完整闭环： flowchart LR A["DSH providers / models"] --> W["DSH Workflow"] B["tool filters / approval"] --> W C["Session / jobs / commands"] --> W W --> D["reusable capsules"] W --> E["durable run graph"] W --> F["resume / governance / evidence"] 因此，DSH 不只会“调用 Agent”，还可以承载长期维护的 Agent 工作流库。

## 📦 Install

```bash
# 构建产物已提交，git 源安装不需要在用户侧编译
dsh plugin --profile web add "github:dsh-external/dsh_workflow#main"

# 验证 bundle 已进入 profile 合成树
dsh --profile web --dump-config
```

## 🚀 Quick Start

```bash
- id: dsh-external-workflow
  name: '@dsh-external/workflow'
```

## 📚 Learn more

**配置**

常见配置如下；完整字段和治理建议见 [配置参考](docs/CONFIGURATION.md)。 name: '@dsh-external/workflow' config: approvalMode: generated-and-local # never | generated-and-local | always maxAgents: 64 maxConcurrency: 8 maxRetainedRuns: 500 fastProvider: spawn # ctx.subagents transport fastModelProvider: deepseek-official fastMaxTokens: 4096 balancedProvider: spawn # ctx.subagents transport balancedModelProvider: deepseek-o

## 🔗 Links

- [GitHub Repository](https://github.com/icetomoyo/dsh_workflow)
- [Full README](https://github.com/icetomoyo/dsh_workflow#readme)
- [Back to the Workflows & Automation list](../workflows.md)
