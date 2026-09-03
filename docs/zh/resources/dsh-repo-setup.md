---
title: "dsh-repo-setup"
description: "只读仓库体检引导工具（repo_setup_scan）：识别技术栈/测试/文档/git/数据库线索，给出插件、MCP 与卫生文件的安装建议（claude-code-setup 对应版）。"
keywords: "dsh-repo-setup, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-repo-setup

> ⭐ **1** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [gongyijie85](https://github.com/gongyijie85) | 更新时间 | 2026-08-16 |
| 子分类 | 🧪 代码·测试·审查 | 能力 | coding |

## 一句话介绍

> 只读仓库体检引导工具（repo_setup_scan）：识别技术栈/测试/文档/git/数据库线索，给出插件、MCP 与卫生文件的安装建议（claude-code-setup 对应版）。

## 详细介绍

[English](README.en.md) | **简体中文** 仓库体检引导插件 —— Anthropic **claude-code-setup** 的 DeepSeek Harness 版。 注册一个**只读**工具 `repo_setup_scan`:扫描项目目录的语言栈、测试设置、 文档、git、Docker 与数据库线索,然后给出设置建议:该装哪些 DSH 技能插件、 该挂哪些 MCP 服务器、该补哪些卫生文件。**绝不修改任何东西。**

## 📦 安装

```bash
# npm
dsh plugin --profile web add dsh-repo-setup

# GitHub
dsh plugin --profile web add github:gongyijie85/dsh-repo-setup

# 本地开发
dsh plugin --profile web add D:\plugins\dsh-repo-setup
```

## 🚀 快速开始

```bash
node --check lib/index.js
# 功能冒烟(伪 ctx 注册 + 直接调 scanRepo 逻辑见 scripts/verify-tool.mjs)
node scripts/verify-tool.mjs
```

## 🔗 链接

- [GitHub 仓库](https://github.com/gongyijie85/dsh-repo-setup)
- [完整 README](https://github.com/gongyijie85/dsh-repo-setup#readme)
- [返回dsh-repo-setup所在分类](../plugins.md)
