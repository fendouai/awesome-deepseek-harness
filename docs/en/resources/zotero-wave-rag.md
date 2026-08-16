---
title: "zotero-wave-rag"
description: "面向 Zotero 论文库的浪潮式 RAG 细节检索系统 —— DSH 外部插件。移植 VCPToolBox 浪潮语义动力学思想（标签河道图传播/虫洞跳转/钟型阻尼/Ω重排），配 BM25+RRF 混合检索、claim-evidence 忠实度校验、两级增量索引"
keywords: "zotero-wave-rag, search, plugin, coding, deepseek harness, dsh"
---
# zotero-wave-rag

> ⭐ 3 · ✅ active · plugin

## One-liner

面向 Zotero 论文库的浪潮式 RAG 细节检索系统 —— DSH 外部插件。移植 VCPToolBox 浪潮语义动力学思想（标签河道图传播/虫洞跳转/钟型阻尼/Ω重排），配 BM25+RRF 混合检索、claim-evidence 忠实度校验、两级增量索引

## About

面向 Zotero 论文库的**浪潮式 RAG** 细节检索系统 —— DeepSeek Harness (DSH) 外部插件（纯 TypeScript，零运行时依赖，`node:sqlite` 直读 Zotero 库）。 在传统向量 RAG（KNN 最近邻）之上，移植并实现了 **VCPToolBox** "浪潮语义动力学" 的四个核心思想 （参考项目：[github.com/lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) ｜ [官网 vcptoolbox.com](https://www.vcptoolbox.com) —— 本仓库按其公开文档所述算法思想**独立重新实现**，未搬运其代码，并在 Zotero 论文库场景落地为可评测的检索系统）： 1. **标签河道图传播** —— 论文为节点、共享标签为河道边（权重 ∝ 1/标签稀有度），查询先做稠密召回得种子，再沿图做 personalized-PageRank 式多跳传播，挖出"语义不相似但沿关系链真实相关"的论文； 2. **虫洞跳转 (Wormhol

## Author
**[Fisfzy](https://github.com/Fisfzy)**

## Links

- [GitHub Repository](https://github.com/Fisfzy/zotero-wave-rag)
- [Full README](https://github.com/Fisfzy/zotero-wave-rag#readme)
- [Back to the Plugins list](../plugins.md)
