---
title: "dsh-auto-review"
description: "LLM approval answerer for DeepSeek Harness: deterministic filter + clean-context LLM review for sandbox escalations (requires the patched core, patches included)"
keywords: "dsh-auto-review, memory, plugin, coding, context, ui, deepseek harness, dsh"
---
# dsh-auto-review

> ⭐ **2** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [accpowered](https://github.com/accpowered) | Updated | — |
| Subcategory | 📦 Context management | Capabilities | coding, context, ui |

## One-liner

> LLM approval answerer for DeepSeek Harness: deterministic filter + clean-context LLM review for sandbox escalations (requires the patched core, patches included)

## About

**Second-model AI approval for DeepSeek Harness — a read-only reviewer subagent decides allow/deny on the approval chain, fail-closed by default.** *When an action crosses the sandbox boundary, a second model reads the evidence and returns a verdict with a reason — so humans approve nothing while nothing unsafe slips through.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## 📦 Install

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-auto-review#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-auto-review

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A4 'id: auto-review'
```

## 🚀 Quick Start

```bash
- id: auto-review
  config:
    toolsPolicy:
      overrides: { bash: ai, write: ai }
    contextBudget: { turns: 4, maxChars: 8000 }
```

## 📚 Learn more

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need. Example (annotated full form: `fixtures/config/config-full.yaml`): - id: auto-review name: dsh-auto-review config: toolsPolicy: overrides: { bash: ai, write: ai } riskRules: - pattern: '(?i)(rm\s+(-[a-z]+\s+)*/|git\s+push\s+--force)' policy: never 

**Where the config actually comes from**

**`~/.dsh/settings.yaml` is NOT a config source for this plugin.** An `auto-review:` block there has no effect and produces no warning: like every DSH function plugin, `dsh-auto-review` receives its `Config` from the row the loader mounts it with — the profile's cordis patch layer. (Some other DSH plugins additionally read the settings service, so the inconsistency is easy to trip over, and the sy

**eval/cases/demo.yaml (abridged)**

suite: name: my-suite cases: - id: math-output input: Solve 17 × 24 and reply with only the final number, nothing else. expect: output: { contains: "408" } - id: glob-trace seedFrom: '.' input: Use the glob tool with pattern "src/**" to list the source files… expect: toolCalls: [{ tool: glob, arguments: { contains: { pattern: "src" } } }] results: [{ tool: glob, contains: "index.ts" }] Run it (a D

**or, after npm install: npx dsh-auto-review-mcp**

Environment config: `DSH_AUTO_REVIEW_RISK_RULES` (JSON array of `{pattern, policy, field?}`), `DSH_AUTO_REVIEW_TOOLS_POLICY` (JSON `{default?, overrides?}`), `DSH_AUTO_REVIEW_CACHE_TTL_MS`, `DSH_AUTO_REVIEW_CACHE_MAX_ENTRIES`. Claude Desktop (`claude_desktop_config.json`) example: { "mcpServers": { "dsh-auto-review": { "command": "npx", "args": ["-y", "dsh-auto-review-mcp"], "env": { "DSH_AUTO_REV

## 🔗 Links

- [GitHub Repository](https://github.com/accpowered/dsh-auto-review)
- [Full README](https://github.com/accpowered/dsh-auto-review#readme)
- [Back to the Plugins list](../plugins.md)
