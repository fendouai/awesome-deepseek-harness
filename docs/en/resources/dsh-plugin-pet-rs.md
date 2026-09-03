---
title: "dsh-plugin-pet-rs"
description: "Rust desktop pet: 5-state whale with dual SSE real-time push, transparent always-on-top window and system tray."
keywords: "dsh-plugin-pet-rs, ui, plugin, desktop, deepseek harness, dsh"
---
# dsh-plugin-pet-rs

> ⭐ **21** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 21 | Status | ✅ active |
| Author | [HuanLinOTO](https://github.com/HuanLinOTO) | Updated | 2026-08-15 |
| Subcategory | 🐋 Desktop pets | Capabilities | ui, desktop |

## One-liner

> Rust desktop pet: 5-state whale with dual SSE real-time push, transparent always-on-top window and system tray.

## About

DeepSeek Harness 桌面宠物鲸鱼，Rust 原生实现，三端支持（Windows / macOS / Linux）。

## ✨ Key Features

- 🐋 5 态鲸鱼：`offline > attention > working > done > idle`
- ⚡ 双 SSE 实时推送（`events.mux` + `events.host`）+ 2s 轮询兜底
- 🎨 HD 像素画鲸鱼（80×58 网格）+ 喷水水滴动画 + zzz/spark 叠层
- 💬 状态气泡（多会话聚合列表，可滚动，popIn 动画）
- 🔔 状态提示音（attention / done，custom/ 可覆盖）
- 🖼️ 透明置顶悬浮窗 + 系统托盘 + 拖拽 + 大小调节
- ⚙️ 内嵌设置面板（双击鲸鱼打开）：声音开关、DSH 地址编辑、热切换
- 📦 `custom/sprites.json` 素材包 + `custom/*.m4a|mp3` 自定义音效

## 🚀 Quick Start

```bash
┌───────────────────────────────┐
│ 设置                      ×   │
│                               │
│ 声音提醒              [ON/OFF] │
│                               │
│ DSH 地址                       │
│ ┌───────────────────────────┐ │
│ │ http://127.0.0.1:3080│    │ │
│ └───────────────────────────┘ │
└───────────────────────────────┘
```

## 📚 Learn more

**配置文件**

配置文件路径： { "scale": 0.67, "bubble_visible": true, "sound_on": true, "endpoint": "http://127.0.0.1:3080", "window_x": 2268, "window_y": 1084 } > 字段均可省略，缺省时使用默认值。旧版配置文件（无 `endpoint` 字段）自动兼容。

## 🔗 Links

- [GitHub Repository](https://github.com/HuanLinOTO/dsh-plugin-pet-rs)
- [Full README](https://github.com/HuanLinOTO/dsh-plugin-pet-rs#readme)
- [Back to the Plugins list](../plugins.md)
