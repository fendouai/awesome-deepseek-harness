---
title: "dsh-track"
description: "嵌入式任务管理引擎：决策点协议、念头捕获墙、Linear 形 issue 存储。"
keywords: "dsh-track, workflow, multi-agent, deepseek harness, dsh"
---
# dsh-track

> ⭐ **6** · ✅ 活跃 · 工作流

| | | | |
|---|---|---|---|
| 类型 | 工作流 | 分类 | 工作流 |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [fakechris](https://github.com/fakechris) | 更新时间 | 2026-08-20 |

## 一句话介绍

> 嵌入式任务管理引擎：决策点协议、念头捕获墙、Linear 形 issue 存储。

## 详细介绍

[English](README.en.md) | 中文 **状态** Active · **测试** 240 passing · **构建** `pnpm run build` · **版本** 0.6.0 ---

## ✨ 核心特性

- 🧠 **捕获墙（Capture Wall）** —— `capture_thought` 零摩擦收录念头；规划时的 `todo_write` 也会被自动捕获，且每条都携带**动机上下文**（当时那条用户请求），永远不会变成"无来由的琐碎清单"。
- ⚖️ **决策账本（Decision Ledger）** —— 遇到不可逆 / 风险 / 范围 / 验收类决策，先上报决策点，用户轻决策回答，**选择与理由**落盘可查（回答率进 funnel）。
- 📋 **任务生命周期（Evidence-driven Lifecycle）** —— Linear 兼容的任务模型；证据驱动的状态机，`done` / `canceled` **永不自动达成**，必须用户确认。
- 🔄 **历史同步（History Sync）** —— 一键把工作区过往会话折叠成 epic/issue 候选，默认 dry-run，确认后才落库。
- 💰 **LLM 用量账本（Usage Ledger）** —— track 引擎自己调用的 LLM 费用（token / 成本）单独计量，"track 花了多少 token" 一句话可查。
- 🖥️ **Web 面板** —— 右侧栏汇集墙 + 任务墙；每条记录都可 **「↩ 对话」跳回来源会话的那条原始 prompt**，高亮定位。
- 🕸️ **会话执行图（Session Graphs）** —— `track_session_graph` 把任意会话建成确定性的 turn→step→tool 执行树，每条边带 (sessionId, seq) 引用回原始日志；支持按工作区批量建图（幂等，可强制重建）；会话标签栏的「会话结构图」tab 实时渲染当前会
- 🧵 **日历纱线（Calendar Yarn）** —— 跨项目 session 生命周期 / 漂移 / 切换一图看清：泳道按事件量降序、零活动仓库折叠、「只看缠绕线」线级过滤；可导出**自包含可视化**（数据 JSON + HTML 视图 + README，浏览器直接打开即交互）。

## 📦 安装

```bash
pnpm install
pnpm run build      # tsc 产物 lib/ + client bundle
pnpm test           # vitest（188 tests）
```

## 🔗 链接

- [GitHub 仓库](https://github.com/fakechris/dsh-track)
- [完整 README](https://github.com/fakechris/dsh-track#readme)
- [返回dsh-track所在分类](../workflows.md)
