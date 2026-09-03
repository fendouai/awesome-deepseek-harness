---
title: "dsh-side-panel"
description: "紧凑侧边栏：文件浏览器、终端与 Git 审查。"
keywords: "dsh-side-panel, ui, plugin, files, terminal, git, deepseek harness, dsh"
---
# dsh-side-panel

> ⭐ **16** · 💤 停更 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 16 | 状态 | 💤 停更 |
| 作者 | [ccq1](https://github.com/ccq1) | 更新时间 | 2026-08-14 |
| 子分类 | 🖥️ 侧边栏与面板 | 能力 | ui, files, terminal, git |

## 一句话介绍

> 紧凑侧边栏：文件浏览器、终端与 Git 审查。

## 详细介绍

DSH Web 的右侧工作区面板，在当前会话旁集中提供 Git 审查、终端和文件操作。 可以点击dsh会话区弹出的文件链接，会自动打开相应的文件以供审阅。

## 📦 安装

```bash
dsh plugin --profile web add github:dsh-external/dsh-side-panel
dsh web
```

## 🚀 快速开始

```bash
git clone git@github.com:dsh-external/dsh-side-panel.git
cd dsh-side-panel
npm install
npm run build
dsh plugin --profile web add .
```

## 📚 更多信息

**安装**

从 github-dsh-external仓库安装 dsh plugin --profile web add github:dsh-external/dsh-side-panel dsh web 或者可以先从git clone 到本地，然后从本地目录安装 git clone git@github.com:dsh-external/dsh-side-panel.git cd dsh-side-panel npm install npm run build dsh plugin --profile web add .

**配置**

组合包默认启用以下配置： - id: side-panel name: '@dsh-external/dsh-side-panel' config: maxTextBytes: 2097152 maxImageBytes: 10485760 searchMaxResults: 200

## 🔗 链接

- [GitHub 仓库](https://github.com/ccq1/dsh-side-panel)
- [完整 README](https://github.com/ccq1/dsh-side-panel#readme)
- [返回dsh-side-panel所在分类](../plugins.md)
