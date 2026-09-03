---
title: "dsh-balance-tide"
description: "DeepSeek Harness (DSH) Web 插件: 余额 + 峰谷计价潮汐提示。显示 DeepSeek 账户余额与本会话花费, 并在余额前提示当前峰/谷价格档位、距切换倒计时与使用建议。"
keywords: "dsh-balance-tide, search, plugin, coding, deepseek harness, dsh"
---
# dsh-balance-tide

> ⭐ **8** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 8 | Status | ✅ active |
| Author | [huanyuLv](https://github.com/huanyuLv) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding |

## One-liner

> DeepSeek Harness (DSH) Web 插件: 余额 + 峰谷计价潮汐提示。显示 DeepSeek 账户余额与本会话花费, 并在余额前提示当前峰/谷价格档位、距切换倒计时与使用建议。

## About

**DeepSeek Harness (DSH) Web plugin: account balance + peak/off-peak pricing tide indicator.** A live readout row under the composer: [standard] peak pricing starts in 2d 5h | Balance ¥28.78 | ~¥0.42 this session | ? Once peak/off-peak pricing takes effect (2026-08-17), the badge and countdown follow Beijing time in real time: [off-peak] peak in 2h 15m | Balance ¥28.78 | ~¥0.42 this session | ? ← off-peak hours [peak] off-peak in 1h 30m | Balance ¥28.78 | ~¥0.42 this session | ? ← peak hours

## ✨ Key Features

- **Pricing badge**: `standard` (before 2026-08-17) / `peak` / `off-peak`, judged live in Beijing time
- **Countdown**: time remaining until the next pricing switch, ticking every second — plan your usage ahead
- **Balance**: live balance from the official `/user/balance` endpoint (granted / topped-up split)
- **Session cost**: estimated at current-period prices (reuses `sessionProjections`; same-turn/step samples replace rather than double-count)
- **Hover details**: full price tables for the current and the next period, the peak/off-peak gap (peak = off-peak × 2), peak windows, and usage advice
- **`?` icon**: opens the official pricing page <https://api-docs.deepseek.com/zh-cn/quick_start/pricing/>
- **Zero config**: reuses `DEEPSEEK_API_KEY` from DSH credentials — no key in the repo, ever
- **i18n**: UI follows the interface language (中文 / English)

## 📦 Install

```bash
dsh plugin --profile web add dsh-balance-tide
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add https://github.com/huanyuLv/dsh-balance-tide
```

## 📚 Learn more

**Install**

**From npm (recommended)** dsh plugin --profile web add dsh-balance-tide **From the Git URL** dsh plugin --profile web add https://github.com/huanyuLv/dsh-balance-tide **From a local directory** dsh plugin --profile web add file:/path/to/dsh-balance-tide Restart `dsh web` to take effect. Requires `pnpm` (`npm i -g pnpm`).

**Configuration (in `$DSH_HOME/profiles/web/cordis.patch.yml`)**

config: refreshIntervalMs: 300000 # how often the host polls the balance API clientPollIntervalMs: 30000 # how often the browser re-reads the cache currency: CNY allowedHosts: [] # register your domain here if you front dsh with a reverse proxy When the official prices or the schedule change, override them in config — no need to wait for a plugin release: config: tideCutoff: '2026-08-17T00:00:00+0

## 🔗 Links

- [GitHub Repository](https://github.com/huanyuLv/dsh-balance-tide)
- [Full README](https://github.com/huanyuLv/dsh-balance-tide#readme)
- [Back to the Plugins list](../plugins.md)
