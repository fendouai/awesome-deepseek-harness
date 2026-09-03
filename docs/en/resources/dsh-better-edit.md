---
title: "dsh-better-edit"
description: "Hash-anchored read/edit/undo_last_edit tools for DeepSeek Harness (dsh), fewer token consumption, lower cost."
keywords: "dsh-better-edit, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-better-edit

> ⭐ **19** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 19 | Status | ✅ active |
| Author | [Rianico](https://github.com/Rianico) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Hash-anchored read/edit/undo_last_edit tools for DeepSeek Harness (dsh), fewer token consumption, lower cost.

## About

**If you've watched `line 47 → 74` corrupt a file after an insert — this is for you.** Not for one-line touch-ups (near parity) or new files (`write`). Pays off in long sessions and structural edits.

## 📦 Install

```bash
npx @deepseek-ai/dsh plugin --profile web add github:Rianico/dsh-better-edit   # from github
npx @deepseek-ai/dsh plugin --profile web add dsh-better-edit                 # from npm
npx @deepseek-ai/dsh plugin --profile web add /path/to/dsh-better-edit       # local
```

## 🚀 Quick Start

```bash
dsh --profile <name> --dump-config   # shows "# == dsh-better-edit" layer
```

## 📚 Learn more

**Install (pick one)**

npx @deepseek-ai/dsh plugin --profile web add github:Rianico/dsh-better-edit # from github npx @deepseek-ai/dsh plugin --profile web add dsh-better-edit # from npm npx @deepseek-ai/dsh plugin --profile web add /path/to/dsh-better-edit # local No config. Next session runs with hashline tools. Verify: dsh --profile <name> --dump-config # shows "# == dsh-better-edit" layer

**Configuration**

Tenancy and prompt guidance declare once, read at `agent/session-start`, no code change. **Store** central by default `$DSH_HOME/plugins/dsh-better-edit/runtime/<name>-<hash8>/` (`ls`-readable + `.wsPath` sidecar). DBs are disposable caches — `rm -rf runtime/<name>-<hash8>/` is safe, rebuilt on next `read`.

**$DSH_HOME/plugins/dsh-better-edit/config.yaml**

storeDir: central # central | workspace | /abs autoGitignore: false undo_ttl_s: 604800 # 7d, -1 forever storeMaxAgeS: 2592000 # 30d janitor storeMaxTotalBytes: 524288000 # 500 MB LRU Env overrides yaml (`DSH_BETTER_EDIT_STORE_DIR`, `DSH_BETTER_EDIT_AUTO_GITIGNORE`). **Guidance per preset** — `tool:read` / `tool:edit` / `tool:undo_last_edit` are plain markdown per preset at `$DSH_HOME/plugins/dsh-b

**Roadmap**

**Current `0.6.1`:** pos-free `resist`/`strict` + tombstone/canons/epoch, per-session `(session,path)` store, `1222` tests, `9/9` harness. <details><summary>Next</summary> </details>

## 🔗 Links

- [GitHub Repository](https://github.com/Rianico/dsh-better-edit)
- [Full README](https://github.com/Rianico/dsh-better-edit#readme)
- [Back to the Plugins list](../plugins.md)
