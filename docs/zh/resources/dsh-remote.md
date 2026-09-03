---
title: "dsh-remote"
description: "远程工作区：SSH 连接远程主机，用 rw_pick_workspace/rw_read_file/rw_exec 等工具远程操作。"
keywords: "dsh-remote, developer, plugin, automation, files, deepseek harness, dsh"
---
# dsh-remote

> ⭐ **31** · ✅ 活跃 · 插件 · 近期 ⬆️ +3

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 31 | 状态 | ✅ 活跃 |
| 作者 | [flymysql](https://github.com/flymysql) | 更新时间 | 2026-08-21 |
| 子分类 | 📁 文件与导入 | 能力 | automation, files |

## 一句话介绍

> 远程工作区：SSH 连接远程主机，用 rw_pick_workspace/rw_read_file/rw_exec 等工具远程操作。

## 详细介绍

**Remote-work assistant for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (DSH).** Manage several SSH machines, then pick a **remote workspace** (or a **local** one) and let the agent operate right there without leaving the harness — listing files, reading code, running builds & commands over the remote host, and keeping that remote directory mirrored into a real local workspace object. The harness Web UI intentionally binds `127.0.0.1` (the CLI rejects `--host 0.0.0.0` for safety). This plugin goes the other way: **you connect out** to the machines you maintain, pick a workspace, and work in it through the normal DSH workspace + agent fs flows — no changes to `dsh-workspace` or the harness core.

## ✨ 核心特性

- **Multi-machine SSH** — save any number of hosts (`host`/`port`/`user` + **private key** or **password**). Passwords are stored locally and never shown back in 
- **`~/.ssh/config` import** — the Settings page lists your `Host` aliases; one click fills the form (path reference only, the plugin never reads key material).
- **Two-tab workspace picker** (fills the native "Add workspace" flow):
- **Git Bash default terminal (Windows remotes)** — the remote platform is auto-detected (`cmd /c ver`, plus an `uname -s` MINGW/MSYS probe as fallback); on Windo
- **Windows path auto-conversion** — typing `C:\Users\dev\project` (or `C:/…`, `/c/…`, `/C:/…`) is normalized underneath to the Git Bash form `/c/Users/dev/projec
- **Bidirectional SFTP sync, conflict-aware** — `rw_sync` (remote → mirror) and `rw_push` (mirror → remote) are **three-way** (remote vs local vs last-synced snap
- **Model tools** — 20 tools, all Windows/POSIX portable via SFTP: `rw_info`, `rw_connect` (with `save`), `rw_pick_workspace`, `rw_list_dir` (size+mtime), `rw_sta
- **Port forwarding panel** — create/start/stop/remove **local** (`127.0.0.1:port → remote`) and **reverse** (`remote → local`) tunnels in the Settings page or vi

## 📦 安装

```bash
dsh plugin add dsh-remote            # add the bundle
```

## 🚀 快速开始

```bash
# Example only — use values for your own machine.
- id: dsh-remote
  name: dsh-remote
  config:
    host: 203.0.113.10   # or your real host / hostname
    port: 22
    username: dev
    privateKeyPath: ~/.ssh/id_rsa
    # or password: '…'
    workspace: ~/project
```

## 📚 更多信息

**Install**

dsh plugin add dsh-remote # add the bundle One command installs everything: since **v0.7.2** the sidebar ([dsh-better-sidebar](https://www.npmjs.com/package/dsh-better-sidebar)) is a hard dependency and is mounted automatically — the 🌐 remote-file explorer and remote file viewer show up in the sidebar with no extra step. If you already have the sidebar installed on its own, the embedded copy backs

**Quick start**

1. **Add a machine** — Settings → 远程工作区 → add host/port/user + key or password → (optional) set it current. 2. **Open a workspace** — click **Add workspace** in the sidebar / conversation: - **本机** → system folder chooser (or type a local path) → local workspace. On hosts without a usable OS dialog (DSH Desktop's browse backend, headless SSH hosts without zenity/kdialog) the in-app directory brows

**Example only — use values for your own machine.**

name: dsh-remote config: host: 203.0.113.10 # or your real host / hostname port: 22 username: dev privateKeyPath: ~/.ssh/id_rsa # or password: '…' workspace: ~/project If `host` is empty the plugin starts disconnected and you configure machines in the UI.

**CLI quick reference**

Installing and driving DSH may live in different shells, so both the `dsh` binary and the `npx` form are shown. Always tell DSH **which profile** to use with `--profile <name>` (usually `web`).

## 🔗 链接

- [GitHub 仓库](https://github.com/flymysql/dsh-remote)
- [完整 README](https://github.com/flymysql/dsh-remote#readme)
- [返回dsh-remote所在分类](../plugins.md)
