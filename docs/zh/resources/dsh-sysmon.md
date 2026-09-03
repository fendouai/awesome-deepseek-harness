---
title: "dsh-sysmon"
description: "DSH Web 系统状态悬浮窗：实时 CPU/内存/磁盘占用率 | System-status overlay showing live CPU, memory and disk usage for DSH Web"
keywords: "dsh-sysmon, memory, plugin, coding, deepseek harness, dsh"
---
# dsh-sysmon

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 记忆与上下文 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [AKS1st](https://github.com/AKS1st) | 更新时间 | — |
| 子分类 | 🧠 记忆系统 | 能力 | coding, memory |

## 一句话介绍

> DSH Web 系统状态悬浮窗：实时 CPU/内存/磁盘占用率 | System-status overlay showing live CPU, memory and disk usage for DSH Web

## 详细介绍

DSH Web 的系统状态悬浮窗：固定在页面右下角，每 1 秒刷新显示 CPU、内存、磁盘占用率。 CPU 39%/16 MEM 46% DISK 22%

## ✨ 核心特性

- **位置**：右下角固定悬浮，`pointer-events: none`，不遮挡界面操作。
- **配色**：默认浅灰色小字（等宽字体、11px）。
- **刷新**：1 秒一次。

## 📦 安装

```bash
dsh plugin --profile web add github:AKS1st/dsh-sysmon
dsh web
```

## 🚀 快速开始

```bash
git clone https://github.com/AKS1st/dsh-sysmon.git
cd dsh-sysmon
npm install
npm run build
dsh plugin --profile web add .
dsh web
```

## 📚 更多信息

**安装**

从 GitHub 仓库安装： dsh plugin --profile web add github:AKS1st/dsh-sysmon dsh web 或 clone 到本地后从本地目录安装： git clone https://github.com/AKS1st/dsh-sysmon.git cd dsh-sysmon npm install npm run build dsh plugin --profile web add . dsh web

## 🔗 链接

- [GitHub 仓库](https://github.com/AKS1st/dsh-sysmon)
- [完整 README](https://github.com/AKS1st/dsh-sysmon#readme)
- [返回dsh-sysmon所在分类](../plugins.md)
