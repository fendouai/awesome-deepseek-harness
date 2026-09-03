---
title: "dsh-super-injector"
description: "Super-injector plugin (cordis) for context injection."
keywords: "dsh-super-injector, developer, integration, context, deepseek harness, dsh"
---
# dsh-super-injector

> ⭐ **133** · ✅ active · integration · ⬆️ +7 recently

| | | | |
|---|---|---|---|
| Type | integration | Category | Developer tools |
| Stars | ⭐ 133 | Status | ✅ active |
| Author | [yjh051108](https://github.com/yjh051108) | Updated | 2026-08-21 |

## One-liner

> Super-injector plugin (cordis) for context injection.

## About

DSH 生态的 **BepInEx 式模组注入入口**：运行时把任意本地插件包注入运行中的 web， 不碰 patch / package.json / bundles 列表、不重启进程。**注入即完整生效（host 工具 + client UI）。**

## ✨ Key Features

- 🔥 **热重载 + 自重载**：`dev_reload_package` 整包重载（清缓存 → 重新 import → 重建 fiber，失败回滚保留旧代）；注入器自身也支持自重载（自杀 → 全局定时器重建）
- 🤖 **自动 watch**：注入即自动监听插件目录，改代码 build 后约 1.5 秒自动重载（无需手动触发）
- 🖥️ **注入插件 UI 完整生效**：清除 loader 幽灵 entry 隔离（normalizeEntry），client 模块补扫/联动/卸载清理——注入的插件 host 工具 + 图谱/面板等 UI 全部可用
- 🧪 **开发侧挂区（staging）+ 持久化**：测试工具挂"后侧"不进 tools schema、缓存零污染；`dev_stage_promote` 一键转正；staging 落盘，**自重载/重启后转正工具自动恢复**
- 🧹 **一键卸载**：`dev_uninject_plugin` fiber 全清理（工具/监听/路由/client 表）→ 清注入清单 → 删 junction，免重启
- 🛠️ **路由自愈**：`dev_clear_routes` 直捣 webserver 内部路由表，热重载残留的孤儿路由免重启清除
- 🔁 **重启自动恢复**：注入清单持久化（`~/.dsh/super-injector/registry.json`），web 重启后自动归位
- 📊 **操作自检**：每次注入/重载/安装返回 `host ✓ / client ✓` 双验证；`dev_plugin_status` 含操作成功率统计

## 📦 Install

```bash
# 官方装配（重启后由 bundles 接管，生产态）
dsh plugin --profile web add <解压目录>

# 或运行时注入（免重启，开发态；需任一环境已常驻注入器）
# 对 AI 说：dev_inject_plugin <解压目录>
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add github:yjh051108/dsh-super-injector
```

## 📚 Learn more

**30 行写一个"会思考的插件"（守护循环最小示例）**

import type { Context } from 'cordis' import type LlmService from '@deepseek-ai/dsh-llm' import { createUserMessage, ReasoningEffortId } from '@deepseek-ai/dsh-llm' type AppContext = Context & { llm: LlmService; setInterval(fn: () => void, ms: number): any } export const name = 'my-daemon' export const inject = ['timer', 'llm'] export function apply(ctx: AppContext): void { let route: { provider: 

## 🔗 Links

- [GitHub Repository](https://github.com/yjh051108/dsh-super-injector)
- [Full README](https://github.com/yjh051108/dsh-super-injector#readme)
- [Back to the MCP & Integrations list](../integrations.md)
