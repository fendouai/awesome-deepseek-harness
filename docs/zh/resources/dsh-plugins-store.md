---
title: "dsh-plugins-store"
description: "自动收录与分类 GitHub dsh-plugin Topic 项目的静态目录网站。"
keywords: "dsh-plugins-store, discovery, plugin, search, ui, deepseek harness, dsh"
---
# dsh-plugins-store

> ⭐ **62** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 插件发现 |
| 星数 | ⭐ 62 | 状态 | ✅ 活跃 |
| 作者 | [ZASENJC](https://github.com/ZASENJC) | 更新时间 | 2026-08-21 |

## 一句话介绍

> 自动收录与分类 GitHub dsh-plugin Topic 项目的静态目录网站。

## 详细介绍

- 自动收录同时带有 `dsh-plugin` 与 `deepseek-harness` Topic 的公开仓库，并排除归档仓库、Fork 和宿主应用 - 提供独立的 [目录](https://dshmk.com/)、[已验证](https://dshmk.com/verified)和 [排行榜](https://dshmk.com/ranking)页面，支持搜索、分类、筛选和排序 - 排行榜支持 24 小时 Star 增速、最多 Star、最新发布和最近更新；项目详情展示分类依据、同标签项目和验证进度 - 每 30 分钟自动同步 GitHub 仓库数据 - 配套 DSH Web 插件支持通过 `/store`、设置页和 Agent 会话浏览市场，并在用户明确请求和确认后安装、更新或移除 Web profile 插件

## ✨ 核心特性

- 自动收录同时带有 `dsh-plugin` 与 `deepseek-harness` Topic 的公开仓库，并排除归档仓库、Fork 和宿主应用
- 提供独立的 [目录](https://dshmk.com/)、[已验证](https://dshmk.com/verified)和 [排行榜](https://dshmk.com/ranking)页面，支持搜索、分类、筛选和排序
- 排行榜支持 24 小时 Star 增速、最多 Star、最新发布和最近更新；项目详情展示分类依据、同标签项目和验证进度
- 每 30 分钟自动同步 GitHub 仓库数据
- 配套 DSH Web 插件支持通过 `/store`、设置页和 Agent 会话浏览市场，并在用户明确请求和确认后安装、更新或移除 Web profile 插件

## 📦 安装

```bash
dsh plugin --profile web add npm:dsh-plugins-store
```

## 🚀 快速开始

```bash
GET https://api.dshmk.com/
```

## 📚 更多信息

**安装 DSH Web 插件**

以下命令安装市场自身的 DSH Web 插件： dsh plugin --profile web add npm:dsh-plugins-store 安装完成后重启 DSH Web 并刷新浏览器。源码安装、本地构建、卸载、市场工具及 `search-dsh-store` skill 的完整说明见 [`packages/dsh-plugins-store/README.md`](packages/dsh-plugins-store/README.md)。

**使用示例**

使用 `curl` 获取目录并读取基础信息： curl --fail --silent --show-error \ --header 'Accept: application/json' \ https://api.dshmk.com/ \ | jq '{schemaVersion, generatedAt, stats}' 在 Node.js 22+ 中筛选当前已验证的插件： const response = await fetch('https://api.dshmk.com/', { headers: { Accept: 'application/json' }, }) if (!response.ok) { throw new Error(`目录请求失败：HTTP ${response.status}`) } const catalog = await response.json

## 🔗 链接

- [GitHub 仓库](https://github.com/ZASENJC/dsh-plugins-store)
- [完整 README](https://github.com/ZASENJC/dsh-plugins-store#readme)
- [返回dsh-plugins-store所在分类](../plugins.md)
