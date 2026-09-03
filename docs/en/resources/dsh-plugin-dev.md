---
title: "dsh-plugin-dev"
description: "Field-tested plugin development playbook (skill + docs): cordis dual copies, tsconfig triplets, Windows junctions and multi-frame zstd."
keywords: "dsh-plugin-dev, learning, skill, coding, deepseek harness, dsh"
---
# dsh-plugin-dev

> ⭐ **13** · ✅ active · skill · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | skill | Category | Learning |
| Stars | ⭐ 13 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | 2026-08-21 |

## One-liner

> Field-tested plugin development playbook (skill + docs): cordis dual copies, tsconfig triplets, Windows junctions and multi-frame zstd.

## About

1. 把 `skills/dsh-plugin-dev` 放进 skills 目录（或在 agent 会话中引用）； 2. 从 [SKILL.md](skills/dsh-plugin-dev/SKILL.md) 的流程与踩坑速查表入手； 3. 构建前看 [references/build-pitfalls.md](skills/dsh-plugin-dev/references/build-pitfalls.md)——第一条就是 cordis 双副本。

## 🚀 Quick Start

```bash
dsh --version && readlink ~/.dsh/source/current     # 快照
node -v                                              # Node
gh --version && gh auth status                       # gh 与认证
node <mono>/node_modules/typescript/bin/tsc --version  # TS（<mono> 换成 current 真实路径）
node <mono>/node_modules/vitest/vitest.mjs --version   # Vitest
```

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-plugin-dev)
- [Full README](https://github.com/omdsh-dev/dsh-plugin-dev#readme)
- [Back to the Skills list](../skills.md)
