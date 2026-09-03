---
title: "dsh-turn-index"
description: "回合索引侧栏：每个用户回合一条，点击跳转，滚动监听高亮。"
keywords: "dsh-turn-index, ui, plugin, deepseek harness, dsh"
---
# dsh-turn-index

> ⭐ **1** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [Simon314620](https://github.com/Simon314620) | 更新时间 | 2026-08-13 |
| 子分类 | 🖥️ 侧边栏与面板 | 能力 | ui |

## 一句话介绍

> 回合索引侧栏：每个用户回合一条，点击跳转，滚动监听高亮。

## 详细介绍

对话轮次索引：在 DeepSeek Harness Web GUI 右侧挂一条侧边栏，按顺序列出每一轮「你问过的话」。点击任意一条，聊天流平滑滚动到那一轮并闪烁高亮；滚动阅读时侧边栏同步高亮当前轮次。 A turn-index sidebar for the DeepSeek Harness web GUI: one entry per user turn, click to jump, scroll-spy keeps the current turn highlighted. ┌──────────────────────────────┬───────┐ │ 聊天流 │ 轮次 2│ │ │ ─────│ │ ▸ #1 帮我查一下……（点击跳转） │ #1 │ │ │ #2 ▸ │ └──────────────────────────────┴───────┘

## ✨ 核心特性

- **逐轮索引**：每条索引 = 一轮用户提问的开场消息；轮次内穿插的补充提问（steering）以 ↳ 缩进显示，不打断轮次编号。
- **点击跳转**：直接定位聊天流里对应的消息行，平滑滚动 + 1.6 秒闪烁高亮（尊重系统的减少动效偏好）。
- **阅读联动**：滚动阅读时索引自动高亮当前轮次，展开态的列表自动跟随，当前轮次始终可见。
- **历史分页**：会话历史窗口未加载完时，顶部出现「加载更早的轮次」，点一下继续向前加载。
- **轨迹视图兜底**：停留在轨迹视图时点击索引，给出提示并一键切回对话。
- **避让右侧详情面板**：工具详情（details）打开时索引栏自动左移避让。
- **响应式**：视口 ≤1024px 自动收成 44px 窄条（只留轮次圆点）；1280px 以下面板收窄；面板高度贴合聊天流区域（不遮 Session log、不压输入框）；偏好记忆在 localStorage。
- **双语文案**：通过 harness 的 locale 服务提供 中文 / English 文案，跟随界面语言。

## 📦 安装

```bash
# npm（推荐，已发布 v0.1.1）
dsh plugin --profile web add dsh-turn-index

# GitHub tag tarball
dsh plugin --profile web add https://github.com/Simon314620/dsh-turn-index/archive/refs/tags/v0.1.1.tar.gz

# 本地目录（开发调试）
dsh plugin --profile web add file:D:/path/to/dsh-turn-index
```

## 🚀 快速开始

```bash
dsh plugin --profile web remove dsh-turn-index
```

## 📚 更多信息

**实现原理**

纯客户端插件：宿主侧（Node）无运行时逻辑，浏览器半边通过 `shell.overlay` 槽位（AppFrame 的加性浮层席位）挂载面板。会话数据取自 `ctx.sessions.binding(currentId).session`（`ConversationSnapshot` 的可观察快照），索引条目从 `chat.order` 中筛出 kind 为 `user` / `steering` 的可见节点；跳转时按节点 key 查找聊天流里带 `data-chat-anchor-key` 属性的 DOM 行（聊天流无虚拟化，行都在 DOM 里），因此跳转天然可靠。面板几何（上下界、details 避让）动态测量 `[data-conversation-scroll]`、`[data-composer-seat]` 与 AppFrame 的 grid 第三轨。

## 🔗 链接

- [GitHub 仓库](https://github.com/Simon314620/dsh-turn-index)
- [完整 README](https://github.com/Simon314620/dsh-turn-index#readme)
- [返回dsh-turn-index所在分类](../plugins.md)
