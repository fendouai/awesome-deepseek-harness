---
title: "dsh-balance-meter"
description: "DeepSeek account balance and session cost readout for the DeepSeek Harness Web GUI"
keywords: "dsh-balance-meter, developer, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-balance-meter

> ⭐ **19** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 19 | 状态 | ✅ 活跃 |
| 作者 | [Ghost011118](https://github.com/Ghost011118) | 更新时间 | 2026-08-20 |
| 子分类 | 💰 费用与统计 | 能力 | coding, ui |

## 一句话介绍

> DeepSeek account balance and session cost readout for the DeepSeek Harness Web GUI

## 详细介绍

DeepSeek account balance and session-cost readout for the DeepSeek Harness (DSH) Web GUI. - Explicit balance sources: official API, proxy-compatible endpoint, or a manual balance accounted and persisted locally - Current session estimated spend (token usage x official pricing) - Per-model pricing: reads the model actually driving each session from its request header (flash vs pro), so the cost tracks the model you used instead of a fixed default - Auto-fetches the official pricing page every 6h, so price changes and the 2026-08-17 peak/off-peak pricing rollout never require a plugin update - Peak-hour band (Beijing 09:00-12:00 / 14:00-18:00) applied automatically once the peak pricing goes live

## ✨ 核心特性

- Explicit balance sources: official API, proxy-compatible endpoint, or a
- Current session estimated spend (token usage x official pricing)
- Per-model pricing: reads the model actually driving each session from its
- Auto-fetches the official pricing page every 6h, so price changes and the
- Peak-hour band (Beijing 09:00-12:00 / 14:00-18:00) applied automatically

## 📦 安装

```bash
dsh plugin --profile web add https://github.com/Ghost011118/dsh-balance-meter
```

## 🚀 快速开始

```bash
git clone https://github.com/Ghost011118/dsh-balance-meter.git
dsh plugin --profile web add link:$(pwd)/dsh-balance-meter
```

## 📚 更多信息

**Installation**

From a git URL (no npm account needed): dsh plugin --profile web add https://github.com/Ghost011118/dsh-balance-meter Or from a local checkout: git clone https://github.com/Ghost011118/dsh-balance-meter.git dsh plugin --profile web add link:$(pwd)/dsh-balance-meter Restart `dsh web`, then refresh the page. The balance chip appears in the composer dock next to the conversation stats line.

**Configuration**

The plugin is zero-config by default (uses `DEEPSEEK_API_KEY` and the official pricing page). Optional composition settings: - id: balance name: 'dsh-balance-meter' config: source: official # official (default) | proxy | manual model: auto # 'auto' (default) | 'flash' | 'pro' pricingRefreshHours: 6

## 🔗 链接

- [GitHub 仓库](https://github.com/Ghost011118/dsh-balance-meter)
- [完整 README](https://github.com/Ghost011118/dsh-balance-meter#readme)
- [返回dsh-balance-meter所在分类](../plugins.md)
