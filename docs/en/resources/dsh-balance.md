---
title: "dsh-balance"
description: "DeepSeek Harness balance plugin for the Settings page."
keywords: "dsh-balance, developer, plugin, observability, ui, deepseek harness, dsh"
---
# dsh-balance

> ⭐ **23** · ✅ active · plugin · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 23 | Status | ✅ active |
| Author | [crazywoola](https://github.com/crazywoola) | Updated | 2026-08-17 |
| Subcategory | 💰 Cost & billing | Capabilities | observability, ui |

## One-liner

> DeepSeek Harness balance plugin for the Settings page.

## About

[简体中文](./README.md) | [English](./README_EN.md) DeepSeek Harness 插件，用于查询 API 余额、当前可用模型和多维消费统计。API Key 仅由本机 Host 使用，不会发送到浏览器。

## ✨ Key Features

- 查看总余额、充值余额和赠送余额
- 在聊天框下方持续显示余额摘要
- 查看当前 API Key 可用的模型
- 在设置页按模型、会话和日期查看实际 usage 消费，并在当前会话的“消费”Tab 查看请求明细
- 缺少 provider usage、未知 provider 或未知模型时标记为“未计费”，不进行 token 估算
- 日期按浏览器 IANA 时区分组；DeepSeek 峰谷价格始终按北京时间计算
- 默认显示 USD；配置 `usdToCny` 后额外显示固定汇率换算的 CNY
- 缓存查询结果并支持手动刷新

## 📦 Install

```bash
dsh plugin --profile web add @pinkbanana/dsh-balance@latest
dsh --profile web
```

## 🚀 Quick Start

```bash
usdToCny: 7.2
```

## 📚 Learn more

**安装**

dsh plugin --profile web add @pinkbanana/dsh-balance@latest dsh --profile web 打开 <http://127.0.0.1:3080/>，进入“设置 → DeepSeek 余额”。该入口位于“Agent 预设”下方，余额摘要也会显示在已有会话的聊天框下方。API Key 可在“设置 → 模型”中保存，或通过 `DEEPSEEK_API_KEY` 环境变量提供。 消费统计从已保存会话和当前运行中的 live session 读取，不展示 prompt 内容。可在插件配置中增加固定汇率，例如： usdToCny: 7.2

## 🔗 Links

- [GitHub Repository](https://github.com/crazywoola/dsh-balance)
- [Full README](https://github.com/crazywoola/dsh-balance#readme)
- [Back to the Plugins list](../plugins.md)
