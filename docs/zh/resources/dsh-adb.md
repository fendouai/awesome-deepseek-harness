---
title: "dsh-adb"
description: "ADB device & bench operations: device discovery, structured logcat (background streaming), apk install, file pull/push, dumpsys performance snapshots."
keywords: "dsh-adb, discovery, plugin, coding, deepseek harness, dsh"
---
# dsh-adb

> ⭐ **2** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 插件发现 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [SamXiaBing](https://github.com/SamXiaBing) | 更新时间 | 2026-08-21 |

## 一句话介绍

> ADB device & bench operations: device discovery, structured logcat (background streaming), apk install, file pull/push, dumpsys performance snapshots.

## 详细介绍

Give DSH agents direct control over Android devices and automotive bench rigs: device discovery, structured logcat, APK install, file pull/push, and performance snapshots. Built for on-vehicle and bench debugging workflows — generic within the domain (no Unity, no vendor protocol lock-in).

## 📦 安装

```bash
dsh plugin --profile web add dsh-adb
```

## 🚀 快速开始

```bash
1. adb_watch_crash (watch for new crash)
2. → crash detected → adb_crash_report (full crash scene: buffer + dropbox + process + memory)
3.                    → adb_screenshot (screen state at crash time)
```

## 📚 更多信息

**Install**

dsh plugin --profile web add dsh-adb Or install directly from GitHub: `dsh plugin --profile web add github:SamXiaBing/dsh-adb`

**Usage: adb_watch_crash (Crash Watchdog)**

Watch the device's crash buffer for **new** real crashes. On start, it reads the current buffer and remembers every existing crash signature (seed), so only crashes that appear *after* the watch begins are reported. Boot markers (`mtk-brm-*`) are not crashes and are ignored. **Foreground mode** (default) — blocks until a new crash appears or the budget expires: // Agent calls: { "name": "adb_watch

**Configuration**

Set the `config` block in `cordis.patch.yml` (or a profile patch): name: dsh-adb config: adbPath: C:\Users\me\AppData\Local\Android\Sdk\platform-tools\adb.exe defaultSerial: emulator-5554 timeoutMs: 30000

## 🔗 链接

- [GitHub 仓库](https://github.com/SamXiaBing/dsh-adb)
- [完整 README](https://github.com/SamXiaBing/dsh-adb#readme)
- [返回dsh-adb所在分类](../plugins.md)
