---
title: "dsh-learn-everything"
description: "费曼学习模式：教→复述→评判→重讲循环，渲染为富 HTML 课程卡片。"
keywords: "dsh-learn-everything, learning, tutorial, ui, deepseek harness, dsh"
---
# dsh-learn-everything

> ⭐ **5** · ✅ 活跃 · 教程 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 教程 | 分类 | 学习 |
| 星数 | ⭐ 5 | 状态 | ✅ 活跃 |
| 作者 | [cendaifeng](https://github.com/cendaifeng) | 更新时间 | 2026-08-13 |

## 一句话介绍

> 费曼学习模式：教→复述→评判→重讲循环，渲染为富 HTML 课程卡片。

## 详细介绍

**一句话定位**：让 DeepSeek Harness 变成"边学边做"的环境——开启学习模式后，模型按费曼学习法讲解概念、出卡片题请你复述、针对缺口重新讲解，教学内容以富 HTML 卡片可视化呈现。

## ✨ 核心特性

- 会话级 `/learn on|off` 切换；开启后注入费曼教学引导（`learning:policy` prompt 段），关闭后完全恢复默认行为。
- 模型经 `teach` 工具产出结构化 Lesson（标题、一句话总结、小节：正文/代码/mermaid 图/类比、可选 raw HTML），Web 客户端经 `tool.call.toolview` keyed 视图渲染为富 HTML 卡片：代码经 shell shiki 高亮（语言横幅 + 复制），mermaid 
- 答题复用现有 `ask_user_question`（卡片选项由 `ui-user-questions` 呈现）；模型在下一步自行判定对错并讲解。
- 模式状态是 log-only `learning/mode` session event：resume/fork/compaction 从日志折叠恢复，无 live mirror。
- 每次会话独立，无跨会话长期记忆。
- 零 mainline core 改动：不加 card kind、不改 agent-loop、不加新事件族（Lesson 卡片直接消费既有 `tool/call` 日志）。

## 🔗 链接

- [GitHub 仓库](https://github.com/cendaifeng/dsh-learn-everything)
- [完整 README](https://github.com/cendaifeng/dsh-learn-everything#readme)
- [返回dsh-learn-everything所在分类](../tutorials.md)
