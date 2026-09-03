---
title: "dsh-plugin-installer"
description: "Marketplace plugin that integrates DeepSeek Harness with the GitHub plugin ecosystem."
keywords: "dsh-plugin-installer, discovery, plugin, workflow, deepseek harness, dsh"
---
# dsh-plugin-installer

> ⭐ **6** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Plugin discovery |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [Toukaiteio](https://github.com/Toukaiteio) | Updated | 2026-08-16 |

## One-liner

> Marketplace plugin that integrates DeepSeek Harness with the GitHub plugin ecosystem.

## About

An in-app marketplace and Profile switcher for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). DSH Plugin Installer adds a **Plugin marketplace** tab to the official Web UI under **Settings → Plugins**. It discovers repositories from the GitHub `dsh-plugin` and `dsh` topics, verifies that a repository is a real DSH bundle, installs it at a pinned commit, and helps users open another Web Profile without leaving the UI. The project intentionally keeps the interface compact and newcomer-friendly. It uses the official Web UI slot and design-token system, with no separate administration page, emoji, or gradient backgrounds.

## ✨ Key Features

- Online discovery from GitHub `dsh-plugin` and `dsh` topics.
- Excludes the DeepSeek Harness host repository from plugin-marketplace results.
- Root `package.json` validation for `dsh.bundle.patch` before installation.
- Verified GitHub Release installs using the published `.tgz` build artifact whenever available; source installs are allowed only when the checked-in JavaScript e
- Optional Release version selection from the marketplace list; stable releases are preferred by default.
- Release archive SHA-256 verification when GitHub provides a digest.
- Installation into a selected DSH Profile.
- Installed-state detection from both GitHub dependency specs and package repository metadata.

## 📦 Install

```bash
dsh plugin --profile web add ./dsh-plugin-installer-<version>.tgz
dsh web
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add github:Toukaiteio/dsh-plugin-installer#<commit>
dsh web
```

## 📚 Learn more

**DSH Plugin Installer**

English | [简体中文](README.zh-CN.md) An in-app marketplace and Profile switcher for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). DSH Plugin Installer adds a **Plugin marketplace** tab to the official Web UI under **Settings → Plugins**. It discovers repositories from the GitHub `dsh-plugin` and `dsh` topics, verifies that a repository is a real DSH bundle, installs it at a pin

**Windows one-click installer**

On Windows, run the PowerShell installer directly. It downloads the latest stable GitHub Release, verifies its SHA-256 digest when available, keeps the archive under `DSH_HOME/plugin-archives/dsh-plugin-installer/` for future dependency resolution, installs it into the `web` Profile, and starts DSH Web: irm https://raw.githubusercontent.com/Toukaiteio/dsh-plugin-installer/main/scripts/Install-DshP

**macOS and Linux installer**

On macOS or Linux, download the Bash installer and run it. It follows the same release download, checksum verification, installation, and start flow as the Windows installer: curl --fail --location --remote-name https://raw.githubusercontent.com/Toukaiteio/dsh-plugin-installer/main/scripts/install-dsh-plugin-installer.sh bash ./install-dsh-plugin-installer.sh It requires `bash`, `curl`, and Node.j

**Manual installation**

Build or download the package archive from the [latest GitHub Release](https://github.com/Toukaiteio/dsh-plugin-installer/releases), then add it to the Web Profile you use: dsh plugin --profile web add ./dsh-plugin-installer-<version>.tgz dsh web For local development only, a source checkout can still be installed directly from a GitHub revision after the repository has been published. The checkou

## 🔗 Links

- [GitHub Repository](https://github.com/Toukaiteio/dsh-plugin-installer)
- [Full README](https://github.com/Toukaiteio/dsh-plugin-installer#readme)
- [Back to the Plugins list](../plugins.md)
