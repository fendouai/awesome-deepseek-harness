---
title: "dsh-save-money"
description: "Save-money plugin for DSH (DeepSeek Harness) — define your own \"pause / resume\" time windows; at pause time running long tasks are paused (not stopped) automatically, and they resume when the window ends."
keywords: "dsh-save-money, learning, skill, coding, deepseek harness, dsh"
---
# dsh-save-money

> ⭐ **35** · ✅ active · skill

| | | | |
|---|---|---|---|
| Type | skill | Category | Learning |
| Stars | ⭐ 35 | Status | ✅ active |
| Author | [zhu168](https://github.com/zhu168) | Updated | — |

## One-liner

> Save-money plugin for DSH (DeepSeek Harness) — define your own "pause / resume" time windows; at pause time running long tasks are paused (not stopped) automatically, and they resume when the window ends.

## About

**Save-money plugin** for DSH (DeepSeek Harness) — define your own "pause / resume" time windows; at pause time running long tasks are **paused** (not stopped) automatically, and they resume when the window ends. Built for LLM API **peak/off-peak pricing** (e.g. DeepSeek peak hours 9:00–12:00, 14:00–18:00 Beijing time, off-peak at half price; since **2026-08-23 weekends are off-peak all day** — the plugin's weekday switch skips Sat/Sun by default), and equally useful for time-of-use electricity rates, bandwidth off-peak shifting, or any "I don't want the machine working during this period" scenario.

## ✨ Key Features

- **Multiple time windows**: add / remove pause-resume windows freely; supports midnight-crossing windows (23:00–08:00) and per-weekday filtering;
- **Automatic pause on schedule**: when the pause time arrives, running tasks are safely "frozen" (their progress is preserved exactly — nothing is interrupted or
- **No requests during the window (the saving core)**: inside a pause window the AI sends no new requests to the model service, so **no cost is incurred**; after 
- **Per-model-tier save mode**: decide per model tier which ones pause during windows. The settings panel shows two compact rows — **Official API** (the DeepSeek 
- **Global weekday switch**: one row above the window list — 一 ☑️ 二 ☑️ 三 ☑️ 四 ☑️ 五 ☑️ 六 ⬜ 日 ⬜. Saving applies only on the checked days (default **Mon–Fri** — unde
- **End this save mode (one-shot, current window only)**: the banner and settings-popover button end the **currently active** pause window only — if paused, tasks
- **UI reminders**: top floating banner (light yellow for upcoming pause / light red for paused, with the **End this save mode** button) + the single persistent s
- **Timezone support**: IANA timezone dropdown, browser auto-detection with Beijing time (+8) fallback; UTC projection checked (Beijing 09:00 == UTC 01:00);

## 📦 Install

```bash
npx @deepseek-ai/dsh plugin --profile web add dsh-save-money
```

## 🚀 Quick Start

```bash
npx @deepseek-ai/dsh plugin --profile web remove dsh-save-money
```

## 📚 Learn more

**Install**

The official DSH plugin form is a **module exporting `apply` + cordis.yml mounting** (see the [DSH official tutorial](https://github.com/deepseek-ai/deepseek-harness/blob/main/docs/user/develop/basic/index.md)). You can install from **npm** (one command, recommended) or build from this repository (three options below: `--patch` quick try, distributable bundle, or the link + HMR development workflo

**Source install (build from this repo)**

Using `~/app/` as an example directory (each step assumes the previous one succeeded): cd ~/app/ git clone https://github.com/zhu168/dsh-save-money.git cd dsh-save-money npm install cd plugin npm pack # runs the build automatically; produces the plugin tarball ls # check the tarball name, e.g. dsh-save-money-1.4.4.tgz cd ~/app/deepseek-harness # change to your harness directory (clone it first if 

**Path 1: `--patch` quick try (official, loads local source)**

Good for trying the plugin on the same machine where you keep this repository. 1. (Optional) Rebuild the latest plugin module — a fresh clone needs the build deps first: ```sh npm install # first clone: installs typescript and friends npm run prepare # one step: src/*.ts -> dist/*.js -> plugin/index.js + plugin/client.js ``` 2. Edit `cordis.patch.yml`, replacing `<REPO_ROOT>` with the repository's

**npx-launched (Step 0, option A) or globally installed dsh: w**

npx @deepseek-ai/dsh plugin --profile web add ~/dsh-save-money-1.4.4.tgz > Both commands do the same thing: install the tgz into `~/.dsh/profiles/web/node_modules/`. Use whichever matches how you start DSH. Git install also works: `dsh plugin --profile web add github:you/dsh-save-money#<sha>` (git install requires `prepare` builds and `allowBuilds`, see the [DSH publish tutorial](https://github.co

## 🔗 Links

- [GitHub Repository](https://github.com/zhu168/dsh-save-money)
- [Full README](https://github.com/zhu168/dsh-save-money#readme)
- [Back to the Skills list](../skills.md)
