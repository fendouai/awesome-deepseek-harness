---
title: "Axern"
description: "面向 AI Agent 的开源沙箱：不可信代码执行与持久服务。"
keywords: "Axern, harness, related, security, deepseek harness, dsh"
---
# Axern

> ⭐ 167 · ✅ 活跃 · 相关

## 一句话介绍

面向 AI Agent 的开源沙箱：不可信代码执行与持久服务。

## 详细介绍

The supported local path runs the complete stack with Docker Compose. It needs only the `axern` CLI and Docker Compose v2 — no source checkout, Make, Helm, or language toolchains. brew install cofy-x/tap/axern Without Homebrew, use the standalone checksummed installer: curl -fsSL https://raw.githubusercontent.com/cofy-x/axern/main/install.sh | sh Then start Axern and run the first workload: axern local up axern run python:3.12-slim -- python -c 'print("hello from axern")' `local up` starts Postg

## 作者
**[cofy-x](https://github.com/cofy-x)**

## 链接

- [GitHub 仓库](https://github.com/cofy-x/axern)
- [完整 README](https://github.com/cofy-x/axern#readme)
- [返回Axern所在分类](../related.md)
