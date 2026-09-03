---
title: "dsh-usage-plugin"
description: "DeepSeek Harness（DSH）的 Token 用量统计 附属插件"
keywords: "dsh-usage-plugin, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-usage-plugin

> ⭐ **4** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [Qiongkura](https://github.com/Qiongkura) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> DeepSeek Harness（DSH）的 Token 用量统计 附属插件

## About

Plugins for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (DSH). A pnpm workspace: one package per plugin under `packages/`.

## 📦 Install

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

## 🚀 Quick Start

```bash
pnpm install
pnpm run build   # tsc for every package
pnpm run test    # node --test for every package
```

## 📚 Learn more

**install the package into your profile (each plugin is a work**

dsh plugin --profile web add -w 'github:Yihong89/dsh-usage-plugin#main&path:packages/usage-report'

## 🔗 Links

- [GitHub Repository](https://github.com/Qiongkura/dsh-usage-plugin)
- [Full README](https://github.com/Qiongkura/dsh-usage-plugin#readme)
- [Back to the Plugins list](../plugins.md)
