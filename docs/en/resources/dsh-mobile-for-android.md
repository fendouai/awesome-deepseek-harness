---
title: "dsh-mobile-for-android"
description: "The Android mobile version of DeepSeek Harness that relies on Tailscale."
keywords: "dsh-mobile-for-android, mobile, client, coding, deepseek harness, dsh"
---
# dsh-mobile-for-android

> ⭐ **12** · ✅ active · client · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | client | Category | Mobile |
| Stars | ⭐ 12 | Status | ✅ active |
| Author | [Hongtwenfive1226](https://github.com/Hongtwenfive1226) | Updated | 2026-08-15 |

## One-liner

> The Android mobile version of DeepSeek Harness that relies on Tailscale.

## About

DeepSeek Harness（DSH）的移动端客户端，基于 React Native（Android）。通过 Tailscale 安全访问运行在桌面端的 DSH，在手机上完成对话、工作区管理、工具审批、任意文件上传/下载等操作，并在**对话中途切换 Agent 模式**。 ---

## ✨ Key Features

- 🔄 **对话中更换模式**：默认以「极简模式」开始，对话进行到任意时刻（首次回复结束后）都能切换成标准/代码/创造等其它预设——手机端侧边栏「切换模式」、桌面端会话头部「切换模式」按钮，两条路共用同一后端能力。
- 🐧 **Git Bash 版极简模式**：Windows 上不用装 WSL，也能让极简模式跑在 Git Bash(MSYS2) 上；手机端默认优先选它。
- 📜 会话历史与桌面端完全同步：上滑可一路翻到第一条（分页 + 主机端 `compact` 瘦身，一页从 MB 级降到 KB 级）。
- 💭 思维链输出：助手回复可展开查看完整推理过程（历史与流式都支持）。
- 🛠 工具调用卡片 + 审批弹窗（允许/拒绝）
- 📎 任意文件上传到宿主机 / 下载到手机（文件桥），🖼 图片附件下载
- ⏹ 停止当前对话、📊 Token 实时显示（输入/输出/缓存命中）
- ⚙️ 设置：服务器地址、Agent 预设、模型选择（本地持久化）

## 📦 Install

```bash
npm install
build-android.cmd assembleRelease -PreactNativeArchitectures=arm64-v8a
# 产物：android/app/build/outputs/apk/release/app-release.apk
```

## 🚀 Quick Start

```bash
git tag v1.4.0
git push origin v1.4.0
```

## 📚 Learn more

**6. 构建并安装 APK**

npm install build-android.cmd assembleRelease -PreactNativeArchitectures=arm64-v8a

## 🔗 Links

- [GitHub Repository](https://github.com/Hongtwenfive1226/DSH-Mobile-for-Android)
- [Full README](https://github.com/Hongtwenfive1226/DSH-Mobile-for-Android#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
