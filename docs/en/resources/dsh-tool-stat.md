---
title: "dsh-tool-stat"
description: "DSH 统计工具插件：描述统计/百分位数/频数分布/相关性，零依赖纯函数确定性"
keywords: "dsh-tool-stat, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-tool-stat

> ⭐ **6** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | — |
| Subcategory | 💰 Cost & billing | Capabilities | coding |

## One-liner

> DSH 统计工具插件：描述统计/百分位数/频数分布/相关性，零依赖纯函数确定性

## About

[English](README.en.md) DSH 统计工具插件 —— 描述统计、百分位数、频数分布、相关性计算。零依赖、纯函数、确定性。

## ✨ Key Features

- **零依赖**：Neumaier 补偿求和、Welford 在线方差、线性插值百分位、Spearman midrank 全部手写，无第三方数值库
- **有限数强约束**：拒绝 `NaN` / `Infinity`（错误信息带下标定位，如 `values[3] must be a finite number (got Infinity)`）；`-0` 在输入与输出中均规范化为 `0`
- **溢出回检**：所有结果在返回前再次做有限数检查，中间或最终结果溢出返回 `numeric-overflow` 错误——canonical 输出**绝不含**非有限值
- **纯函数**：输入数组永不被修改（只读遍历；需要排序时先拷贝）
- **零方差语义**：`correlation` 遇零方差配对返回 `defined: false` + `reason: "zero-variance"`，而不是 NaN 或 ±Infinity
- **预算**：

## 📦 Install

```bash
# 交互式（web）profile —— 从 GitHub 仓库安装
dsh plugin --profile web add github:omdsh-dev/dsh-tool-stat
# 一次性任务（headless）profile —— dsh run 默认使用 headless
dsh plugin --profile headless add github:omdsh-dev/dsh-tool-stat
```

## 🚀 Quick Start

```bash
npm pack     # 生成 dsh-tool-stat-<version>.tgz
# 交互式（web）profile
dsh plugin --profile web add ./dsh-tool-stat-<version>.tgz
# 一次性任务（headless）profile
dsh plugin --profile headless add ./dsh-tool-stat-<version>.tgz
```

## 📚 Learn more

**输出示例**

{"action":"describe","count":5,"sum":15,"min":1,"max":5,"mean":3,"median":3,"variance":2, "standardDeviation":1.4142135623730951,"q1":2,"q3":4,"iqr":2,"sample":false} {"action":"correlation","method":"pearson","count":4,"defined":true,"value":1,"reason":null}

**一次性任务（headless）profile —— dsh run 默认使用 headless**

dsh plugin --profile headless add github:omdsh-dev/dsh-tool-stat 或使用 `npm pack` 生成的 tarball 安装： npm pack # 生成 dsh-tool-stat-<version>.tgz

**手动安装与旧版本兼容（monorepo 旧场景）**

monorepo 方式仅适用于旧场景：不支持 Profile Bundle 的旧快照或插件开发调试环境（本地 junction/symlink、手动编辑 profile 层）。

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-tool-stat)
- [Full README](https://github.com/omdsh-dev/dsh-tool-stat#readme)
- [Back to the Plugins list](../plugins.md)
