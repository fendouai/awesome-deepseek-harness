---
title: "dsh-pet"
description: "🐋 DSH 有声桌宠：悬浮桌面的 DeepSeek 小鲸鱼，不打开 DSH 也能实时感知会话状态（需要确认/工作中/完成/空闲/离线），支持音效提醒与零代码定制素材"
keywords: "dsh-pet, fun, plugin, coding, deepseek harness, dsh"
---
# dsh-pet

> ⭐ **13** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 娱乐与生活 |
| 星数 | ⭐ 13 | 状态 | ✅ 活跃 |
| 作者 | [FlytoMAYDAY80](https://github.com/FlytoMAYDAY80) | 更新时间 | 2026-08-17 |

## 一句话介绍

> 🐋 DSH 有声桌宠：悬浮桌面的 DeepSeek 小鲸鱼，不打开 DSH 也能实时感知会话状态（需要确认/工作中/完成/空闲/离线），支持音效提醒与零代码定制素材

## 详细介绍

- **离屏状态感知**：独立置顶悬浮窗，跨全屏 App 可见，不打开 DSH 也能看见状态 - **人工介入零遗漏**：「需要确认」（审批/提问）最高优先级呈现 + 专属音效，不会错过需要你的节点 - **毫秒级实时**：双 WebSocket 通道（审批/提问推送 + 运行状态翻转推送），状态变化即时响应 - **跨会话聚合**：多会话并行时气泡逐行列出每个会话，数量再多也可滚动查看 - **低打扰**：只在状态真正变化时动画/发声，不刷存在感 - **对 DSH 零侵入**：纯只读 HTTP/WebSocket 接口，不写入任何数据，卸载即消失 - **零代码定制**：`custom/` 目录一键换图案、配色、音效（见下方"定制"）

## ✨ 核心特性

- **离屏状态感知**：独立置顶悬浮窗，跨全屏 App 可见，不打开 DSH 也能看见状态
- **人工介入零遗漏**：「需要确认」（审批/提问）最高优先级呈现 + 专属音效，不会错过需要你的节点
- **毫秒级实时**：双 WebSocket 通道（审批/提问推送 + 运行状态翻转推送），状态变化即时响应
- **跨会话聚合**：多会话并行时气泡逐行列出每个会话，数量再多也可滚动查看
- **低打扰**：只在状态真正变化时动画/发声，不刷存在感
- **对 DSH 零侵入**：纯只读 HTTP/WebSocket 接口，不写入任何数据，卸载即消失
- **零代码定制**：`custom/` 目录一键换图案、配色、音效（见下方"定制"）

## 📦 安装

```bash
pnpm install   # 安装依赖（Electron）
pnpm start     # 启动桌宠（默认右下角）
```

## 🚀 快速开始

```bash
custom/
├── sprites.json      ← 像素图案 + 配色（可用脚本从参考图生成）
├── attention.m4a     ← 「需要确认」音效
└── done.m4a          ← 「任务完成」音效
```

## 📚 更多信息

**⬇️ 下载与安装**

**方式一：下载安装包（推荐）** — 从 [GitHub Releases](https://github.com/FlytoMAYDAY80/dsh-pet/releases/latest) 下载： **方式二：从源码运行** — 需要 [Node.js](https://nodejs.org) 18+ 与 [pnpm](https://pnpm.io)： pnpm install # 安装依赖（Electron） pnpm start # 启动桌宠（默认右下角） > 可选：`DSH_PET_URL=http://127.0.0.1:3080` 指定 DSH GUI 地址（默认 3080）。

## 🔗 链接

- [GitHub 仓库](https://github.com/FlytoMAYDAY80/dsh-pet)
- [完整 README](https://github.com/FlytoMAYDAY80/dsh-pet#readme)
- [返回dsh-pet所在分类](../plugins.md)
