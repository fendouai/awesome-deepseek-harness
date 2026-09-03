---
title: "dsh-recommend"
description: "透明插件排行榜与推荐：每日自动抓取 dsh-plugin 主题数据，开放评分模型。"
keywords: "dsh-recommend, discovery, plugin, search, ui, deepseek harness, dsh"
---
# dsh-recommend

> ⭐ **18** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 插件发现 |
| 星数 | ⭐ 18 | 状态 | ✅ 活跃 |
| 作者 | [zp-home](https://github.com/zp-home) | 更新时间 | 2026-08-21 |

## 一句话介绍

> 透明插件排行榜与推荐：每日自动抓取 dsh-plugin 主题数据，开放评分模型。

## 详细介绍

[设计文档](docs/DESIGN.md) · [评分模型](docs/scoring.md) · [路线图](docs/roadmap.md) · [数据](data/rankings.json) · [中文](README.zh.md)

## ✨ 核心特性

- **透明**：评分公式、权重、全部原始数据都公开在这个仓库里，任何人 `clone` 后跑一遍 `node scripts/sync.mjs` 即可复算——这是排行类项目信任的基石
- **可信**：官方本体/非插件 denylist（`scripts/exclude-list.json`）+ 榜单前 200 名**深扫插件性验证**（`scripts/scan.mjs` 检测 `dsh` 声明 / `@deepseek-ai/*` 依赖 / cordis 配置 / skills 特征），未检出特征的
- **安全提示（仅供参考）**：市场 GitHub Actions 以公开的只读规则扫描源码和发布 bundle，规则、版本、上限与已知盲区见 [静态安全扫描算法](docs/security-scanning.md)。未命中规则不等于安全，提示不构成安全认证，也不影响评分或安装资格
- **可审计全量**：GitHub Search 单查询超过 1000 条时，采集器按创建日期、仓库大小与 Star 的无重叠闭区间递归分片；`topic-coverage.json` 记录每个叶子查询的 `total_count`、去重数、重试与溢出。任一叶子不完整即终止全量发布，不以部分数据更新榜单
- **自动化**：GitHub Actions 每 5 小时全量重算并提交 `data/`（含深扫、历史快照、徽章、月度报告），数据永不人工维护
- **一份数据，多个消费端**：`data/registry.json` 是唯一事实源，静态排行站、DSH 插件（模型工具 + 设置页标签）、外部工具共用；`data/history.json` 提供每日趋势

## 📦 安装

```bash
dsh plugin --profile web add dsh-recommend
# 重启 dsh web 后生效
```

## 🚀 快速开始

```bash
dsh plugin --profile web add github:zp-home/dsh-recommend
dsh --profile web --dump-config   # 应出现 "# == dsh-recommend" 层
# 重启 dsh web 后生效
```

## 📚 更多信息

**1️⃣ 网页版排行（不用安装）**

👉 打开 **https://zp-home.github.io/dsh-recommend/site/** —— Neo-Brutalism 高对比排行榜：醒目的前三名奖牌、四维信号分数与 🏅 精选认证，支持搜索 / 分类筛选 / 四种排序（综合分 / 热度 / 最近更新 / 最新发布）、分页浏览、详情展开（主题标签 / 许可证 / 发布时间 / 深扫状态）、近 N 天**综合分走势图**，以及一键复制**安装命令**。 🏆 **发展排行榜**（独立页面）：**https://zp-home.github.io/dsh-recommend/site/rankings.html** —— star 增长最快（7/30/90 天）、排名上升最快、npm 下载量最多、本周新上榜、精选认证，每条带增长曲线 sparkline。 **📸 效果预览：** 也可以直接看原始数据：[`data/rank

**2️⃣ 在 DSH 里安装插件（✅ 已真机验证）**

**方式 A：npm 安装（国内用户推荐，走 npmmirror 镜像）** dsh plugin --profile web add dsh-recommend

## 🔗 链接

- [GitHub 仓库](https://github.com/zp-home/dsh-recommend)
- [完整 README](https://github.com/zp-home/dsh-recommend#readme)
- [返回dsh-recommend所在分类](../plugins.md)
