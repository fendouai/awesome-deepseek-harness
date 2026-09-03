---
title: "firecrawl-research-engine"
description: "Multi-tier technical research & verification skill using Firecrawl with graceful degradation, cross-source verification, and inline citations. Works with DSH / Claude Code / Codex / Cursor."
keywords: "firecrawl-research-engine, research, skill, search, deepseek harness, dsh"
---
# firecrawl-research-engine

> ⭐ **0** · ✅ active · skill

| | | | |
|---|---|---|---|
| Type | skill | Category | Research |
| Stars | ⭐ 0 | Status | ✅ active |
| Author | [hecailiaoPFS](https://github.com/hecailiaoPFS) | Updated | — |

## One-liner

> Multi-tier technical research & verification skill using Firecrawl with graceful degradation, cross-source verification, and inline citations. Works with DSH / Claude Code / Codex / Cursor.

## About

A [DSH (DeepSeek Harness)](https://github.com/deepseek-ai/deepseek-harness) skill that turns an LLM agent into a technical research and verification engine. When the user asks about concrete parameters, versions, code details, or recent releases, the skill: 1. **Searches first** with Firecrawl's Search API (not scrape-only) — returns Top-N results *with full page Markdown bodies* 2. **Optionally re-scrapes** the 1-2 most authoritative URLs for missing details 3. **Degrades gracefully** to the built-in `web_search` when Firecrawl is unavailable 4. **Falls back** to local knowledge with an explicit ⚠️ warning when the web has nothing 5. **Verifies and cites**: cross-checks hard facts across ≥2 sources, always inline-cites `[来源: 标题 + URL]`, and surfaces contradictions side by side Its purpose

## 🚀 Quick Start

```bash
# any MCP-capable client
export FIRECRAWL_API_KEY=fc-xxxx
# register the server: npx -y firecrawl-mcp
```

## 📚 Learn more

**安装**

1. 将 `SKILL.md` 放入对应环境的技能目录(见上表或 `references/INSTALLATION.md`) 2. 配置 Firecrawl(三选一): - **A(推荐)**:Firecrawl MCP server,配置见 [`examples/cordis.patch.yml`](examples/cordis.patch.yml) - **B**:直接调用 v2 API(`references/FIRECRAWL-API.md`) - **C**:不配置——自动降级内置 `web_search`,反幻觉机制仍生效

## 🔗 Links

- [GitHub Repository](https://github.com/hecailiaoPFS/firecrawl-research-engine)
- [Full README](https://github.com/hecailiaoPFS/firecrawl-research-engine#readme)
- [Back to the Skills list](../skills.md)
