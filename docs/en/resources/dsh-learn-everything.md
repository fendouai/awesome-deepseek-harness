---
title: "dsh-learn-everything"
description: "Feynman learning-mode plugin: teach → teach-back → judge → re-explain loop rendered as rich HTML lesson cards."
keywords: "dsh-learn-everything, learning, tutorial, ui, deepseek harness, dsh"
---
# dsh-learn-everything

> ⭐ **5** · ✅ active · tutorial · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | tutorial | Category | Learning |
| Stars | ⭐ 5 | Status | ✅ active |
| Author | [cendaifeng](https://github.com/cendaifeng) | Updated | 2026-08-13 |

## One-liner

> Feynman learning-mode plugin: teach → teach-back → judge → re-explain loop rendered as rich HTML lesson cards.

## About

**一句话定位**：让 DeepSeek Harness 变成"边学边做"的环境——开启学习模式后，模型按费曼学习法讲解概念、出卡片题请你复述、针对缺口重新讲解，教学内容以富 HTML 卡片可视化呈现。

## ✨ Key Features

- 会话级 `/learn on|off` 切换；开启后注入费曼教学引导（`learning:policy` prompt 段），关闭后完全恢复默认行为。
- 模型经 `teach` 工具产出结构化 Lesson（标题、一句话总结、小节：正文/代码/mermaid 图/类比、可选 raw HTML），Web 客户端经 `tool.call.toolview` keyed 视图渲染为富 HTML 卡片：代码经 shell shiki 高亮（语言横幅 + 复制），mermaid 
- 答题复用现有 `ask_user_question`（卡片选项由 `ui-user-questions` 呈现）；模型在下一步自行判定对错并讲解。
- 模式状态是 log-only `learning/mode` session event：resume/fork/compaction 从日志折叠恢复，无 live mirror。
- 每次会话独立，无跨会话长期记忆。
- 零 mainline core 改动：不加 card kind、不改 agent-loop、不加新事件族（Lesson 卡片直接消费既有 `tool/call` 日志）。

## 🔗 Links

- [GitHub Repository](https://github.com/cendaifeng/dsh-learn-everything)
- [Full README](https://github.com/cendaifeng/dsh-learn-everything#readme)
- [Back to the Tutorials & Learning list](../tutorials.md)
