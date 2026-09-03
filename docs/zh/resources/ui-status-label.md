---
title: "ui-status-label"
description: "把鲸鱼娘思考时的 deep diving 状态自定义成任意文字。"
keywords: "ui-status-label, ui, plugin, deepseek harness, dsh"
---
# ui-status-label

> ⭐ **39** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 39 | 状态 | ✅ 活跃 |
| 作者 | [alingalingling](https://github.com/alingalingling) | 更新时间 | 2026-08-15 |
| 子分类 | 🐋 桌面宠物 | 能力 | ui |

## 一句话介绍

> 把鲸鱼娘思考时的 deep diving 状态自定义成任意文字。

## 详细介绍

把你的鲸鱼娘思考时的 deep diving 自定义成任意你想要的样子。 为 **dsh Web** 聊天视图提供可配置的运行中轮次状态文案：General 设置区的一行文本输入，插件把聊天视图运行状态栏的文案替换为你输入的文字（支持 DOM 注入和上游 `conversationStatus` 服务两条路径，见[兼容性](#兼容性)）。插件注册持久的 `ui-status-label` settings 命名空间（默认 `小难梁在0721`）；在设置行输入新文字后，聊天视图在轮次运行期间（等待首 token、工具执行、流式输出）显示的状态文案随之更新。选择持久化在 `$DSH_HOME/settings.yaml`，跟随同一个用户 home 跨越 Web 端口。

## ✨ 核心特性

- **dsh Web**（`dsh --profile web` 或自定义 Web 组合）。本插件只面向浏览器交互面；headless/TUI profile 装它没有意义。
- 依赖分两类：`@deepseek-ai/cordis`、`dsh-client-*` 等为 **peer 依赖**（由 dsh 安装提供）；`@deepseek-ai/dsh-settings`、`schemastery` 为**直接依赖**（从 npm 安装）。仓库内的 `pnpm-workspace.yaml` 已

## 📦 安装

```bash
# ① tarball（需要先在仓库根执行 pnpm pack 生成 dsh-ui-status-label-0.1.0.tgz）
dsh plugin --profile web add ./dsh-ui-status-label-0.1.0.tgz

# ② git 仓库直装
dsh plugin --profile web add github:alingalingling/ui-status-label

# ③ npm（当前 npm 上尚未发布，发布后可用）
dsh plugin --profile web add dsh-ui-status-label
```

## 🚀 快速开始

```bash
allowBuilds:
  dsh-ui-status-label: true
```

## 📚 更多信息

**安装**

本包声明了 `dsh.bundle`，`dsh plugin add` 会自动激活它的 `cordis.patch.yml` 层（把 `dsh-ui-status-label` 行插入 Web roster）。

## 🔗 链接

- [GitHub 仓库](https://github.com/alingalingling/ui-status-label)
- [完整 README](https://github.com/alingalingling/ui-status-label#readme)
- [返回ui-status-label所在分类](../plugins.md)
