---
title: "dsh-plugin-spur"
description: "Hang a whip in the chat stream: flick it (>2.0 px/ms) to send the agent a 'go work' message."
keywords: "dsh-plugin-spur, workflow, ui, deepseek harness, dsh"
---
# dsh-plugin-spur

> ⭐ **6** · ✅ active · workflow · ⬆️ +3 recently

| | | | |
|---|---|---|---|
| Type | workflow | Category | Workflows |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [HuanLinOTO](https://github.com/HuanLinOTO) | Updated | 2026-08-15 |

## One-liner

> Hang a whip in the chat stream: flick it (>2.0 px/ms) to send the agent a 'go work' message.

## About

一根悬挂在 DSH 聊天流中的辫子（皮鞭）。抓住辫梢甩动——速度足够快时，向 agent 发送一条 `go work!` 消息，鞭策它去干活。

## ✨ Key Features

- Verlet 物理引擎渲染的辫子，作为 `position: fixed` 的 SVG 叠层，锚定在视口右上角，垂入聊天区域。
- 辫梢圆点是唯一可抓取的元素（在整体 `pointer-events: none` 的叠层上设为 `pointer-events: auto`）。
- 鼠标按下 → 辫梢锁定到光标；鼠标移动 → 跟踪速度（指数移动平均）；鼠标释放 → 带末速度释放。
- 释放速度超过阈值（2.0 px/ms）时：
- 释放后辫子继续摆动，阻尼振荡直至静止。

## 📦 Install

```bash
pnpm install          # 安装开发依赖
pnpm run typecheck    # tsc --noEmit（通过 ../dsh 解析 DSH 源码）
pnpm test             # vitest run（物理引擎单元测试）
pnpm run build        # tsc + tsdown → lib/index.js, lib/invariant.js, lib/client.js
```

## 🚀 Quick Start

```bash
# 从 npm 安装（推荐）：
dsh plugin --profile web add @huanlin/dsh-plugin-spur
```

## 🔗 Links

- [GitHub Repository](https://github.com/HuanLinOTO/dsh-plugin-spur)
- [Full README](https://github.com/HuanLinOTO/dsh-plugin-spur#readme)
- [Back to the Workflows & Automation list](../workflows.md)
