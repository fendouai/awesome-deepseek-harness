---
title: "dsh-deepseek-billing"
description: "DSH WebUI 插件:DeepSeek 余额显示与按会话费用估算"
keywords: "dsh-deepseek-billing, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-deepseek-billing

> ⭐ **5** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 5 | Status | ✅ active |
| Author | [Jolly-J](https://github.com/Jolly-J) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, ui |

## One-liner

> DSH WebUI 插件:DeepSeek 余额显示与按会话费用估算

## About

给 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)(DSH)网页版装一个**余额小卡片**:左侧边栏底部常驻显示你的 DeepSeek **账户余额**,以及**当前会话花了多少钱**。不用翻网页、不用开账单,一眼看住钱包。

## ✨ Key Features

- **一行摘要**:状态点 · `余额:¥xx.xx元` · `会话:¥x.xxx` · 刷新按钮 · 展开箭头;
- **点击展开详情**:充值/赠送余额、token 明细(输入/缓存命中/输出)、缓存命中率、输入与输出费用小计、当前费率说明(标注"估算,非账单");
- 数字变化时是**滚动动画**;切换会话自动跟着变;
- 侧边栏收起(窄栏)时自动隐藏,不挡东西;
- 每 60 秒自动刷新一次,也可以随时点刷新按钮。

## 📦 Install

```bash
dsh plugin --profile web add https://github.com/Jolly-J/dsh-deepseek-billing.git
```

## 🚀 Quick Start

```bash
dsh plugin --profile web update dsh-deepseek-billing
```

## 📚 Learn more

**费用准确性说明(与余额对账必读)**

卡片上的"会话费用"是**估算值,不是账单**:官方刊例价 × 会话内**成功请求**的用量。以下三样是会话日志看不见、但余额会扣的: 1. **失败重试**:模型请求失败重试时,每次尝试的输入 token 都会被计费,但只有最终成功的那次会写进会话日志; 2. **后台模型调用**:会话标题生成、联网搜索的查询等不在会话 usage 里; 3. **余额异步入账**:DeepSeek 结算有延迟,余额读数可能滞后或提前包含窗口外的消费。 **作者实测对账案例**(7 分钟窗口):余额 -¥1.36,会话估算 +¥1.035,差 ¥0.325——正是上述不可见计费。**余额是唯一真值,卡片费用仅作归因参考。**

## 🔗 Links

- [GitHub Repository](https://github.com/Jolly-J/dsh-deepseek-billing)
- [Full README](https://github.com/Jolly-J/dsh-deepseek-billing#readme)
- [Back to the Plugins list](../plugins.md)
