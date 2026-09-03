---
title: "dsh-plugin-market"
description: "DeepSeek Harness plugin market - browse, search & install dsh-plugin topic plugins (dsh 插件市场：浏览/搜索/安装插件)"
keywords: "dsh-plugin-market, registry, awesome-list, coding, search, deepseek harness, dsh"
---
# dsh-plugin-market

> ⭐ **5** · ✅ 活跃 · 精选列表 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 精选列表 | 分类 | 注册表 |
| 星数 | ⭐ 5 | 状态 | ✅ 活跃 |
| 作者 | [TheYoungChen](https://github.com/TheYoungChen) | 更新时间 | 2026-08-21 |

## 一句话介绍

> DeepSeek Harness plugin market - browse, search & install dsh-plugin topic plugins (dsh 插件市场：浏览/搜索/安装插件)

## 详细介绍

一个 DeepSeek Harness（dsh）插件市场 bundle 插件：在 Web UI 左侧「设置」上方新增「插件市场」入口（同时集成到 设置 → 插件 → 插件市场 标签页），分页浏览 GitHub [`dsh-plugin`](https://github.com/topics/dsh-plugin) topic 里的全部插件，支持搜索、一键安装与实时进度。

## ✨ 核心特性

- **双入口**：侧边栏「设置」上方的入口按钮；设置 → 插件 → 插件市场 标签页，内容一致
- **浏览 / 搜索 / 分页**：聚合 `dsh-plugin` topic 全部插件，按 star 排序，关键字搜索，每页 20 条，带「刷新」按钮
- **静态索引 + CDN**：数据优先来自 GitHub Action 每 2 小时生成的 `registry.json`（jsDelivr CDN 分发，国内快），终端零 API 调用、零限流；索引不可用时自动回退搜索 API
- **已安装识别 + 更新**：读 profile 真实依赖 + `repository` 归属校验，已装的插件置顶；自动对比最新版本，有新版显示「更新」按钮，一键覆盖升级
- **一键安装**：确认框 → 真实执行 `pnpm add github:<owner/repo>`（等价于官方 `dsh plugin add`），自动把声明 `dsh.bundle` 的依赖 reconcile 进 `dsh.profile.bundles` 层栈
- **安装可视化**：实时日志 + 已用时长，可随时**终止**（真正杀掉进程）或转**后台下载**
- **后台通知**：右上角常驻状态条（不遮挡会话页头），运行中可终止、可点击展开为终端面板看实时日志；完成后带「立即重启」按钮，手动关闭
- **统计与指引**：插件总数统计、「如何发布插件」引导链接

## 📦 安装

```bash
dsh plugin --profile web add github:TheYoungChen/dsh-plugin-market && dsh web
```

## 🚀 快速开始

```bash
cd dsh-plugin-market
pnpm install          # 装 tsdown / react / @types/react 等 devDeps
pnpm build            # 产出 lib/index.mjs + lib/index.js
```

## 📚 更多信息

**⚡ 一键安装（复制即用）**

**喂给 AI 的一句话**（AI 具备命令执行能力即可，无需解释）： > 安装 dsh-plugin-market：运行 `dsh plugin --profile web add github:TheYoungChen/dsh-plugin-market`，然后重启 `dsh web`。 **或者直接复制命令：** dsh plugin --profile web add github:TheYoungChen/dsh-plugin-market && dsh web > 本插件无 `prepare` 构建脚本、`lib/` 已预编译，git 安装零额外构建；安装完成后重启 dsh 生效。

## 🔗 链接

- [GitHub 仓库](https://github.com/TheYoungChen/dsh-plugin-market)
- [完整 README](https://github.com/TheYoungChen/dsh-plugin-market#readme)
- [返回dsh-plugin-market所在分类](../awesome-lists.md)
