---
title: "deepseek-auto-evolving-harness"
description: "Auto-evolving LLM agent harness: benchmark-driven evolution via Claude Code and a self_evolution.md guide."
keywords: "deepseek-auto-evolving-harness, harness, related, research, deepseek harness, dsh"
---
# deepseek-auto-evolving-harness

> ⭐ **28** · ✅ active · related

| | | | |
|---|---|---|---|
| Type | related | Category | Harness |
| Stars | ⭐ 28 | Status | ✅ active |
| Author | [liuchen6667](https://github.com/liuchen6667) | Updated | 2026-05-26 |

## One-liner

> Auto-evolving LLM agent harness: benchmark-driven evolution via Claude Code and a self_evolution.md guide.

## About

从零开始创建的 harness，在单数据集上经过 6 轮进化，用DeepSeek-V3.2非思考模型逼近Claude Code + Opus 4.6思考模型。 6轮进化主要方法为：缩短执行路径，修正工具调用兼容错误格式，调整system prompt，调整推理参数，增加执行完毕后的反思过程。

## ✨ Key Features

- **通用模型** — 任何 OpenAI 兼容模型都能用，切换只需改一行配置
- **流式输出** — 回复实时逐字显示，工具调用标签自动过滤不展示
- **工具系统** — 自动发现、按行编辑、文件读写、Shell 执行、文件搜索
- **长期记忆** — 用户要求记住的信息持久化到 `memory/`，跨会话保留
- **上下文压缩** — 对话过长时自动压缩旧工具结果，防止 token 溢出
- **格式纠错** — 模型输出错误的工具调用格式时自动要求重试
- **自动重试** — 网络错误/限流时指数退避重试
- **会话日志** — 每次对话完整记录到 `sessions/`，方便回溯

## 📦 Install

```bash
cd deepseek-auto-evolving-harness
pip install -r requirements.txt

# 编辑 config.py 填入你的 API 配置
python main.py
```

## 🚀 Quick Start

```bash
❯ 列出工作区里的文件
❯ 创建一个 hello.py，打印 hello world
❯ 运行 python hello.py
❯ 记住我喜欢简洁的代码风格
```

## 📚 Learn more

**编辑 config.py 填入你的 API 配置**

python main.py 示例交互： ❯ 列出工作区里的文件 ❯ 创建一个 hello.py，打印 hello world ❯ 运行 python hello.py ❯ 记住我喜欢简洁的代码风格

## 🔗 Links

- [GitHub Repository](https://github.com/liuchen6667/deepseek-auto-evolving-harness)
- [Full README](https://github.com/liuchen6667/deepseek-auto-evolving-harness#readme)
- [Back to the Related Agent Harnesses list](../related.md)
