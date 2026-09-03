---
title: "dsh-pocket"
description: "把 DeepSeek Harness 装进你的口袋：电脑上跑 dsh web，手机扫码即同步访问（局域网 + 公网，实时同屏）Put DeepSeek Harness in your pocket: run dsh web on your computer and access it synchronously by scanning a QR code on your phone (LAN + public network, real‑time screen mirroring)"
keywords: "dsh-pocket, search, plugin, coding, deepseek harness, dsh"
---
# dsh-pocket

> ⭐ **796** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 796 | Status | ✅ active |
| Author | [shaobeichen](https://github.com/shaobeichen) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding |

## One-liner

> 把 DeepSeek Harness 装进你的口袋：电脑上跑 dsh web，手机扫码即同步访问（局域网 + 公网，实时同屏）Put DeepSeek Harness in your pocket: run dsh web on your computer and access it synchronously by scanning a QR code on your phone (LAN + public network, real‑time screen mirroring)

## About

**你不在电脑前，也想用电脑上的 DeepSeek Harness。** - 下班路上，agent 在电脑上跑任务，你想掏出手机看看它干到哪了、结果如何 - 出门在外，突然想让电脑上的 agent 查点资料、写段代码，但没有远程桌面、没有 SSH - 电脑在宿舍/办公室，你人在外面，想随时"操控你的 DeepSeek Harness"——发任务、看输出、点审批 DSH Pocket 就是干这个的：**装上它，手机扫个码，就能实时看到并操控电脑上的 DeepSeek Harness 界面**——人在外面也能用。 实际效果——手机上的界面就是电脑上的界面，实时同步：

## ✨ Key Features

- 下班路上，agent 在电脑上跑任务，你想掏出手机看看它干到哪了、结果如何
- 出门在外，突然想让电脑上的 agent 查点资料、写段代码，但没有远程桌面、没有 SSH
- 电脑在宿舍/办公室，你人在外面，想随时"操控你的 DeepSeek Harness"——发任务、看输出、点审批

## 📦 Install

```bash
npm install -g @deepseek-ai/dsh     # 全局安装；验证：dsh --version
# 不想全局装？每次命令前加 npx：npx @deepseek-ai/dsh <命令>
```

## 🚀 Quick Start

```bash
# 1. 装插件（一个包全都有）
dsh plugin --profile web add dsh-pocket -w

# 2. 重启 dsh web
npx @deepseek-ai/dsh web
```

## 🔗 Links

- [GitHub Repository](https://github.com/shaobeichen/dsh-pocket)
- [Full README](https://github.com/shaobeichen/dsh-pocket#readme)
- [Back to the Plugins list](../plugins.md)
