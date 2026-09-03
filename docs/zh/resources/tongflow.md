---
title: "tongflow"
description: "TongFlow — multimodal workflow studio and engine (canvas + Python plugin engine) and dsh-tongflow, the DeepSeek Harness studio plugin"
keywords: "tongflow, workflow, coding, multimodal, deepseek harness, dsh"
---
# tongflow

> ⭐ **902** · ✅ 活跃 · 工作流 · 近期 ⬆️ +16

| | | | |
|---|---|---|---|
| 类型 | 工作流 | 分类 | 工作流 |
| 星数 | ⭐ 902 | 状态 | ✅ 活跃 |
| 作者 | [tong-io](https://github.com/tong-io) | 更新时间 | 2026-08-21 |

## 一句话介绍

> TongFlow — multimodal workflow studio and engine (canvas + Python plugin engine) and dsh-tongflow, the DeepSeek Harness studio plugin

## 详细介绍

With TongFlow, you can expand your imagination and stretch your ideas with generative AI, just have a try now!

## ✨ 核心特性

- **macOS (Universal — Apple Silicon & Intel):** [TongFlow-mac-universal.dmg](https://github.com/tong-io/tongflow/releases/latest/download/TongFlow-mac-universal.
- **Windows:** [TongFlow-win-x64.msi](https://github.com/tong-io/tongflow/releases/latest/download/TongFlow-win-x64.msi)

## 📦 安装

```bash
pnpm install
pnpm plugins:install   # clone official plugins into plugins/
pnpm start:prod        # builds once, then serves at http://localhost:3000
```

## 🚀 快速开始

```bash
docker run -d -p 3000:3000 \
  -v tongflow-data:/data -v tongflow-plugins:/plugins \
  ghcr.io/tong-io/tongflow:latest
```

## 📚 更多信息

**Demo Examples**

With TongFlow, you can expand your imagination and stretch your ideas with generative AI, just have a try now!

**Step 1 — Install the desktop app**

Download the installer for your platform, install it, and open it. All builds are on the [Releases](https://github.com/tong-io/tongflow/releases/latest) page. > **macOS:** the builds are not yet notarized with Apple, so Gatekeeper will block the first launch ("TongFlow is damaged and can't be opened"). After moving the app to Applications, clear the quarantine flag once and it opens normally: > > 

**1 — Install plugins**

Open the **plugin manager** (the blocks icon, top-right) and install what you need. Newly installed plugins are usable immediately, no restart. To run the preloaded **example workflow** (text → image → fusion → video), install these three plugins: These run on [Modal](https://modal.com) (up to **$30/month** of free GPU compute). Add `MODAL_TOKEN_ID` / `MODAL_TOKEN_SECRET` in **Settings**; create a

**2 — Configure credentials**

Open **Settings** (the gear icon, top-right) and add the environment variables your plugins need — e.g. `OPENAI_API_KEY` for the API plugins, or the credentials your GPU/CPU plugins require. > **Plugin credentials live in Settings.** TongFlow is platform-agnostic and hardcodes no provider: the Settings dialog is a generic key/value editor for environment variables passed to plugins. Each plugin's 

## 🔗 链接

- [GitHub 仓库](https://github.com/tong-io/tongflow)
- [完整 README](https://github.com/tong-io/tongflow#readme)
- [返回tongflow所在分类](../workflows.md)
