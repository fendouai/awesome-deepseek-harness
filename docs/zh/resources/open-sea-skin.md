---
title: "Open Sea Skin"
description: "实时 WebGPU 海洋皮肤，可调节波浪、日光、玻璃不透明度和自动昼夜循环。"
keywords: "Open Sea Skin, ui, plugin, deepseek harness, dsh"
---
# Open Sea Skin

> ⭐ **185** · ✅ 活跃 · 插件 · 近期 ⬆️ +4

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 185 | 状态 | ✅ 活跃 |
| 作者 | [d-dev0101](https://github.com/d-dev0101) | 更新时间 | 2026-08-19 |
| 子分类 | 🎨 皮肤与主题 | 能力 | ui |

## 一句话介绍

> 实时 WebGPU 海洋皮肤，可调节波浪、日光、玻璃不透明度和自动昼夜循环。

## 详细介绍

[Interactive website](https://d-dev0101.github.io/open-sea-skin/) · [中文](README.zh.md) · [Architecture](docs/architecture.md) · [Release guide](docs/releasing.md) Before installing, preview the official website first Open the live demo, tune the waves, sunset, and glass transparency, then install only after you like the result. Official website · Install guide · Releases · Source code · DSH plugin directory · Support / Issues Need login or installation help? Leave a message in Issues and mention @d-dev0101. A self-contained WebGPU ocean skin for DeepSeek Harness. It keeps the original five-wave Gerstner/TSL look, adds a translucent Harness theme, and is available as a one-line DSH plugin, Harness-only Chrome/Edge extension, one-command static installer, or native Harness source integration

## ✨ 核心特性

- WebGPU + three.js 0.178.0 + TSL, five Gerstner waves, analytic normals, FBM
- A local-only runtime: three.js and Geist are vendored; the extension and
- 256×256 mesh (160×160 in low/reduced-motion mode), DPR cap 1.5, adaptive
- Twelve-minute daylight cycle; manual daylight adjustment pins the selected
- Shared host controller for the extension and static installer, with only the
- Duplicate-render prevention across all installation methods, bilingual UI,
- A corrected layout stacking model: Settings stays above the conversation

## 📦 安装

```bash
dsh plugin --profile web add 'github:d-dev0101/open-sea-skin#v1.2.2'
```

## 🚀 快速开始

```bash
dsh plugin --profile web remove open-sea-skin
```

## 📚 更多信息

**Recommended — install as a DSH plugin**

Install the complete local-only ocean runtime and lower-left quick controls directly from GitHub: dsh plugin --profile web add 'github:d-dev0101/open-sea-skin#v1.2.2' Restart `dsh web`, then use **Skin settings** at the lower left to adjust wave size, daylight, 40% glass opacity, and the automatic day/night cycle. Remove it with: dsh plugin --profile web remove open-sea-skin This package is tested

**Install option 1 — Chrome or Edge extension**

1. Download and unzip the latest `open-sea-skin-extension-*.zip` release, or clone this repository. 2. Open `chrome://extensions` (Edge: `edge://extensions`) and enable **Developer mode**. 3. Select **Load unpacked** and choose this repository's `extension/` folder. 4. Open DeepSeek Harness on `127.0.0.1` or `localhost`, then reload it once. The extension does **not** replace Chrome or Edge's new-

**Install option 2 — Harness static build (no source compilati**

Run this from **any directory**. It downloads the pinned `v1.2.2` source archive to a temporary directory, runs the installer, and removes the download when it finishes. **Stop Harness before running it**, then start `dsh web` again, keep that terminal process running, and reload the browser: curl -fsSL https://raw.githubusercontent.com/d-dev0101/open-sea-skin/main/install.sh | bash The script fin

## 🔗 链接

- [GitHub 仓库](https://github.com/d-dev0101/open-sea-skin)
- [完整 README](https://github.com/d-dev0101/open-sea-skin#readme)
- [返回Open Sea Skin所在分类](../plugins.md)
