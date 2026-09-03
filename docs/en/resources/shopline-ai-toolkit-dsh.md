---
title: "shopline-ai-toolkit-dsh"
description: "SHOPLINE AI Toolkit for DeepSeek Harness (dsh-plugin): official SHOPLINE Developer MCP bridge + SHOPLINE agent skills, mirroring the Shopify AI Toolkit architecture. dsh-plugin"
keywords: "shopline-ai-toolkit-dsh, mcp, integration, coding, multi-agent, deepseek harness, dsh"
---
# shopline-ai-toolkit-dsh

> ⭐ **3** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | MCP |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [lunw](https://github.com/lunw) | Updated | 2026-08-20 |

## One-liner

> SHOPLINE AI Toolkit for DeepSeek Harness (dsh-plugin): official SHOPLINE Developer MCP bridge + SHOPLINE agent skills, mirroring the Shopify AI Toolkit architecture. dsh-plugin

## About

The **Shopify AI Toolkit** gives AI coding agents Shopify-aware context through three layers: agent **skills**, a **Dev MCP server**, and per-tool **plugins**. This project brings the same architecture to SHOPLINE developers working inside **DeepSeek Harness (dsh)**:

## 📦 Install

```bash
dsh plugin --profile web add shopline-ai-toolkit-dsh
# add "shopline-ai-toolkit-dsh" to dsh.profile.bundles in ~/.dsh/profiles/web/package.json
dsh web
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add shopline-ai-toolkit-dsh
# 在 ~/.dsh/profiles/web/package.json 的 dsh.profile.bundles 中加入 "shopline-ai-toolkit-dsh"
dsh web
```

## 📚 Learn more

**Install**

See [docs/install.md](docs/install.md). Quick start (full bundle): dsh plugin --profile web add shopline-ai-toolkit-dsh

**Example**

> "Search the SHOPLINE Admin REST endpoints for products, then give me the full endpoint > detail for updating a product variant, including request parameters and a curl example." The agent loads `shopline-admin-rest` + `shopline-dev-mcp` skills and calls `mcp__shopline__search_admin_rest_endpoints` → `mcp__shopline__get_admin_rest_endpoint_detail`. More prompts: [examples/prompts.md](examples/pro

**安装**

详见 [docs/install.md](docs/install.md)。快速开始（完整插件）： dsh plugin --profile web add shopline-ai-toolkit-dsh

**示例**

> 「搜索 SHOPLINE Admin REST 端点中商品相关接口，然后给出更新商品变体的完整端点详情， > 包括请求参数和 curl 示例。」 助手会加载 `shopline-admin-rest` 与 `shopline-dev-mcp` 技能，并依次调用 `mcp__shopline__search_admin_rest_endpoints` → `mcp__shopline__get_admin_rest_endpoint_detail`。 更多示例： [examples/prompts.md](examples/prompts.md) · 设计文档：[docs/architecture.md](docs/architecture.md)

## 🔗 Links

- [GitHub Repository](https://github.com/lunw/shopline-ai-toolkit-dsh)
- [Full README](https://github.com/lunw/shopline-ai-toolkit-dsh#readme)
- [Back to the MCP & Integrations list](../integrations.md)
