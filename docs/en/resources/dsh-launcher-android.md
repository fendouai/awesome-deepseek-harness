---
title: "dsh-launcher-android"
description: "DshLauncher: single-APK Android launcher for DeepSeek Harness with embedded Node runtime"
keywords: "dsh-launcher-android, mobile, client, coding, deepseek harness, dsh"
---
# dsh-launcher-android

> ⭐ **4** · ✅ active · client · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | client | Category | Mobile |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [qawse110](https://github.com/qawse110) | Updated | 2026-08-21 |

## One-liner

> DshLauncher: single-APK Android launcher for DeepSeek Harness with embedded Node runtime

## About

单 APK 的 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（dsh）Android 启动器： 内置 Node.js aarch64 运行时与 Termux 工具链，通过官方 npm 包 `@deepseek-ai/dsh` 安装/更新 dsh， 并在设备本机直接启动 `dsh web`（`http://127.0.0.1:3080`），自带 WebView 界面。 **不需要 Termux、不需要外部 Node**；联网仅用于 npm 首次安装与后续更新。 - 包名 `com.dsh.launcher` · 当前版本 **v4.10.2**（versionCode 33） - 架构：AGP 9.0 / Kotlin / Gradle 8.x · minSdk 24 / targetSdk 28 / compileSdk 35

## ✨ Key Features

- 包名 `com.dsh.launcher` · 当前版本 **v4.10.2**（versionCode 33）
- 架构：AGP 9.0 / Kotlin / Gradle 8.x · minSdk 24 / targetSdk 28 / compileSdk 35

## 🚀 Quick Start

```bash
# 在项目根放 signing/release.keystore（或设置 DSH_KEYSTORE_FILE/DSH_KEYSTORE_PASS）
./gradlew assembleRelease        # 或 assembleDebug
```

## 🔗 Links

- [GitHub Repository](https://github.com/qawse110/dsh-launcher-android)
- [Full README](https://github.com/qawse110/dsh-launcher-android#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
