---
title: "dsh-lark-link"
description: "High-reliability Feishu/Lark bridge for DeepSeek Harness — QR one-click auth, multi-mode agents, card-based commands, zero-loss outbox, media in/out, session-log doctor, reusable DSH Web GUI"
keywords: "dsh-lark-link, channel, integration, coding, multi-agent, ui, deepseek harness, dsh"
---
# dsh-lark-link

> ⭐ **30** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 渠道 |
| 星数 | ⭐ 30 | 状态 | ✅ 活跃 |
| 作者 | [amlyczz](https://github.com/amlyczz) | 更新时间 | — |

## 一句话介绍

> High-reliability Feishu/Lark bridge for DeepSeek Harness — QR one-click auth, multi-mode agents, card-based commands, zero-loss outbox, media in/out, session-log doctor, reusable DSH Web GUI

## 详细介绍

**DeepSeek Harness × 飞书/Lark 双向桥接插件** —— 把你的 DSH 智能体装进飞书：扫码 30 秒上线、消息零丢失、卡片化交互、每飞书会话独立 Agent。手机上随时给 Agent 派任务、看结果、切模型切模式——不用守着终端。

## ✨ 核心特性

- **零门槛**：扫码即建飞书应用，不用手搓开放平台、不用配回调、不用公网服务器
- **零丢失**：出站 Outbox + 入站 WAL 双持久化，进程崩溃 / 插件热更 / dsh 重启，消息和回答都补得回来
- **零学习成本**：所有切换类命令都是单选卡片，点一下即生效；DSH 原生命令（/goal /compact …）直接用
- **真 Agent**：不是聊天机器人——bash/文件/子代理/工作流全套工具，飞书里跑完整 Harness

## 📦 安装

```bash
# 1. 绕过标签，直接看官方源的真实版本列表：
npm view dsh-lark-link versions --registry https://registry.npmjs.org

# 2. 显式版本号安装（最可靠，不依赖镜像标签）：
dsh plugin --profile web add dsh-lark-link@<新版本号> --ignore-scripts

# 3. 或强制官方源再走 @latest：
dsh plugin --profile web add dsh-lark-link@latest --ignore-scripts --registry https://registry.npmjs.org
```

## 🚀 快速开始

```bash
# 2. 启动 DSH Web GUI
dsh web

# 3. 在 GUI 的输入框（或终端 CLI）执行：
/lark setup       # 扫码创建飞书应用（30 秒，面板显示二维码）
/lark start       # 启动桥接
```

## 📚 更多信息

**🚀 Quickstart**

Prerequisites: Node.js ≥ 24 and DeepSeek Harness installed (`npm i -g @deepseek-ai/dsh`). dsh plugin --profile web add dsh-lark-link@latest --ignore-scripts dsh web /lark setup # scan QR (30s) /lark start Open Feishu, find your bot, send anything — reaction receipt + full reply = end-to-end. **Group chats need no @-mention.** Install variants: local tarball (`npm pack`, then `dsh plugin --profile 

**⚙️ Configuration (`/lark-config`, hot-reloaded & persisted)**

Credentials (appId/appSecret) live in the DSH credentials service, never in config files.

## 🔗 链接

- [GitHub 仓库](https://github.com/amlyczz/dsh-lark-link)
- [完整 README](https://github.com/amlyczz/dsh-lark-link#readme)
- [返回dsh-lark-link所在分类](../integrations.md)
