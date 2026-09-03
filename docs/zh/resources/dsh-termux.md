---
title: "deepseek-harness-termux"
description: "在 Android/Termux 上运行 DeepSeek Harness。"
keywords: "deepseek-harness-termux, mobile, client, terminal, deepseek harness, dsh"
---
# deepseek-harness-termux

> ⭐ **37** · ✅ 活跃 · 客户端 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 移动端 |
| 星数 | ⭐ 37 | 状态 | ✅ 活跃 |
| 作者 | [Vengisk](https://github.com/Vengisk) | 更新时间 | 2026-08-19 |

## 一句话介绍

> 在 Android/Termux 上运行 DeepSeek Harness。

## 详细介绍

**Run the full [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`@deepseek-ai/dsh`) on Android / Termux — no features disabled.** --- `deepseek-harness-termux` is a community-maintained compatibility layer that ports the official `@deepseek-ai/dsh` [agent harness](https://github.com/deepseek-ai/deepseek-harness) to Android environments running [Termux](https://termux.com/). The official npm package is built for glibc-based Linux distributions and depends on several native modules that fail to compile or misbehave on Android's Bionic libc. Instead of disabling plugins that depend on those modules, this repository patches the source code so every feature works on Termux. All required patches were generated automatically against the pristine upstream tarballs (`@deepseek-a

## ✨ 核心特性

- **Android 8+** recommended (older versions may work but are untested)
- **Termux** from [F-Droid](https://f-droid.org/en/packages/com.termux/) (the Play Store version is unsupported and outdated)
- **Node.js >= 24**, **npm**, and the build toolchain for native modules:
- **Internet connection** for downloading packages

## 📦 安装

```bash
# Clone this repository
git clone https://github.com/Vengisk/deepseek-harness-termux.git
cd deepseek-harness-termux

# Run the automated installer (installs dsh, applies patches, builds node-pty)
bash install.sh
```

## 🚀 快速开始

```bash
# Recommended: fully self-contained (whole patched dsh + node_modules, ~57 MB)
npm i -g https://github.com/Vengisk/deepseek-harness-termux/releases/latest/download/dsh-termux-full.tgz
dsh web
```

## 📚 更多信息

**Plan A — compile on device (install.sh)**

Full control, works on any arm64 Termux; compiles `node-pty`/`koffi` once (clang + cmake + NDK sysroot needed, ~5–10 min):

**Run the automated installer (installs dsh, applies patches, **

bash install.sh The installer is idempotent — re-running it skips already-applied patches and already-built artifacts. After install, `dsh` is usable directly: the installed `bin.js` shebang is patched with `--expose-internals` (so npm's `dsh` bin works in any shell), and a `dsh` alias is auto-appended to `~/.bashrc` (created if missing, or `~/.zshrc` for zsh) — your existing shell config is never

**How installation script work**

1. **Installs** `@deepseek-ai/dsh` globally. 2. **Applies the Android source patches** under [`patches/`](patches/) to the installed packages. 3. **Builds the native addons** (`koffi`, `node-pty`) against the Termux bionic sysroot — the build environment (node headers, `GYP_DEFINES`, the `common.gypi` fix) is prepared and the source patches are applied **before** anything compiles. 4. **Patches `k

## 🔗 链接

- [GitHub 仓库](https://github.com/Vengisk/deepseek-harness-termux)
- [完整 README](https://github.com/Vengisk/deepseek-harness-termux#readme)
- [返回deepseek-harness-termux所在分类](../clients.md)
