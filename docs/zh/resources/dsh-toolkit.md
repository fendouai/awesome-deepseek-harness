---
title: "dsh-toolkit"
description: "零依赖工具包：计算器、CSV、diff、编码、JSON、Markdown、正则、时间。"
keywords: "dsh-toolkit, developer, plugin, files, coding, deepseek harness, dsh"
---
# dsh-toolkit

> ⭐ **24** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 24 | 状态 | ✅ 活跃 |
| 作者 | [omdsh-dev](https://github.com/omdsh-dev) | 更新时间 | 2026-08-21 |
| 子分类 | 🧪 代码·测试·审查 | 能力 | files, coding |

## 一句话介绍

> 零依赖工具包：计算器、CSV、diff、编码、JSON、Markdown、正则、时间。

## 详细介绍

[English](README.en.md) DSH 零依赖工具包 collection —— time / encoding / json / calculator / csv / regex / markdown / diff / stat / schema 十个确定性工具，**统一入口一键安装**。

## 📦 安装

```bash
# 安装单个工具到 web profile
dsh plugin --profile web add github:omdsh-dev/dsh-tool-csv
# 一次性任务（headless）profile
dsh plugin --profile headless add github:omdsh-dev/dsh-tool-diff
```

## 🚀 快速开始

```bash
./scripts/install-web.sh       # 全部 10 工具 → web profile
./scripts/install-headless.sh  # 全部 10 工具 → headless profile（dsh run 使用面）
./scripts/install-all.sh       # 两个 profile 都装
```

## 📚 更多信息

**手动安装与旧版本兼容**

旧场景（monorepo 集成、不支持 Profile Bundle 的旧快照或插件开发调试环境——本地 junction/symlink、手动编辑 profile 层）。

## 🔗 链接

- [GitHub 仓库](https://github.com/omdsh-dev/dsh-toolkit)
- [完整 README](https://github.com/omdsh-dev/dsh-toolkit#readme)
- [返回dsh-toolkit所在分类](../plugins.md)
