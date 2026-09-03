---
title: "dsh-plugin-workshop"
description: "Steam Workshop-style plugin browser for the DSH Web UI: zero-server, GitHub-powered search and one-click install."
keywords: "dsh-plugin-workshop, discovery, plugin, ui, workflow, deepseek harness, dsh"
---
# dsh-plugin-workshop

> ⭐ **25** · ✅ active · plugin · ⬆️ +5 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Plugin discovery |
| Stars | ⭐ 25 | Status | ✅ active |
| Author | [yyyyukari](https://github.com/yyyyukari) | Updated | 2026-08-17 |

## One-liner

> Steam Workshop-style plugin browser for the DSH Web UI: zero-server, GitHub-powered search and one-click install.

## About

DeepSeek Harness（DSH）的**创意工坊式插件浏览器**——零服务器、单包开箱即用，内置在 DSH Web UI 侧栏「新会话」按钮正下方。

## ✨ Key Features

- **侧栏常驻入口**：官方「新会话」按钮正下方，同款样式（DOM 克隆官方按钮，宽/窄侧栏自适应），刷新、重启都不丢
- **搜索与排序**：关键词搜索（支持中文，自动映射英文）、★最热 / ⏰最新、**飙升榜时间窗口**（近 7/30/90 天新建 + 热度排序，Steam Trending 近似）
- **默认只搜 DSH 插件**：默认「插件话题」（`topic:dsh-plugin`）；搜索结果自动排除官方 harness 等核心仓库（查询级 `-repo:` 过滤，不再占据榜首）；全站模式自带**插件特征验证**（检查 `package.json` 的 `dsh` 字段 / `cordis.yml` 等，走 r
- **已安装管理**：工具栏「📦 已安装」视图——合并 profile 依赖/激活行/本地预设展示本机插件（类型、激活状态、安装来源），一键更新（pnpm update / git pull）与卸载
- **双语体验**：描述一键切换原文/中文机翻，README 可整篇翻译（Google 翻译接口，自动缓存）
- **智能一键安装/卸载（预检分级）**：详情页自动预检仓库结构，给出「可直接安装 / 有风险 / 建议手动」三级评级——标准 bundle/nested/preset 一键安装照旧；特殊结构（多包 monorepo、非插件仓库、带构建脚本等）自动降级为**作者给出的安装方式**（从 README 提取安装命令，可复制，
- **详情页**：星数/fork/语言/许可证/创建时间、README 轻量渲染、手动安装命令、GitHub 直达
- **额度透明**：实时显示 GitHub 搜索剩余额度与恢复倒计时；可选填 GitHub Token（30 次/分，仅存本机浏览器）

## 📦 Install

```bash
# 一条命令即可：本包在 package.json 声明了 dsh.bundle.patch，
# dsh plugin add 会自动把它加入 profile 的 dsh.profile.bundles，
# 启动时其 cordis.patch.yml 作为 bundle 补丁层自动激活，无需手改配置。
dsh plugin --profile web add "github:yyyyukari/dsh-plugin-workshop"

# 重启 dsh web 并刷新浏览器
```

## 🚀 Quick Start

```bash
> - insert:
>     - id: plugin-workshop
>       name: '@dsh-external/dsh-plugin-workshop'
>
```

## 🔗 Links

- [GitHub Repository](https://github.com/yyyyukari/dsh-plugin-workshop)
- [Full README](https://github.com/yyyyukari/dsh-plugin-workshop#readme)
- [Back to the Plugins list](../plugins.md)
