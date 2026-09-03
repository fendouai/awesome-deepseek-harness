---
title: "dsh-usage-plugin"
description: "DeepSeek Harness（DSH）的 Token 用量统计 附属插件"
keywords: "dsh-usage-plugin, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-usage-plugin

> ⭐ **4** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [Qiongkura](https://github.com/Qiongkura) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> DeepSeek Harness（DSH）的 Token 用量统计 附属插件

## 详细介绍

Plugins for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (DSH). A pnpm workspace: one package per plugin under `packages/`.

## 📦 安装

```bash
# install the package into your profile (each plugin is a workspace package)
dsh plugin --profile web add -w 'github:Yihong89/dsh-usage-plugin#main&path:packages/usage-report'

# activate by inserting the plugin row into the profile's patch layer
# (~/.dsh/profiles/web/cordis.patch.yml):
#
#   - insert:
#       - id: usage-report
#         name: 'dsh-usage-plugin'
```

## 🚀 快速开始

```bash
pnpm install
pnpm run build   # tsc for every package
pnpm run test    # node --test for every package
```

## 📚 更多信息

**install the package into your profile (each plugin is a work**

dsh plugin --profile web add -w 'github:Yihong89/dsh-usage-plugin#main&path:packages/usage-report'

## 🔗 链接

- [GitHub 仓库](https://github.com/Qiongkura/dsh-usage-plugin)
- [完整 README](https://github.com/Qiongkura/dsh-usage-plugin#readme)
- [返回dsh-usage-plugin所在分类](../plugins.md)
