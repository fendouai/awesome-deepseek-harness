---
title: "dsh-split-panes"
description: "Split panes."
keywords: "dsh-split-panes, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-split-panes

> ⭐ **5** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 5 | 状态 | ✅ 活跃 |
| 作者 | [lehhair](https://github.com/lehhair) | 更新时间 | 2026-08-15 |

## 一句话介绍

> Split panes.

## 详细介绍

DSH 对话分屏插件（PiUI 风格）：把信息流分成多个可独立操作的窗格，每个窗格绑定自己的会话——分屏/层叠、四向拖拽分配、侧边栏会话拖入、单行融合 header。信息流本体完全复用原生渲染，插件只做容器与交互。

## ✨ 核心特性

- **分屏组合**：header 操作行分屏按钮 + `mod+shift+方向键`（左右/上下），`mod+shift+w` 关闭窗格；分隔条可拖拽、可键盘调节（比例 0.1–0.9）
- **每窗格独立会话**：通过框架的 `SessionScope` 座位把每个窗格绑定到各自的会话；分屏是**纯视图操作**——新窗格是"新建对话"占位（不创建 host 会话），在占位窗格里开始对话时才真正创建会话并绑定到该窗格，互不干扰
- **侧边栏拖拽分配**：把侧边栏会话拖到窗格上——中心落下替换该窗格会话，四条边缘落下向该侧分屏（被拖会话进新窗格，焦点跟随）；拖拽通道完全插件化（capture dragstart 反查）
- **原生视觉**：未分屏时逐字节等同原生（无边框、无 chrome）；分屏后窗格带焦点蓝边框（选中 `deepseek-500` / 未选中灰）；header 单行化 + PiUI 渐变 + 内容留白

## 📦 安装

```bash
git clone https://github.com/lehhair/dsh-split-panes.git
dsh plugin --profile web add link:/path/to/dsh-split-panes
```

## 🚀 快速开始

```bash
pnpm install        # devDeps link 到 ../dsh2026/deepseek-harness（DSH 源码，需先构建其 client 包）
pnpm run check      # typecheck + test + build
```

## 📚 更多信息

**安装**

git clone https://github.com/lehhair/dsh-split-panes.git dsh plugin --profile web add link:/path/to/dsh-split-panes 重启 `dsh web` 即可使用（右上角/header 出现分屏按钮）。

## 🔗 链接

- [GitHub 仓库](https://github.com/lehhair/dsh-split-panes)
- [完整 README](https://github.com/lehhair/dsh-split-panes#readme)
- [返回dsh-split-panes所在分类](../plugins.md)
