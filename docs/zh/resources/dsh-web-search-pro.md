---
title: "dsh-web-search-pro"
description: "多引擎持久搜索：DeepSeek/Exa/DDG/Bing/Jina + GitHub/B站/YouTube/V2EX/小红书/推特/Reddit/RSS，SQLite+LRU 缓存 + Playwright 渲染。"
keywords: "dsh-web-search-pro, search, plugin, browser, deepseek harness, dsh"
---
# dsh-web-search-pro

> ⭐ **29** · ✅ 活跃 · 插件 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 29 | 状态 | ✅ 活跃 |
| 作者 | [anweat](https://github.com/anweat) | 更新时间 | 2026-08-14 |
| 子分类 | 🌐 网页搜索 | 能力 | search, browser |

## 一句话介绍

> 多引擎持久搜索：DeepSeek/Exa/DDG/Bing/Jina + GitHub/B站/YouTube/V2EX/小红书/推特/Reddit/RSS，SQLite+LRU 缓存 + Playwright 渲染。

## 详细介绍

增强型、可持久化的扩展网页搜索插件 for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（DSH）。 一个 DSH **bundle 插件**，把多引擎网页搜索、平台搜索、持久化缓存、受控按站增强和 Playwright 渲染打包成模型可直接调用的 11 个工具。路由控制面借鉴 Agent-Reach 的后端探测、顺序选择和失败冷却思路，核心逻辑为本项目原生 TypeScript 实现。

## 📦 安装

```bash
dsh plugin --profile web add @anweat/dsh-browser@^0.1.8 dsh-web-search-pro@^0.1.8
# 或本地目录 / tarball：
dsh plugin --profile web add ../dsh-browser ./dsh-web-search-pro
# 重启（web profile 关闭了 HMR）：
dsh --profile web
```

## 🚀 快速开始

```bash
# npm 安装：显式升级两个包，避免 profile 锁文件继续保留旧版 browser
dsh plugin --profile web add @anweat/dsh-browser@^0.1.8 dsh-web-search-pro@^0.1.8

# 本地 checkout 联调：两个目录一起重新挂载
dsh plugin --profile web add ../dsh-browser ../dsh-web-search-pro
```

## 📚 更多信息

**安装**

dsh plugin --profile web add @anweat/dsh-browser@^0.1.8 dsh-web-search-pro@^0.1.8

**npm 安装：显式升级两个包，避免 profile 锁文件继续保留旧版 browser**

dsh plugin --profile web add @anweat/dsh-browser@^0.1.8 dsh-web-search-pro@^0.1.8

**快速使用与适用情形**

安装并重启后，直接在 DSH 会话里要求模型调用工具即可： 请调用 web_backend_status 检查后端，然后用 web_search_pro 搜索 "DeepSeek Harness community feedback"，指定 exa、fresh=true、返回 8 条来源。 先运行 `web_backend_status` 判断后端是否 ready。指定单一引擎时失败会原样返回；不指定时才会按 `engines` 顺序自动回退。

**配置**

三层，越靠前越日常： 1. **DSH 可视化面板**：打开 `设置 → 插件 → 插件配置 → Web Search Pro`。面板按搜索策略、服务凭据、运行时后端和高级规则分组；修改先保留为本地草稿，点击“保存”后写入 `settings.yaml` 并热更新，支持放弃修改和逐字段恢复部署值。 - Exa、Jina、GitHub 密钥通过 DSH Credentials 写入，面板只显示“已配置/未配置”，不会把明文密钥读回浏览器。 - `platformRules`、`customPlatforms`、`browserBindings` 与 Playwright 设置使用 JSON 对象编辑器；格式或数值范围无效时会阻止保存。 - 浏览器工具的审批自由度由 `dsh-browser.automationMode` 管辖，调用缓冲由 `dsh-browser.usagePolicy` 

## 🔗 链接

- [GitHub 仓库](https://github.com/anweat/dsh-web-search-pro)
- [完整 README](https://github.com/anweat/dsh-web-search-pro#readme)
- [返回dsh-web-search-pro所在分类](../plugins.md)
