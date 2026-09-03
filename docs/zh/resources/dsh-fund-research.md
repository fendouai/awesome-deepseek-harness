---
title: "dsh-fund-research"
description: "中国公募基金研究：公开源数据采集 + 确定性经理/组合指标计算。"
keywords: "dsh-fund-research, research, plugin, deepseek harness, dsh"
---
# dsh-fund-research

> ⭐ **18** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 研究 |
| 星数 | ⭐ 18 | 状态 | ✅ 活跃 |
| 作者 | [PerryLink](https://github.com/PerryLink) | 更新时间 | — |

## 一句话介绍

> 中国公募基金研究：公开源数据采集 + 确定性经理/组合指标计算。

## 详细介绍

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-fund-research` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Deterministic research reports for Chinese public mutual funds, on DeepSeek Harness.** *Every key number in every report traces back to a hashed source snapshot — gaps declared, never invented. Research only; not investment advice.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-fund-research` (counts toward the [deepseek1024.com](https://deepsee

## 📦 安装

```bash
dsh plugin --profile web add dsh-fund-research     # install (npm or tarball)
dsh plugin --profile web remove dsh-fund-research  # uninstall
```

## 🚀 快速开始

```bash
> 用 fund_research 出一份 161725 的研究报告
```

## 📚 更多信息

**Quick start**

> 用 fund_research 出一份 161725 的研究报告 The agent calls `fund_research({ code: "161725" })`; a minute later the workspace holds: fund-reports/161725/20260819-153012/ ├── snapshot.json # raw extracted data + computed metrics + per-source sha256 ├── sources-discovery.json # code-generated endpoint roster + coverage + gaps ├── report.md # the research report with the traceability appendix └── manifest.jso

**Install & uninstall**

dsh plugin --profile web add dsh-fund-research # install (npm or tarball) dsh plugin --profile web remove dsh-fund-research # uninstall Restart the profile after installing (bundle activation is restart-based). The bundle patch composes the storage stack (`dsh-storage` + `dsh-storage-json` + `dsh-storage-domain`) the snapshot layer needs.

## 🔗 链接

- [GitHub 仓库](https://github.com/PerryLink/dsh-fund-research)
- [完整 README](https://github.com/PerryLink/dsh-fund-research#readme)
- [返回dsh-fund-research所在分类](../plugins.md)
