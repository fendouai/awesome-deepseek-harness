---
title: "dsh-plugin-hub"
description: "DeepSeek Harness community plugin registry with evidence-based screening"
keywords: "dsh-plugin-hub, registry, awesome-list, coding, deepseek harness, dsh"
---
# dsh-plugin-hub

> ⭐ **17** · ✅ active · awesome-list · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 17 | Status | ✅ active |
| Author | [cclank](https://github.com/cclank) | Updated | 2026-08-21 |

## One-liner

> DeepSeek Harness community plugin registry with evidence-based screening

## About

DeepSeek Harness 的插件生态增长很快，但仓库描述、安装命令和真实权限边界经常散落在不同位置。DSH Plugin Hub 将这些公开证据汇总成一个可搜索目录，帮助用户在安装前先确认： - 项目是否真的声明了 `dsh.bundle`、`dsh.plugin`、`dsh.profile` 或 `dsh.client`； - 安装命令是否绑定到完成静态检查的不可变 Git commit； - 仓库是否活跃、是否有许可证和锁文件； - 是否存在生命周期脚本、网络访问、文件写入、凭据读取或动态代码执行信号； - 当前结果来自自动发现、社区精选，还是离线快照。 本站是独立社区项目，与 DeepSeek 官方没有隶属关系。

## ✨ Key Features

- 项目是否真的声明了 `dsh.bundle`、`dsh.plugin`、`dsh.profile` 或 `dsh.client`；
- 安装命令是否绑定到完成静态检查的不可变 Git commit；
- 仓库是否活跃、是否有许可证和锁文件；
- 是否存在生命周期脚本、网络访问、文件写入、凭据读取或动态代码执行信号；
- 当前结果来自自动发现、社区精选，还是离线快照。

## 📦 Install

```bash
git clone https://github.com/cclank/dsh-plugin-hub.git
cd dsh-plugin-hub
npm ci
npm run data:sync
npm run dev
```

## 🚀 Quick Start

```bash
GITHUB_TOKEN=github_pat_xxx npm run data:sync
```

## 🔗 Links

- [GitHub Repository](https://github.com/cclank/dsh-plugin-hub)
- [Full README](https://github.com/cclank/dsh-plugin-hub#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
