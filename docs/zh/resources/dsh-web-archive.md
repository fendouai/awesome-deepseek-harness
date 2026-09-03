---
title: "dsh-web-archive"
description: "折叠对话当中众多的“无用消息”，例如Think、Bash等"
keywords: "dsh-web-archive, search, plugin, coding, deepseek harness, dsh"
---
# dsh-web-archive

> ⭐ **9** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 9 | 状态 | ✅ 活跃 |
| 作者 | [renat3u](https://github.com/renat3u) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding |

## 一句话介绍

> 折叠对话当中众多的“无用消息”，例如Think、Bash等

## 详细介绍

**Deep Sleeping...** — DeepSeek Harness (dsh) Web 模式的客户端插件。 把会话里**正文之外的所有 display**（工具卡片 read / bash / web_search / grep / edit 等，以及消息内的 **Think 推理块**，含运行中的调用）折叠成内联的小卡片， **无 emoji、与 Read/Think/Bash 卡片同款样式、放在它们原来的位置**： - **每条消息的 think 组 + 其后紧跟的工具组合成一块**（落单的 think 组 / 工具组各自成块），工具组区域随块折叠、不留空白； - 正文消息保持 `文本a - [折叠块] - 文本b - 文本c` 的原始结构。 Deep Sleeping... (3) ← 折叠态，点击展开 Deep Sleeping... (3) · 收起 ← 展开态，所有卡片原地显示 前端不再出现一长串 Read / Think / Bash 卡片；正文消息完全不受影响。

## ✨ 核心特性

- **零核心改动**：纯浏览器端插件，不修改 dsh 任何源码、不注册 slot key，
- **零运行时依赖**：bundle 完全自包含，不 require 任何模块表条目。
- **Think 也折叠**：消息内的推理块（`data-variant="think"`）与工具卡片
- **实时跟随**：MutationObserver + rAF 合并，流式新卡片、卡片结算、切换
- **选择联动**：折叠态下若有行被选中（详情联动），自动展开该簇，避免
- **主题适配**：颜色走 dsh 的 `--dsw-*` CSS 变量（带兜底值），明暗主题

## 📦 安装

```bash
pnpm dsh plugin --profile web add file:/path/to/dsh-web-archive
```

## 🚀 快速开始

```bash
ln -s /path/to/dsh-web-archive $DSH_HOME/profiles/node_modules/dsh-web-archive
```

## 📚 更多信息

**特性**

不会与内置工具卡片的 `conversation.chat.toolview` 注册冲突。 一并合并。 会话都自动重放折叠状态。 看不到正在查看的卡片。 都可用。

**工作原理**

ChatView 渲染时对每个工具调用行写入稳定 data 属性： 插件只做两件事： 1. 把 `[data-chat-flow]` 里的**非正文行**——顶层 `[data-chat-call-id]` 工具卡片行 + `[data-variant="think"]` 且无 `data-tool` 的推理块行—— `display:none`（React 的 vdom diff 不会覆盖 CSSOM 上的手动样式）； 2. 把**每个回合合成一块**：某条消息的 think 组与紧跟其后的工具组（跳过 装饰元素）合并，在 think 消息的**原位**插入一张与工具卡片同款样式的 小卡片（`Deep Sleeping... (N)`，N = think 行数 + 工具卡片数），工具组 元素随块折叠；点击切换展开/收起。落单的 think 组 / 工具组各自成块。 正文消息保持 `文本a

**安装**

插件以 **bundle 层** 方式挂载进 dsh web profile（`package.json` 里的 `dsh.bundle.patch` 声明 + 包内 `cordis.patch.yml` 的 `insert` 行）， `dsh.client` 声明（`platform: "web"`）让 client-modules 服务自动注入浏览器 bundle。 > 命令形式：官方约定源码 checkout 场景统一用 `pnpm dsh <args...>` 运行 > TypeScript 入口并透传参数（见下文「运行与构建」）；npm 全局安装后可直接 > `dsh <args...>`。下文命令按 `dsh …` 泛称书写。

## 🔗 链接

- [GitHub 仓库](https://github.com/renat3u/dsh-web-archive)
- [完整 README](https://github.com/renat3u/dsh-web-archive#readme)
- [返回dsh-web-archive所在分类](../plugins.md)
