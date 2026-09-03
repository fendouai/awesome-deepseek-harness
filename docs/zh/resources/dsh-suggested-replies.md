---
title: "dsh-suggested-replies"
description: "DSH Web 预测回复插件：AI 回复后在输入框上方生成可点击填入草稿的候选。"
keywords: "dsh-suggested-replies, ui, plugin, deepseek harness, dsh"
---
# dsh-suggested-replies

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [Anionex](https://github.com/Anionex) | 更新时间 | 2026-08-14 |
| 子分类 | 💡 生成式界面 | 能力 | ui |

## 一句话介绍

> DSH Web 预测回复插件：AI 回复后在输入框上方生成可点击填入草稿的候选。

## 详细介绍

DSH Web 的“预测回复”插件：AI 回复结束后，生成几条用户下一步可能会发送的消息候选，并将它们显示在**聊天输入框上方**。点击候选只会将文本填入输入框，**不会自动发送**。

## ✨ 核心特性

- **正确位置**：注册 `conversation.input.dock`，位于 DSH 的消息输入卡片上方；不会放到输入框下方的 `conversation.composer.dock`。
- **单行展示**：候选始终保持在一条横线上；宽度不足时横向滚动查看，不换到第二行。
- **只填入草稿**：点击候选会替换当前草稿为该候选，不会调用发送动作。
- **候选内容**：优先覆盖合理的下一步执行、验证/追问、或决策/选择；候选跟随最近对话语言，彼此去重且可直接发送。
- **失败兜底**：辅助模型没有返回规定 JSON 时，插件仍按最近对话语言生成配置数量的保守候选，不再把空数组当成成功结果隐藏整行。
- **上下文范围**：辅助提示词只截取直接用户消息和 AI 回复；AGENTS、运行时快照和 Skill 目录等注入上下文不会挤占最近对话窗口。

## 📦 安装

```bash
dsh plugin --profile web add @anionex/dsh-suggested-replies
```

## 🚀 快速开始

```bash
dsh plugin --profile web add /absolute/path/to/dsh-suggested-replies
```

## 📚 更多信息

**本地开发目录安装**

dsh plugin --profile web add /absolute/path/to/dsh-suggested-replies 安装或更新后，重启正在运行的 `dsh web` 服务，并在浏览器硬刷新页面。新建或重新打开一个会话后进行验证。

**设置与配置**

Web 设置页中的“下一步建议”分区提供 `enabled` 总开关。它写入 `$DSH_HOME/settings.yaml` 的 `suggested-replies` 区域，下一轮立即生效。 其余部署参数在 `cordis.patch.yml` 或 profile overlay 中配置： 示例 overlay： - id: suggested-replies config: suggestionCount: 4 maxSuggestionChars: 120 timeoutMs: 10000 suggestionProvider: deepseek-official suggestionModel: deepseek-v4-flash

## 🔗 链接

- [GitHub 仓库](https://github.com/Anionex/dsh-suggested-replies)
- [完整 README](https://github.com/Anionex/dsh-suggested-replies#readme)
- [返回dsh-suggested-replies所在分类](../plugins.md)
