---
title: "dsh-plugin-marketplace"
description: "Out-of-tree installable plugin marketplace bundle for DeepSeek Harness"
keywords: "dsh-plugin-marketplace, registry, awesome-list, coding, deepseek harness, dsh"
---
# dsh-plugin-marketplace

> ⭐ **12** · ✅ 活跃 · 精选列表 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 精选列表 | 分类 | 注册表 |
| 星数 | ⭐ 12 | 状态 | ✅ 活跃 |
| 作者 | [w2112515](https://github.com/w2112515) | 更新时间 | 2026-08-18 |

## 一句话介绍

> Out-of-tree installable plugin marketplace bundle for DeepSeek Harness

## 详细介绍

**The plugin marketplace for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (DSH): browse, review, and install DSH plugins from inside DSH's own Settings UI — with evidence-based install safety, consent-gated install scripts, curated solution packs, and zero telemetry.** **中文文档：[README.zh-CN.md](README.zh-CN.md)**（界面语言跟随 DSH 自动切换）

## ✨ 核心特性

- **2,200+ plugins** discovered by a daily scan of every GitHub repository carrying the `dsh-plugin` topic — no GitHub account or token needed to browse.
- **Evidence-based install eligibility**: the scanner proves which install targets exist at each plugin's pinned commit, so "one-click" means *proven installable*
- **Consent-gated scripts**: install scripts are shown verbatim and run only after explicit, per-install consent — never persisted, never bulk-approved.
- **Curated solution packs** that install a coherent capability baseline in one reviewed action.
- **No telemetry, no install counts, no server** — the catalog is static JSON on GitHub Pages.

## 📦 安装

```bash
dsh plugin --profile web add @w2112515/dsh-plugin-marketplace
```

## 🚀 快速开始

```bash
dsh plugin --profile web add github:w2112515/dsh-plugin-marketplace#<40-char-commit>
```

## 📚 更多信息

**Install into your DSH**

From npm: dsh plugin --profile web add @w2112515/dsh-plugin-marketplace Or pin an immutable commit from GitHub (this repository commits its built `lib/`, so no `prepare` runs on your machine): dsh plugin --profile web add github:w2112515/dsh-plugin-marketplace#<40-char-commit> Regular users need no GitHub token. Automatic installs require the Host to run `pnpm` 11 (the plugin also tries `corepack 

**Install safety**

Automatic installs pin an immutable 40-character commit and always go through capability preflight → short-lived review plan → confirmed execution, with rollback of the profile manifest, lockfile, and workspace config on failure. Eligibility is decided by evidence at the pinned commit:

**Configuration**

The bundle's patch row id is `plugin-marketplace`. Override the full config in `$DSH_HOME/profiles/web/cordis.patch.yml` (patch `config` is replaced wholesale, not deep-merged — write every field): config: catalogUrl: https://w2112515.github.io/dsh-plugin-marketplace/plugin-marketplace/catalog-v1.json maxAgeMs: 172800000 timeoutMs: 60000 maxBytes: 15000000 agentTools: true The catalog is a daily G

## 🔗 链接

- [GitHub 仓库](https://github.com/w2112515/dsh-plugin-marketplace)
- [完整 README](https://github.com/w2112515/dsh-plugin-marketplace#readme)
- [返回dsh-plugin-marketplace所在分类](../awesome-lists.md)
