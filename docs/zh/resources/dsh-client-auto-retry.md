---
title: "dsh-client-auto-retry"
description: "回合中断自动续跑：turn/end 因 error/interrupted/max-tokens 结束时自动发送「继续」，支持宽限期、冷却、连发上限、启动扫描与设置卡片；不切换模型/provider。"
keywords: "dsh-client-auto-retry, developer, plugin, workflow, ui, deepseek harness, dsh"
---
# dsh-client-auto-retry

> ⭐ **0** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 0 | 状态 | ✅ 活跃 |
| 作者 | [Frog755](https://github.com/Frog755) | 更新时间 | 2026-08-20 |
| 子分类 | 💰 费用与统计 | 能力 | workflow, ui |

## 一句话介绍

> 回合中断自动续跑：turn/end 因 error/interrupted/max-tokens 结束时自动发送「继续」，支持宽限期、冷却、连发上限、启动扫描与设置卡片；不切换模型/provider。

## 详细介绍

DeepSeek Harness（DSH）的回合（turn）偶尔会因为网络抖动、provider 报错、超时、 或输出达到 token 上限而中断。大多数情况下模型其实已经跑完大部分内容，只要再发一句 「继续」就能接着完成，完全不需要人工介入、也不需要切换模型。 这个插件就是干这件事的： 1. 监听会话事件流（`api.events.mux`）； 2. 发现 `turn/end` 的 `reason.kind` 属于 `error` / `interrupted` / `max-tokens` 时， 等一个宽限期（默认 5 秒，给 host 留出重连/恢复的时间）； 3. 宽限期后向该会话自动发送「继续」（可配置文本）； 4. 带冷却期、连续次数上限、启动时扫描最近被中断的会话等防护措施，避免失控循环。

## 📦 安装

```bash
pnpm add @frog755/dsh-client-auto-retry
```

## 🚀 快速开始

```bash
{
  "dependencies": {
    "@frog755/dsh-client-auto-retry": "^0.3.0"
  },
  "dsh": {
    "profile": {
      "bundles": [
        "@deepseek-ai/dsh-base",
        "@deepseek-ai/dsh-web-app",
        // ... 其他 bundle ...
        "@frog755/dsh-client-auto-retry"
      ]
    }
  }
}
```

## 📚 更多信息

**方式 A：通过 npm 安装（推荐）**

在 DSH 的 profile 目录（例如 `~/.dsh/profiles/web`）里执行： pnpm add @frog755/dsh-client-auto-retry 然后编辑该目录下的 `package.json`，把 `@frog755/dsh-client-auto-retry` 加入 `dsh.profile.bundles` （插件自带的 `cordis.patch.yml` 会以 bundle 层的形式把 `auto-retry` 行插入插件清单）： { "dependencies": { "@frog755/dsh-client-auto-retry": "^0.3.0" }, "dsh": { "profile": { "bundles": [ "@deepseek-ai/dsh-base", "@deepseek-ai/dsh-web-app", // ... 

**工作原理**

flowchart LR A[api.events.mux 事件流] --> B{turn/end?} B -- "error / interrupted / max-tokens" --> C[schedule: 宽限期 graceMs] B -- "completed / aborted / blocked" --> D[重置连续计数] C --> E{冷却期已过? 未超上限?} E -- 否 --> F[跳过, 等人工] E -- 是 --> G[fire: sessions.prompt 发送「继续」] G --> H[连续次数 +1] A --> I[user/message 到来] --> D A --> J[scanOnBoot: 启动扫描最近中断会话] --> C 核心逻辑都在 `lib/client.js` 的 `AutoRetryRunner` 里；`lib/index

## 🔗 链接

- [GitHub 仓库](https://github.com/Frog755/dsh-client-auto-retry)
- [完整 README](https://github.com/Frog755/dsh-client-auto-retry#readme)
- [返回dsh-client-auto-retry所在分类](../plugins.md)
