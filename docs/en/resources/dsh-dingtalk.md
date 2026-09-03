---
title: "dsh-dingtalk"
description: "DeepSeek Harness 钉钉群机器人通知插件：dingtalk_notify/dingtalk_text 两工具，自定义机器人 webhook + HMAC 加签安全模式，手写签名实现、零运行时依赖；纯 Node 全平台。· DingTalk group-robot notifications for DeepSeek Harness agents."
keywords: "dsh-dingtalk, channel, integration, coding, multi-agent, deepseek harness, dsh"
---
# dsh-dingtalk

> ⭐ **3** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | Channels |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [STARDUSTLC666](https://github.com/STARDUSTLC666) | Updated | 2026-08-18 |

## One-liner

> DeepSeek Harness 钉钉群机器人通知插件：dingtalk_notify/dingtalk_text 两工具，自定义机器人 webhook + HMAC 加签安全模式，手写签名实现、零运行时依赖；纯 Node 全平台。· DingTalk group-robot notifications for DeepSeek Harness agents.

## About

DeepSeek Harness 钉钉群机器人通知插件：让 agent 能**单向推送 Markdown / 纯文本消息到钉钉群**。纯插件实现，零核心改动，安装即可用。 纯 Node 实现，**全平台通用**（Windows / macOS / Linux 同一份代码），只依赖 `node:crypto` 与内置 `fetch`，无运行时依赖、无原生二进制。

## 📦 Install

```bash
dsh plugin --profile web add dsh-dingtalk
```

## 🚀 Quick Start

```bash
dsh plugin --profile web remove dsh-dingtalk
```

## 📚 Learn more

**安装**

dsh plugin --profile web add dsh-dingtalk 装好后重启 `dsh web`。插件自带空配置，**不会弄崩启动**；配置前调用任何 `dingtalk_*` 工具都会返回明确的中文配置提示。

**配置**

在你 profile 的 `cordis.patch.yml` 里覆盖 `tool-dingtalk` 行（在 `$DSH_HOME/profiles/<name>/` 下），然后重启： config: webhook: https://oapi.dingtalk.com/robot/send?access_token=你的token secret: SEC你的加签密钥 # 可选，但强烈建议；也可用环境变量 DSH_DINGTALK_SECRET

## 🔗 Links

- [GitHub Repository](https://github.com/STARDUSTLC666/dsh-dingtalk)
- [Full README](https://github.com/STARDUSTLC666/dsh-dingtalk#readme)
- [Back to the MCP & Integrations list](../integrations.md)
