---
title: "dsh-plugin-template (sunshine-lang)"
description: "可直接发布的插件骨架：bundle 格式、工具 DSL、配置与测试。"
keywords: "dsh-plugin-template (sunshine-lang), learning, example, coding, deepseek harness, dsh"
---
# dsh-plugin-template (sunshine-lang)

> ⭐ **6** · ✅ 活跃 · 示例 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 示例 | 分类 | 学习 |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [sunshine-lang](https://github.com/sunshine-lang) | 更新时间 | 2026-08-14 |

## 一句话介绍

> 可直接发布的插件骨架：bundle 格式、工具 DSL、配置与测试。

## 详细介绍

[English](README.en.md) | 中文 一个开箱即用的 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 插件骨架。一切皆插件：本模板把 bundle 格式、工具 DSL、配置校验、测试与发布清单集中在一个项目里。

## 🚀 快速开始

```bash
├── package.json           # dsh.bundle.patch —— bundle 清单
├── cordis.patch.yml       # profile 挂载本 bundle 时插入的层
├── src/index.ts           # 插件本体：name / inject / Config / apply + 工具
├── test-integration.ts    # 无 key 的 harness 上下文测试
├── tsconfig.json          # 干净的构建配置（随包发布）
└── tsconfig.local.json    # 在 harness 仓库内构建（工作区类型路径）
```

## 🔗 链接

- [GitHub 仓库](https://github.com/sunshine-lang/dsh-plugin-template)
- [完整 README](https://github.com/sunshine-lang/dsh-plugin-template#readme)
- [返回dsh-plugin-template (sunshine-lang)所在分类](../examples.md)
