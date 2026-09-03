---
title: "dsh-desktop"
description: "Desktop client for DeepSeek Harness: AI screensaver, phone PWA remote control (LAN pairing), QQ/Telegram bot channels with approval/question buttons, mode prompts (assistant/friend), wallpapers and more."
keywords: "dsh-desktop, desktop, client, mobile, channels, automation, notifications, ui, deepseek harness, dsh"
---
# dsh-desktop

> ⭐ **1** · ✅ active · client · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [xiaowei2025cqu23phy](https://github.com/xiaowei2025cqu23phy) | Updated | 2026-08-20 |

## One-liner

> Desktop client for DeepSeek Harness: AI screensaver, phone PWA remote control (LAN pairing), QQ/Telegram bot channels with approval/question buttons, mode prompts (assistant/friend), wallpapers and more.

## About

[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 的桌面客户端(Electron + TypeScript)。

## ✨ Key Features

- **内嵌 Web UI**:原生控制条 + 内嵌完整 harness Web UI(会话、工具、插件全功能)。
- **AI 屏保(替换系统屏保)**:空闲 N 分钟自动全屏显示 agent 实时工作画面(思考过程、文本流、工具调用),鼠标移动即退出;内置**任务超时守卫**,杜绝失控循环烧 CPU;可注册为 Windows 系统屏保,空闲时间即生产力时间。
- **手机 PWA 遥控**:扫码配对(自动填地址+令牌),手机上发任务、看流式进展、停止任务;**审批/提问卡片一键应答**——agent 卡住等你批准时不再"失联"。远程访问仅面向可信局域网,默认启用 2 小时自动关闭;**禁止使用内网穿透、端口转发或公网反向代理暴露 Harness**。
- **QQ / Telegram 机器人通道**:群聊/私聊发指令即干活;打通**主动推送**(QQ 交互后 48h 窗口),任务完成、失败、要审批都会主动找你;QQ 审批带「允许/拒绝」内联按钮,点一下即批;还支持**扫码登录**自动获取机器人凭据。
- **QQ 机器人体验(0.6.0)**:未指定工作区的任务自动并入「默认任务会话」(不再刷屏);指定工作区用 `任务 @工作区名` 或「进入工作区后直接发」;`进展` 显示阶段(思考/工具/输出/完成+产物提示);任务过程默认静默、`播报` 按需开;机器人对话(私聊/群聊)集中放在可见的「机器人对话」工作区;**群聊仅
- **默认对话模式**:机器人开启后,普通消息直接进入纯对话(不绑定工作区),无需任何指令前缀。
- **各种模型选择**:快捷切换默认模型(DeepSeek 官方、OpenAI、Anthropic 及 37+ 目录 Provider),添加自定义 OpenAI 兼容网关(公司网关、Ollama 本地等),密钥安全写入 credentials 存储。
- **三端独立壁纸 + 拼豆像素滤镜**:主窗口 / 手机 / 屏保各配一张,导入自己的图片一键拼豆化(本地处理,不碰版权);内置鲸鱼系列壁纸包一键应用。

## 📦 Install

```bash
npm install
npm start        # 构建并启动桌面端
```

## 🚀 Quick Start

```bash
npm run build    # tsc 编译 main/preload/renderer 到 dist/
npm start        # 构建 + electron .
npm run smoke    # 冒烟测试:验证 RPC 客户端与模型目录(需 harness 运行中)
npm run pack     # 打包 Windows portable 单文件 exe(electron-builder)
```

## 📚 Learn more

**下载与安装**

从 [GitHub Releases](https://github.com/xiaowei2025cqu23phy/dsh-desktop/releases) 下载,三种形态任选: 安装版卸载时保留用户配置与壁纸(不会删除 `%APPDATA%` 数据);如需彻底清理请手动删除 `%APPDATA%/DeepSeek Harness Desktop`。 > 系统要求:Windows x64、Node.js 18+(建议 22 或 24 LTS;仅在桌面端需要托管拉起 harness 时使用)。 > 提示:先运行 `npx @deepseek-ai/dsh web` 并配置好模型密钥,再打开桌面端,体验最佳。

## 🔗 Links

- [GitHub Repository](https://github.com/xiaowei2025cqu23phy/dsh-desktop)
- [Full README](https://github.com/xiaowei2025cqu23phy/dsh-desktop#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
