# Awesome DeepSeek Harness 🐋

> A curated ecosystem of **plugins, skills, workflows, agents, clients, tools and examples** for the official [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness).

[简体中文](README.zh-CN.md) · [MkDocs 站点](https://deepseekserver.com)

DeepSeek Harness (`dsh`) is DeepSeek AI's open-source agent harness built around a simple idea:

> **Everything is a Plugin.**

This repository tracks the ecosystem around the official `deepseek-ai/deepseek-harness` project — not just plugins, but the **entire Harness ecosystem**:

**Plugins · Skills · Workflows · Agents · Tools · Desktop · TUI · Integrations · Examples · Tutorials**

**✨ Built-in features:** 🔥 **Trending** (auto-ranked Top 10 per category + global Top 20) · 🧮 machine-readable registry (`data/*.json`) · ✅ live-verified links · 🌐 bilingual (EN / 简体中文) · 📊 weekly auto-refresh

> ⚠️ DeepSeek Harness is currently in developer preview and evolving rapidly. Compatibility may change. Always check the linked repository before installation.
>
> This list is **community-maintained and independently verified** — many older registries (e.g. the former `dsh-external` org) contain dead links. Every entry here was checked against the live GitHub API on 2026-08-14.

---

## Contents

- [Official Resources](#official-resources)
- [Getting Started](#getting-started)
- [🔥 Trending](#-trending)
- [Plugins](#plugins)
- [Skills](#skills)
- [Workflows & Automation](#workflows--automation)
- [Agents & Multi-Agent](#agents--multi-agent)
- [Clients (Desktop & TUI)](#clients-desktop--tui)
- [MCP & Integrations](#mcp--integrations)
- [Examples & Starters](#examples--starters)
- [Tutorials & Learning](#tutorials--learning)
- [Awesome Lists & Registries](#awesome-lists--registries)
- [Related Agent Harnesses](#related-agent-harnesses)
- [Research](#research)
- [Project Structure](#project-structure)
- [Quality Levels](#quality-levels)
- [Submit a Project](#submit-a-project)
- [Not the Same Project](#not-the-same-project)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)

---

# Official Resources

### DeepSeek Harness

**Repository** — https://github.com/deepseek-ai/deepseek-harness

Official open-source agent harness developed by DeepSeek AI. MIT licensed, built on [Cordis](https://github.com/cordiverse/cordis).

### Install

```bash
npx @deepseek-ai/dsh web
```

Run from source:

```bash
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness

pnpm install
pnpm run build
pnpm dsh web
```

Default Web UI:

```text
http://127.0.0.1:3080
```

### Plugin discovery

Official ecosystem convention — add the topic to your plugin repo:

```text
GitHub topic: dsh-plugin
```

Browse: https://github.com/topics/dsh-plugin

### Architecture

DeepSeek Harness is built on **Cordis** (a meta-framework of spatiotemporal composability). Core concepts include:

* Plugin-based architecture · Profiles · Bundles · Tools · Model adapters
* Sessions · Agent loops · Sandboxes · Background jobs · Subagents
* Web UI · Headless execution

---

# Getting Started

## Run DSH

```bash
npx @deepseek-ai/dsh web
```

## Install a plugin

```bash
dsh plugin --profile web add <package>
```

Restart the profile if required:

```bash
dsh web
```

Plugins intended to become active DSH bundles should expose the corresponding `dsh.bundle` metadata. Manage installed plugins under **Settings → Plugins**.

---

# 🔥 Trending

> **✨ Built-in Trending.** This directory is not a static list — it ships with a live ranking engine:

> * **🔥 Top 10 per category** — every section below auto-ranks its entries by live GitHub star count, so you instantly see what the community cares about
> * **🌍 Global Top 20** — an all-ecosystem ranking on the [docs site](https://deepseekserver.com) front page
> * **♻️ Auto-refresh** — star counts and statuses are refreshed automatically (`scripts/update-metadata.py` + weekly GitHub Action); ranking is re-computed on every build
> * **🧭 Signals roadmap** — trending (star growth / commits / releases), popular (long-term adoption), new (recently discovered) and verified rankings are planned in the [Roadmap](#roadmap)

> Hot projects right now (top by stars, as of 2026-08-14):

| # | Project | ⭐ | Why it matters |
|---|---|---|---|
| 1 | [dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | 1.7k | Largest plugin/skin collection: task board, git graph, pets, token stats |
| 2 | [dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) | 793 | Claude Code-style fullscreen terminal plugin |
| 3 | [DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) | 684 | Workbench-style sidebar: files, terminal, Git, subagents |
| 4 | [dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) | 506 | Whale-girl skin series |
| 5 | [DeepSeek Harness Orange Book](https://github.com/alchaincyf/deepseek-harness-orange-book) | 465 | First-hand community book: system prompts, startup checklist, raw logs |
| 6 | [dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) | 302 | Vision for text-only models: image Q&A, OCR, UI restoration |
| 7 | [dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) | 222 | Multi-agent team extensions |
| 8 | [oh-dsh](https://github.com/hust-open-atom-club/oh-dsh) | 160 | One-stop community distribution (TUI + desktop + Web UI) |
| 9 | [dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) | 167 | From 0 to 1 handbook (CN + EN PDF) |
| 10 | [dsh-at-file](https://github.com/omdsh-dev/dsh-at-file) | 116 | Codex-style `@file` mentions |

---

# Plugins

> The DSH plugin ecosystem is the heart of the Harness. 111 curated plugins below, grouped by category — sorted by stars within each group. A plugin adds **runtime capability**; a skill adds reusable knowledge (see [Skills](#skills)).

<!-- AUTO:resources:START -->
### Plugins


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [petdex](https://github.com/crafter-station/petdex) | ⭐3,777 | A public gallery of animated pets for Codex, Claude Code, DeepSeek Harness, Hermes, OpenCode, Gemini CLI, and more. | ✅ active |
| 2 | [dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | ⭐1,697 | Large plugin and skin collection for DSH Web: task board, git graph, side panels, remote/mobile UI, pets, token stats and themes. | ✅ active |
| 3 | [modlens](https://github.com/liustack/modlens) | ⭐1,158 | The first vision plugin for DeepSeek Harness and the vision bridge for every text-only coding agent: paste an image and it works. | ✅ active |
| 4 | [DSH Better Sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) | ⭐684 | Workbench-style sidebar: file viewer/editor, terminal, Git, subagents and plugin-extensible tabs. | ✅ active |
| 5 | [museai](https://github.com/yejiming/MuseAI) | ⭐538 | 创建你的 AI 角色，进入你的故事世界。和角色聊天、冒险、穿书，让每一次互动都留下羁绊（支持 DeepSeek Harness 插件，欢迎使用） | ✅ active |
| 6 | [dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) | ⭐506 | Whale-girl skin series for DSH Web (CC BY-NC-SA 4.0). | ✅ active |
| 7 | [dsh-ads](https://github.com/Nagi-ovo/dsh-ads) | ⭐309 | Joke plugin: 2005 Chinese-web-style ad layer with sidebar banners, in-chat feed ads and corner popups. | ✅ active |
| 8 | [dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) | ⭐302 | Vision toolkit for text-only models: intent-aware image Q&A, long-screenshot OCR, UI restoration, grounding and pixel diff. | ✅ active |
| 9 | [whale-girl](https://github.com/vlln/whale-girl) | ⭐118 | Desktop pet plugin (QQ-pet style) floating at the bottom-right of the DSH Web GUI: draggable, feedable and playable. | ✅ active |
| 10 | [dsh-at-file](https://github.com/omdsh-dev/dsh-at-file) | ⭐116 | Codex-style @file mentions inside the DSH composer: search workspace files and attach their contents to prompts. | ✅ active |

#### Complete list (141)

- [petdex](https://github.com/crafter-station/petdex) ⭐3,777 — A public gallery of animated pets for Codex, Claude Code, DeepSeek Harness, Hermes, OpenCode, Gemini CLI, and more. (✅ active)
- [dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) ⭐1,697 — Large plugin and skin collection for DSH Web: task board, git graph, side panels, remote/mobile UI, pets, token stats and themes. (✅ active)
- [modlens](https://github.com/liustack/modlens) ⭐1,158 — The first vision plugin for DeepSeek Harness and the vision bridge for every text-only coding agent: paste an image and it works. (✅ active)
- [DSH Better Sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) ⭐684 — Workbench-style sidebar: file viewer/editor, terminal, Git, subagents and plugin-extensible tabs. (✅ active)
- [museai](https://github.com/yejiming/MuseAI) ⭐538 — 创建你的 AI 角色，进入你的故事世界。和角色聊天、冒险、穿书，让每一次互动都留下羁绊（支持 DeepSeek Harness 插件，欢迎使用） (✅ active)
- [dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) ⭐506 — Whale-girl skin series for DSH Web (CC BY-NC-SA 4.0). (✅ active)
- [dsh-ads](https://github.com/Nagi-ovo/dsh-ads) ⭐309 — Joke plugin: 2005 Chinese-web-style ad layer with sidebar banners, in-chat feed ads and corner popups. (✅ active)
- [dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) ⭐302 — Vision toolkit for text-only models: intent-aware image Q&A, long-screenshot OCR, UI restoration, grounding and pixel diff. (✅ active)
- [whale-girl](https://github.com/vlln/whale-girl) ⭐118 — Desktop pet plugin (QQ-pet style) floating at the bottom-right of the DSH Web GUI: draggable, feedable and playable. (✅ active)
- [dsh-at-file](https://github.com/omdsh-dev/dsh-at-file) ⭐116 — Codex-style @file mentions inside the DSH composer: search workspace files and attach their contents to prompts. (✅ active)
- [modsearch](https://github.com/liustack/modsearch) ⭐85 — Web plugin for DSH and the search bridge for every model without native web access. (✅ active)
- [dsh-browser](https://github.com/Lum1104/dsh-browser) ⭐78 — Chrome sidebar extension that lets DSH operate your browser directly, no vision capabilities required. (✅ active)
- [dsh-visualize](https://github.com/Nagi-ovo/dsh-visualize) ⭐74 — Interactive HTML UI rendered directly in conversation with streaming preview and sandbox rendering. (✅ active)
- [dsh-genui](https://github.com/omdsh-dev/dsh-genui) ⭐71 — Generative UI inside conversations: layouts, charts, forms, quizzes, Mermaid and interactive events rendered inline. (✅ active)
- [dsh-find-plugins](https://github.com/Nagi-ovo/dsh-find-plugins) ⭐67 — Plugin discovery utility for the DSH ecosystem. (✅ active)
- [dsh-memory-evolve](https://github.com/csyangwen/dsh-memory-evolve) ⭐47 — Cross-session long-term memory + background self-evolution: five-track memory, git-branch awareness, in-turn self-review and skill evolution. (✅ active)
- [dsh-annotation](https://github.com/omdsh-dev/dsh-annotation) ⭐39 — Select text in DSH Web, annotate it and send the annotation with your message; replies cross-reference each annotation. (✅ active)
- [dsh-open-in-vscode](https://github.com/omdsh-dev/dsh-open-in-vscode) ⭐39 — Open DSH workspace directories/files directly in VS Code from the web GUI. (✅ active)
- [dsh-notification](https://github.com/omdsh-dev/dsh-notification) ⭐37 — Desktop notifications for turn completions with per-outcome controls and include/exclude keyword filters. (✅ active)
- [dsh-turn-rewind](https://github.com/Anionex/dsh-turn-rewind) ⭐35 — Rewind conversation and workspace state, powered by a persistent change ledger. (✅ active)
- [dsh-vision-router](https://github.com/ysr666/dsh-vision-router) ⭐29 — Eyes for text-only agents: built-in free keyless vision chain plus pixel-level tools (Q&A, grounding, crop, OCR, SVG trace). (✅ active)
- [DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) ⭐28 — Browse, install and update every GitHub topic:dsh-plugin plugin from the DSH Web GUI. (✅ active)
- [ui-status-label](https://github.com/alingalingling/ui-status-label) ⭐28 — Customize the whale's 'Deep diving' status label into anything you want. (✅ active)
- [dsh-ui-whale](https://github.com/lhh010/dsh-ui-whale) ⭐27 — Hand-drawn pixel whale companion in the session title bar: blinks, wags its tail, spouts water when a turn completes. (✅ active)
- [dsh-custom-tool](https://github.com/omdsh-dev/dsh-custom-tool) ⭐22 — Create and manage sandboxed JavaScript tools for DSH with a Monaco editor and model-driven tool lists. (✅ active)
- [dskin](https://github.com/dancingmemory/dskin) ⭐22 — Cartoon pixel skin plugin for DSH Web GUI: pixel pets that walk, blink and jump over the original interface. (✅ active)
- [dsh-chat-import](https://github.com/Nwflower/dsh-chat-import) ⭐20 — Import conversation history from Claude Code, Codex, ChatGPT, Cursor, Gemini, Reasonix and OpenCode into resumable DSH sessions. (✅ active)
- [deepseek-harness-skin](https://github.com/HeiGeAi/deepseek-harness-skin) ⭐18 — Skin system with 21 built-in themes plus one-image custom skin generation, contrast-validated at build time. (✅ active)
- [dsh-computer-use](https://github.com/Anionex/dsh-computer-use) ⭐18 — 为 DeepSeek Harness 提供电脑控制插件：新鲜 Accessibility 观测、过期状态拒绝、作用域权限与安全输入（目前支持macos）｜Accessibility-first macOS Computer Use bundle for DSH with fresh observations, stale-state rejection, scoped permissions, and safe input. (✅ active)
- [dsh-side-panel](https://github.com/ccq1/dsh-side-panel) ⭐18 — Compact side panel with a file browser, terminal and Git review. (✅ active)
- [anysearch-dsh](https://github.com/anysearch-team/anysearch-dsh) ⭐17 — AnySearch web search provider and advanced search tools for DeepSeek Harness. (✅ active)
- [deepseek-harness-snowsalt](https://github.com/KYZHXL/deepseek-harness-snowsalt) ⭐17 — Snow-salt themed skin for DeepSeek Harness. (✅ active)
- [dsh-plugin-check](https://github.com/omdsh-dev/dsh-plugin-check) ⭐17 — Plugin health checks: manifest protocol, patch format, build pitfalls and hub listing status, zero-dependency read-only. (✅ active)
- [dsh-message-edit](https://github.com/Moeblack/dsh-message-edit) ⭐16 — Branch-based message editing, reroll, retry and version timeline. (✅ active)
- [dsh-share](https://github.com/hellodigua/dsh-share) ⭐16 — One-click conversation sharing for DSH. (✅ active)
- [dsh-usage-stats](https://github.com/Ychris12138/dsh-usage-stats) ⭐16 — Token usage heatmap, per-model breakdowns, and DeepSeek account balance for the DeepSeek Harness Web GUI (dsh web). (✅ active)
- [dsh-vision (william-jin-cmu)](https://github.com/william-jin-cmu/dsh-vision) ⭐16 — Vision bridge: view_image tool over any OpenAI-compatible VLM, defaulting to Zhipu's free tier. (✅ active)
- [dsh-toolkit](https://github.com/omdsh-dev/dsh-toolkit) ⭐15 — Zero-dependency tool suite: calculator, CSV, diff, encoding, JSON, Markdown, regex and time utilities. (✅ active)
- [dsh-group-photo](https://github.com/SenmuuuuW/dsh-group-photo) ⭐14 — DSH 内测收官合影墙：GitHub OAuth 零权限登录 + 冻结白名单校验的拍立得合影站（含 DSH Skill 包装） (✅ active)
- [dsh-navbar](https://github.com/vlln/dsh-navbar) ⭐14 — DSH 插件：对话节点导航条（右缘节点串快速跳转 user 消息）。官方 bundle 插件，dsh plugin --profile web add 安装 (✅ active)
- [dsh-web-review](https://github.com/CanglongCl/dsh-web-review) ⭐13 — DeepSeek Harness Web GUI 的网页预览与元素批注插件，让 AI 根据可视化反馈直接修改前端源码。 (✅ active)
- [dsh-focus-chat](https://github.com/dingyi222666/dsh-focus-chat) ⭐12 — 为 dsh 提供新的「聚焦会话」精简会话视图，更轻松易于阅读，只关注最终产出结果。 (✅ active)
- [dsh-kun-like-pet](https://github.com/liyupi/dsh-kun-like-pet) ⭐12 — Kun Like 桌宠 —— DeepSeek Harness 桌面宠物插件：右下角小坤宠随 Agent 工作状态切换 9 种动作，任务完成播放「你干嘛~哎哟」 (✅ active)
- [dsh-market](https://github.com/dsh-market/dsh-market) ⭐12 — Visual plugin market inside DeepSeek Harness: browse, search and one-click install. (✅ active)
- [dsh-minigames](https://github.com/lhh010/dsh-minigames) ⭐12 — DSH Web UI 右侧小游戏面板：18 款离线小游戏（恐龙跳一跳 / 俄罗斯方块 / 坦克大战 / 扫雷 / 2048 / 数独 / 吃豆人 / 跟枪练习等），可扩展游戏注册表，等待模型回复或修 bug 时的摸鱼神器 (✅ active)
- [dsh-plugins-store](https://github.com/ZASENJC/dsh-plugins-store) ⭐12 — Static directory site that automatically collects and categorizes GitHub dsh-plugin topic projects. (✅ active)
- [ego-browser](https://github.com/Fisfzy/ego-browser) ⭐12 — Bring the ego-lite agent browser (Chromium for AI agents) into DSH with 13 structured tools. (✅ active)
- [DeepSeek-Harness-Web-Tools](https://github.com/tonyd2wild/DeepSeek-Harness-Web-Tools) ⭐11 — Free, keyless web_search and web_fetch for DSH, DuckDuckGo-backed with no signup. (✅ active)
- [dsh-balance-meter](https://github.com/Ghost011118/dsh-balance-meter) ⭐11 — DeepSeek account balance and session cost readout for the DeepSeek Harness Web GUI (✅ active)
- [dsh-emoji](https://github.com/hellodigua/dsh-emoji) ⭐11 — Let AI replies add custom emoji reactions. (✅ active)
- [dsh-find-plugin](https://github.com/awesome-dsh-plugin/dsh-find-plugin) ⭐11 — Agent-assisted plugin discovery: search the live GitHub dsh-plugin topic from inside DSH. (✅ active)
- [dsh-gomoku](https://github.com/omdsh-dev/dsh-gomoku) ⭐11 — Play Gomoku with AI inside DSH, or let two AIs battle to compare models. (✅ active)
- [dsh-mnemon](https://github.com/omdsh-dev/dsh-mnemon) ⭐11 — Three-tier local memory: runtime hot memory, project documents and long-term memory spaces, with supervised writeback. (✅ active)
- [dsh-sdk-platform-rs](https://github.com/kpn-dsh/dsh-sdk-platform-rs) ⭐11 — A Rust SDK to interact with the DSH Platform. This library provides convenient building blocks for services that need to connect to DSH Kafka, fetch tokens for various protocols, manage Prometheus metrics, and more. (✅ active)
- [dsh-web-plugin-manager](https://github.com/LX2000WASD/dsh-web-plugin-manager) ⭐11 — Manage plugins from the Web UI: view, live enable/disable, install/uninstall, env management and plugin market. (✅ active)
- [dsh-plugin-workshop](https://github.com/yyyyukari/dsh-plugin-workshop) ⭐10 — Steam Workshop-style plugin browser for the DSH Web UI: zero-server, GitHub-powered search and one-click install. (✅ active)
- [dsh-security-audit](https://github.com/omdsh-dev/dsh-security-audit) ⭐10 — DSH 本机安全审计插件：配置/插件来源/会话/网络暴露面，只读脱敏风险报告 (✅ active)
- [dsh-stock-market](https://github.com/AnacondaKC/dsh-stock-market) ⭐10 — Stock market data plugin (joke: fixes the bug where your account loses money while you code). (✅ active)
- [dsh-webui-market-plugin](https://github.com/Sanqi-normal/dsh-webui-market-plugin) ⭐10 — Community plugin market in the Web GUI: browse the awesome-dsh-plugin.com catalog and install/uninstall to a profile. (✅ active)
- [dsh-milestone](https://github.com/SnowCrescenter-tech/dsh-milestone) ⭐9 — Git-style milestone timeline rail: hover for metadata, click to jump to any message. (✅ active)
- [dsh-plugin-mineru](https://github.com/HuanLinOTO/dsh-plugin-mineru) ⭐9 — Expose MinerU document parsing to the model: PDF/images/DOCX/PPTX/XLSX to structured Markdown/JSON. (✅ active)
- [dsh-session-health](https://github.com/omdsh-dev/dsh-session-health) ⭐9 — Frame-level diagnostics for multi-frame zstd session files: torn/corrupted/empty session detection, zero-dependency read-only. (✅ active)
- [dsh-web-ui-notify](https://github.com/bill9109/dsh-web-ui-notify) ⭐9 — Adds desktop notification reminders to DSH. (✅ active)
- [deepseek-harness-SupportVisionModel](https://github.com/TryDing-T/deepseek-harness-SupportVisionModel) ⭐8 — Secondary development of deepseek-harness supporting a separately configured vision model for reading images. (✅ active)
- [DeepSeek-Harness-Vision-Tools](https://github.com/tonyd2wild/DeepSeek-Harness-Vision-Tools) ⭐8 — Vision proxy for chat: give DSH eyes with any text model plus any vision model. (✅ active)
- [dsh-mneme](https://github.com/modusensus/dsh-mneme) ⭐8 — Local cross-session memory with memory sovereignty: SQLite + human-editable Markdown mirror and background autoDream consolidation. (✅ active)
- [dsh-paste-input](https://github.com/lhh010/dsh-paste-input) ⭐8 — WebUI file input enhancement: Ctrl+V paste, drag & drop and file picker, copied into the session workspace. (✅ active)
- [billion-context-dsh](https://github.com/Tyan66666/billion-context-dsh) ⭐7 — Model-driven context compression (Active Context Pruning): the model decides when and what to compress. (✅ active)
- [DeepSeek-Harness-billing-plugin](https://github.com/WilliamLIiii/DeepSeek-Harness-billing-plugin) ⭐7 — Account balance plus per-model remaining-task estimator with a session cost ledger. (✅ active)
- [dsh-director-toolkit](https://github.com/lhmd/dsh-director-toolkit) ⭐7 — DSH Director Toolkit is a DeepSeek Harness plugin for 3D artists, technical designers, and creative coders. Paste a half-formed idea, a reference note, or a portfolio caption and get a compact direction pack for Blender, Three.js, Houdini, or C4D. (✅ active)
- [dsh-plugin-better-sidebar-plugin-office](https://github.com/HuanLinOTO/dsh-plugin-better-sidebar-plugin-office) ⭐7 — Office-suite preview (.docx/.xlsx/.pptx) for the Better Sidebar, as a standalone slim bundle. (✅ active)
- [dsh-plugin-pet-rs](https://github.com/HuanLinOTO/dsh-plugin-pet-rs) ⭐7 — Rust desktop pet: 5-state whale with dual SSE real-time push, transparent always-on-top window and system tray. (✅ active)
- [dsh-context-doctor](https://github.com/Zhenyu98/dsh-context-doctor) ⭐6 — Audits what actually enters every model request: token cost of AGENTS.md chains, skill catalogs and tool schemas, with duplicate/conflict detection. (✅ active)
- [dsh-diff-viewer](https://github.com/lehhair/dsh-diff-viewer) ⭐6 — PiUI-style Web diff viewer replacing the default diff view. (✅ active)
- [dsh-skin](https://github.com/KinGao294/dsh-skin) ⭐6 — Codex-style skin switcher plus custom translucent wallpaper with opacity/blur controls. (✅ active)
- [dsh-balance](https://github.com/crazywoola/dsh-balance) ⭐5 — DeepSeek Harness balance plugin for the Settings page. (✅ active)
- [dsh-deepcel](https://github.com/Small-tailqwq/dsh-deepcel) ⭐5 — Spreadsheet-style skin for DSH, mimicking Excel. (✅ active)
- [dsh-ohos-patch](https://github.com/shenjackyuanjie/dsh-ohos-patch) ⭐5 — 让deepseek harness能在 ohos上跑！ (✅ active)
- [dsh-plugin-d399](https://github.com/HuanLinOTO/dsh-plugin-d399) ⭐5 — Mini-game menu (Wordle, match-3, 192 parameterized games) that pops up while the model generates. (✅ active)
- [dsh-plugin-installer](https://github.com/Toukaiteio/dsh-plugin-installer) ⭐5 — Marketplace plugin that integrates DeepSeek Harness with the GitHub plugin ecosystem. (✅ active)
- [dsh-plugin-ya-workspace-sidebar](https://github.com/HuanLinOTO/dsh-plugin-ya-workspace-sidebar) ⭐5 — DSH Web 工作区侧栏替代，顶部全局最近会话 + Workspace→Session 二级菜单 + 面包屑 | DSH Web workspace sidebar replacement: top global recent sessions + Workspace→Session two-level menu + breadcrumbs (✅ active)
- [dsh-status-rotator](https://github.com/01Virex/dsh-status-rotator) ⭐5 — Replaces the 'Deep diving…' turn-status label with phase-aware typewriter messages. (✅ active)
- [nowledge-mem-deepseek-harness](https://github.com/nowledge-co/nowledge-mem-deepseek-harness) ⭐5 — Community plugin bundle integrating the Nowledge Mem memory service with DeepSeek Harness. (✅ active)
- [dsh-cost-plugin](https://github.com/RoxsLee/dsh-cost-plugin) ⭐4 — DSH 费用/余额读数插件：在输入框统计行旁实时显示「本次 ≈¥x · 会话 ≈¥x · 余额 ¥x」，内置 DeepSeek 官方价目表，支持 2026-08-17 起生效的峰谷定价（按节点时间戳自动选档），余额经官方 /user/balance 实时查询，失败静默降级。 (✅ active)
- [dsh-cue-plugin](https://github.com/unnnnoooo/dsh-cue-plugin) ⭐4 — DeepSeek Harness 的跨会话引用(cue)插件 (✅ active)
- [dsh-guardian](https://github.com/cdxiaodong/dsh-guardian) ⭐4 — Agent security guardrail: intercepts and audits every tool call, requiring human confirmation on sensitive operations. (✅ active)
- [dsh-input-history](https://github.com/lhh010/dsh-input-history) ⭐4 — Terminal-style input history: Ctrl+Up/Ctrl+Down to recall and switch sent messages. (✅ active)
- [dsh-pet](https://github.com/PC2005-cloud/dsh-pet) ⭐4 — DeepSeek Harness 桌面宠物插件 + 完整素材生成链：AI 提示词 → 绿幕视频 → 透明动画 → 可安装插件，从零到宠物全流程可复现 (✅ active)
- [dsh-plugin-anti-ads](https://github.com/HuanLinOTO/dsh-plugin-anti-ads) ⭐4 — DSH Web 广告拦截器，四层独立防御拦截 dsh-ads 插件的所有广告位 | DSH Web ad blocker with four independent defense layers targeting the dsh-ads plugin (✅ active)
- [dsh-plugin-deepeye](https://github.com/Favio8/dsh-plugin-deepeye) ⭐4 — DeepEye vision plugin for DeepSeek Harness (DSH): image description, OCR, VQA, UI layout, and clipboard analysis. (✅ active)
- [dsh-plugin-hub](https://github.com/Noob-stupid/dsh-plugin-hub) ⭐4 — Plugin management panel: enable/disable installed plugins plus a GitHub dsh-plugin marketplace with one-click install. (✅ active)
- [dsh-plugin-interpreters](https://github.com/HuanLinOTO/dsh-plugin-interpreters) ⭐4 — Expose run_python/run_node tools that execute code via stdin and return stdout/stderr/exit code. (✅ active)
- [dsh-remote](https://github.com/flymysql/dsh-remote) ⭐4 — Remote workspace: connect a host over SSH and operate a remote directory with rw_* tools. (✅ active)
- [dsh-spotlight](https://github.com/0xsline/dsh-spotlight) ⭐4 — Keyboard-first command palette for DeepSeek Harness Web. (✅ active)
- [weshop-dsh-plugin](https://github.com/weshopai/weshop-dsh-plugin) ⭐4 — Native WeShop Cordis plugin for DeepSeek Harness. Allow you to use infinite canvas with infinite creative skills. (✅ active)
- [context-vista](https://github.com/GooodWei/context-vista) ⭐3 — Live context/token monitor: floating panel + /context command with donut charts of token usage, allocation and estimated cost. (✅ active)
- [dsh-builtin-toggles](https://github.com/Starfie1d1272/dsh-builtin-toggles) ⭐3 — Human-readable catalog of official DSH Web built-ins with safe GUI toggles. (✅ active)
- [dsh-calculator](https://github.com/bobcat848/dsh-calculator) ⭐3 — Calculate the real-time cost of DeepSeek API calls made by DeepSeek Harness. (✅ active)
- [dsh-llm-inspector](https://github.com/cdxiaodong/dsh-llm-inspector) ⭐3 — Unified LLM request/response inspector: reasoning-effort tuning, external-think export, traffic & bundle analysis. (✅ active)
- [dsh-opencode-go-usage](https://github.com/Xenia0922/dsh-opencode-go-usage) ⭐3 — DeepSeek Harness 插件:OpenCode Go 用量与花费悬浮仪表盘(配额、逐请求成本、模型/来源分布) (✅ active)
- [dsh-plugins-raincode](https://github.com/rainforest888/dsh-plugins-raincode) ⭐3 — dsh plugin: DeepSeek Harness 的模型层 = raincode(模型池/缓存/重试) + /skills 浏览 (✅ active)
- [dsh-token-panel](https://github.com/juhe291/dsh-token-panel) ⭐3 — A corner HUD for DeepSeek Harness that shows your session's token pressure, per-model cost, and daily/monthly usage at a glance — with an editable budget & balance that tracks spending for you. 右下角常驻的 Token 仪表盘：实时查看会话压力、按模型估算花费，预算和余额点一下就能改，每天每月用了多少都有记录。 (✅ active)
- [dsh-usage-plugin](https://github.com/Yihong89/dsh-usage-plugin) ⭐3 — DeepSeek Harness (DSH) plugins. First: dsh-usage-report — per-session token usage & estimated cost (/usage + usage_report), priced from the DeepSeek pricing table. (✅ active)
- [dsh-weather](https://github.com/sunshine-lang/dsh-weather) ⭐3 — Weather tool: current conditions and multi-day forecasts via Open-Meteo, free with no API key. (✅ active)
- [dsh-web-search-pro](https://github.com/anweat/dsh-web-search-pro) ⭐3 — Multi-engine persistent search: DeepSeek/Exa/DDG/Bing/Jina + GitHub/Bilibili/YouTube/V2EX/XHS/Twitter/Reddit/RSS, with SQLite+LRU cache and Playwright rendering. (✅ active)
- [dsh-webbridge](https://github.com/bill9109/dsh-webbridge) ⭐3 — DSH combined with Kimi WebBridge for real browser control. (✅ active)
- [dsh-wordbox](https://github.com/arcmosin/dsh-wordbox) ⭐3 — Persistent common-word panel beside the composer with global/project buckets and one-click insert. (✅ active)
- [dsh-drag-and-drop](https://github.com/bill9109/dsh-drag-and-drop) ⭐2 — Cross-platform drag & drop for DSH Web UI with original-path insertion, no file copying. (✅ active)
- [dsh-file-claim](https://github.com/Nwflower/dsh-file-claim) ⭐2 — File ownership/claim system for parallel agent sessions on the same project: claim/release, heartbeat stale takeover and async 3-way merge. (✅ active)
- [dsh-file-mount](https://github.com/acefun29/dsh-file-mount) ⭐2 — Incremental file mounting with line-range deduplication: identical file contents are never re-sent to the model. (✅ active)
- [dsh-memory (Jesse-njx)](https://github.com/Jesse-njx/dsh-memory) ⭐2 — Cited memory over DSH's lossless session log: distilled, human-auditable facts with citations. (✅ active)
- [dsh-notify-windows](https://github.com/SeverusZh/dsh-notify-windows) ⭐2 — Windows notifications for DSH, zero dependencies. (✅ active)
- [dsh-pdf](https://github.com/sunshine-lang/dsh-pdf) ⭐2 — PDF toolbox: extract text, metadata and page ranges via pdfjs-dist, local with no API key. (✅ active)
- [dsh-prompt-studio](https://github.com/Moeblack/dsh-prompt-studio) ⭐2 — Edit user and built-in system-prompt sections with live preview. (✅ active)
- [dsh-review-loop](https://github.com/wuxiangru915/dsh-review-loop) ⭐2 — Incremental diff reviewer: checkpoint-based review queue with a Web UI panel and /review command. (✅ active)
- [dsh-session-search](https://github.com/Tieboyh/dsh-session-search) ⭐2 — Index-free cross-agent session search for DeepSeek Harness. (✅ active)
- [dsh-suggested-replies](https://github.com/Anionex/dsh-suggested-replies) ⭐2 — Predicted next-message candidates above the DSH Web composer, one click to fill the draft. (✅ active)
- [dsh-web-billing](https://github.com/bpc-oss/dsh-web-billing) ⭐2 — RMB/USD token billing for the DSH web: official-policy auto pricing with peak/off-peak hours and per-message cost ledger. (✅ active)
- [URL Manager](https://github.com/Piccolo123/url-manager) ⭐2 — Agent-first URL and knowledge collection system: auto-categorize, tag, full-text search and shared collections. (✅ active)
- [dsh-computer-use](https://github.com/xiaoheizi1212/dsh-computer-use) ⭐1 — Model-agnostic Computer Use for DSH: isolated browser, Windows native helper and third-party bridges. (✅ active)
- [dsh-memento](https://github.com/PerryLink/dsh-memento) ⭐1 — Bounded, layered, approval-gated and auditable cross-session memory with frozen snapshot injection. (✅ active)
- [dsh-payload-capture](https://github.com/Moeblack/dsh-payload-capture) ⭐1 — Captures every upstream model API payload to JSON for debugging and observability. (✅ active)
- [dsh-pin-recall](https://github.com/kerwin2046/dsh-pin-recall) ⭐1 — Pin assistant replies from the action strip and recall them into the next model turn (/pin /recall). (✅ active)
- [dsh-plugin-anydoc](https://github.com/beancookie/dsh-plugin-anydoc) ⭐1 — Convert Word, PPT, Excel, PDF, EPUB and CSV documents to GitHub-Flavored Markdown via @firecrawl/anydoc. (✅ active)
- [dsh-spend](https://github.com/nonewind/dsh-spend) ⭐1 — Token usage and estimated spend: floating panel with per-model/day/session stats and auto-detected billing plans. (✅ active)
- [dsh-test-runner](https://github.com/suimi8/dsh-test-runner) ⭐1 — Structured test runner tool: auto-detect vitest/jest/pytest/node:test, run tests and parse failure summaries for the model. (✅ active)
- [dsh-view-modes](https://github.com/NigelYao/dsh-view-modes) ⭐1 — Output modes with Verbose, Normal and Summary views plus semantic grouping for tool calls and thinking. (✅ active)
- [dsh-web-search-exa](https://github.com/TonyDua/dsh-web-search-exa) ⭐1 — Zero-config Exa web search provider: keyless anonymous MCP fallback plus keyed REST search. (✅ active)
- [dsh-workspace-search](https://github.com/tsonglew/dsh-workspace-search) ⭐1 — VS Code-style workspace keyword search: a Search tab for the Better Sidebar ecosystem. (✅ active)
- [dsh-file-mentions](https://github.com/a903067276-rgb/dsh-file-mentions)  — Clickable file paths in DSH replies: inline open, reveal in file manager and a mentioned-files chip list. (✅ active)
- [dsh-file-uploads](https://github.com/l541402398/dsh-file-uploads)  — Upload arbitrary local files from the Web composer with pending cards, managed in Settings. (✅ active)
- [dsh-git-branch-switcher](https://github.com/mixin-ai/dsh-git-branch-switcher)  — Session-header git branch pill: shows the workspace branch and switches it from the Web UI. (✅ active)
- [dsh-hud](https://github.com/a903067276-rgb/dsh-hud)  — HUD status panel: git status, MCP servers, skills, model and token usage in a floating side panel. (✅ active)
- [dsh-island](https://github.com/cdxiaodong/dsh-island)  — Bridge DSH agent sessions, tool calls, and approvals to the CodeIsland macOS notch panel over a Unix socket, with in-panel allow/deny. (✅ active)
- [dsh-memoria](https://github.com/jiayan-xu/dsh-memoria)  — Vector + graph memory backend with namespace isolation, automatic observation, recall, importance handling and hot reload. (🧪 experimental)
- [dsh-memory](https://github.com/flymysql/dsh-memory)  — Cross-session memory vault: memory_remember / memory_recall / memory_forget tools with a Settings page. (🧪 experimental)
- [dsh-news-plugin](https://github.com/canghai666x/dsh-news-plugin)  — RSS/news ingestion returning structured title/link/source/date/summary for downstream model ranking and briefing. (✅ active)
- [dsh-recommend](https://github.com/zp-home/dsh-recommend)  — Transparent plugin rankings and recommendations: daily auto-fetched dsh-plugin topic data with an open scoring model. (✅ active)
- [dsh-tool-git](https://github.com/lxj808624/dsh-tool-git)  — Structured safe Git tools: status/diff/log/branch/stage/commit/stash/show with a destructive-command guard. (✅ active)
- [dsh-tool-search](https://github.com/vibeinging/dsh-tool-search)  — Per-agent on-demand tool discovery and progressive schema disclosure. (✅ active)
- [dsh-turn-index](https://github.com/Simon314620/dsh-turn-index)  — Turn-index sidebar: one entry per user turn, click to jump with scroll-spy highlighting. (✅ active)

### Skills


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [dsh-skill-viewer](https://github.com/Fishquito7/dsh-skill-viewer) | ⭐12 | DSH Web UI plugin: Skills settings section with hot enable/disable, delete and add. | ✅ active |
| 2 | [dsh-plugin-dev](https://github.com/omdsh-dev/dsh-plugin-dev) | ⭐9 | Field-tested plugin development playbook (skill + docs): cordis dual copies, tsconfig triplets, Windows junctions and multi-frame zstd. | ✅ active |
| 3 | [dsh-plugin-skills](https://github.com/omdsh-dev/dsh-plugin-skills) | ⭐7 | Agent skills for building and testing DeepSeek Harness plugins, from scaffolding a package to publishing. | ✅ active |
| 4 | [dsh-book2skill](https://github.com/omdsh-dev/dsh-book2skill) | ⭐3 | Book-to-skill plugin: a 5-stage long task that fetches, parses, understands, generates and installs a skill. | ✅ active |
| 5 | [dsh-godot-skill](https://github.com/akira399/dsh-godot-skill) | ⭐2 | Godot Engine 4.x full-stack game development skill plugin for DSH. | ✅ active |
| 6 | [dsh-review-skills](https://github.com/ben7am1n/dsh-review-skills) | ⭐2 | Code review skill pack for DeepSeek Harness. | ✅ active |
| 7 | [dsh-find-skill](https://github.com/Moximxxx/dsh-find-skill) | ⭐1 | Bridges the vercel-labs/skills ecosystem: LLM-driven skill search, install and management. | ✅ active |
| 8 | [dsh-skill-pack-security](https://github.com/PerryLink/dsh-skill-pack-security) | ⭐1 | Security-audit skill pack: 5 agent skills covering secret scan, dependency audit and more. | ✅ active |
| 9 | [dsh-skillport](https://github.com/Jesse-njx/dsh-skillport) | ⭐1 | Every skill you already have — Claude Code, Codex, Cursor, Gemini CLI — works in DSH. | ✅ active |
| 10 | [dsh-skillradar](https://github.com/hellosky983/dsh-skillradar) | ⭐1 | Scans session-visible skills and ranks them by relevance to the recent conversation. | ✅ active |

#### Complete list (14)

- [dsh-skill-viewer](https://github.com/Fishquito7/dsh-skill-viewer) ⭐12 — DSH Web UI plugin: Skills settings section with hot enable/disable, delete and add. (✅ active)
- [dsh-plugin-dev](https://github.com/omdsh-dev/dsh-plugin-dev) ⭐9 — Field-tested plugin development playbook (skill + docs): cordis dual copies, tsconfig triplets, Windows junctions and multi-frame zstd. (✅ active)
- [dsh-plugin-skills](https://github.com/omdsh-dev/dsh-plugin-skills) ⭐7 — Agent skills for building and testing DeepSeek Harness plugins, from scaffolding a package to publishing. (✅ active)
- [dsh-book2skill](https://github.com/omdsh-dev/dsh-book2skill) ⭐3 — Book-to-skill plugin: a 5-stage long task that fetches, parses, understands, generates and installs a skill. (✅ active)
- [dsh-godot-skill](https://github.com/akira399/dsh-godot-skill) ⭐2 — Godot Engine 4.x full-stack game development skill plugin for DSH. (✅ active)
- [dsh-review-skills](https://github.com/ben7am1n/dsh-review-skills) ⭐2 — Code review skill pack for DeepSeek Harness. (✅ active)
- [dsh-find-skill](https://github.com/Moximxxx/dsh-find-skill) ⭐1 — Bridges the vercel-labs/skills ecosystem: LLM-driven skill search, install and management. (✅ active)
- [dsh-skill-pack-security](https://github.com/PerryLink/dsh-skill-pack-security) ⭐1 — Security-audit skill pack: 5 agent skills covering secret scan, dependency audit and more. (✅ active)
- [dsh-skillport](https://github.com/Jesse-njx/dsh-skillport) ⭐1 — Every skill you already have — Claude Code, Codex, Cursor, Gemini CLI — works in DSH. (✅ active)
- [dsh-skillradar](https://github.com/hellosky983/dsh-skillradar) ⭐1 — Scans session-visible skills and ranks them by relevance to the recent conversation. (✅ active)
- [deepseek-harness-skillx](https://github.com/drowned-fish1/deepseek-harness-skillx)  — Skill collection for DeepSeek Harness workflows. (✅ active)
- [dsh-humanize](https://github.com/zevorn/dsh-humanize)  — De-AI writing skill: rewrite agent output to sound more human. (✅ active)
- [dsh-news-briefing](https://github.com/canghai666x/dsh-news-briefing)  — News briefing skill: multi-dimensional story scoring, anti-clickbait rules, content prioritization and Chinese editorial style. (✅ active)
- [dsh-web-novel-research](https://github.com/canghai666x/dsh-web-novel-research)  — Chinese web-novel plot lookup skill: free mirror-site workflow with GBK decoding and duplicate-chapter disambiguation. (✅ active)

### Workflows & Automation


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [dsh_workflow](https://github.com/icetomoyo/dsh_workflow) | ⭐54 | Brings Claude Code's UltraCode mode to DSH: upgrade one-shot multi-agent dispatch into a generatable, saveable, governable, observable, recoverable workflow layer. | ✅ active |
| 2 | [mstar-harness](https://github.com/btspoony/mstar-harness) | ⭐42 | Skill-driven harness/loop engineering workflow agent: tune agent loops as a first-class workflow. | ✅ active |
| 3 | [dsh-automation](https://github.com/titanwings/dsh-automation) | ⭐27 | Run coding tasks on a schedule in fresh Agent sessions, managed by the user or the agent itself. | ✅ active |
| 4 | [dsh-auto-continue](https://github.com/HsiangNianian/dsh-auto-continue) | ⭐9 | Auto-resumes interrupted DSH Web requests: failure classification, adaptive retry, configurable continue message and browser notifications. | ✅ active |
| 5 | [dsh-deep-research](https://github.com/omdsh-dev/dsh-deep-research) | ⭐9 | Adaptive deep-research orchestrator built on the official workflow engine. | ✅ active |
| 6 | [dsh-harness-ops](https://github.com/fakechris/dsh-harness-ops) | ⭐7 | Ops toolbox: A/B dual-slot daily snapshot rotation with atomic switch and one-click rollback, plus a 10s watchdog. | ✅ active |
| 7 | [dsh-track](https://github.com/fakechris/dsh-track) | ⭐5 | Embedded task-management engine: decision-point protocol, thought-capture wall and Linear-style issue storage. | ✅ active |
| 8 | [engineer-software](https://github.com/KirschBluteX/engineer-software) | ⭐5 | Runtime-neutral, evidence-driven software engineering workflow for Codex and DeepSeek Harness. | ✅ active |
| 9 | [dsh-companion](https://github.com/william-jin-cmu/dsh-companion) | ⭐4 | Resident desktop assistant: global hotkey, scheduled automation, quick replies and a plugin market. | ✅ active |
| 10 | [dsh-plans](https://github.com/Optim-Agent/dsh-plans) | ⭐4 | Human-in-the-loop planning preset adapted from prime-plans: researched, reviewed, executed. | ✅ active |

#### Complete list (20)

- [dsh_workflow](https://github.com/icetomoyo/dsh_workflow) ⭐54 — Brings Claude Code's UltraCode mode to DSH: upgrade one-shot multi-agent dispatch into a generatable, saveable, governable, observable, recoverable workflow layer. (✅ active)
- [mstar-harness](https://github.com/btspoony/mstar-harness) ⭐42 — Skill-driven harness/loop engineering workflow agent: tune agent loops as a first-class workflow. (✅ active)
- [dsh-automation](https://github.com/titanwings/dsh-automation) ⭐27 — Run coding tasks on a schedule in fresh Agent sessions, managed by the user or the agent itself. (✅ active)
- [dsh-auto-continue](https://github.com/HsiangNianian/dsh-auto-continue) ⭐9 — Auto-resumes interrupted DSH Web requests: failure classification, adaptive retry, configurable continue message and browser notifications. (✅ active)
- [dsh-deep-research](https://github.com/omdsh-dev/dsh-deep-research) ⭐9 — Adaptive deep-research orchestrator built on the official workflow engine. (✅ active)
- [dsh-harness-ops](https://github.com/fakechris/dsh-harness-ops) ⭐7 — Ops toolbox: A/B dual-slot daily snapshot rotation with atomic switch and one-click rollback, plus a 10s watchdog. (✅ active)
- [dsh-track](https://github.com/fakechris/dsh-track) ⭐5 — Embedded task-management engine: decision-point protocol, thought-capture wall and Linear-style issue storage. (✅ active)
- [engineer-software](https://github.com/KirschBluteX/engineer-software) ⭐5 — Runtime-neutral, evidence-driven software engineering workflow for Codex and DeepSeek Harness. (✅ active)
- [dsh-companion](https://github.com/william-jin-cmu/dsh-companion) ⭐4 — Resident desktop assistant: global hotkey, scheduled automation, quick replies and a plugin market. (✅ active)
- [dsh-plans](https://github.com/Optim-Agent/dsh-plans) ⭐4 — Human-in-the-loop planning preset adapted from prime-plans: researched, reviewed, executed. (✅ active)
- [dsh-deepresearch](https://github.com/havingautism/dsh-deepresearch) ⭐3 — DeepResearch plugin (cordis) for the Harness. (🧪 experimental)
- [dsh-inspect](https://github.com/omdsh-dev/dsh-inspect) ⭐3 — Adversarial checkup → fix → review loop built on the official workflow engine. (✅ active)
- [dsh-plugin-spur](https://github.com/HuanLinOTO/dsh-plugin-spur) ⭐3 — Hang a whip in the chat stream: flick it (>2.0 px/ms) to send the agent a 'go work' message. (✅ active)
- [dsh-prime-agent](https://github.com/yoke233/dsh-prime-agent) ⭐3 — Prime Agent-inspired persistent RLM control plane for DSH Code Mode. (✅ active)
- [dsh-doublecheck](https://github.com/PerryLink/dsh-doublecheck) ⭐1 — Engineering-discipline loop: requirement grilling before edits, red/green test-evidence gates and adversarial delivery review. (✅ active)
- [dsh-governance](https://github.com/tappass/dsh-governance) ⭐1 — Authority layer for agentic AI as a DSH plugin: governs every tool call against your policies. (✅ active)
- [dsh-eval](https://github.com/hccccc01333/dsh-eval)  — Agent evaluation platform: benchmark YAML, headless dsh runs, trace-based metrics, scripted grading and run comparison. (✅ active)
- [dsh-report-studio](https://github.com/ciceroyang/dsh-report-studio)  — Turn a DSH session into deliverable work reports (daily/weekly/handoff/article) with verifiable receipts. (✅ active)
- [dsh-task-dag](https://github.com/LeemanCheung/dsh-task-dag)  — Persistent live DAG visualization of workflow runs, subagents, status and dependencies. (✅ active)
- [dsh-trajectory-debug](https://github.com/devmom/dsh-trajectory-debug)  — Trajectory waterfall, deterministic replay, breakpoints, edit-and-rerun, fork compare and performance analytics. (✅ active)

### Agents & Multi-Agent


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [openbiliclaw](https://github.com/whiteguo233/OpenBiliClaw) | ⭐2,324 | 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin） | ✅ active |
| 2 | [dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) | ⭐222 | Multi-agent team-oriented extensions for DSH. | ✅ active |
| 3 | [dsh-agent-rp](https://github.com/hewzhew/dsh-agent-rp) | ⭐101 | SillyTavern migration and next-generation Agent roleplay for DSH. | ✅ active |
| 4 | [allinluna](https://github.com/zenx0x/allinluna) | ⭐25 | Resource-aware multi-agent orchestration for Codex and DeepSeek Harness (All in Flash DSH plugin). | ✅ active |
| 5 | [dsh-interconnect](https://github.com/Chinesezjc/dsh-interconnect) | ⭐24 | Cross-instance message/event handoff plugins (interconnect service + tools). | ✅ active |
| 6 | [dsh-openbiliclaw](https://github.com/whiteguo233/dsh-openbiliclaw) | ⭐19 | OpenBiliClaw 是本地运行的跨平台个性化内容推荐 Agent，持续理解你的兴趣并主动找内容。本仓库是它的 DeepSeek Harness 插件：DSH 界面常驻第四栏（推荐/内容库/对话/画像/设置），注册 22 个 Agent Bridge 工具，让 Agent 也能读推荐、答探测、闭环学习。 | ✅ active |
| 7 | [dsh-tianshu-build](https://github.com/huiliyi37/dsh-tianshu-build) | ⭐19 | DeepSeek X Tianshu  Harness build 是一款完全体开源 coding agent:在 dsh harness 基础之上带视觉、跨会话记忆、验证门、agent 路由、语义 + 图谱代码检索、文件回滚和全屏终端 UI——全部以插件组合。  它是 DeepSeek Harness(dsh)的友好 MIT fork, 它保留了上游一切皆插件的架构，并将以harness最佳形态和架构往下演进。 | ✅ active |
| 8 | [dsh-data-agent](https://github.com/omdsh-dev/dsh-data-agent) | ⭐17 | Session-scoped database connections with a dedicated data agent: let the model connect to databases and write SQL. | ✅ active |
| 9 | [dsh-plugin-cc](https://github.com/cpj-dev/dsh-plugin-cc) | ⭐12 | Bridge DeepSeek Harness into Claude Code for review, critique, delegation and session import. | ✅ active |
| 10 | [dsh-plugin-product-subagents](https://github.com/shaokeyibb/dsh-plugin-product-subagents) | ⭐8 | Role-based Codex/Claude Code/ACP subagent providers: continuable children with durable state. | ✅ active |

#### Complete list (23)

- [openbiliclaw](https://github.com/whiteguo233/OpenBiliClaw) ⭐2,324 — 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin） (✅ active)
- [dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) ⭐222 — Multi-agent team-oriented extensions for DSH. (✅ active)
- [dsh-agent-rp](https://github.com/hewzhew/dsh-agent-rp) ⭐101 — SillyTavern migration and next-generation Agent roleplay for DSH. (✅ active)
- [allinluna](https://github.com/zenx0x/allinluna) ⭐25 — Resource-aware multi-agent orchestration for Codex and DeepSeek Harness (All in Flash DSH plugin). (✅ active)
- [dsh-interconnect](https://github.com/Chinesezjc/dsh-interconnect) ⭐24 — Cross-instance message/event handoff plugins (interconnect service + tools). (✅ active)
- [dsh-openbiliclaw](https://github.com/whiteguo233/dsh-openbiliclaw) ⭐19 — OpenBiliClaw 是本地运行的跨平台个性化内容推荐 Agent，持续理解你的兴趣并主动找内容。本仓库是它的 DeepSeek Harness 插件：DSH 界面常驻第四栏（推荐/内容库/对话/画像/设置），注册 22 个 Agent Bridge 工具，让 Agent 也能读推荐、答探测、闭环学习。 (✅ active)
- [dsh-tianshu-build](https://github.com/huiliyi37/dsh-tianshu-build) ⭐19 — DeepSeek X Tianshu  Harness build 是一款完全体开源 coding agent:在 dsh harness 基础之上带视觉、跨会话记忆、验证门、agent 路由、语义 + 图谱代码检索、文件回滚和全屏终端 UI——全部以插件组合。  它是 DeepSeek Harness(dsh)的友好 MIT fork, 它保留了上游一切皆插件的架构，并将以harness最佳形态和架构往下演进。 (✅ active)
- [dsh-data-agent](https://github.com/omdsh-dev/dsh-data-agent) ⭐17 — Session-scoped database connections with a dedicated data agent: let the model connect to databases and write SQL. (✅ active)
- [dsh-plugin-cc](https://github.com/cpj-dev/dsh-plugin-cc) ⭐12 — Bridge DeepSeek Harness into Claude Code for review, critique, delegation and session import. (✅ active)
- [dsh-plugin-product-subagents](https://github.com/shaokeyibb/dsh-plugin-product-subagents) ⭐8 — Role-based Codex/Claude Code/ACP subagent providers: continuable children with durable state. (✅ active)
- [dsh-advisor](https://github.com/omdsh-dev/dsh-advisor) ⭐5 — Pair a second model that passively reviews each turn and injects notes. (✅ active)
- [dsh-plugin-claude-bridge](https://github.com/YYTbit/dsh-plugin-claude-bridge) ⭐5 — Bridge Claude Code memory, skills and config into DeepSeek Harness. (✅ active)
- [dsh-plugin-yet-another-subagent](https://github.com/HuanLinOTO/dsh-plugin-yet-another-subagent) ⭐5 — Configurable subagent profile system: a single subagent tool with profile parameters, Web UI settings and live progress. (✅ active)
- [Task Passport](https://github.com/dongsheng123132/task-passport) ⭐5 — Open task handoff protocol for DeepSeek Harness, WorkBuddy, Claude Code and Codex: verified state, not chat logs. (✅ active)
- [dsh-agent-messaging](https://github.com/happyren/dsh-agent-messaging) ⭐4 — Cross-session agent-to-agent messaging: address another session by name. (✅ active)
- [dsh-sidechain](https://github.com/omdsh-dev/dsh-sidechain) ⭐4 — Side sessions: persistent /side sessions (Codex style) and one-off /btw questions (Claude style) in temporary forks. (✅ active)
- [dsh-a2a](https://github.com/dpskh/dsh-a2a) ⭐2 — Agent2Agent mesh for the Harness. (✅ active)
- [dsh-llm-fallbacks](https://github.com/omdsh-dev/dsh-llm-fallbacks) ⭐2 — Role-based LLM retry and fallback strategy plugin. (✅ active)
- [dsh-cross-session](https://github.com/Wha1eChai/dsh-cross-session) ⭐1 — Same-runtime cross-session discovery and communication for DeepSeek Harness. (✅ active)
- [dsh-crosstalk](https://github.com/Jesse-njx/dsh-crosstalk) ⭐1 — Cross-session messaging: DSH sessions on the same machine can discover, message and coordinate with each other. (✅ active)
- [dsh-slice-agent-loop](https://github.com/TT-Wang/dsh-slice-agent-loop) ⭐1 — Drop-in agent loop whose context engine is a bounded slice instead of a growing transcript. (✅ active)
- [dsh-subagent-tools](https://github.com/lynx-gt/dsh-subagent-tools) ⭐1 — Per-call model/provider/persona/toolFilter overrides for subagent delegation with @preset references. (✅ active)
- [dsh-supervisor](https://github.com/Wha1eChai/dsh-supervisor) ⭐1 — Same-runtime cross-session discovery and communication for DeepSeek Harness. (✅ active)

### Clients (Desktop & TUI)


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [deepseek-harness-desktop (Anywhere Labs)](https://github.com/anywhere-labs/deepseek-harness-desktop) | ⭐962 | Modern desktop experience built for the DeepSeek Harness ecosystem (plugin). | ✅ active |
| 2 | [dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) | ⭐793 | Claude Code-style full-screen terminal plugin: pixel-whale top bar, live status line, streaming thoughts, double-Esc rollback, context progress bar and TPS meter. | ✅ active |
| 3 | [oh-dsh](https://github.com/hust-open-atom-club/oh-dsh) | ⭐160 | One-stop community distribution: TUI, desktop and Web UI in a unified experience with layered installation. | ✅ active |
| 4 | [dsh-desktop (DataElement)](https://github.com/dataelement/dsh-desktop) | ⭐140 | Desktop app for DeepSeek Harness. | ✅ active |
| 5 | [dsh-tianshu-tui](https://github.com/huiliyi37/dsh-tianshu-tui) | ⭐125 | Interactive terminal UI plugin for DSH with added TDD, evidence gates and vision modules. | ✅ active |
| 6 | [deepseek-harness-desktop (steven-kid)](https://github.com/steven-kid/deepseek-harness-desktop) | ⭐104 | Minimal cross-platform desktop wrapper: no config, out of the box. | ✅ active |
| 7 | [dsh_desktop](https://github.com/myYangyunfan/dsh_desktop) | ⭐74 | DeepSeek Harness (dsh) Windows desktop client - bundled Node.js + dsh CLI, one-click launch | ✅ active |
| 8 | [deepseek-harness-desktop (salathleizhang)](https://github.com/salathleizhang/deepseek-harness-desktop) | ⭐67 | Desktop wrapper for DeepSeek Harness. | ✅ active |
| 9 | [dsh-launcher](https://github.com/Ruler4396/dsh-launcher) | ⭐65 | Lightweight Windows launcher: silent autostart at logon plus a minimal WebView2 window. | ✅ active |
| 10 | [deepseek-harness-desktop (hairyf)](https://github.com/hairyf/deepseek-harness-desktop) | ⭐63 | One-click desktop app: fully local with self-healing core updates, zero environment setup. Windows/macOS/Linux. | ✅ active |

#### Complete list (35)

- [deepseek-harness-desktop (Anywhere Labs)](https://github.com/anywhere-labs/deepseek-harness-desktop) ⭐962 — Modern desktop experience built for the DeepSeek Harness ecosystem (plugin). (✅ active)
- [dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) ⭐793 — Claude Code-style full-screen terminal plugin: pixel-whale top bar, live status line, streaming thoughts, double-Esc rollback, context progress bar and TPS meter. (✅ active)
- [oh-dsh](https://github.com/hust-open-atom-club/oh-dsh) ⭐160 — One-stop community distribution: TUI, desktop and Web UI in a unified experience with layered installation. (✅ active)
- [dsh-desktop (DataElement)](https://github.com/dataelement/dsh-desktop) ⭐140 — Desktop app for DeepSeek Harness. (✅ active)
- [dsh-tianshu-tui](https://github.com/huiliyi37/dsh-tianshu-tui) ⭐125 — Interactive terminal UI plugin for DSH with added TDD, evidence gates and vision modules. (✅ active)
- [deepseek-harness-desktop (steven-kid)](https://github.com/steven-kid/deepseek-harness-desktop) ⭐104 — Minimal cross-platform desktop wrapper: no config, out of the box. (✅ active)
- [dsh_desktop](https://github.com/myYangyunfan/dsh_desktop) ⭐74 — DeepSeek Harness (dsh) Windows desktop client - bundled Node.js + dsh CLI, one-click launch (✅ active)
- [deepseek-harness-desktop (salathleizhang)](https://github.com/salathleizhang/deepseek-harness-desktop) ⭐67 — Desktop wrapper for DeepSeek Harness. (✅ active)
- [dsh-launcher](https://github.com/Ruler4396/dsh-launcher) ⭐65 — Lightweight Windows launcher: silent autostart at logon plus a minimal WebView2 window. (✅ active)
- [deepseek-harness-desktop (hairyf)](https://github.com/hairyf/deepseek-harness-desktop) ⭐63 — One-click desktop app: fully local with self-healing core updates, zero environment setup. Windows/macOS/Linux. (✅ active)
- [deepseek-harness-desktop (xiincs)](https://github.com/xiincs/deepseek-harness-desktop) ⭐53 — Native desktop built on Tauri 2 with bundled Node.js runtime, tray residency and auto-update. (✅ active)
- [Deepseek-Harness-Desktop (ChisaAlter)](https://github.com/ChisaAlter/Deepseek-Harness-Desktop) ⭐50 — Electron desktop shell with theme and background-image customization. (✅ active)
- [dsh-multica-runtime](https://github.com/multica-ai/dsh-multica-runtime) ⭐27 — Support the dsh runtime on Multica. (✅ active)
- [dsh-work](https://github.com/vibeinging/dsh-work) ⭐25 — Local-first AI workbench for DSH Plugins, combining Agent sessions, project files, data analysis, web research, MCP, and Office artifacts in an Electron desktop app. (✅ active)
- [deepseek-harness-app (ipfred)](https://github.com/ipfred/deepseek-harness-app) ⭐23 — Desktop app for DeepSeek Harness. (✅ active)
- [deepseek-harness-desktop (hongfeiyucode)](https://github.com/hongfeiyucode/deepseek-harness-desktop) ⭐23 — Desktop wrapper for DeepSeek Harness. (✅ active)
- [deepseek-harness-desktop (ningbainb)](https://github.com/ningbainb/deepseek-harness-desktop) ⭐21 — Lossless Windows desktop app with the complete DSH Web UI, plugins, skins and skill dock. (✅ active)
- [DeepSeekHarnessDesktop (wess09)](https://github.com/wess09/DeepSeekHarnessDesktop) ⭐20 — Desktop packaging for DeepSeek Harness. (✅ active)
- [dsh-desktop (bruc3van)](https://github.com/bruc3van/dsh-desktop) ⭐20 — Third-party desktop client loading the official Web UI: reuses a running official instance or a bundled dsh runtime. (✅ active)
- [DeepSeek Harness TUI (openma-ai)](https://github.com/openma-ai/deepseek-harness-tui) ⭐15 — Rust/Ratatui terminal client speaking the DSH SDK JSON-RPC protocol directly; runs standalone or as a profile bundle. (✅ active)
- [deepseek-harness-desktop (cc1252)](https://github.com/cc1252/deepseek-harness-desktop) ⭐14 — Unofficial open-source Windows Electron wrapper for DeepSeek Harness. (✅ active)
- [DeepSeek-Harness-Desktop (sleep2agi)](https://github.com/sleep2agi/DeepSeek-Harness-Desktop) ⭐11 — Unofficial community desktop shell for the public dsh runtime. (✅ active)
- [awesome-deepseek-harness-desktop (ADHD)](https://github.com/omdsh-dev/awesome-deepseek-harness-desktop) ⭐10 — ADHD — out-of-the-box Electron desktop wrapper for DeepSeek Harness. (✅ active)
- [deepseek-harness-desktop (chyra-moon)](https://github.com/chyra-moon/deepseek-harness-desktop) ⭐10 — Native Windows desktop shell: 1:1 official web UI with embedded server, tray and auto-recovery. (✅ active)
- [deepseek-harness-termux](https://github.com/Vengisk/deepseek-harness-termux) ⭐9 — Run @deepseek-ai/dsh on Android/Termux. (✅ active)
- [deepseek-harness-desktop](https://github.com/omdsh-dev/deepseek-harness-desktop) ⭐7 — DSH 桌面应用打包器 (✅ active)
- [deepseek-harness-desktop](https://github.com/qyqy-1109/deepseek-harness-desktop) ⭐6 — DeepSeek Harness Desktop: self-contained Windows desktop shell (Electron) that auto-starts dsh web, plus a subtle Codex-flavored theme plugin. (✅ active)
- [deepseek-harness-tui (gxinxing)](https://github.com/gxinxing/deepseek-harness-tui) ⭐6 — Terminal-native interactive TUI built with Ink (React for terminals). (✅ active)
- [deepseek-harness-cli](https://github.com/Richard-Yang0130/deepseek-harness-cli) ⭐5 — Claude Code-style terminal interface for DeepSeek Harness (✅ active)
- [deepseek-harness-desktop](https://github.com/RZX00/deepseek-harness-desktop) ⭐5 — DeepSeek Harness with a Windows desktop build: an Electron shell over the dsh web profile, packaged as an installer (✅ active)
- [deepseek-harness-tui (boxeryao)](https://github.com/boxeryao/deepseek-harness-tui) ⭐5 — Lightweight fast terminal plugin connected directly to the DSH runtime. (✅ active)
- [deepseek-harness-fnos](https://github.com/techysy/deepseek-harness-fnos) ⭐4 — DeepSeek Harness (DeepSeek 官方 agent 浏览器 UI) fnOS 应用 — 本地常驻服务, 官方统一网关接入 (✅ active)
- [dsh-desktop-electron](https://github.com/Void0312Aurora/dsh-desktop-electron) ⭐4 — Cross-platform Electron shell for the DSH Web GUI: tray-resident standalone window. (✅ active)
- [dsh-pi-tui](https://github.com/lqhl/dsh-pi-tui) ⭐1 — Pi TUI front end: streaming markdown, thinking collapse, tool cards, slash commands and approval overlays. (✅ active)
- [dsh-grok-tui](https://github.com/chen-001/dsh-grok-tui)  — TUI built with grok-build. (✅ active)

### MCP & Integrations


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [Coding Tools MCP](https://github.com/xyTom/coding-tools-mcp) | ⭐758 | Coding-oriented MCP tool collection that appears in the emerging DSH ecosystem: give any AI agent the ability to code. | ✅ active |
| 2 | [dsh-openpencil](https://github.com/ZSeven-W/dsh-openpencil) | ⭐64 | OpenPencil design preview and editing integration. | ✅ active |
| 3 | [dsh-lark](https://github.com/omdsh-dev/dsh-lark) | ⭐14 | Lark/Feishu IM bot channel for DeepSeek Harness | 飞书 DeepSeek Harness 插件 | ✅ active |
| 4 | [deepseek-harness-acp](https://github.com/openma-ai/deepseek-harness-acp) | ⭐6 | ACP server implementation for DeepSeek Harness: exposes the full DSH agent to ACP clients while reusing credentials and sessions. | ✅ active |
| 5 | [deepseek-harness-docker](https://github.com/runzhliu/deepseek-harness-docker) | ⭐6 | Community Docker and Kubernetes packaging for @deepseek-ai/dsh with a hardened image. | ✅ active |
| 6 | [dsh-oauth-mcp-client](https://github.com/springbrand-lab/dsh-oauth-mcp-client) | ⭐6 | OAuth 2.1 Streamable HTTP MCP client plugin for DeepSeek Harness. | ✅ active |
| 7 | [deepseek-harness-action](https://github.com/Lixiaoyiao/deepseek-harness-action) | ⭐5 | Community GitHub Action: AI code review, CI diagnosis, auto-fix and issue-to-PR implementation. | ✅ active |
| 8 | [dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) | ⭐5 | MCP server manager: Settings page with OAuth (PKCE + dynamic client registration) or static-token auth. | ✅ active |
| 9 | [deepseek-harness-vsc-extension](https://github.com/weinibuliu/deepseek-harness-vsc-extension) | ⭐4 | DeepSeek Harness for VS Code as extension | ✅ active |
| 10 | [DSH Telegram Relay](https://github.com/congchuanling-dot/DSH-Telegram-Relay) | ⭐4 | Relay that turns Telegram into a remote conversation channel for DSH with notifications. | ✅ active |

#### Complete list (25)

- [Coding Tools MCP](https://github.com/xyTom/coding-tools-mcp) ⭐758 — Coding-oriented MCP tool collection that appears in the emerging DSH ecosystem: give any AI agent the ability to code. (✅ active)
- [dsh-openpencil](https://github.com/ZSeven-W/dsh-openpencil) ⭐64 — OpenPencil design preview and editing integration. (✅ active)
- [dsh-lark](https://github.com/omdsh-dev/dsh-lark) ⭐14 — Lark/Feishu IM bot channel for DeepSeek Harness | 飞书 DeepSeek Harness 插件 (✅ active)
- [deepseek-harness-acp](https://github.com/openma-ai/deepseek-harness-acp) ⭐6 — ACP server implementation for DeepSeek Harness: exposes the full DSH agent to ACP clients while reusing credentials and sessions. (✅ active)
- [deepseek-harness-docker](https://github.com/runzhliu/deepseek-harness-docker) ⭐6 — Community Docker and Kubernetes packaging for @deepseek-ai/dsh with a hardened image. (✅ active)
- [dsh-oauth-mcp-client](https://github.com/springbrand-lab/dsh-oauth-mcp-client) ⭐6 — OAuth 2.1 Streamable HTTP MCP client plugin for DeepSeek Harness. (✅ active)
- [deepseek-harness-action](https://github.com/Lixiaoyiao/deepseek-harness-action) ⭐5 — Community GitHub Action: AI code review, CI diagnosis, auto-fix and issue-to-PR implementation. (✅ active)
- [dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) ⭐5 — MCP server manager: Settings page with OAuth (PKCE + dynamic client registration) or static-token auth. (✅ active)
- [deepseek-harness-vsc-extension](https://github.com/weinibuliu/deepseek-harness-vsc-extension) ⭐4 — DeepSeek Harness for VS Code as extension (✅ active)
- [DSH Telegram Relay](https://github.com/congchuanling-dot/DSH-Telegram-Relay) ⭐4 — Relay that turns Telegram into a remote conversation channel for DSH with notifications. (✅ active)
- [dsh-telegram-channel](https://github.com/hi-wenw/dsh-telegram-channel) ⭐4 — Telegram mobile remote for live DSH Web sessions: session picker, bind/unbind, same trajectory as desktop. (✅ active)
- [PicGo DSH Plugin](https://github.com/PicGo/dsh-plugin) ⭐4 — Official PicGo plugin: upload images/files to your image host from DSH and get public URLs. (✅ active)
- [dsh-browser](https://github.com/xylt369/dsh-browser) ⭐3 — Browser capability for DeepSeek Harness: headed Edge/Playwright provider, SSRF-safe navigation, a11y-ref clicking, permission gate with auto-remember, gated evaluate (✅ active)
- [dsh-mcp-panel](https://github.com/PerryLink/dsh-mcp-panel) ⭐3 — Read-only runtime management panel for the official DSH MCP client: /mcp command and a Settings tab. (✅ active)
- [dsh-search-mcp](https://github.com/gxpppp/dsh-search-mcp) ⭐3 — Replace DSH's built-in web search with search MCP servers (Tavily/Brave/Exa/Perplexity/DuckDuckGo). (✅ active)
- [dsh-harness-mcp-server](https://github.com/chushixixin/dsh-harness-mcp-server) ⭐2 — Expose DeepSeek Harness agent capabilities as an MCP server (brain=Hermes, arms=Harness). (✅ active)
- [dsh-chrome](https://github.com/YJSoooooo/dsh-chrome) ⭐1 — Chrome profile bridge: control an existing signed-in Chrome profile through Chrome DevTools Protocol. (✅ active)
- [vscode-deepseek-harness](https://github.com/kalynnka/vscode-deepseek-harness) ⭐1 — Unofficial: drive your own dsh as a native VS Code chat agent. (✅ active)
- [deepseek-harness-rs](https://github.com/Tokimorphling/deepseek-harness-rs)  — A Rust port of DeepSeek Harness. (🧪 experimental)
- [dsh-github-integration](https://github.com/omdsh-dev/dsh-github-integration)  — GitHub integration plugin for DSH. (✅ active)
- [dsh-lan-access](https://github.com/Leon0555/dsh-lan-access)  — LAN access for the Web GUI: 0.0.0.0 bind plus a crypto.randomUUID polyfill for non-secure contexts. (✅ active)
- [dsh-super-injector](https://github.com/yjh051108/dsh-super-injector)  — Super-injector plugin (cordis) for context injection. (✅ active)
- [dsh4vscode](https://github.com/DoggyHU/dsh4vscode)  — VS Code chat windows backed by the DSH agent: OpenCode-style independent sessions with model auto-routing. (✅ active)
- [opendsh](https://github.com/TheChengXi/opendsh)  — Open the DeepSeek Harness Web UI inside VS Code with one-command start/stop. (✅ active)
- [URL Manager MCP](https://github.com/Piccolo123/url-manager-mcp)  — MCP companion for URL Manager: 21 tools for save/search/categorize/share with magic-link delivery. (✅ active)

### Examples & Starters


#### 🔥 Top 7

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [hello-dsh](https://github.com/pingfanfan/hello-dsh) | ⭐37 | Zero-to-plugin tutorial: understand 'everything is a plugin' with 22 Chinese skill examples. | ✅ active |
| 2 | [dsh-plugin-template](https://github.com/bugmaker2/dsh-plugin-template) | ⭐16 | Template for DeepSeek Harness plugin development. | ✅ active |
| 3 | [turtle-ui](https://github.com/turtle1999/turtle-ui) | ⭐6 | Official UI plugin reference implementation. | ✅ active |
| 4 | [dsh-101](https://github.com/bill9109/dsh-101) | ⭐2 | DSH documentation reading mode. | ✅ active |
| 5 | [dsh-plugin-template (sunshine-lang)](https://github.com/sunshine-lang/dsh-plugin-template) | ⭐2 | Ready-to-publish plugin skeleton: bundle format, tool DSL, config and tests. | ✅ active |
| 6 | [dsh-plugin-hello](https://github.com/xu1132/dsh-plugin-hello) |  | Hello-world style starter plugin for DSH. | ✅ active |
| 7 | [plugin-template (omdsh-dev)](https://github.com/omdsh-dev/plugin-template) |  | Plugin template repository derived from the original turtle-ui official repo. | ✅ active |

#### Complete list (7)

- [hello-dsh](https://github.com/pingfanfan/hello-dsh) ⭐37 — Zero-to-plugin tutorial: understand 'everything is a plugin' with 22 Chinese skill examples. (✅ active)
- [dsh-plugin-template](https://github.com/bugmaker2/dsh-plugin-template) ⭐16 — Template for DeepSeek Harness plugin development. (✅ active)
- [turtle-ui](https://github.com/turtle1999/turtle-ui) ⭐6 — Official UI plugin reference implementation. (✅ active)
- [dsh-101](https://github.com/bill9109/dsh-101) ⭐2 — DSH documentation reading mode. (✅ active)
- [dsh-plugin-template (sunshine-lang)](https://github.com/sunshine-lang/dsh-plugin-template) ⭐2 — Ready-to-publish plugin skeleton: bundle format, tool DSL, config and tests. (✅ active)
- [dsh-plugin-hello](https://github.com/xu1132/dsh-plugin-hello)  — Hello-world style starter plugin for DSH. (✅ active)
- [plugin-template (omdsh-dev)](https://github.com/omdsh-dev/plugin-template)  — Plugin template repository derived from the original turtle-ui official repo. (✅ active)

### Tutorials & Learning


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [DeepSeek Harness Orange Book](https://github.com/alchaincyf/deepseek-harness-orange-book) | ⭐465 | Community Orange Book: complete system prompts, a 129-line startup checklist and three raw session logs — first-hand testing the official docs lack. Free PDF/EPUB/HTML. | ✅ active |
| 2 | [dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) | ⭐167 | From 0 to 1 handbook: installation, plugin development, performance tuning, real-world cases and same-model multi-agent comparisons (CN + EN PDF). | ✅ active |
| 3 | [dshfind](https://github.com/hikariming/dshfind) | ⭐56 | Learn DSH principles, plugin marketplace and best practices — from chapter-by-chapter Cordis paper reading to an auto-aggregated plugin market. | ✅ active |
| 4 | [dsh-harness-tutorial](https://github.com/yanhua1010/dsh-harness-tutorial) | ⭐32 | DeepSeek Harness Agent 的原理与实现：从零到一实现一个 AI Agent —— 一切皆插件的中文教程（VitePress 站点 + 8 个 Demo + mini-harness 教学项目） | ✅ active |
| 5 | [deepseek-harness-tutorial](https://github.com/ht426/deepseek-harness-tutorial) | ⭐17 | Detailed Chinese learning tutorial for DeepSeek Harness. | ✅ active |
| 6 | [dsh-explain](https://github.com/yuezengwu/dsh-explain) | ⭐9 | Local-first learning mode: cross-session global learning threads, explain-by-source, ExplainContext and compression. | ✅ active |
| 7 | [deepseek-harness-prompts](https://github.com/demouo/deepseek-harness-prompts) | ⭐6 | DeepSeek Harness prompts for different modes. | ✅ active |
| 8 | [deepseek-harness-learning](https://github.com/Lucky2024-pllove/deepseek-harness-learning) | ⭐5 | Learning website built from a systematic breakdown of the deepseek-harness repository, for developers curious how AI agent frameworks work. | ✅ active |
| 9 | [dsh-book-deepseek-harness](https://github.com/LaplaceYoung/dsh-book-deepseek-harness) | ⭐5 | 'Deep Dive into DeepSeek Harness' — source-level architecture book: 37 chapter files, PDF, Mermaid diagrams and writing conventions. | ✅ active |
| 10 | [dsh-learn-everything](https://github.com/cendaifeng/dsh-learn-everything) | ⭐3 | Feynman learning-mode plugin: teach → teach-back → judge → re-explain loop rendered as rich HTML lesson cards. | ✅ active |

#### Complete list (11)

- [DeepSeek Harness Orange Book](https://github.com/alchaincyf/deepseek-harness-orange-book) ⭐465 — Community Orange Book: complete system prompts, a 129-line startup checklist and three raw session logs — first-hand testing the official docs lack. Free PDF/EPUB/HTML. (✅ active)
- [dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) ⭐167 — From 0 to 1 handbook: installation, plugin development, performance tuning, real-world cases and same-model multi-agent comparisons (CN + EN PDF). (✅ active)
- [dshfind](https://github.com/hikariming/dshfind) ⭐56 — Learn DSH principles, plugin marketplace and best practices — from chapter-by-chapter Cordis paper reading to an auto-aggregated plugin market. (✅ active)
- [dsh-harness-tutorial](https://github.com/yanhua1010/dsh-harness-tutorial) ⭐32 — DeepSeek Harness Agent 的原理与实现：从零到一实现一个 AI Agent —— 一切皆插件的中文教程（VitePress 站点 + 8 个 Demo + mini-harness 教学项目） (✅ active)
- [deepseek-harness-tutorial](https://github.com/ht426/deepseek-harness-tutorial) ⭐17 — Detailed Chinese learning tutorial for DeepSeek Harness. (✅ active)
- [dsh-explain](https://github.com/yuezengwu/dsh-explain) ⭐9 — Local-first learning mode: cross-session global learning threads, explain-by-source, ExplainContext and compression. (✅ active)
- [deepseek-harness-prompts](https://github.com/demouo/deepseek-harness-prompts) ⭐6 — DeepSeek Harness prompts for different modes. (✅ active)
- [deepseek-harness-learning](https://github.com/Lucky2024-pllove/deepseek-harness-learning) ⭐5 — Learning website built from a systematic breakdown of the deepseek-harness repository, for developers curious how AI agent frameworks work. (✅ active)
- [dsh-book-deepseek-harness](https://github.com/LaplaceYoung/dsh-book-deepseek-harness) ⭐5 — 'Deep Dive into DeepSeek Harness' — source-level architecture book: 37 chapter files, PDF, Mermaid diagrams and writing conventions. (✅ active)
- [dsh-learn-everything](https://github.com/cendaifeng/dsh-learn-everything) ⭐3 — Feynman learning-mode plugin: teach → teach-back → judge → re-explain loop rendered as rich HTML lesson cards. (✅ active)
- [deepseek-protocol-doctor](https://github.com/Whning0513/deepseek-protocol-doctor) ⭐1 — Checks DeepSeek tool loops, reasoning_content, strict schemas and captured SSE; also works as a DSH plugin. (✅ active)

### Awesome Lists & Registries


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | ⭐751 | Large curated list of installable DSH plugins (bilingual). | ✅ active |
| 2 | [awesome-dsh-plugins (Radar)](https://github.com/AdamPlatin123/awesome-dsh-plugins) | ⭐751 | Radar index repo: auto-scanning all discovered dsh plugin candidates with an evidence-based compatibility matrix. | ✅ active |
| 3 | [awesome-deepseek-harness (0xsline)](https://github.com/0xsline/awesome-deepseek-harness) | ⭐360 | Curated DSH ecosystem directory: plugins, tools and infrastructure from dsh-external/hub and the public dsh-plugin topic. | ✅ active |
| 4 | [notes (zhaoolee)](https://github.com/zhaoolee/notes) | ⭐138 | Open-source Smartisan Notes clone: Docker private deployment, skill invocation, dsh plugin support and one-click WeChat-format export. | ✅ active |
| 5 | [awesome-dsh-plugin (bruc3van)](https://github.com/bruc3van/awesome-dsh-plugin) | ⭐86 | Find the right DSH plugin in 30 seconds: what problem each plugin solves, who it is for and where to start. | ✅ active |
| 6 | [Awesome-DeepSeek-Harness-Plugins](https://github.com/Zhiyuan-Fan/Awesome-DeepSeek-Harness-Plugins) | ⭐47 | Curated list of DeepSeek Harness plugins. | ✅ active |
| 7 | [awesome-DSH-plugin (Alex-Yanggg)](https://github.com/Alex-Yanggg/awesome-DSH-plugin) | ⭐47 | Meticulously curated list of plugins, extensions, tools and development resources for DSH. | ✅ active |
| 8 | [oh-my-dsh](https://github.com/LaplaceYoung/oh-my-dsh) | ⭐43 | Plugin ecosystem for DSH: 700+ plugins registered only through extension seams, without modifying the agent-loop skeleton. | ✅ active |
| 9 | [plugin-registry](https://github.com/vlln/plugin-registry) | ⭐31 | DSH plugin ecosystem infrastructure: thin console to manage official repository plugins (0 patch) plus the make-dsh-plugin skill. | ✅ active |
| 10 | [awesome-deepseek-harness (Dominic789654)](https://github.com/Dominic789654/awesome-deepseek-harness) | ⭐30 | Curated list of plugins, skills, MCP servers, patch/profile layers, orchestrators and UIs for DeepSeek Harness. | ✅ active |

#### Complete list (25)

- [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) ⭐751 — Large curated list of installable DSH plugins (bilingual). (✅ active)
- [awesome-dsh-plugins (Radar)](https://github.com/AdamPlatin123/awesome-dsh-plugins) ⭐751 — Radar index repo: auto-scanning all discovered dsh plugin candidates with an evidence-based compatibility matrix. (✅ active)
- [awesome-deepseek-harness (0xsline)](https://github.com/0xsline/awesome-deepseek-harness) ⭐360 — Curated DSH ecosystem directory: plugins, tools and infrastructure from dsh-external/hub and the public dsh-plugin topic. (✅ active)
- [notes (zhaoolee)](https://github.com/zhaoolee/notes) ⭐138 — Open-source Smartisan Notes clone: Docker private deployment, skill invocation, dsh plugin support and one-click WeChat-format export. (✅ active)
- [awesome-dsh-plugin (bruc3van)](https://github.com/bruc3van/awesome-dsh-plugin) ⭐86 — Find the right DSH plugin in 30 seconds: what problem each plugin solves, who it is for and where to start. (✅ active)
- [Awesome-DeepSeek-Harness-Plugins](https://github.com/Zhiyuan-Fan/Awesome-DeepSeek-Harness-Plugins) ⭐47 — Curated list of DeepSeek Harness plugins. (✅ active)
- [awesome-DSH-plugin (Alex-Yanggg)](https://github.com/Alex-Yanggg/awesome-DSH-plugin) ⭐47 — Meticulously curated list of plugins, extensions, tools and development resources for DSH. (✅ active)
- [oh-my-dsh](https://github.com/LaplaceYoung/oh-my-dsh) ⭐43 — Plugin ecosystem for DSH: 700+ plugins registered only through extension seams, without modifying the agent-loop skeleton. (✅ active)
- [plugin-registry](https://github.com/vlln/plugin-registry) ⭐31 — DSH plugin ecosystem infrastructure: thin console to manage official repository plugins (0 patch) plus the make-dsh-plugin skill. (✅ active)
- [awesome-deepseek-harness (Dominic789654)](https://github.com/Dominic789654/awesome-deepseek-harness) ⭐30 — Curated list of plugins, skills, MCP servers, patch/profile layers, orchestrators and UIs for DeepSeek Harness. (✅ active)
- [awesome-deepseek-harness (libukai)](https://github.com/libukai/awesome-deepseek-harness) ⭐29 — Ultimate guide: quick start, resources, curated plugins and practical tools. (✅ active)
- [oh-my-dsh](https://github.com/like-study1/Oh-My-DSH) ⭐21 — 🐳 DeepSeek Harness 插件聚合社区 — 自动同步 dsh-plugin 生态 · 精选目录 · 每 8 小时自动维护 | Oh-My-DSH: a community-maintained catalog of DeepSeek Harness plugins, auto-synced from the dsh-plugin topic (✅ active)
- [deepseek-plugin-store](https://github.com/Ericwong5021/deepseek-plugin-store) ⭐12 — DeepSeek Harness 独立社区插件商店：发现、安装并提交经过验证的插件、工具与扩展。 | Independent community plugin directory. (✅ active)
- [dsh-suite](https://github.com/whyihaveyou/dsh-suite) ⭐11 — Living DSH plugin directory (785+ plugins, refreshed hourly) with daily compatibility CI, a bilingual catalog site and an in-app plugin store. (✅ active)
- [dsh-meme-hub](https://github.com/the-beating-light-of-the-nail/dsh-meme-hub) ⭐9 — Curated navigation of community meme plugins (skins, desktop pets, mini-games), bilingual. (✅ active)
- [awesome-dsh-plugins (white0dew)](https://github.com/white0dew/awesome-dsh-plugins) ⭐7 — Public GitHub directory for DSH plugins with install commands. (✅ active)
- [awesome-deepseek-harness (jiji262)](https://github.com/jiji262/awesome-deepseek-harness) ⭐6 — Curated DeepSeek Harness resources. (✅ active)
- [awesome-dsh-plugin (billLiao)](https://github.com/billLiao/awesome-dsh-plugin) ⭐5 — Curated list of plugins for DeepSeek Harness. (✅ active)
- [awesome-dsh-plugins (kejixiaoliang)](https://github.com/kejixiaoliang/awesome-dsh-plugins) ⭐5 — Curated DSH plugin catalog: 14 categories, 280+ community plugins covering MCP/Skill/TUI/multi-agent/context memory/UI skins. (✅ active)
- [dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) ⭐4 — Verified plugin marketplace and autonomous registry for DeepSeek Harness (✅ active)
- [dsh-plugins](https://github.com/HackSing/dsh-plugins) ⭐4 — A bilingual, continuously maintained directory of plugins for DeepSeek Harness (DSH). (✅ active)
- [zat-dsh-engine](https://github.com/mishibeikejie/zat-dsh-engine) ⭐4 — Visual plugin marketplace for DeepSeek Harness — browse, search and install community plugins (✅ active)
- [dsh-market](https://github.com/2BingLing/dsh-market) ⭐3 — DeepSeek Harness 插件市场 · 持续收录 500+ DSH 插件：中文搜索 + 实用五维评分 + 一键安装。Web 版与 DSH 侧边栏插件双形态。Plugin marketplace for DeepSeek Harness: 500+ plugins, Chinese search, 5-dim scoring, one-click install. (✅ active)
- [dsh-plugins](https://github.com/lwmxiaobei/dsh-plugins) ⭐3 — DeepSeek Harness 社区插件目录，自动汇总并基础校验 GitHub 插件，支持搜索、筛选、双语详情与最新版本安装命令复制。Community directory for DeepSeek Harness plugins with automated discovery, basic validation, search, filters, bilingual details, and latest version install commands. (✅ active)
- [awesome-deepseek-agent (official)](https://github.com/deepseek-ai/awesome-deepseek-agent)  — Official curated guides for integrating DeepSeek models into agent/coding-assistant tools (AstrBot, Cherry Studio, Claude Code, Codex, DeepSeek-TUI, Reasonix and more). (✅ active)

### Related Agent Harnesses


#### 🔥 Top 8

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [DeerFlow](https://github.com/bytedance/deer-flow) | ⭐80,001 | Open-source long-horizon SuperAgent harness by ByteDance: skills, memory, sandboxes, subagents, tools and a message gateway. | ✅ active |
| 2 | [Cordis](https://github.com/cordiverse/cordis) | ⭐3,182 | Meta-Framework of Spatiotemporal Composability — the plugin runtime DeepSeek Harness is built on. | ✅ active |
| 3 | [sandbase-harness](https://github.com/sandbaseai/sandbase-harness) | ⭐573 | Open-source CMA-compatible agent runtime for any model: MCP tools, sandboxed sessions, audit, replay. | ✅ active |
| 4 | [mnemon](https://github.com/mnemon-dev/mnemon) | ⭐430 | LLM-supervised persistent memory for AI agents: graph-based recall and cross-session knowledge in a single binary. | ✅ active |
| 5 | [claude-paper](https://github.com/alaliqing/claude-paper) | ⭐294 | Cross-agent research paper toolkit for Claude Code, Codex, OpenCode and DeepSeek Harness: quick summaries and deep dives. | ✅ active |
| 6 | [Axern](https://github.com/cofy-x/axern) | ⭐272 | Open-source sandboxes for AI agents: untrusted code execution and durable services. | ✅ active |
| 7 | [open-managed-agents](https://github.com/openma-ai/open-managed-agents) | ⭐235 | Open-source Claude Managed Agents API implementation and self-hosted Claude Tag-style agent runtime. | ✅ active |
| 8 | [deepseek-auto-evolving-harness](https://github.com/liuchen6667/deepseek-auto-evolving-harness) | ⭐28 | Auto-evolving LLM agent harness: benchmark-driven evolution via Claude Code and a self_evolution.md guide. | ✅ active |

#### Complete list (8)

- [DeerFlow](https://github.com/bytedance/deer-flow) ⭐80,001 — Open-source long-horizon SuperAgent harness by ByteDance: skills, memory, sandboxes, subagents, tools and a message gateway. (✅ active)
- [Cordis](https://github.com/cordiverse/cordis) ⭐3,182 — Meta-Framework of Spatiotemporal Composability — the plugin runtime DeepSeek Harness is built on. (✅ active)
- [sandbase-harness](https://github.com/sandbaseai/sandbase-harness) ⭐573 — Open-source CMA-compatible agent runtime for any model: MCP tools, sandboxed sessions, audit, replay. (✅ active)
- [mnemon](https://github.com/mnemon-dev/mnemon) ⭐430 — LLM-supervised persistent memory for AI agents: graph-based recall and cross-session knowledge in a single binary. (✅ active)
- [claude-paper](https://github.com/alaliqing/claude-paper) ⭐294 — Cross-agent research paper toolkit for Claude Code, Codex, OpenCode and DeepSeek Harness: quick summaries and deep dives. (✅ active)
- [Axern](https://github.com/cofy-x/axern) ⭐272 — Open-source sandboxes for AI agents: untrusted code execution and durable services. (✅ active)
- [open-managed-agents](https://github.com/openma-ai/open-managed-agents) ⭐235 — Open-source Claude Managed Agents API implementation and self-hosted Claude Tag-style agent runtime. (✅ active)
- [deepseek-auto-evolving-harness](https://github.com/liuchen6667/deepseek-auto-evolving-harness) ⭐28 — Auto-evolving LLM agent harness: benchmark-driven evolution via Claude Code and a self_evolution.md guide. (✅ active)
<!-- AUTO:resources:END -->

---

# Skills

The DeepSeek Harness skill ecosystem is still developing. This directory includes both native DSH skills and reusable agent procedures compatible with Harness workflows.

> We intentionally distinguish between **plugins** and **skills**: a plugin adds runtime capability; a skill primarily adds reusable knowledge, instructions, procedures or task methodology.

**Skill discovery:** look for repositories containing `SKILL.md`, or projects combining `DeepSeek Harness + skills + workflow`.

---

# Workflows & Automation

One of the most promising parts of the DSH ecosystem. Deep-research orchestrators, plan → execute patterns, task DAGs and auto-resume tooling are listed above in [Workflows & Automation](#workflows--automation).

> **dsh-plan-execute (concept):** the dual-model plan/execute architecture (planner model thinks, executor model acts) has no standalone repo yet — the pattern lives inside [dsh-deep-research](https://github.com/omdsh-dev/dsh-deep-research) and [mstar-harness](https://github.com/btspoony/mstar-harness).

---

# Examples

We strongly encourage projects that can be run in minutes rather than merely inspected. Beyond the templates listed above, the following example categories are worth building or finding:

- **Basic:** `01-hello-harness` · `02-custom-model` · `03-custom-tool` · `04-custom-plugin` · `05-custom-profile`
- **Coding:** `06-code-review-agent` · `07-github-issue-agent` · `08-bug-fixing-agent` · `09-test-generator` · `10-frontend-builder`
- **Research:** `11-deep-research` · `12-web-research` · `13-paper-research` · `14-competitor-research` · `15-news-research`
- **Multi-Agent:** `16-agent-team` · `17-planner-executor` · `18-parallel-research` · `19-reviewer-agent` · `20-agent-crosstalk`
- **Workflow:** `21-product-launch` · `22-security-audit` · `23-seo-research` · `24-reddit-research` · `25-content-pipeline`
- **Memory & Context:** `26-long-term-memory` · `27-context-compression` · `28-cross-session-memory` · `29-session-search` · `30-context-audit`

---

# Research

The term **agent harness** is increasingly studied as its own optimization layer.

### Harness Engineering

How task decomposition, workflow structure, tool policies, retry budgets and execution guidance affect agent performance.

### Harness Evolution

Instead of keeping the harness fixed — `Harness v1 → Execute → Evaluate → Modify → Harness v2`. This opens future directions:

* Harness benchmarks · Workflow evaluation · Automated skill optimization
* Tool-set optimization · Self-improving agents · Cross-harness portability

---

# Project Structure

```text
awesome-deepseek-harness/
│
├── README.md            ← generated tables (see below)
├── README.zh-CN.md      ← 简体中文版
├── CONTRIBUTING.md
├── LICENSE
│
├── data/                ← machine-readable source of truth
│   ├── plugins.json
│   ├── skills.json
│   ├── workflows.json
│   ├── agents.json
│   ├── clients.json
│   ├── integrations.json
│   ├── examples.json
│   ├── tutorials.json
│   ├── awesome-lists.json
│   └── related.json
│
├── schemas/
│   └── resource.schema.json
│
├── scripts/             ← zero-dependency Python (no build step)
│   ├── validate.py
│   ├── check-links.py
│   ├── discover-github.py
│   ├── update-metadata.py
│   ├── generate-readme.py
│   └── generate-docs.py
│
├── docs/                ← MkDocs site (en/ + zh/, generated)
├── mkdocs.yml
│
└── .github/
    ├── workflows/
    │   ├── validate.yml
    │   └── discover.yml
    └── ISSUE_TEMPLATE/
        └── submit-project.yml
```

**The README is generated from `data/`** — resource tables between `<!-- AUTO:resources:START -->
### Plugins


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [petdex](https://github.com/crafter-station/petdex) | ⭐3,777 | A public gallery of animated pets for Codex, Claude Code, DeepSeek Harness, Hermes, OpenCode, Gemini CLI, and more. | ✅ active |
| 2 | [dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | ⭐1,697 | Large plugin and skin collection for DSH Web: task board, git graph, side panels, remote/mobile UI, pets, token stats and themes. | ✅ active |
| 3 | [modlens](https://github.com/liustack/modlens) | ⭐1,158 | The first vision plugin for DeepSeek Harness and the vision bridge for every text-only coding agent: paste an image and it works. | ✅ active |
| 4 | [DSH Better Sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) | ⭐684 | Workbench-style sidebar: file viewer/editor, terminal, Git, subagents and plugin-extensible tabs. | ✅ active |
| 5 | [museai](https://github.com/yejiming/MuseAI) | ⭐538 | 创建你的 AI 角色，进入你的故事世界。和角色聊天、冒险、穿书，让每一次互动都留下羁绊（支持 DeepSeek Harness 插件，欢迎使用） | ✅ active |
| 6 | [dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) | ⭐506 | Whale-girl skin series for DSH Web (CC BY-NC-SA 4.0). | ✅ active |
| 7 | [dsh-ads](https://github.com/Nagi-ovo/dsh-ads) | ⭐309 | Joke plugin: 2005 Chinese-web-style ad layer with sidebar banners, in-chat feed ads and corner popups. | ✅ active |
| 8 | [dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) | ⭐302 | Vision toolkit for text-only models: intent-aware image Q&A, long-screenshot OCR, UI restoration, grounding and pixel diff. | ✅ active |
| 9 | [whale-girl](https://github.com/vlln/whale-girl) | ⭐118 | Desktop pet plugin (QQ-pet style) floating at the bottom-right of the DSH Web GUI: draggable, feedable and playable. | ✅ active |
| 10 | [dsh-at-file](https://github.com/omdsh-dev/dsh-at-file) | ⭐116 | Codex-style @file mentions inside the DSH composer: search workspace files and attach their contents to prompts. | ✅ active |

#### Complete list (141)

- [petdex](https://github.com/crafter-station/petdex) ⭐3,777 — A public gallery of animated pets for Codex, Claude Code, DeepSeek Harness, Hermes, OpenCode, Gemini CLI, and more. (✅ active)
- [dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) ⭐1,697 — Large plugin and skin collection for DSH Web: task board, git graph, side panels, remote/mobile UI, pets, token stats and themes. (✅ active)
- [modlens](https://github.com/liustack/modlens) ⭐1,158 — The first vision plugin for DeepSeek Harness and the vision bridge for every text-only coding agent: paste an image and it works. (✅ active)
- [DSH Better Sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) ⭐684 — Workbench-style sidebar: file viewer/editor, terminal, Git, subagents and plugin-extensible tabs. (✅ active)
- [museai](https://github.com/yejiming/MuseAI) ⭐538 — 创建你的 AI 角色，进入你的故事世界。和角色聊天、冒险、穿书，让每一次互动都留下羁绊（支持 DeepSeek Harness 插件，欢迎使用） (✅ active)
- [dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) ⭐506 — Whale-girl skin series for DSH Web (CC BY-NC-SA 4.0). (✅ active)
- [dsh-ads](https://github.com/Nagi-ovo/dsh-ads) ⭐309 — Joke plugin: 2005 Chinese-web-style ad layer with sidebar banners, in-chat feed ads and corner popups. (✅ active)
- [dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) ⭐302 — Vision toolkit for text-only models: intent-aware image Q&A, long-screenshot OCR, UI restoration, grounding and pixel diff. (✅ active)
- [whale-girl](https://github.com/vlln/whale-girl) ⭐118 — Desktop pet plugin (QQ-pet style) floating at the bottom-right of the DSH Web GUI: draggable, feedable and playable. (✅ active)
- [dsh-at-file](https://github.com/omdsh-dev/dsh-at-file) ⭐116 — Codex-style @file mentions inside the DSH composer: search workspace files and attach their contents to prompts. (✅ active)
- [modsearch](https://github.com/liustack/modsearch) ⭐85 — Web plugin for DSH and the search bridge for every model without native web access. (✅ active)
- [dsh-browser](https://github.com/Lum1104/dsh-browser) ⭐78 — Chrome sidebar extension that lets DSH operate your browser directly, no vision capabilities required. (✅ active)
- [dsh-visualize](https://github.com/Nagi-ovo/dsh-visualize) ⭐74 — Interactive HTML UI rendered directly in conversation with streaming preview and sandbox rendering. (✅ active)
- [dsh-genui](https://github.com/omdsh-dev/dsh-genui) ⭐71 — Generative UI inside conversations: layouts, charts, forms, quizzes, Mermaid and interactive events rendered inline. (✅ active)
- [dsh-find-plugins](https://github.com/Nagi-ovo/dsh-find-plugins) ⭐67 — Plugin discovery utility for the DSH ecosystem. (✅ active)
- [dsh-memory-evolve](https://github.com/csyangwen/dsh-memory-evolve) ⭐47 — Cross-session long-term memory + background self-evolution: five-track memory, git-branch awareness, in-turn self-review and skill evolution. (✅ active)
- [dsh-annotation](https://github.com/omdsh-dev/dsh-annotation) ⭐39 — Select text in DSH Web, annotate it and send the annotation with your message; replies cross-reference each annotation. (✅ active)
- [dsh-open-in-vscode](https://github.com/omdsh-dev/dsh-open-in-vscode) ⭐39 — Open DSH workspace directories/files directly in VS Code from the web GUI. (✅ active)
- [dsh-notification](https://github.com/omdsh-dev/dsh-notification) ⭐37 — Desktop notifications for turn completions with per-outcome controls and include/exclude keyword filters. (✅ active)
- [dsh-turn-rewind](https://github.com/Anionex/dsh-turn-rewind) ⭐35 — Rewind conversation and workspace state, powered by a persistent change ledger. (✅ active)
- [dsh-vision-router](https://github.com/ysr666/dsh-vision-router) ⭐29 — Eyes for text-only agents: built-in free keyless vision chain plus pixel-level tools (Q&A, grounding, crop, OCR, SVG trace). (✅ active)
- [DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) ⭐28 — Browse, install and update every GitHub topic:dsh-plugin plugin from the DSH Web GUI. (✅ active)
- [ui-status-label](https://github.com/alingalingling/ui-status-label) ⭐28 — Customize the whale's 'Deep diving' status label into anything you want. (✅ active)
- [dsh-ui-whale](https://github.com/lhh010/dsh-ui-whale) ⭐27 — Hand-drawn pixel whale companion in the session title bar: blinks, wags its tail, spouts water when a turn completes. (✅ active)
- [dsh-custom-tool](https://github.com/omdsh-dev/dsh-custom-tool) ⭐22 — Create and manage sandboxed JavaScript tools for DSH with a Monaco editor and model-driven tool lists. (✅ active)
- [dskin](https://github.com/dancingmemory/dskin) ⭐22 — Cartoon pixel skin plugin for DSH Web GUI: pixel pets that walk, blink and jump over the original interface. (✅ active)
- [dsh-chat-import](https://github.com/Nwflower/dsh-chat-import) ⭐20 — Import conversation history from Claude Code, Codex, ChatGPT, Cursor, Gemini, Reasonix and OpenCode into resumable DSH sessions. (✅ active)
- [deepseek-harness-skin](https://github.com/HeiGeAi/deepseek-harness-skin) ⭐18 — Skin system with 21 built-in themes plus one-image custom skin generation, contrast-validated at build time. (✅ active)
- [dsh-computer-use](https://github.com/Anionex/dsh-computer-use) ⭐18 — 为 DeepSeek Harness 提供电脑控制插件：新鲜 Accessibility 观测、过期状态拒绝、作用域权限与安全输入（目前支持macos）｜Accessibility-first macOS Computer Use bundle for DSH with fresh observations, stale-state rejection, scoped permissions, and safe input. (✅ active)
- [dsh-side-panel](https://github.com/ccq1/dsh-side-panel) ⭐18 — Compact side panel with a file browser, terminal and Git review. (✅ active)
- [anysearch-dsh](https://github.com/anysearch-team/anysearch-dsh) ⭐17 — AnySearch web search provider and advanced search tools for DeepSeek Harness. (✅ active)
- [deepseek-harness-snowsalt](https://github.com/KYZHXL/deepseek-harness-snowsalt) ⭐17 — Snow-salt themed skin for DeepSeek Harness. (✅ active)
- [dsh-plugin-check](https://github.com/omdsh-dev/dsh-plugin-check) ⭐17 — Plugin health checks: manifest protocol, patch format, build pitfalls and hub listing status, zero-dependency read-only. (✅ active)
- [dsh-message-edit](https://github.com/Moeblack/dsh-message-edit) ⭐16 — Branch-based message editing, reroll, retry and version timeline. (✅ active)
- [dsh-share](https://github.com/hellodigua/dsh-share) ⭐16 — One-click conversation sharing for DSH. (✅ active)
- [dsh-usage-stats](https://github.com/Ychris12138/dsh-usage-stats) ⭐16 — Token usage heatmap, per-model breakdowns, and DeepSeek account balance for the DeepSeek Harness Web GUI (dsh web). (✅ active)
- [dsh-vision (william-jin-cmu)](https://github.com/william-jin-cmu/dsh-vision) ⭐16 — Vision bridge: view_image tool over any OpenAI-compatible VLM, defaulting to Zhipu's free tier. (✅ active)
- [dsh-toolkit](https://github.com/omdsh-dev/dsh-toolkit) ⭐15 — Zero-dependency tool suite: calculator, CSV, diff, encoding, JSON, Markdown, regex and time utilities. (✅ active)
- [dsh-group-photo](https://github.com/SenmuuuuW/dsh-group-photo) ⭐14 — DSH 内测收官合影墙：GitHub OAuth 零权限登录 + 冻结白名单校验的拍立得合影站（含 DSH Skill 包装） (✅ active)
- [dsh-navbar](https://github.com/vlln/dsh-navbar) ⭐14 — DSH 插件：对话节点导航条（右缘节点串快速跳转 user 消息）。官方 bundle 插件，dsh plugin --profile web add 安装 (✅ active)
- [dsh-web-review](https://github.com/CanglongCl/dsh-web-review) ⭐13 — DeepSeek Harness Web GUI 的网页预览与元素批注插件，让 AI 根据可视化反馈直接修改前端源码。 (✅ active)
- [dsh-focus-chat](https://github.com/dingyi222666/dsh-focus-chat) ⭐12 — 为 dsh 提供新的「聚焦会话」精简会话视图，更轻松易于阅读，只关注最终产出结果。 (✅ active)
- [dsh-kun-like-pet](https://github.com/liyupi/dsh-kun-like-pet) ⭐12 — Kun Like 桌宠 —— DeepSeek Harness 桌面宠物插件：右下角小坤宠随 Agent 工作状态切换 9 种动作，任务完成播放「你干嘛~哎哟」 (✅ active)
- [dsh-market](https://github.com/dsh-market/dsh-market) ⭐12 — Visual plugin market inside DeepSeek Harness: browse, search and one-click install. (✅ active)
- [dsh-minigames](https://github.com/lhh010/dsh-minigames) ⭐12 — DSH Web UI 右侧小游戏面板：18 款离线小游戏（恐龙跳一跳 / 俄罗斯方块 / 坦克大战 / 扫雷 / 2048 / 数独 / 吃豆人 / 跟枪练习等），可扩展游戏注册表，等待模型回复或修 bug 时的摸鱼神器 (✅ active)
- [dsh-plugins-store](https://github.com/ZASENJC/dsh-plugins-store) ⭐12 — Static directory site that automatically collects and categorizes GitHub dsh-plugin topic projects. (✅ active)
- [ego-browser](https://github.com/Fisfzy/ego-browser) ⭐12 — Bring the ego-lite agent browser (Chromium for AI agents) into DSH with 13 structured tools. (✅ active)
- [DeepSeek-Harness-Web-Tools](https://github.com/tonyd2wild/DeepSeek-Harness-Web-Tools) ⭐11 — Free, keyless web_search and web_fetch for DSH, DuckDuckGo-backed with no signup. (✅ active)
- [dsh-balance-meter](https://github.com/Ghost011118/dsh-balance-meter) ⭐11 — DeepSeek account balance and session cost readout for the DeepSeek Harness Web GUI (✅ active)
- [dsh-emoji](https://github.com/hellodigua/dsh-emoji) ⭐11 — Let AI replies add custom emoji reactions. (✅ active)
- [dsh-find-plugin](https://github.com/awesome-dsh-plugin/dsh-find-plugin) ⭐11 — Agent-assisted plugin discovery: search the live GitHub dsh-plugin topic from inside DSH. (✅ active)
- [dsh-gomoku](https://github.com/omdsh-dev/dsh-gomoku) ⭐11 — Play Gomoku with AI inside DSH, or let two AIs battle to compare models. (✅ active)
- [dsh-mnemon](https://github.com/omdsh-dev/dsh-mnemon) ⭐11 — Three-tier local memory: runtime hot memory, project documents and long-term memory spaces, with supervised writeback. (✅ active)
- [dsh-sdk-platform-rs](https://github.com/kpn-dsh/dsh-sdk-platform-rs) ⭐11 — A Rust SDK to interact with the DSH Platform. This library provides convenient building blocks for services that need to connect to DSH Kafka, fetch tokens for various protocols, manage Prometheus metrics, and more. (✅ active)
- [dsh-web-plugin-manager](https://github.com/LX2000WASD/dsh-web-plugin-manager) ⭐11 — Manage plugins from the Web UI: view, live enable/disable, install/uninstall, env management and plugin market. (✅ active)
- [dsh-plugin-workshop](https://github.com/yyyyukari/dsh-plugin-workshop) ⭐10 — Steam Workshop-style plugin browser for the DSH Web UI: zero-server, GitHub-powered search and one-click install. (✅ active)
- [dsh-security-audit](https://github.com/omdsh-dev/dsh-security-audit) ⭐10 — DSH 本机安全审计插件：配置/插件来源/会话/网络暴露面，只读脱敏风险报告 (✅ active)
- [dsh-stock-market](https://github.com/AnacondaKC/dsh-stock-market) ⭐10 — Stock market data plugin (joke: fixes the bug where your account loses money while you code). (✅ active)
- [dsh-webui-market-plugin](https://github.com/Sanqi-normal/dsh-webui-market-plugin) ⭐10 — Community plugin market in the Web GUI: browse the awesome-dsh-plugin.com catalog and install/uninstall to a profile. (✅ active)
- [dsh-milestone](https://github.com/SnowCrescenter-tech/dsh-milestone) ⭐9 — Git-style milestone timeline rail: hover for metadata, click to jump to any message. (✅ active)
- [dsh-plugin-mineru](https://github.com/HuanLinOTO/dsh-plugin-mineru) ⭐9 — Expose MinerU document parsing to the model: PDF/images/DOCX/PPTX/XLSX to structured Markdown/JSON. (✅ active)
- [dsh-session-health](https://github.com/omdsh-dev/dsh-session-health) ⭐9 — Frame-level diagnostics for multi-frame zstd session files: torn/corrupted/empty session detection, zero-dependency read-only. (✅ active)
- [dsh-web-ui-notify](https://github.com/bill9109/dsh-web-ui-notify) ⭐9 — Adds desktop notification reminders to DSH. (✅ active)
- [deepseek-harness-SupportVisionModel](https://github.com/TryDing-T/deepseek-harness-SupportVisionModel) ⭐8 — Secondary development of deepseek-harness supporting a separately configured vision model for reading images. (✅ active)
- [DeepSeek-Harness-Vision-Tools](https://github.com/tonyd2wild/DeepSeek-Harness-Vision-Tools) ⭐8 — Vision proxy for chat: give DSH eyes with any text model plus any vision model. (✅ active)
- [dsh-mneme](https://github.com/modusensus/dsh-mneme) ⭐8 — Local cross-session memory with memory sovereignty: SQLite + human-editable Markdown mirror and background autoDream consolidation. (✅ active)
- [dsh-paste-input](https://github.com/lhh010/dsh-paste-input) ⭐8 — WebUI file input enhancement: Ctrl+V paste, drag & drop and file picker, copied into the session workspace. (✅ active)
- [billion-context-dsh](https://github.com/Tyan66666/billion-context-dsh) ⭐7 — Model-driven context compression (Active Context Pruning): the model decides when and what to compress. (✅ active)
- [DeepSeek-Harness-billing-plugin](https://github.com/WilliamLIiii/DeepSeek-Harness-billing-plugin) ⭐7 — Account balance plus per-model remaining-task estimator with a session cost ledger. (✅ active)
- [dsh-director-toolkit](https://github.com/lhmd/dsh-director-toolkit) ⭐7 — DSH Director Toolkit is a DeepSeek Harness plugin for 3D artists, technical designers, and creative coders. Paste a half-formed idea, a reference note, or a portfolio caption and get a compact direction pack for Blender, Three.js, Houdini, or C4D. (✅ active)
- [dsh-plugin-better-sidebar-plugin-office](https://github.com/HuanLinOTO/dsh-plugin-better-sidebar-plugin-office) ⭐7 — Office-suite preview (.docx/.xlsx/.pptx) for the Better Sidebar, as a standalone slim bundle. (✅ active)
- [dsh-plugin-pet-rs](https://github.com/HuanLinOTO/dsh-plugin-pet-rs) ⭐7 — Rust desktop pet: 5-state whale with dual SSE real-time push, transparent always-on-top window and system tray. (✅ active)
- [dsh-context-doctor](https://github.com/Zhenyu98/dsh-context-doctor) ⭐6 — Audits what actually enters every model request: token cost of AGENTS.md chains, skill catalogs and tool schemas, with duplicate/conflict detection. (✅ active)
- [dsh-diff-viewer](https://github.com/lehhair/dsh-diff-viewer) ⭐6 — PiUI-style Web diff viewer replacing the default diff view. (✅ active)
- [dsh-skin](https://github.com/KinGao294/dsh-skin) ⭐6 — Codex-style skin switcher plus custom translucent wallpaper with opacity/blur controls. (✅ active)
- [dsh-balance](https://github.com/crazywoola/dsh-balance) ⭐5 — DeepSeek Harness balance plugin for the Settings page. (✅ active)
- [dsh-deepcel](https://github.com/Small-tailqwq/dsh-deepcel) ⭐5 — Spreadsheet-style skin for DSH, mimicking Excel. (✅ active)
- [dsh-ohos-patch](https://github.com/shenjackyuanjie/dsh-ohos-patch) ⭐5 — 让deepseek harness能在 ohos上跑！ (✅ active)
- [dsh-plugin-d399](https://github.com/HuanLinOTO/dsh-plugin-d399) ⭐5 — Mini-game menu (Wordle, match-3, 192 parameterized games) that pops up while the model generates. (✅ active)
- [dsh-plugin-installer](https://github.com/Toukaiteio/dsh-plugin-installer) ⭐5 — Marketplace plugin that integrates DeepSeek Harness with the GitHub plugin ecosystem. (✅ active)
- [dsh-plugin-ya-workspace-sidebar](https://github.com/HuanLinOTO/dsh-plugin-ya-workspace-sidebar) ⭐5 — DSH Web 工作区侧栏替代，顶部全局最近会话 + Workspace→Session 二级菜单 + 面包屑 | DSH Web workspace sidebar replacement: top global recent sessions + Workspace→Session two-level menu + breadcrumbs (✅ active)
- [dsh-status-rotator](https://github.com/01Virex/dsh-status-rotator) ⭐5 — Replaces the 'Deep diving…' turn-status label with phase-aware typewriter messages. (✅ active)
- [nowledge-mem-deepseek-harness](https://github.com/nowledge-co/nowledge-mem-deepseek-harness) ⭐5 — Community plugin bundle integrating the Nowledge Mem memory service with DeepSeek Harness. (✅ active)
- [dsh-cost-plugin](https://github.com/RoxsLee/dsh-cost-plugin) ⭐4 — DSH 费用/余额读数插件：在输入框统计行旁实时显示「本次 ≈¥x · 会话 ≈¥x · 余额 ¥x」，内置 DeepSeek 官方价目表，支持 2026-08-17 起生效的峰谷定价（按节点时间戳自动选档），余额经官方 /user/balance 实时查询，失败静默降级。 (✅ active)
- [dsh-cue-plugin](https://github.com/unnnnoooo/dsh-cue-plugin) ⭐4 — DeepSeek Harness 的跨会话引用(cue)插件 (✅ active)
- [dsh-guardian](https://github.com/cdxiaodong/dsh-guardian) ⭐4 — Agent security guardrail: intercepts and audits every tool call, requiring human confirmation on sensitive operations. (✅ active)
- [dsh-input-history](https://github.com/lhh010/dsh-input-history) ⭐4 — Terminal-style input history: Ctrl+Up/Ctrl+Down to recall and switch sent messages. (✅ active)
- [dsh-pet](https://github.com/PC2005-cloud/dsh-pet) ⭐4 — DeepSeek Harness 桌面宠物插件 + 完整素材生成链：AI 提示词 → 绿幕视频 → 透明动画 → 可安装插件，从零到宠物全流程可复现 (✅ active)
- [dsh-plugin-anti-ads](https://github.com/HuanLinOTO/dsh-plugin-anti-ads) ⭐4 — DSH Web 广告拦截器，四层独立防御拦截 dsh-ads 插件的所有广告位 | DSH Web ad blocker with four independent defense layers targeting the dsh-ads plugin (✅ active)
- [dsh-plugin-deepeye](https://github.com/Favio8/dsh-plugin-deepeye) ⭐4 — DeepEye vision plugin for DeepSeek Harness (DSH): image description, OCR, VQA, UI layout, and clipboard analysis. (✅ active)
- [dsh-plugin-hub](https://github.com/Noob-stupid/dsh-plugin-hub) ⭐4 — Plugin management panel: enable/disable installed plugins plus a GitHub dsh-plugin marketplace with one-click install. (✅ active)
- [dsh-plugin-interpreters](https://github.com/HuanLinOTO/dsh-plugin-interpreters) ⭐4 — Expose run_python/run_node tools that execute code via stdin and return stdout/stderr/exit code. (✅ active)
- [dsh-remote](https://github.com/flymysql/dsh-remote) ⭐4 — Remote workspace: connect a host over SSH and operate a remote directory with rw_* tools. (✅ active)
- [dsh-spotlight](https://github.com/0xsline/dsh-spotlight) ⭐4 — Keyboard-first command palette for DeepSeek Harness Web. (✅ active)
- [weshop-dsh-plugin](https://github.com/weshopai/weshop-dsh-plugin) ⭐4 — Native WeShop Cordis plugin for DeepSeek Harness. Allow you to use infinite canvas with infinite creative skills. (✅ active)
- [context-vista](https://github.com/GooodWei/context-vista) ⭐3 — Live context/token monitor: floating panel + /context command with donut charts of token usage, allocation and estimated cost. (✅ active)
- [dsh-builtin-toggles](https://github.com/Starfie1d1272/dsh-builtin-toggles) ⭐3 — Human-readable catalog of official DSH Web built-ins with safe GUI toggles. (✅ active)
- [dsh-calculator](https://github.com/bobcat848/dsh-calculator) ⭐3 — Calculate the real-time cost of DeepSeek API calls made by DeepSeek Harness. (✅ active)
- [dsh-llm-inspector](https://github.com/cdxiaodong/dsh-llm-inspector) ⭐3 — Unified LLM request/response inspector: reasoning-effort tuning, external-think export, traffic & bundle analysis. (✅ active)
- [dsh-opencode-go-usage](https://github.com/Xenia0922/dsh-opencode-go-usage) ⭐3 — DeepSeek Harness 插件:OpenCode Go 用量与花费悬浮仪表盘(配额、逐请求成本、模型/来源分布) (✅ active)
- [dsh-plugins-raincode](https://github.com/rainforest888/dsh-plugins-raincode) ⭐3 — dsh plugin: DeepSeek Harness 的模型层 = raincode(模型池/缓存/重试) + /skills 浏览 (✅ active)
- [dsh-token-panel](https://github.com/juhe291/dsh-token-panel) ⭐3 — A corner HUD for DeepSeek Harness that shows your session's token pressure, per-model cost, and daily/monthly usage at a glance — with an editable budget & balance that tracks spending for you. 右下角常驻的 Token 仪表盘：实时查看会话压力、按模型估算花费，预算和余额点一下就能改，每天每月用了多少都有记录。 (✅ active)
- [dsh-usage-plugin](https://github.com/Yihong89/dsh-usage-plugin) ⭐3 — DeepSeek Harness (DSH) plugins. First: dsh-usage-report — per-session token usage & estimated cost (/usage + usage_report), priced from the DeepSeek pricing table. (✅ active)
- [dsh-weather](https://github.com/sunshine-lang/dsh-weather) ⭐3 — Weather tool: current conditions and multi-day forecasts via Open-Meteo, free with no API key. (✅ active)
- [dsh-web-search-pro](https://github.com/anweat/dsh-web-search-pro) ⭐3 — Multi-engine persistent search: DeepSeek/Exa/DDG/Bing/Jina + GitHub/Bilibili/YouTube/V2EX/XHS/Twitter/Reddit/RSS, with SQLite+LRU cache and Playwright rendering. (✅ active)
- [dsh-webbridge](https://github.com/bill9109/dsh-webbridge) ⭐3 — DSH combined with Kimi WebBridge for real browser control. (✅ active)
- [dsh-wordbox](https://github.com/arcmosin/dsh-wordbox) ⭐3 — Persistent common-word panel beside the composer with global/project buckets and one-click insert. (✅ active)
- [dsh-drag-and-drop](https://github.com/bill9109/dsh-drag-and-drop) ⭐2 — Cross-platform drag & drop for DSH Web UI with original-path insertion, no file copying. (✅ active)
- [dsh-file-claim](https://github.com/Nwflower/dsh-file-claim) ⭐2 — File ownership/claim system for parallel agent sessions on the same project: claim/release, heartbeat stale takeover and async 3-way merge. (✅ active)
- [dsh-file-mount](https://github.com/acefun29/dsh-file-mount) ⭐2 — Incremental file mounting with line-range deduplication: identical file contents are never re-sent to the model. (✅ active)
- [dsh-memory (Jesse-njx)](https://github.com/Jesse-njx/dsh-memory) ⭐2 — Cited memory over DSH's lossless session log: distilled, human-auditable facts with citations. (✅ active)
- [dsh-notify-windows](https://github.com/SeverusZh/dsh-notify-windows) ⭐2 — Windows notifications for DSH, zero dependencies. (✅ active)
- [dsh-pdf](https://github.com/sunshine-lang/dsh-pdf) ⭐2 — PDF toolbox: extract text, metadata and page ranges via pdfjs-dist, local with no API key. (✅ active)
- [dsh-prompt-studio](https://github.com/Moeblack/dsh-prompt-studio) ⭐2 — Edit user and built-in system-prompt sections with live preview. (✅ active)
- [dsh-review-loop](https://github.com/wuxiangru915/dsh-review-loop) ⭐2 — Incremental diff reviewer: checkpoint-based review queue with a Web UI panel and /review command. (✅ active)
- [dsh-session-search](https://github.com/Tieboyh/dsh-session-search) ⭐2 — Index-free cross-agent session search for DeepSeek Harness. (✅ active)
- [dsh-suggested-replies](https://github.com/Anionex/dsh-suggested-replies) ⭐2 — Predicted next-message candidates above the DSH Web composer, one click to fill the draft. (✅ active)
- [dsh-web-billing](https://github.com/bpc-oss/dsh-web-billing) ⭐2 — RMB/USD token billing for the DSH web: official-policy auto pricing with peak/off-peak hours and per-message cost ledger. (✅ active)
- [URL Manager](https://github.com/Piccolo123/url-manager) ⭐2 — Agent-first URL and knowledge collection system: auto-categorize, tag, full-text search and shared collections. (✅ active)
- [dsh-computer-use](https://github.com/xiaoheizi1212/dsh-computer-use) ⭐1 — Model-agnostic Computer Use for DSH: isolated browser, Windows native helper and third-party bridges. (✅ active)
- [dsh-memento](https://github.com/PerryLink/dsh-memento) ⭐1 — Bounded, layered, approval-gated and auditable cross-session memory with frozen snapshot injection. (✅ active)
- [dsh-payload-capture](https://github.com/Moeblack/dsh-payload-capture) ⭐1 — Captures every upstream model API payload to JSON for debugging and observability. (✅ active)
- [dsh-pin-recall](https://github.com/kerwin2046/dsh-pin-recall) ⭐1 — Pin assistant replies from the action strip and recall them into the next model turn (/pin /recall). (✅ active)
- [dsh-plugin-anydoc](https://github.com/beancookie/dsh-plugin-anydoc) ⭐1 — Convert Word, PPT, Excel, PDF, EPUB and CSV documents to GitHub-Flavored Markdown via @firecrawl/anydoc. (✅ active)
- [dsh-spend](https://github.com/nonewind/dsh-spend) ⭐1 — Token usage and estimated spend: floating panel with per-model/day/session stats and auto-detected billing plans. (✅ active)
- [dsh-test-runner](https://github.com/suimi8/dsh-test-runner) ⭐1 — Structured test runner tool: auto-detect vitest/jest/pytest/node:test, run tests and parse failure summaries for the model. (✅ active)
- [dsh-view-modes](https://github.com/NigelYao/dsh-view-modes) ⭐1 — Output modes with Verbose, Normal and Summary views plus semantic grouping for tool calls and thinking. (✅ active)
- [dsh-web-search-exa](https://github.com/TonyDua/dsh-web-search-exa) ⭐1 — Zero-config Exa web search provider: keyless anonymous MCP fallback plus keyed REST search. (✅ active)
- [dsh-workspace-search](https://github.com/tsonglew/dsh-workspace-search) ⭐1 — VS Code-style workspace keyword search: a Search tab for the Better Sidebar ecosystem. (✅ active)
- [dsh-file-mentions](https://github.com/a903067276-rgb/dsh-file-mentions)  — Clickable file paths in DSH replies: inline open, reveal in file manager and a mentioned-files chip list. (✅ active)
- [dsh-file-uploads](https://github.com/l541402398/dsh-file-uploads)  — Upload arbitrary local files from the Web composer with pending cards, managed in Settings. (✅ active)
- [dsh-git-branch-switcher](https://github.com/mixin-ai/dsh-git-branch-switcher)  — Session-header git branch pill: shows the workspace branch and switches it from the Web UI. (✅ active)
- [dsh-hud](https://github.com/a903067276-rgb/dsh-hud)  — HUD status panel: git status, MCP servers, skills, model and token usage in a floating side panel. (✅ active)
- [dsh-island](https://github.com/cdxiaodong/dsh-island)  — Bridge DSH agent sessions, tool calls, and approvals to the CodeIsland macOS notch panel over a Unix socket, with in-panel allow/deny. (✅ active)
- [dsh-memoria](https://github.com/jiayan-xu/dsh-memoria)  — Vector + graph memory backend with namespace isolation, automatic observation, recall, importance handling and hot reload. (🧪 experimental)
- [dsh-memory](https://github.com/flymysql/dsh-memory)  — Cross-session memory vault: memory_remember / memory_recall / memory_forget tools with a Settings page. (🧪 experimental)
- [dsh-news-plugin](https://github.com/canghai666x/dsh-news-plugin)  — RSS/news ingestion returning structured title/link/source/date/summary for downstream model ranking and briefing. (✅ active)
- [dsh-recommend](https://github.com/zp-home/dsh-recommend)  — Transparent plugin rankings and recommendations: daily auto-fetched dsh-plugin topic data with an open scoring model. (✅ active)
- [dsh-tool-git](https://github.com/lxj808624/dsh-tool-git)  — Structured safe Git tools: status/diff/log/branch/stage/commit/stash/show with a destructive-command guard. (✅ active)
- [dsh-tool-search](https://github.com/vibeinging/dsh-tool-search)  — Per-agent on-demand tool discovery and progressive schema disclosure. (✅ active)
- [dsh-turn-index](https://github.com/Simon314620/dsh-turn-index)  — Turn-index sidebar: one entry per user turn, click to jump with scroll-spy highlighting. (✅ active)

### Skills


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [dsh-skill-viewer](https://github.com/Fishquito7/dsh-skill-viewer) | ⭐12 | DSH Web UI plugin: Skills settings section with hot enable/disable, delete and add. | ✅ active |
| 2 | [dsh-plugin-dev](https://github.com/omdsh-dev/dsh-plugin-dev) | ⭐9 | Field-tested plugin development playbook (skill + docs): cordis dual copies, tsconfig triplets, Windows junctions and multi-frame zstd. | ✅ active |
| 3 | [dsh-plugin-skills](https://github.com/omdsh-dev/dsh-plugin-skills) | ⭐7 | Agent skills for building and testing DeepSeek Harness plugins, from scaffolding a package to publishing. | ✅ active |
| 4 | [dsh-book2skill](https://github.com/omdsh-dev/dsh-book2skill) | ⭐3 | Book-to-skill plugin: a 5-stage long task that fetches, parses, understands, generates and installs a skill. | ✅ active |
| 5 | [dsh-godot-skill](https://github.com/akira399/dsh-godot-skill) | ⭐2 | Godot Engine 4.x full-stack game development skill plugin for DSH. | ✅ active |
| 6 | [dsh-review-skills](https://github.com/ben7am1n/dsh-review-skills) | ⭐2 | Code review skill pack for DeepSeek Harness. | ✅ active |
| 7 | [dsh-find-skill](https://github.com/Moximxxx/dsh-find-skill) | ⭐1 | Bridges the vercel-labs/skills ecosystem: LLM-driven skill search, install and management. | ✅ active |
| 8 | [dsh-skill-pack-security](https://github.com/PerryLink/dsh-skill-pack-security) | ⭐1 | Security-audit skill pack: 5 agent skills covering secret scan, dependency audit and more. | ✅ active |
| 9 | [dsh-skillport](https://github.com/Jesse-njx/dsh-skillport) | ⭐1 | Every skill you already have — Claude Code, Codex, Cursor, Gemini CLI — works in DSH. | ✅ active |
| 10 | [dsh-skillradar](https://github.com/hellosky983/dsh-skillradar) | ⭐1 | Scans session-visible skills and ranks them by relevance to the recent conversation. | ✅ active |

#### Complete list (14)

- [dsh-skill-viewer](https://github.com/Fishquito7/dsh-skill-viewer) ⭐12 — DSH Web UI plugin: Skills settings section with hot enable/disable, delete and add. (✅ active)
- [dsh-plugin-dev](https://github.com/omdsh-dev/dsh-plugin-dev) ⭐9 — Field-tested plugin development playbook (skill + docs): cordis dual copies, tsconfig triplets, Windows junctions and multi-frame zstd. (✅ active)
- [dsh-plugin-skills](https://github.com/omdsh-dev/dsh-plugin-skills) ⭐7 — Agent skills for building and testing DeepSeek Harness plugins, from scaffolding a package to publishing. (✅ active)
- [dsh-book2skill](https://github.com/omdsh-dev/dsh-book2skill) ⭐3 — Book-to-skill plugin: a 5-stage long task that fetches, parses, understands, generates and installs a skill. (✅ active)
- [dsh-godot-skill](https://github.com/akira399/dsh-godot-skill) ⭐2 — Godot Engine 4.x full-stack game development skill plugin for DSH. (✅ active)
- [dsh-review-skills](https://github.com/ben7am1n/dsh-review-skills) ⭐2 — Code review skill pack for DeepSeek Harness. (✅ active)
- [dsh-find-skill](https://github.com/Moximxxx/dsh-find-skill) ⭐1 — Bridges the vercel-labs/skills ecosystem: LLM-driven skill search, install and management. (✅ active)
- [dsh-skill-pack-security](https://github.com/PerryLink/dsh-skill-pack-security) ⭐1 — Security-audit skill pack: 5 agent skills covering secret scan, dependency audit and more. (✅ active)
- [dsh-skillport](https://github.com/Jesse-njx/dsh-skillport) ⭐1 — Every skill you already have — Claude Code, Codex, Cursor, Gemini CLI — works in DSH. (✅ active)
- [dsh-skillradar](https://github.com/hellosky983/dsh-skillradar) ⭐1 — Scans session-visible skills and ranks them by relevance to the recent conversation. (✅ active)
- [deepseek-harness-skillx](https://github.com/drowned-fish1/deepseek-harness-skillx)  — Skill collection for DeepSeek Harness workflows. (✅ active)
- [dsh-humanize](https://github.com/zevorn/dsh-humanize)  — De-AI writing skill: rewrite agent output to sound more human. (✅ active)
- [dsh-news-briefing](https://github.com/canghai666x/dsh-news-briefing)  — News briefing skill: multi-dimensional story scoring, anti-clickbait rules, content prioritization and Chinese editorial style. (✅ active)
- [dsh-web-novel-research](https://github.com/canghai666x/dsh-web-novel-research)  — Chinese web-novel plot lookup skill: free mirror-site workflow with GBK decoding and duplicate-chapter disambiguation. (✅ active)

### Workflows & Automation


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [dsh_workflow](https://github.com/icetomoyo/dsh_workflow) | ⭐54 | Brings Claude Code's UltraCode mode to DSH: upgrade one-shot multi-agent dispatch into a generatable, saveable, governable, observable, recoverable workflow layer. | ✅ active |
| 2 | [mstar-harness](https://github.com/btspoony/mstar-harness) | ⭐42 | Skill-driven harness/loop engineering workflow agent: tune agent loops as a first-class workflow. | ✅ active |
| 3 | [dsh-automation](https://github.com/titanwings/dsh-automation) | ⭐27 | Run coding tasks on a schedule in fresh Agent sessions, managed by the user or the agent itself. | ✅ active |
| 4 | [dsh-auto-continue](https://github.com/HsiangNianian/dsh-auto-continue) | ⭐9 | Auto-resumes interrupted DSH Web requests: failure classification, adaptive retry, configurable continue message and browser notifications. | ✅ active |
| 5 | [dsh-deep-research](https://github.com/omdsh-dev/dsh-deep-research) | ⭐9 | Adaptive deep-research orchestrator built on the official workflow engine. | ✅ active |
| 6 | [dsh-harness-ops](https://github.com/fakechris/dsh-harness-ops) | ⭐7 | Ops toolbox: A/B dual-slot daily snapshot rotation with atomic switch and one-click rollback, plus a 10s watchdog. | ✅ active |
| 7 | [dsh-track](https://github.com/fakechris/dsh-track) | ⭐5 | Embedded task-management engine: decision-point protocol, thought-capture wall and Linear-style issue storage. | ✅ active |
| 8 | [engineer-software](https://github.com/KirschBluteX/engineer-software) | ⭐5 | Runtime-neutral, evidence-driven software engineering workflow for Codex and DeepSeek Harness. | ✅ active |
| 9 | [dsh-companion](https://github.com/william-jin-cmu/dsh-companion) | ⭐4 | Resident desktop assistant: global hotkey, scheduled automation, quick replies and a plugin market. | ✅ active |
| 10 | [dsh-plans](https://github.com/Optim-Agent/dsh-plans) | ⭐4 | Human-in-the-loop planning preset adapted from prime-plans: researched, reviewed, executed. | ✅ active |

#### Complete list (20)

- [dsh_workflow](https://github.com/icetomoyo/dsh_workflow) ⭐54 — Brings Claude Code's UltraCode mode to DSH: upgrade one-shot multi-agent dispatch into a generatable, saveable, governable, observable, recoverable workflow layer. (✅ active)
- [mstar-harness](https://github.com/btspoony/mstar-harness) ⭐42 — Skill-driven harness/loop engineering workflow agent: tune agent loops as a first-class workflow. (✅ active)
- [dsh-automation](https://github.com/titanwings/dsh-automation) ⭐27 — Run coding tasks on a schedule in fresh Agent sessions, managed by the user or the agent itself. (✅ active)
- [dsh-auto-continue](https://github.com/HsiangNianian/dsh-auto-continue) ⭐9 — Auto-resumes interrupted DSH Web requests: failure classification, adaptive retry, configurable continue message and browser notifications. (✅ active)
- [dsh-deep-research](https://github.com/omdsh-dev/dsh-deep-research) ⭐9 — Adaptive deep-research orchestrator built on the official workflow engine. (✅ active)
- [dsh-harness-ops](https://github.com/fakechris/dsh-harness-ops) ⭐7 — Ops toolbox: A/B dual-slot daily snapshot rotation with atomic switch and one-click rollback, plus a 10s watchdog. (✅ active)
- [dsh-track](https://github.com/fakechris/dsh-track) ⭐5 — Embedded task-management engine: decision-point protocol, thought-capture wall and Linear-style issue storage. (✅ active)
- [engineer-software](https://github.com/KirschBluteX/engineer-software) ⭐5 — Runtime-neutral, evidence-driven software engineering workflow for Codex and DeepSeek Harness. (✅ active)
- [dsh-companion](https://github.com/william-jin-cmu/dsh-companion) ⭐4 — Resident desktop assistant: global hotkey, scheduled automation, quick replies and a plugin market. (✅ active)
- [dsh-plans](https://github.com/Optim-Agent/dsh-plans) ⭐4 — Human-in-the-loop planning preset adapted from prime-plans: researched, reviewed, executed. (✅ active)
- [dsh-deepresearch](https://github.com/havingautism/dsh-deepresearch) ⭐3 — DeepResearch plugin (cordis) for the Harness. (🧪 experimental)
- [dsh-inspect](https://github.com/omdsh-dev/dsh-inspect) ⭐3 — Adversarial checkup → fix → review loop built on the official workflow engine. (✅ active)
- [dsh-plugin-spur](https://github.com/HuanLinOTO/dsh-plugin-spur) ⭐3 — Hang a whip in the chat stream: flick it (>2.0 px/ms) to send the agent a 'go work' message. (✅ active)
- [dsh-prime-agent](https://github.com/yoke233/dsh-prime-agent) ⭐3 — Prime Agent-inspired persistent RLM control plane for DSH Code Mode. (✅ active)
- [dsh-doublecheck](https://github.com/PerryLink/dsh-doublecheck) ⭐1 — Engineering-discipline loop: requirement grilling before edits, red/green test-evidence gates and adversarial delivery review. (✅ active)
- [dsh-governance](https://github.com/tappass/dsh-governance) ⭐1 — Authority layer for agentic AI as a DSH plugin: governs every tool call against your policies. (✅ active)
- [dsh-eval](https://github.com/hccccc01333/dsh-eval)  — Agent evaluation platform: benchmark YAML, headless dsh runs, trace-based metrics, scripted grading and run comparison. (✅ active)
- [dsh-report-studio](https://github.com/ciceroyang/dsh-report-studio)  — Turn a DSH session into deliverable work reports (daily/weekly/handoff/article) with verifiable receipts. (✅ active)
- [dsh-task-dag](https://github.com/LeemanCheung/dsh-task-dag)  — Persistent live DAG visualization of workflow runs, subagents, status and dependencies. (✅ active)
- [dsh-trajectory-debug](https://github.com/devmom/dsh-trajectory-debug)  — Trajectory waterfall, deterministic replay, breakpoints, edit-and-rerun, fork compare and performance analytics. (✅ active)

### Agents & Multi-Agent


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [openbiliclaw](https://github.com/whiteguo233/OpenBiliClaw) | ⭐2,324 | 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin） | ✅ active |
| 2 | [dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) | ⭐222 | Multi-agent team-oriented extensions for DSH. | ✅ active |
| 3 | [dsh-agent-rp](https://github.com/hewzhew/dsh-agent-rp) | ⭐101 | SillyTavern migration and next-generation Agent roleplay for DSH. | ✅ active |
| 4 | [allinluna](https://github.com/zenx0x/allinluna) | ⭐25 | Resource-aware multi-agent orchestration for Codex and DeepSeek Harness (All in Flash DSH plugin). | ✅ active |
| 5 | [dsh-interconnect](https://github.com/Chinesezjc/dsh-interconnect) | ⭐24 | Cross-instance message/event handoff plugins (interconnect service + tools). | ✅ active |
| 6 | [dsh-openbiliclaw](https://github.com/whiteguo233/dsh-openbiliclaw) | ⭐19 | OpenBiliClaw 是本地运行的跨平台个性化内容推荐 Agent，持续理解你的兴趣并主动找内容。本仓库是它的 DeepSeek Harness 插件：DSH 界面常驻第四栏（推荐/内容库/对话/画像/设置），注册 22 个 Agent Bridge 工具，让 Agent 也能读推荐、答探测、闭环学习。 | ✅ active |
| 7 | [dsh-tianshu-build](https://github.com/huiliyi37/dsh-tianshu-build) | ⭐19 | DeepSeek X Tianshu  Harness build 是一款完全体开源 coding agent:在 dsh harness 基础之上带视觉、跨会话记忆、验证门、agent 路由、语义 + 图谱代码检索、文件回滚和全屏终端 UI——全部以插件组合。  它是 DeepSeek Harness(dsh)的友好 MIT fork, 它保留了上游一切皆插件的架构，并将以harness最佳形态和架构往下演进。 | ✅ active |
| 8 | [dsh-data-agent](https://github.com/omdsh-dev/dsh-data-agent) | ⭐17 | Session-scoped database connections with a dedicated data agent: let the model connect to databases and write SQL. | ✅ active |
| 9 | [dsh-plugin-cc](https://github.com/cpj-dev/dsh-plugin-cc) | ⭐12 | Bridge DeepSeek Harness into Claude Code for review, critique, delegation and session import. | ✅ active |
| 10 | [dsh-plugin-product-subagents](https://github.com/shaokeyibb/dsh-plugin-product-subagents) | ⭐8 | Role-based Codex/Claude Code/ACP subagent providers: continuable children with durable state. | ✅ active |

#### Complete list (23)

- [openbiliclaw](https://github.com/whiteguo233/OpenBiliClaw) ⭐2,324 — 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin） (✅ active)
- [dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) ⭐222 — Multi-agent team-oriented extensions for DSH. (✅ active)
- [dsh-agent-rp](https://github.com/hewzhew/dsh-agent-rp) ⭐101 — SillyTavern migration and next-generation Agent roleplay for DSH. (✅ active)
- [allinluna](https://github.com/zenx0x/allinluna) ⭐25 — Resource-aware multi-agent orchestration for Codex and DeepSeek Harness (All in Flash DSH plugin). (✅ active)
- [dsh-interconnect](https://github.com/Chinesezjc/dsh-interconnect) ⭐24 — Cross-instance message/event handoff plugins (interconnect service + tools). (✅ active)
- [dsh-openbiliclaw](https://github.com/whiteguo233/dsh-openbiliclaw) ⭐19 — OpenBiliClaw 是本地运行的跨平台个性化内容推荐 Agent，持续理解你的兴趣并主动找内容。本仓库是它的 DeepSeek Harness 插件：DSH 界面常驻第四栏（推荐/内容库/对话/画像/设置），注册 22 个 Agent Bridge 工具，让 Agent 也能读推荐、答探测、闭环学习。 (✅ active)
- [dsh-tianshu-build](https://github.com/huiliyi37/dsh-tianshu-build) ⭐19 — DeepSeek X Tianshu  Harness build 是一款完全体开源 coding agent:在 dsh harness 基础之上带视觉、跨会话记忆、验证门、agent 路由、语义 + 图谱代码检索、文件回滚和全屏终端 UI——全部以插件组合。  它是 DeepSeek Harness(dsh)的友好 MIT fork, 它保留了上游一切皆插件的架构，并将以harness最佳形态和架构往下演进。 (✅ active)
- [dsh-data-agent](https://github.com/omdsh-dev/dsh-data-agent) ⭐17 — Session-scoped database connections with a dedicated data agent: let the model connect to databases and write SQL. (✅ active)
- [dsh-plugin-cc](https://github.com/cpj-dev/dsh-plugin-cc) ⭐12 — Bridge DeepSeek Harness into Claude Code for review, critique, delegation and session import. (✅ active)
- [dsh-plugin-product-subagents](https://github.com/shaokeyibb/dsh-plugin-product-subagents) ⭐8 — Role-based Codex/Claude Code/ACP subagent providers: continuable children with durable state. (✅ active)
- [dsh-advisor](https://github.com/omdsh-dev/dsh-advisor) ⭐5 — Pair a second model that passively reviews each turn and injects notes. (✅ active)
- [dsh-plugin-claude-bridge](https://github.com/YYTbit/dsh-plugin-claude-bridge) ⭐5 — Bridge Claude Code memory, skills and config into DeepSeek Harness. (✅ active)
- [dsh-plugin-yet-another-subagent](https://github.com/HuanLinOTO/dsh-plugin-yet-another-subagent) ⭐5 — Configurable subagent profile system: a single subagent tool with profile parameters, Web UI settings and live progress. (✅ active)
- [Task Passport](https://github.com/dongsheng123132/task-passport) ⭐5 — Open task handoff protocol for DeepSeek Harness, WorkBuddy, Claude Code and Codex: verified state, not chat logs. (✅ active)
- [dsh-agent-messaging](https://github.com/happyren/dsh-agent-messaging) ⭐4 — Cross-session agent-to-agent messaging: address another session by name. (✅ active)
- [dsh-sidechain](https://github.com/omdsh-dev/dsh-sidechain) ⭐4 — Side sessions: persistent /side sessions (Codex style) and one-off /btw questions (Claude style) in temporary forks. (✅ active)
- [dsh-a2a](https://github.com/dpskh/dsh-a2a) ⭐2 — Agent2Agent mesh for the Harness. (✅ active)
- [dsh-llm-fallbacks](https://github.com/omdsh-dev/dsh-llm-fallbacks) ⭐2 — Role-based LLM retry and fallback strategy plugin. (✅ active)
- [dsh-cross-session](https://github.com/Wha1eChai/dsh-cross-session) ⭐1 — Same-runtime cross-session discovery and communication for DeepSeek Harness. (✅ active)
- [dsh-crosstalk](https://github.com/Jesse-njx/dsh-crosstalk) ⭐1 — Cross-session messaging: DSH sessions on the same machine can discover, message and coordinate with each other. (✅ active)
- [dsh-slice-agent-loop](https://github.com/TT-Wang/dsh-slice-agent-loop) ⭐1 — Drop-in agent loop whose context engine is a bounded slice instead of a growing transcript. (✅ active)
- [dsh-subagent-tools](https://github.com/lynx-gt/dsh-subagent-tools) ⭐1 — Per-call model/provider/persona/toolFilter overrides for subagent delegation with @preset references. (✅ active)
- [dsh-supervisor](https://github.com/Wha1eChai/dsh-supervisor) ⭐1 — Same-runtime cross-session discovery and communication for DeepSeek Harness. (✅ active)

### Clients (Desktop & TUI)


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [deepseek-harness-desktop (Anywhere Labs)](https://github.com/anywhere-labs/deepseek-harness-desktop) | ⭐962 | Modern desktop experience built for the DeepSeek Harness ecosystem (plugin). | ✅ active |
| 2 | [dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) | ⭐793 | Claude Code-style full-screen terminal plugin: pixel-whale top bar, live status line, streaming thoughts, double-Esc rollback, context progress bar and TPS meter. | ✅ active |
| 3 | [oh-dsh](https://github.com/hust-open-atom-club/oh-dsh) | ⭐160 | One-stop community distribution: TUI, desktop and Web UI in a unified experience with layered installation. | ✅ active |
| 4 | [dsh-desktop (DataElement)](https://github.com/dataelement/dsh-desktop) | ⭐140 | Desktop app for DeepSeek Harness. | ✅ active |
| 5 | [dsh-tianshu-tui](https://github.com/huiliyi37/dsh-tianshu-tui) | ⭐125 | Interactive terminal UI plugin for DSH with added TDD, evidence gates and vision modules. | ✅ active |
| 6 | [deepseek-harness-desktop (steven-kid)](https://github.com/steven-kid/deepseek-harness-desktop) | ⭐104 | Minimal cross-platform desktop wrapper: no config, out of the box. | ✅ active |
| 7 | [dsh_desktop](https://github.com/myYangyunfan/dsh_desktop) | ⭐74 | DeepSeek Harness (dsh) Windows desktop client - bundled Node.js + dsh CLI, one-click launch | ✅ active |
| 8 | [deepseek-harness-desktop (salathleizhang)](https://github.com/salathleizhang/deepseek-harness-desktop) | ⭐67 | Desktop wrapper for DeepSeek Harness. | ✅ active |
| 9 | [dsh-launcher](https://github.com/Ruler4396/dsh-launcher) | ⭐65 | Lightweight Windows launcher: silent autostart at logon plus a minimal WebView2 window. | ✅ active |
| 10 | [deepseek-harness-desktop (hairyf)](https://github.com/hairyf/deepseek-harness-desktop) | ⭐63 | One-click desktop app: fully local with self-healing core updates, zero environment setup. Windows/macOS/Linux. | ✅ active |

#### Complete list (35)

- [deepseek-harness-desktop (Anywhere Labs)](https://github.com/anywhere-labs/deepseek-harness-desktop) ⭐962 — Modern desktop experience built for the DeepSeek Harness ecosystem (plugin). (✅ active)
- [dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) ⭐793 — Claude Code-style full-screen terminal plugin: pixel-whale top bar, live status line, streaming thoughts, double-Esc rollback, context progress bar and TPS meter. (✅ active)
- [oh-dsh](https://github.com/hust-open-atom-club/oh-dsh) ⭐160 — One-stop community distribution: TUI, desktop and Web UI in a unified experience with layered installation. (✅ active)
- [dsh-desktop (DataElement)](https://github.com/dataelement/dsh-desktop) ⭐140 — Desktop app for DeepSeek Harness. (✅ active)
- [dsh-tianshu-tui](https://github.com/huiliyi37/dsh-tianshu-tui) ⭐125 — Interactive terminal UI plugin for DSH with added TDD, evidence gates and vision modules. (✅ active)
- [deepseek-harness-desktop (steven-kid)](https://github.com/steven-kid/deepseek-harness-desktop) ⭐104 — Minimal cross-platform desktop wrapper: no config, out of the box. (✅ active)
- [dsh_desktop](https://github.com/myYangyunfan/dsh_desktop) ⭐74 — DeepSeek Harness (dsh) Windows desktop client - bundled Node.js + dsh CLI, one-click launch (✅ active)
- [deepseek-harness-desktop (salathleizhang)](https://github.com/salathleizhang/deepseek-harness-desktop) ⭐67 — Desktop wrapper for DeepSeek Harness. (✅ active)
- [dsh-launcher](https://github.com/Ruler4396/dsh-launcher) ⭐65 — Lightweight Windows launcher: silent autostart at logon plus a minimal WebView2 window. (✅ active)
- [deepseek-harness-desktop (hairyf)](https://github.com/hairyf/deepseek-harness-desktop) ⭐63 — One-click desktop app: fully local with self-healing core updates, zero environment setup. Windows/macOS/Linux. (✅ active)
- [deepseek-harness-desktop (xiincs)](https://github.com/xiincs/deepseek-harness-desktop) ⭐53 — Native desktop built on Tauri 2 with bundled Node.js runtime, tray residency and auto-update. (✅ active)
- [Deepseek-Harness-Desktop (ChisaAlter)](https://github.com/ChisaAlter/Deepseek-Harness-Desktop) ⭐50 — Electron desktop shell with theme and background-image customization. (✅ active)
- [dsh-multica-runtime](https://github.com/multica-ai/dsh-multica-runtime) ⭐27 — Support the dsh runtime on Multica. (✅ active)
- [dsh-work](https://github.com/vibeinging/dsh-work) ⭐25 — Local-first AI workbench for DSH Plugins, combining Agent sessions, project files, data analysis, web research, MCP, and Office artifacts in an Electron desktop app. (✅ active)
- [deepseek-harness-app (ipfred)](https://github.com/ipfred/deepseek-harness-app) ⭐23 — Desktop app for DeepSeek Harness. (✅ active)
- [deepseek-harness-desktop (hongfeiyucode)](https://github.com/hongfeiyucode/deepseek-harness-desktop) ⭐23 — Desktop wrapper for DeepSeek Harness. (✅ active)
- [deepseek-harness-desktop (ningbainb)](https://github.com/ningbainb/deepseek-harness-desktop) ⭐21 — Lossless Windows desktop app with the complete DSH Web UI, plugins, skins and skill dock. (✅ active)
- [DeepSeekHarnessDesktop (wess09)](https://github.com/wess09/DeepSeekHarnessDesktop) ⭐20 — Desktop packaging for DeepSeek Harness. (✅ active)
- [dsh-desktop (bruc3van)](https://github.com/bruc3van/dsh-desktop) ⭐20 — Third-party desktop client loading the official Web UI: reuses a running official instance or a bundled dsh runtime. (✅ active)
- [DeepSeek Harness TUI (openma-ai)](https://github.com/openma-ai/deepseek-harness-tui) ⭐15 — Rust/Ratatui terminal client speaking the DSH SDK JSON-RPC protocol directly; runs standalone or as a profile bundle. (✅ active)
- [deepseek-harness-desktop (cc1252)](https://github.com/cc1252/deepseek-harness-desktop) ⭐14 — Unofficial open-source Windows Electron wrapper for DeepSeek Harness. (✅ active)
- [DeepSeek-Harness-Desktop (sleep2agi)](https://github.com/sleep2agi/DeepSeek-Harness-Desktop) ⭐11 — Unofficial community desktop shell for the public dsh runtime. (✅ active)
- [awesome-deepseek-harness-desktop (ADHD)](https://github.com/omdsh-dev/awesome-deepseek-harness-desktop) ⭐10 — ADHD — out-of-the-box Electron desktop wrapper for DeepSeek Harness. (✅ active)
- [deepseek-harness-desktop (chyra-moon)](https://github.com/chyra-moon/deepseek-harness-desktop) ⭐10 — Native Windows desktop shell: 1:1 official web UI with embedded server, tray and auto-recovery. (✅ active)
- [deepseek-harness-termux](https://github.com/Vengisk/deepseek-harness-termux) ⭐9 — Run @deepseek-ai/dsh on Android/Termux. (✅ active)
- [deepseek-harness-desktop](https://github.com/omdsh-dev/deepseek-harness-desktop) ⭐7 — DSH 桌面应用打包器 (✅ active)
- [deepseek-harness-desktop](https://github.com/qyqy-1109/deepseek-harness-desktop) ⭐6 — DeepSeek Harness Desktop: self-contained Windows desktop shell (Electron) that auto-starts dsh web, plus a subtle Codex-flavored theme plugin. (✅ active)
- [deepseek-harness-tui (gxinxing)](https://github.com/gxinxing/deepseek-harness-tui) ⭐6 — Terminal-native interactive TUI built with Ink (React for terminals). (✅ active)
- [deepseek-harness-cli](https://github.com/Richard-Yang0130/deepseek-harness-cli) ⭐5 — Claude Code-style terminal interface for DeepSeek Harness (✅ active)
- [deepseek-harness-desktop](https://github.com/RZX00/deepseek-harness-desktop) ⭐5 — DeepSeek Harness with a Windows desktop build: an Electron shell over the dsh web profile, packaged as an installer (✅ active)
- [deepseek-harness-tui (boxeryao)](https://github.com/boxeryao/deepseek-harness-tui) ⭐5 — Lightweight fast terminal plugin connected directly to the DSH runtime. (✅ active)
- [deepseek-harness-fnos](https://github.com/techysy/deepseek-harness-fnos) ⭐4 — DeepSeek Harness (DeepSeek 官方 agent 浏览器 UI) fnOS 应用 — 本地常驻服务, 官方统一网关接入 (✅ active)
- [dsh-desktop-electron](https://github.com/Void0312Aurora/dsh-desktop-electron) ⭐4 — Cross-platform Electron shell for the DSH Web GUI: tray-resident standalone window. (✅ active)
- [dsh-pi-tui](https://github.com/lqhl/dsh-pi-tui) ⭐1 — Pi TUI front end: streaming markdown, thinking collapse, tool cards, slash commands and approval overlays. (✅ active)
- [dsh-grok-tui](https://github.com/chen-001/dsh-grok-tui)  — TUI built with grok-build. (✅ active)

### MCP & Integrations


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [Coding Tools MCP](https://github.com/xyTom/coding-tools-mcp) | ⭐758 | Coding-oriented MCP tool collection that appears in the emerging DSH ecosystem: give any AI agent the ability to code. | ✅ active |
| 2 | [dsh-openpencil](https://github.com/ZSeven-W/dsh-openpencil) | ⭐64 | OpenPencil design preview and editing integration. | ✅ active |
| 3 | [dsh-lark](https://github.com/omdsh-dev/dsh-lark) | ⭐14 | Lark/Feishu IM bot channel for DeepSeek Harness | 飞书 DeepSeek Harness 插件 | ✅ active |
| 4 | [deepseek-harness-acp](https://github.com/openma-ai/deepseek-harness-acp) | ⭐6 | ACP server implementation for DeepSeek Harness: exposes the full DSH agent to ACP clients while reusing credentials and sessions. | ✅ active |
| 5 | [deepseek-harness-docker](https://github.com/runzhliu/deepseek-harness-docker) | ⭐6 | Community Docker and Kubernetes packaging for @deepseek-ai/dsh with a hardened image. | ✅ active |
| 6 | [dsh-oauth-mcp-client](https://github.com/springbrand-lab/dsh-oauth-mcp-client) | ⭐6 | OAuth 2.1 Streamable HTTP MCP client plugin for DeepSeek Harness. | ✅ active |
| 7 | [deepseek-harness-action](https://github.com/Lixiaoyiao/deepseek-harness-action) | ⭐5 | Community GitHub Action: AI code review, CI diagnosis, auto-fix and issue-to-PR implementation. | ✅ active |
| 8 | [dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) | ⭐5 | MCP server manager: Settings page with OAuth (PKCE + dynamic client registration) or static-token auth. | ✅ active |
| 9 | [deepseek-harness-vsc-extension](https://github.com/weinibuliu/deepseek-harness-vsc-extension) | ⭐4 | DeepSeek Harness for VS Code as extension | ✅ active |
| 10 | [DSH Telegram Relay](https://github.com/congchuanling-dot/DSH-Telegram-Relay) | ⭐4 | Relay that turns Telegram into a remote conversation channel for DSH with notifications. | ✅ active |

#### Complete list (25)

- [Coding Tools MCP](https://github.com/xyTom/coding-tools-mcp) ⭐758 — Coding-oriented MCP tool collection that appears in the emerging DSH ecosystem: give any AI agent the ability to code. (✅ active)
- [dsh-openpencil](https://github.com/ZSeven-W/dsh-openpencil) ⭐64 — OpenPencil design preview and editing integration. (✅ active)
- [dsh-lark](https://github.com/omdsh-dev/dsh-lark) ⭐14 — Lark/Feishu IM bot channel for DeepSeek Harness | 飞书 DeepSeek Harness 插件 (✅ active)
- [deepseek-harness-acp](https://github.com/openma-ai/deepseek-harness-acp) ⭐6 — ACP server implementation for DeepSeek Harness: exposes the full DSH agent to ACP clients while reusing credentials and sessions. (✅ active)
- [deepseek-harness-docker](https://github.com/runzhliu/deepseek-harness-docker) ⭐6 — Community Docker and Kubernetes packaging for @deepseek-ai/dsh with a hardened image. (✅ active)
- [dsh-oauth-mcp-client](https://github.com/springbrand-lab/dsh-oauth-mcp-client) ⭐6 — OAuth 2.1 Streamable HTTP MCP client plugin for DeepSeek Harness. (✅ active)
- [deepseek-harness-action](https://github.com/Lixiaoyiao/deepseek-harness-action) ⭐5 — Community GitHub Action: AI code review, CI diagnosis, auto-fix and issue-to-PR implementation. (✅ active)
- [dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) ⭐5 — MCP server manager: Settings page with OAuth (PKCE + dynamic client registration) or static-token auth. (✅ active)
- [deepseek-harness-vsc-extension](https://github.com/weinibuliu/deepseek-harness-vsc-extension) ⭐4 — DeepSeek Harness for VS Code as extension (✅ active)
- [DSH Telegram Relay](https://github.com/congchuanling-dot/DSH-Telegram-Relay) ⭐4 — Relay that turns Telegram into a remote conversation channel for DSH with notifications. (✅ active)
- [dsh-telegram-channel](https://github.com/hi-wenw/dsh-telegram-channel) ⭐4 — Telegram mobile remote for live DSH Web sessions: session picker, bind/unbind, same trajectory as desktop. (✅ active)
- [PicGo DSH Plugin](https://github.com/PicGo/dsh-plugin) ⭐4 — Official PicGo plugin: upload images/files to your image host from DSH and get public URLs. (✅ active)
- [dsh-browser](https://github.com/xylt369/dsh-browser) ⭐3 — Browser capability for DeepSeek Harness: headed Edge/Playwright provider, SSRF-safe navigation, a11y-ref clicking, permission gate with auto-remember, gated evaluate (✅ active)
- [dsh-mcp-panel](https://github.com/PerryLink/dsh-mcp-panel) ⭐3 — Read-only runtime management panel for the official DSH MCP client: /mcp command and a Settings tab. (✅ active)
- [dsh-search-mcp](https://github.com/gxpppp/dsh-search-mcp) ⭐3 — Replace DSH's built-in web search with search MCP servers (Tavily/Brave/Exa/Perplexity/DuckDuckGo). (✅ active)
- [dsh-harness-mcp-server](https://github.com/chushixixin/dsh-harness-mcp-server) ⭐2 — Expose DeepSeek Harness agent capabilities as an MCP server (brain=Hermes, arms=Harness). (✅ active)
- [dsh-chrome](https://github.com/YJSoooooo/dsh-chrome) ⭐1 — Chrome profile bridge: control an existing signed-in Chrome profile through Chrome DevTools Protocol. (✅ active)
- [vscode-deepseek-harness](https://github.com/kalynnka/vscode-deepseek-harness) ⭐1 — Unofficial: drive your own dsh as a native VS Code chat agent. (✅ active)
- [deepseek-harness-rs](https://github.com/Tokimorphling/deepseek-harness-rs)  — A Rust port of DeepSeek Harness. (🧪 experimental)
- [dsh-github-integration](https://github.com/omdsh-dev/dsh-github-integration)  — GitHub integration plugin for DSH. (✅ active)
- [dsh-lan-access](https://github.com/Leon0555/dsh-lan-access)  — LAN access for the Web GUI: 0.0.0.0 bind plus a crypto.randomUUID polyfill for non-secure contexts. (✅ active)
- [dsh-super-injector](https://github.com/yjh051108/dsh-super-injector)  — Super-injector plugin (cordis) for context injection. (✅ active)
- [dsh4vscode](https://github.com/DoggyHU/dsh4vscode)  — VS Code chat windows backed by the DSH agent: OpenCode-style independent sessions with model auto-routing. (✅ active)
- [opendsh](https://github.com/TheChengXi/opendsh)  — Open the DeepSeek Harness Web UI inside VS Code with one-command start/stop. (✅ active)
- [URL Manager MCP](https://github.com/Piccolo123/url-manager-mcp)  — MCP companion for URL Manager: 21 tools for save/search/categorize/share with magic-link delivery. (✅ active)

### Examples & Starters


#### 🔥 Top 7

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [hello-dsh](https://github.com/pingfanfan/hello-dsh) | ⭐37 | Zero-to-plugin tutorial: understand 'everything is a plugin' with 22 Chinese skill examples. | ✅ active |
| 2 | [dsh-plugin-template](https://github.com/bugmaker2/dsh-plugin-template) | ⭐16 | Template for DeepSeek Harness plugin development. | ✅ active |
| 3 | [turtle-ui](https://github.com/turtle1999/turtle-ui) | ⭐6 | Official UI plugin reference implementation. | ✅ active |
| 4 | [dsh-101](https://github.com/bill9109/dsh-101) | ⭐2 | DSH documentation reading mode. | ✅ active |
| 5 | [dsh-plugin-template (sunshine-lang)](https://github.com/sunshine-lang/dsh-plugin-template) | ⭐2 | Ready-to-publish plugin skeleton: bundle format, tool DSL, config and tests. | ✅ active |
| 6 | [dsh-plugin-hello](https://github.com/xu1132/dsh-plugin-hello) |  | Hello-world style starter plugin for DSH. | ✅ active |
| 7 | [plugin-template (omdsh-dev)](https://github.com/omdsh-dev/plugin-template) |  | Plugin template repository derived from the original turtle-ui official repo. | ✅ active |

#### Complete list (7)

- [hello-dsh](https://github.com/pingfanfan/hello-dsh) ⭐37 — Zero-to-plugin tutorial: understand 'everything is a plugin' with 22 Chinese skill examples. (✅ active)
- [dsh-plugin-template](https://github.com/bugmaker2/dsh-plugin-template) ⭐16 — Template for DeepSeek Harness plugin development. (✅ active)
- [turtle-ui](https://github.com/turtle1999/turtle-ui) ⭐6 — Official UI plugin reference implementation. (✅ active)
- [dsh-101](https://github.com/bill9109/dsh-101) ⭐2 — DSH documentation reading mode. (✅ active)
- [dsh-plugin-template (sunshine-lang)](https://github.com/sunshine-lang/dsh-plugin-template) ⭐2 — Ready-to-publish plugin skeleton: bundle format, tool DSL, config and tests. (✅ active)
- [dsh-plugin-hello](https://github.com/xu1132/dsh-plugin-hello)  — Hello-world style starter plugin for DSH. (✅ active)
- [plugin-template (omdsh-dev)](https://github.com/omdsh-dev/plugin-template)  — Plugin template repository derived from the original turtle-ui official repo. (✅ active)

### Tutorials & Learning


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [DeepSeek Harness Orange Book](https://github.com/alchaincyf/deepseek-harness-orange-book) | ⭐465 | Community Orange Book: complete system prompts, a 129-line startup checklist and three raw session logs — first-hand testing the official docs lack. Free PDF/EPUB/HTML. | ✅ active |
| 2 | [dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) | ⭐167 | From 0 to 1 handbook: installation, plugin development, performance tuning, real-world cases and same-model multi-agent comparisons (CN + EN PDF). | ✅ active |
| 3 | [dshfind](https://github.com/hikariming/dshfind) | ⭐56 | Learn DSH principles, plugin marketplace and best practices — from chapter-by-chapter Cordis paper reading to an auto-aggregated plugin market. | ✅ active |
| 4 | [dsh-harness-tutorial](https://github.com/yanhua1010/dsh-harness-tutorial) | ⭐32 | DeepSeek Harness Agent 的原理与实现：从零到一实现一个 AI Agent —— 一切皆插件的中文教程（VitePress 站点 + 8 个 Demo + mini-harness 教学项目） | ✅ active |
| 5 | [deepseek-harness-tutorial](https://github.com/ht426/deepseek-harness-tutorial) | ⭐17 | Detailed Chinese learning tutorial for DeepSeek Harness. | ✅ active |
| 6 | [dsh-explain](https://github.com/yuezengwu/dsh-explain) | ⭐9 | Local-first learning mode: cross-session global learning threads, explain-by-source, ExplainContext and compression. | ✅ active |
| 7 | [deepseek-harness-prompts](https://github.com/demouo/deepseek-harness-prompts) | ⭐6 | DeepSeek Harness prompts for different modes. | ✅ active |
| 8 | [deepseek-harness-learning](https://github.com/Lucky2024-pllove/deepseek-harness-learning) | ⭐5 | Learning website built from a systematic breakdown of the deepseek-harness repository, for developers curious how AI agent frameworks work. | ✅ active |
| 9 | [dsh-book-deepseek-harness](https://github.com/LaplaceYoung/dsh-book-deepseek-harness) | ⭐5 | 'Deep Dive into DeepSeek Harness' — source-level architecture book: 37 chapter files, PDF, Mermaid diagrams and writing conventions. | ✅ active |
| 10 | [dsh-learn-everything](https://github.com/cendaifeng/dsh-learn-everything) | ⭐3 | Feynman learning-mode plugin: teach → teach-back → judge → re-explain loop rendered as rich HTML lesson cards. | ✅ active |

#### Complete list (11)

- [DeepSeek Harness Orange Book](https://github.com/alchaincyf/deepseek-harness-orange-book) ⭐465 — Community Orange Book: complete system prompts, a 129-line startup checklist and three raw session logs — first-hand testing the official docs lack. Free PDF/EPUB/HTML. (✅ active)
- [dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) ⭐167 — From 0 to 1 handbook: installation, plugin development, performance tuning, real-world cases and same-model multi-agent comparisons (CN + EN PDF). (✅ active)
- [dshfind](https://github.com/hikariming/dshfind) ⭐56 — Learn DSH principles, plugin marketplace and best practices — from chapter-by-chapter Cordis paper reading to an auto-aggregated plugin market. (✅ active)
- [dsh-harness-tutorial](https://github.com/yanhua1010/dsh-harness-tutorial) ⭐32 — DeepSeek Harness Agent 的原理与实现：从零到一实现一个 AI Agent —— 一切皆插件的中文教程（VitePress 站点 + 8 个 Demo + mini-harness 教学项目） (✅ active)
- [deepseek-harness-tutorial](https://github.com/ht426/deepseek-harness-tutorial) ⭐17 — Detailed Chinese learning tutorial for DeepSeek Harness. (✅ active)
- [dsh-explain](https://github.com/yuezengwu/dsh-explain) ⭐9 — Local-first learning mode: cross-session global learning threads, explain-by-source, ExplainContext and compression. (✅ active)
- [deepseek-harness-prompts](https://github.com/demouo/deepseek-harness-prompts) ⭐6 — DeepSeek Harness prompts for different modes. (✅ active)
- [deepseek-harness-learning](https://github.com/Lucky2024-pllove/deepseek-harness-learning) ⭐5 — Learning website built from a systematic breakdown of the deepseek-harness repository, for developers curious how AI agent frameworks work. (✅ active)
- [dsh-book-deepseek-harness](https://github.com/LaplaceYoung/dsh-book-deepseek-harness) ⭐5 — 'Deep Dive into DeepSeek Harness' — source-level architecture book: 37 chapter files, PDF, Mermaid diagrams and writing conventions. (✅ active)
- [dsh-learn-everything](https://github.com/cendaifeng/dsh-learn-everything) ⭐3 — Feynman learning-mode plugin: teach → teach-back → judge → re-explain loop rendered as rich HTML lesson cards. (✅ active)
- [deepseek-protocol-doctor](https://github.com/Whning0513/deepseek-protocol-doctor) ⭐1 — Checks DeepSeek tool loops, reasoning_content, strict schemas and captured SSE; also works as a DSH plugin. (✅ active)

### Awesome Lists & Registries


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | ⭐751 | Large curated list of installable DSH plugins (bilingual). | ✅ active |
| 2 | [awesome-dsh-plugins (Radar)](https://github.com/AdamPlatin123/awesome-dsh-plugins) | ⭐751 | Radar index repo: auto-scanning all discovered dsh plugin candidates with an evidence-based compatibility matrix. | ✅ active |
| 3 | [awesome-deepseek-harness (0xsline)](https://github.com/0xsline/awesome-deepseek-harness) | ⭐360 | Curated DSH ecosystem directory: plugins, tools and infrastructure from dsh-external/hub and the public dsh-plugin topic. | ✅ active |
| 4 | [notes (zhaoolee)](https://github.com/zhaoolee/notes) | ⭐138 | Open-source Smartisan Notes clone: Docker private deployment, skill invocation, dsh plugin support and one-click WeChat-format export. | ✅ active |
| 5 | [awesome-dsh-plugin (bruc3van)](https://github.com/bruc3van/awesome-dsh-plugin) | ⭐86 | Find the right DSH plugin in 30 seconds: what problem each plugin solves, who it is for and where to start. | ✅ active |
| 6 | [Awesome-DeepSeek-Harness-Plugins](https://github.com/Zhiyuan-Fan/Awesome-DeepSeek-Harness-Plugins) | ⭐47 | Curated list of DeepSeek Harness plugins. | ✅ active |
| 7 | [awesome-DSH-plugin (Alex-Yanggg)](https://github.com/Alex-Yanggg/awesome-DSH-plugin) | ⭐47 | Meticulously curated list of plugins, extensions, tools and development resources for DSH. | ✅ active |
| 8 | [oh-my-dsh](https://github.com/LaplaceYoung/oh-my-dsh) | ⭐43 | Plugin ecosystem for DSH: 700+ plugins registered only through extension seams, without modifying the agent-loop skeleton. | ✅ active |
| 9 | [plugin-registry](https://github.com/vlln/plugin-registry) | ⭐31 | DSH plugin ecosystem infrastructure: thin console to manage official repository plugins (0 patch) plus the make-dsh-plugin skill. | ✅ active |
| 10 | [awesome-deepseek-harness (Dominic789654)](https://github.com/Dominic789654/awesome-deepseek-harness) | ⭐30 | Curated list of plugins, skills, MCP servers, patch/profile layers, orchestrators and UIs for DeepSeek Harness. | ✅ active |

#### Complete list (25)

- [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) ⭐751 — Large curated list of installable DSH plugins (bilingual). (✅ active)
- [awesome-dsh-plugins (Radar)](https://github.com/AdamPlatin123/awesome-dsh-plugins) ⭐751 — Radar index repo: auto-scanning all discovered dsh plugin candidates with an evidence-based compatibility matrix. (✅ active)
- [awesome-deepseek-harness (0xsline)](https://github.com/0xsline/awesome-deepseek-harness) ⭐360 — Curated DSH ecosystem directory: plugins, tools and infrastructure from dsh-external/hub and the public dsh-plugin topic. (✅ active)
- [notes (zhaoolee)](https://github.com/zhaoolee/notes) ⭐138 — Open-source Smartisan Notes clone: Docker private deployment, skill invocation, dsh plugin support and one-click WeChat-format export. (✅ active)
- [awesome-dsh-plugin (bruc3van)](https://github.com/bruc3van/awesome-dsh-plugin) ⭐86 — Find the right DSH plugin in 30 seconds: what problem each plugin solves, who it is for and where to start. (✅ active)
- [Awesome-DeepSeek-Harness-Plugins](https://github.com/Zhiyuan-Fan/Awesome-DeepSeek-Harness-Plugins) ⭐47 — Curated list of DeepSeek Harness plugins. (✅ active)
- [awesome-DSH-plugin (Alex-Yanggg)](https://github.com/Alex-Yanggg/awesome-DSH-plugin) ⭐47 — Meticulously curated list of plugins, extensions, tools and development resources for DSH. (✅ active)
- [oh-my-dsh](https://github.com/LaplaceYoung/oh-my-dsh) ⭐43 — Plugin ecosystem for DSH: 700+ plugins registered only through extension seams, without modifying the agent-loop skeleton. (✅ active)
- [plugin-registry](https://github.com/vlln/plugin-registry) ⭐31 — DSH plugin ecosystem infrastructure: thin console to manage official repository plugins (0 patch) plus the make-dsh-plugin skill. (✅ active)
- [awesome-deepseek-harness (Dominic789654)](https://github.com/Dominic789654/awesome-deepseek-harness) ⭐30 — Curated list of plugins, skills, MCP servers, patch/profile layers, orchestrators and UIs for DeepSeek Harness. (✅ active)
- [awesome-deepseek-harness (libukai)](https://github.com/libukai/awesome-deepseek-harness) ⭐29 — Ultimate guide: quick start, resources, curated plugins and practical tools. (✅ active)
- [oh-my-dsh](https://github.com/like-study1/Oh-My-DSH) ⭐21 — 🐳 DeepSeek Harness 插件聚合社区 — 自动同步 dsh-plugin 生态 · 精选目录 · 每 8 小时自动维护 | Oh-My-DSH: a community-maintained catalog of DeepSeek Harness plugins, auto-synced from the dsh-plugin topic (✅ active)
- [deepseek-plugin-store](https://github.com/Ericwong5021/deepseek-plugin-store) ⭐12 — DeepSeek Harness 独立社区插件商店：发现、安装并提交经过验证的插件、工具与扩展。 | Independent community plugin directory. (✅ active)
- [dsh-suite](https://github.com/whyihaveyou/dsh-suite) ⭐11 — Living DSH plugin directory (785+ plugins, refreshed hourly) with daily compatibility CI, a bilingual catalog site and an in-app plugin store. (✅ active)
- [dsh-meme-hub](https://github.com/the-beating-light-of-the-nail/dsh-meme-hub) ⭐9 — Curated navigation of community meme plugins (skins, desktop pets, mini-games), bilingual. (✅ active)
- [awesome-dsh-plugins (white0dew)](https://github.com/white0dew/awesome-dsh-plugins) ⭐7 — Public GitHub directory for DSH plugins with install commands. (✅ active)
- [awesome-deepseek-harness (jiji262)](https://github.com/jiji262/awesome-deepseek-harness) ⭐6 — Curated DeepSeek Harness resources. (✅ active)
- [awesome-dsh-plugin (billLiao)](https://github.com/billLiao/awesome-dsh-plugin) ⭐5 — Curated list of plugins for DeepSeek Harness. (✅ active)
- [awesome-dsh-plugins (kejixiaoliang)](https://github.com/kejixiaoliang/awesome-dsh-plugins) ⭐5 — Curated DSH plugin catalog: 14 categories, 280+ community plugins covering MCP/Skill/TUI/multi-agent/context memory/UI skins. (✅ active)
- [dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) ⭐4 — Verified plugin marketplace and autonomous registry for DeepSeek Harness (✅ active)
- [dsh-plugins](https://github.com/HackSing/dsh-plugins) ⭐4 — A bilingual, continuously maintained directory of plugins for DeepSeek Harness (DSH). (✅ active)
- [zat-dsh-engine](https://github.com/mishibeikejie/zat-dsh-engine) ⭐4 — Visual plugin marketplace for DeepSeek Harness — browse, search and install community plugins (✅ active)
- [dsh-market](https://github.com/2BingLing/dsh-market) ⭐3 — DeepSeek Harness 插件市场 · 持续收录 500+ DSH 插件：中文搜索 + 实用五维评分 + 一键安装。Web 版与 DSH 侧边栏插件双形态。Plugin marketplace for DeepSeek Harness: 500+ plugins, Chinese search, 5-dim scoring, one-click install. (✅ active)
- [dsh-plugins](https://github.com/lwmxiaobei/dsh-plugins) ⭐3 — DeepSeek Harness 社区插件目录，自动汇总并基础校验 GitHub 插件，支持搜索、筛选、双语详情与最新版本安装命令复制。Community directory for DeepSeek Harness plugins with automated discovery, basic validation, search, filters, bilingual details, and latest version install commands. (✅ active)
- [awesome-deepseek-agent (official)](https://github.com/deepseek-ai/awesome-deepseek-agent)  — Official curated guides for integrating DeepSeek models into agent/coding-assistant tools (AstrBot, Cherry Studio, Claude Code, Codex, DeepSeek-TUI, Reasonix and more). (✅ active)

### Related Agent Harnesses


#### 🔥 Top 8

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [DeerFlow](https://github.com/bytedance/deer-flow) | ⭐80,001 | Open-source long-horizon SuperAgent harness by ByteDance: skills, memory, sandboxes, subagents, tools and a message gateway. | ✅ active |
| 2 | [Cordis](https://github.com/cordiverse/cordis) | ⭐3,182 | Meta-Framework of Spatiotemporal Composability — the plugin runtime DeepSeek Harness is built on. | ✅ active |
| 3 | [sandbase-harness](https://github.com/sandbaseai/sandbase-harness) | ⭐573 | Open-source CMA-compatible agent runtime for any model: MCP tools, sandboxed sessions, audit, replay. | ✅ active |
| 4 | [mnemon](https://github.com/mnemon-dev/mnemon) | ⭐430 | LLM-supervised persistent memory for AI agents: graph-based recall and cross-session knowledge in a single binary. | ✅ active |
| 5 | [claude-paper](https://github.com/alaliqing/claude-paper) | ⭐294 | Cross-agent research paper toolkit for Claude Code, Codex, OpenCode and DeepSeek Harness: quick summaries and deep dives. | ✅ active |
| 6 | [Axern](https://github.com/cofy-x/axern) | ⭐272 | Open-source sandboxes for AI agents: untrusted code execution and durable services. | ✅ active |
| 7 | [open-managed-agents](https://github.com/openma-ai/open-managed-agents) | ⭐235 | Open-source Claude Managed Agents API implementation and self-hosted Claude Tag-style agent runtime. | ✅ active |
| 8 | [deepseek-auto-evolving-harness](https://github.com/liuchen6667/deepseek-auto-evolving-harness) | ⭐28 | Auto-evolving LLM agent harness: benchmark-driven evolution via Claude Code and a self_evolution.md guide. | ✅ active |

#### Complete list (8)

- [DeerFlow](https://github.com/bytedance/deer-flow) ⭐80,001 — Open-source long-horizon SuperAgent harness by ByteDance: skills, memory, sandboxes, subagents, tools and a message gateway. (✅ active)
- [Cordis](https://github.com/cordiverse/cordis) ⭐3,182 — Meta-Framework of Spatiotemporal Composability — the plugin runtime DeepSeek Harness is built on. (✅ active)
- [sandbase-harness](https://github.com/sandbaseai/sandbase-harness) ⭐573 — Open-source CMA-compatible agent runtime for any model: MCP tools, sandboxed sessions, audit, replay. (✅ active)
- [mnemon](https://github.com/mnemon-dev/mnemon) ⭐430 — LLM-supervised persistent memory for AI agents: graph-based recall and cross-session knowledge in a single binary. (✅ active)
- [claude-paper](https://github.com/alaliqing/claude-paper) ⭐294 — Cross-agent research paper toolkit for Claude Code, Codex, OpenCode and DeepSeek Harness: quick summaries and deep dives. (✅ active)
- [Axern](https://github.com/cofy-x/axern) ⭐272 — Open-source sandboxes for AI agents: untrusted code execution and durable services. (✅ active)
- [open-managed-agents](https://github.com/openma-ai/open-managed-agents) ⭐235 — Open-source Claude Managed Agents API implementation and self-hosted Claude Tag-style agent runtime. (✅ active)
- [deepseek-auto-evolving-harness](https://github.com/liuchen6667/deepseek-auto-evolving-harness) ⭐28 — Auto-evolving LLM agent harness: benchmark-driven evolution via Claude Code and a self_evolution.md guide. (✅ active)
<!-- AUTO:resources:END -->` are produced by `scripts/generate-readme.py`. Edit the JSON, never the tables.

---

# Quality Levels

Every entry carries one of the following statuses:

| Status | Meaning |
|---|---|
| ✅ **Active** | Recently pushed; linked repo exists and contains code |
| 🧪 **Experimental** | Very new, unstable API, incomplete docs or limited validation |
| 🚧 **WIP** | Work in progress |
| 💤 **Inactive** | No longer maintained |

All entries are checked against the live GitHub API. The `dsh-external` org was emptied/redirected in mid-2026 — most other registries still point at dozens of dead links; we do not list dead repositories here.

---

# Submit a Project

PRs are welcome. A submitted project should include:

```yaml
name:
repository:
type: plugin | skill | workflow | agent | client | tool | integration | example | tutorial
category:
description:
capabilities:
status:
license:
```

Projects should:
* directly support the official `deepseek-ai/deepseek-harness`, or provide clearly useful surrounding tooling
* contain meaningful source code or documentation
* avoid deceptive naming, and clearly disclose experimental status

The simplest path: open an issue via the [submit template](.github/ISSUE_TEMPLATE/submit-project.yml) or add the `dsh-plugin` topic to your repo and open a PR against `data/`.

---

# Not the Same Project

⚠️ There are older/unrelated projects using the name **DeepSeek Harness** (e.g. standalone DeepSeek API wrappers). This directory specifically tracks the ecosystem around `deepseek-ai/deepseek-harness`. Verify the target before submitting.

---

# Roadmap

## Phase 1 — Awesome Directory ✅
- [x] Plugins · Skills · Workflows · Agents · Clients · Examples · Tutorials
- [x] Machine-readable registry + schema
- [x] Automated validation & link checking
- [ ] Verified badge rollout across all entries

## Phase 2 — Automation
- [ ] Weekly `update-metadata.py` run (stars/status refresh)
- [ ] Weekly `discover-github.py` run → candidate review issue
- [ ] CI-generated MkDocs deployment

## Phase 3 — HarnessHub
- [ ] Search & categories on the website
- [ ] Resource pages with install instructions
- [ ] Trending/related projects
- [ ] One-click install commands

## Phase 4 — CLI

```bash
dshx search browser
dshx search memory
dshx info dsh-at-file
dshx add <plugin>
```

## Phase 5 — Desktop
A GUI for discovering, installing, configuring, running and updating the ecosystem.

---

# Contributing

DeepSeek Harness is moving extremely fast. If you find a new plugin, a new workflow, a new client, an outdated entry, a broken link or incorrect compatibility information — open an issue or PR.

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

# Disclaimer

This is an independent community project and is **not affiliated with or endorsed by DeepSeek AI**. DeepSeek and DeepSeek Harness are trademarks or projects of their respective owners. Projects listed here are maintained by independent authors unless explicitly marked otherwise.

---

## Star History

If this directory helps you discover useful DeepSeek Harness projects, consider starring it ⭐.

**Built for the DeepSeek Harness community. 🐋**
