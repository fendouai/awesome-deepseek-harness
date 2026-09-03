---
title: "dsh-feishu"
description: "通过扫码把飞书机器人接入DeepSeek Harness"
keywords: "dsh-feishu, channel, integration, coding, deepseek harness, dsh"
---
# dsh-feishu

> ⭐ **10** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | Channels |
| Stars | ⭐ 10 | Status | ✅ active |
| Author | [xmanrui](https://github.com/xmanrui) | Updated | — |

## One-liner

> 通过扫码把飞书机器人接入DeepSeek Harness

## About

把一个或多个飞书机器人直接接入 DeepSeek Harness。安装插件后，在 Harness 的设置页扫码即可逐个创建机器人；每次确认完成并通过连接检查后，都能立即在飞书里与同一个 Harness 智能体连续对话。

## ✨ Key Features

- Add multiple bots by repeatedly scanning QR codes under **Harness → Settings → Plugins → Feishu**, without manually copying an App ID or App Secret
- Keep separate credentials, Feishu long connections, authorized users, session mappings, and message deduplication state for every bot
- Reconnect or remove one bot without interrupting any other bot
- Automatically authorize the user who scans the QR code, so the bot is ready for direct messages immediately after setup
- Add a processing reaction as soon as a message arrives, then update it when the request succeeds or fails
- Stream replies through native Feishu CardKit cards, with a safe fallback to plain text
- Map every Feishu conversation to a persistent Harness session for multi-turn context
- Use the Harness `standard` agent preset by default, including tools such as web search

## 📦 Install

```bash
git clone https://github.com/xmanrui/dsh-feishu.git
cd dsh-feishu
npm install
npm test
npm run build
node bin/dsh-feishu.mjs install --source .
```

## 🚀 Quick Start

```bash
npx -y github:xmanrui/dsh-feishu install
```

## 📚 Learn more

**安装**

从 GitHub 一条命令安装： npx -y github:xmanrui/dsh-feishu install 安装后重启 `dsh web`，打开「设置 → 插件 → 飞书」，点击「添加机器人」，再用飞书扫码确认。需要更多机器人时再次点击「添加机器人」即可；扫码只会新增，不会覆盖现有机器人。页面只有在以下条件全部满足后才把该机器人显示为“已连接”： 1. 飞书应用创建成功； 2. 凭据已安全保存； 3. 机器人身份校验成功； 4. 飞书长连接已建立； 5. DeepSeek Harness Host 可访问。 连接成功后，在飞书中找到刚创建的机器人并发送消息即可。每个机器人都支持 `/new`、`/status` 和 `/help`。

**Installation**

Install from GitHub with one command: npx -y github:xmanrui/dsh-feishu install Restart `dsh web` after installation. Open **Settings → Plugins → Feishu** in Harness, click **Add bot**, and scan the QR code with Feishu. Repeat the same process to add more bots; a new scan never overwrites an existing bot. A bot is shown as **Connected** only after all of the following checks succeed: 1. The Feishu 

## 🔗 Links

- [GitHub Repository](https://github.com/xmanrui/dsh-feishu)
- [Full README](https://github.com/xmanrui/dsh-feishu#readme)
- [Back to the MCP & Integrations list](../integrations.md)
