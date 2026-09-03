---
title: "dsh-scout"
description: "面向 DeepSeek Harness 的只读环境探测插件，为智能体提供运行环境、软件版本、系统资源、端口、服务、硬件及工作区信息。"
keywords: "dsh-scout, discovery, plugin, coding, deepseek harness, dsh"
---
# dsh-scout

> ⭐ **2** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 插件发现 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [omdsh-dev](https://github.com/omdsh-dev) | 更新时间 | 2026-08-14 |

## 一句话介绍

> 面向 DeepSeek Harness 的只读环境探测插件，为智能体提供运行环境、软件版本、系统资源、端口、服务、硬件及工作区信息。

## 详细介绍

A model-facing environment probe tool for **DeepSeek Harness**: on demand, the agent can learn the runtime environment (platform, shell, user, timezone…), which commands resolve on PATH, which software is installed and at what version, and how much CPU/memory/disk is available — without guessing or burning tool calls on slow discovery commands.

## 📦 安装

```bash
# from the public Harness source checkout:
cd /path/to/deepseek-harness
pnpm dsh plugin --profile web add /path/to/dsh-scout
```

## 🚀 快速开始

```bash
[environment]
platform: darwin (Darwin 24.5.0)
arch: arm64
hostname: dev-machine.local
user: developer
home: /Users/developer
cwd: /Users/developer/Projects/dsh-scout
node: v24.19.0
shell: /bin/zsh
timezone: Asia/Shanghai
locale: zh-CN
endianness: LE
pid: 1234
dsh home: /Users/developer/.dsh
```

## 📚 更多信息

**Install**

This package is a dsh **bundle**: it ships its own patch layer (`cordis.patch.yml`) and joins a profile's layer stack automatically once installed.

**Configuration**

Example patch row (in the profile's `cordis.patch.yml`, overriding the bundle row by id): name: '@deepseek-ai/dsh-tool-scout' config: softwareProbeTimeoutMs: 2000 softwareCacheTtlMs: 0 maxNames: 30

**Why there is no settings-page card**

The web GUI's "plugin configuration" section renders only plugins that ship a browser-side card (`settings.plugin.item` slot; today only the in-box `bash`/`agent-loop`/`web-search` cards). This package is deliberately a Host-side-only out-of-tree plugin: it does not appear in that section, and its configuration lives in the profile patch layer above — no harness-repo change is required to install,

## 🔗 链接

- [GitHub 仓库](https://github.com/omdsh-dev/dsh-scout)
- [完整 README](https://github.com/omdsh-dev/dsh-scout#readme)
- [返回dsh-scout所在分类](../plugins.md)
