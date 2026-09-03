---
title: "DeerFlow"
description: "Open-source long-horizon SuperAgent harness by ByteDance: skills, memory, sandboxes, subagents, tools and a message gateway."
keywords: "DeerFlow, harness, related, workflow, memory, deepseek harness, dsh"
---
# DeerFlow

> ⭐ **80,462** · ✅ active · related · ⬆️ +55 recently

| | | | |
|---|---|---|---|
| Type | related | Category | Harness |
| Stars | ⭐ 80,462 | Status | ✅ active |
| Author | [bytedance](https://github.com/bytedance) | Updated | 2026-08-20 |

## One-liner

> Open-source long-horizon SuperAgent harness by ByteDance: skills, memory, sandboxes, subagents, tools and a message gateway.

## About

DeerFlow (**D**eep **E**xploration and **E**fficient **R**esearch **Flow**) is an open-source **super agent harness** that orchestrates **sub-agents**, **memory**, and **sandboxes** to do almost anything — powered by **extensible skills**. https://github.com/user-attachments/assets/a8bcadc4-e040-4cf2-8fda-dd768b999c18

## ✨ Key Features

- [**LLM Space**](https://github.com/deer-flow/llm-space) - Meet our secret weapon behind DeerFlow — one desktop tool to prototype agent ideas, inspect each harne

## 📦 Install

```bash
git clone https://github.com/bytedance/deer-flow.git
   cd deer-flow
```

## 🚀 Quick Start

```bash
make setup
```

## 📚 Learn more

**Configuration**

1. **Clone the DeerFlow repository** ```bash git clone https://github.com/bytedance/deer-flow.git cd deer-flow ``` 2. **Run the setup wizard** From the project root directory (`deer-flow/`), run: ```bash make setup ``` This launches an interactive wizard that guides you through choosing an LLM provider, optional web search, and execution/safety preferences such as sandbox mode, bash access, and fi

**Configuration & management — returns Gateway-aligned dicts**

models = client.list_models() # {"models": [...]} skills = client.list_skills() # {"skills": [...]} client.update_skill("web-search", enabled=True) client.upload_files("thread-1", ["./report.pdf"]) # {"success": True, "files": [...]} client.set_goal("thread-1", "finish the implementation and make all tests pass") client.get_goal("thread-1") # {"goal": {...}} or {"goal": None} client.clear_goal("th

## 🔗 Links

- [GitHub Repository](https://github.com/bytedance/deer-flow)
- [Full README](https://github.com/bytedance/deer-flow#readme)
- [Back to the Related Agent Harnesses list](../related.md)
