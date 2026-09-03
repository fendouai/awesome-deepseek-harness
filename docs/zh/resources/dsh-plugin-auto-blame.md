---
title: "dsh-plugin-auto-blame"
description: "模型回合结束后用 LLM 生成 3 条批判性跟进建议，点击即发送 | After a model turn, an LLM generates 3 critical follow-up suggestions shown as click-to-send chips"
keywords: "dsh-plugin-auto-blame, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-auto-blame

> ⭐ **9** · ✅ 活跃 · 插件 · 近期 ⬆️ +3

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 9 | 状态 | ✅ 活跃 |
| 作者 | [HuanLinOTO](https://github.com/HuanLinOTO) | 更新时间 | 2026-08-15 |

## 一句话介绍

> 模型回合结束后用 LLM 生成 3 条批判性跟进建议，点击即发送 | After a model turn, an LLM generates 3 critical follow-up suggestions shown as click-to-send chips

## 详细介绍

当模型完成当前轮次对话后，将最后 3 条消息发送给 LLM，生成 3 条批判性跟进请求，显示在输入框上方作为可选项，点击直接发送。生成期间"领导视野"标签带 DeepSeek 蓝色流光扫过（同 Deep diving... 特效），建议到达后气泡依次淡入。

## ✨ 核心特性

- **fire-and-forget**：LLM 调用不阻塞 turn 关闭，建议晚几百 ms 出现
- **非 surface 事件**：`auto-blame/suggestions` 不进入 model-visible 历史，不干扰 agent loop
- **失败静默**：LLM 失败 / 解析失败 → 不 append 事件，不显示气泡
- **点击发送**：走 InputBar 同一路径（`inputActions.setDraft + submit`）
- **下一轮清空**：新 turn 开始时 projection 归零，旧气泡立即消失

## 📦 安装

```bash
# 从 npm 安装（推荐）
dsh plugin --profile web add @huanlin/dsh-plugin-auto-blame

# 本地开发（热更新）
dsh plugin --profile web add "link:D:/Projects/deepseek-harness/dsh-auto-blame"
```

## 🚀 快速开始

```bash
[host] agent/turn-stopping 触发
  → fire-and-forget 调 ctx.llm.stream() 生成 3 条毒舌跟进
  → session.append('auto-blame/suggestions', { turn, suggestions })
  → projection unit 折叠该事件 → session/projection 推送帧
  ↓
[client] useProjection('autoBlame') 收到值
  → conversation.composer.dock 渲染 3 个气泡
  → 点击 → inputActions.setDraft(text) + submit()
```

## 📚 更多信息

**工作原理**

[host] agent/turn-stopping 触发 → fire-and-forget 调 ctx.llm.stream() 生成 3 条毒舌跟进 → session.append('auto-blame/suggestions', { turn, suggestions }) → projection unit 折叠该事件 → session/projection 推送帧 ↓ [client] useProjection('autoBlame') 收到值 → conversation.composer.dock 渲染 3 个气泡 → 点击 → inputActions.setDraft(text) + submit()

## 🔗 链接

- [GitHub 仓库](https://github.com/HuanLinOTO/dsh-plugin-auto-blame)
- [完整 README](https://github.com/HuanLinOTO/dsh-plugin-auto-blame#readme)
- [返回dsh-plugin-auto-blame所在分类](../plugins.md)
