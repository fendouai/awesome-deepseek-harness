---
title: "ikanban"
description: "Monorepo for the iKanban browser-surface fork for DeepSeek Harness."
keywords: "ikanban, browser, integration, coding, deepseek harness, dsh"
---
# ikanban

> ⭐ **12** · ✅ 活跃 · 集成 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 浏览器控制 |
| 星数 | ⭐ 12 | 状态 | ✅ 活跃 |
| 作者 | [isomoes](https://github.com/isomoes) | 更新时间 | 2026-08-21 |

## 一句话介绍

> Monorepo for the iKanban browser-surface fork for DeepSeek Harness.

## 详细介绍

[English](./README.en.md) | 简体中文 iKanban 是一个面向键盘操作、基于 [DeepSeek Harness](https://github.com/deepseek-ai/DeepSeek-Harness) 的多智能体编码工作空间。它专为跨项目地驱动、审查和协调并行智能体工作而构建，将会话管理、差异审查和项目感知导航集于一处。 本 monorepo 包含 iKanban DSH bundle，以及由 iKanban 和 IPaper 共同使用、公开发布的产品中立浏览器软件包。

## ✨ 核心特性

- [`@isomoes/dsh-ikanban`](packages/ikanban) - 公开发布的 iKanban DSH bundle、编码预设、产品组合配置和品牌
- [`@isomoes/dsh-web-ui`](packages/web-ui) - 与 IPaper 共用、公开发布的产品中立浏览器插件界面和 Vite shell

## 📦 安装

```bash
npm install -g @deepseek-ai/dsh --registry=https://registry.npmjs.org
```

## 🚀 快速开始

```bash
dsh plugin --profile ikanban add @isomoes/dsh-ikanban @isomoes/dsh-web-ui --registry=https://registry.npmjs.org
```

## 📚 更多信息

**1. 安装 DSH**

首先通过 npm 全局安装 DeepSeek Harness CLI： npm install -g @deepseek-ai/dsh --registry=https://registry.npmjs.org 中国大陆用户可以将命令中的 npm 官方 registry 替换为国内镜像，例如 `https://registry.npmmirror.com`。镜像同步可能存在延迟；如果需要最新发布的版本，请使用官方地址 `https://registry.npmjs.org`。

**2. 安装 iKanban**

将已发布的 iKanban bundle 和共享 Web UI 安装到 `ikanban` profile 中。如果该 profile 尚不存在，`dsh plugin` 命令会自动创建： dsh plugin --profile ikanban add @isomoes/dsh-ikanban @isomoes/dsh-web-ui --registry=https://registry.npmjs.org `@isomoes/dsh-web-ui` 必须是 profile 的直接依赖，因为 Cordis 从 profile 根目录解析浏览器 loader entry；它不会加入 `dsh.profile.bundles`，组合补丁仍然只由 `@isomoes/dsh-ikanban` 提供。这里的 `--registry` 同样可以替换为国内镜像；需要最新 iKanban 版本时请使用

## 🔗 链接

- [GitHub 仓库](https://github.com/isomoes/ikanban)
- [完整 README](https://github.com/isomoes/ikanban#readme)
- [返回ikanban所在分类](../integrations.md)
