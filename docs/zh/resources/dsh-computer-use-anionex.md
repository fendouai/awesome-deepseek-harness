---
title: "dsh-computer-use"
description: "为 DeepSeek Harness 提供电脑控制插件：新鲜 Accessibility 观测、过期状态拒绝、作用域权限与安全输入（目前支持macos）｜Accessibility-first macOS Computer Use bundle for DSH with fresh observations, stale-state rejection, scoped permissions, and safe input."
keywords: "dsh-computer-use, browser, plugin, coding, deepseek harness, dsh"
---
# dsh-computer-use

> ⭐ **26** · ✅ 活跃 · 插件 · 近期 ⬆️ +4

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 浏览器控制 |
| 星数 | ⭐ 26 | 状态 | ✅ 活跃 |
| 作者 | [Anionex](https://github.com/Anionex) | 更新时间 | 2026-08-14 |

## 一句话介绍

> 为 DeepSeek Harness 提供电脑控制插件：新鲜 Accessibility 观测、过期状态拒绝、作用域权限与安全输入（目前支持macos）｜Accessibility-first macOS Computer Use bundle for DSH with fresh observations, stale-state rejection, scoped permissions, and safe input.

## 详细介绍

**Native macOS control for DeepSeek Harness that keeps your real cursor and foreground application alone by default; the Bundle may bring the target app forward before keyboard input for reliable typing.** DSH Computer Use gives an Agent fresh Accessibility observations, exact process/window targeting, stale-state rejection, scoped application access, and verified post-action state. Semantic Accessibility comes first; mouse, drag, wheel, and keyboard fallback are routed to the selected process instead of the global desktop.

## ✨ 核心特性

- **No system-cursor movement:** the helper contains no cursor-warp path.
- **No global pointer injection:** click, scroll, and drag fallback use a pid/window-targeted SkyLight route, not the global HID event stream.
- **No pointer-triggered activation:** semantic Accessibility, process-targeted pointer input, and `keyboardPolicy: preserve` run without activation; `keyboardPol
- **A separate Agent cursor:** click, scroll, and drag actions animate a click-through, nonactivating software cursor while the macOS system cursor remains untouc
- **No blind replay:** every action is tied to an exact, unexpired observation and returns fresh state.

## 📦 安装

```bash
dsh plugin --profile web add @anionex/dsh-computer-use
dsh plugin --profile headless add @anionex/dsh-computer-use

dsh --profile web --dump-config | grep computer-use
dsh --profile headless --dump-config | grep computer-use
```

## 🚀 快速开始

```bash
/computer-use
```

## 📚 更多信息

**Configuration**

<details> <summary>Show Bundle configuration fields</summary> </details> The deprecated 0.2.x `interaction.cursorMotionMs` field remains accepted so existing Settings documents load, but it is ignored at runtime and removed the next time Web Settings saves the configuration. Settings updates replace the active provider generation only after validation and health checks pass. Replacement invalidate

## 🔗 链接

- [GitHub 仓库](https://github.com/Anionex/dsh-computer-use)
- [完整 README](https://github.com/Anionex/dsh-computer-use#readme)
- [返回dsh-computer-use所在分类](../plugins.md)
