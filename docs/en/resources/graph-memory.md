---
title: "graph-memory"
description: "Deepseek Harness、Openclaw知识图谱记忆插件。2026年4月受邀发布在清华大学讨论会。Knowledge Graph + Memory；Knowledge Graph Context Engine for OpenClaw — extracts structured triples from conversations, compresses context 75%, enables cross-session experience reuse"
keywords: "graph-memory, memory, plugin, coding, deepseek harness, dsh"
---
# graph-memory

> ⭐ **564** · ✅ active · plugin · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 564 | Status | ✅ active |
| Author | [adoresever](https://github.com/adoresever) | Updated | 2026-08-21 |
| Subcategory | 🧠 Memory systems | Capabilities | coding, memory |

## One-liner

> Deepseek Harness、Openclaw知识图谱记忆插件。2026年4月受邀发布在清华大学讨论会。Knowledge Graph + Memory；Knowledge Graph Context Engine for OpenClaw — extracts structured triples from conversations, compresses context 75%, enables cross-session experience reuse

## About

Traceable, searchable, cross-session memory for AI agents. One memory core, native to DeepSeek Harness, with the OpenClaw plugin entry retained. 中文 · Advantages · Architecture · DSH Install · Pro Plugin · Technical Report (Chinese) Compaction answers “how much of this conversation still fits?” Graph Memory answers “which past knowledge is worth recalling now?” Reusable conversation knowledge becomes typed nodes: - `TASK`: goals, execution, and outcomes; - `SKILL`: validated reusable methods; - `EVENT`: errors, fixes, decisions, changes, and facts. Typed edges such as `USED_SKILL`, `SOLVED_BY`, `REQUIRES`, `PATCHES`, and `CONFLICTS_WITH` preserve relationships. A new question retrieves a relevant local subgraph instead of replaying the complete history.

## ✨ Key Features

- `TASK`: goals, execution, and outcomes;
- `SKILL`: validated reusable methods;
- `EVENT`: errors, fixes, decisions, changes, and facts.

## 📦 Install

```bash
npx @deepseek-ai/dsh plugin --profile web add github:adoresever/graph-memory
npx @deepseek-ai/dsh --profile web --dump-config
npx @deepseek-ai/dsh web
```

## 🚀 Quick Start

```bash
git clone https://github.com/adoresever/graph-memory.git
cd graph-memory
npm install
npm test
npm pack
npx @deepseek-ai/dsh plugin --profile web add /absolute/path/to/graph-memory-1.6.0-beta.10.tgz
```

## 📚 Learn more

**Install on DeepSeek Harness**

Prerequisite: Node.js `22.13+`. The current beta is not yet published to npm, but the repository ships its prebuilt runtime and can be installed without authorizing install scripts: npx @deepseek-ai/dsh plugin --profile web add github:adoresever/graph-memory npx @deepseek-ai/dsh --profile web --dump-config npx @deepseek-ai/dsh web Alternatively, build and install a tarball from a checkout: git clo

**Current local installation**

The npm package `graph-memory@1.5.8` is still the OpenClaw release. The new Community beta can be installed from GitHub; `graph-memory-pro-dsh` still installs from a checkout: dsh plugin --profile web add \ git+https://github.com/adoresever/graph-memory.git dsh plugin --profile web add \ /absolute/path/to/graph-memory/dsh-pro dsh web Both plugins share `~/.dsh/graph-memory/graph-memory.db` by defa

## 🔗 Links

- [GitHub Repository](https://github.com/adoresever/graph-memory)
- [Full README](https://github.com/adoresever/graph-memory#readme)
- [Back to the Plugins list](../plugins.md)
