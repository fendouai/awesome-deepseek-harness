---
title: "anime-find"
description: "DeepSeek Harness 搜番插件：对话内多源搜索番剧，卡片展示 Bangumi 评分与详情，支持复制磁力。"
keywords: "anime-find, search, plugin, coding, deepseek harness, dsh"
---
# anime-find

> ⭐ **157** · ✅ 活跃 · 插件 · 近期 ⬆️ +5

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 157 | 状态 | ✅ 活跃 |
| 作者 | [cocofhu](https://github.com/cocofhu) | 更新时间 | 2026-08-19 |
| 子分类 | 🌐 网页搜索 | 能力 | coding |

## 一句话介绍

> DeepSeek Harness 搜番插件：对话内多源搜索番剧，卡片展示 Bangumi 评分与详情，支持复制磁力。

## 详细介绍

DeepSeek Harness 搜番插件。在对话中搜索番剧，以可点击卡片展示结果，并在详情面板中查看字幕组、磁力链接和种子文件。

## ✨ 核心特性

- 聚合 [Mikan](https://mikanani.me)、[AniBT](https://anibt.net) 和 [AnimeGarden](https://animes.garden)
- 在对话流中展示番剧封面、标题、评分、格式和资源数量
- 根据 Asia/Shanghai 时区识别当前新番季度
- 支持「还有吗」「换一批」等追问并分页展示更多结果
- 点击卡片后按字幕组和集数浏览资源，并可查看 Bangumi 介绍、评分和短评
- 支持复制磁力链接和打开 `.torrent` 文件
- 可选流媒体 Tab：按搜索结果显示用户规则解析出的可播源，并在同页选集播放
- 可在 Harness 插件设置中启用来源、调整结果数量和站点地址

## 📦 安装

```bash
dsh plugin --profile web add @cocofhu/anime-find
```

## 🚀 快速开始

```bash
dsh plugin --profile web add /absolute/path/to/anime-find
```

## 📚 更多信息

**安装**

从 [npm](https://www.npmjs.com/package/@cocofhu/anime-find) 安装： dsh plugin --profile web add @cocofhu/anime-find 本地开发： dsh plugin --profile web add /absolute/path/to/anime-find 安装后重启 `dsh web`，并强制刷新浏览器页面。不要用 `github:cocofhu/anime-find` 或无前缀的 `anime-find` 安装：git 源会跑 `prepare`；旧包名已迁到 `@cocofhu/anime-find`。

**使用**

可以直接对 Agent 说： > 搜一下无职转生，看看有没有磁力 > 最近有哪些好看的动漫 > 还有吗 插件向 Agent 提供 `anime_find_search` 工具。搜索完成后，对话中会显示可点击卡片；点击卡片即可查看字幕组与下载资源。

**配置**

打开 **设置 → 插件 → 插件配置 → 搜番**： 保存后立即生效。用户配置落在 Harness 用户目录 `$DSH_HOME/settings.yaml` 的 `anime-find:` 段（由 dsh 设置服务原子写入）。版本与安装来源为只读信息，不会写入该段。 从旧版升级时，若仍存在 `$DSH_HOME/anime-find.json` 且 yaml 中尚无该用户段，插件会把 json 导入 `anime-find:` 后将原文件改名为 `anime-find.json.bak`；若 yaml 里已有用户配置则跳过导入，仍只改名备份，之后不再读取 json。

## 🔗 链接

- [GitHub 仓库](https://github.com/cocofhu/anime-find)
- [完整 README](https://github.com/cocofhu/anime-find#readme)
- [返回anime-find所在分类](../plugins.md)
