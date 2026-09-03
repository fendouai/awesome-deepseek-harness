---
title: "dsh-interconnect"
description: "Cross-instance message/event handoff plugins (interconnect service + tools)."
keywords: "dsh-interconnect, multi-agent, agent, deepseek harness, dsh"
---
# dsh-interconnect

> ⭐ **34** · ✅ active · agent · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | agent | Category | Multi-agent |
| Stars | ⭐ 34 | Status | ✅ active |
| Author | [Chinesezjc](https://github.com/Chinesezjc) | Updated | 2026-08-19 |

## One-liner

> Cross-instance message/event handoff plugins (interconnect service + tools).

## About

跨实例消息互通与事件通知插件，用于 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (DSH)。 让一个 DSH 实例能向同一个实例、另一台机器、或另一台机器上的别的 DSH 实例发送消息、探测活性，并在实例之间双向推送事件。

## ✨ Key Features

- 全走持久 WebSocket 链接：跨实例、跨机器投递消息、枚举 live session、探测活性（`send`/`reply`/`ping`/`list` 经 `/interconnect/link` 的 `msg`/`query` 帧）
- `/interconnect/link` WebSocket 端点：双向实时事件推流，含心跳与指数退避重连；也承载
- 事件 fan-out（HTTP + WebSocket），入站事件以 `interconnect/event` 发出
- 共享密钥鉴权（`DSH_INTERCONNECT_TOKEN`，bearer，fail-closed，timing-safe 比较）
- `interconnect_send`：向对端实例的指定 session 投递消息；可选 `delivery` 选投递模式、`resume` 唤醒离线 session
- `interconnect_list`：列出对端实例的 live session（id + 标题 + 状态），用于在不预先知道 session id 时寻址

## 🚀 Quick Start

```bash
session-264d37b0-…  重构 interconnect 插件  [idle]
session-b07326da-…                          [running]
```

## 📚 Learn more

**配置**

`interconnect` 行的 `config`（全部可选，下表为默认值）： config: instanceId: my-box peers: peer-a: http://127.0.0.1:13080 # 我拨向对端 peer-a 的 origin peer-b: http://127.0.0.1:13081 delivery: followup allowResume: false # 拒绝一切唤醒请求 鉴权用的共享密钥不在这里，而是取自 credentials 的 `DSH_INTERCONNECT_TOKEN`（fail-closed： 没有 token 时端点返回 403）。

**安装**

本包已发布到 npm：[`dsh-interconnect`](https://www.npmjs.com/package/dsh-interconnect)。 本仓库是一个 DSH profile bundle（根 `package.json` 声明 `dsh.bundle.patch` 指向 根 `cordis.patch.yml`，后者 `insert` 三个插件行）。

**架构说明**

服务（有 HTTP/WS 端点），必须 host 级；`tool-interconnect` 和 `skill-interconnect` 也放 host，因为 `interconnect` 未做 TypeRT `@Remote`/Gateway 绑定，放进 agent preset 的 isolate realm 会导致工具/技能行无法 inject 到该服务。

## 🔗 Links

- [GitHub Repository](https://github.com/Chinesezjc/dsh-interconnect)
- [Full README](https://github.com/Chinesezjc/dsh-interconnect#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
