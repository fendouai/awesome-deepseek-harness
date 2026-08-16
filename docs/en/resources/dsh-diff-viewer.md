---
title: "dsh-diff-viewer"
description: "PiUI-style Web diff viewer replacing the default diff view."
keywords: "dsh-diff-viewer, ui, plugin, git, deepseek harness, dsh"
---
# dsh-diff-viewer

> ⭐ 12 · ✅ active · plugin

## One-liner

PiUI-style Web diff viewer replacing the default diff view.

## About

DSH Web GUI 的 PiUI 风格 diff 查看器插件：替换 write/edit 工具调用的 diff 渲染（原 DiffBlock）。 - **unified 单栏默认**：同一 gutter 并排显示旧/新行号，无左右错位；split 双栏可选（`viewMode`） - **变更条**：新增实心绿条、删除条纹红条；行背景色带统一延伸到最宽行 - **词级高亮**：行内改动叠加绿/红标记，shiki 语法着色（`highlightLines`） - **上下文折叠**：长段未变更行折叠为"`N 行未变更`"，向上/向下/全部展开 - **窗口化渲染**：固定行高窗口化，大 diff 不挂载全部行；sticky 横向滚动条（hover 显现） - **复制 + `└ +A -R · N file(s)` 页脚**

## Author
**[lehhair](https://github.com/lehhair)**

## Links

- [GitHub Repository](https://github.com/lehhair/dsh-diff-viewer)
- [Full README](https://github.com/lehhair/dsh-diff-viewer#readme)
- [Back to the Plugins list](../plugins.md)
