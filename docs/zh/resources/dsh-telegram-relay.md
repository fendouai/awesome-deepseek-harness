---
title: "DSH Telegram Relay"
description: "把 Telegram 变成 DSH 远程对话渠道并接收通知。"
keywords: "DSH Telegram Relay, channel, integration, channels, deepseek harness, dsh"
---
# DSH Telegram Relay

> ⭐ **6** · ✅ 活跃 · 集成 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 渠道 |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [congchuanling-dot](https://github.com/congchuanling-dot) | 更新时间 | 2026-08-13 |

## 一句话介绍

> 把 Telegram 变成 DSH 远程对话渠道并接收通知。

## 详细介绍

让 Telegram 成为 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 的移动端对话入口。 插件在本机通过 Telegram Bot API 长轮询接收私聊文本，将消息交给 DSH Agent 处理，并把最终回答发送回原会话。每个 Telegram `chat_id` 对应一个持久化 DSH Session，因此连续追问和进程重启后都能保留上下文。

## 📦 安装

```bash
cd DSH-Telegram-Relay
pnpm install --config.auto-install-peers=false

pnpm link \
  ../deepseek-harness/vendor/cordis \
  ../deepseek-harness/packages/core/agent \
  ../deepseek-harness/packages/core/agent-default-model \
  ../deepseek-harness/packages/llm/llm \
  ../deepseek-harness/packages/core/session \
  ../deepseek-harness/packages/session/session-persistence

pnpm run build
```

## 🚀 快速开始

```bash
pnpm --dir ../deepseek-harness \
  dsh plugin --profile web add \
  "$(pwd)"
```

## 📚 更多信息

**工作原理**

Telegram 用户 │ │ 私聊文本 ▼ Telegram Bot API │ getUpdates 长轮询 ▼ DSH Telegram Relay │ allowlist 校验 │ chat_id -> Session ID ▼ DeepSeek Harness Agent │ 模型推理 / 工具调用 / Session 持久化 ▼ DSH Telegram Relay │ sendMessage ▼ Telegram 用户 等待 `getUpdates` 返回时使用异步网络 I/O，不会通过 CPU 忙等持续轮询。

**2. 配置环境变量**

Token 和 allowlist 只通过环境变量传入。不要将 Token 写入代码、YAML、README 或 Git。 export TELEGRAM_BOT_TOKEN='<BotFather 返回的 Token>' export TELEGRAM_ALLOWED_CHAT_IDS='<你的私聊 chat_id>' 允许多个私聊时使用英文逗号分隔： export TELEGRAM_ALLOWED_CHAT_IDS='123456789,987654321' `export` 只对当前终端会话及其启动的子进程生效。关闭终端或新开终端后，需要重新设置。Bot Token 通常保持不变，只有通过 BotFather 重新生成后才会变化；个人私聊 `chat_id` 通常也不会变化。 为了避免每次启动前重复设置，可以写入 `deepseek-harness` 根目录的 `.env`： TEL

**3. 安装依赖并构建**

当前开发方式假设 `DSH-Telegram-Relay` 与 `deepseek-harness` 位于同一父目录： myOwnProject/ ├── deepseek-harness/ └── DSH-Telegram-Relay/ 首次开发时安装依赖，并将 DSH peer dependencies 链接到本地 Harness： cd DSH-Telegram-Relay pnpm install --config.auto-install-peers=false pnpm link \ ../deepseek-harness/vendor/cordis \ ../deepseek-harness/packages/core/agent \ ../deepseek-harness/packages/core/agent-default-model \ ../deepseek-har

**4. 安装到 DSH**

将插件加入 `web` profile： pnpm --dir ../deepseek-harness \ dsh plugin --profile web add \ "$(pwd)" 确认插件已经安装： pnpm --dir ../deepseek-harness \ dsh plugin --profile web list 输出中应包含： dsh-telegram-relay@link:.../DSH-Telegram-Relay

## 🔗 链接

- [GitHub 仓库](https://github.com/congchuanling-dot/DSH-Telegram-Relay)
- [完整 README](https://github.com/congchuanling-dot/DSH-Telegram-Relay#readme)
- [返回DSH Telegram Relay所在分类](../integrations.md)
