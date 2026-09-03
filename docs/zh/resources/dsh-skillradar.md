---
title: "dsh-skillradar"
description: "扫描会话可见技能，按与近期对话的相关度排序。"
keywords: "dsh-skillradar, learning, plugin, context, workflow, deepseek harness, dsh"
---
# dsh-skillradar

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 学习 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [hellosky983](https://github.com/hellosky983) | 更新时间 | 2026-08-16 |

## 一句话介绍

> 扫描会话可见技能，按与近期对话的相关度排序。

## 详细介绍

A DeepSeek Harness plugin that scans every skill visible to the current session, scores each against the recent conversation text (English + Chinese token overlap), and returns a ranked recommendation of which skill to load next.

## ✨ 核心特性

- DSH version: `0.1.0-rc.6`
- Mainline: verified against `deepseek-harness` mainline snapshots of 2026-08-14
- Last verified: 2026-08-14

## 📦 安装

```bash
dsh plugin add github:hellosky983/dsh-skillradar
```

## 🚀 快速开始

```bash
git clone https://github.com/hellosky983/dsh-skillradar.git
cd dsh-skillradar
dsh plugin add .
```

## 📚 更多信息

**Install / Uninstall**

Install (from GitHub): dsh plugin add github:hellosky983/dsh-skillradar Or clone and install locally: git clone https://github.com/hellosky983/dsh-skillradar.git cd dsh-skillradar dsh plugin add . Upgrade: re-run the install command after `git pull`. Disable temporarily: remove the plugin row from your profile composition, or run: dsh plugin remove dsh-skillradar Uninstall: remove the `dsh-skillra

**Quick start**

After install and restart, tell the agent: > Scan the current session and tell me which skill fits this task. or invoke the tool directly: skill_radar # with no arguments, scans the current session Example output: Skill Radar — 16 skills visible 100% github-upload [github, 仓库, readme, 上传] 85% cordis-plugin-development [client, host, cordis, run]

## 🔗 链接

- [GitHub 仓库](https://github.com/hellosky983/dsh-skillradar)
- [完整 README](https://github.com/hellosky983/dsh-skillradar#readme)
- [返回dsh-skillradar所在分类](../skills.md)
