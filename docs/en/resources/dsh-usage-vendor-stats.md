---
title: "dsh-usage-vendor-stats"
description: "DeepSeek Harness usage stats by vendor (subscription / official API) × KPI: 53-week heatmap, trend chart, model drilldown, CSV export, and health cards."
keywords: "dsh-usage-vendor-stats, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-usage-vendor-stats

> ⭐ **2** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [kirigayakazima](https://github.com/kirigayakazima) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> DeepSeek Harness usage stats by vendor (subscription / official API) × KPI: 53-week heatmap, trend chart, model drilldown, CSV export, and health cards.

## About

DeepSeek Harness usage statistics plugin: aggregates API usage **by vendor (subscription / official API) × KPI**, with a GitHub-style calendar heatmap and daily / monthly dashboards.

## ✨ Key Features

- **Vendor dimension**: auto-discovers every vendor used (e.g. `huoshan`, `hebox`, `deepseek-official`, `tokenrhythm`, `opencode`), with manual labels for **subsc
- **KPI cards**: total tokens (input / cache hit / output / reasoning breakdown), cache hit rate, model calls, turns, sessions, vendor count, with a multi-color t
- **53-week heatmap**: GitHub-green style, intensity by daily model calls; click a vendor chip to filter; hover for per-vendor and per-token details.
- **Trend line chart**: Token / Calls dual-axis trend, per-day by default and **per-hour for "today"** (hourly aggregation).
- **Vendor model drilldown**: click a vendor row to expand its per-model consumption.
- **Daily detail**: per-day tokens / cache / output / reasoning / hit rate / turns (last 30 days).
- **Monthly summary**: all history aggregated by month.
- **Vendor KPI table**: sorted by total tokens, with hit rate, model count, type badge; click a row to drill into models.

## 📦 Install

```bash
dsh plugin --profile web add "github:kirigayakazima/dsh-usage-vendor-stats"
```

## 🚀 Quick Start

```bash
New-Item -ItemType Junction -Path "$env:DSH_HOME\profiles\node_modules\dsh-usage-vendor-stats" -Target "<absolute path to this dir>"
```

## 📚 Learn more

**Install**

This is a standard DSH community plugin package (declares `dsh.bundle` manifest + web client half).

**Usage**

1. Open **Settings** (sidebar footer) and find the **API Usage Stats** page, or click the **📊 Usage Stats** entry in the sidebar footer to open the fullscreen panel. 2. Heatmap color = daily call count; click a vendor chip or table row to filter / drill down. 3. In **Vendor Management**, set each vendor's alias and type (subscription / official API), and optionally a per-million-token unit price f

**Architecture**

- `GET /api/usage-vendor-stats` — stats snapshot (vendors / models / daily / monthly / hourly / totals) - `POST /api/usage-vendor-stats/vendor` — set vendor alias, type, and unit price

**从 GitHub 直接安装（推荐）**

dsh plugin --profile web add "github:kirigayakazima/dsh-usage-vendor-stats" 安装后刷新页面即可，无需手动改配置、无需重启。

## 🔗 Links

- [GitHub Repository](https://github.com/kirigayakazima/dsh-usage-vendor-stats)
- [Full README](https://github.com/kirigayakazima/dsh-usage-vendor-stats#readme)
- [Back to the Plugins list](../plugins.md)
