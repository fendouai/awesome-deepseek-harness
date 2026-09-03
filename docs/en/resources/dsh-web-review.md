---
title: "dsh-web-review"
description: "DeepSeek Harness Web GUI 的网页预览与元素批注插件，让 AI 根据可视化反馈直接修改前端源码。"
keywords: "dsh-web-review, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-web-review

> ⭐ **15** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 15 | Status | ✅ active |
| Author | [CanglongCl](https://github.com/CanglongCl) | Updated | 2026-08-20 |
| Subcategory | 💡 Generative UI | Capabilities | coding, ui |

## One-liner

> DeepSeek Harness Web GUI 的网页预览与元素批注插件，让 AI 根据可视化反馈直接修改前端源码。

## About

[English](./README_en.md) 在内置浏览器中，像使用设计工具一样选择页面元素、填写修改意见，并临时调整文本、颜色、字体、尺寸、间距、边框与效果。确认发送后，Agent 会结合页面批注修改当前工作区中的源码。

## 📦 Install

```bash
dsh plugin --profile web add @canglongcl/dsh-web-review
dsh web
```

## 📚 Learn more

**使用方法**

1. 告诉启动要评审的前端页面，点击AI返回的地址页面。 也可以切换到 DSH 的「网页预览」Tab，输入页面的绝对 HTTP(S) URL。 2. 点击批注按钮，再点击页面中的目标元素。 3. 填写修改意见；如需视觉调整，展开「调整」并修改属性。 4. 点击批注工具栏中的发送按钮，发送后会自动切回「对话」Tab；或在 DSH 的输入框中填写更多提示词，然后点击 DSH 发送按钮，注释会随着你的提示词一同发送。 5. Agent 修改源码后，刷新预览进行验收；不满意可以继续下一轮批注。

## 🔗 Links

- [GitHub Repository](https://github.com/CanglongCl/dsh-web-review)
- [Full README](https://github.com/CanglongCl/dsh-web-review#readme)
- [Back to the Plugins list](../plugins.md)
