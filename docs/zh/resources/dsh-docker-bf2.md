---
title: "dsh-docker"
description: "隔离的 DeepSeek Harness 插件安装沙箱，并对本机 MCP 口做防御性探测。"
keywords: "dsh-docker, mcp, integration, coding, deepseek harness, dsh"
---
# dsh-docker

> ⭐ **0** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | MCP |
| 星数 | ⭐ 0 | 状态 | ✅ 活跃 |
| 作者 | [dshoneys](https://github.com/dshoneys) | 更新时间 | 2026-08-19 |

## 一句话介绍

> 隔离的 DeepSeek Harness 插件安装沙箱，并对本机 MCP 口做防御性探测。

## 详细介绍

Isolated installability **and MCP loopback** sandbox for DeepSeek Harness plugins. Org: [dshoneys](https://github.com/dshoneys) · sister tool: [mcp_guard](https://github.com/dshoneys/mcp_guard) The image pins `@deepseek-ai/dsh`, keeps `$DSH_HOME` on a tmpfs (never your host `~/.dsh`), and proves a plugin composed with `--dump-config`. That step does not boot a model, so it does not spend tokens.

## ✨ 核心特性

- Repeat `dsh plugin add` without polluting the real profile
- Same Node / pnpm / dsh version on every run
- Cache the pnpm store so the 2nd install of the same spec is cheap
- Later: optional `dsh web` or `dsh --profile headless "..."` with keys in `.env`

## 🚀 快速开始

```bash
docker compose build
docker compose run --rm dsh dsh-selfcheck
```

## 📚 更多信息

**Install smoke (no model)**

One plugin, clean home each time: docker compose run --rm dsh dsh-smoke dsh-ai4scholar docker compose run --rm dsh dsh-smoke github:Vncntvx/dsh-zotero docker compose run --rm dsh dsh-smoke --expect writing-guard dsh-plugin-writing-guard Stack two plugins in the same home (`--no-reset` on the second): docker compose run --rm dsh bash -lc "dsh-smoke dsh-ai4scholar && dsh-smoke --no-reset dsh-zotero"

## 🔗 链接

- [GitHub 仓库](https://github.com/dshoneys/dsh-docker)
- [完整 README](https://github.com/dshoneys/dsh-docker#readme)
- [返回dsh-docker所在分类](../integrations.md)
