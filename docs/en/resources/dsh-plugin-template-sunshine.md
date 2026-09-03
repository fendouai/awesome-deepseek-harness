---
title: "dsh-plugin-template (sunshine-lang)"
description: "Ready-to-publish plugin skeleton: bundle format, tool DSL, config and tests."
keywords: "dsh-plugin-template (sunshine-lang), learning, example, coding, deepseek harness, dsh"
---
# dsh-plugin-template (sunshine-lang)

> ⭐ **6** · ✅ active · example · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | example | Category | Learning |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [sunshine-lang](https://github.com/sunshine-lang) | Updated | 2026-08-14 |

## One-liner

> Ready-to-publish plugin skeleton: bundle format, tool DSL, config and tests.

## About

[English](README.en.md) | 中文 一个开箱即用的 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 插件骨架。一切皆插件：本模板把 bundle 格式、工具 DSL、配置校验、测试与发布清单集中在一个项目里。

## 🚀 Quick Start

```bash
├── package.json           # dsh.bundle.patch —— bundle 清单
├── cordis.patch.yml       # profile 挂载本 bundle 时插入的层
├── src/index.ts           # 插件本体：name / inject / Config / apply + 工具
├── test-integration.ts    # 无 key 的 harness 上下文测试
├── tsconfig.json          # 干净的构建配置（随包发布）
└── tsconfig.local.json    # 在 harness 仓库内构建（工作区类型路径）
```

## 🔗 Links

- [GitHub Repository](https://github.com/sunshine-lang/dsh-plugin-template)
- [Full README](https://github.com/sunshine-lang/dsh-plugin-template#readme)
- [Back to the Examples & Starters list](../examples.md)
