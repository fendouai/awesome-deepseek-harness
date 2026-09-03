---
title: "dsh-launcher-android"
description: "DshLauncher: single-APK Android launcher for DeepSeek Harness with embedded Node runtime"
keywords: "dsh-launcher-android, mobile, client, coding, deepseek harness, dsh"
---
# dsh-launcher-android

> ⭐ **4** · ✅ 活跃 · 客户端 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 移动端 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [qawse110](https://github.com/qawse110) | 更新时间 | 2026-08-21 |

## 一句话介绍

> DshLauncher: single-APK Android launcher for DeepSeek Harness with embedded Node runtime

## 详细介绍

单 APK 的 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（dsh）Android 启动器： 内置 Node.js aarch64 运行时与 Termux 工具链，通过官方 npm 包 `@deepseek-ai/dsh` 安装/更新 dsh， 并在设备本机直接启动 `dsh web`（`http://127.0.0.1:3080`），自带 WebView 界面。 **不需要 Termux、不需要外部 Node**；联网仅用于 npm 首次安装与后续更新。 - 包名 `com.dsh.launcher` · 当前版本 **v4.10.2**（versionCode 33） - 架构：AGP 9.0 / Kotlin / Gradle 8.x · minSdk 24 / targetSdk 28 / compileSdk 35

## ✨ 核心特性

- 包名 `com.dsh.launcher` · 当前版本 **v4.10.2**（versionCode 33）
- 架构：AGP 9.0 / Kotlin / Gradle 8.x · minSdk 24 / targetSdk 28 / compileSdk 35

## 🚀 快速开始

```bash
# 在项目根放 signing/release.keystore（或设置 DSH_KEYSTORE_FILE/DSH_KEYSTORE_PASS）
./gradlew assembleRelease        # 或 assembleDebug
```

## 🔗 链接

- [GitHub 仓库](https://github.com/qawse110/dsh-launcher-android)
- [完整 README](https://github.com/qawse110/dsh-launcher-android#readme)
- [返回dsh-launcher-android所在分类](../clients.md)
