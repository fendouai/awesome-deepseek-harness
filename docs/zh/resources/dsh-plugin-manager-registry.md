---
title: "dsh-plugin-manager-registry"
description: "@dsh-pm/registry — discover dsh plugins by merging the awesome-dsh-plugin list, GitHub dsh-plugin-topic search, and npm keyword search into one deduped, offline-tolerant registry (the discovery engine of dsh pm)"
keywords: "dsh-plugin-manager-registry, discovery, plugin, search, deepseek harness, dsh"
---
# dsh-plugin-manager-registry

> ⭐ **1** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 插件发现 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [Jesse-njx](https://github.com/Jesse-njx) | 更新时间 | 2026-08-13 |

## 一句话介绍

> @dsh-pm/registry — discover dsh plugins by merging the awesome-dsh-plugin list, GitHub dsh-plugin-topic search, and npm keyword search into one deduped, offline-tolerant registry (the discovery engine of dsh pm)

## 详细介绍

The discovery engine of `dsh pm` — find dsh plugins by merging three independent sources into one deduped, sorted, **offline-tolerant** registry: 1. **awesome-list** — the [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) README, parsed under its category headings (config `awesomeUrl`). 2. **GitHub topic** — repo search for the `dsh-plugin` topic via the `gh` CLI, with a plain `api.github.com` https fallback. 3. **npm keyword** — `npm search --json ` (config `npmKeyword`, default `dsh`), with a registry `/-/v1/search` https fallback. A GitHub hit and an npm hit for the same project collapse into one `RegistryEntry` carrying both `repoUrl` and `npmName`; entries dedupe by normalized repo URL first, then by bare name. Every source degrades independently — a dead 

## 📦 安装

```bash
dsh plugin add github:Jesse-njx/dsh-plugin-manager
```

## 🚀 快速开始

```bash
pnpm install            # from the monorepo root (requires packages/core to exist)
pnpm --filter @dsh-pm/registry test        # node --test, 43 tests
pnpm --filter @dsh-pm/registry typecheck
pnpm --filter @dsh-pm/registry build       # tsc → lib/
```

## 📚 更多信息

**Install**

Workspace package of the `dsh-plugin-manager` monorepo; consumed through `@dsh-pm/core` (workspace dep). The product that wires it into DSH is the plugin manager CLI: dsh plugin add github:Jesse-njx/dsh-plugin-manager

**Usage**

import { createRegistryClient, search } from '@dsh-pm/registry' import type { PmConfig } from '@dsh-pm/core' const cfg: PmConfig['registry'] = { awesomeUrl: 'https://raw.githubusercontent.com/awesome-dsh-plugin/awesome-dsh-plugin/main/README.md', npmKeyword: 'dsh', } const client = createRegistryClient(cfg) // Filtered, sorted: stars desc, then name. const hits = await client.search('memory') // E

## 🔗 链接

- [GitHub 仓库](https://github.com/Jesse-njx/dsh-plugin-manager-registry)
- [完整 README](https://github.com/Jesse-njx/dsh-plugin-manager-registry#readme)
- [返回dsh-plugin-manager-registry所在分类](../plugins.md)
