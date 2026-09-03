---
title: "dsh-prompt-studio"
description: "Edit user and built-in system-prompt sections with live preview."
keywords: "dsh-prompt-studio, developer, plugin, ui, context, deepseek harness, dsh"
---
# dsh-prompt-studio

> ⭐ **3** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [Moeblack](https://github.com/Moeblack) | Updated | 2026-08-13 |
| Subcategory | 🧪 Code, tests & review | Capabilities | ui, context |

## One-liner

> Edit user and built-in system-prompt sections with live preview.

## About

Prompt Studio 的 DeepSeek Harness 插件分发形态。插件在对话页注册 **Prompt Studio** 标签页，以同一组件列表展示运行时原生提示词和用户补充，并提供编辑、原生覆盖与完整请求预览。

## ✨ Key Features

- `kind` 只区分来源：`native` 是 Host 在运行时发现的只读组件；`supplement` 是用户可编排并持久化的补充组件。
- `role` 决定内容归宿：
- `position` 只描述 user/assistant 消息所处的间隙：
- `order` 有两种与归宿对应的含义：
- `origin` 只用于覆盖。补充组件未设置 `origin` 时是普通注入；设置为某个原生组件 id 时，同一个补充组件即覆盖该原生组件，不存在单独的覆盖 kind。

## 📦 Install

```bash
# 先完成构建（见下），再安装到 profile（profile 名可自取，例如 web）
dsh plugin --profile web add /path/to/dsh-prompt-studio
dsh --profile web --dump-config   # 应能看到 "# == dsh-prompt-studio" 层
dsh web                           # 或 dsh --profile web
```

## 🚀 Quick Start

```bash
DSH_ROOT=/path/to/dsh node scripts/build.mjs
```

## 📚 Learn more

**使用**

1. 打开任意对话，选择 **Prompt Studio** 标签页。 2. 选择 **新增补充**，分别编辑标识、角色、顺序、可选覆盖目标与模板；只有 user/assistant 角色显示消息间隙选择器。 3. 如需覆盖原生组件，也可在对应原生行选择 **创建覆盖**；生成的仍是 `kind=supplement` 组件，只是带有 `origin`。 4. 在 **完整预览** 中检查合并后的完整 system 内容及各消息间隙的补充内容。模型内容预览不插入 `[位置 · role · id]` 一类展示标签，补充内容以纯文本直接注入。 5. 选择 **保存更改**。设置保存后立即撤销旧组合并施加新组合。

**安装与启用**

Prompt Studio 以**组合包（bundle）**分发：`package.json` 的 `dsh.bundle.patch` 指向 `cordis.patch.yml`，`dsh.client` 声明浏览器端注入面。安装进一个 profile：

**先完成构建（见下），再安装到 profile（profile 名可自取，例如 web）**

dsh plugin --profile web add /path/to/dsh-prompt-studio dsh --profile web --dump-config # 应能看到 "# == dsh-prompt-studio" 层 dsh web # 或 dsh --profile web `dsh plugin --profile <name> add <path>` 会把包链接进 profile 并把包名追加进 `dsh.profile.bundles`。已安装的 bundle 通过 `dsh plugin --profile <name> remove dsh-prompt-studio` 移除。命令行与已经运行的 Web 进程不共享内存，因此替换插件产物后需重启 `dsh web` 并刷新浏览器。

## 🔗 Links

- [GitHub Repository](https://github.com/Moeblack/dsh-prompt-studio)
- [Full README](https://github.com/Moeblack/dsh-prompt-studio#readme)
- [Back to the Plugins list](../plugins.md)
