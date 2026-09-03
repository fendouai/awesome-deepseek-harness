---
title: "awesome-deepseek-harness (libukai)"
description: "Ultimate guide: quick start, resources, curated plugins and practical tools."
keywords: "awesome-deepseek-harness (libukai), registry, awesome-list, search, learning, deepseek harness, dsh"
---
# awesome-deepseek-harness (libukai)

> ⭐ **175** · ✅ active · awesome-list · ⬆️ +12 recently

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 175 | Status | ✅ active |
| Author | [libukai](https://github.com/libukai) | Updated | 2026-08-21 |

## One-liner

> Ultimate guide: quick start, resources, curated plugins and practical tools.

## About

[DeepSeek Harness](https://deepseek.com/harness/)（简称 DSH 或 `dsh`）是 DeepSeek AI 开源的 Agent Harness 项目。它基于 [Cordis](https://github.com/cordiverse/cordis)，采用 **Everything is a Plugin（一切皆插件）** 的架构：模型适配器、工具、会话日志、界面和 Agent Loop 都可以通过插件树组合与替换。 当前核验到的官方 GitHub 开发者预览版为 [`0.1.2-alpha.1`](https://github.com/deepseek-ai/deepseek-harness/releases/tag/dsh-v0.1.2-alpha.1)，而 npm `latest` 仍为 `0.1.1-rc.2`。该 Alpha 增加子代理模型配置、ACP 自动化与多模态 / 持久终端修复；DeepSeek 适配器默认会附带已启用插件包的名称和版本（可关闭），会话日志增量上传仍为默认关闭。下方各项目标注的 DSH 版本表示其作者实际声明的开发或测试基线，不应自动视为已兼容最新预览版。

## ✨ Key Features

- [目录](#目录)
- [快速开始](#快速开始)
- [官方资源](#官方资源)
- [社区资源](#社区资源)
- [第三方客户端](#第三方客户端)
- [精选插件](#精选插件)

## 📦 Install

```bash
npx @deepseek-ai/dsh web
```

## 🚀 Quick Start

```bash
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
pnpm install
pnpm run build
pnpm dsh web
```

## 📚 Learn more

**使用 Python SDK**

官方 Python SDK 支持通过内置运行时以编程方式调用 Harness，无需在系统中安装 Node.js。当前要求 Python 3.10+，支持情况和平台限制以[官方 Python SDK 指南](https://deepseek-harness.github.io/deepseek-harness/guide/python-sdk)为准。 python -m venv .venv . .venv/bin/activate python -m pip install deepseek-harness-sdk

**安装插件**

`web` 和 `headless` 是发行版内置的 Profile。外部插件以声明 `dsh.bundle` 的 Bundle 加入指定 Profile： dsh plugin --profile web add <package-or-git-spec> dsh --profile web --dump-config 从 Git 仓库安装时，建议固定 commit，并先检查安装脚本。pnpm 可能要求显式授权依赖的构建脚本；这些构建脚本会在 Agent 沙箱之外执行。完整机制见[官方插件打包与安装教程](https://deepseek-harness.github.io/deepseek-harness/develop/basic/publish)。

## 🔗 Links

- [GitHub Repository](https://github.com/libukai/awesome-deepseek-harness)
- [Full README](https://github.com/libukai/awesome-deepseek-harness#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
