---
title: "dsh-kun-like-pet"
description: "Kun Like 桌宠 —— DeepSeek Harness 桌面宠物插件：右下角小坤宠随 Agent 工作状态切换 9 种动作，任务完成播放「你干嘛~哎哟」"
keywords: "dsh-kun-like-pet, fun, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-kun-like-pet

> ⭐ **80** · ✅ active · plugin · ⬆️ +7 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Fun & lifestyle |
| Stars | ⭐ 80 | Status | ✅ active |
| Author | [liyupi](https://github.com/liyupi) | Updated | 2026-08-14 |

## One-liner

> Kun Like 桌宠 —— DeepSeek Harness 桌面宠物插件：右下角小坤宠随 Agent 工作状态切换 9 种动作，任务完成播放「你干嘛~哎哟」

## About

- **9 种状态动画**：完全沿用 Codex 桌宠精灵图契约（8 列 × 9 行、每格 192×208），素材零重绘 - **实时感知 Agent 状态**：轮询 `agents` 服务感知每个 Agent 的 running/idle 状态，配合 `tools/execute`、`approval/request`、`agent/request-error` 事件推导工作 / 思考 / 等待 / 出错 / 空闲五种模式 - **任务完成全机可闻**：宿主进程用系统命令播放「你干嘛~哎哟」，任何窗口、任何会话完成任务都会响，与浏览器静音无关 - **可互动**：拖动桌宠到处跑（跑步动画方向跟随），点击它会挥手打招呼 - **内置调试工具**：`kun_pet_debug` 可随时查看状态机内部计数与轮询健康度

## ✨ Key Features

- **9 种状态动画**：完全沿用 Codex 桌宠精灵图契约（8 列 × 9 行、每格 192×208），素材零重绘
- **实时感知 Agent 状态**：轮询 `agents` 服务感知每个 Agent 的 running/idle 状态，配合 `tools/execute`、`approval/request`、`agent/request-error` 事件推导工作 / 思考 / 等待 / 出错 / 空闲五种模式
- **任务完成全机可闻**：宿主进程用系统命令播放「你干嘛~哎哟」，任何窗口、任何会话完成任务都会响，与浏览器静音无关
- **可互动**：拖动桌宠到处跑（跑步动画方向跟随），点击它会挥手打招呼
- **内置调试工具**：`kun_pet_debug` 可随时查看状态机内部计数与轮询健康度

## 📦 Install

```bash
git clone https://github.com/liyupi/dsh-kun-like-pet.git
```

## 🚀 Quick Start

```bash
const CONFIG = {
     spritePath: '/你的/路径/dsh-kun-like-pet/assets/spritesheet.webp',
     voicePath:  '/你的/路径/dsh-kun-like-pet/assets/voice.mp3',
     // macOS 默认用 afplay；Windows / Linux 请改成对应播放命令
     playCommand: (path) => "afplay '" + path.replace(/'/g, "'\\''") + "'",
   }
```

## 📚 Learn more

**方式二：直接预览动画（无需 DSH）**

打开 `demo/index.html`（建议起个静态服务器，如 `npx serve .` 或 `python3 -m http.server`），即可查看全部 9 种动画并拖动互动。

## 🔗 Links

- [GitHub Repository](https://github.com/liyupi/dsh-kun-like-pet)
- [Full README](https://github.com/liyupi/dsh-kun-like-pet#readme)
- [Back to the Plugins list](../plugins.md)
