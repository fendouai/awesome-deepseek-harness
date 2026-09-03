---
title: "dsh-plugin-d399"
description: "Mini-game menu (Wordle, match-3, 192 parameterized games) that pops up while the model generates."
keywords: "dsh-plugin-d399, fun, plugin, ui, deepseek harness, dsh"
---
# dsh-plugin-d399

> ⭐ **8** · ✅ active · plugin · ⬆️ +3 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Fun & lifestyle |
| Stars | ⭐ 8 | Status | ✅ active |
| Author | [HuanLinOTO](https://github.com/HuanLinOTO) | Updated | 2026-08-15 |

## One-liner

> Mini-game menu (Wordle, match-3, 192 parameterized games) that pops up while the model generates.

## About

当模型正在生成响应时，右下角弹出一个蓝鲸游戏弹窗。点击「来♂」展开游戏菜单，内置 Wordle + 消消乐 + **192 款参数化小游戏**（覆盖反应/解谜/策略/街机/问答/卡牌等品类，同族变体折叠成组），并支持自定义网页书签。等待不再寂寞。

## ✨ Key Features

- **生成检测**：订阅 `ctx.sessions.list` 的 `running` 标志。`false→true` 边沿触发右下角 teaser 弹窗；`true→false` 自动收起（除非用户已打开游戏菜单或正在游戏中——此时保留到用户手动关闭）。
- **内置游戏**：
- **同族变体折叠**：菜单里同类型的变体（如 5 款贪吃蛇）折叠为一个可展开的组，组头显示名称与变体数量，默认收起，支持「全部展开/全部收起」。
- **可拓展**：暴露 `ctx.d399Games` 客户端服务，第三方插件可通过 `inject: ['d399Games']` 注册更多游戏；游戏条目带可选 `group` 字段即可参与折叠。

## 📦 Install

```bash
pnpm install          # 安装开发依赖
pnpm run typecheck    # tsc --noEmit（通过 ../dsh 解析 DSH 源码类型）
pnpm test             # vitest run（wordle / match3 / 注册表 / mini catalog 单元测试）
pnpm run build        # tsc + tsdown → lib/index.js, lib/invariant.js, lib/client.js
pnpm run bundle:client  # 只跑 tsdown，跳过 tsc（用于绕开 ../dsh vendor 的预存在类型错误）
```

## 🚀 Quick Start

```bash
# 从 npm 安装（推荐）：
dsh plugin --profile web add @huanlin/dsh-plugin-d399
```

## 📚 Learn more

**配置**

通过 `cordis.patch.yml` 的 `config` 块覆盖默认值： - id: dsh-d399 name: '@huanlin/dsh-plugin-d399' config: message: '❤深❤夜❤寂❤寞❤，❤来❤玩❤ D399❤' # teaser 文案 buttonText: '来♂' # teaser 按钮文字 enabled: true # 总开关

## 🔗 Links

- [GitHub Repository](https://github.com/HuanLinOTO/dsh-plugin-d399)
- [Full README](https://github.com/HuanLinOTO/dsh-plugin-d399#readme)
- [Back to the Plugins list](../plugins.md)
