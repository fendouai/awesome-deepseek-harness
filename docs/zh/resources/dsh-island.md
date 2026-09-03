---
title: "dsh-island"
description: "通过 Unix socket 把 DSH agent 的会话、工具调用与审批实时桥接到 CodeIsland macOS 刘海面板，可直接在面板上批准/拒绝。"
keywords: "dsh-island, notifications, plugin, deepseek harness, dsh"
---
# dsh-island

> ⭐ **6** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 通知 |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [cdxiaodong](https://github.com/cdxiaodong) | 更新时间 | 2026-08-17 |

## 一句话介绍

> 通过 Unix socket 把 DSH agent 的会话、工具调用与审批实时桥接到 CodeIsland macOS 刘海面板，可直接在面板上批准/拒绝。

## 详细介绍

**交互式预览（浏览器直接体验）**：`docs/` 下是一整套可运行的产品预览。本地起一个静态服务器即可逐页体验全部交互： cd docs && python3 -m http.server 8080

## ✨ 核心特性

- **自动拉起**：插件加载即常驻菜单栏（已运行则不重复启动）
- **动态菜单栏**：按钮文案随状态变（空闲/运行中/等待授权）
- **会话状态**：`SessionStart` / `SessionEnd` 跟随 DSH 会话生命周期
- **工具调用**：`PreToolUse` / `PostToolUse` / `PostToolUseFailure` 实时展示正在执行的工具
- **面板审批**：`approval/request` → 面板出现「需要授权」卡，点「允许 / 拒绝」直接回写 DSH
- **子代理**：`SubagentStart` / `SubagentStop`
- **状态变化**：`agent/status` → 面板状态灯与提示
- **零侵入**：不修改 DSH 配置、不拦截工具决策（`next()` 总是放行）

## 📦 安装

```bash
dsh plugin --profile <profile> add github:cdxiaodong/dsh-island
```

## 🚀 快速开始

```bash
DSH 进程
  └─ dsh-island 插件（cordis）
       ├─ apply() 时 spawn → bin/dsh-island-panel（Swift 原生，常驻菜单栏）
       ├─ 监听 DSH 事件（session/tools/approval/subagent/status）
       └─ Unix socket /tmp/dsh-island-<uid>.sock → 菜单栏图标 + 面板实时更新
                            ↑ 面板上点「允许/拒绝」→ 决策回写 DSH
```

## 📚 更多信息

**🎬 功能预览**

**交互式预览（浏览器直接体验）**：`docs/` 下是一整套可运行的产品预览。本地起一个静态服务器即可逐页体验全部交互： cd docs && python3 -m http.server 8080

**⚡ 快速安装**

dsh plugin --profile <profile> add github:cdxiaodong/dsh-island 前提：macOS 14+（面板为 arm64 二进制；Intel 需自行用 `panel/build.sh` 重编）。 ---

**配置**

interface Config { socketPath?: string // 面板 socket（默认 /tmp/dsh-island-<uid>.sock） source?: string // 上报的 source 标识（默认 dsh） approvalTimeoutMs?: number // 审批等待面板决策超时（默认 5 分钟） approvals?: boolean // 是否把审批转发给面板（默认 true） subagents?: boolean // 是否上报子代理事件（默认 true） agentStatus?: boolean // 是否上报 agent 状态（默认 true） autoLaunchPanel?: boolean // apply 时自动拉起面板（默认 true） panelBin?: string // 覆盖面板二进制路径 debug?: bo

**🗺️ 路线图 Roadmap**

以下能力已进入产品设计（见上方功能预览），正在陆续落地： > 想看每一步的真实交互？运行上方「功能预览」里的演示即可 —— 界面、动效、状态流转皆是可点击的。 ---

## 🔗 链接

- [GitHub 仓库](https://github.com/cdxiaodong/dsh-island)
- [完整 README](https://github.com/cdxiaodong/dsh-island#readme)
- [返回dsh-island所在分类](../plugins.md)
