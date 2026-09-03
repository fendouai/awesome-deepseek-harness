---
title: "DeerFlow"
description: "字节跳动开源的长时间跨度 SuperAgent harness：技能、记忆、沙箱、子代理、工具与消息网关。"
keywords: "DeerFlow, harness, related, workflow, memory, deepseek harness, dsh"
---
# DeerFlow

> ⭐ **80,462** · ✅ 活跃 · 相关 · 近期 ⬆️ +55

| | | | |
|---|---|---|---|
| 类型 | 相关 | 分类 | Harness |
| 星数 | ⭐ 80,462 | 状态 | ✅ 活跃 |
| 作者 | [bytedance](https://github.com/bytedance) | 更新时间 | 2026-08-20 |

## 一句话介绍

> 字节跳动开源的长时间跨度 SuperAgent harness：技能、记忆、沙箱、子代理、工具与消息网关。

## 详细介绍

DeerFlow (**D**eep **E**xploration and **E**fficient **R**esearch **Flow**) is an open-source **super agent harness** that orchestrates **sub-agents**, **memory**, and **sandboxes** to do almost anything — powered by **extensible skills**. https://github.com/user-attachments/assets/a8bcadc4-e040-4cf2-8fda-dd768b999c18

## ✨ 核心特性

- [**LLM Space**](https://github.com/deer-flow/llm-space) - Meet our secret weapon behind DeerFlow — one desktop tool to prototype agent ideas, inspect each harne

## 📦 安装

```bash
git clone https://github.com/bytedance/deer-flow.git
   cd deer-flow
```

## 🚀 快速开始

```bash
make setup
```

## 📚 更多信息

**Configuration**

1. **Clone the DeerFlow repository** ```bash git clone https://github.com/bytedance/deer-flow.git cd deer-flow ``` 2. **Run the setup wizard** From the project root directory (`deer-flow/`), run: ```bash make setup ``` This launches an interactive wizard that guides you through choosing an LLM provider, optional web search, and execution/safety preferences such as sandbox mode, bash access, and fi

**Configuration & management — returns Gateway-aligned dicts**

models = client.list_models() # {"models": [...]} skills = client.list_skills() # {"skills": [...]} client.update_skill("web-search", enabled=True) client.upload_files("thread-1", ["./report.pdf"]) # {"success": True, "files": [...]} client.set_goal("thread-1", "finish the implementation and make all tests pass") client.get_goal("thread-1") # {"goal": {...}} or {"goal": None} client.clear_goal("th

## 🔗 链接

- [GitHub 仓库](https://github.com/bytedance/deer-flow)
- [完整 README](https://github.com/bytedance/deer-flow#readme)
- [返回DeerFlow所在分类](../related.md)
