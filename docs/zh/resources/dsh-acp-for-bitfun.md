---
title: "dsh-acp-for-bitfun"
description: "BitFun 与 DSH ACP 交互对接 插件"
keywords: "dsh-acp-for-bitfun, developer, integration, coding, deepseek harness, dsh"
---
# dsh-acp-for-bitfun

> ⭐ **10** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 开发者工具 |
| 星数 | ⭐ 10 | 状态 | ✅ 活跃 |
| 作者 | [bobleer](https://github.com/bobleer) | 更新时间 | — |

## 一句话介绍

> BitFun 与 DSH ACP 交互对接 插件

## 详细介绍

BitFun 支持 ACP deepseek-harness。 一个 [DeepSeek Harness (dsh)](https://github.com/deepseek-ai/deepseek-harness) 插件 bundle： 通过 **Agent Client Protocol (ACP) v1 over stdio** 把 [BitFun](https://github.com/GCWing/BitFun) 接入 dsh，作为 dsh 会话的 subagent。dsh 里任意会话都可以用 `subagent_bitfun` 工具把任务委托给 BitFun 执行。 - [BitFun](https://github.com/GCWing/BitFun) - [deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)

## ✨ 核心特性

- [BitFun](https://github.com/GCWing/BitFun)
- [deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)

## 📦 安装

```bash
# 把 bundle 加进你的 dsh profile（从 npm 或本地目录）
dsh plugin --profile web add dsh-acp-for-bitfun

# 或者从本地 checkout 安装
dsh plugin --profile web add ./dsh-acp-for-bitfun

# 启动
dsh web
```

## 🚀 快速开始

```bash
dsh --profile web --dump-config | grep -A 2 bitfun
```

## 📚 更多信息

**工作原理**

dsh 会话 ──subagent_bitfun 工具──▶ dsh-subagent-acp (ACP 客户端) │ 每个任务 spawn 一个独立进程 ▼ bitfun acp (ACP server, stdio JSON-RPC) │ ▼ BitFun Agent Runtime 作为 ACP 客户端：每次委托启动一个全新的 `bitfun acp` 子进程，完成 `initialize → session/new → session/prompt` 并流式收集 `agent_message_chunk`。 挂载，模型见到的工具名默认为 `subagent_bitfun`。 在 SIGTERM 下立即退出，会话数据由 BitFun 自身持久化。

**配置**

在 profile 的 `cordis.patch.yml`（`$DSH_HOME/profiles/<name>/cordis.patch.yml`）里 按 id 覆盖： name: dsh-acp-for-bitfun config: command: /absolute/path/to/bitfun # 默认 'bitfun'（PATH 解析） providerName: bitfun # 默认 'bitfun' toolName: subagent_bitfun # 默认 'subagent_bitfun' permission: reject # 'reject' | 'allow' acpArgs: ['acp'] # 默认 ['acp'] env: {} # 传给 BitFun 子进程的额外环境变量 checkOnStart: true # 加载时探测 bitfun，缺失则启

## 🔗 链接

- [GitHub 仓库](https://github.com/bobleer/dsh-acp-for-bitfun)
- [完整 README](https://github.com/bobleer/dsh-acp-for-bitfun#readme)
- [返回dsh-acp-for-bitfun所在分类](../integrations.md)
