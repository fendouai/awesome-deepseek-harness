---
title: "dsh-kb-sieve"
description: "DSH knowledge-base plugin: build audit-able KB packs (references + SQLite FTS5) from md/txt/docx/pdf, deterministic retrieval (kb_query) and original-text reading (kb_read), zero-script generated skills. Apache-2.0."
keywords: "dsh-kb-sieve, learning, skill, coding, deepseek harness, dsh"
---
# dsh-kb-sieve

> ⭐ **2** · ✅ active · skill

| | | | |
|---|---|---|---|
| Type | skill | Category | Learning |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | 2026-08-12 |

## One-liner

> DSH knowledge-base plugin: build audit-able KB packs (references + SQLite FTS5) from md/txt/docx/pdf, deterministic retrieval (kb_query) and original-text reading (kb_read), zero-script generated skills. Apache-2.0.

## About

知识库筛子——把文档做成**可审计、确定性检索**的知识库插件（DSH 版 kb-sieve）。 三个工具，纯计算（零子代理、零 workflow、零外部服务）：

## 📦 Install

```bash
# 安装
dsh plugin --profile <profile> add git+https://github.com/dsh-external/dsh-kb-sieve.git
dsh --profile <profile>        # 重启生效：kb_build / kb_query / kb_read 随 profile 注入

# 更新 / 卸载
dsh plugin --profile <profile> update
dsh plugin --profile <profile> remove @dsh-external/dsh-kb-sieve
# 或：从 profile 的 package.json 移除依赖后 dsh plugin --profile <profile> update
```

## 🚀 Quick Start

```bash
pnpm install        # typescript/@types/node + fflate（docx 抽取）
pnpm run typecheck  # tsc -b，类型从 sibling deepseek-harness checkout 解析
```

## 📚 Learn more

**安装与使用方式**

装进任意 profile（把 `<profile>` 换成 `tui` / `headless` / `web` 或自建 profile； 需要支持 `dsh plugin` 子命令的 dsh 版本）：

**安装**

dsh plugin --profile <profile> add git+https://github.com/dsh-external/dsh-kb-sieve.git dsh --profile <profile> # 重启生效：kb_build / kb_query / kb_read 随 profile 注入

**设计说明**

line_rowmap + contentful line_fts）。查询主路径全索引化且语义与原版等价： 行匹配 = 每候选文档一次 SQL 子串扫描（instr 命中预小写的 text_lower 列， 流式 top-10 不物化命中集，与原版小写子串语义逐位一致）； 窗口密度重排 = **命中行事件算法**（窗口槽 ∈ [l-20, l-1]，每个命中行至多 4 个槽， 成本 O(命中行数)，与文档总行数解耦；仅计纯字母 token，与原版 [a-z]+ 窗口语义一致）； 置信度 token 覆盖/整句命中 = 行扫描过程中的流式摘要（covered 集合 + phraseHit）。 kb_read 全部模式走 line_text 精准 SQL（sections 走构建时物化的 is_heading 列——标题判定单一来源（src/heading.ts），索引点查；around/fi

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-kb-sieve)
- [Full README](https://github.com/omdsh-dev/dsh-kb-sieve#readme)
- [Back to the Skills list](../skills.md)
