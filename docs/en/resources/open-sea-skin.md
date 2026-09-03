---
title: "Open Sea Skin"
description: "Realtime WebGPU ocean skin with controls for waves, daylight, glass opacity and automatic day cycling."
keywords: "Open Sea Skin, ui, plugin, deepseek harness, dsh"
---
# Open Sea Skin

> ⭐ **185** · ✅ active · plugin · ⬆️ +4 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 185 | Status | ✅ active |
| Author | [d-dev0101](https://github.com/d-dev0101) | Updated | 2026-08-19 |
| Subcategory | 🎨 Skins & themes | Capabilities | ui |

## One-liner

> Realtime WebGPU ocean skin with controls for waves, daylight, glass opacity and automatic day cycling.

## About

[Interactive website](https://d-dev0101.github.io/open-sea-skin/) · [中文](README.zh.md) · [Architecture](docs/architecture.md) · [Release guide](docs/releasing.md) Before installing, preview the official website first Open the live demo, tune the waves, sunset, and glass transparency, then install only after you like the result. Official website · Install guide · Releases · Source code · DSH plugin directory · Support / Issues Need login or installation help? Leave a message in Issues and mention @d-dev0101. A self-contained WebGPU ocean skin for DeepSeek Harness. It keeps the original five-wave Gerstner/TSL look, adds a translucent Harness theme, and is available as a one-line DSH plugin, Harness-only Chrome/Edge extension, one-command static installer, or native Harness source integration

## ✨ Key Features

- WebGPU + three.js 0.178.0 + TSL, five Gerstner waves, analytic normals, FBM
- A local-only runtime: three.js and Geist are vendored; the extension and
- 256×256 mesh (160×160 in low/reduced-motion mode), DPR cap 1.5, adaptive
- Twelve-minute daylight cycle; manual daylight adjustment pins the selected
- Shared host controller for the extension and static installer, with only the
- Duplicate-render prevention across all installation methods, bilingual UI,
- A corrected layout stacking model: Settings stays above the conversation

## 📦 Install

```bash
dsh plugin --profile web add 'github:d-dev0101/open-sea-skin#v1.2.2'
```

## 🚀 Quick Start

```bash
dsh plugin --profile web remove open-sea-skin
```

## 📚 Learn more

**Recommended — install as a DSH plugin**

Install the complete local-only ocean runtime and lower-left quick controls directly from GitHub: dsh plugin --profile web add 'github:d-dev0101/open-sea-skin#v1.2.2' Restart `dsh web`, then use **Skin settings** at the lower left to adjust wave size, daylight, 40% glass opacity, and the automatic day/night cycle. Remove it with: dsh plugin --profile web remove open-sea-skin This package is tested

**Install option 1 — Chrome or Edge extension**

1. Download and unzip the latest `open-sea-skin-extension-*.zip` release, or clone this repository. 2. Open `chrome://extensions` (Edge: `edge://extensions`) and enable **Developer mode**. 3. Select **Load unpacked** and choose this repository's `extension/` folder. 4. Open DeepSeek Harness on `127.0.0.1` or `localhost`, then reload it once. The extension does **not** replace Chrome or Edge's new-

**Install option 2 — Harness static build (no source compilati**

Run this from **any directory**. It downloads the pinned `v1.2.2` source archive to a temporary directory, runs the installer, and removes the download when it finishes. **Stop Harness before running it**, then start `dsh web` again, keep that terminal process running, and reload the browser: curl -fsSL https://raw.githubusercontent.com/d-dev0101/open-sea-skin/main/install.sh | bash The script fin

## 🔗 Links

- [GitHub Repository](https://github.com/d-dev0101/open-sea-skin)
- [Full README](https://github.com/d-dev0101/open-sea-skin#readme)
- [Back to the Plugins list](../plugins.md)
