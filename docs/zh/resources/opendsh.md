---
title: "opendsh"
description: "在 VS Code 内打开 DSH Web UI，一键启停。"
keywords: "opendsh, ide, integration, ui, deepseek harness, dsh"
---
# opendsh

> ⭐ **0** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | IDE 与编辑器 |
| 星数 | ⭐ 0 | 状态 | ✅ 活跃 |
| 作者 | [TheChengXi](https://github.com/TheChengXi) | 更新时间 | 2026-08-20 |

## 一句话介绍

> 在 VS Code 内打开 DSH Web UI，一键启停。

## 详细介绍

**Open DSH** 是一个极简的 VS Code 扩展：编辑器标题栏（标签栏同层）的大写 D 按钮与底部状态栏的 「DSH」按钮都可一键打开 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) （`dsh`）的 Web UI——单击直接执行 `DSH: Open DSH`，在编辑器内以**单标签页**打开 （重复点击只聚焦已有标签页，不会越开越多；webview 不可用时回退系统浏览器）， 并能为当前工作区自动启动 / 停止 `dsh web` 服务。

## ✨ 核心特性

- **标题栏快捷按钮** —— 编辑器标签栏同层右上角的大写 D 按钮，单击直接执行 `DSH: Open DSH`
- **状态栏快捷按钮** —— 底部状态栏左侧的「DSH」按钮，同样单击直接执行 `DSH: Open DSH`；
- **启动自动打开（默认开启）** —— 由设置 `opendsh.autoStart`（默认 `true`）控制：VS Code 启动时
- **打开方式三选一（可选）** —— 设置 `opendsh.openWith`（默认 `"tab"`）：
- **多标签页（可选）** —— 设置 `opendsh.multipleTabs`（默认 `false`）为 `true` 时，`"tab"` 方式下每次打开都
- `DSH: Open DSH` —— 打开 Web UI：如果当前工作区的服务没在运行，会先自动启动（自动识别工作区目录、
- **单标签页复用** —— DSH 以唯一标签页展示（自定义 webview 承载），重复打开只聚焦、不新建；
- `DSH: Stop DSH` —— 停止由本扩展启动的服务。

## 🚀 快速开始

```bash
node --test
```

## 📚 更多信息

**安装**

用 `npx @vscode/vsce package` 打包出 `.vsix` 后安装；或把本目录复制到扩展目录下，命名为 `TheChengXi.opendsh-0.1.1`，然后重载窗口。

**Settings**

`.dsh/*.patch.yml` in the workspace root. survives VS Code), one of: - `integrated`: in a VS Code integrated terminal; stops when VS Code closes (default). - `window`: in a desktop console window; stops when VS Code closes. - `hidden`: silent, logs in the Output panel "DSH" channel; stops when VS Code closes. - `window-keepalive`: in a desktop console window; **keeps running** after VS Code closes

**Install**

Build a `.vsix` with `npx @vscode/vsce package`, then install it; or copy this folder into your extensions directory as `TheChengXi.opendsh-0.1.1` and reload the window.

## 🔗 链接

- [GitHub 仓库](https://github.com/TheChengXi/opendsh)
- [完整 README](https://github.com/TheChengXi/opendsh#readme)
- [返回opendsh所在分类](../integrations.md)
