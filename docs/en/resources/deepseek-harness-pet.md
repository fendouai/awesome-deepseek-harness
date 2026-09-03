---
title: "deepseek-harness-pet"
description: "A Windows desktop pet that visualizes DeepSeek Harness task progress."
keywords: "deepseek-harness-pet, desktop, client, coding, deepseek harness, dsh"
---
# deepseek-harness-pet

> ⭐ **23** · ✅ active · client

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 23 | Status | ✅ active |
| Author | [wraven68](https://github.com/wraven68) | Updated | — |

## One-liner

> A Windows desktop pet that visualizes DeepSeek Harness task progress.

## About

Codex 风格的「桌面宠物」DSH 客户端插件：在 DeepSeek Harness（DSH）Web GUI 里漂浮一只动画小宠物，由当前会话的 **agent 运行状态**实时驱动（工作 / 等待输入 / 报错 / 刚完成 / 待机）。

## ✨ Key Features

- **漂浮宠物**：注册进 DSH 的 `shell.overlay` 槽（帧级浮动层，可点透，右下角常驻，可拖拽换位）。
- **状态驱动**：读当前会话状态并映射到 Codex 的 9 状态动画行；会话信号按 Codex `ambient.rs` 的**存活期**衰减（Running 3min / Failed 1h / Waiting 24h / Review 7d，超时回退 idle）：
- **减少动态**：跟随系统 `prefers-reduced-motion`，或在设置里手动锁定「完整 / 减少动态」；减少动态时按 Codex 行为固定显示 idle 第一帧。
- **交互**：
- **养成数值**：🍖 饱食 / 😊 心情 0–100，随**墙钟时间**衰减（关掉浏览器也计时，约 8h / 6h 见底）；喂食 +30 饱食、玩耍 +25 心情；菜单里有两条数值条，待机且某项 <20 时宠物会冒「🍖 饿了 / 🎾 想玩」提示。
- **多宠物**：内置五只宠物——Dee（青绿）/ Amber（琥珀）/ Berry（莓紫）同模配色，以及**灰鲸**（DeepSeek Harness logo 造型）/ **蓝鲸**（DeepSeek 官方 logo 造型，品牌蓝）两只侧视鲸鱼，设置面板一键切换。

## 📦 Install

```bash
# 从 npm（发布后）
dsh plugin --profile web add @minybear/dsh-pet

# 或一条命令装本地 checkout（包自带 dsh.bundle.patch 自注册）
dsh plugin --profile web add .

# 或从 GitHub
dsh plugin --profile web add github:minybear/DeepSeek-Harness-Pet
```

## 🚀 Quick Start

```bash
lib/pet-core.js    纯逻辑（Node 可测）：pet.json 解析 + 帧切片 + 状态机 + 状态存活期
lib/index.js       host 侧 apply（空，纯 UI 插件）
lib/client.js      浏览器侧：window.__ModuleLoader__.load + apply/inject + PetOverlay + 精灵生成
test/*.test.mjs    Node 单测（pet-core + client 契约 + 双副本一致性）
docs/              调研、方案与差距分析
```

## 🔗 Links

- [GitHub Repository](https://github.com/wraven68/deepseek-harness-pet)
- [Full README](https://github.com/wraven68/deepseek-harness-pet#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
