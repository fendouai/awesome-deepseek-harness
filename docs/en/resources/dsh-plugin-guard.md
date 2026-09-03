---
title: "dsh-plugin-guard"
description: "Install safety net for DeepSeek Harness: pre-install snapshots, one-click/automatic rollback, guarded boot, and incident reports that auto-trigger agent analysis. 中文: DeepSeek Harness 插件安装安全网（安装前自动快照、一键/自动回退、守护启动、事故报告自动触发 Agent 分析）。"
keywords: "dsh-plugin-guard, vision, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-plugin-guard

> ⭐ **28** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 28 | Status | ✅ active |
| Author | [lxzy-7](https://github.com/lxzy-7) | Updated | 2026-08-18 |
| Subcategory | 👁️ Vision tools | Capabilities | coding, multi-agent |

## One-liner

> Install safety net for DeepSeek Harness: pre-install snapshots, one-click/automatic rollback, guarded boot, and incident reports that auto-trigger agent analysis. 中文: DeepSeek Harness 插件安装安全网（安装前自动快照、一键/自动回退、守护启动、事故报告自动触发 Agent 分析）。

## About

A bad plugin install can leave the app unable to boot, and fixing it by hand usually means digging through config files. This plugin automates the whole chain: Install a plugin (any method) │ tools.guard hook: automatic snapshot BEFORE the install (in-process) ▼ Guarded boot (boot-guard script) │ snapshot before boot → start dsh web → health check ├─ healthy ─────────────────────────────► passes through untouched └─ unhealthy ─► auto-rollback to last good snapshot → retry once → write an incident report + set a pending marker → the next session's prompt tells the agent to analyze it → after fixing, call `incident_resolved` to clear the marker

## 📦 Install

```bash
# From GitHub source (current):
dsh plugin --profile web add github:lxzy-7/dsh-plugin-guard

# From the tarball stored in the repo:
dsh plugin --profile web add https://raw.githubusercontent.com/lxzy-7/dsh-plugin-guard/main/dist/dsh-plugin-guard-0.3.2.tgz
```

## 🚀 Quick Start

```bash
@echo off
set DSH_HOME=%~dp0.dsh-home
cd /d %~dp0
powershell -NoProfile -ExecutionPolicy Bypass -File node_modules\dsh-plugin-guard\scripts\boot-guard.ps1
```

## 📚 Learn more

**Usage**

**Settings panel — 备份管理 (Backup Manager).** In the web UI, open **设置 (Settings) → 备份管理**: per-environment snapshot lists, **load a specific backup**, **create a manual snapshot**, and **set how many snapshots each environment keeps (minimum 2)**. Since v0.3.0 the plugin also registers a **设置 → 插件 → 插件配置** settings card (rc.7 plugin-owned settings surface): it edits the same keep-count through the 

**Configuration**

`$DSH_HOME/guard/config.json` (auto-created on first write; all optional): { "keepSnapshots": 10, "port": 3080 } Every path is anchored at `$DSH_HOME` (defaults to `~/.dsh` when the env var is unset): $DSH_HOME/rollbacks/<profile>/<stamp>/ snapshots (5 config files + manifest.json) $DSH_HOME/guard/logs/ boot/server logs, incident reports, last-boot.txt $DSH_HOME/guard/pending-incident.json pending

**或从仓库里的安装包：**

dsh plugin --profile web add https://raw.githubusercontent.com/lxzy-7/dsh-plugin-guard/main/dist/dsh-plugin-guard-0.3.2.tgz 重启 `dsh web`。这是标准 **bundle 插件**：加入 profile 层栈自动生效。(发布到 npm 后 `dsh plugin --profile web add dsh-plugin-guard` 也可用。) **启用守护启动(强烈推荐)：** 把启动命令改为经过 `scripts/boot-guard.ps1`(Windows) 或 `scripts/boot-guard.sh`(macOS/Linux)，而不是直接跑 `dsh web`。Windows 启动器示例： @echo off set DSH_HOME=%~dp0

**使用**

**设置面板 — 备份管理。** 网页界面里打开 **设置 → 备份管理**：按环境列出快照、**加载指定备份**、**手动存档**、**设置每个环境保留的快照数量(最少 2)**。v0.3.0 起插件还会注册 **设置 → 插件 → 插件配置** 设置卡片（rc.7 插件自有设置表面）：通过 harness 的 `settings` 服务编辑同一保留数量（schema 校验 + revision 冲突保护），与备份管理面板、CLI 通过 `config.json` 保持同步。 **Agent 工具**(profile 内每个会话都会注册)： **CLI**(`dsh-guard`，应用起不来时也能用)： snapshot [--profile X] [--tag T] [--reason R] [--force] list [--profile X] rollback [--profil

## 🔗 Links

- [GitHub Repository](https://github.com/lxzy-7/dsh-plugin-guard)
- [Full README](https://github.com/lxzy-7/dsh-plugin-guard#readme)
- [Back to the Plugins list](../plugins.md)
