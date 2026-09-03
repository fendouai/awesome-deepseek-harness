---
title: "dsh-session-health"
description: "Frame-level diagnostics for multi-frame zstd session files: torn/corrupted/empty session detection, zero-dependency read-only."
keywords: "dsh-session-health, memory, plugin, observability, files, deepseek harness, dsh"
---
# dsh-session-health

> ⭐ **8** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 8 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | 2026-08-21 |
| Subcategory | 🔍 Context audit | Capabilities | observability, files |

## One-liner

> Frame-level diagnostics for multi-frame zstd session files: torn/corrupted/empty session detection, zero-dependency read-only.

## About

[English](README.en.md) DSH 会话健康检查插件 —— 对 `$DSH_HOME/sessions` 下的**多帧 zstd 会话文件**做帧级扫描诊断（torn / 损坏 / 空会话 / stray 文件），输出健康报告与清理建议。**只读**：绝不修改或删除任何文件。 仓库：[https://github.com/omdsh-dev/dsh-session-health](https://github.com/omdsh-dev/dsh-session-health)（public）

## ✨ Key Features

- **只读保证**：绝不修改/删除任何文件（测试覆盖"扫描后文件字节数不变"，见 files.spec SH-06 用例）
- **路径围栏**：session id 严格目录名白名单（防 `../` 穿越）；绝对路径与最终文件均做 `fs.realpath` 真实路径 containment（防符号链接/junction 逃逸）；枚举用 lstat 拒绝 symlink
- **零业务依赖**：zstd 帧扫描器为独立实现（DataView 读字节，RFC 8878 结构，与官方 `scanZstdFrames` 差分一致）
- **深度分析可选**：`deep: true` 时动态 import 官方解码器；解析失败明确降级 `deep: "unavailable"`，绝不静默
- 输入范围固定（sessions 目录），无网络、无执行面

## 📦 Install

```bash
# 交互式（web）profile
dsh plugin --profile web add github:omdsh-dev/dsh-session-health
# 一次性任务（headless）profile —— dsh run 默认使用 headless
dsh plugin --profile headless add github:omdsh-dev/dsh-session-health
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add dsh-session-health-*.tgz
```

## 📚 Learn more

**示例**

session_health { action: "scan" } → {"root":"C:\\Users\\admin\\.dsh\\sessions","scanned":39,"errors":{...},"suspicious":{...},"suggestions":[...]} session_health { action: "file", path: "session-abc123", deep: true } → 单文件报告（含事件分布与中断检测）

**安装**

DSH 0.1.2-rc.1（npm）下，插件通过 `dsh plugin --profile <profile> add <source>` 安装，source 支持 GitHub 仓库或 npm pack tarball。

**从 npm pack tarball 安装**

`npm pack` 产物可直接作为 source 安装： dsh plugin --profile web add dsh-session-health-*.tgz 包内 `dsh.bundle.patch` 会在安装后自动把插件加入 profile 的 layer stack（row id：`tool-session-health`）。插件缺失的 peer 依赖（`@deepseek-ai/cordis`、`@deepseek-ai/dsh-tools`）由 profile 的 healed `profiles/node_modules` 回退安装提供。 > ⚠️ web 与 headless 是**不同 profile**：web 安装不会自动覆盖 headless；`dsh run` 默认使用 headless profile。Windows 路径使用正斜杠（`C:/...`）。

**旧场景：monorepo / 本地路径安装**

monorepo 方式已标注为旧场景（本地 junction/symlink、手动编辑 profile 层、不支持 GitHub/tarball source 的旧快照）： dsh plugin --profile web add "C:/path/to/dsh-session-health"

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-session-health)
- [Full README](https://github.com/omdsh-dev/dsh-session-health#readme)
- [Back to the Plugins list](../plugins.md)
