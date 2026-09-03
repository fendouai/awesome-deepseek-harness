---
title: "deepseek-auto-evolving-harness"
description: "自进化 LLM Agent Harness：通过 Claude Code 与 self_evolution.md 指南进行基准驱动进化。"
keywords: "deepseek-auto-evolving-harness, harness, related, research, deepseek harness, dsh"
---
# deepseek-auto-evolving-harness

> ⭐ **28** · ✅ 活跃 · 相关

| | | | |
|---|---|---|---|
| 类型 | 相关 | 分类 | Harness |
| 星数 | ⭐ 28 | 状态 | ✅ 活跃 |
| 作者 | [liuchen6667](https://github.com/liuchen6667) | 更新时间 | 2026-05-26 |

## 一句话介绍

> 自进化 LLM Agent Harness：通过 Claude Code 与 self_evolution.md 指南进行基准驱动进化。

## 详细介绍

从零开始创建的 harness，在单数据集上经过 6 轮进化，用DeepSeek-V3.2非思考模型逼近Claude Code + Opus 4.6思考模型。 6轮进化主要方法为：缩短执行路径，修正工具调用兼容错误格式，调整system prompt，调整推理参数，增加执行完毕后的反思过程。

## ✨ 核心特性

- **通用模型** — 任何 OpenAI 兼容模型都能用，切换只需改一行配置
- **流式输出** — 回复实时逐字显示，工具调用标签自动过滤不展示
- **工具系统** — 自动发现、按行编辑、文件读写、Shell 执行、文件搜索
- **长期记忆** — 用户要求记住的信息持久化到 `memory/`，跨会话保留
- **上下文压缩** — 对话过长时自动压缩旧工具结果，防止 token 溢出
- **格式纠错** — 模型输出错误的工具调用格式时自动要求重试
- **自动重试** — 网络错误/限流时指数退避重试
- **会话日志** — 每次对话完整记录到 `sessions/`，方便回溯

## 📦 安装

```bash
cd deepseek-auto-evolving-harness
pip install -r requirements.txt

# 编辑 config.py 填入你的 API 配置
python main.py
```

## 🚀 快速开始

```bash
❯ 列出工作区里的文件
❯ 创建一个 hello.py，打印 hello world
❯ 运行 python hello.py
❯ 记住我喜欢简洁的代码风格
```

## 📚 更多信息

**编辑 config.py 填入你的 API 配置**

python main.py 示例交互： ❯ 列出工作区里的文件 ❯ 创建一个 hello.py，打印 hello world ❯ 运行 python hello.py ❯ 记住我喜欢简洁的代码风格

## 🔗 链接

- [GitHub 仓库](https://github.com/liuchen6667/deepseek-auto-evolving-harness)
- [完整 README](https://github.com/liuchen6667/deepseek-auto-evolving-harness#readme)
- [返回deepseek-auto-evolving-harness所在分类](../related.md)
