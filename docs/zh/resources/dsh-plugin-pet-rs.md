---
title: "dsh-plugin-pet-rs"
description: "Rust 桌宠：5 态鲸鱼 + 双 SSE 实时推送 + 透明置顶窗 + 系统托盘，三端支持。"
keywords: "dsh-plugin-pet-rs, ui, plugin, desktop, deepseek harness, dsh"
---
# dsh-plugin-pet-rs

> ⭐ **21** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 21 | 状态 | ✅ 活跃 |
| 作者 | [HuanLinOTO](https://github.com/HuanLinOTO) | 更新时间 | 2026-08-15 |
| 子分类 | 🐋 桌面宠物 | 能力 | ui, desktop |

## 一句话介绍

> Rust 桌宠：5 态鲸鱼 + 双 SSE 实时推送 + 透明置顶窗 + 系统托盘，三端支持。

## 详细介绍

DeepSeek Harness 桌面宠物鲸鱼，Rust 原生实现，三端支持（Windows / macOS / Linux）。

## ✨ 核心特性

- 🐋 5 态鲸鱼：`offline > attention > working > done > idle`
- ⚡ 双 SSE 实时推送（`events.mux` + `events.host`）+ 2s 轮询兜底
- 🎨 HD 像素画鲸鱼（80×58 网格）+ 喷水水滴动画 + zzz/spark 叠层
- 💬 状态气泡（多会话聚合列表，可滚动，popIn 动画）
- 🔔 状态提示音（attention / done，custom/ 可覆盖）
- 🖼️ 透明置顶悬浮窗 + 系统托盘 + 拖拽 + 大小调节
- ⚙️ 内嵌设置面板（双击鲸鱼打开）：声音开关、DSH 地址编辑、热切换
- 📦 `custom/sprites.json` 素材包 + `custom/*.m4a|mp3` 自定义音效

## 🚀 快速开始

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

## 📚 更多信息

**配置文件**

配置文件路径： { "scale": 0.67, "bubble_visible": true, "sound_on": true, "endpoint": "http://127.0.0.1:3080", "window_x": 2268, "window_y": 1084 } > 字段均可省略，缺省时使用默认值。旧版配置文件（无 `endpoint` 字段）自动兼容。

## 🔗 链接

- [GitHub 仓库](https://github.com/HuanLinOTO/dsh-plugin-pet-rs)
- [完整 README](https://github.com/HuanLinOTO/dsh-plugin-pet-rs#readme)
- [返回dsh-plugin-pet-rs所在分类](../plugins.md)
