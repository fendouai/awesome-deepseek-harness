---
title: "dsh-vault"
description: "Encrypted credential vault for DeepSeek Harness — AES-256-GCM + TOTP, model tools + Settings UI"
keywords: "dsh-vault, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-vault

> ⭐ **7** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 7 | Status | ✅ active |
| Author | [Ox0400](https://github.com/Ox0400) | Updated | — |

## One-liner

> Encrypted credential vault for DeepSeek Harness — AES-256-GCM + TOTP, model tools + Settings UI

## About

**English** · [简体中文](./README.zh.md) [GitHub](https://github.com/feiyang-dev/dsh-vault) · [npm](https://www.npmjs.com/package/@feiyang666/dsh-vault) · MIT License **A community plugin for DeepSeek Harness** — auto backup → wipe detection → one-click restore. Backs up chat history, workspace data, settings, and credentials to a safe location outside `~/.dsh`. --- ---

## 📦 Install

```bash
# Prerequisite: install dsh (npm install -g @deepseek-ai/dsh)
dsh plugin --profile web add @feiyang666/dsh-vault
```

## 🚀 Quick Start

```bash
# 1. Install into the profile (equivalent to the official bundle mechanism)
npm install --prefix "$HOME/.dsh/profiles/web" @feiyang666/dsh-vault

# 2. Register the bundle in the profile's package.json (the dsh.vault row mounts automatically via cordis.patch.yml)
#    Or use your desktop app's plugin manager
```

## 📚 Learn more

**Recommended Installation**

> Either method works and is equivalent. **We recommend the desktop app** — fully graphical, no command line needed.

**Prerequisite: install dsh (npm install -g @deepseek-ai/dsh)**

dsh plugin --profile web add @feiyang666/dsh-vault This plugin is a standard Cordis bundle plugin installed via npm and mounted into a dsh profile:

**Usage 2: `backup_vault` tool (TUI / Web universal)**

The plugin registers the `backup_vault` model tool — just tell the assistant "back me up / check backup status / restore chat history from the latest backup / delete that old backup":

## 🔗 Links

- [GitHub Repository](https://github.com/Ox0400/dsh-vault)
- [Full README](https://github.com/Ox0400/dsh-vault#readme)
- [Back to the Plugins list](../plugins.md)
