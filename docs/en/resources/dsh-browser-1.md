---
title: "dsh-browser"
description: "Shared real browser plugin for DeepSeek Harness"
keywords: "dsh-browser, browser, integration, coding, deepseek harness, dsh"
---
# dsh-browser

> ⭐ **37** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | Browser control |
| Stars | ⭐ 37 | Status | ✅ active |
| Author | [wqty123](https://github.com/wqty123) | Updated | — |

## One-liner

> Shared real browser plugin for DeepSeek Harness

## About

`dsh-builtin-browser` 给 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 提供浏览器能力: - **真实视图,而非转播**:浏览器是原生 `WebContentsView`,用户直接看到 agent 在做什么,随时可以上手接管; - **装好即用**:有桌面外壳时嵌入外壳视图;纯 `dsh web` 也能**自托管**——插件自己拉起一个 Electron 窗口,不需要任何额外配置; - **一插件即一套工具**:安装后 agent 自动获得 33 个 `browser_*` 工具(打开、查看、无障碍树、等待、语义/坐标操作、滚动、回退、批量/单控件填表、按键、结构化提取、截图、下载、登录态管理……)。 一句话:**安装插件 = 获得一个与用户共享、可被 agent 驱动的真实浏览器。**

## ✨ Key Features

- **真实视图,而非转播**:浏览器是原生 `WebContentsView`,用户直接看到 agent 在做什么,随时可以上手接管;
- **装好即用**:有桌面外壳时嵌入外壳视图;纯 `dsh web` 也能**自托管**——插件自己拉起一个 Electron 窗口,不需要任何额外配置;
- **一插件即一套工具**:安装后 agent 自动获得 33 个 `browser_*` 工具(打开、查看、无障碍树、等待、语义/坐标操作、滚动、回退、批量/单控件填表、按键、结构化提取、截图、下载、登录态管理……)。

## 📦 Install

```bash
# 方式一:从 npm 安装(已发布)
dsh plugin --profile web add dsh-builtin-browser

# 方式二:从源码目录安装(独立仓库,一插件一仓库)
dsh plugin --profile web add <本仓库路径>
```

## 🚀 Quick Start

```bash
agent (browser_* 工具)
  → ctx.browser (seam, dsh-builtin-browser/browser)
  → dsh-builtin-browser/browser-electron (provider)
  → ElectronBrowserViewHost (由宿主外壳提供)
  → WebContentsView + webContents.debugger (CDP)
```

## 📚 Learn more

**方式二:从源码目录安装(独立仓库,一插件一仓库)**

dsh plugin --profile web add <本仓库路径> 安装后,agent 即可使用浏览器工具,例如: 完整清单见[工具参考](#工具参考)。

**工作原理**

agent (browser_* 工具) → ctx.browser (seam, dsh-builtin-browser/browser) → dsh-builtin-browser/browser-electron (provider) → ElectronBrowserViewHost (由宿主外壳提供) → WebContentsView + webContents.debugger (CDP) **自托管模式**:没有桌面外壳时,插件自己拉起一个 Electron 子进程(`host-main.js`),通过本机 TCP JSON-RPC 驱动。RPC 带随机 token 认证,token 经 **stdin + 环境变量双通道**传递——Windows 上 Electron 是 GUI 子系统进程、收不到 piped stdin,环境变量兜底保证握手稳定。子进程崩溃会自动重启;

## 🔗 Links

- [GitHub Repository](https://github.com/wqty123/dsh-browser)
- [Full README](https://github.com/wqty123/dsh-browser#readme)
- [Back to the MCP & Integrations list](../integrations.md)
