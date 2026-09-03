---
title: "dshmarketplace"
description: "Bilingual directory of DeepSeek Harness (DSH) plugins — 3,400+ listings, sandbox-verified install commands, written detail pages, public API. Next.js on Cloudflare Workers."
keywords: "dshmarketplace, registry, awesome-list, coding, deepseek harness, dsh"
---
# dshmarketplace

> ⭐ **2** · ✅ active · awesome-list

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [DshMarketPlace](https://github.com/DshMarketPlace) | Updated | 2026-08-20 |

## One-liner

> Bilingual directory of DeepSeek Harness (DSH) plugins — 3,400+ listings, sandbox-verified install commands, written detail pages, public API. Next.js on Cloudflare Workers.

## About

[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) is DeepSeek's open agent harness, where every capability is a plugin. The ecosystem passed a thousand plugins within weeks of launch. Several directories index them already. Nearly all are card walls: repository name, star count, a link straight out to GitHub. That is a table of contents, not a reference — you still have to read the source to learn what a plugin touches. So the differentiator here is **written depth**. A promoted plugin gets its own page carrying an overview, a documentation section and an illustration, in both languages. That is slow to produce and cannot be scraped, which is the point. This is deliberately early. **60 of 3,420 listings have that page today.** The rest carry metadata, a verdict from a rea

## 📦 Install

```bash
{
  "fullName": "Anionex/dsh-vision-toolkit",
  "summary": "…",
  "summaryZh": "…",
  "stars": 128,
  "npmPackage": "dsh-vision-toolkit",
  "install": "dsh plugin --profile web add dsh-vision-toolkit",
  "installable": true,
  "riskFlags": ["install script"],
  "repoUrl": "https://github.com/Anionex/dsh-vision-toolkit",
  "url": "https://dshmarketplace.dev/plugins/anionex-dsh-vision-toolkit"
}
```

## 🚀 Quick Start

```bash
curl -s 'https://dshmarketplace.dev/api/v1/index'
```

## 📚 Learn more

**Two things about installing DSH plugins**

Both cost real time to find, and neither is this project's doing. **`--profile` is mandatory.** `dsh plugin` forwards to pnpm inside a profile directory, so `dsh plugin add x` exits with *required option '--profile &lt;name&gt;' not specified* and installs nothing. Every command this catalogue emits carries it. **`github:owner/repo#subpath` fails, but `#path:` works.** The bare form is read as a g

**Architecture**

app/(en)/ English routes — root layout sets lang="en" app/(zh)/zh/ Chinese routes — root layout sets lang="zh-Hans" components/views/ The pages themselves, locale-parameterised, shared by both lib/dict.ts Every visible string, both languages db/schema.ts plugins, categories, plugin_stats, submissions scripts/ Author-time jobs: seed, sync, write, promote Next.js 16 on Cloudflare Workers via [OpenNe

## 🔗 Links

- [GitHub Repository](https://github.com/DshMarketPlace/dshmarketplace)
- [Full README](https://github.com/DshMarketPlace/dshmarketplace#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
