---
title: "dsh-mobile"
description: "DeepSeek Harness 移动端适配与安全局域网访问插件，支持 Android App 和手机浏览器。"
keywords: "dsh-mobile, mobile, client, coding, deepseek harness, dsh"
---
# dsh-mobile

> ⭐ **79** · ✅ 活跃 · 客户端 · 近期 ⬆️ +28

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 移动端 |
| 星数 | ⭐ 79 | 状态 | ✅ 活跃 |
| 作者 | [saya-ch](https://github.com/saya-ch) | 更新时间 | 2026-08-19 |

## 一句话介绍

> DeepSeek Harness 移动端适配与安全局域网访问插件，支持 Android App 和手机浏览器。

## 详细介绍

- **在手机上继续电脑端的工作**：同一份会话、工作区、消息和工具，实时同步。 - **用对话定制手机端**：直接在 DSH 对话里改手机页面的布局、交互和功能，几秒内刷新。 - **专属触屏布局**：会话抽屉、工具详情、设置、提问卡片和输入栏都按手机重新组织。App 原生页面跟随系统显示简体中文、英文或意大利文；插件界面跟随 DSH 的语言设置，意大利语资源已为 DSH 后续支持预留。 - **图片附件**：在已打开会话的输入栏加号菜单顶部选择图片或拍照；支持 PNG、JPEG、WebP、GIF（不超过 8 MiB）和完整分辨率 JPEG。 - **自动发现、无需重新配对**：切换 Wi-Fi、热点或 IP 后通常自动恢复。 - **一键连接诊断**：检查版本、网关、网卡、防火墙和远程通道；稳定的原因码在界面中本地化，并生成不含凭据与完整地址的脱敏报告。 - **更快恢复连接**：远程重开会并行恢复可信连接、复用版本化资源，并压缩移动端启动批次。 - **三种配对方式**：扫码、配对链接、密钥。 配对设备被视为完全信任，可以操作电脑上的 DSH；建议只在可信的家庭、办公局域网或可信 VPN 中使用。

## ✨ 核心特性

- **在手机上继续电脑端的工作**：同一份会话、工作区、消息和工具，实时同步。
- **用对话定制手机端**：直接在 DSH 对话里改手机页面的布局、交互和功能，几秒内刷新。
- **专属触屏布局**：会话抽屉、工具详情、设置、提问卡片和输入栏都按手机重新组织。App 原生页面跟随系统显示简体中文、英文或意大利文；插件界面跟随 DSH 的语言设置，意大利语资源已为 DSH 后续支持预留。
- **图片附件**：在已打开会话的输入栏加号菜单顶部选择图片或拍照；支持 PNG、JPEG、WebP、GIF（不超过 8 MiB）和完整分辨率 JPEG。
- **自动发现、无需重新配对**：切换 Wi-Fi、热点或 IP 后通常自动恢复。
- **一键连接诊断**：检查版本、网关、网卡、防火墙和远程通道；稳定的原因码在界面中本地化，并生成不含凭据与完整地址的脱敏报告。

## 📦 安装

```bash
dsh plugin --profile web add dsh-mobile@latest
dsh plugin --profile web exec dsh-mobile setup
dsh --profile web
```

## 🚀 快速开始

```bash
corepack enable; pnpm install
pnpm dsh plugin --profile web add dsh-mobile@latest
pnpm dsh plugin --profile web exec dsh-mobile setup
pnpm dsh --profile web
```

## 📚 更多信息

**工作原理**

flowchart LR Phone["Android App / 手机浏览器"] -->|"局域网 HTTPS"| Lan["局域网网关"] Phone -->|"远程 HTTPS"| Remote["独立远程网关"] Lan --> Gateway["DSH Mobile Gateway Core"] Remote --> Gateway Gateway -->|"回环代理"| DSH["原生 DSH Web 与 Host"] DSH -->|"同一工作区、会话和事件流"| Phone 插件包含三层：Host face 负责发现、配对、HTTPS、回环代理和扩展注册表；Client face 提供独立的移动布局与扩展 SDK；Android App 提供受限的原生 Bridge。Bridge 使用 `androidx.webkit` WebMessage，每条消息都校验精确顶层 Ori

## 🔗 链接

- [GitHub 仓库](https://github.com/saya-ch/dsh-mobile)
- [完整 README](https://github.com/saya-ch/dsh-mobile#readme)
- [返回dsh-mobile所在分类](../clients.md)
