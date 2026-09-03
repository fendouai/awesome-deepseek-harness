---
title: "dsh-plugin-diff-review"
description: "Diff Review Plugin for DeepSeek Harness"
keywords: "dsh-plugin-diff-review, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-diff-review

> ⭐ **7** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 7 | Status | ✅ active |
| Author | [Civitasv](https://github.com/Civitasv) | Updated | 2026-08-16 |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Diff Review Plugin for DeepSeek Harness

## About

本插件依赖 [dsh-plugin-open-editor](https://github.com/Civitasv/dsh-plugin-open-editor)，请一并安装： dsh plugin --profile web add github:Civitasv/dsh-plugin-open-editor#main dsh plugin --profile web add github:Civitasv/dsh-plugin-diff-review#v0.1.2 上面两条 `dsh plugin add` 命令负责安装包，但 DSH 只会加载在 web profile 的补丁文件中注册的插件，因此还需在 `~/.dsh/profiles/web/cordis.patch.yml` 中列出它们： - insert: - id: open-editor name: dsh-plugin-open-editor - id: diff-review name: dsh-plugin-diff-review 重启 DSH 后即可使用。更新时重新执行两条安装命令。

## ✨ Key Features

- insert:

## 📦 Install

```bash
dsh plugin --profile web add github:Civitasv/dsh-plugin-open-editor#main
dsh plugin --profile web add github:Civitasv/dsh-plugin-diff-review#v0.1.2
```

## 🚀 Quick Start

```bash
- insert:
    - id: open-editor
      name: dsh-plugin-open-editor
    - id: diff-review
      name: dsh-plugin-diff-review
```

## 📚 Learn more

**安装**

本插件依赖 [dsh-plugin-open-editor](https://github.com/Civitasv/dsh-plugin-open-editor)，请一并安装： dsh plugin --profile web add github:Civitasv/dsh-plugin-open-editor#main dsh plugin --profile web add github:Civitasv/dsh-plugin-diff-review#v0.1.2 上面两条 `dsh plugin add` 命令负责安装包，但 DSH 只会加载在 web profile 的补丁文件中注册的插件，因此还需在 `~/.dsh/profiles/web/cordis.patch.yml` 中列出它们： - id: open-editor name: dsh-plugin-open-edit

## 🔗 Links

- [GitHub Repository](https://github.com/Civitasv/dsh-plugin-diff-review)
- [Full README](https://github.com/Civitasv/dsh-plugin-diff-review#readme)
- [Back to the Plugins list](../plugins.md)
