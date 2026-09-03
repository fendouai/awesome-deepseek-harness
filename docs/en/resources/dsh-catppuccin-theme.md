---
title: "dsh-catppuccin-theme"
description: "DeepSeek Harness Web GUI 的 Catppuccin 主题插件：Latte / Frappé / Macchiato / Mocha 四种主题一键切换，内置可开关的玻璃质感（Glassmorphism）"
keywords: "dsh-catppuccin-theme, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-catppuccin-theme

> ⭐ **22** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 22 | Status | ✅ active |
| Author | [NoNameLeGo](https://github.com/NoNameLeGo) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, ui |

## One-liner

> DeepSeek Harness Web GUI 的 Catppuccin 主题插件：Latte / Frappé / Macchiato / Mocha 四种主题一键切换，内置可开关的玻璃质感（Glassmorphism）

## About

[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 的 [Catppuccin](https://github.com/catppuccin/catppuccin) 主题插件——一个包同时适配 **Web GUI**（`dsh web`）、**DSH Desktop** 与 **dsh-TUI** 终端：Web / 桌面端做全界面换色与玻璃质感， TUI 端自动同步四套官方主题色板。 它内置 Catppuccin 的四个主题——**Latte**、**Frappé**、**Macchiato**、**Mocha**—— 把整个界面的配色都换成对应的 Catppuccin 色板；并在 **设置 → 常规 → 外观** 下方提供一行 **Catppuccin** 快捷切换，选择会自动保存、重启自动恢复。 同时内置一套可开关的**玻璃质感**（Glassmorphism）皮肤：顶栏、侧边栏、 输入框、统计行、轨迹视图、聊天气泡、新会话按钮都变成磨砂玻璃卡片， 模糊度、磨砂度、背景亮度均可自由调节，玻璃颜色自动跟随当前 Catppuccin 主题。

## ✨ Key Features

- 🎨 四个主题：Latte（浅色）、Frappé / Macchiato / Mocha（深色）
- 🧩 接入官方主题系统，与内置浅色 / 深色 / 跟随系统主题平级
- 🎯 全界面配色覆盖，不只是一两个强调色
- ⚙️ 设置页一行切换，选择自动保存、重启自动恢复
- 🌐 中英文双语文案（跟随系统语言）
- 🪟 **玻璃质感**：顶栏 / 侧边栏 / 输入框 / 统计行 / 轨迹视图 / 聊天气泡 /
- 🌫️ **玻璃拟态细节**：页面上下边缘渐变模糊、折叠侧边栏悬浮玻璃、
- 🎨 玻璃配色自动跟随当前 Catppuccin 主题

## 📦 Install

```bash
dsh plugin --profile web add @nonamelego/dsh-catppuccin
```

## 🚀 Quick Start

```bash
dsh plugin --profile desktop add @nonamelego/dsh-catppuccin
```

## 📚 Learn more

**特性**

新会话按钮磨砂玻璃效果，设置里一键开关；云母 / 兼容双模式，模糊度、磨砂度、 背景亮度自由调节（交互参考 [DSH-Transparent-UI-Plugin](https://github.com/WYH66666666/DSH-Transparent-UI-Plugin)） 纯色背景跟随主题底色——内容滚入视口边缘时柔化穿过，层次更立体

**预览**

四个主题在 DeepSeek Harness 中的实际效果（截图来自本地 GUI，文首大图为四主题斜切合成）： <details> <summary>🌻 Latte（浅色）</summary>  </details> <details> <summary>🪴 Frappé（深色）</summary>  </details> <details> <summary>🌺 Macchiato（深色）</summary>  </details> <details> <summary>🌿 Mocha（深色）</summary>  </details>

**方式一：从 npm 安装（推荐）**

dsh plugin --profile web add @nonamelego/dsh-catppuccin 装完重启 `dsh web` 即可，`dsh plugin` 会自动把它加进 profile 的 bundles。 其他 profile 把命令里的 `web` 换成对应名字即可（如 `headless`）。 **[DSH Desktop](https://github.com/anywhere-labs/deepseek-harness-desktop)**：桌面版默认激活的 profile 就叫 `desktop`，把命令里的 `web` 换成 `desktop` 即可： dsh plugin --profile desktop add @nonamelego/dsh-catppuccin 在桌面的 **DSH 终端**里运行即可（`dsh plugin` 默认作用于当前激活

**方式二：从仓库安装**

dsh plugin --profile web add https://github.com/NoNameLeGo/dsh-catppuccin-theme 从 git 安装时 pnpm 可能要求允许构建脚本——按 pnpm 的提示把对应包加进 profile `pnpm-workspace.yaml` 的 `allowBuilds` 后重跑一次即可。

## 🔗 Links

- [GitHub Repository](https://github.com/NoNameLeGo/dsh-catppuccin-theme)
- [Full README](https://github.com/NoNameLeGo/dsh-catppuccin-theme#readme)
- [Back to the Plugins list](../plugins.md)
