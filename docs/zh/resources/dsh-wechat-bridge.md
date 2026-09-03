---
title: "dsh-wechat-bridge"
description: "DeepSeek Harness (dsh) transport plugin: chat with your agents on WeChat via official Tencent iLink bot API — zero runtime deps, no OpenClaw, QR-code login, one friend = one persistent agent session."
keywords: "dsh-wechat-bridge, channel, integration, coding, multi-agent, deepseek harness, dsh"
---
# dsh-wechat-bridge

> ⭐ **10** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 渠道 |
| 星数 | ⭐ 10 | 状态 | ✅ 活跃 |
| 作者 | [gtaifu](https://github.com/gtaifu) | 更新时间 | — |

## 一句话介绍

> DeepSeek Harness (dsh) transport plugin: chat with your agents on WeChat via official Tencent iLink bot API — zero runtime deps, no OpenClaw, QR-code login, one friend = one persistent agent session.

## 详细介绍

基于 [Wechat-ggGitHub/wechat-claude-code](https://github.com/Wechat-ggGitHub/wechat-claude-code) 开发的 **DeepSeek Harness (DSH) 微信桥接插件**。 **三端通用**：Windows / macOS / Linux 均使用纯 Node.js 进程管理，不依赖 launchd / systemd / Windows Service；同时提供 DSH 模型工具（CLI/Headless 可用）和 Web 管理面板（Web/桌面可用）。

## ✨ 核心特性

- 微信扫码绑定个人微信后，在微信里直接与 **DSH 本机 Agent** 对话。
- 复用 wechat-claude-code 的 iLink Bot 微信协议层：文字、图片、语音转文字、文件收发。
- 守护进程由 DSH 插件管理：启动 / 停止 / 重启 / 状态 / 日志，全部走模型工具或 Web 面板。
- 每个微信账号对应一个 DSH 会话，DSH Host 重启后会自动 `resume` 原持久化会话，对话上下文不断档；`/clear`、`/new`、`/stop`、`/cwd`、`/model`、`/prompt` 等斜杠命令可用。
- 流式回复：DSH Agent 的 `assistant/chunk` 通过本地 SSE 推送到微信（批量发送，不刷屏）。
- 超时安抚：DSH 超过 5 分钟无输出时自动发一条“还在处理”的消息。
- 主动通知：agent 可通过 `wechat_notify` 工具在任务完成 / 失败 / 需要确认时主动推送微信，内置节流（每小时 ≤6 条、每日 ≤50 条，超限排队延迟发送），规避个人号风控。
- **微信内审批**：agent 请求权限时推送审批消息到微信，回复 `/yes` 批准、`/no` 拒绝；超时自动拒绝（fail-closed），仅绑定账号本人可裁决，不影响桌面 GUI 会话。

## 📦 安装

```bash
npm install @lanbaolu/dsh-wechat-bridge
dsh plugin --profile web add @lanbaolu/dsh-wechat-bridge
dsh web
```

## 🚀 快速开始

```bash
git clone https://github.com/lanbaolu/dsh-wechat-bridge.git
dsh plugin --profile web add /path/to/dsh-wechat-bridge
dsh web
```

## 📚 更多信息

**方式一：npm 一键安装（推荐）**

npm install @lanbaolu/dsh-wechat-bridge dsh plugin --profile web add @lanbaolu/dsh-wechat-bridge dsh web

**方式二：本地路径安装（开发/个人使用）**

在 DSH profile 中安装本地包： git clone https://github.com/lanbaolu/dsh-wechat-bridge.git dsh plugin --profile web add /path/to/dsh-wechat-bridge dsh web 或者使用超级注入器（开发模式）： dev_inject_plugin /path/to/dsh-wechat-bridge

**超时安抚配置**

DSH 长时间没有产出消息时，桥接会主动发一条"还在处理"的安抚消息（默认 5 分钟静默后、每 5 分钟一条，避免用户以为卡死）。嫌频繁或想自定义，可在 Web 面板「⏳ 超时安抚」区块调整，或直接编辑 `config.json` 的 `calm` 节： { "calm": { "enabled": true, // 是否启用安抚，默认 true "silenceMs": 600000, // 首次静默多久后安抚（毫秒），默认 300000（5 分钟） "intervalMs": 900000, // 两次安抚最小间隔（毫秒），默认同 silenceMs "maxCount": 3, // 每轮任务最多安抚次数，0/省略 = 不限制 "messages": [ // 自定义文案（随机取一条），留空用内置默认 "还在处理中，这个问题有点复杂，请再稍等一下", "马上就好，正在收尾" ] } 

## 🔗 链接

- [GitHub 仓库](https://github.com/gtaifu/dsh-wechat-bridge)
- [完整 README](https://github.com/gtaifu/dsh-wechat-bridge#readme)
- [返回dsh-wechat-bridge所在分类](../integrations.md)
