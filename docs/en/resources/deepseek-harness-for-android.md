---
title: "deepseek-harness-for-android"
description: "该程序是一个独立的 Capacitor Android 应用，用于管理本机 DeepSeek Harness Ubuntu 用户空间。它提供运行时安装与重置、Ubuntu 终端、可选的 Shizuku 设备 Shell 访问、设置，以及仅限回环地址的内嵌 Harness Web 界面。"
keywords: "deepseek-harness-for-android, mobile, client, coding, deepseek harness, dsh"
---
# deepseek-harness-for-android

> ⭐ **4** · ✅ active · client · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | client | Category | Mobile |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [standtrain](https://github.com/standtrain) | Updated | 2026-08-20 |

## One-liner

> 该程序是一个独立的 Capacitor Android 应用，用于管理本机 DeepSeek Harness Ubuntu 用户空间。它提供运行时安装与重置、Ubuntu 终端、可选的 Shizuku 设备 Shell 访问、设置，以及仅限回环地址的内嵌 Harness Web 界面。

## About

[English](README.md) | [中文](README.zh.md) `app/` is an independent Capacitor Android application for running DeepSeek Harness in a local Ubuntu userspace. Once the runtime is ready, opening the app starts Harness and enters the in-app conversation directly; no external browser is required. Harness service controls, Ubuntu installation and reset, terminals, runtime source details, and optional Shizuku-backed device shell access live under Settings.

## ✨ Key Features

- Node.js `^22.19.0 || >=24.0.0`, matching the current DeepSeek Harness engine range. Node.js 11.9 cannot build supported Capacitor releases or the current DeepSe
- JDK 23.0.1, with `JAVA_HOME` set explicitly when the system default still points to Java 8.
- Android SDK 35 and a compatible Android NDK.
- The pinned ARM64 PRoot runner and loader used by the release. The current

## 📦 Install

```bash
pnpm install --frozen-lockfile
pnpm run build
pnpm run android:sync
```

## 🔗 Links

- [GitHub Repository](https://github.com/standtrain/deepseek-harness-for-android)
- [Full README](https://github.com/standtrain/deepseek-harness-for-android#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
