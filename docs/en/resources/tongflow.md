---
title: "tongflow"
description: "TongFlow — multimodal workflow studio and engine (canvas + Python plugin engine) and dsh-tongflow, the DeepSeek Harness studio plugin"
keywords: "tongflow, workflow, coding, multimodal, deepseek harness, dsh"
---
# tongflow

> ⭐ **902** · ✅ active · workflow · ⬆️ +16 recently

| | | | |
|---|---|---|---|
| Type | workflow | Category | Workflows |
| Stars | ⭐ 902 | Status | ✅ active |
| Author | [tong-io](https://github.com/tong-io) | Updated | 2026-08-21 |

## One-liner

> TongFlow — multimodal workflow studio and engine (canvas + Python plugin engine) and dsh-tongflow, the DeepSeek Harness studio plugin

## About

With TongFlow, you can expand your imagination and stretch your ideas with generative AI, just have a try now!

## ✨ Key Features

- **macOS (Universal — Apple Silicon & Intel):** [TongFlow-mac-universal.dmg](https://github.com/tong-io/tongflow/releases/latest/download/TongFlow-mac-universal.
- **Windows:** [TongFlow-win-x64.msi](https://github.com/tong-io/tongflow/releases/latest/download/TongFlow-win-x64.msi)

## 📦 Install

```bash
pnpm install
pnpm plugins:install   # clone official plugins into plugins/
pnpm start:prod        # builds once, then serves at http://localhost:3000
```

## 🚀 Quick Start

```bash
docker run -d -p 3000:3000 \
  -v tongflow-data:/data -v tongflow-plugins:/plugins \
  ghcr.io/tong-io/tongflow:latest
```

## 📚 Learn more

**Demo Examples**

With TongFlow, you can expand your imagination and stretch your ideas with generative AI, just have a try now!

**Step 1 — Install the desktop app**

Download the installer for your platform, install it, and open it. All builds are on the [Releases](https://github.com/tong-io/tongflow/releases/latest) page. > **macOS:** the builds are not yet notarized with Apple, so Gatekeeper will block the first launch ("TongFlow is damaged and can't be opened"). After moving the app to Applications, clear the quarantine flag once and it opens normally: > > 

**1 — Install plugins**

Open the **plugin manager** (the blocks icon, top-right) and install what you need. Newly installed plugins are usable immediately, no restart. To run the preloaded **example workflow** (text → image → fusion → video), install these three plugins: These run on [Modal](https://modal.com) (up to **$30/month** of free GPU compute). Add `MODAL_TOKEN_ID` / `MODAL_TOKEN_SECRET` in **Settings**; create a

**2 — Configure credentials**

Open **Settings** (the gear icon, top-right) and add the environment variables your plugins need — e.g. `OPENAI_API_KEY` for the API plugins, or the credentials your GPU/CPU plugins require. > **Plugin credentials live in Settings.** TongFlow is platform-agnostic and hardcodes no provider: the Settings dialog is a generic key/value editor for environment variables passed to plugins. Each plugin's 

## 🔗 Links

- [GitHub Repository](https://github.com/tong-io/tongflow)
- [Full README](https://github.com/tong-io/tongflow#readme)
- [Back to the Workflows & Automation list](../workflows.md)
