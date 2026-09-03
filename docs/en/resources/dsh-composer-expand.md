---
title: "dsh-composer-expand"
description: "Composer expand/collapse toggle for DeepSeek Harness (dsh): a ⬆/⬇ button in the composer tool row grows the input to a tall 70vh writing view for long drafts."
keywords: "dsh-composer-expand, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-composer-expand

> ⭐ **6** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [13071301808](https://github.com/13071301808) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Composer expand/collapse toggle for DeepSeek Harness (dsh): a ⬆/⬇ button in the composer tool row grows the input to a tall 70vh writing view for long drafts.

## About

为 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（`dsh`）打造的 composer 展开/收起插件。在 composer 工具行放一个 ⬆/⬇ 按钮，点击在「默认封顶高度」与「70vh 高书写视图」之间切换，长草稿不再挤在一个小窗口里滚动。

## ✨ Key Features

- **⬆ 按钮在 composer 工具行** — 位于 `conversation.input.right`（发送按钮旁官方预留的可点击控件位）。
- **展开到 70vh** — 在会话滚动容器上切换 CSS class；composer 卡片与 textarea 同步放宽 `max-height`。再点一次恢复默认封顶高度。
- **展开最小高度 300px** — 输入内容较少时也保持足够的书写空间；内容变多后最高仍受 `70vh` 限制。
- **展开状态回车换行** — 展开时普通回车只插入换行，不触发发送；`Ctrl/Cmd + Enter` 等带修饰键快捷键仍可用于发送。
- **浏览器内持久化** — 状态写入 `localStorage[dsh-composer-expand:expanded]`，刷新页面、切换工作区都保留。
- **中英文双语** — 按钮文案与提示跟随 DSH 的 `locale` 服务。
- **纯前端** — 无自定义协议、无 host 命令、无 LLM 调用、不进会话日志。
- **不依赖构建哈希** — CSS 锚定 DSH 稳定的 `data-conversation-scroll` / `data-composer-seat` / `data-input-mirror` 属性，而不是每次构建都会变的哈希类名。

## 📦 Install

```bash
dsh plugin --profile web add dsh-composer-expand
```

## 🚀 Quick Start

```bash
npm install -g @deepseek-ai/dsh
```

## 🔗 Links

- [GitHub Repository](https://github.com/13071301808/dsh-composer-expand)
- [Full README](https://github.com/13071301808/dsh-composer-expand#readme)
- [Back to the Plugins list](../plugins.md)
