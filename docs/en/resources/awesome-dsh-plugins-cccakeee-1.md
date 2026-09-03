---
title: "awesome-dsh-plugins"
description: "A curated, evidence-led directory of DeepSeek Harness (DSH) plugins: verified loadable extensions, skills, and permission-aware installation guidance."
keywords: "awesome-dsh-plugins, registry, awesome-list, search, deepseek harness, dsh"
---
# awesome-dsh-plugins

> ⭐ **6** · ✅ active · awesome-list

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [cccakeee](https://github.com/cccakeee) | Updated | 2026-08-20 |

## One-liner

> A curated, evidence-led directory of DeepSeek Harness (DSH) plugins: verified loadable extensions, skills, and permission-aware installation guidance.

## About

[English](README.en.md) | **简体中文** | [🌐 网站](https://deepseekharnessplugins.com) DeepSeek Harness 目前处于 **Developer Preview**。官方采用 Cordis 的“Everything is a plugin”架构：Profile 组合 Bundle，外部插件通常以 `package.json` 的 `dsh` 字段及 patch 文件声明挂载方式。[1] [2] 因此，本目录中的安装方法和兼容性应在你自己的 DSH 版本上先行验证。 **快照日期：2026-09-03。** 本版主目录收录 **1794 个**经源码或安装清单核验的插件与 Skill，按 22 个能力分类组织（与配套网站 [deepseekharnessplugins.com](https://deepseekharnessplugins.com) 同构）；完整清单已拆分到 [`docs/categories/`](docs/categories/) 的 22 个分类页面。同时提供 **全量聚合目录 [`CATALOG.md`](CATALOG.md)（2591 个仓库）**，合并 GitHub 搜索与多个社区目录去重后得到。**聚合 ≠ 可装载、可兼容、可安全运行**；只有本目录核验子集进入主目录，证据见 [data/verified-plugins.csv](data/verified-plugins.csv) 与 [data/audit-results.csv](data/audit-results.csv)。[3]

## ✨ Key Features

- 聚合池是**发现清单**，不是推荐或兼容性列表；只有 `✅` 已核验子集进入下方主目录。
- 用 [scripts/aggregate.py](scripts/aggregate.py) 重新拉取并重建 `CATALOG.md` 与 `data/repositories.csv`（需要 `gh` 登录）。

## 📦 Install

```bash
npx @deepseek-ai/dsh web
```

## 📚 Learn more

**安装与安全**

先安装 DSH 并启动一个 Profile。官方快速开始方式是： npx @deepseek-ai/dsh web 随后使用项目说明中给出的 `dsh plugin --profile <profile> add …` 命令。安装前应锁定版本或 commit、阅读 `package.json`、`cordis.patch.yml` 与依赖安装脚本；不要在不了解代码的情况下执行 `curl \| bash`、`pnpm` 生命周期脚本或授予系统级凭据。 详细检查清单见 [docs/SECURITY.zh-CN.md](docs/SECURITY.zh-CN.md)。

## 🔗 Links

- [GitHub Repository](https://github.com/cccakeee/awesome-dsh-plugins)
- [Full README](https://github.com/cccakeee/awesome-dsh-plugins#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
