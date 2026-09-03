---
title: "dsh-chrome"
description: "DeepSeek Harness (dsh) browser companion: Chrome side panel embedding the full dsh web UI + host plugins for page reading, HTTP capture, and browser control."
keywords: "dsh-chrome, browser, integration, coding, ui, deepseek harness, dsh"
---
# dsh-chrome

> ⭐ **6** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 浏览器控制 |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [stuarthu](https://github.com/stuarthu) | 更新时间 | — |

## 一句话介绍

> DeepSeek Harness (dsh) browser companion: Chrome side panel embedding the full dsh web UI + host plugins for page reading, HTTP capture, and browser control.

## 详细介绍

`dsh-chrome` 是一个面向 DeepSeek Harness 的 Chrome 控制插件。它把 `chrome_repl` 工具、`control-chrome` Skill、通用审批和 `/chrome` 管理命令打包成可安装的 DSH Bundle，让 Agent 能在用户授权后复用真实 Chrome Profile 中的登录态、标签页和扩展环境。 适合这些任务：操作登录后的后台、复用当前网页、检查页面状态、点击和输入、截图、上传文件、验证 Web UI，以及读取虚拟列表或无限滚动内容。

## ✨ 核心特性

- **真实 Chrome Profile**：复用现有登录态、标签页和浏览器环境。
- **受限 JavaScript REPL**：持久保存变量，但不暴露 Node.js、文件系统、进程、网络全局或任意 `eval`。
- **观察—操作—验证**：支持 snapshot、find、inspect、click、fill、press、scroll、evaluate、screenshot、upload、console 和 network。
- **用户标签保护**：接管用户已有标签页不会移动、分组或关闭它。
- **任务级标签清理**：Agent 创建的普通研究标签页在当前 Turn 结束后自动关闭。
- **明确交付**：`markHandoff()` 和 `markDeliverable()` 可以保留需要交给用户的标签页。
- **通用审批**：默认每次 `chrome_repl` 调用进入 DSH 审批；也可以用 `/chrome authorize` 建立当前 Session 的限时授权。
- **多 Session 隔离**：同一进程内的多个 Agent 分别持有状态，共享机器级 Bridge 而不共享 REPL binding。

## 📦 安装

```bash
npx @deepseek-ai/dsh web
```

## 🚀 快速开始

```bash
pnpm install
pnpm run build
npx @deepseek-ai/dsh plugin --profile web add .
```

## 📚 更多信息

**2. 构建并安装本地插件**

在 `dsh-chrome` 目录执行： pnpm install pnpm run build npx @deepseek-ai/dsh plugin --profile web add . `dsh-chrome` 的 `package.json` 声明了 `dsh.bundle.patch`。安装成功后，它会自动加入 `web` Profile 的 Bundle 层。 然后重新启动 Web UI： npx @deepseek-ai/dsh web

**配置**

默认 Bundle 配置： name: dsh-chrome config: host: 127.0.0.1 port: 17318 可以在 Profile 的 `cordis.patch.yml` 中覆盖该行。DSH Patch 会整体替换 `config`，因此覆盖时请同时保留 `host` 和 `port`。 配套商店扩展固定访问 `127.0.0.1:17318`。除非同时维护并重新构建 Chrome 扩展，否则不要修改端口，也不要把 Bridge 绑定到非 loopback 地址。

## 🔗 链接

- [GitHub 仓库](https://github.com/stuarthu/dsh-chrome)
- [完整 README](https://github.com/stuarthu/dsh-chrome#readme)
- [返回dsh-chrome所在分类](../integrations.md)
