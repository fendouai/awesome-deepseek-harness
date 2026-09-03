---
title: "dsh-share"
description: "One-click conversation sharing for DSH."
keywords: "dsh-share, ui, plugin, deepseek harness, dsh"
---
# dsh-share

> ⭐ **29** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 29 | Status | ✅ active |
| Author | [hellodigua](https://github.com/hellodigua) | Updated | 2026-08-19 |

## One-liner

> One-click conversation sharing for DSH.

## About

DSH 对话分享插件，分享单轮或多轮对话，可导出为图片或 Markdown。 和 DeepSeek 网页端一致的多选交互，操作体验完全一致。 生成图片前可调整宽度、字号和过程显示，完成后可下载或复制图片。

## ✨ Key Features

- 从右上角进入问答选择模式，默认全选
- 每轮的分享按钮也会进入选择模式，并只预选当前问答
- 问题和回答两侧都有联动勾选框，也可直接点击内容整组选择，支持不连续选择
- 勾选框会在长内容滚动时吸附在页面上，到当前问题或回答末尾再移出
- 可复制图片、下载 PNG 或 Markdown
- 保留 Markdown、代码块、表格、图片和工具调用摘要
- 可调整图片宽度和字号，长图支持滚动预览
- 可勾选“不展示过程”，只保留提问和最终回答

## 📦 Install

```bash
dsh plugin --profile web add dsh-share
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add github:hellodigua/dsh-share#vX.Y.Z
```

## 📚 Learn more

**快速安装**

使用 DSH CLI 把插件加入 Web Profile，然后重启 `dsh web`： dsh plugin --profile web add dsh-share

**其他安装方式**

安装指定的 GitHub 版本： dsh plugin --profile web add github:hellodigua/dsh-share#vX.Y.Z 安装本地源码： dsh plugin --profile web add /absolute/path/to/dsh-share 修改源码后，先运行 `corepack pnpm build`，再使用 `dsh plugin --profile web add --force /absolute/path/to/dsh-share` 刷新插件。

## 🔗 Links

- [GitHub Repository](https://github.com/hellodigua/dsh-share)
- [Full README](https://github.com/hellodigua/dsh-share#readme)
- [Back to the Plugins list](../plugins.md)
