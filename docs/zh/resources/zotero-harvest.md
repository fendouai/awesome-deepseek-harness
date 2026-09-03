---
title: "zotero-harvest"
description: "Zotero 文献采集入库插件（DSH external plugin）：多源检索（OpenAlex/arXiv/Crossref/Europe PMC/Semantic Scholar）+ OA 下载链接解析（Unpaywall）+ 充分性审计 + 入库本地 Zotero + 触发 zotero-wave-rag 重建"
keywords: "zotero-harvest, search, plugin, coding, deepseek harness, dsh"
---
# zotero-harvest

> ⭐ **5** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 5 | 状态 | ✅ 活跃 |
| 作者 | [Fisfzy](https://github.com/Fisfzy) | 更新时间 | 2026-08-08 |
| 子分类 | 🌐 网页搜索 | 能力 | coding |

## 一句话介绍

> Zotero 文献采集入库插件（DSH external plugin）：多源检索（OpenAlex/arXiv/Crossref/Europe PMC/Semantic Scholar）+ OA 下载链接解析（Unpaywall）+ 充分性审计 + 入库本地 Zotero + 触发 zotero-wave-rag 重建

## 详细介绍

zotero-harvest 把"检索文献 → 判断够不够 → 存进本地 Zotero → 让 zotero-wave-rag 能检索到"这条链路做成 **6 个纯确定性工具**（无 LLM 依赖），机制取自 AgentLaboratory / STORM / PaperQA / Anaxa： - **检索原语化**（AgentLab）：`lit_fetch` 一次取多源结果 - **高精度命中 + 下载链接**（参考 paper-qa 的 OpenAlex/Crossref/Unpaywall 客户端设计）： - query 传 **DOI 或 arXiv id 直接精确定位**该文献（OpenAlex `doi:` 过滤 / arXiv id_list / Crossref DOI） - 每篇结果解析 **OA 下载链接**：arXiv/Europe PMC/OpenAlex 直链 + **Unpaywall**（DOI→最佳 OA PDF + 全部 OA 位置） - `open_access_only` 过滤、`sort_by: relevance|citations` - **充分性判定 = 配额 + 覆盖审计**（Anaxa + AgentLab）：`lit_sufficiency_check` - **缺口显式化**（STORM）：审计输出 `gaps` + 由缺口推导下一轮查询 - **循环驱动 + 预算上限**（AgentLab）：`lit_review_run` 凑够配额或预算耗尽即停 - **入库**：Zotero 本地 API（桌面运行）→ 离线 sqlite 直写（桌面关闭）→ inbox（RIS/BibTeX+PDF） - **与 RAG 打通**：入库后触发 zotero-wave-rag 增量重建，`zotero_search` 立即可检索新文

## ✨ 核心特性

- **检索原语化**（AgentLab）：`lit_fetch` 一次取多源结果
- **高精度命中 + 下载链接**（参考 paper-qa 的 OpenAlex/Crossref/Unpaywall 客户端设计）：
- **充分性判定 = 配额 + 覆盖审计**（Anaxa + AgentLab）：`lit_sufficiency_check`
- **缺口显式化**（STORM）：审计输出 `gaps` + 由缺口推导下一轮查询
- **循环驱动 + 预算上限**（AgentLab）：`lit_review_run` 凑够配额或预算耗尽即停
- **入库**：Zotero 本地 API（桌面运行）→ 离线 sqlite 直写（桌面关闭）→ inbox（RIS/BibTeX+PDF）

## 🚀 快速开始

```bash
# 构建（用 DSH checkout 的 tsc）
<dsh-checkout>/node_modules/.bin/tsc -p tsconfig.json

# 冒烟：5 工具注册 + 真实 API 调用 + 入库 inbox
node tests/smoke.mjs

# 端到端：空测试库 → review 采集 → sqlite 入库 → zotero-wave-rag 重建 → BM25 可检索
node tests/e2e.mjs

# 真实 Zotero schema 兼容性（在副本上验证写入/去重/附件/RAG 读回）
# 先 cp 真实库到 /tmp/lit-real-test/zotero/ 再运行（路径可改，见脚本内 DB/STORAGE）：
#   node tests/real-lib-check.mjs
```

## 📚 更多信息

**配置**

优先级：运行时配置文件 > 环境变量 > 默认值。 `{"dataDir": "/path/to/zotero", "minCorePapers": 5, "minTotalPapers": 10, "maxRounds": 3, "autoReindex": true}` `LIT_AUTO_REINDEX`、`LIT_S2_API_KEY`、`LIT_UNPAYWALL_EMAIL`（默认 `lit-harvest@users.noreply.github.com`）、 `LIT_RESOLVE_DOWNLOADS`、`LIT_SCHOLAR_PROXY`（可选 scholar 源的 HTTP 代理，如 `http://<proxy-host>:7890`）、`LIT_ZWR_DIR` `~/.config/zotero-wave-rag/config.json` 的 `dataDir

## 🔗 链接

- [GitHub 仓库](https://github.com/Fisfzy/zotero-harvest)
- [完整 README](https://github.com/Fisfzy/zotero-harvest#readme)
- [返回zotero-harvest所在分类](../plugins.md)
