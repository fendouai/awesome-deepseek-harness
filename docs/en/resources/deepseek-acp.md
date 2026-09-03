---
title: "deepseek-acp"
description: "把 DeepSeek Harness 接成一个面向编辑器的完整编码 Agent， 通过 Agent Client Protocol（ACP）与客户端通话。"
keywords: "deepseek-acp, developer, integration, coding, multi-agent, deepseek harness, dsh"
---
# deepseek-acp

> ⭐ **9** · ✅ active · integration · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | integration | Category | Developer tools |
| Stars | ⭐ 9 | Status | ✅ active |
| Author | [xintaofei](https://github.com/xintaofei) | Updated | 2026-08-18 |

## One-liner

> 把 DeepSeek Harness 接成一个面向编辑器的完整编码 Agent， 通过 Agent Client Protocol（ACP）与客户端通话。

## About

Turns [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) into a **full-featured editor-facing coding agent** that communicates with clients over the [Agent Client Protocol](https://agentclientprotocol.com) (ACP). **Supported clients**: any editor that implements ACP. Development testing is done with **[codeg](https://github.com/xintaofei/codeg)**. **[Zed](https://zed.dev)** uses the same protocol and can be configured as shown below, but has not yet been validated feature by feature. ---

## ✨ Key Features

- **You cannot see what the model is doing.** Tool calls, command output, and file changes remain
- **There is no token-by-token streaming.** Updates arrive only after a complete message is
- **Sessions are disposable.** Once closed, they are gone: there is no restore, list, or title.
- **There is no control surface.** You cannot switch models, change file permissions, enable plan
- **MCP is rejected.** Any non-empty `mcpServers` value fails immediately.

## 🚀 Quick Start

```bash
{ "id": "terminal", "type": "terminal", "args": ["--setup"] }
```

## 🔗 Links

- [GitHub Repository](https://github.com/xintaofei/deepseek-acp)
- [Full README](https://github.com/xintaofei/deepseek-acp#readme)
- [Back to the MCP & Integrations list](../integrations.md)
