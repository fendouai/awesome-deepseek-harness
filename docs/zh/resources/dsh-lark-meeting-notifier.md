---
title: "dsh-lark-meeting-notifier"
description: "一个只有副作用的DeepSeekHarness插件：在你跟 AI 聊得神魂颠倒时，提醒你「该去跟碳基生命开会了」。"
keywords: "dsh-lark-meeting-notifier, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-lark-meeting-notifier

> ⭐ **7** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 7 | 状态 | ✅ 活跃 |
| 作者 | [yeruizhi](https://github.com/yeruizhi) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> 一个只有副作用的DeepSeekHarness插件：在你跟 AI 聊得神魂颠倒时，提醒你「该去跟碳基生命开会了」。

## 详细介绍

一个 DeepSeek Harness（DSH）插件：在工作区右侧显示一个可展开/收起的悬浮框，列出**今天剩余的飞书会议**，让你埋头写代码时不会错过会议。 - 会议室名称（从飞书日历的「会议室」资源参会人读取） - 多闹钟提醒：每个提醒提前量独立触发，开始前到点闪烁（黄/橙/红随紧迫度） - 点击会议记录关闭当前提醒（关闹钟）；可开启「30 秒后自动停止闪烁」 - 提醒触发时自动展开面板（可关） - 单条「✕」移除提醒（本地持久化，不会动飞书日历里的真实日程） - 开始时间已过的会议自动移除；今日会议清空时可查看「明日」会议 - 配置持久化，设置面板可调 ---

## ✨ 核心特性

- 会议室名称（从飞书日历的「会议室」资源参会人读取）
- 多闹钟提醒：每个提醒提前量独立触发，开始前到点闪烁（黄/橙/红随紧迫度）
- 点击会议记录关闭当前提醒（关闹钟）；可开启「30 秒后自动停止闪烁」
- 提醒触发时自动展开面板（可关）
- 单条「✕」移除提醒（本地持久化，不会动飞书日历里的真实日程）
- 开始时间已过的会议自动移除；今日会议清空时可查看「明日」会议

## 📦 安装

```bash
dsh plugin --profile web add github:yeruizhi/dsh-lark-meeting-notifier
```

## 🚀 快速开始

```bash
npm install -g @larksuite/cli
```

## 📚 更多信息

**安装**

dsh plugin --profile web add github:yeruizhi/dsh-lark-meeting-notifier 然后重启 `dsh web`（或 `npx @deepseek-ai/dsh web`）。页面右侧会出现「🕐 会议」小胶囊。

**前置条件：lark-cli 安装与授权**

本插件通过 [`@larksuite/cli`](https://www.npmjs.com/package/@larksuite/cli)（命令名 `lark-cli`）读取飞书日历。

**1. 安装 lark-cli**

npm install -g @larksuite/cli 验证：`lark-cli --version` 应输出 `lark-cli version x.y.z`。

## 🔗 链接

- [GitHub 仓库](https://github.com/yeruizhi/dsh-lark-meeting-notifier)
- [完整 README](https://github.com/yeruizhi/dsh-lark-meeting-notifier#readme)
- [返回dsh-lark-meeting-notifier所在分类](../plugins.md)
