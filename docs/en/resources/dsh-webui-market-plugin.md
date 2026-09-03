---
title: "dsh-webui-market-plugin"
description: "Community plugin market in the Web GUI: browse the awesome-dsh-plugin.com catalog and install/uninstall to a profile."
keywords: "dsh-webui-market-plugin, discovery, plugin, ui, workflow, deepseek harness, dsh"
---
# dsh-webui-market-plugin

> ⭐ **96** · ✅ active · plugin · ⬆️ +3 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Plugin discovery |
| Stars | ⭐ 96 | Status | ✅ active |
| Author | [Sanqi-normal](https://github.com/Sanqi-normal) | Updated | 2026-08-18 |

## One-liner

> Community plugin market in the Web GUI: browse the awesome-dsh-plugin.com catalog and install/uninstall to a profile.

## About

在 dsh web GUI 内部的社区插件市场：浏览 [awesome-dsh-plugin.com](https://awesome-dsh-plugin.com/) 的插件目录，直接在 **设置 → 插件 → 插件市场** 里安装 / 卸载插件到 profile。界面风格与 harness 前端一致（跟随系统深浅色主题），支持中英文（按系统语言自动切换）。 推荐 awesome-dsh-plugin.com 网站的实现 [dsh-market](https://github.com/dsh-market/dsh-market)。

## 📦 Install

```bash
dsh plugin --profile web add @sanqi-normal/dsh-webui-market-plugin
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add github:Sanqi-normal/dsh-webui-market-plugin
```

## 📚 Learn more

**安装**

方式一：从 **npm registry** 安装（推荐，无 git 克隆 / prepare 脚本步骤）： dsh plugin --profile web add @sanqi-normal/dsh-webui-market-plugin 方式二：从 GitHub 源码安装： dsh plugin --profile web add github:Sanqi-normal/dsh-webui-market-plugin 安装后**重启 web 服务**生效： pnpm dsh web GitHub 源安装会执行包内 prepare 脚本，如被 pnpm 拦截，把提示的包名加入 profile 的 `pnpm-workspace.yaml` 的 `allowBuilds` 后重试。 pnpm 11 起，依赖树中"构建脚本未在 `allowBuilds` 中显式放行或拒绝"的包会直接导致 

**宿主依赖说明**

本插件是 DSH web profile 内运行的插件，不是独立 npm 应用。以下 peer 依赖由 DSH 宿主环境提供，用户无需手动安装： 当前版本面向 DSH `0.0.1-rc.2+`（不含已知解析问题的 `0.0.1-rc.1`）及 `0.1.0-rc.2+` 环境。若使用纯 npm registry 工具解析本包，可能因为 DSH 上游部分 host 包未发布而提示依赖图不完整，这属于 DSH 宿主依赖的发布问题。

**使用**

打开 **设置（Settings）→ 插件（Plugins）→ 插件市场（Plugin Market）**： - **默认「有什么装什么」**：`安装设置` 里的「自动同步到其它 profile」**默认开启**——安装插件时自动装到本机所有已初始化的 profile（有 web 装 web，有 desktop 也装 desktop；在确认框直接选了 desktop 的也会自动补装到 web）；关闭后仅装到安装时选择的 profile - **安装确认框可选目标 profile**（默认 web）；**跨 Profile 同步** 区把 web 里已装的插件一键补装到目标 profile（只新增缺失项） - 同步是**本地复制**：源已在源 profile 安装过（syncFrom 校验），所以不再受目录白名单限制——装在 web 但不在精选目录的插件（如 aegis）也能同步；每个补装任

**工作原理**

持久化 bundle（`package.json` 的 `dsh.bundle.patch` → `cordis.patch.yml`），由 `dsh plugin add` 的 reconcile 自动加入 profile 的 `dsh.profile.bundles` 层：

## 🔗 Links

- [GitHub Repository](https://github.com/Sanqi-normal/dsh-webui-market-plugin)
- [Full README](https://github.com/Sanqi-normal/dsh-webui-market-plugin#readme)
- [Back to the Plugins list](../plugins.md)
