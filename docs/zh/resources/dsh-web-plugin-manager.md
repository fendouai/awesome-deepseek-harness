---
title: "dsh-web-plugin-manager"
description: "Web UI 中一键管理 DSH 插件：查看、实时启停、安装/卸载、环境管理、插件市场。"
keywords: "dsh-web-plugin-manager, discovery, plugin, ui, workflow, deepseek harness, dsh"
---
# dsh-web-plugin-manager

> ⭐ **62** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 插件发现 |
| 星数 | ⭐ 62 | 状态 | ✅ 活跃 |
| 作者 | [LX2000WASD](https://github.com/LX2000WASD) | 更新时间 | 2026-08-20 |

## 一句话介绍

> Web UI 中一键管理 DSH 插件：查看、实时启停、安装/卸载、环境管理、插件市场。

## 详细介绍

[中文](./README.md) | [English](./README.en.md) 在 Web UI 中一键管理 DeepSeek Harness (DSH) 插件：查看、实时启停、安装/卸载、更新检测、健康检查（依赖/冲突/兼容性分析）、环境管理、插件市场。bundle 与非 bundle 插件全覆盖。

## 📦 安装

```bash
# 方式一（推荐）：从 npm 安装（务必带 @latest）
dsh plugin --profile <name> add dsh-web-plugin-manager@latest

# 方式二：从源码构建
cd /path/to/dsh-web-plugin-manager
pnpm install && pnpm run build
dsh plugin --profile <name> add .
```

## 🚀 快速开始

```bash
# 命令方式（推荐）：升级到最新版（重写 specifier，质量门 + 失败自动回滚到旧版本）
dshpm update dsh-web-plugin-manager --profile NAME
# 等价命令（pnpm 语义）
dsh plugin --profile NAME add dsh-web-plugin-manager@latest
```

## 🔗 链接

- [GitHub 仓库](https://github.com/LX2000WASD/dsh-web-plugin-manager)
- [完整 README](https://github.com/LX2000WASD/dsh-web-plugin-manager#readme)
- [返回dsh-web-plugin-manager所在分类](../plugins.md)
