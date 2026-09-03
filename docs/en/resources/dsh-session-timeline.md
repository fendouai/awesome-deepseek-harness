---
title: "dsh-session-timeline"
description: "DeepSeek Harness 会话时间轴插件：横短横线波浪、当前消息定位、点击跳转、圆角预览 tooltip、可收起/展开"
keywords: "dsh-session-timeline, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-session-timeline

> ⭐ **5** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 5 | Status | ✅ active |
| Author | [XiLuovo](https://github.com/XiLuovo) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> DeepSeek Harness 会话时间轴插件：横短横线波浪、当前消息定位、点击跳转、圆角预览 tooltip、可收起/展开

## About

[English](README.en.md) | 中文 DeepSeek Harness 会话时间轴插件：在会话左侧渲染一条**横短横线时间轴**，用于在长会话中快速定位、跳转和预览。

## ✨ Key Features

- **横短横线时间轴**：只在用户输入的位置显示一条横向短横线，无消息处无线；条数等于**整个会话**的用户消息数，放得下时居中排布，放不下时时间轴内部滚动（无滚动条）。
- **全量统计（投影机制）**：通过 DSH sessionProjections 增量统计整个会话的用户消息与 AI 回复预览，持久化缓存保证刷新秒出、新消息实时更新；对长会话压力可控。
- **当前消息定位（scroll-spy）**：激活条始终对应右侧视口当前显示的那条用户消息；滚动右侧对话，激活条随之移动（手动滚动时间轴后保持不动，点击某条跳转后恢复跟随）。
- **波浪聚焦**：鼠标在时间轴上移动时，鼠标接近的那条变为激活色并变长，相邻条向上下递减，形成波浪效果。
- **圆角预览 tooltip**：悬停某条时立即显示圆角提示——第一行用户消息（黑色加粗、单行省略），下方 AI 回复（灰色、多行），时间贴在最后一行右下角；字体与右侧对话一致。窗口外的历史消息同样可以预览。
- **点击跳转**：点击任意横线，对话立即滚动到该次用户输入所在位置；窗口外（未加载）的历史消息会自动加载更早历史后跳转。
- **收起 / 展开**：第一条消息上方有一个悬停淡入的**胶囊把手**（点击收起；悬停时第一、二条灰色递减，胶囊扮演激活条角色）。收起后变成一条**全高细竖条**，常态隐藏，鼠标接近识别区域时淡入，点击展开。任何滚动位置，胶囊与最上方条目之间始终保留固定空白。

## 📦 Install

```bash
dsh plugin --profile web add dsh-session-timeline
```

## 🚀 Quick Start

```bash
dsh web
```

## 📚 Learn more

**方式一：npm 安装（推荐）**

已发布到 npm，预构建安装**无需 GitHub 构建授权**： dsh plugin --profile web add dsh-session-timeline 然后启动（或重启）web： dsh web

**方式二：GitHub 安装**

dsh plugin --profile web add github:XiLuovo/dsh-session-timeline 然后启动（或重启）web： dsh web > 本包是纯 JS 实现，`client.js` 即最终 bundle 产物，**无需 prepare 构建脚本**，GitHub 直接安装即可用。

**方式三：本地目录安装（开发调试）**

git clone https://github.com/XiLuovo/dsh-session-timeline.git dsh plugin --profile web add ./dsh-session-timeline dsh web

## 🔗 Links

- [GitHub Repository](https://github.com/XiLuovo/dsh-session-timeline)
- [Full README](https://github.com/XiLuovo/dsh-session-timeline#readme)
- [Back to the Plugins list](../plugins.md)
