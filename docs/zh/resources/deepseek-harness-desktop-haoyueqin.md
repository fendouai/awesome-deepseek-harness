---
title: "deepseek-harness-desktop"
description: "A desktop shell for DeepSeek Harness — the pluggable AI agent harness from DeepSeek. Wrap the official dsh web UI into a native-feeling, always-on desktop app. / 为 DeepSeek Harness（DeepSeek 开源的可插拔 AI Agent harness）打造的桌面应用壳，把官方 dsh web 界面包装成原生质感、常驻后台的桌面应用。"
keywords: "deepseek-harness-desktop, desktop, client, coding, multi-agent, ui, deepseek harness, dsh"
---
# deepseek-harness-desktop

> ⭐ **6** · ✅ 活跃 · 客户端

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [HaoyueQin](https://github.com/HaoyueQin) | 更新时间 | 2026-08-21 |

## 一句话介绍

> A desktop shell for DeepSeek Harness — the pluggable AI agent harness from DeepSeek. Wrap the official dsh web UI into a native-feeling, always-on desktop app. / 为 DeepSeek Harness（DeepSeek 开源的可插拔 AI Agent harness）打造的桌面应用壳，把官方 dsh web 界面包装成原生质感、常驻后台的桌面应用。

## 详细介绍

A desktop shell for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) — the pluggable AI agent harness from DeepSeek. Wrap the official `dsh web` UI into a native-feeling, always-on desktop app, **reusing the `dsh` CLI you already have**.

## ✨ 核心特性

- **Dual backend sources** — run the `dsh` from your npm global install (stable channel) or from a local git checkout (any version, including pre-releases), switc
- **Zero-intrusion wrapper** — spawns the chosen `dsh` as a child process (`dsh web`), loads its localhost UI; the harness source is never modified. One dsh share
- **Source mode without terminals** — pick a folder and the shell drives everything: clone the official repo, run `pnpm install` + `pnpm build` with live logs, va
- **Source-mode updates like npm's** — check the upstream tags, see "current → latest", then one click checks out the tag, reinstalls, rebuilds and restarts the b
- **One proxy for every update channel** — a single proxy setting covers git (clone/fetch), pnpm (install/build) and npm (check/upgrade); git uses per-invocation 
- **First-run setup page** — no dsh detected? The app offers a copyable install command, a one-click in-app install, or the source-mode path (clone + prepare), th

## 📦 安装

```bash
npm install        # installs electron 43 + toolchain
npm run dev        # dev mode: system Node + your chosen backend (npm or source dir)
```

## 🚀 快速开始

```bash
> printf "electron.exe" > node_modules/electron/path.txt
> # and unzip the archive into node_modules/electron/dist/
>
```

## 🔗 链接

- [GitHub 仓库](https://github.com/HaoyueQin/deepseek-harness-desktop)
- [完整 README](https://github.com/HaoyueQin/deepseek-harness-desktop#readme)
- [返回deepseek-harness-desktop所在分类](../clients.md)
