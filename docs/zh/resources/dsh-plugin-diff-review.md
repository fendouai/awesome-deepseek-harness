---
title: "dsh-plugin-diff-review"
description: "Diff Review Plugin for DeepSeek Harness"
keywords: "dsh-plugin-diff-review, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-diff-review

> ⭐ **7** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 7 | 状态 | ✅ 活跃 |
| 作者 | [Civitasv](https://github.com/Civitasv) | 更新时间 | 2026-08-16 |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Diff Review Plugin for DeepSeek Harness

## 详细介绍

本插件依赖 [dsh-plugin-open-editor](https://github.com/Civitasv/dsh-plugin-open-editor)，请一并安装： dsh plugin --profile web add github:Civitasv/dsh-plugin-open-editor#main dsh plugin --profile web add github:Civitasv/dsh-plugin-diff-review#v0.1.2 上面两条 `dsh plugin add` 命令负责安装包，但 DSH 只会加载在 web profile 的补丁文件中注册的插件，因此还需在 `~/.dsh/profiles/web/cordis.patch.yml` 中列出它们： - insert: - id: open-editor name: dsh-plugin-open-editor - id: diff-review name: dsh-plugin-diff-review 重启 DSH 后即可使用。更新时重新执行两条安装命令。

## ✨ 核心特性

- insert:

## 📦 安装

```bash
dsh plugin --profile web add github:Civitasv/dsh-plugin-open-editor#main
dsh plugin --profile web add github:Civitasv/dsh-plugin-diff-review#v0.1.2
```

## 🚀 快速开始

```bash
- insert:
    - id: open-editor
      name: dsh-plugin-open-editor
    - id: diff-review
      name: dsh-plugin-diff-review
```

## 📚 更多信息

**安装**

本插件依赖 [dsh-plugin-open-editor](https://github.com/Civitasv/dsh-plugin-open-editor)，请一并安装： dsh plugin --profile web add github:Civitasv/dsh-plugin-open-editor#main dsh plugin --profile web add github:Civitasv/dsh-plugin-diff-review#v0.1.2 上面两条 `dsh plugin add` 命令负责安装包，但 DSH 只会加载在 web profile 的补丁文件中注册的插件，因此还需在 `~/.dsh/profiles/web/cordis.patch.yml` 中列出它们： - id: open-editor name: dsh-plugin-open-edit

## 🔗 链接

- [GitHub 仓库](https://github.com/Civitasv/dsh-plugin-diff-review)
- [完整 README](https://github.com/Civitasv/dsh-plugin-diff-review#readme)
- [返回dsh-plugin-diff-review所在分类](../plugins.md)
