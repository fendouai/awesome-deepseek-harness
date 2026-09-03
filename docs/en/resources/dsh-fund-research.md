---
title: "dsh-fund-research"
description: "Chinese public mutual fund research: public-source data collection and deterministic manager/portfolio metrics."
keywords: "dsh-fund-research, research, plugin, deepseek harness, dsh"
---
# dsh-fund-research

> ⭐ **18** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Research |
| Stars | ⭐ 18 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | — |

## One-liner

> Chinese public mutual fund research: public-source data collection and deterministic manager/portfolio metrics.

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-fund-research` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Deterministic research reports for Chinese public mutual funds, on DeepSeek Harness.** *Every key number in every report traces back to a hashed source snapshot — gaps declared, never invented. Research only; not investment advice.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-fund-research` (counts toward the [deepseek1024.com](https://deepsee

## 📦 Install

```bash
dsh plugin --profile web add dsh-fund-research     # install (npm or tarball)
dsh plugin --profile web remove dsh-fund-research  # uninstall
```

## 🚀 Quick Start

```bash
> 用 fund_research 出一份 161725 的研究报告
```

## 📚 Learn more

**Quick start**

> 用 fund_research 出一份 161725 的研究报告 The agent calls `fund_research({ code: "161725" })`; a minute later the workspace holds: fund-reports/161725/20260819-153012/ ├── snapshot.json # raw extracted data + computed metrics + per-source sha256 ├── sources-discovery.json # code-generated endpoint roster + coverage + gaps ├── report.md # the research report with the traceability appendix └── manifest.jso

**Install & uninstall**

dsh plugin --profile web add dsh-fund-research # install (npm or tarball) dsh plugin --profile web remove dsh-fund-research # uninstall Restart the profile after installing (bundle activation is restart-based). The bundle patch composes the storage stack (`dsh-storage` + `dsh-storage-json` + `dsh-storage-domain`) the snapshot layer needs.

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-fund-research)
- [Full README](https://github.com/PerryLink/dsh-fund-research#readme)
- [Back to the Plugins list](../plugins.md)
