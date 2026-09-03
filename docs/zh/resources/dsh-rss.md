---
title: "dsh-rss"
description: "DeepSeek Harness RSS 订阅插件：rss_list/add/remove/fetch/check 五工具，RSS 0.9x/1.0/2.0 与 Atom 归一化解析，订阅列表持久化到 settings，proxyUrl 特殊代理支持；纯 Node 全平台。· RSS/Atom subscription tools for DeepSeek Harness agents."
keywords: "dsh-rss, search, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-rss

> ⭐ **4** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [STARDUSTLC666](https://github.com/STARDUSTLC666) | 更新时间 | 2026-08-18 |
| 子分类 | 📰 新闻与资讯 | 能力 | coding, multi-agent |

## 一句话介绍

> DeepSeek Harness RSS 订阅插件：rss_list/add/remove/fetch/check 五工具，RSS 0.9x/1.0/2.0 与 Atom 归一化解析，订阅列表持久化到 settings，proxyUrl 特殊代理支持；纯 Node 全平台。· RSS/Atom subscription tools for DeepSeek Harness agents.

## 详细介绍

DSH（DeepSeek Harness）的 RSS/Atom 订阅工具插件：管理订阅源，抓取并解析 RSS 0.9x / 1.0 / 2.0 与 Atom，支持 OPML 批量导入导出，给模型提供九个可直接调用的工具。

## 📦 安装

```bash
dsh plugin --profile web add dsh-rss
```

## 🚀 快速开始

```bash
dsh plugin --profile web remove dsh-rss
```

## 📚 更多信息

**配置**

在你自己的 profile 的 `cordis.patch.yml` 里覆盖本插件行（缺省时插件也能加载，只是全部用默认值）： name: 'dsh-rss' config: # proxyUrl: http://127.0.0.1:7890 # 部分订阅源需要特殊代理（梯子）才能访问时启用 timeoutMs: 15000 # 抓取超时（毫秒，默认 15000） # maxBodyBytes: 5242880 # 订阅源体积上限（默认 5MB，防超大响应） # userAgent: 'dsh-rss/0.2.0' # 自定义抓取 UA # feedsYaml: | # 可选：预置订阅列表（也可用 rss_add 工具添加） # - url: https://example.com/feed.xml # name: 示例订阅 # category: 技术

**示例**

rss_add { url: https://example.com/feed.xml, name: 我的订阅 } rss_fetch { name: 我的订阅, limit: 10 } rss_check { url: https://example.com/feed.xml } rss_opml_export { path: subscriptions.opml } rss_opml_import { opml: "<?xml version=\"1.0\"?>..." }

## 🔗 链接

- [GitHub 仓库](https://github.com/STARDUSTLC666/dsh-rss)
- [完整 README](https://github.com/STARDUSTLC666/dsh-rss#readme)
- [返回dsh-rss所在分类](../plugins.md)
