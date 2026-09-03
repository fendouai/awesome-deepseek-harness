---
title: "ai-novel-writer"
description: "本地优先 AI 小说创作工作台，提供 Windows/macOS 桌面版与 DeepSeek Harness 插件开发预览，支持角色、大纲、章节蓝图、审稿修稿和本地模型。"
keywords: "ai-novel-writer, desktop, client, coding, deepseek harness, dsh"
---
# ai-novel-writer

> ⭐ **422** · ✅ 活跃 · 客户端 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 422 | 状态 | ✅ 活跃 |
| 作者 | [EthanYoQ](https://github.com/EthanYoQ) | 更新时间 | 2026-08-21 |

## 一句话介绍

> 本地优先 AI 小说创作工作台，提供 Windows/macOS 桌面版与 DeepSeek Harness 插件开发预览，支持角色、大纲、章节蓝图、审稿修稿和本地模型。

## 详细介绍

除了 Windows 与 macOS 桌面版，本仓库还在 [插件目录](https://github.com/EthanYoQ/AI-Novel-Writer/tree/master/plugins/dsh-ai-novel-writer) 维护 `@ethanyoq/dsh-ai-novel-writer` `0.1.0` 开发预览。DeepSeek Harness 的 V2 工作台是刻意收敛的早期 MVP，当前能力不足桌面软件版的 10%；它不读取桌面版 `.vela` 项目，也不能替代桌面版的项目树、批量工作流、成熟编辑器或自动审校。 V2 只提供人工审核的最小创作链：项目设置 → 故事架构 → 人物设定 → 全书纲要 → 逐章蓝图 → 逐章正文。模型生成的待审核建议到达 Proposal 收件箱后，会先填入右侧工作台的本地编辑表单，供人工查看和修改；只有用户明确审核并应用 Proposal，权威项目状态才会改变。 该插件不属于桌面版正式 Release，但已发布为独立 npm 包，拥有独立锁文件、CI 和 MIT 许可；仓库根目录仍为 GPL-3.0 桌面应用。将它安装到 DeepSeek Harness 的 `web` profile： dsh plugin --profile web add @ethanyoq/dsh-ai-novel-writer dsh --profile web 开发时也可以从源码安装： git clone https://github.com/EthanYoQ/AI-Novel-Writer.git cd AI-Novel-Writer/plugins/dsh-ai-novel-writer pnpm install pnpm run build dsh plugin --profile web add . dsh --profile 

## 📦 安装

```bash
dsh plugin --profile web add @ethanyoq/dsh-ai-novel-writer
dsh --profile web
```

## 🚀 快速开始

```bash
git clone https://github.com/EthanYoQ/AI-Novel-Writer.git
cd AI-Novel-Writer/plugins/dsh-ai-novel-writer
pnpm install
pnpm run build
dsh plugin --profile web add .
dsh --profile web
```

## 📚 更多信息

**模型配置**

目前支持两类调用协议： “自定义 API”指的是在上述协议范围内自定义地址、模型标识和凭据；它不是任意 HTTP 协议或可执行脚本编辑器。Anthropic、Azure、KoboldAI 原生协议等不同接口需要单独的适配器，不能仅靠替换 URL 保证兼容。

## 🔗 链接

- [GitHub 仓库](https://github.com/EthanYoQ/AI-Novel-Writer)
- [完整 README](https://github.com/EthanYoQ/AI-Novel-Writer#readme)
- [返回ai-novel-writer所在分类](../clients.md)
