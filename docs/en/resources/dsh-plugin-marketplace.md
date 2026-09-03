---
title: "dsh-plugin-marketplace"
description: "Plugin marketplace for DeepSeek Harness — live-syncs the GitHub dsh-plugin topic (1800+ repos) into a searchable, paginated settings tab with one-click install and agent tools (market_search / market_install)."
keywords: "dsh-plugin-marketplace, registry, awesome-list, coding, git, multi-agent, search, deepseek harness, dsh"
---
# dsh-plugin-marketplace

> ⭐ **27** · ✅ active · awesome-list · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 27 | Status | ✅ active |
| Author | [AwesomeHou](https://github.com/AwesomeHou) | Updated | 2026-08-19 |

## One-liner

> Plugin marketplace for DeepSeek Harness — live-syncs the GitHub dsh-plugin topic (1800+ repos) into a searchable, paginated settings tab with one-click install and agent tools (market_search / market_install).

## About

[English](README.en.md) | 中文 一个 DeepSeek Harness 的**永久插件**，把 GitHub [`dsh-plugin`](https://github.com/topics/dsh-plugin) topic 变成**插件市场**——既是 **设置 → 插件** 里的标签页，也提供一组模型工具，让 agent 自己就能搜索并安装插件。 *插件市场：搜索、浏览、一键安装、检查更新。*

## ✨ Key Features

- **全量分页** — 完整 topic 按页拉取（默认 50 / 最大 100），UI 带"加载更多"按钮。不再有"只看 50 个"的硬限制：`total` 反映真实的 `total_count`。
- **搜索** — 关键词搜索走 GitHub 自己的 `q`（所以是在**整个 topic** 里搜，而不是只在已加载的页里过滤），UI 搜索框和 `market_search` 工具都用它。
- **Agent 工具**（Host 侧通过 `ctx.tools.register` 注册）：
- **安装（默认：直装，优先 npm 包）** — 每个插件卡片都有 **安装** 按钮，点击后通过 `POST /api/market/install` 启动**确定性的异步安装任务**：host 侧 `planInstall` 先探测仓库形态——根 `package.json` 声明了 `dsh.bundle`/`d
- **pnpm 兼容层（借鉴 dsh-market）** — 所有安装子进程注入 `CI=true`（pnpm ≥10 无 TTY 时不再无限等交互提示而卡死，遇错直接报错）；检测到 **pnpm 大版本漂移**（`ERR_PNPM_VIRTUAL_STORE_DIR_MAX_LENGTH_DIFF` / `PUBLIC
- **安装卡住自动止损** — pnpm / git 在死网络或过慢的下载上可能**零输出挂死**（例如 GitHub 暂不可达时停在"正在解析依赖… 8%"）。host 侧带**停滞看门狗**：一段时间（默认 120s，可用 `DSH_MARKET_STALL_MS` 覆盖）没有任何进度（无输出行、无字节增长）就杀掉进
- **对等依赖失败识别** — 若插件声明了 `@deepseek-ai/*@^0.1.0-rc.6` 这类**预发布对等依赖**，`dsh plugin add` 可能以 `ERR_PNPM_NO_MATCHING_VERSION` 退出。host 侧会识别并给出**可操作的说明**（而不是裸的 "exit 1"），卡
- **workspace 缺失的友好报错** — host 侧在安装/更新前检查 web profile：`package.json` 或 `pnpm-workspace.yaml` 缺失时，`market_install` / `/api/market/install` 会返回可操作的错误信息（告诉用户如何创建 `pn

## 📦 Install

```bash
dsh plugin --profile web add https://github.com/AwesomeHou/dsh-plugin-marketplace
```

## 🚀 Quick Start

```bash
帮我安装这个插件 https://github.com/AwesomeHou/dsh-plugin-marketplace
```

## 📚 Learn more

**手动安装**

dsh plugin --profile web add https://github.com/AwesomeHou/dsh-plugin-marketplace 安装后需**重启 harness** 才能生效。

## 🔗 Links

- [GitHub Repository](https://github.com/AwesomeHou/dsh-plugin-marketplace)
- [Full README](https://github.com/AwesomeHou/dsh-plugin-marketplace#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
