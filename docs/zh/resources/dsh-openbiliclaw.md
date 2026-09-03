---
title: "dsh-openbiliclaw"
description: "OpenBiliClaw 是本地运行的跨平台个性化内容推荐 Agent，持续理解你的兴趣并主动找内容。本仓库是它的 DeepSeek Harness 插件：DSH 界面常驻第四栏（推荐/内容库/对话/画像/设置），注册 22 个 Agent Bridge 工具，让 Agent 也能读推荐、答探测、闭环学习。"
keywords: "dsh-openbiliclaw, research, agent, coding, multi-agent, deepseek harness, dsh"
---
# dsh-openbiliclaw

> ⭐ **48** · ✅ 活跃 · 智能体 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 智能体 | 分类 | 研究 |
| 星数 | ⭐ 48 | 状态 | ✅ 活跃 |
| 作者 | [whiteguo233](https://github.com/whiteguo233) | 更新时间 | 2026-08-17 |

## 一句话介绍

> OpenBiliClaw 是本地运行的跨平台个性化内容推荐 Agent，持续理解你的兴趣并主动找内容。本仓库是它的 DeepSeek Harness 插件：DSH 界面常驻第四栏（推荐/内容库/对话/画像/设置），注册 22 个 Agent Bridge 工具，让 Agent 也能读推荐、答探测、闭环学习。

## 详细介绍

**OpenBiliClaw 是本地运行、跨平台、可调教的个性化内容推荐 Agent；本仓库是它的 DeepSeek Harness 客户端插件——DSH 左侧栏一个 OpenBiliClaw 按钮，点开右侧滑出抽屉（推荐/内容库/对话/画像/设置），并注册 22 个 Agent Bridge 工具，让 Agent 读推荐、答探测、闭环学习。** [English](#english) | 中文 ---

## ✨ 核心特性

- **人用侧**：在 DSH 左侧栏底部加一个 OpenBiliClaw 按钮，点开从右侧滑出一个与浏览器插件 / 手机版视觉一致的抽屉面板——推荐流、惊喜推荐、内容库、苏格拉底式对话、用户画像、后端设置，全部在 DSH 里点开即用；
- **Agent 用侧**：注册 22 个 `openbiliclaw_*` 工具（Agent Bridge v2 CLI）和 `openbiliclaw-adapter` skill，让 DSH 里的 Agent 能读取推荐、回答探测、保存内容、和用户对话，形成「推荐 → 反馈 → 画像 → 更准的推荐」的闭环。

## 📦 安装

```bash
npm install @openbiliclaw/dsh-plugin
# 或 pnpm add @openbiliclaw/dsh-plugin
```

## 🚀 快速开始

```bash
cp -r <本仓库> ~/.dsh/profiles/<profile>/node_modules/@openbiliclaw/dsh-plugin
```

## 📚 更多信息

**通过 DSH 插件 bundle 安装**

本仓库声明了 `dsh.bundle`，因此可以作为完整插件包交给 `dsh plugin add` 或插件市场安装。bundle 会自动提供 `openbiliclaw` 配置行；安装后仍需按下面的配置说明，把 `workdir` 指向本地 OpenBiliClaw 主项目目录。

**1. 界面槽位（当前 DSH 免配置）**

面板渲染在两个**加法槽位**上，无需改 DSH 源码： 两个槽位都是官方 DSH 自带的 `list` 槽（当前官方 DSH 已移除旧的 `aside` 列），此步直接跳过。

**2. 安装插件包**

把本仓库放进 web profile 的依赖目录并声明插件行： cp -r <本仓库> ~/.dsh/profiles/<profile>/node_modules/@openbiliclaw/dsh-plugin 在 `~/.dsh/profiles/<profile>/cordis.patch.yml` 增加：

**DSH 0.1.1-rc.2+: 新增配置行必须放在 insert 下**

- id: openbiliclaw name: '@openbiliclaw/dsh-plugin' config: workdir: '/你的/OpenBiliClaw/项目目录' # 后端项目根目录（含 .venv 与 skills/） `cordis.patch.yml` 的顶层是 patch 列表；不带 `insert` 的 `id` 条目会被当作已有配置行覆盖，找不到 `openbiliclaw` 时会被跳过。

## 🔗 链接

- [GitHub 仓库](https://github.com/whiteguo233/dsh-openbiliclaw)
- [完整 README](https://github.com/whiteguo233/dsh-openbiliclaw#readme)
- [返回dsh-openbiliclaw所在分类](../agents.md)
