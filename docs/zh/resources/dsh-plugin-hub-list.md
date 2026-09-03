---
title: "dsh-plugin-hub"
description: "DeepSeek Harness community plugin registry with evidence-based screening"
keywords: "dsh-plugin-hub, registry, awesome-list, coding, deepseek harness, dsh"
---
# dsh-plugin-hub

> ⭐ **17** · ✅ 活跃 · 精选列表 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 精选列表 | 分类 | 注册表 |
| 星数 | ⭐ 17 | 状态 | ✅ 活跃 |
| 作者 | [cclank](https://github.com/cclank) | 更新时间 | 2026-08-21 |

## 一句话介绍

> DeepSeek Harness community plugin registry with evidence-based screening

## 详细介绍

DeepSeek Harness 的插件生态增长很快，但仓库描述、安装命令和真实权限边界经常散落在不同位置。DSH Plugin Hub 将这些公开证据汇总成一个可搜索目录，帮助用户在安装前先确认： - 项目是否真的声明了 `dsh.bundle`、`dsh.plugin`、`dsh.profile` 或 `dsh.client`； - 安装命令是否绑定到完成静态检查的不可变 Git commit； - 仓库是否活跃、是否有许可证和锁文件； - 是否存在生命周期脚本、网络访问、文件写入、凭据读取或动态代码执行信号； - 当前结果来自自动发现、社区精选，还是离线快照。 本站是独立社区项目，与 DeepSeek 官方没有隶属关系。

## ✨ 核心特性

- 项目是否真的声明了 `dsh.bundle`、`dsh.plugin`、`dsh.profile` 或 `dsh.client`；
- 安装命令是否绑定到完成静态检查的不可变 Git commit；
- 仓库是否活跃、是否有许可证和锁文件；
- 是否存在生命周期脚本、网络访问、文件写入、凭据读取或动态代码执行信号；
- 当前结果来自自动发现、社区精选，还是离线快照。

## 📦 安装

```bash
git clone https://github.com/cclank/dsh-plugin-hub.git
cd dsh-plugin-hub
npm ci
npm run data:sync
npm run dev
```

## 🚀 快速开始

```bash
GITHUB_TOKEN=github_pat_xxx npm run data:sync
```

## 🔗 链接

- [GitHub 仓库](https://github.com/cclank/dsh-plugin-hub)
- [完整 README](https://github.com/cclank/dsh-plugin-hub#readme)
- [返回dsh-plugin-hub所在分类](../awesome-lists.md)
