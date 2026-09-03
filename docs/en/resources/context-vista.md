---
title: "context-vista"
description: "Live context/token monitor: floating panel + /context command with donut charts of token usage, allocation and estimated cost."
keywords: "context-vista, memory, plugin, context, observability, deepseek harness, dsh"
---
# context-vista

> ⭐ **10** · ✅ active · plugin · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 10 | Status | ✅ active |
| Author | [GooodWei](https://github.com/GooodWei) | Updated | 2026-08-17 |
| Subcategory | 📦 Context management | Capabilities | context, observability |

## One-liner

> Live context/token monitor: floating panel + /context command with donut charts of token usage, allocation and estimated cost.

## About

为 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 提供 `/context` 斜杠命令，用**环形图**实时展示当前上下文 token 用量与分配。对话区右侧还常驻一张迷你悬浮卡，实时显示占用率与估算费用，可拖动、可收起。

## 📦 Install

```bash
npx @deepseek-ai/dsh plugin --profile web add github:GooodWei/context-vista
npx @deepseek-ai/dsh web
```

## 🚀 Quick Start

```bash
context-vista:
  pricing:
    "https://api.deepseek.com":
      models:
        deepseek-v4-pro:
          peak:    { hit: 0.3, miss: 9, output: 27 }
          offpeak: { hit: 0.15, miss: 4.5, output: 13.5 }
```

## 📚 Learn more

**安装**

npx @deepseek-ai/dsh plugin --profile web add github:GooodWei/context-vista npx @deepseek-ai/dsh web > 需先安装 pnpm（`dsh plugin add` 内部会调用它）。已全局安装 dsh 时，`npx @deepseek-ai/dsh` 可简写为 `dsh`。

**使用**

输入 `/context` 回车，展示一张卡片：上下文组成环形图（系统 / 工具 / 消息 / 剩余）、占用进度条、会话累计与估算费用。 右侧的迷你环形图悬浮卡实时更新、无需输入命令；按住标题栏可上下拖动（位置自动记忆），点右上角箭头可收起/展开。悬浮卡底部还有「压缩上下文」按钮，点击即触发 `/compact`（效果等同输入命令），压缩进行中会显示「压缩中…」并禁用。

**最简示例**

context-vista: pricing: "https://api.deepseek.com": models: deepseek-v4-pro: peak: { hit: 0.3, miss: 9, output: 27 } offpeak: { hit: 0.15, miss: 4.5, output: 13.5 }

**完整示例（DeepSeek ¥ + OpenAI $，标注全部键值对）**

context-vista: pricing: # 定价表：外层键 = 路由名 或 baseURL "https://api.deepseek.com": # 路由①：DeepSeek，人民币 + 北京时间峰谷 currency: "¥" # 本 API 的计价货币单位（省略默认 "¥"） timezone: 8 # 峰谷时段所在时区（UTC 偏移；省略默认 8） peakWindows: # 高峰窗口，HH:MM，含起点不含终点；start > end 表示跨午夜 - start: "09:00" # 高峰起点 end: "12:00" # 高峰终点 - start: "14:00" # 第二段高峰起点 end: "18:00" # 第二段高峰终点 models: # 本 API 下的模型（必填） deepseek-v4-pro: # 模型名 peak: # 写法一（峰谷分档）· 高峰价

## 🔗 Links

- [GitHub Repository](https://github.com/GooodWei/context-vista)
- [Full README](https://github.com/GooodWei/context-vista#readme)
- [Back to the Plugins list](../plugins.md)
