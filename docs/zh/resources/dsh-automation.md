---
title: "dsh-automation"
description: "让 Coding 任务按计划在全新 Agent Session 中运行，由用户或 Agent 创建和管理定时任务。"
keywords: "dsh-automation, automation, workflow, deepseek harness, dsh"
---
# dsh-automation

> ⭐ **70** · ✅ 活跃 · 工作流 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 工作流 | 分类 | 自动化 |
| 星数 | ⭐ 70 | 状态 | ✅ 活跃 |
| 作者 | [titanwings](https://github.com/titanwings) | 更新时间 | 2026-08-17 |

## 一句话介绍

> 让 Coding 任务按计划在全新 Agent Session 中运行，由用户或 Agent 创建和管理定时任务。

## 详细介绍

🕒  Need recurring or one-shot coding work to run later without relying on an old chat? 🧭  Need each unattended run to stay inside an explicit workspace and permission boundary? 🧾  Need to inspect what ran, which revision it used, and how it ended?

## 📦 安装

```bash
dsh plugin --profile web add github:titanwings/dsh-automation#v0.1.7
```

## 🚀 快速开始

```bash
git clone https://github.com/titanwings/dsh-automation.git
cd dsh-automation
pnpm install
pnpm check

cd /path/to/deepseek-harness
pnpm dsh plugin --profile web add /absolute/path/to/dsh-automation
```

## 📚 更多信息

**⚡ Install**

Install the GitHub bundle into the DSH Web profile, then restart `dsh web`: dsh plugin --profile web add github:titanwings/dsh-automation#v0.1.7 The version tag keeps the install reproducible; a reviewed commit SHA is equally valid. If you run DSH from its source checkout, use `pnpm dsh` in place of `dsh`. <details> <summary><strong>Install from a local checkout</strong></summary> <br> Node.js 22.

**⚙️ Configuration**

The included `cordis.patch.yml` uses conservative defaults: Edit the plugin row in the deployment profile if you need different values. Increasing concurrency or timeout expands the amount of unattended work; treat those changes as policy decisions.

## 🔗 链接

- [GitHub 仓库](https://github.com/titanwings/dsh-automation)
- [完整 README](https://github.com/titanwings/dsh-automation#readme)
- [返回dsh-automation所在分类](../workflows.md)
