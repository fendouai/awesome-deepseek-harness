---
title: "dsh-automation"
description: "Run coding tasks on a schedule in fresh Agent sessions, managed by the user or the agent itself."
keywords: "dsh-automation, automation, workflow, deepseek harness, dsh"
---
# dsh-automation

> ⭐ **70** · ✅ active · workflow · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | workflow | Category | Automation |
| Stars | ⭐ 70 | Status | ✅ active |
| Author | [titanwings](https://github.com/titanwings) | Updated | 2026-08-17 |

## One-liner

> Run coding tasks on a schedule in fresh Agent sessions, managed by the user or the agent itself.

## About

🕒  Need recurring or one-shot coding work to run later without relying on an old chat? 🧭  Need each unattended run to stay inside an explicit workspace and permission boundary? 🧾  Need to inspect what ran, which revision it used, and how it ended?

## 📦 Install

```bash
dsh plugin --profile web add github:titanwings/dsh-automation#v0.1.7
```

## 🚀 Quick Start

```bash
git clone https://github.com/titanwings/dsh-automation.git
cd dsh-automation
pnpm install
pnpm check

cd /path/to/deepseek-harness
pnpm dsh plugin --profile web add /absolute/path/to/dsh-automation
```

## 📚 Learn more

**⚡ Install**

Install the GitHub bundle into the DSH Web profile, then restart `dsh web`: dsh plugin --profile web add github:titanwings/dsh-automation#v0.1.7 The version tag keeps the install reproducible; a reviewed commit SHA is equally valid. If you run DSH from its source checkout, use `pnpm dsh` in place of `dsh`. <details> <summary><strong>Install from a local checkout</strong></summary> <br> Node.js 22.

**⚙️ Configuration**

The included `cordis.patch.yml` uses conservative defaults: Edit the plugin row in the deployment profile if you need different values. Increasing concurrency or timeout expands the amount of unattended work; treat those changes as policy decisions.

## 🔗 Links

- [GitHub Repository](https://github.com/titanwings/dsh-automation)
- [Full README](https://github.com/titanwings/dsh-automation#readme)
- [Back to the Workflows & Automation list](../workflows.md)
