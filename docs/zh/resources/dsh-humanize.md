---
title: "dsh-humanize"
description: "去 AI 味写作技能：让 Agent 输出更自然。"
keywords: "dsh-humanize, coding, skill, research, deepseek harness, dsh"
---
# dsh-humanize

> ⭐ **3** · ✅ 活跃 · 技能

| | | | |
|---|---|---|---|
| 类型 | 技能 | 分类 | 编码 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [zevorn](https://github.com/zevorn) | 更新时间 | 2026-08-13 |

## 一句话介绍

> 去 AI 味写作技能：让 Agent 输出更自然。

## 详细介绍

**Current Version: 1.18.0** A Claude Code plugin that provides iterative development with independent AI review. Build with confidence through continuous feedback loops.

## ✨ 核心特性

- **Iteration over Perfection** -- Instead of expecting perfect output in one shot, Humanize leverages continuous feedback loops where issues 
- **One Build + One Review** -- Claude implements, Codex independently reviews. No blind spots.
- **Ralph Loop with Swarm Mode** -- Iterative refinement continues until all acceptance criteria are met. Optionally parallelize with Agent Te
- **Capability Anchors** -- Generated plans include a feature/capability map, and RLCR rounds keep Claude and Codex anchored to the relevant c

## 📦 安装

```bash
# Install the standard bundle into the web profile.
dsh plugin --profile web add github:dsh-external/dsh-humanize#<commit-or-tag>
```

## 🚀 快速开始

```bash
/humanize:gen-idea "add undo/redo to the editor"
```

## 🔗 链接

- [GitHub 仓库](https://github.com/zevorn/dsh-humanize)
- [完整 README](https://github.com/zevorn/dsh-humanize#readme)
- [返回dsh-humanize所在分类](../skills.md)
