---
title: "dsh-deepseek-balance"
description: "deepseek-harness 插件，实时查询deepseek账号余额"
keywords: "dsh-deepseek-balance, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-deepseek-balance

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [CN-Leo](https://github.com/CN-Leo) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> deepseek-harness 插件，实时查询deepseek账号余额

## About

DeepSeek 账户余额实时显示插件（DeepSeek Harness / DSH）。 在 DSH Web 界面的输入框下方（`conversation.composer.dock`）常驻显示 DeepSeek 官方账户余额，每 15 秒自动刷新；同时按官网最新定价实时计算**本次会话消费金额**。数据来自官方接口 `GET https://api.deepseek.com/user/balance`，API Key 由 Host 端从 DSH 凭据库解析，**绝不会进入浏览器**。

## 📦 Install

```bash
# 从 Git 仓库（发布后）
dsh plugin add https://github.com/<你的用户名>/dsh-deepseek-balance

# 或从本地目录
dsh plugin add /path/to/dsh-deepseek-balance
```

## 🚀 Quick Start

```bash
DEEPSEEK_API_KEY: sk-xxxxxxxxxxxxxxxx
```

## 📚 Learn more

**配置（必需）**

插件通过 `credentials` 服务解析 `DEEPSEEK_API_KEY`，按以下顺序查找（任选其一）： 1. 环境变量 `DEEPSEEK_API_KEY` 2. `$DSH_HOME/.credentials.yaml`： ```yaml DEEPSEEK_API_KEY: sk-xxxxxxxxxxxxxxxx ``` 配置后无需重启插件：每次请求都会重新解析凭据。

**使用**

- 绿点 = 正常，黄点 = 加载中，红点 = 获取失败 - 「本会话消费」**按会话实际使用的模型分模型计价**（从会话日志逐次提取每个模型调用的 token 用量），仅 deepseek-v4-flash / deepseek-v4-pro 套用官网价格，自动区分**高峰/空闲时段**（北京时间 9:00-12:00、14:00-18:00 为高峰，其余空闲），每 15 秒与余额一同刷新 - 各币种余额：总额 / 赠送 / 充值 / 账户可用状态 - 本次会话**按模型分列**的 token 用量：输入（未命中/命中/写入）、输出 - 当前时段、本次会话消费金额

## 🔗 Links

- [GitHub Repository](https://github.com/CN-Leo/dsh-deepseek-balance)
- [Full README](https://github.com/CN-Leo/dsh-deepseek-balance#readme)
- [Back to the Plugins list](../plugins.md)
