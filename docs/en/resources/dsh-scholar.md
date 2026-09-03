---
title: "dsh-scholar"
description: "dsh-scholar"
keywords: "dsh-scholar, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-scholar

> ⭐ **25** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 25 | Status | ✅ active |
| Author | [lzszq](https://github.com/lzszq) | Updated | — |

## One-liner

> dsh-scholar

## About

[简体中文](README.zh-CN.md) | **English** DSH Scholar is an AI research workspace for computational research. It keeps project conversations, research materials, code and data, controlled experiment runs, evidence, and TeX manuscripts in one recoverable project. You can start from a new question or continue work that already exists elsewhere.

## ✨ Key Features

- **Stage-aware research guidance**: Chat supports natural conversation, Grill Me intake, file upload, visual-model input, explicit slash commands, and an authori
- **Governed research workflow**: Scope, Idea, Contract, Evidence, Direction, and Release decisions remain explicit, revision-bound, and auditable.
- **Controlled execution**: Runner Profiles describe local, local-Docker, or remote-SSH environments, including pinned container images and declared NVIDIA GPU ca
- **Integrated workspace**: project-scoped Chat, editable files, session-bound Web terminals, run logs, artifacts, TeX source, compilation diagnostics, and PDF pr
- **Traceable methodology**: Protocol revisions, run classifications, synthesis requests, assurance results, reviewer findings, knowledge-pack activation, and cla
- **Visible collaboration**: Trajectory and Topology expose subagent parent-child relationships, status, follow-ups, and outputs.

## 📦 Install

```bash
pnpm install --frozen-lockfile
pnpm run build
```

## 🚀 Quick Start

```bash
bash scripts/start-standalone-ui.sh
```

## 📚 Learn more

**Quick start**

The local workspace requires Linux, Node.js 24, pnpm 11.20.0, and Docker Engine for controlled experiments, TeX compilation, and clean-room reproduction.

**3. Configure an execution environment**

Open **Settings → Execution environment** and select an explicit Runner Profile: Formal Jobs do not execute until the selected profile and target pass readiness checks. A missing Runner, offline target, unavailable SecretRef, capability mismatch, or incomplete Contract/Protocol is shown as preparation or a blocker instead of being treated as ready. See the [runtime guide](docs/test-instance-plan.m

**4. Install the plugin in DSH**

Install the current DSH prerelease through its moving `next` tag, then record the exact installed version: npm install -g @deepseek-ai/dsh@next npm ls -g @deepseek-ai/dsh --depth=0 The `@dsh-scholar/*` packages are not published yet. Build this repository and add its absolute path to DSH's `web` profile: cd /absolute/path/to/dsh-scholar pnpm install --frozen-lockfile pnpm run build dsh plugin --pr

**Plugin configuration**

Open **Settings → Plugin config → dsh Scholar** in DSH. Saved plugin changes take effect after the next DSH restart. When `full-auto` is enabled for a valid fixture, Settings also reports worker state, restart-required state, the fixture-only boundary, and the latest park reason. Release remains Human-controlled. The Standalone URL cannot contain credentials, query parameters, or fragments. **Copy

## 🔗 Links

- [GitHub Repository](https://github.com/lzszq/dsh-scholar)
- [Full README](https://github.com/lzszq/dsh-scholar#readme)
- [Back to the Plugins list](../plugins.md)
