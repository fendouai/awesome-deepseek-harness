---
title: "zotero-wave-rag"
description: "面向 Zotero 论文库的浪潮式 RAG 细节检索系统 —— DSH 外部插件。移植 VCPToolBox 浪潮语义动力学思想（标签河道图传播/虫洞跳转/钟型阻尼/Ω重排），配 BM25+RRF 混合检索、claim-evidence 忠实度校验、两级增量索引"
keywords: "zotero-wave-rag, search, plugin, coding, deepseek harness, dsh"
---
# zotero-wave-rag

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [Fisfzy](https://github.com/Fisfzy) | 更新时间 | 2026-08-07 |
| 子分类 | 🌐 网页搜索 | 能力 | coding |

## 一句话介绍

> 面向 Zotero 论文库的浪潮式 RAG 细节检索系统 —— DSH 外部插件。移植 VCPToolBox 浪潮语义动力学思想（标签河道图传播/虫洞跳转/钟型阻尼/Ω重排），配 BM25+RRF 混合检索、claim-evidence 忠实度校验、两级增量索引

## 详细介绍

面向 Zotero 论文库的**浪潮式 RAG** 细节检索系统 —— DeepSeek Harness (DSH) 外部插件（纯 TypeScript，零运行时依赖，`node:sqlite` 直读 Zotero 库）。 在传统向量 RAG（KNN 最近邻）之上，移植并实现了 **VCPToolBox** "浪潮语义动力学" 的四个核心思想 （参考项目：[github.com/lioensky/VCPToolBox](https://github.com/lioensky/VCPToolBox) ｜ [官网 vcptoolbox.com](https://www.vcptoolbox.com) —— 本仓库按其公开文档所述算法思想**独立重新实现**，未搬运其代码，并在 Zotero 论文库场景落地为可评测的检索系统）： 1. **标签河道图传播** —— 论文为节点、共享标签为河道边（权重 ∝ 1/标签稀有度），查询先做稠密召回得种子，再沿图做 personalized-PageRank 式多跳传播，挖出"语义不相似但沿关系链真实相关"的论文； 2. **虫洞跳转 (Wormhole)** —— 预计算"结构相连但语义疏远"的桥接边（共享作者/收藏夹、无共享标签、低向量相似），让能量跨领域跳跃； 3. **钟型阻尼 (Bell Damper)** —— 贪心选集时对与已选论文高度同质的候选做重叠惩罚，抑制"同义回音"、保证多样性； 4. **Ω 泛函重排** —— `score = Π[0,1]( α·语义基线 + β·拓扑创新 + γ·直接锚点 )`，其中创新通道只奖励"传播分超过其标签类期望"的候选（对应 RiverMemo Topology V3 的条件创新项），锚点通道保护 hop-0 事实匹配（查询点名标题/作者/标签）。 配套：**论文细节卡生成**（元数据

## ✨ 核心特性

- **直读 Zotero 数据目录**：指向含 `zotero.sqlite`（及 `storage/` PDF）的目录即可，无需导出/迁移；
- **两级索引成本工程**：`ZWR_INDEX_LEVEL=abstract` 只嵌入标题+摘要（成本约全文字级的 1/60），
- **增量嵌入缓存**（缓存 v3）：per-paper 内容哈希，只重嵌变化的论文；全库未变时零嵌入调用直接命中；
- **Zotero 6/7 适配**：Zotero 6 的 `fulltextItems.indexableText` 存原始全文直接读取；Zotero 7
- **校验**：`node scripts/check-zotero-dir.mjs <数据目录>`。

## 🚀 快速开始

```bash
zotero.sqlite(node:sqlite) / 内置示例库
  → 元数据/作者/标签/收藏夹/批注/全文(fulltextItems)
  → 分块 → 可插拔嵌入(hash 离线 | API) → 标签河道图(含wormhole候选边)
  → 稠密种子 → 图传播 → 虫洞 → Ω重排 → 钟型阻尼 → Top-K
  → BM25 全文稀疏通道 + RRF 融合
  → 细节卡生成(抽取式 | LLM，逐句证据校验)   →   评测/消融 CLI
```

## 🔗 链接

- [GitHub 仓库](https://github.com/Fisfzy/zotero-wave-rag)
- [完整 README](https://github.com/Fisfzy/zotero-wave-rag#readme)
- [返回zotero-wave-rag所在分类](../plugins.md)
