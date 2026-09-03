---
title: "dsh-specflow"
description: "Specification-driven development toolkit for DeepSeek Harness."
keywords: "dsh-specflow, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-specflow

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [lonelymoon87](https://github.com/lonelymoon87) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Specification-driven development toolkit for DeepSeek Harness.

## About

Turn an idea into a reviewable specification, implementation plan, task list, and resumable [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) goal. SpecFlow stores the work in the repository instead of one conversation. A later session can read the same artifacts, recover the next unchecked task, and resume the matching durable DSH goal. The v0.1.4 release is live on npm and tested with DSH 0.1.0-rc.8 and 0.1.1-rc.1 while retaining the rc.6-compatible peer range. [简体中文](./README.zh-CN.md)

## ✨ Key Features

- five portable skills: `constitution`, `specify`, `plan-spec`, `tasks`, and `implement`;
- six discoverable UI commands: `/specflow`, `/constitution`, `/specify`, `/plan-spec`, `/tasks`, and `/implement`;
- a `specflow_status` tool that reads checkbox progress from `tasks.md`;
- goal creation and explicit resume for `/implement`;
- active goal and task progress in DSH runtime context;
- templates for `spec.md`, `plan.md`, and `tasks.md`.

## 📦 Install

```bash
dsh plugin --profile web add dsh-specflow
dsh web
```

## 🚀 Quick Start

```bash
/constitution Require focused tests for every behavior change
/specify Add resumable exports to the CLI
/plan-spec 001-resumable-exports
/tasks 001-resumable-exports
/implement 001-resumable-exports
```

## 📚 Learn more

**Quick start**

dsh plugin --profile web add dsh-specflow dsh web In a DSH session, enter `/specflow` to see the workflow. A complete run uses these commands: /constitution Require focused tests for every behavior change /specify Add resumable exports to the CLI /plan-spec 001-resumable-exports /tasks 001-resumable-exports /implement 001-resumable-exports After a restart or a new session, recover the durable stat

**Install**

The package supports the DSH `>=0.1.0-rc.6 <0.2.0` plugin APIs and Node.js `^22.19 || >=24`. dsh plugin --profile web add dsh-specflow To pin the current release or install without npm resolution, use the prebuilt GitHub Release tarball: dsh plugin --profile web add https://github.com/lonelymoon87/dsh-specflow/releases/download/v0.1.4/dsh-specflow-0.1.4.tgz The release tarball needs no build allow

**Configuration**

The bundle inserts the plugin with defaults. A profile may configure the plugin entry directly: name: dsh-specflow config: specsDir: .dsh/specs autoInjectContext: true `specsDir` may be workspace-relative or absolute. `autoInjectContext` controls only the model-facing progress snapshot; it does not change goal or artifact behavior.

## 🔗 Links

- [GitHub Repository](https://github.com/lonelymoon87/dsh-specflow)
- [Full README](https://github.com/lonelymoon87/dsh-specflow#readme)
- [Back to the Plugins list](../plugins.md)
