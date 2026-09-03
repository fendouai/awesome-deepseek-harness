---
title: "whale-girl"
description: "Desktop pet plugin (QQ-pet style) floating at the bottom-right of the DSH Web GUI: draggable, feedable and playable."
keywords: "whale-girl, ui, plugin, deepseek harness, dsh"
---
# whale-girl

> ⭐ **260** · ✅ active · plugin · ⬆️ +8 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 260 | Status | ✅ active |
| Author | [vlln](https://github.com/vlln) | Updated | 2026-08-19 |
| Subcategory | 🐋 Desktop pets | Capabilities | ui |

## One-liner

> Desktop pet plugin (QQ-pet style) floating at the bottom-right of the DSH Web GUI: draggable, feedable and playable.

## About

Official **bundle plugin** (`dsh.bundle` + `dsh.client` in root `package.json`), managed via the official profile: dsh plugin --profile web add "github:vlln/whale-girl#main" # single-line git source (build artifacts committed)

## 📦 Install

```bash
dsh plugin --profile web add "github:vlln/whale-girl#main"   # single-line git source (build artifacts committed)
# or npm source: dsh plugin --profile web add whale-girl@0.1.0
# or local directory: dsh plugin --profile web add <path-to-whale-girl>
```

## 🚀 Quick Start

```bash
whale-girl:
  enabled: true      # web render toggle (false disables the in-page pet while a desktop companion runs)
  size: 110          # pet size px (64–160)
  opacity: 1         # default opacity (0.2–1)
  walk:
    enabled: true    # wandering toggle
  sleepAfterMs: 60000
```

## 📚 Learn more

**Installation**

Official **bundle plugin** (`dsh.bundle` + `dsh.client` in root `package.json`), managed via the official profile: dsh plugin --profile web add "github:vlln/whale-girl#main" # single-line git source (build artifacts committed)

**Usage**

Full state machine (priorities / transitions / triggers): [docs/state-machine.md](docs/state-machine.md).

**Configuration**

**Settings → Plugins → Whale Girl** (in-page card): the high-frequency subset — show on page, size, opacity, wandering, sleep delay, and the feed/play reply pools (one per line). Changes **save and apply live, no restart**. The full option list stays in the `whale-girl:` section of `<dshHome>/settings.yaml` (advanced/additional knobs like window durations): whale-girl: enabled: true # web render t

## 🔗 Links

- [GitHub Repository](https://github.com/vlln/whale-girl)
- [Full README](https://github.com/vlln/whale-girl#readme)
- [Back to the Plugins list](../plugins.md)
