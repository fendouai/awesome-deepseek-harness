---
title: "dsh-sysmon"
description: "DSH Web 系统状态悬浮窗：实时 CPU/内存/磁盘占用率 | System-status overlay showing live CPU, memory and disk usage for DSH Web"
keywords: "dsh-sysmon, memory, plugin, coding, deepseek harness, dsh"
---
# dsh-sysmon

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [AKS1st](https://github.com/AKS1st) | Updated | — |
| Subcategory | 🧠 Memory systems | Capabilities | coding, memory |

## One-liner

> DSH Web 系统状态悬浮窗：实时 CPU/内存/磁盘占用率 | System-status overlay showing live CPU, memory and disk usage for DSH Web

## About

DSH Web 的系统状态悬浮窗：固定在页面右下角，每 1 秒刷新显示 CPU、内存、磁盘占用率。 CPU 39%/16 MEM 46% DISK 22%

## ✨ Key Features

- **位置**：右下角固定悬浮，`pointer-events: none`，不遮挡界面操作。
- **配色**：默认浅灰色小字（等宽字体、11px）。
- **刷新**：1 秒一次。

## 📦 Install

```bash
dsh plugin --profile web add github:AKS1st/dsh-sysmon
dsh web
```

## 🚀 Quick Start

```bash
git clone https://github.com/AKS1st/dsh-sysmon.git
cd dsh-sysmon
npm install
npm run build
dsh plugin --profile web add .
dsh web
```

## 📚 Learn more

**安装**

从 GitHub 仓库安装： dsh plugin --profile web add github:AKS1st/dsh-sysmon dsh web 或 clone 到本地后从本地目录安装： git clone https://github.com/AKS1st/dsh-sysmon.git cd dsh-sysmon npm install npm run build dsh plugin --profile web add . dsh web

## 🔗 Links

- [GitHub Repository](https://github.com/AKS1st/dsh-sysmon)
- [Full README](https://github.com/AKS1st/dsh-sysmon#readme)
- [Back to the Plugins list](../plugins.md)
