---
title: "deepseek-harness-workbench"
description: "DeepSeek Harness 官方架构的 Windows 桌面发行版 (Desktop distribution of the official DeepSeek Harness)"
keywords: "deepseek-harness-workbench, desktop, client, coding, deepseek harness, dsh"
---
# deepseek-harness-workbench

> ⭐ **3** · ✅ 活跃 · 客户端

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [xuan-ao-1](https://github.com/xuan-ao-1) | 更新时间 | 2026-08-15 |

## 一句话介绍

> DeepSeek Harness 官方架构的 Windows 桌面发行版 (Desktop distribution of the official DeepSeek Harness)

## 详细介绍

- **开箱即用**：单个安装包内置 Node.js 运行时 + 官方 `dsh`（`@deepseek-ai/dsh@0.1.0-rc.6`）+ 预生成 Profile 模板，**无需预先安装 Node/pnpm/DSH**，装完即用。 - **无边框沉浸式窗口**：Windows 完全自绘标题栏与最小化/最大化/关闭按钮（对齐 Windows 11 / TraeWork 风格），自适应浅色/深色主题。 - **官方原生 UI**：直接加载官方 `dsh-web-app` Web 界面（Phase 0 loopback），非自研聊天界面。 - **插件生态**：完整兼容官方 DeepSeek Harness 插件体系 —— 官方 DSH 插件不改版即可运行。 - **数据隔离可选**：安装版用户数据在 `~/.dsh`（与命令行 `dsh` 共享）；便携版数据在 exe 旁 `data/.dsh`（绿色携带、零残留）。 - **架构合规**：不 fork Core、不建第二套插件 API、所有能力通过官方 Profile + Bundle 组合（详见 `docs/`）。

## ✨ 核心特性

- **开箱即用**：单个安装包内置 Node.js 运行时 + 官方 `dsh`（`@deepseek-ai/dsh@0.1.0-rc.6`）+ 预生成 Profile 模板，**无需预先安装 Node/pnpm/DSH**，装完即用。
- **无边框沉浸式窗口**：Windows 完全自绘标题栏与最小化/最大化/关闭按钮（对齐 Windows 11 / TraeWork 风格），自适应浅色/深色主题。
- **官方原生 UI**：直接加载官方 `dsh-web-app` Web 界面（Phase 0 loopback），非自研聊天界面。
- **插件生态**：完整兼容官方 DeepSeek Harness 插件体系 —— 官方 DSH 插件不改版即可运行。
- **数据隔离可选**：安装版用户数据在 `~/.dsh`（与命令行 `dsh` 共享）；便携版数据在 exe 旁 `data/.dsh`（绿色携带、零残留）。
- **架构合规**：不 fork Core、不建第二套插件 API、所有能力通过官方 Profile + Bundle 组合（详见 `docs/`）。

## 📚 更多信息

**安装 Setup 版（静默安装，自动建快捷方式）**

irm https://raw.githubusercontent.com/xuan-ao-1/deepseek-harness-workbench/main/scripts/install.ps1 | iex

## 🔗 链接

- [GitHub 仓库](https://github.com/xuan-ao-1/deepseek-harness-workbench)
- [完整 README](https://github.com/xuan-ao-1/deepseek-harness-workbench#readme)
- [返回deepseek-harness-workbench所在分类](../clients.md)
