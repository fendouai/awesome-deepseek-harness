---
title: "zotero-harvest"
description: "Zotero 文献采集入库插件（DSH external plugin）：多源检索（OpenAlex/arXiv/Crossref/Europe PMC/Semantic Scholar）+ OA 下载链接解析（Unpaywall）+ 充分性审计 + 入库本地 Zotero + 触发 zotero-wave-rag 重建"
keywords: "zotero-harvest, search, plugin, coding, deepseek harness, dsh"
---
# zotero-harvest

> ⭐ 5 · ✅ active · plugin

## One-liner

Zotero 文献采集入库插件（DSH external plugin）：多源检索（OpenAlex/arXiv/Crossref/Europe PMC/Semantic Scholar）+ OA 下载链接解析（Unpaywall）+ 充分性审计 + 入库本地 Zotero + 触发 zotero-wave-rag 重建

## About

zotero-harvest 把"检索文献 → 判断够不够 → 存进本地 Zotero → 让 zotero-wave-rag 能检索到"这条链路做成 **6 个纯确定性工具**（无 LLM 依赖），机制取自 AgentLaboratory / STORM / PaperQA / Anaxa： - **检索原语化**（AgentLab）：`lit_fetch` 一次取多源结果 - **高精度命中 + 下载链接**（参考 paper-qa 的 OpenAlex/Crossref/Unpaywall 客户端设计）： - query 传 **DOI 或 arXiv id 直接精确定位**该文献（OpenAlex `doi:` 过滤 / arXiv id_list / Crossref DOI） - 每篇结果解析 **OA 下载链接**：arXiv/Europe PMC/OpenAlex 直链 + **Unpaywall**（DOI→最佳 OA PDF + 全部 OA 位置） - `open_access_only` 过滤、`sort_by: relevance|citations` - **

## Author
**[Fisfzy](https://github.com/Fisfzy)**

## Links

- [GitHub Repository](https://github.com/Fisfzy/zotero-harvest)
- [Full README](https://github.com/Fisfzy/zotero-harvest#readme)
- [Back to the Plugins list](../plugins.md)
