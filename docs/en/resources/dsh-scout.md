---
title: "dsh-scout"
description: "面向 DeepSeek Harness 的只读环境探测插件，为智能体提供运行环境、软件版本、系统资源、端口、服务、硬件及工作区信息。"
keywords: "dsh-scout, discovery, plugin, coding, deepseek harness, dsh"
---
# dsh-scout

> ⭐ **2** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Plugin discovery |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | 2026-08-14 |

## One-liner

> 面向 DeepSeek Harness 的只读环境探测插件，为智能体提供运行环境、软件版本、系统资源、端口、服务、硬件及工作区信息。

## About

A model-facing environment probe tool for **DeepSeek Harness**: on demand, the agent can learn the runtime environment (platform, shell, user, timezone…), which commands resolve on PATH, which software is installed and at what version, and how much CPU/memory/disk is available — without guessing or burning tool calls on slow discovery commands.

## 📦 Install

```bash
# from the public Harness source checkout:
cd /path/to/deepseek-harness
pnpm dsh plugin --profile web add /path/to/dsh-scout
```

## 🚀 Quick Start

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

## 📚 Learn more

**Install**

This package is a dsh **bundle**: it ships its own patch layer (`cordis.patch.yml`) and joins a profile's layer stack automatically once installed.

**Configuration**

Example patch row (in the profile's `cordis.patch.yml`, overriding the bundle row by id): name: '@deepseek-ai/dsh-tool-scout' config: softwareProbeTimeoutMs: 2000 softwareCacheTtlMs: 0 maxNames: 30

**Why there is no settings-page card**

The web GUI's "plugin configuration" section renders only plugins that ship a browser-side card (`settings.plugin.item` slot; today only the in-box `bash`/`agent-loop`/`web-search` cards). This package is deliberately a Host-side-only out-of-tree plugin: it does not appear in that section, and its configuration lives in the profile patch layer above — no harness-repo change is required to install,

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-scout)
- [Full README](https://github.com/omdsh-dev/dsh-scout#readme)
- [Back to the Plugins list](../plugins.md)
