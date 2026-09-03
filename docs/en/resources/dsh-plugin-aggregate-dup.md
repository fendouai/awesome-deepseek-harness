---
title: "dsh-plugin"
description: "Tabbit Broser plugins for Deepseek Harness"
keywords: "dsh-plugin, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin

> ⭐ **91** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 91 | Status | ✅ active |
| Author | [Tabbit-Browser](https://github.com/Tabbit-Browser) | Updated | 2026-08-21 |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Tabbit Broser plugins for Deepseek Harness

## About

[English](README.en.md) | **简体中文** | [Changelog](CHANGELOG.md) Tabbit Browser 的 DeepSeek Harness（dsh）插件包（bundle）。dsh 可以通过此插件调用 Tabbit 完成 Agent 任务：真实页面、真实登录态、真实交互，经原生 code-first 工具驱动（不走 shell 转发）。适用于网页自动化、信息提取、QA 与评测。

## 📦 Install

```bash
dsh plugin --profile web add dsh-tabbit                 # npm 主路线
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add github:Tabbit-Browser/dsh-tabbit # npm 不可达时的回退
dsh plugin --profile web add link:/path/to/dsh-tabbit   # 本地开发
```

## 📚 Learn more

**其他安装模式**

dsh plugin --profile web add github:Tabbit-Browser/dsh-tabbit # npm 不可达时的回退 dsh plugin --profile web add link:/path/to/dsh-tabbit # 本地开发 > 本包取代早期的 `tabbit-browser` skill-only 插件；npm 上的 0.2.x 版本也由本版本接续——0.2.x 用户经每日更新检查会收到升级提示，重跑安装命令即可原地升级。

**基本配置**

dsh Settings → tabbit，或 `$DSH_HOME/settings.yaml` tabbit: instance: "" # 显式指定 16 位大写 hex 实例 id（/tabbit-info 可列出）；通常留空即可 launcherPath: "" # 默认自动发现：优先 ~/.local/bin/tabbit-cli，回退 tabbit-playwright；Windows 为 %LOCALAPPDATA%\Tabbit\LocalAgent\bin\tabbit-cli.exe pageAccess: ask # ask（每会话询问一次）| always | never intranetFetch: ask # web_fetch 访问内网/回环目标：ask（每会话每 origin 询问一次）| always | never

## 🔗 Links

- [GitHub Repository](https://github.com/Tabbit-Browser/dsh-plugin)
- [Full README](https://github.com/Tabbit-Browser/dsh-plugin#readme)
- [Back to the Plugins list](../plugins.md)
