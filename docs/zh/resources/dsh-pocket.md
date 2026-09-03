---
title: "dsh-pocket"
description: "把 DeepSeek Harness 装进你的口袋：电脑上跑 dsh web，手机扫码即同步访问（局域网 + 公网，实时同屏）Put DeepSeek Harness in your pocket: run dsh web on your computer and access it synchronously by scanning a QR code on your phone (LAN + public network, real‑time screen mirroring)"
keywords: "dsh-pocket, search, plugin, coding, deepseek harness, dsh"
---
# dsh-pocket

> ⭐ **796** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 796 | 状态 | ✅ 活跃 |
| 作者 | [shaobeichen](https://github.com/shaobeichen) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding |

## 一句话介绍

> 把 DeepSeek Harness 装进你的口袋：电脑上跑 dsh web，手机扫码即同步访问（局域网 + 公网，实时同屏）Put DeepSeek Harness in your pocket: run dsh web on your computer and access it synchronously by scanning a QR code on your phone (LAN + public network, real‑time screen mirroring)

## 详细介绍

**你不在电脑前，也想用电脑上的 DeepSeek Harness。** - 下班路上，agent 在电脑上跑任务，你想掏出手机看看它干到哪了、结果如何 - 出门在外，突然想让电脑上的 agent 查点资料、写段代码，但没有远程桌面、没有 SSH - 电脑在宿舍/办公室，你人在外面，想随时"操控你的 DeepSeek Harness"——发任务、看输出、点审批 DSH Pocket 就是干这个的：**装上它，手机扫个码，就能实时看到并操控电脑上的 DeepSeek Harness 界面**——人在外面也能用。 实际效果——手机上的界面就是电脑上的界面，实时同步：

## ✨ 核心特性

- 下班路上，agent 在电脑上跑任务，你想掏出手机看看它干到哪了、结果如何
- 出门在外，突然想让电脑上的 agent 查点资料、写段代码，但没有远程桌面、没有 SSH
- 电脑在宿舍/办公室，你人在外面，想随时"操控你的 DeepSeek Harness"——发任务、看输出、点审批

## 📦 安装

```bash
npm install -g @deepseek-ai/dsh     # 全局安装；验证：dsh --version
# 不想全局装？每次命令前加 npx：npx @deepseek-ai/dsh <命令>
```

## 🚀 快速开始

```bash
# 1. 装插件（一个包全都有）
dsh plugin --profile web add dsh-pocket -w

# 2. 重启 dsh web
npx @deepseek-ai/dsh web
```

## 🔗 链接

- [GitHub 仓库](https://github.com/shaobeichen/dsh-pocket)
- [完整 README](https://github.com/shaobeichen/dsh-pocket#readme)
- [返回dsh-pocket所在分类](../plugins.md)
