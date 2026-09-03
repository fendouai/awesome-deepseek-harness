---
title: "dsh-explain"
description: "本地优先学习模式：跨会话全局学习线程、按来源讲解、ExplainContext、压缩与可诊断设置。"
keywords: "dsh-explain, learning, tutorial, context, deepseek harness, dsh"
---
# dsh-explain

> ⭐ **11** · ✅ 活跃 · 教程 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 教程 | 分类 | 学习 |
| 星数 | ⭐ 11 | 状态 | ✅ 活跃 |
| 作者 | [yuezengwu](https://github.com/yuezengwu) | 更新时间 | 2026-08-20 |

## 一句话介绍

> 本地优先学习模式：跨会话全局学习线程、按来源讲解、ExplainContext、压缩与可诊断设置。

## 详细介绍

The 28-second preview runs against real assembled DSH Web `0.1.2-alpha.5` with deterministic, private fixture data. [Watch the higher-quality MP4](docs/assets/dsh-explain-demo.mp4) or read the [recording contract](docs/DEMO.md).

## 📦 安装

```bash
npx @deepseek-ai/dsh@0.1.2-alpha.5 plugin --profile web add github:yuezengwu/dsh-explain
npx @deepseek-ai/dsh@0.1.2-alpha.5 --profile web
```

## 🚀 快速开始

```bash
pnpm install
DSH_SOURCE_DIR=/absolute/path/to/dsh pnpm dsh:link
DSH_SOURCE_DIR=/absolute/path/to/dsh pnpm dsh:link:check
pnpm typecheck
pnpm test
DSH_SOURCE_DIR=/absolute/path/to/dsh pnpm test:web
DSH_SOURCE_DIR=/absolute/path/to/dsh pnpm test:m6
pnpm build
```

## 📚 更多信息

**Quick start**

Current `main` targets DSH `0.1.2-alpha.5`: npx @deepseek-ai/dsh@0.1.2-alpha.5 plugin --profile web add github:yuezengwu/dsh-explain npx @deepseek-ai/dsh@0.1.2-alpha.5 --profile web Open **Settings → Learning**, choose an auxiliary provider and model, enable learning mode, and save. Explain observes only future completed top-level turns; it does not scan existing history. Git-hosted plugins build 

## 🔗 链接

- [GitHub 仓库](https://github.com/yuezengwu/dsh-explain)
- [完整 README](https://github.com/yuezengwu/dsh-explain#readme)
- [返回dsh-explain所在分类](../tutorials.md)
