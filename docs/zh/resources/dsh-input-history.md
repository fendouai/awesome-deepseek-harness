---
title: "dsh-input-history"
description: "终端风格输入历史：Ctrl+Up/Down 召回与切换已发送消息。"
keywords: "dsh-input-history, input-editing, plugin, ui, deepseek harness, dsh"
---
# dsh-input-history

> ⭐ **4** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 输入与编辑 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [lhh010](https://github.com/lhh010) | 更新时间 | 2026-08-21 |

## 一句话介绍

> 终端风格输入历史：Ctrl+Up/Down 召回与切换已发送消息。

## 详细介绍

DSH Web 输入历史插件：像终端一样用 **Ctrl+Up / Ctrl+Down** 召回和切换已发送的消息，零核心改动。

## ✨ 核心特性

- **Ctrl+Up**：把最近一条已发送的用户消息填入输入框；连续按向上遍历更早的消息
- **Ctrl+Down**：向下遍历回更新的消息；回到最新位置时恢复你按 Ctrl+Up 之前未发送的草稿
- 裸方向键、Enter、Ctrl+Z/Y、斜杠菜单等全部原样放行——多行输入的光标移动不受影响（对应 [dsh-external/issues#153](https://github.com/dsh-external/issues/issues/153) 的约束）
- 历史来自当前会话快照的用户消息（自动去相邻重复、跳过空白），刷新页面后仍然可用
- 输入框被手动编辑、粘贴、或发送清空草稿后，浏览状态自动复位

## 📦 安装

```bash
# 方式一：git 依赖固定 tag（公开镜像，推荐；也可用 github:lhh010/dsh-input-history）
dsh plugin --profile web add '@dsh-external/dsh-input-history@github:lhh010/dsh-input-history#v0.1.7'

# 方式二：本地 link（开发）
git clone https://github.com/lhh010/dsh-input-history.git
cd dsh-input-history && pnpm install && pnpm run build
dsh plugin --profile web add link:/path/to/dsh-input-history
```

## 🚀 快速开始

```bash
- insert:
    - id: dsh-input-history
      name: '@dsh-external/dsh-input-history'
```

## 📚 更多信息

**提示词安装（让 DSH 自己装）**

把下面这段提示词发给任意一个 DSH 会话，模型会替你完成安装： > 帮我安装 dsh-input-history 插件（DSH 输入历史召回插件（Ctrl+Up/Ctrl+Down 终端式输入历史）），步骤： > 1. 执行 `dsh plugin --profile web add '@dsh-external/dsh-input-history@github:lhh010/dsh-input-history#v0.1.7'`（首次可能被 pnpm 11 拦截 node-pty 构建脚本而失败） > 2. 在 `~/.dsh/profiles/web` 下执行 `pnpm approve-builds --all`（放行构建脚本） > 3. 再执行一次第 1 步的安装命令 > 4. 完成后提醒我硬刷新浏览器（Ctrl/Cmd+Shift+R） > 遇到报错先查 https://gith

**提示词安装（让 DSH 自己装）**

把下面这段提示词发给任意一个 DSH 会话，模型会替你完成安装： > 帮我安装 dsh-input-history 插件（DSH 输入历史召回插件（Ctrl+Up/Ctrl+Down 终端式输入历史）），步骤： > 1. 执行 `dsh plugin --profile web add '@dsh-external/dsh-input-history@github:lhh010/dsh-input-history#v0.1.7'`（首次可能被 pnpm 11 拦截 node-pty 构建脚本而失败） > 2. 在 `~/.dsh/profiles/web` 下执行 `pnpm approve-builds --all`（放行构建脚本） > 3. 再执行一次第 1 步的安装命令 > 4. 完成后提醒我硬刷新浏览器（Ctrl/Cmd+Shift+R） > 遇到报错先查 https://gith

## 🔗 链接

- [GitHub 仓库](https://github.com/lhh010/dsh-input-history)
- [完整 README](https://github.com/lhh010/dsh-input-history#readme)
- [返回dsh-input-history所在分类](../plugins.md)
