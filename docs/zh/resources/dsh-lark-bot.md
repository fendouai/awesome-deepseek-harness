---
title: "dsh-lark-bot"
description: "DeepSeek Harness (dsh) 接入飞书/Lark bot，扫码即用：流式卡片、项目工作区、并行任务、多角色 Agent、跨会话通知、对话内模型/密钥管理与安全网守护（dsh 崩溃后飞书仍可自救）。A scan-to-connect bridge bot connecting DeepSeek Harness (dsh) into Feishu/Lark: streaming cards, workspaces, parallel tasks, multi-role agents, cross-session notify, in-chat model/key management, and a safety-net guardian."
keywords: "dsh-lark-bot, channel, integration, coding, multi-agent, deepseek harness, dsh"
---
# dsh-lark-bot

> ⭐ **37** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 渠道 |
| 星数 | ⭐ 37 | 状态 | ✅ 活跃 |
| 作者 | [PlutoKeating](https://github.com/PlutoKeating) | 更新时间 | — |

## 一句话介绍

> DeepSeek Harness (dsh) 接入飞书/Lark bot，扫码即用：流式卡片、项目工作区、并行任务、多角色 Agent、跨会话通知、对话内模型/密钥管理与安全网守护（dsh 崩溃后飞书仍可自救）。A scan-to-connect bridge bot connecting DeepSeek Harness (dsh) into Feishu/Lark: streaming cards, workspaces, parallel tasks, multi-role agents, cross-session notify, in-chat model/key management, and a safety-net guardian.

## 详细介绍

让 DeepSeek Harness 成为你飞书里的一员，在手机、群聊、话题里直接指挥本机 coding agent。 走飞书 WebSocket 长连接，**不需要公网 IP、域名、服务器或内网穿透**；Linux / macOS / Windows 通用，Node.js ≥ 22。 ---

## ✨ 核心特性

- **安全网守护**：dsh 崩溃后飞书仍会回复你，`/safemode` 进入仅核心安全模式直接自愈；重启后自动恢复排队任务，`/jobs` 可显式重试。多数桥接方案是「串行单聊 + 崩溃就失联」。
- **多机器人可信交接**：`bot add` 增加独立实例，可信机器人在同群真实 @ 交接，连续协作有上限。
- **完善的工作区与会话管理**：每会话自动创建隔离 git worktree 项目工作区；`/session` 浏览 / 绑定会话，`/archive` + `/retention` 自动归档与清理，会话列表不会烂掉。
- **完善的版本管理机制**：管理员直接在飞书发 `/upgrade` 后台更新、验证并重载；有新版本才提醒，不打断当前工作。
- **dsh Web 可视化设置**：官方 Settings → Plugins 页面点选工作目录、模型、并行数、提醒，不用背环境变量。
- **并行多任务**：同一群聊同时跑多个任务、会话隔离。
- **多角色 Agent**：`/role` 切换或指派 PM / 开发 / 文档等角色，各带人设、模型偏好与规则。
- **对话内管理模型与密钥**：一张 `/config` 卡片切换供应商、热更新密钥，不用离开飞书。

## 🚀 快速开始

```bash
npx dsh-lark-bot@latest setup --profile dsh-lark   # ① 一键安装（装进 dsh profile + 默认装「安全网守护」）
dsh --profile dsh-lark                              # ② 启动
```

## 📚 更多信息

**配置说明**

> 行为细节（崩溃对账、会话隔离、计划门禁、逐操作审批、多机器人交接、安全网守护等）见 [`docs/FEATURES.md`](docs/FEATURES.md)； > 权限与数据见 [`docs/MANUAL.md`](docs/MANUAL.md) §6 与 [`SECURITY.md`](SECURITY.md)。

## 🔗 链接

- [GitHub 仓库](https://github.com/PlutoKeating/dsh-lark-bot)
- [完整 README](https://github.com/PlutoKeating/dsh-lark-bot#readme)
- [返回dsh-lark-bot所在分类](../integrations.md)
