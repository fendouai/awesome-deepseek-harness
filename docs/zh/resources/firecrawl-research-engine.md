---
title: "firecrawl-research-engine"
description: "基于 Firecrawl 的 LLM 深度技术调研与验证技能：搜索优先、精抓补充、自动降级、交叉验证、强制溯源，让技术回答准确、可查、不幻觉。支持 DSH / Claude Code / Codex / Cursor。"
keywords: "firecrawl-research-engine, research, skill, search, deepseek harness, dsh"
---
# firecrawl-research-engine

> ⭐ **0** · ✅ 活跃 · 技能

| | | | |
|---|---|---|---|
| 类型 | 技能 | 分类 | 研究 |
| 星数 | ⭐ 0 | 状态 | ✅ 活跃 |
| 作者 | [hecailiaoPFS](https://github.com/hecailiaoPFS) | 更新时间 | — |

## 一句话介绍

> 基于 Firecrawl 的 LLM 深度技术调研与验证技能：搜索优先、精抓补充、自动降级、交叉验证、强制溯源，让技术回答准确、可查、不幻觉。支持 DSH / Claude Code / Codex / Cursor。

## 详细介绍

A [DSH (DeepSeek Harness)](https://github.com/deepseek-ai/deepseek-harness) skill that turns an LLM agent into a technical research and verification engine. When the user asks about concrete parameters, versions, code details, or recent releases, the skill: 1. **Searches first** with Firecrawl's Search API (not scrape-only) — returns Top-N results *with full page Markdown bodies* 2. **Optionally re-scrapes** the 1-2 most authoritative URLs for missing details 3. **Degrades gracefully** to the built-in `web_search` when Firecrawl is unavailable 4. **Falls back** to local knowledge with an explicit ⚠️ warning when the web has nothing 5. **Verifies and cites**: cross-checks hard facts across ≥2 sources, always inline-cites `[来源: 标题 + URL]`, and surfaces contradictions side by side Its purpose

## 🚀 快速开始

```bash
# any MCP-capable client
export FIRECRAWL_API_KEY=fc-xxxx
# register the server: npx -y firecrawl-mcp
```

## 📚 更多信息

**安装**

1. 将 `SKILL.md` 放入对应环境的技能目录(见上表或 `references/INSTALLATION.md`) 2. 配置 Firecrawl(三选一): - **A(推荐)**:Firecrawl MCP server,配置见 [`examples/cordis.patch.yml`](examples/cordis.patch.yml) - **B**:直接调用 v2 API(`references/FIRECRAWL-API.md`) - **C**:不配置——自动降级内置 `web_search`,反幻觉机制仍生效

## 🔗 链接

- [GitHub 仓库](https://github.com/hecailiaoPFS/firecrawl-research-engine)
- [完整 README](https://github.com/hecailiaoPFS/firecrawl-research-engine#readme)
- [返回firecrawl-research-engine所在分类](../skills.md)
