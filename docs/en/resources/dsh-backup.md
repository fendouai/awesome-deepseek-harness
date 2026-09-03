---
title: "dsh-backup"
description: "Automated backups of DSH sessions, config and custom directories — scheduled or manual, packed as tgz with rotation"
keywords: "dsh-backup, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-backup

> ⭐ **1** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [a903067276-rgb](https://github.com/a903067276-rgb) | Updated | — |

## One-liner

> Automated backups of DSH sessions, config and custom directories — scheduled or manual, packed as tgz with rotation

## About

**Your entire DeepSeek Harness (DSH) workspace lives in one folder: `~/.dsh`. One failed upgrade, one accidental delete, one new laptop — without a backup, sessions, settings and skills are all gone. dsh-backup gives them back with one command.** dsh plugin --profile web add @xiaoyuyu6420/dsh-backup # install

## 📦 Install

```bash
dsh plugin --profile web add @xiaoyuyu6420/dsh-backup   # install
# restart dsh web, then type:
/backup                                                  # → a verified archive lands in ~/Desktop/dsh-backups/
```

## 🚀 Quick Start

```bash
备份完成: dsh-20260826-195150036.tar.gz
sha256: 8f9ae6322ef782d21554981cf4547220d5bb3e64d7964a883317415ad54e3cbb
轮换删除 0 份（保留 7 份）
```

## 📚 Learn more

**Install**

Requires macOS / Linux / Windows 10+ (ships `tar`) and DSH `0.1.1-rc.2` or compatible. dsh plugin --profile web add @xiaoyuyu6420/dsh-backup

**Quickstart**

1. Install (above) and restart `dsh web` 2. Type `/backup` 3. Done — the archive lands in `~/Desktop/dsh-backups/`, timestamped, with a `.sha256` next to it Want it on a schedule? `/backup auto 12` (every 12 hours; `off` stops it, `status` checks it).

**FAQ**

**Are my API keys / credentials inside the archive?** No. Known credential files are redacted before archiving; the plaintext stays in a local vault that never leaves the machine. Restoring puts them back. **What exactly gets backed up?** Everything under `~/.dsh` — sessions, settings, skills, plugin config — minus your exclude patterns and `node_modules`. **I messed up `~/.dsh` and now `dsh` won'

## 🔗 Links

- [GitHub Repository](https://github.com/a903067276-rgb/dsh-backup)
- [Full README](https://github.com/a903067276-rgb/dsh-backup#readme)
- [Back to the Plugins list](../plugins.md)
