---
title: "dsh-plugin-evaluation-standards"
description: "Open evaluation datasets, test cases, and metrics for DSH plugins."
keywords: "dsh-plugin-evaluation-standards, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-evaluation-standards

> ⭐ **1** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [dsh-plugin-evaluation](https://github.com/dsh-plugin-evaluation) | 更新时间 | 2026-08-20 |
| 子分类 | 🧪 代码·测试·审查 | 能力 | coding |

## 一句话介绍

> Open evaluation datasets, test cases, and metrics for DSH plugins.

## 详细介绍

Each dataset is a profile (which metrics to use) and a cases file (test prompts and expected answers). Pick one that fits your plugin, run its cases, and use the results to understand how your plugin behaves.

## ✨ 核心特性

- **Have a real scenario?** Open an [issue](https://github.com/dsh-plugin-evaluation/dsh-plugin-evaluation-standards/issues/new) with how a user would ask, what t
- **Have a small set of cases?** Submit a profile and cases following the [contribution guide](CONTRIBUTING.md).
- **Maintain a dataset long term?** Keep it in your own repository and add it to this catalog using the [external dataset listing guide](DATASET_LISTING.md).

## 📦 安装

```bash
git clone --branch v1.1.0 --depth 1 \
  https://github.com/dsh-plugin-evaluation/dsh-plugin-evaluation-standards.git
```

## 🚀 快速开始

```bash
profiles/<id>.json  Which metrics to use and where to find the cases
cases/<id>.json     Plugin types and test cases
```

## 🔗 链接

- [GitHub 仓库](https://github.com/dsh-plugin-evaluation/dsh-plugin-evaluation-standards)
- [完整 README](https://github.com/dsh-plugin-evaluation/dsh-plugin-evaluation-standards#readme)
- [返回dsh-plugin-evaluation-standards所在分类](../plugins.md)
