---
title: "deepseek-protocol-doctor"
description: "检查 DeepSeek 工具循环、reasoning_content、严格 schema 与捕获的 SSE，也可作为 DSH 插件。"
keywords: "deepseek-protocol-doctor, learning, tutorial, observability, deepseek harness, dsh"
---
# deepseek-protocol-doctor

> ⭐ **2** · ✅ 活跃 · 教程

| | | | |
|---|---|---|---|
| 类型 | 教程 | 分类 | 学习 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [Whning0513](https://github.com/Whning0513) | 更新时间 | 2026-08-18 |

## 一句话介绍

> 检查 DeepSeek 工具循环、reasoning_content、严格 schema 与捕获的 SSE，也可作为 DSH 插件。

## 详细介绍

[English](README.en.md) | 中文 我在接 DeepSeek tool calling 时碰到过几类很像“模型抽风”的问题：工具结果明明传回去了，请求还是 400；流式输出看着正常，最后拼出来的参数却不是 JSON；同一段 history 在关掉 thinking 后能跑，打开就报错。 最后发现不少问题都出在请求和响应的拼接上。于是写了这个小工具，把 request JSON 或 SSE 录制丢进去，先排查这些常见坑。它只看你给它的内容，不会调用模型。

## ✨ 核心特性

- `deepseek_protocol_check`：检查请求和消息历史。
- `deepseek_stream_check`：检查保存下来的 SSE / JSONL 流。

## 📦 安装

```bash
dsh plugin --profile demo add github:Whning0513/deepseek-protocol-doctor
```

## 🚀 快速开始

```bash
用 deepseek_protocol_check 看看这个请求里的工具调用哪里不对：{ ... }
```

## 🔗 链接

- [GitHub 仓库](https://github.com/Whning0513/deepseek-protocol-doctor)
- [完整 README](https://github.com/Whning0513/deepseek-protocol-doctor#readme)
- [返回deepseek-protocol-doctor所在分类](../tutorials.md)
