---
title: "dsh-sticky-disclosure"
description: "DSH Web client plugin: collapse every expanded section (Think / tool cards) in the conversation in one click, with a customizable hotkey."
keywords: "dsh-sticky-disclosure, search, plugin, coding, deepseek harness, dsh"
---
# dsh-sticky-disclosure

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [Han-1413141](https://github.com/Han-1413141) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding |

## 一句话介绍

> DSH Web client plugin: collapse every expanded section (Think / tool cards) in the conversation in one click, with a customizable hotkey.

## 详细介绍

[English](README.en.md) | 中文 DSH Web 客户端插件：**一键收起会话里所有展开的可折叠区块**（Think 思考行、工具卡片、命令卡片、上下文注入行等），带实时计数的常驻按钮 + **可自定义的快捷键**。展开的区块滑出屏幕时，标题会自动钉在会话顶部，随时可以点一下收起。

## 📦 安装

```bash
dsh plugin --profile web add github:Han-1413141/dsh-sticky-disclosure
```

## 🚀 快速开始

```bash
dsh plugin --profile web add https://github.com/Han-1413141/dsh-sticky-disclosure/archive/refs/heads/main.tar.gz
```

## 📚 更多信息

**安装**

> 需求：Node.js ≥ 20 + DeepSeek Harness（带 `dsh plugin` 命令的版本，`npm install -g @deepseek-ai/dsh`）。插件随 `dsh web` 启动。

**方式〇：一键安装（推荐，无需克隆仓库）**

**PowerShell 一键脚本**（复制整行粘贴回车；自动补齐 pnpm、自动探测 git）： irm https://raw.githubusercontent.com/Han-1413141/dsh-sticky-disclosure/main/install.ps1 | iex **或直接命令行**（机器上需已有 pnpm 与 git）： dsh plugin --profile web add github:Han-1413141/dsh-sticky-disclosure 没有 git 时可用 GitHub 打包直链（更新时先 remove 再 add）： dsh plugin --profile web add https://github.com/Han-1413141/dsh-sticky-disclosure/archive/refs/heads/main.tar.g

**方式二：手工安装（机器上没有 pnpm）**

1. 在 `<DSH_HOME>\profiles\web\package.json`（默认 `%USERPROFILE%\.dsh\profiles\web\package.json`）中： - `dependencies` 增加 `"dsh-sticky-disclosure": "link:<本仓库的绝对路径>"` - `dsh.profile.bundles` 末尾追加 `"dsh-sticky-disclosure"` 2. 在 profile 的 node_modules 里建目录联接（与 pnpm `link:` 依赖留下的链接一致）： ```powershell New-Item -ItemType Junction ` -Path "$env:USERPROFILE\.dsh\profiles\web\node_modules\dsh-sticky-disclosure"

**首次安装后：停掉当前 dsh web 再启动**

dsh web 验证是否进入插件图（应看到 `id: sticky-disclosure` 与 `name: dsh-sticky-disclosure`）： dsh --profile web --dump-config | findstr sticky-disclosure 页面加载后，聊天区右下角出现「全部收起」药丸按钮即表示插件已激活。

## 🔗 链接

- [GitHub 仓库](https://github.com/Han-1413141/dsh-sticky-disclosure)
- [完整 README](https://github.com/Han-1413141/dsh-sticky-disclosure#readme)
- [返回dsh-sticky-disclosure所在分类](../plugins.md)
