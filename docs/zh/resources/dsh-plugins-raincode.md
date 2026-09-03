---
title: "dsh-plugins-raincode"
description: "dsh plugin: DeepSeek Harness 的模型层 = raincode(模型池/缓存/重试) + /skills 浏览"
keywords: "dsh-plugins-raincode, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-plugins-raincode

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [rainforest888](https://github.com/rainforest888) | 更新时间 | 2026-08-20 |

## 一句话介绍

> dsh plugin: DeepSeek Harness 的模型层 = raincode(模型池/缓存/重试) + /skills 浏览

## 详细介绍

Make **raincode** the model layer of **DeepSeek Harness (dsh)**: a cheap model pool with StablePrefix prompt caching, retries and failover, driven by a local OpenAI-compatible gateway (Rust). This repository is the **dsh plugin monorepo** for raincode. It ships that capability as two independently publishable dsh plugins that share the adapter core in `packages/core`.

## 📦 安装

```bash
dsh plugin --profile web add dsh-plugins-raincode-skill
dsh plugin --profile web add dsh-plugins-raincode-routing
```

## 🚀 快速开始

```bash
- insert:
    - id: raincode-skill
      name: dsh-plugins-raincode-skill
      config:
        baseURL: http://127.0.0.1:8787
        apiKeyEnv: RAINCODE_API_KEY
    - id: raincode-routing
      name: dsh-plugins-raincode-routing
      config:
        baseURL: http://127.0.0.1:8787
        apiKeyEnv: RAINCODE_API_KEY
```

## 📚 更多信息

**Architecture**

The plugins are the "mouth": they translate dsh's `GenerateOptions` into the OpenAI wire format and stream chunks back. The raincode gateway (Rust) is the "brain": it owns profile selection, prompt caching, retries and failover. The plugins hold no model logic.

**Quick start**

1. Install the raincode CLI (`>= 0.1.0`): `cargo install --path crates/rc-cli` (or use `./install.sh`). 2. Configure your model pool: `raincode setup` (writes `~/.raincode/profiles.toml`). 3. Start the gateway: `raincode proxy --port 8787`, then verify `curl http://127.0.0.1:8787/health` → `{"ok":true,"service":"raincode-gateway"}`.

**Install in dsh**

dsh plugin --profile web add dsh-plugins-raincode-skill dsh plugin --profile web add dsh-plugins-raincode-routing Then add a row for each plugin to the profile's patch layer (`~/.dsh/profiles/web/cordis.patch.yml`): - id: raincode-skill name: dsh-plugins-raincode-skill config: baseURL: http://127.0.0.1:8787 apiKeyEnv: RAINCODE_API_KEY - id: raincode-routing name: dsh-plugins-raincode-routing confi

## 🔗 链接

- [GitHub 仓库](https://github.com/rainforest888/dsh-plugins-raincode)
- [完整 README](https://github.com/rainforest888/dsh-plugins-raincode#readme)
- [返回dsh-plugins-raincode所在分类](../plugins.md)
