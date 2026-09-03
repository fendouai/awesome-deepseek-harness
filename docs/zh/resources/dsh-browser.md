---
title: "dsh-browser"
description: "Self-contained browser runtime plugin for DeepSeek Harness — bundles Playwright (chromium) and OpenCLI as plugin-local dependencies, exposes a browser service and interactive browser tools."
keywords: "dsh-browser, browser, plugin, coding, deepseek harness, dsh"
---
# dsh-browser

> ⭐ **7** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 浏览器控制 |
| 星数 | ⭐ 7 | 状态 | ✅ 活跃 |
| 作者 | [anweat](https://github.com/anweat) | 更新时间 | 2026-08-14 |

## 一句话介绍

> Self-contained browser runtime plugin for DeepSeek Harness — bundles Playwright (chromium) and OpenCLI as plugin-local dependencies, exposes a browser service and interactive browser tools.

## 详细介绍

自包含的浏览器运行时插件 for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（DSH）。 把 **Playwright / Patchright（可选 Chromium 驱动）** 与 **OpenCLI** 作为插件自身的 npm 依赖打包（优先插件本地，缺省回退全局复用），对外提供一个 `browser` 服务 + 一组交互式浏览器工具。`dsh-web-search-pro` 通过 `inject: ['browser']` 注入该服务，驱动它的浏览器 / OpenCLI 后端——**不再依赖全局 CLI**。

## 📦 安装

```bash
dsh plugin --profile web add @anweat/dsh-browser
# 或本地目录 / tarball：
dsh plugin --profile web add ./dsh-browser
# 重启（web profile 关闭了 HMR）：
dsh --profile web
```

## 🚀 快速开始

```bash
dsh plugin --profile web add @anweat/dsh-browser@^0.1.10 dsh-web-search-pro@^0.1.11
```

## 📚 更多信息

**快速使用与适用情形**

安装并重启后，可先让模型调用 `browser_status`，再按任务选择工具。默认 `automationMode: standard`：读取直接执行，点击、输入、滚动及页面写操作走 DSH 原生一次性审批。 DSH 会话示例： 先调用 browser_status；然后用 browser_open 打开目标页。 若页面需要登录，使用 authProfile=forum；不要把 Cookie 放进工具参数。

**配置（cordis.yml / patch config）**

- id: browser name: '@anweat/dsh-browser' config: automationMode: standard # read-only | standard | autonomous | unrestricted browserRuntime: playwright # playwright | patchright channel: chromium # 'chromium'（打包内核）| 'msedge'（系统 Edge） headless: true opencliEnabled: true usagePolicy: # 所有模式都生效；无审批模式也不会绕过 minDelayMs: 750 maxConcurrency: 2 burst: 3 maxPagesPerRun: 20 maxDepth: 2 retryLimit: 2 backoff

## 🔗 链接

- [GitHub 仓库](https://github.com/anweat/dsh-browser)
- [完整 README](https://github.com/anweat/dsh-browser#readme)
- [返回dsh-browser所在分类](../plugins.md)
