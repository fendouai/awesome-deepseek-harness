---
title: "dsh-status-rotator"
description: "Replaces the 'Deep diving…' turn-status label with phase-aware typewriter messages."
keywords: "dsh-status-rotator, ui, plugin, deepseek harness, dsh"
---
# dsh-status-rotator

> ⭐ **42** · ✅ active · plugin · ⬆️ +3 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 42 | Status | ✅ active |
| Author | [01Virex](https://github.com/01Virex) | Updated | 2026-08-21 |
| Subcategory | 📊 Status & stats | Capabilities | ui |

## One-liner

> Replaces the 'Deep diving…' turn-status label with phase-aware typewriter messages.

## About

dsh plugin --profile web add dsh-status-rotator **v0.10.0 — stable release** Replaces the `Deep diving...` status line in the DeepSeek Harness (dsh) Web UI's turn footer with your own text: phase-aware switching, typewriter output, animated rainbow gradient (optional), timed rotation, **template placeholders with live values** (`{elapsed}`, `{phase}`, `{model}`, `{tps}`…), optional **browser tab title** rotation, **a live status pill** (model, phase, elapsed, tokens/s — fed by the same real-time engine), **Danmaku** (your phrases float across the page behind the UI like bullet-screen comments on video sites), and **presets with time-of-day scheduling**. The elapsed-time clock (which appears after 15 seconds) is untouched.

## ✨ Key Features

- **Phase-aware**: three sets of phrases — `thinking` (just started) / `running` (after 15s) / `long` (past the threshold). Switches immediately when the clock ap
- **Typewriter effect**: phrases are typed out character by character, speed configurable, 0 disables it;
- **Template placeholders**: `{elapsed}` (live, refreshed every `liveTickMs`), `{phase}`, `{phaseLabel}`, `{locale}`, `{date}`, `{time}`, plus live-engine values 
- **Real-time status engine**: subscribes to the dsh session snapshot (session list, conversation snapshot, model RPC, DOM clock fallback) — one source feeding th
- **Live status pill**: a floating pill in the official `shell.overlay` seat, template-driven live info (`{model} · {phaseLabel} · {elapsed} · ⚡{tps} tok/s`), pos
- **Browser tab title**: rotate `document.title` through your own templates (`⏳ {phase} {elapsed}`), restore the original title when idle (configurable);
- **Presets & scheduling**: multiple named phrase banks with their own config, switchable from the settings page or automatically by time-of-day / weekday rules;
- **Rainbow gradient**: text rendered with an animated gradient, colors and speed configurable, can be turned off with one switch;

## 📦 Install

```bash
# One-line install
dsh plugin --profile web add dsh-status-rotator
```

## 🚀 Quick Start

```bash
- insert:
       - id: status-rotator
         name: dsh-status-rotator
```

## 📚 Learn more

**One-line install**

dsh plugin --profile web add dsh-status-rotator **v0.10.0 — stable release** > ⭐ **If this made you smile, give it a star** — it keeps the memes flowing. Replaces the `Deep diving...` status line in the DeepSeek Harness (dsh) Web UI's turn footer with your own text: phase-aware switching, typewriter output, animated rainbow gradient (optional), timed rotation, **template placeholders with live val

**Installation**

Two ways to install: the recommended `dsh plugin add` command, or the manual copy. Either way, you need to restart `dsh web` once after first install.

**Option B: manual install**

1. Put this project directory under your profile's node_modules (default `C:\Users\<you>\.dsh\profiles\node_modules\dsh-status-rotator\`); 2. Insert the following into the profile's `cordis.patch.yml`: ```yaml - insert: - id: status-rotator name: dsh-status-rotator ``` 3. Run `node gen-config.cjs` to initialize the local `config.json` (copied from `config.example.json`); 4. Restart `dsh web` and h

**Configuration**

Phrases are fully separated from the source code and live in JSON config files. There are two config files at the project root: **Auto-loading (default)**: the plugin's node half registers an HTTP route (`/plugins/dsh-status-rotator/config.json`) that serves the `config.json` next to the plugin (read from disk on every request). The browser fetches it automatically by default, and **while the page

## 🔗 Links

- [GitHub Repository](https://github.com/01Virex/dsh-status-rotator)
- [Full README](https://github.com/01Virex/dsh-status-rotator#readme)
- [Back to the Plugins list](../plugins.md)
