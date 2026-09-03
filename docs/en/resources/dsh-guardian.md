---
title: "dsh-guardian"
description: "Agent security guardrail: intercepts and audits every tool call, requiring human confirmation on sensitive operations."
keywords: "dsh-guardian, security, plugin, deepseek harness, dsh"
---
# dsh-guardian

> ⭐ **4** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Security |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [cdxiaodong](https://github.com/cdxiaodong) | Updated | 2026-08-21 |

## One-liner

> Agent security guardrail: intercepts and audits every tool call, requiring human confirmation on sensitive operations.

## About

LLM Agent（Claude Code / DeepSeek Harness）能自主执行 shell、读写文件、发网络请求。一旦被**提示注入**、**工具投毒**或**模型误判**带偏，可能在你不知情时 `rm -rf`、读取 `.ssh/id_rsa`、把密钥外泄到远程。本插件是一道**运行时安全网**： Agent 想执行工具 → guardian/check 前置审查 → 命中规则 → 拦截 / 人工批准 → 才放行

## ✨ Key Features

- **路径沙箱**（`guardian/path`）：realpath 解析 + 白名单根目录 + 编码变体解码 + 空字节截断检测——比纯正则可靠
- **风险评分引擎**（`risk.ts`）：多信号并集概率式加权成 0~1 分，按阈值分级处置（deny/block/warn/allow）

## 📦 Install

```bash
dsh plugin --profile web add github:cdxiaodong/dsh-guardian
```

## 🚀 Quick Start

```bash
npm ci && npm test     # 19/19 通过
```

## 🔗 Links

- [GitHub Repository](https://github.com/cdxiaodong/dsh-guardian)
- [Full README](https://github.com/cdxiaodong/dsh-guardian#readme)
- [Back to the Plugins list](../plugins.md)
