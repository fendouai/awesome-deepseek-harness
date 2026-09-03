---
title: "seo-audit"
description: "Full local & technical SEO audit toolkit for DeepSeek Harness: deterministic Python measurement (53 scripts) + LLM judgment (24 sub-skills, 18 agents), weighted scoring, gated multi-agent fan-out, schema.org, E-E-A-T, GBP, GEO/AI Overviews."
keywords: "seo-audit, research, skill, search, multi-agent, deepseek harness, dsh"
---
# seo-audit

> ⭐ **0** · ✅ active · skill

| | | | |
|---|---|---|---|
| Type | skill | Category | Research |
| Stars | ⭐ 0 | Status | ✅ active |
| Author | [Haniubub](https://github.com/Haniubub) | Updated | — |

## One-liner

> Full local & technical SEO audit toolkit for DeepSeek Harness: deterministic Python measurement (53 scripts) + LLM judgment (24 sub-skills, 18 agents), weighted scoring, gated multi-agent fan-out, schema.org, E-E-A-T, GBP, GEO/AI Overviews.

## About

[English](README.md) | [简体中文](README.zh.md) A production-grade SEO audit toolkit **built for DeepSeek Harness (DSH)** that runs a full, weighted technical, content, schema and local audit on any website — **self-contained and strictly local**: no Claude Code, no plugin marketplace, no third-party SaaS, no per-domain pricing, and **no API key required for the core audit**. It executes as a plain CLI + agent library in the DeepSeek Harness environment and works out of the box. Unlike SEO skills bound to Claude Code, seo-audit is **DSH-native**: you run it in the harness you already use, with nothing leaving your machine. Built for **local SEO**, **technical SEO**, **schema.org**, **E-E-A-T**, **GEO / AI Overviews**, **Google Business Profile (GBP)**, **on-page & content** audits across any i

## 🚀 Quick Start

```bash
Claude Sonnet 5: (0.10 M × $2)   + (0.025 M × $10)   = $0.20 + $0.25 = $0.45
Claude Opus 5:   (0.10 M × $5)   + (0.025 M × $25)   = $0.50 + $0.625 = $1.13
DeepSeek V3.2:   (0.10 M × $0.27)+ (0.025 M × $0.40)  = $0.027 + $0.01 = $0.037
```

## 📚 Learn more

**Quick answer**

**seo-audit is a free, local SEO audit toolkit for DeepSeek Harness (DSH).** You run one command (`./seo audit <url>`) and get a weighted, prioritised action plan covering technical SEO, on-page, schema/JSON-LD, E-E-A-T, GEO/AI Overviews, Local/GBP, backlinks, e-commerce, sitemap, image SEO, content briefs, keyword clustering, drift tracking and Google APIs (PSI/CrUX/GSC). It runs on your own mach

**Example output**

A sample of the top recommendations an audit produces, with their four fields. These are illustrative (anonymised, no real site data) — they show the shape of the output, not a specific client's findings. **① Complete the local structured data** (LocalBusiness / Restaurant) **② Fix a case-sensitive asset path** (stylesheet 404) **③ Add crawlable fallback content + robots & sitemap** These three sp

**Quick start**

New here? See [docs/TUTORIAL.md](docs/TUTORIAL.md) — an end-to-end audit in 5 minutes. cd seo-toolkit ./setup.sh # installs workspace-local deps + Playwright Chromium ./seo doctor # environment health check ./seo audit https://example.com # full weighted audit ./seo technical <url> # technical SEO (9 categories) ./seo page <url> # on-page / content signals ./seo schema <url> # schema.org / LocalBu

**Architecture**

seo-toolkit/ ├── seo.py # CLI orchestrator (weighted score, redaction, gating) ├── lib/ # measurement core (fetch, report, drift, checks_*) ├── scripts/ # 53 ported measurement scripts ├── skills/ # 24 sub-skill prompt packs + reference knowledge ├── agents/ # 18 specialist agent prompts ├── extensions/ # DataForSEO, Firecrawl, Ahrefs, Bing, Banana, … ├── schema/ pdf/ data/ # support assets └── au

## 🔗 Links

- [GitHub Repository](https://github.com/Haniubub/seo-toolkit)
- [Full README](https://github.com/Haniubub/seo-toolkit#readme)
- [Back to the Skills list](../skills.md)
