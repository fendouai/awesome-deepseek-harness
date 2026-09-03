---
title: "whale-girl"
description: "QQ 宠物形态桌面宠物：DSH Web 右下角悬浮，可拖拽/投喂/玩耍。"
keywords: "whale-girl, ui, plugin, deepseek harness, dsh"
---
# whale-girl

> ⭐ **260** · ✅ 活跃 · 插件 · 近期 ⬆️ +8

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 260 | 状态 | ✅ 活跃 |
| 作者 | [vlln](https://github.com/vlln) | 更新时间 | 2026-08-19 |
| 子分类 | 🐋 桌面宠物 | 能力 | ui |

## 一句话介绍

> QQ 宠物形态桌面宠物：DSH Web 右下角悬浮，可拖拽/投喂/玩耍。

## 详细介绍

Official **bundle plugin** (`dsh.bundle` + `dsh.client` in root `package.json`), managed via the official profile: dsh plugin --profile web add "github:vlln/whale-girl#main" # single-line git source (build artifacts committed)

## 📦 安装

```bash
dsh plugin --profile web add "github:vlln/whale-girl#main"   # single-line git source (build artifacts committed)
# or npm source: dsh plugin --profile web add whale-girl@0.1.0
# or local directory: dsh plugin --profile web add <path-to-whale-girl>
```

## 🚀 快速开始

```bash
whale-girl:
  enabled: true      # web render toggle (false disables the in-page pet while a desktop companion runs)
  size: 110          # pet size px (64–160)
  opacity: 1         # default opacity (0.2–1)
  walk:
    enabled: true    # wandering toggle
  sleepAfterMs: 60000
```

## 📚 更多信息

**Installation**

Official **bundle plugin** (`dsh.bundle` + `dsh.client` in root `package.json`), managed via the official profile: dsh plugin --profile web add "github:vlln/whale-girl#main" # single-line git source (build artifacts committed)

**Usage**

Full state machine (priorities / transitions / triggers): [docs/state-machine.md](docs/state-machine.md).

**Configuration**

**Settings → Plugins → Whale Girl** (in-page card): the high-frequency subset — show on page, size, opacity, wandering, sleep delay, and the feed/play reply pools (one per line). Changes **save and apply live, no restart**. The full option list stays in the `whale-girl:` section of `<dshHome>/settings.yaml` (advanced/additional knobs like window durations): whale-girl: enabled: true # web render t

## 🔗 链接

- [GitHub 仓库](https://github.com/vlln/whale-girl)
- [完整 README](https://github.com/vlln/whale-girl#readme)
- [返回whale-girl所在分类](../plugins.md)
