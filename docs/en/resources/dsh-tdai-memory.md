---
title: "dsh-tdai-memory"
description: "Agent memory for DeepSeek Harness | DeepSeek Harness 记忆插件"
keywords: "dsh-tdai-memory, memory, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-tdai-memory

> ⭐ **6** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [Scorp1o117](https://github.com/Scorp1o117) | Updated | 2026-08-21 |
| Subcategory | 🧠 Memory systems | Capabilities | coding, memory, multi-agent |

## One-liner

> Agent memory for DeepSeek Harness | DeepSeek Harness 记忆插件

## About

**GitHub**: [Scorp1o117/dsh-tdai-memory](https://github.com/Scorp1o117/dsh-tdai-memory) · **npm**: [dsh-tdai-memory](https://www.npmjs.com/package/dsh-tdai-memory) Part of the [DeepSeek Harness Enhancement Suite](https://github.com/Scorp1o117/dsh-enhancement-suite) — Vision · Soul/Persona · Long-term Memory · Plugin Marketplace. A port of **TencentDB Agent Memory** (Tencent Cloud's open-source four-layer memory system, originally an OpenClaw plugin) into DeepSeek Harness.

## ✨ Key Features

- **L0 conversation capture**: every turn (turn end, request boundary) is
- **L1 structured memory**: a background pipeline uses an LLM to extract
- **L2 scenes / L3 persona**: scene blocks and user profile generation
- **Automatic recall injection**: on every prompt assembly, relevant memories
- **Tools**: `tdai_memory_search` (L1 structured search),

## 📦 Install

```bash
dsh plugin --profile web add dsh-tdai-memory
```

## 🚀 Quick Start

```bash
- insert:
    - id: tdai-memory
      name: 'dsh-tdai-memory'
      config: {}          # keys can live in settings.yaml instead
```

## 📚 Learn more

**Architecture (porting approach)**

Hard-won wiring details: headless exits); `turn/start` timestamps as the L0 cursor floor; turn-id dedup (L1 extraction finishes before exit; otherwise the 5s shutdown timeout kills it) the agent scope; root listeners never see it); attach one tick after `session/created` by resolving the agent from the `agents` service

**Configuration (profile patch + settings)**

Configuration is **settings-namespace driven**: the profile patch is the base layer, and the `tdai-memory:` section of `$DSH_HOME/settings.yaml` overrides it (LLM/embedding keys live in settings.yaml). The **Web UI Settings → 记忆** section edits every field (v0.2.0, write-only keys); TdaiCore is built at startup, so changes apply **after a restart**.

**Install**

dsh plugin --profile web add dsh-tdai-memory then mount it in `$DSH_HOME/profiles/web/cordis.patch.yml`: - id: tdai-memory name: 'dsh-tdai-memory' config: {} # keys can live in settings.yaml instead and restart `dsh web`. LLM/embedding API keys can be set in the Web UI settings page (记忆 / Memory) or directly in `settings.yaml` under `tdai-memory:`. > **Note for users** > - This plugin is a standar

## 🔗 Links

- [GitHub Repository](https://github.com/Scorp1o117/dsh-tdai-memory)
- [Full README](https://github.com/Scorp1o117/dsh-tdai-memory#readme)
- [Back to the Plugins list](../plugins.md)
