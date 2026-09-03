---
title: "dsh-llm-verifier"
description: "Configurable DSH-native LLM verifier with a Web settings page"
keywords: "dsh-llm-verifier, search, plugin, coding, deepseek harness, dsh"
---
# dsh-llm-verifier

> ⭐ **11** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 11 | Status | ✅ active |
| Author | [Aa728848](https://github.com/Aa728848) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding |

## One-liner

> Configurable DSH-native LLM verifier with a Web settings page

## About

Generate several coding-agent patches, reject the ones that fail your tests, and let an LLM verifier rank the rest before you decide whether to apply the winner. 简体中文 `dsh-llm-verifier` is a developer-preview plugin for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). It runs **3 or 5 independent coding candidates** in detached Git worktrees, validates every candidate against project tests, ranks the passing patches with [`llm-verifier`](https://pypi.org/project/llm-verifier/), and keeps the original checkout unchanged until a separate approval applies the selected patch.

## ✨ Key Features

- **Best-of-3 or Best-of-5:** use 3 candidates by default, or 5 for higher-value tasks.
- **Validation-first selection:** failing candidates never enter model ranking.
- **Efficient ranking:** one passing candidate wins by validation; two use one pivot; three to five use two pivots.
- **Two approval gates:** one before candidate execution and another before applying the winner.
- **Integrity checks before apply:** repository path, base `HEAD`, clean state, and winner-patch SHA-256 are checked again.
- **Auditable artifacts:** reports include rankings, changed files, timings, process status, patch hashes, verifier requests, and token usage.

## 📦 Install

```bash
git clone https://github.com/Web0926/dsh-llm-verifier.git
cd dsh-llm-verifier

pnpm install --frozen-lockfile
uv sync --frozen --project python
pnpm run check
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add "$(pwd)"
dsh plugin --profile web list
```

## 📚 Learn more

**1. Clone, install, and verify**

git clone https://github.com/Web0926/dsh-llm-verifier.git cd dsh-llm-verifier pnpm install --frozen-lockfile uv sync --frozen --project python pnpm run check

**Configuration**

Default values: Override the plugin entry in the Web profile's `cordis.patch.yml`: config: defaultCandidateCount: 3 candidateProfile: headless credentialRef: DEEPSEEK_API_KEY verifierModel: deepseek-v4-flash nEvaluations: 2 maxVerifierWorkers: 8 verifierEffort: high verifierMaxTokens: 32768 candidateTimeoutMs: 1200000 validationTimeoutMs: 600000 runTimeoutMs: 2700000 maxVerifierTraceBytes: 524288 

## 🔗 Links

- [GitHub Repository](https://github.com/Aa728848/dsh-llm-verifier)
- [Full README](https://github.com/Aa728848/dsh-llm-verifier#readme)
- [Back to the Plugins list](../plugins.md)
