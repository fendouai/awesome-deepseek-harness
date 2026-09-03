---
title: "dsh-deep-research"
description: "Adaptive deep-research orchestrator built on the official workflow engine."
keywords: "dsh-deep-research, research, workflow, search, deepseek harness, dsh"
---
# dsh-deep-research

> ⭐ **18** · ✅ active · workflow · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | workflow | Category | Research |
| Stars | ⭐ 18 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | 2026-08-12 |

## One-liner

> Adaptive deep-research orchestrator built on the official workflow engine.

## About

把 deep-research 流程做成 **DSH 扩展插件**（plugin，与 skill 体系分开）， 基于 **DSH 官方 workflow 引擎**（`ctx.workflows` / `@deepseek-ai/dsh-workflow-workerthread`） 实现，按 **控制论 + 信息论** 设计——不是固定提示词流水线，而是**活的、自适应的研究闭环**。

## 📦 Install

```bash
pnpm install        # 仅 typescript/@types/node（typecheck 用）
pnpm run typecheck  # tsc -b，类型从 sibling deepseek-harness checkout 解析
```

## 🚀 Quick Start

```bash
dsh plugin --profile <profile> add git+https://github.com/dsh-external/dsh-deep-research.git
dsh --profile <profile>        # 重启生效：工具 deep_research 随 profile 注入
```

## 📚 Learn more

**安装与使用方式**

包声明了 `dsh.bundle.patch`（cordis.patch.yml），通过 `dsh plugin` 装进**任意** profile （把 `<profile>` 换成 `tui` / `headless` / `web` 或自建 profile）： dsh plugin --profile <profile> add git+https://github.com/dsh-external/dsh-deep-research.git dsh --profile <profile> # 重启生效：工具 deep_research 随 profile 注入 > 若 pnpm 把 https URL 重写成 git+ssh（本机全局 git `insteadof` 配置所致），用上面的 > `git+https://` 形式；`dsh plugin` 会提示需要 `allowBu

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-deep-research)
- [Full README](https://github.com/omdsh-dev/dsh-deep-research#readme)
- [Back to the Workflows & Automation list](../workflows.md)
