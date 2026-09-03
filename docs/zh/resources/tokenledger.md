---
title: "tokenledger"
description: "Token usage accounting for DeepSeek Harness, reconciled against New API and Sub2API relay-site billing"
keywords: "tokenledger, vision, plugin, coding, deepseek harness, dsh"
---
# tokenledger

> ⭐ **126** · ✅ 活跃 · 插件 · 近期 ⬆️ +8

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 126 | 状态 | ✅ 活跃 |
| 作者 | [zh667](https://github.com/zh667) | 更新时间 | 2026-08-17 |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Token usage accounting for DeepSeek Harness, reconciled against New API and Sub2API relay-site billing

## 详细介绍

把 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 的 Token 用量算清楚，并归属到**实际服务这次请求的中转站**——不用配置，不用凭据。 Token-usage accounting for DeepSeek Harness, attributed to the relay site that served each request. The existing Web GUI (`dsh web`) and renderer-neutral consumers share the same host-owned aggregation. Zero configuration.

## 📦 安装

```bash
dsh plugin --profile web add "github:zh667/TokenLedger"
```

## 🚀 快速开始

```bash
dsh plugin --profile web update dsh-tokenledger
dsh plugin --profile web remove dsh-tokenledger
```

## 📚 更多信息

**快速安装 / Quick start**

需要 DeepSeek Harness `web` profile（`@deepseek-ai/dsh >= 0.1.0-rc.6`）。 dsh plugin --profile web add "github:zh667/TokenLedger" 重启已经在跑的 `dsh web`，浏览器硬刷新。侧边栏底部会出现「用量账本」入口。 升级或卸载： dsh plugin --profile web update dsh-tokenledger dsh plugin --profile web remove dsh-tokenledger 重装同一个 spec 会重新解析，所以 `add` 一遍就能拿到最新的 `main`（实测过，不是推测）。 **要钉某个版本，必须用完整的 40 位 commit SHA。** 包管理器把 ref 拿去和 `git ls-remote` 广播的引用列表比对，

**配置 / Configuration**

**通常不需要任何配置。** 中转站从宿主的 provider 设置里读出来。 需要覆盖时，写进你已有的 `settings.yaml`（改完热更新，不用重启）： tokenledger: # 只在自动发现看不到时才需要——比如组合里没挂 settings 服务， # 或 provider 是 agent preset 在 agent.cordis.yml 里挂的 relays: my-route: https://relay.example.com/v1 # 费率表，用于费用估算；不配就显示破折号，不会猜 rates: [] # 探测中转站跑的是哪套程序。默认关闭，第一次查余额时会自动探一次 fingerprint: false

## 🔗 链接

- [GitHub 仓库](https://github.com/zh667/TokenLedger)
- [完整 README](https://github.com/zh667/TokenLedger#readme)
- [返回tokenledger所在分类](../plugins.md)
