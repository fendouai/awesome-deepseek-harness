---
title: "deepseek-protocol-doctor"
description: "Checks DeepSeek tool loops, reasoning_content, strict schemas and captured SSE; also works as a DSH plugin."
keywords: "deepseek-protocol-doctor, learning, tutorial, observability, deepseek harness, dsh"
---
# deepseek-protocol-doctor

> ⭐ **2** · ✅ active · tutorial

| | | | |
|---|---|---|---|
| Type | tutorial | Category | Learning |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [Whning0513](https://github.com/Whning0513) | Updated | 2026-08-18 |

## One-liner

> Checks DeepSeek tool loops, reasoning_content, strict schemas and captured SSE; also works as a DSH plugin.

## About

[English](README.en.md) | 中文 我在接 DeepSeek tool calling 时碰到过几类很像“模型抽风”的问题：工具结果明明传回去了，请求还是 400；流式输出看着正常，最后拼出来的参数却不是 JSON；同一段 history 在关掉 thinking 后能跑，打开就报错。 最后发现不少问题都出在请求和响应的拼接上。于是写了这个小工具，把 request JSON 或 SSE 录制丢进去，先排查这些常见坑。它只看你给它的内容，不会调用模型。

## ✨ Key Features

- `deepseek_protocol_check`：检查请求和消息历史。
- `deepseek_stream_check`：检查保存下来的 SSE / JSONL 流。

## 📦 Install

```bash
dsh plugin --profile demo add github:Whning0513/deepseek-protocol-doctor
```

## 🚀 Quick Start

```bash
用 deepseek_protocol_check 看看这个请求里的工具调用哪里不对：{ ... }
```

## 🔗 Links

- [GitHub Repository](https://github.com/Whning0513/deepseek-protocol-doctor)
- [Full README](https://github.com/Whning0513/deepseek-protocol-doctor#readme)
- [Back to the Tutorials & Learning list](../tutorials.md)
