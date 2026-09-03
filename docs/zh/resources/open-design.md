---
title: "open-design"
description: "🎨 The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode / Hermes & 20+ CLIs via BYOK."
keywords: "open-design, desktop, client, coding, multi-agent, multimodal, deepseek harness, dsh"
---
# open-design

> ⭐ **90,033** · ✅ 活跃 · 客户端 · 近期 ⬆️ +429

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 90,033 | 状态 | ✅ 活跃 |
| 作者 | [nexu-io](https://github.com/nexu-io) | 更新时间 | 2026-08-21 |

## 一句话介绍

> 🎨 The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode / Hermes & 20+ CLIs via BYOK.

## 详细介绍

🎨 **The open-source Claude Design alternative.**  🖥️ **Local-first native desktop app for macOS and Windows.**  ⚡ **Composable skills, brand-grade `DESIGN.md` design systems, and ready-to-use plugins.**  🖼️ Generates **web · desktop · mobile prototypes**, **live dashboards / artifacts**, **decks**, **images**, **video**, plus **HyperFrames** motion graphics. 🔒 Sandboxed iframe preview · HTML / PDF / PPTX / MP4 export.  🤖 **Runs on DeepSeek Harness (`dsh`) · Claude Code · OpenClaw · Codex · Cursor · OpenCode · Qwen · Copilot · Amp · Hermes · Kimi · Antigravity and 26 distinct local CLI executables**, or any OpenAI-compatible endpoint via BYOK. OpenDesign is what you get when the **agent-native** loop Anthropic shipped with Claude Design — discover the brief, lock the dir

## ✨ 核心特性

- 🤖 **Run in any coding agent** — [Claude Code](docs/agent-adapters.md), Codex, Cursor, Copilot, [OpenClaw](https://github.com/openclaw/openclaw), [Antigravity](h
- 🔁 **Migrate Figma / Pencil workflows** → React, Next.js, or Vue source. See [`od-figma-migration`](plugins/_official/scenarios/od-figma-migration/).
- 🛠️ **Refresh an existing codebase to a brand spec** — point a plugin at a `git` repo + `DESIGN.md`, get a PR. See [`od-code-migration`](plugins/_official/scenar
- 💾 **Persist custom workflows** — your team's reusable templates sit next to the shipped ones.

## 📦 安装

```bash
git clone https://github.com/nexu-io/open-design.git
cd open-design/deploy
cp .env.example .env
echo "OD_API_TOKEN=$(openssl rand -hex 32)" >> .env
docker compose up -d
# open http://127.0.0.1:7456
```

## 🚀 快速开始

```bash
git clone https://github.com/nexu-io/open-design.git
cd open-design
corepack enable && pnpm install
pnpm tools-dev run web
```

## 📚 更多信息

**Demo**

Four core product categories, all rendered by a coding agent running on your laptop. Click a thumbnail to see the real example.

**🖥️ Download the desktop app (recommended — zero config)**

The fastest way to use OpenDesign. No Node, no pnpm, no clone. After install: the app auto-detects every coding-agent CLI on your `PATH`, loads 100+ functional skills, the separate rendering-template catalog, and 151 design systems, and lets you type a brief in the entry view.

**🤖 Install into your coding agent (no UI)**

You can use OpenDesign without ever opening the GUI — call it as a skill, plugin, or MCP server inside Claude Code, Codex, Cursor, Copilot, OpenClaw, Antigravity, Hermes, Kimi, and more. If you installed the macOS desktop app via the DMG or Homebrew cask, your shell may still resolve `od` to Apple's built-in `/usr/bin/od` octal-dump utility. In that case, open **Settings → MCP server** in the desk

**Architecture**

┌────────────────── browser (Next.js 16) / Electron shell ──────────────┐ │ chat · file workspace · iframe preview · settings · import · MCP │ └──────────────┬─────────────────────────────────────┬─────────────────┘ │ /api/* │ ▼ ▼ ┌─────────────────────────────────┐ /api/proxy/{provider}/stream (SSE) │ local daemon (Express+SQLite) │ ─→ any OpenAI-compatible BYOK, │ │ SSRF-guarded at the edge │ /a

## 🔗 链接

- [GitHub 仓库](https://github.com/nexu-io/open-design)
- [完整 README](https://github.com/nexu-io/open-design#readme)
- [返回open-design所在分类](../clients.md)
