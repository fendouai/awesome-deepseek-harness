---
title: "dsh-skillradar"
description: "Scans session-visible skills and ranks them by relevance to the recent conversation."
keywords: "dsh-skillradar, learning, plugin, context, workflow, deepseek harness, dsh"
---
# dsh-skillradar

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Learning |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [hellosky983](https://github.com/hellosky983) | Updated | 2026-08-16 |

## One-liner

> Scans session-visible skills and ranks them by relevance to the recent conversation.

## About

A DeepSeek Harness plugin that scans every skill visible to the current session, scores each against the recent conversation text (English + Chinese token overlap), and returns a ranked recommendation of which skill to load next.

## ✨ Key Features

- DSH version: `0.1.0-rc.6`
- Mainline: verified against `deepseek-harness` mainline snapshots of 2026-08-14
- Last verified: 2026-08-14

## 📦 Install

```bash
dsh plugin add github:hellosky983/dsh-skillradar
```

## 🚀 Quick Start

```bash
git clone https://github.com/hellosky983/dsh-skillradar.git
cd dsh-skillradar
dsh plugin add .
```

## 📚 Learn more

**Install / Uninstall**

Install (from GitHub): dsh plugin add github:hellosky983/dsh-skillradar Or clone and install locally: git clone https://github.com/hellosky983/dsh-skillradar.git cd dsh-skillradar dsh plugin add . Upgrade: re-run the install command after `git pull`. Disable temporarily: remove the plugin row from your profile composition, or run: dsh plugin remove dsh-skillradar Uninstall: remove the `dsh-skillra

**Quick start**

After install and restart, tell the agent: > Scan the current session and tell me which skill fits this task. or invoke the tool directly: skill_radar # with no arguments, scans the current session Example output: Skill Radar — 16 skills visible 100% github-upload [github, 仓库, readme, 上传] 85% cordis-plugin-development [client, host, cordis, run]

## 🔗 Links

- [GitHub Repository](https://github.com/hellosky983/dsh-skillradar)
- [Full README](https://github.com/hellosky983/dsh-skillradar#readme)
- [Back to the Skills list](../skills.md)
