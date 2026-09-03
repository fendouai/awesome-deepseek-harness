---
title: "deepseek-harness-for-android"
description: "该程序是一个独立的 Capacitor Android 应用，用于管理本机 DeepSeek Harness Ubuntu 用户空间。它提供运行时安装与重置、Ubuntu 终端、可选的 Shizuku 设备 Shell 访问、设置，以及仅限回环地址的内嵌 Harness Web 界面。"
keywords: "deepseek-harness-for-android, mobile, client, coding, deepseek harness, dsh"
---
# deepseek-harness-for-android

> ⭐ **4** · ✅ 活跃 · 客户端 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 移动端 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [standtrain](https://github.com/standtrain) | 更新时间 | 2026-08-20 |

## 一句话介绍

> 该程序是一个独立的 Capacitor Android 应用，用于管理本机 DeepSeek Harness Ubuntu 用户空间。它提供运行时安装与重置、Ubuntu 终端、可选的 Shizuku 设备 Shell 访问、设置，以及仅限回环地址的内嵌 Harness Web 界面。

## 详细介绍

[English](README.md) | [中文](README.zh.md) `app/` is an independent Capacitor Android application for running DeepSeek Harness in a local Ubuntu userspace. Once the runtime is ready, opening the app starts Harness and enters the in-app conversation directly; no external browser is required. Harness service controls, Ubuntu installation and reset, terminals, runtime source details, and optional Shizuku-backed device shell access live under Settings.

## ✨ 核心特性

- Node.js `^22.19.0 || >=24.0.0`, matching the current DeepSeek Harness engine range. Node.js 11.9 cannot build supported Capacitor releases or the current DeepSe
- JDK 23.0.1, with `JAVA_HOME` set explicitly when the system default still points to Java 8.
- Android SDK 35 and a compatible Android NDK.
- The pinned ARM64 PRoot runner and loader used by the release. The current

## 📦 安装

```bash
pnpm install --frozen-lockfile
pnpm run build
pnpm run android:sync
```

## 🔗 链接

- [GitHub 仓库](https://github.com/standtrain/deepseek-harness-for-android)
- [完整 README](https://github.com/standtrain/deepseek-harness-for-android#readme)
- [返回deepseek-harness-for-android所在分类](../clients.md)
