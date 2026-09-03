---
title: "dsh-plugin-smooth-stream"
description: "DSH 流式渲染插件：按段落分批呈现、8 种入场动画、平滑滚动、设置面板。DeepSeek Harness: paragraph-batched streaming reveals, 8 designed animations, smooth scroll-follow and a settings panel."
keywords: "dsh-plugin-smooth-stream, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-smooth-stream

> ⭐ **9** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 9 | Status | ✅ active |
| Author | [SpookySandwich](https://github.com/SpookySandwich) | Updated | — |
| Subcategory | 💡 Generative UI | Capabilities | coding, ui |

## One-liner

> DSH 流式渲染插件：按段落分批呈现、8 种入场动画、平滑滚动、设置面板。DeepSeek Harness: paragraph-batched streaming reveals, 8 designed animations, smooth scroll-follow and a settings panel.

## About

把逐字抖动的流式输出，换成按段落分批、淡入呈现的阅读体验。流式期间平滑跟随滚动，思考块显示实时单行摘要。 **左：DSH 原生渲染 · 右：Smooth Stream** —— 同一个问题，同时开始：

## ✨ Key Features

- **按段落呈现** — 回复不再一个字一个字地蹦，而是攒满一段，整段淡入。断句时自动避开没写完的代码块和表格，Markdown 不会渲染到一半。
- **平滑滚动** — 流式输出时页面匀速滑向底部，长回复也不会猛地一跳；往上滚就交还给你，滚回底部自动继续跟随。
- **思考摘要** — 模型思考时，折叠行里实时滚动最新一句，两端渐隐过渡；回合结束时下划线缓缓收起，示意"想完了"。
- **Markdown 与公式** — 正文走 DSH 自带的渲染器：代码高亮、复制按钮、表格、KaTeX 公式都和原生一模一样。

## 📦 Install

```bash
dsh plugin --profile web add dsh-plugin-smooth-stream
```

## 📚 Learn more

**安装**

dsh plugin --profile web add dsh-plugin-smooth-stream 打开任意会话即可生效。设置入口：设置面板 → **Smooth Stream**。

## 🔗 Links

- [GitHub Repository](https://github.com/SpookySandwich/dsh-plugin-smooth-stream)
- [Full README](https://github.com/SpookySandwich/dsh-plugin-smooth-stream#readme)
- [Back to the Plugins list](../plugins.md)
