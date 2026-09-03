---
title: "dsh-cost-plugin"
description: "DSH 费用/余额读数插件：在输入框统计行旁实时显示「本次 ≈¥x · 会话 ≈¥x · 余额 ¥x」，内置 DeepSeek 官方价目表，支持 2026-08-17 起生效的峰谷定价（按节点时间戳自动选档），余额经官方 /user/balance 实时查询，失败静默降级。"
keywords: "dsh-cost-plugin, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-cost-plugin

> ⭐ **5** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 5 | Status | ✅ active |
| Author | [RoxsLee](https://github.com/RoxsLee) | Updated | 2026-08-14 |
| Subcategory | 💰 Cost & billing | Capabilities | coding |

## One-liner

> DSH 费用/余额读数插件：在输入框统计行旁实时显示「本次 ≈¥x · 会话 ≈¥x · 余额 ¥x」，内置 DeepSeek 官方价目表，支持 2026-08-17 起生效的峰谷定价（按节点时间戳自动选档），余额经官方 /user/balance 实时查询，失败静默降级。

## About

在 [DSH](https://github.com/deepseek-ai/dsh) Web 界面的输入框统计行（`3 轮 · 27 步 | …`）旁追加一行实时费用读数： 本次 ≈¥0.0123 | 会话 ≈¥1.2346 | 余额 ¥70.16 三个读数：**本次费用**（最新一轮 token 消耗 × 单价）、**会话费用**（会话累计 token × 单价）、**余额**（DeepSeek 官方账户余额，可选）。 这是一个 **DSH 动态 Cordis 插件**，由 Host（进程端）与 Client（浏览器端）两半组成，纯 JavaScript、无构建步骤。

## ✨ Key Features

- ✅ 与官方统计行**并列显示**（list 槽位叠加，order 1），不覆盖、不破坏任何现有 UI
- ✅ 内置 DeepSeek 官方价目表（deepseek-v4-flash / deepseek-v4-pro，CNY + USD 双币种），可自由增删模型/改价
- ✅ 支持 **2026-08-17 起生效的峰谷定价**：高峰时段为北京时间 9:00-12:00、14:00-18:00（低谷价减半）；生效前的历史节点按旧价计，本次费用按每个节点时间戳自动选档
- ✅ 计价公式与 [DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) 的 `OriginalCostAmount` 一致：缓存命中按 cacheHit 价，其余输入（含 cache-write）按 input 价，输出按 output 价，
- ✅ 费用一律带 `≈`（估计值）；模型不在价目表时显示 `n/a`，**绝不把 0 当真实花费**
- ✅ 余额通过官方 `GET /user/balance` 查询，异步拉取、**失败静默降级**（显示 `n/a` 或隐藏），不阻塞会话；多币种只显示非零项（对齐官方页面 `¥13.68 + $0.00` 的呈现）
- ✅ 余额不配置 key 就不查询、不显示（网关/代理部署无余额项属正常行为）

## 🚀 Quick Start

```bash
本次 ≈¥0.0123 | 会话 ≈¥1.2346 | 余额 ¥70.16
```

## 📚 Learn more

**安装与使用（DSH 创造模式动态插件）**

1. 在 DSH Web 新建一个**「创造模式」（cordis）**会话。 2. `cordis_define`： - `code.host` ← [plugin-host.js](plugin-host.js) 全文 - `code.client` ← [plugin-client.js](plugin-client.js) 全文 - `name` / `purpose` 自填（如 `cost-line` / 「会话费用与余额读数」） 3. `cordis_run` 运行刚定义的包：Host 半立即生效；浏览器弹出审批卡片时**确认授权**（单勾授权当前包即可）。 4. 回到任意会话页面（不止安装它的会话），输入框统计行旁即出现费用行，数值随轮次推进变化。 > 动态插件是进程内存态：DSH 重启后需要重新定义/运行。如需常驻，见下文「永久安装」。

**永久安装（常驻，DSH 重启后自动加载）**

本仓库即一个正式的 DSH 插件包：host 半（`lib/index.js`）通过 `webServer` 注册 `GET /_dsh-cost/balance` 路由，client 半（`lib/client.js`，dsh ModuleLoader 格式）注册进 `conversation.composer.dock` 槽位。

## 🔗 Links

- [GitHub Repository](https://github.com/RoxsLee/dsh-cost-plugin)
- [Full README](https://github.com/RoxsLee/dsh-cost-plugin#readme)
- [Back to the Plugins list](../plugins.md)
