---
title: "dsh-news-briefing"
description: "新闻简报技能：多维故事评分、反标题党规则、内容优先级与中文编辑风格。"
keywords: "dsh-news-briefing, research, skill, search, deepseek harness, dsh"
---
# dsh-news-briefing

> ⭐ **0** · ✅ 活跃 · 技能

| | | | |
|---|---|---|---|
| 类型 | 技能 | 分类 | 研究 |
| 星数 | ⭐ 0 | 状态 | ✅ 活跃 |
| 作者 | [canghai666x](https://github.com/canghai666x) | 更新时间 | 2026-08-14 |

## 一句话介绍

> 新闻简报技能：多维故事评分、反标题党规则、内容优先级与中文编辑风格。

## 详细介绍

新闻早报/晚报生成 Skill —— 多源采集 + 五维度评分筛选 + 反标题党写作。聚焦企业故事、人物传记、科技史、时代情绪等深度内容，**不做官媒合集**。 适用于 DeepSeek Harness（DSH）等支持 Skill 概念的 Agent 框架。

## ✨ 核心特性

- RSS：IT之家、36氪、少数派、OSCHINA、阮一峰、The Verge、NPR、华尔街见闻、界面、触乐等（分类：科技/技术社区/国际/财经/文化）
- 实时热点（可选）：社交平台热榜，弥补 RSS 时效；每个请求设 8-10 秒超时，分小批并行

## 🚀 快速开始

```bash
# 📰 新闻早报 | YYYY年MM月DD日

> 每天早上8点，准时推送。专注故事、人物、商业、科技。

## 🔥 今日热点

**1. 标题**
内容描述
来源：xxx
```

## 📚 更多信息

**搭配使用**

配合 **dsh-news-plugin**（新闻采集工具插件）可以自动抓取 RSS 素材：`news_fetch` 返回结构化条目 → 本 Skill 负责五维评分筛选与编排写作。

**安装（一句话版，推荐）**

在 DSH 对话里直接说： > 安装 https://github.com/canghai666x/dsh-news-briefing 这个 skill Agent 安装时会读取仓库内的 `AGENT_INSTALL.md`（给 AI 看的精确安装说明书），按步骤执行并验证。 Agent 会自动完成：clone 仓库 → 放入 skills 目录 → 加载 SKILL.md → 确认可用。全程不用手动敲命令。 **手动安装（备选）：** 将 `SKILL.md` 放入 Agent 的 skills 目录。触发词：新闻早报/晚报/今日新闻。

## 🔗 链接

- [GitHub 仓库](https://github.com/canghai666x/dsh-news-briefing)
- [完整 README](https://github.com/canghai666x/dsh-news-briefing#readme)
- [返回dsh-news-briefing所在分类](../skills.md)
