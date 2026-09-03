---
title: "dsh-memoria"
description: "Vector + graph memory backend with namespace isolation, automatic observation, recall, importance handling and hot reload."
keywords: "dsh-memoria, memory, plugin, context, deepseek harness, dsh"
---
# dsh-memoria

> ⭐ **2** · 🧪 experimental · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 2 | Status | 🧪 experimental |
| Author | [jiayan-xu](https://github.com/jiayan-xu) | Updated | 2026-08-14 |
| Subcategory | 🧠 Memory systems | Capabilities | memory, context |

## One-liner

> Vector + graph memory backend with namespace isolation, automatic observation, recall, importance handling and hot reload.

## About

memoria 记忆后端插件：把 [memoria](https://github.com/jiayan-xu/memoria)（向量 + 图记忆层）接入 DeepSeek Harness (dsh)，让 dsh agent 会话可以**记住**和**回忆**。 - 4 个工具：`memoria_observe` / `memoria_remember` / `memoria_search` / `memoria_recall` - 自动写入：每轮对话结束自动 `observe` 沉淀；用户肯定反馈（不错/很好/good/赞…）自动 `remember`（importance=5） - 配置热重载：改 `~/.dsh/settings.yaml` 的 `memoria:` section 免重启生效 - 命名空间隔离：所有读写强制落在配置的 namespace（默认 `dsh-test`），不碰其他业务数据

## ✨ Key Features

- 4 个工具：`memoria_observe` / `memoria_remember` / `memoria_search` / `memoria_recall`
- 自动写入：每轮对话结束自动 `observe` 沉淀；用户肯定反馈（不错/很好/good/赞…）自动 `remember`（importance=5）
- 配置热重载：改 `~/.dsh/settings.yaml` 的 `memoria:` section 免重启生效
- 命名空间隔离：所有读写强制落在配置的 namespace（默认 `dsh-test`），不碰其他业务数据

## 📦 Install

```bash
# 安装（自动挂载，无需手动改 profile）——两种源任选
dsh plugin --profile web add github:jiayan-xu/dsh-memoria
# 或 npm 源：
dsh plugin --profile web add @jhp830901/dsh-memoria

# 启动 dsh web 即可使用
dsh web
```

## 🚀 Quick Start

```bash
# ~/.dsh/settings.yaml
memoria:
  baseURL: http://127.0.0.1:9003
  namespace: my-namespace
  autoWrite: true
```

## 📚 Learn more

**使用前提**

⚠️ **本插件是 memoria 的前端，不是记忆存储本身**。使用前需要： 1. **自建并运行 memoria 服务**（默认连接 `http://127.0.0.1:9003`）：memoria 是独立的开源项目（[jiayan-xu/memoria](https://github.com/jiayan-xu/memoria)，Rust 向量 + 图记忆服务）。没有该服务时工具会报连接失败。 2. **准备 badge token**：memoria 工具调用要求 `register_agent` 签发的 badge token（admin key 不能直连），见下文「获取 memoria badge token」。以环境变量 `MEMORIA_AGENT_KEY` 提供（不落盘）。 装完发现工具报 `Connection refused` / `HTTP 200 but auth

**~/.dsh/settings.yaml**

memoria: baseURL: http://127.0.0.1:9003 namespace: my-namespace autoWrite: true agentKey **不要落盘**，用环境变量： export MEMORIA_AGENT_KEY=<badge-token>

**用 admin key 注册 agent（示例），返回 badge 有效期 1 年**

curl -X POST http://127.0.0.1:9003/mcp -H 'Content-Type: application/json' \ -H 'X-Agent-Id: dsh-memoria' -H 'X-Agent-Key: <ADMIN_KEY>' \ -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"register_agent","arguments":{"agent_id":"dsh-memoria","display_name":"dsh-memoria plugin","namespace":"dsh-test"}}}'

## 🔗 Links

- [GitHub Repository](https://github.com/jiayan-xu/dsh-memoria)
- [Full README](https://github.com/jiayan-xu/dsh-memoria#readme)
- [Back to the Plugins list](../plugins.md)
