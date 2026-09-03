---
title: "dsh-plugin-template"
description: "Minimal, verified template for DeepSeek Harness plugins: bundle manifest, one tool, runtime peer guard, tests, and CI that really invokes the tool (dsh 0.1.0-rc.6)."
keywords: "dsh-plugin-template, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-template

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [zoahdev](https://github.com/zoahdev) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Minimal, verified template for DeepSeek Harness plugins: bundle manifest, one tool, runtime peer guard, tests, and CI that really invokes the tool (dsh 0.1.0-rc.6).

## About

A complete dual-side [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugin template. It demonstrates the full plugin surface — a **host** plugin exposing a Typert Remote, and a **client** plugin mounting that Remote into a React view — with type-checking, linting, unit tests, CI, and publishing metadata wired up. Out of the box it registers a `greet` Remote: the host composes `"Hello, "` from a configurable prefix, and the client renders the result in a new "Greet" tab.

## ✨ Key Features

- Node.js `>= 22.19` (or `>= 24`)
- pnpm `>= 9`
- DeepSeek Harness `>=0.1.0-rc.6`

## 📦 Install

```bash
pnpm install
pnpm run build
dsh plugin --profile web add .
```

## 🚀 Quick Start

```bash
dsh plugin --profile web remove dsh-plugin-template
```

## 📚 Learn more

**Install from a local checkout**

pnpm install pnpm run build dsh plugin --profile web add . Restart the Web Harness after rebuilding the plugin. A "Greet" tab appears in the session view ring showing `Hello, DSH`. Remove it with: dsh plugin --profile web remove dsh-plugin-template

**Install from Git**

dsh plugin --profile web add github:you/dsh-plugin-template A Git install fetches sources, not built artifacts, so pnpm runs the `prepare` script to build `lib/`. pnpm ≥10 blocks that build until you allow it; on the first failed `add`, `dsh` prints the fix — copy the package key it shows into the profile's `pnpm-workspace.yaml`: allowBuilds: dsh-plugin-template: true then re-run the `add`. That a

## 🔗 Links

- [GitHub Repository](https://github.com/zoahdev/dsh-plugin-template)
- [Full README](https://github.com/zoahdev/dsh-plugin-template#readme)
- [Back to the Plugins list](../plugins.md)
