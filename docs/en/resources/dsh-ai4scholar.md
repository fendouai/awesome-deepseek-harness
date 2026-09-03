---
title: "dsh-ai4scholar"
description: "AI4Scholar for DeepSeek Harness (dsh): 38 native academic tools — Semantic Scholar, PubMed, Google Scholar, arXiv, bioRxiv/medRxiv, DOI, full text, auto-cite, figures, unified search. Powered by ai4scholar.net"
keywords: "dsh-ai4scholar, search, plugin, coding, deepseek harness, dsh"
---
# dsh-ai4scholar

> ⭐ **14** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 14 | Status | ✅ active |
| Author | [literaf](https://github.com/literaf) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, search |

## One-liner

> AI4Scholar for DeepSeek Harness (dsh): 38 native academic tools — Semantic Scholar, PubMed, Google Scholar, arXiv, bioRxiv/medRxiv, DOI, full text, auto-cite, figures, unified search. Powered by ai4scholar.net

## About

Academic literature tools for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`), delivered as 38 native agent tools — the same coverage as the AI4Scholar plugins for OpenClaw, Codex, and Hermes. Powered by [ai4scholar.net](https://ai4scholar.net?src=dsh). Every paper-list tool returns one normalized record shape — title, authors, year, venue, citation count, DOI/PMID/arXiv ids, URL, open-access PDF, abstract — so the model (and Code Mode programs) can chain calls across platforms without special cases. Results render as citation cards in the dsh Web UI; full-text tools return the PDF text in slices (`offset` / `max_chars`) so a 40-page paper never floods the context. **Credits are visible.** Every billed tool card in the chat carries the charge in its title (`Sema

## 📚 Learn more

**Configuration**

The bundle mounts one row (`id: ai4scholar`) with these defaults. Override from your profile's `cordis.patch.yml` (a patch replaces the whole `config`, so restate every key you keep): config: apiKeyEnv: AI4SCHOLAR_API_KEY # credential reference; the key itself never lives in config baseUrl: https://ai4scholar.net # tool families semanticScholar: true pubmed: true googleScholar: true arxiv: true bi

## 🔗 Links

- [GitHub Repository](https://github.com/literaf/dsh-ai4scholar)
- [Full README](https://github.com/literaf/dsh-ai4scholar#readme)
- [Back to the Plugins list](../plugins.md)
