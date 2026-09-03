---
title: "telegram"
description: "Telegram Bot API 桥接插件：长轮询、per-chat 会话、HTML 格式化"
keywords: "telegram, channel, integration, coding, deepseek harness, dsh"
---
# telegram

> ⭐ **7** · ✅ 活跃 · 集成 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 渠道 |
| 星数 | ⭐ 7 | 状态 | ✅ 活跃 |
| 作者 | [LoserFox](https://github.com/LoserFox) | 更新时间 | 2026-08-13 |

## 一句话介绍

> Telegram Bot API 桥接插件：长轮询、per-chat 会话、HTML 格式化

## 详细介绍

dsh --profile web --dump-config | grep telegram - 插入行 id：`telegram`（cordis.patch.yml）；不声明模型面工具或技能——它是把 Telegram 聊天桥接到 agent 会话的后台服务插件。 - **加载即需要 token**：缺少 bot token（配置 `token` 或环境变量 `DSH_TELEGRAM_TOKEN`）时 `apply` 直接报错；没有 token 不会惰性启动。 - **宿主前置条件**：dsh 组合必须挂载 `agents` 服务（`@deepseek-ai/dsh-agent`）；LLM 适配器、会话与工具来自外围 `cordis.yml`（见 [`telegram-agent`](examples/telegram-agent/README.zh.md) 示例）。 - 卸载：`dsh plugin --profile web remove telegram`。 - 安装后需重启目标 profile 的 DSH 进程（组合层变更不参与 HMR 热更新）。

## 📦 安装

```bash
# 从本仓库 checkout 安装到 profile（web / headless 等），bundle 声明自动加入组合层
dsh plugin --profile web add <dir|git-url>
# 验证
dsh --profile web --dump-config | grep telegram
```

## 📚 更多信息

**配置**

缺少 token 时加载即报错（fail loud）。未配置白名单时 bot 拒绝所有用户（fail closed）。`TelegramConfig` 还接受仅运行时使用的 `client` 与 `sleep` 接缝供测试使用；生产环境使用全局 `fetch` 与真实定时器。所有错误经 `ctx.logger` 记录且 bot token 被脱敏。

## 🔗 链接

- [GitHub 仓库](https://github.com/LoserFox/telegram)
- [完整 README](https://github.com/LoserFox/telegram#readme)
- [返回telegram所在分类](../integrations.md)
