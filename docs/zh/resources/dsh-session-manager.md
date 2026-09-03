---
title: "dsh-session-manager"
description: "DeepSeek Harness 会话管理设置面板：列出本机全部会话（运行中/空闲/已归档），支持继续会话、预览大纲、删除会话 | Session management settings section for dsh web: resume, outline, and delete any session"
keywords: "dsh-session-manager, search, plugin, coding, deepseek harness, dsh"
---
# dsh-session-manager

> ⭐ **5** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 5 | 状态 | ✅ 活跃 |
| 作者 | [Vim0x3c](https://github.com/Vim0x3c) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding |

## 一句话介绍

> DeepSeek Harness 会话管理设置面板：列出本机全部会话（运行中/空闲/已归档），支持继续会话、预览大纲、删除会话 | Session management settings section for dsh web: resume, outline, and delete any session

## 详细介绍

[English](README.en.md) | 中文 这可能是目前功能最全的 DSH 会话管理插件：在 DeepSeek Harness Web 界面中全面**管理会话**，设置页与对话顶部均提供入口——删除（回收站可恢复或彻底清除）、恢复已归档会话、近期活动统计、继续/暂停会话、打开日志目录、未读/已读标记、新聊天中继续（fork）、工作区分组与排序管理、上下文压缩阈值设置，不修改 DSH 核心代码。 本项目由 dsh + Deepseek-V4-Flash0731 独立完成 如果觉得有用，欢迎点个 ⭐ Star，谢谢支持！

## ✨ 核心特性

- 设置页新增独立的「会话管理」分栏（与 Notifications 同级的设置分区）
- 面板列出全部会话（标题 / 工作目录），底部折叠区单独展示**已归档会话**，支持**一键恢复**回到会话列表
- **回收站**：删除的会话移入回收站（保留最近 10 条，超出自动清除最早一条），可**恢复**或**彻底删除**
- **统计**：每个会话可在居中弹窗中查看完整近期活动统计（轮次 / 用户消息 / 助手消息 / 全部工具调用 / 活动窗口）
- **继续会话**：一键打开会话并关闭面板；**暂停**：停止正在运行会话的当前回合
- **未读 / 已读**：会话行标题旁显示状态点——手动未读为蓝色、官方等待输入为琥珀、官方完成提醒为绿色、运行中为转圈；点击官方状态点**就地已读**（不跳转），点击蓝色点清除未读，打开会话自动已读；官方侧边栏的对应会话行旁同步显示蓝色未读点
- **新聊天中继续**：每个会话一键 fork 子会话（官方 `sessions.fork`）并打开
- **文件夹**：在系统文件管理器中打开会话日志目录

## 📦 安装

```bash
dsh plugin --profile web add 'github:dream12347/dsh-session-manager#v0.2.2'
```

## 🚀 快速开始

```bash
# CMD
dsh plugin --profile web add github:dream12347/dsh-session-manager#v0.2.2
```

## 🔗 链接

- [GitHub 仓库](https://github.com/Vim0x3c/dsh-session-manager)
- [完整 README](https://github.com/Vim0x3c/dsh-session-manager#readme)
- [返回dsh-session-manager所在分类](../plugins.md)
