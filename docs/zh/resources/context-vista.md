---
title: "context-vista"
description: "上下文/Token 实时监控：悬浮面板 + /context 命令，环形图展示用量、分配与估算费用。"
keywords: "context-vista, memory, plugin, context, observability, deepseek harness, dsh"
---
# context-vista

> ⭐ **10** · ✅ 活跃 · 插件 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 记忆与上下文 |
| 星数 | ⭐ 10 | 状态 | ✅ 活跃 |
| 作者 | [GooodWei](https://github.com/GooodWei) | 更新时间 | 2026-08-17 |
| 子分类 | 📦 上下文管理 | 能力 | context, observability |

## 一句话介绍

> 上下文/Token 实时监控：悬浮面板 + /context 命令，环形图展示用量、分配与估算费用。

## 详细介绍

为 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 提供 `/context` 斜杠命令，用**环形图**实时展示当前上下文 token 用量与分配。对话区右侧还常驻一张迷你悬浮卡，实时显示占用率与估算费用，可拖动、可收起。

## 📦 安装

```bash
npx @deepseek-ai/dsh plugin --profile web add github:GooodWei/context-vista
npx @deepseek-ai/dsh web
```

## 🚀 快速开始

```bash
context-vista:
  pricing:
    "https://api.deepseek.com":
      models:
        deepseek-v4-pro:
          peak:    { hit: 0.3, miss: 9, output: 27 }
          offpeak: { hit: 0.15, miss: 4.5, output: 13.5 }
```

## 📚 更多信息

**安装**

npx @deepseek-ai/dsh plugin --profile web add github:GooodWei/context-vista npx @deepseek-ai/dsh web > 需先安装 pnpm（`dsh plugin add` 内部会调用它）。已全局安装 dsh 时，`npx @deepseek-ai/dsh` 可简写为 `dsh`。

**使用**

输入 `/context` 回车，展示一张卡片：上下文组成环形图（系统 / 工具 / 消息 / 剩余）、占用进度条、会话累计与估算费用。 右侧的迷你环形图悬浮卡实时更新、无需输入命令；按住标题栏可上下拖动（位置自动记忆），点右上角箭头可收起/展开。悬浮卡底部还有「压缩上下文」按钮，点击即触发 `/compact`（效果等同输入命令），压缩进行中会显示「压缩中…」并禁用。

**最简示例**

context-vista: pricing: "https://api.deepseek.com": models: deepseek-v4-pro: peak: { hit: 0.3, miss: 9, output: 27 } offpeak: { hit: 0.15, miss: 4.5, output: 13.5 }

**完整示例（DeepSeek ¥ + OpenAI $，标注全部键值对）**

context-vista: pricing: # 定价表：外层键 = 路由名 或 baseURL "https://api.deepseek.com": # 路由①：DeepSeek，人民币 + 北京时间峰谷 currency: "¥" # 本 API 的计价货币单位（省略默认 "¥"） timezone: 8 # 峰谷时段所在时区（UTC 偏移；省略默认 8） peakWindows: # 高峰窗口，HH:MM，含起点不含终点；start > end 表示跨午夜 - start: "09:00" # 高峰起点 end: "12:00" # 高峰终点 - start: "14:00" # 第二段高峰起点 end: "18:00" # 第二段高峰终点 models: # 本 API 下的模型（必填） deepseek-v4-pro: # 模型名 peak: # 写法一（峰谷分档）· 高峰价

## 🔗 链接

- [GitHub 仓库](https://github.com/GooodWei/context-vista)
- [完整 README](https://github.com/GooodWei/context-vista#readme)
- [返回context-vista所在分类](../plugins.md)
