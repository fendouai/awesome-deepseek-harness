---
title: "dsh-calculator"
description: "Calculate the real-time cost of DeepSeek API calls made by DeepSeek Harness."
keywords: "dsh-calculator, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-calculator

> ⭐ **5** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 5 | Status | ✅ active |
| Author | [bobcat848](https://github.com/bobcat848) | Updated | 2026-08-20 |
| Subcategory | 💰 Cost & billing | Capabilities | coding |

## One-liner

> Calculate the real-time cost of DeepSeek API calls made by DeepSeek Harness.

## About

A DeepSeek Harness (DSH) web plugin that shows your **DeepSeek API spend** and **account balance** in a top-right floating card of the DSH web GUI (collapsible to a pill). - **当前会话费用** — the cost of the session you are looking at (per model) - **当天全部会话累计** — today's total spend across all sessions (per model, **in your local timezone**; resets at local midnight) - **胶囊实时费用** — the collapsed pill shows today's total spend live - **账户余额** — live balance from the DeepSeek API (`GET /user/balance`) - **第三方模型不计费** — only `deepseek-official` routes are billed; any other provider/model is listed as unbilled - **峰谷计价** — prices events by the Beijing peak/off-peak schedule (peak 09:00–12:00 & 14:00–18:00, off-peak = half price); events before 2026-08-17 are still billed at the then-current flat rat

## ✨ Key Features

- **当前会话费用** — the cost of the session you are looking at (per model)
- **当天全部会话累计** — today's total spend across all sessions (per model,
- **胶囊实时费用** — the collapsed pill shows today's total spend live
- **账户余额** — live balance from the DeepSeek API (`GET /user/balance`)
- **第三方模型不计费** — only `deepseek-official` routes are billed; any other
- **峰谷计价** — prices events by the Beijing peak/off-peak schedule (peak

## 📦 Install

```bash
git clone https://github.com/bobcat848/dsh-calculator.git
cd dsh-calculator

# macOS / Linux
bash install.sh

# Windows PowerShell
.\install.ps1
```

## 🚀 Quick Start

```bash
# 1. copy the package into the profile's hoisted node_modules
mkdir -p ~/.dsh/profiles/node_modules/dsh-calculator
cp -r lib package.json ~/.dsh/profiles/node_modules/dsh-calculator/

# 2. append the loader row to the web profile patch (once)
#    edit ~/.dsh/profiles/web/cordis.patch.yml and add:
#    - insert:
#        - id: dsh-calculator
#          name: 'dsh-calculator'
#          config: {}
```

## 📚 Learn more

**安装**

DSH is a Cordis application. The plugin has a host half (event accounting + balance fetching) and a browser half (top-right overlay card). Install it into the `web` profile:

**本地克隆安装**

或者克隆仓库后运行脚本（安装脚本会自动识别本地模式，从仓库内复制文件）： git clone https://github.com/bobcat848/dsh-calculator.git cd dsh-calculator

**配置**

The plugin needs no configuration beyond your DeepSeek API key, which DSH already stores through its credentials service (the Models page writes it to `~/.dsh/.credentials.yaml` as `DEEPSEEK_API_KEY`, or you can export it in the launching environment). The balance feature reads that same credential. If the key is missing, the balance card shows a friendly error and the cost panel keeps working.

## 🔗 Links

- [GitHub Repository](https://github.com/bobcat848/dsh-calculator)
- [Full README](https://github.com/bobcat848/dsh-calculator#readme)
- [Back to the Plugins list](../plugins.md)
