---
title: "dsh-better-edit"
description: "Hash-anchored read/edit/undo_last_edit tools for DeepSeek Harness (dsh), fewer token consumption, lower cost."
keywords: "dsh-better-edit, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-better-edit

> ⭐ **19** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 19 | 状态 | ✅ 活跃 |
| 作者 | [Rianico](https://github.com/Rianico) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Hash-anchored read/edit/undo_last_edit tools for DeepSeek Harness (dsh), fewer token consumption, lower cost.

## 详细介绍

**If you've watched `line 47 → 74` corrupt a file after an insert — this is for you.** Not for one-line touch-ups (near parity) or new files (`write`). Pays off in long sessions and structural edits.

## 📦 安装

```bash
npx @deepseek-ai/dsh plugin --profile web add github:Rianico/dsh-better-edit   # from github
npx @deepseek-ai/dsh plugin --profile web add dsh-better-edit                 # from npm
npx @deepseek-ai/dsh plugin --profile web add /path/to/dsh-better-edit       # local
```

## 🚀 快速开始

```bash
dsh --profile <name> --dump-config   # shows "# == dsh-better-edit" layer
```

## 📚 更多信息

**Install (pick one)**

npx @deepseek-ai/dsh plugin --profile web add github:Rianico/dsh-better-edit # from github npx @deepseek-ai/dsh plugin --profile web add dsh-better-edit # from npm npx @deepseek-ai/dsh plugin --profile web add /path/to/dsh-better-edit # local No config. Next session runs with hashline tools. Verify: dsh --profile <name> --dump-config # shows "# == dsh-better-edit" layer

**Configuration**

Tenancy and prompt guidance declare once, read at `agent/session-start`, no code change. **Store** central by default `$DSH_HOME/plugins/dsh-better-edit/runtime/<name>-<hash8>/` (`ls`-readable + `.wsPath` sidecar). DBs are disposable caches — `rm -rf runtime/<name>-<hash8>/` is safe, rebuilt on next `read`.

**$DSH_HOME/plugins/dsh-better-edit/config.yaml**

storeDir: central # central | workspace | /abs autoGitignore: false undo_ttl_s: 604800 # 7d, -1 forever storeMaxAgeS: 2592000 # 30d janitor storeMaxTotalBytes: 524288000 # 500 MB LRU Env overrides yaml (`DSH_BETTER_EDIT_STORE_DIR`, `DSH_BETTER_EDIT_AUTO_GITIGNORE`). **Guidance per preset** — `tool:read` / `tool:edit` / `tool:undo_last_edit` are plain markdown per preset at `$DSH_HOME/plugins/dsh-b

**Roadmap**

**Current `0.6.1`:** pos-free `resist`/`strict` + tombstone/canons/epoch, per-session `(session,path)` store, `1222` tests, `9/9` harness. <details><summary>Next</summary> </details>

## 🔗 链接

- [GitHub 仓库](https://github.com/Rianico/dsh-better-edit)
- [完整 README](https://github.com/Rianico/dsh-better-edit#readme)
- [返回dsh-better-edit所在分类](../plugins.md)
