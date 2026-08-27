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
| 1 | [voyager](https://github.com/Nagi-ovo/voyager) | ⭐19,755 | Enhancement suite for Gemini, AI Studio, Claude & ChatGPT — plus a prompt manager for any web UI, DeepSeek Harness included. / 面向 Gemini、AI Studio、Claude 与 ChatGPT 的增强套件；提示词管理器可用于任意 Web UI，含 DeepSeek Harness。 | ✅ active |
| 2 | [dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | ⭐5,349 | Large plugin and skin collection for DSH Web: task board, git graph, side panels, remote/mobile UI, pets, token stats and themes. | ✅ active |
| 3 | [petdex](https://github.com/crafter-station/petdex) | ⭐3,945 | A public gallery of animated pets for Codex, Claude Code, DeepSeek Harness, Hermes, OpenCode, Gemini CLI, and more. | ✅ active |
| 4 | [dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) | ⭐3,697 | Two-phase DeepSeek Harness preset: Minimal-aligned bootstrap, then full Standard tools (Project2 98/99) | ✅ active |
| 5 | [modlens](https://github.com/liustack/modlens) | ⭐3,495 | The first vision plugin for DeepSeek Harness and the vision bridge for every text-only coding agent: paste an image and it works. | ✅ active |
| 6 | [DSH Better Sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) | ⭐2,552 | Workbench-style sidebar: file viewer/editor, terminal, Git, subagents and plugin-extensible tabs. | ✅ active |
| 7 | [dsh-market](https://github.com/dsh-market/dsh-market) | ⭐1,582 | Visual plugin market inside DeepSeek Harness: browse, search and one-click install. | ✅ active |
| 8 | [dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) | ⭐1,548 | Whale-girl skin series for DSH Web (CC BY-NC-SA 4.0). | ✅ active |
| 9 | [TokenTracker](https://github.com/xiufengsun/TokenTracker) | ⭐1,395 | Local-first AI token usage & cost tracker for 31 coding tools including Claude Code, Codex, Cursor, Gemini & DeepSeek Harness. | ✅ active |
| 10 | [dsh-vision-router](https://github.com/ysr666/dsh-vision-router) | ⭐927 | Eyes for text-only agents: built-in free keyless vision chain plus pixel-level tools (Q&A, grounding, crop, OCR, SVG trace). | ✅ active |

#### Complete list (263)

- [voyager](https://github.com/Nagi-ovo/voyager) ⭐19,755 — Enhancement suite for Gemini, AI Studio, Claude & ChatGPT — plus a prompt manager for any web UI, DeepSeek Harness included. / 面向 Gemini、AI Studio、Claude 与 ChatGPT 的增强套件；提示词管理器可用于任意 Web UI，含 DeepSeek Harness。 (✅ active)
- [dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) ⭐5,349 — Large plugin and skin collection for DSH Web: task board, git graph, side panels, remote/mobile UI, pets, token stats and themes. (✅ active)
- [petdex](https://github.com/crafter-station/petdex) ⭐3,945 — A public gallery of animated pets for Codex, Claude Code, DeepSeek Harness, Hermes, OpenCode, Gemini CLI, and more. (✅ active)
- [dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) ⭐3,697 — Two-phase DeepSeek Harness preset: Minimal-aligned bootstrap, then full Standard tools (Project2 98/99) (✅ active)
- [modlens](https://github.com/liustack/modlens) ⭐3,495 — The first vision plugin for DeepSeek Harness and the vision bridge for every text-only coding agent: paste an image and it works. (✅ active)
- [DSH Better Sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) ⭐2,552 — Workbench-style sidebar: file viewer/editor, terminal, Git, subagents and plugin-extensible tabs. (✅ active)
- [dsh-market](https://github.com/dsh-market/dsh-market) ⭐1,582 — Visual plugin market inside DeepSeek Harness: browse, search and one-click install. (✅ active)
- [dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) ⭐1,548 — Whale-girl skin series for DSH Web (CC BY-NC-SA 4.0). (✅ active)
- [TokenTracker](https://github.com/xiufengsun/TokenTracker) ⭐1,395 — Local-first AI token usage & cost tracker for 31 coding tools including Claude Code, Codex, Cursor, Gemini & DeepSeek Harness. (✅ active)
- [dsh-vision-router](https://github.com/ysr666/dsh-vision-router) ⭐927 — Eyes for text-only agents: built-in free keyless vision chain plus pixel-level tools (Q&A, grounding, crop, OCR, SVG trace). (✅ active)
- [dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) ⭐802 — Vision toolkit for text-only models: intent-aware image Q&A, long-screenshot OCR, UI restoration, grounding and pixel diff. (✅ active)
- [dsh-context](https://github.com/bowenliang123/dsh-context) ⭐666 — A DeepSeek Harness plugin for  Context insight dashboard — showing what the model's context window is made of and how it evolves. (✅ active)
- [museai](https://github.com/yejiming/MuseAI) ⭐595 — 创建你的 AI 角色，进入你的故事世界。和角色聊天、冒险、穿书，让每一次互动都留下羁绊（支持 DeepSeek Harness 插件，欢迎使用） (✅ active)
- [graph-memory](https://github.com/adoresever/graph-memory) ⭐564 — Deepseek Harness、Openclaw知识图谱记忆插件。2026年4月受邀发布在清华大学讨论会。Knowledge Graph + Memory；Knowledge Graph Context Engine for OpenClaw — extracts structured triples from conversations, compresses context 75%, enables cross-session experience reuse (✅ active)
- [dsh-ads](https://github.com/Nagi-ovo/dsh-ads) ⭐525 — Joke plugin: 2005 Chinese-web-style ad layer with sidebar banners, in-chat feed ads and corner popups. (✅ active)
- [v4-flash-godmode-opencode-go](https://github.com/SheberDavid/v4-flash-godmode-opencode-go) ⭐494 — V4 Flash 神模式 (opencode-go)：让 opencode-go 的 DeepSeek V4 Flash 从鬼模式切换到神模式的 dsh agent preset (✅ active)
- [dsh-at-file](https://github.com/omdsh-dev/dsh-at-file) ⭐445 — Codex-style @file mentions inside the DSH composer: search workspace files and attach their contents to prompts. (✅ active)
- [dsh-browser](https://github.com/Lum1104/dsh-browser) ⭐366 — Chrome sidebar extension that lets DSH operate your browser directly, no vision capabilities required. (✅ active)
- [dsh-transparent-ui-plugin](https://github.com/WYH66666666/DSH-Transparent-UI-Plugin) ⭐355 — 是一层高自由度的玻璃质感主题，套在 DeepSeek Harness 网页端。顶栏、侧边栏、输入框、统计行、轨迹视图都成了磨砂玻璃片。玻璃模糊度、磨砂度、背景（流体或自定义壁纸，壁纸还能单独调模糊和磨砂）全都能在设置卡片里自由调节。关掉开关就回到原生界面，不改 DSH 任何一行源码。 (✅ active)
- [flowix](https://github.com/text2future/flowix) ⭐338 — Notes for you, Memory for your agents. / 内置 Deepseek harness Agent / 适用 办公 & 写作 & Coding (✅ active)
- [dsh-genui](https://github.com/omdsh-dev/dsh-genui) ⭐282 — Generative UI inside conversations: layouts, charts, forms, quizzes, Mermaid and interactive events rendered inline. (✅ active)
- [dsh-pet](https://github.com/PC2005-cloud/dsh-pet) ⭐274 — DeepSeek Harness 桌面宠物插件 + 完整素材生成链：AI 提示词 → 绿幕视频 → 透明动画 → 可安装插件，从零到宠物全流程可复现 (✅ active)
- [whale-girl](https://github.com/vlln/whale-girl) ⭐260 — Desktop pet plugin (QQ-pet style) floating at the bottom-right of the DSH Web GUI: draggable, feedable and playable. (✅ active)
- [dsh-plugin-subscriptions](https://github.com/V1ki/dsh-plugin-subscriptions) ⭐216 — Use ChatGPT (Codex), Claude, and Grok (X Premium) subscriptions as DeepSeek Harness LLM providers — OAuth login in the web UI, no API keys (✅ active)
- [dsh-memory-evolve](https://github.com/csyangwen/dsh-memory-evolve) ⭐211 — Cross-session long-term memory + background self-evolution: five-track memory, git-branch awareness, in-turn self-review and skill evolution. (✅ active)
- [modsearch](https://github.com/liustack/modsearch) ⭐207 — Web plugin for DSH and the search bridge for every model without native web access. (✅ active)
- [dsh-visualize](https://github.com/Nagi-ovo/dsh-visualize) ⭐196 — Interactive HTML UI rendered directly in conversation with streaming preview and sandbox rendering. (✅ active)
- [Open Sea Skin](https://github.com/d-dev0101/open-sea-skin) ⭐185 — Realtime WebGPU ocean skin with controls for waves, daylight, glass opacity and automatic day cycling. (✅ active)
- [anysearch-dsh](https://github.com/anysearch-team/anysearch-dsh) ⭐174 — AnySearch web search provider and advanced search tools for DeepSeek Harness. (✅ active)
- [dsh-find-plugins](https://github.com/Nagi-ovo/dsh-find-plugins) ⭐162 — Plugin discovery utility for the DSH ecosystem. (✅ active)
- [anime-find](https://github.com/cocofhu/anime-find) ⭐157 — DeepSeek Harness 搜番插件：对话内多源搜索番剧，卡片展示 Bangumi 评分与详情，支持复制磁力。 (✅ active)
- [dsh-mnemon](https://github.com/omdsh-dev/dsh-mnemon) ⭐156 — Three-tier local memory: runtime hot memory, project documents and long-term memory spaces, with supervised writeback. (✅ active)
- [dsh-cost-meter](https://github.com/Han-1413141/dsh-cost-meter) ⭐139 — DeepSeek Harness 会话费用统计插件:本会话费用、当日费用、历史记录与官方价格同步 (✅ active)
- [dsh-gitbash-preset](https://github.com/liceses/dsh-gitbash-preset) ⭐136 — DeepSeek Harness 插件：一键安装「极简模式 (Git Bash)」agent preset —— 把 DSH 自带极简模式中的 bash 调用映射到 Git for Windows 的 bash（MSYS），让 Windows 上的极简模式真正可用。 (✅ active)
- [DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) ⭐132 — Browse, install and update every GitHub topic:dsh-plugin plugin from the DSH Web GUI. (✅ active)
- [tokenledger](https://github.com/zh667/TokenLedger) ⭐126 — Token usage accounting for DeepSeek Harness, reconciled against New API and Sub2API relay-site billing (✅ active)
- [dsh-auto-mode](https://github.com/NanmiCoder/dsh-auto-mode) ⭐115 — Safe automatic permissions for DeepSeek Harness. (✅ active)
- [dsh-undo-plugin](https://github.com/lire1131/dsh-undo-plugin) ⭐108 — DSH plugin: snapshot & rollback your plugin/skin/settings configs. Auto-save on change, undo/redo stack, snapshot manager panel, keyboard shortcuts, plus an offline PowerShell CLI & GUI that work even when DSH won't boot. (✅ active)
- [dsh-usage-stats](https://github.com/Ychris12138/dsh-usage-stats) ⭐98 — Token usage heatmap, per-model breakdowns, and DeepSeek account balance for the DeepSeek Harness Web GUI (dsh web). (✅ active)
- [dsh-reasoning-effort](https://github.com/HanaAyane/dsh-reasoning-effort) ⭐97 — DSH适用的Codex风格的思考强度滑块，以及大肥鱼跑步滑块。Codex-style model and reasoning-effort slider for DeepSeek Harness (✅ active)
- [dsh-webui-market-plugin](https://github.com/Sanqi-normal/dsh-webui-market-plugin) ⭐96 — Community plugin market in the Web GUI: browse the awesome-dsh-plugin.com catalog and install/uninstall to a profile. (✅ active)
- [dsh-turn-rewind](https://github.com/Anionex/dsh-turn-rewind) ⭐94 — Rewind conversation and workspace state, powered by a persistent change ledger. (✅ active)
- [dsh-plugin](https://github.com/Tabbit-Browser/dsh-plugin) ⭐91 — Tabbit Broser plugins for Deepseek Harness (✅ active)
- [dsh-annotation](https://github.com/omdsh-dev/dsh-annotation) ⭐87 — Select text in DSH Web, annotate it and send the annotation with your message; replies cross-reference each annotation. (✅ active)
- [dsh-chat-import](https://github.com/Nwflower/dsh-chat-import) ⭐87 — Import conversation history from Claude Code, Codex, ChatGPT, Cursor, Gemini, Reasonix and OpenCode into resumable DSH sessions. (✅ active)
- [dsh-commandcode-provider](https://github.com/Mars-Sea/dsh-commandcode-provider) ⭐83 — Unofficial DeepSeek Harness LLM provider plugin for Command Code: live model catalog, reasoning-effort support, Models-page card. Ported from pi-commandcode-provider (MIT). (✅ active)
- [dsh-kun-like-pet](https://github.com/liyupi/dsh-kun-like-pet) ⭐80 — Kun Like 桌宠 —— DeepSeek Harness 桌面宠物插件：右下角小坤宠随 Agent 工作状态切换 9 种动作，任务完成播放「你干嘛~哎哟」 (✅ active)
- [dockyard-dsh](https://github.com/AITabby/dockyard-dsh) ⭐73 — A macOS-only native account-pool and provider plugin for DeepSeek Harness. (✅ active)
- [dsh-dream-skin](https://github.com/RevolutionLA/dsh-dream-skin) ⭐73 — One-command skinning for DSH Web: 8 original themes, wallpaper (opacity/blur/gradient/URL), per-user accent, shareable theme packs, favorites and surprise-me — purely native on DSH's token system. (✅ active)
- [dsh-find-plugin](https://github.com/awesome-dsh-plugin/dsh-find-plugin) ⭐73 — Agent-assisted plugin discovery: search the live GitHub dsh-plugin topic from inside DSH. (✅ active)
- [dsh-notification](https://github.com/omdsh-dev/dsh-notification) ⭐70 — Desktop notifications for turn completions with per-outcome controls and include/exclude keyword filters. (✅ active)
- [dsh-plugin-hub](https://github.com/Noob-stupid/dsh-plugin-hub) ⭐64 — Plugin management panel: enable/disable installed plugins plus a GitHub dsh-plugin marketplace with one-click install. (✅ active)
- [dsh-plugins-store](https://github.com/ZASENJC/dsh-plugins-store) ⭐62 — Static directory site that automatically collects and categorizes GitHub dsh-plugin topic projects. (✅ active)
- [dsh-web-plugin-manager](https://github.com/LX2000WASD/dsh-web-plugin-manager) ⭐62 — Manage plugins from the Web UI: view, live enable/disable, install/uninstall, env management and plugin market. (✅ active)
- [deepseek-harness-control-center](https://github.com/feibi-mochi/deepseek-harness-control-center) ⭐61 — DeepSeek Harness account monitoring, usage accounting, completion alerts, official recharge, flexible layout, and agent-assisted session controls. / 账户监控、提醒、充值与会话控制中心 (✅ active)
- [dsh-claude-ux](https://github.com/eri64/dsh-claude-ux) ⭐60 — DSH plugin: Claude-style Chinese risk control & conversation autonomy for DeepSeek Harness web (✅ active)
- [dsh-memento](https://github.com/PerryLink/dsh-memento) ⭐59 — Bounded, layered, approval-gated and auditable cross-session memory with frozen snapshot injection. (✅ active)
- [dsh-open-in-vscode](https://github.com/omdsh-dev/dsh-open-in-vscode) ⭐53 — Open DSH workspace directories/files directly in VS Code from the web GUI. (✅ active)
- [dsh-navbar](https://github.com/vlln/dsh-navbar) ⭐52 — DSH 插件：对话节点导航条（右缘节点串快速跳转 user 消息）。官方 bundle 插件，dsh plugin --profile web add 安装 (✅ active)
- [deepseek-harness-skin](https://github.com/HeiGeAi/deepseek-harness-skin) ⭐49 — Skin system with 21 built-in themes plus one-image custom skin generation, contrast-validated at build time. (✅ active)
- [dsh-plugins](https://github.com/Ephemeral-AI-Lab/dsh-plugins) ⭐45 — Make Deepseek Harness Great (✅ active)
- [dsh-smooth-stream](https://github.com/Laplace-bit/dsh-smooth-stream) ⭐45 — Silky streaming reveal for the Web UI: text appears at the model's arrival rate, new lines glide in, no flicker; follow stays with the user and respects prefers-reduced-motion. (✅ active)
- [dsh-status-rotator](https://github.com/01Virex/dsh-status-rotator) ⭐42 — Replaces the 'Deep diving…' turn-status label with phase-aware typewriter messages. (✅ active)
- [dsh-trace-compare](https://github.com/lamost423/dsh-trace-compare) ⭐41 — Trace Compare & Live Maze for DeepSeek Harness: visualize agent exploration (main path, detours, backtracks) from session logs or live sessions (✅ active)
- [xgone/dsh-remote](https://github.com/xgone/dsh-remote) ⭐41 — Remote access & authentication for DeepSeek Harness web UI: account/password login gate, MFA (TOTP), signed session cookies, role-based access, in-browser directory picker, and a Settings page for account management. (🧪 experimental)
- [dsh-prompt-enhancer](https://github.com/Fishsb/dsh-prompt-enhancer) ⭐39 — DeepSeek Harness DSH 提示词增强插件：✨ 一键优化草稿，增强提示词。 (✅ active)
- [ui-status-label](https://github.com/alingalingling/ui-status-label) ⭐39 — Customize the whale's 'Deep diving' status label into anything you want. (✅ active)
- [dsh-free-search](https://github.com/DDDMUC/dsh-free-search) ⭐38 — Free web search provider for DeepSeek Harness - DuckDuckGo backend, no API key needed (✅ active)
- [dsh-plugin-mineru](https://github.com/HuanLinOTO/dsh-plugin-mineru) ⭐38 — Expose MinerU document parsing to the model: PDF/images/DOCX/PPTX/XLSX to structured Markdown/JSON. (✅ active)
- [dsh-expression](https://github.com/yyh-001/dsh-expression) ⭐36 — DeepSeek Harness 的表情包插件——找得到、发得出、学得会 (✅ active)
- [dsh-vision (william-jin-cmu)](https://github.com/william-jin-cmu/dsh-vision) ⭐36 — Vision bridge: view_image tool over any OpenAI-compatible VLM, defaulting to Zhipu's free tier. (✅ active)
- [dsh-message-edit](https://github.com/Moeblack/dsh-message-edit) ⭐35 — Branch-based message editing, reroll, retry and version timeline. (✅ active)
- [dsh-codex-connect](https://github.com/franksong2702/dsh-codex-connect) ⭐34 — ChatGPT OAuth and Codex models for DeepSeek Harness. (✅ active)
- [dsh-emoji](https://github.com/hellodigua/dsh-emoji) ⭐34 — Let AI replies add custom emoji reactions. (✅ active)
- [dsh-omi-voice](https://github.com/PolinniZhong/dsh-omi-voice) ⭐34 — Immersive voice reading plugin: in-chat read/pause/resume with Doubao TTS natural voices (BYOK), reads only the final answer, filters code/tables/graphics. (✅ active)
- [billion-context-dsh](https://github.com/Tyan66666/billion-context-dsh) ⭐33 — Model-driven context compression (Active Context Pruning): the model decides when and what to compress. (✅ active)
- [dsh-mneme](https://github.com/modusensus/dsh-mneme) ⭐31 — Local cross-session memory with memory sovereignty: SQLite + human-editable Markdown mirror and background autoDream consolidation. (✅ active)
- [dsh-remote](https://github.com/flymysql/dsh-remote) ⭐31 — Remote workspace: connect a host over SSH and operate a remote directory with rw_* tools. (✅ active)
- [dsh-share](https://github.com/hellodigua/dsh-share) ⭐29 — One-click conversation sharing for DSH. (✅ active)
- [dsh-ui-whale](https://github.com/lhh010/dsh-ui-whale) ⭐29 — Hand-drawn pixel whale companion in the session title bar: blinks, wags its tail, spouts water when a turn completes. (✅ active)
- [dsh-web-search-pro](https://github.com/anweat/dsh-web-search-pro) ⭐29 — Multi-engine persistent search: DeepSeek/Exa/DDG/Bing/Jina + GitHub/Bilibili/YouTube/V2EX/XHS/Twitter/Reddit/RSS, with SQLite+LRU cache and Playwright rendering. (✅ active)
- [ego-browser](https://github.com/Fisfzy/ego-browser) ⭐29 — Bring the ego-lite agent browser (Chromium for AI agents) into DSH with 13 structured tools. (✅ active)
- [deepseek-harness-snowsalt](https://github.com/KYZHXL/deepseek-harness-snowsalt) ⭐28 — Snow-salt themed skin for DeepSeek Harness. (✅ active)
- [dsh-plugin-guard](https://github.com/lxzy-7/dsh-plugin-guard) ⭐28 — Install safety net for DeepSeek Harness: pre-install snapshots, one-click/automatic rollback, guarded boot, and incident reports that auto-trigger agent analysis. 中文: DeepSeek Harness 插件安装安全网（安装前自动快照、一键/自动回退、守护启动、事故报告自动触发 Agent 分析）。 (✅ active)
- [dsh-plugin-check](https://github.com/omdsh-dev/dsh-plugin-check) ⭐27 — Plugin health checks: manifest protocol, patch format, build pitfalls and hub listing status, zero-dependency read-only. (✅ active)
- [dsh-computer-use](https://github.com/Anionex/dsh-computer-use) ⭐26 — 为 DeepSeek Harness 提供电脑控制插件：新鲜 Accessibility 观测、过期状态拒绝、作用域权限与安全输入（目前支持macos）｜Accessibility-first macOS Computer Use bundle for DSH with fresh observations, stale-state rejection, scoped permissions, and safe input. (✅ active)
- [dsh-auto-memory](https://github.com/Aik358/dsh-auto-memory) ⭐25 — DSH 自动记忆插件:三层记忆(用户级/项目笔记/每日日志)自动注入与检索、每日反思、可视化面板与设置页,支持继承其他 AI 工具的历史记忆。An auto-memory plugin for the DeepSeek Harness Web GUI: three-layer memory (user-level / project notes / daily logs) with automatic injection and retrieval, daily reflections, a visual panel and settings page, and inheritance of memories from other AI tools. (✅ active)
- [dsh-minigames](https://github.com/lhh010/dsh-minigames) ⭐25 — DSH Web UI 右侧小游戏面板：18 款离线小游戏（恐龙跳一跳 / 俄罗斯方块 / 坦克大战 / 扫雷 / 2048 / 数独 / 吃豆人 / 跟枪练习等），可扩展游戏注册表，等待模型回复或修 bug 时的摸鱼神器 (✅ active)
- [dsh-plugin-workshop](https://github.com/yyyyukari/dsh-plugin-workshop) ⭐25 — Steam Workshop-style plugin browser for the DSH Web UI: zero-server, GitHub-powered search and one-click install. (✅ active)
- [dsh-custom-tool](https://github.com/omdsh-dev/dsh-custom-tool) ⭐24 — Create and manage sandboxed JavaScript tools for DSH with a Monaco editor and model-driven tool lists. (✅ active)
- [dsh-diff-viewer](https://github.com/lehhair/dsh-diff-viewer) ⭐24 — PiUI-style Web diff viewer replacing the default diff view. (✅ active)
- [dsh-recall-plugin](https://github.com/limbo947/dsh-recall-plugin) ⭐24 — DSH 消息撤回插件：回到发送该消息时的状态 DSH Message Recall Plugin: Return to the state when the message was sent (✅ active)
- [dsh-toolkit](https://github.com/omdsh-dev/dsh-toolkit) ⭐24 — Zero-dependency tool suite: calculator, CSV, diff, encoding, JSON, Markdown, regex and time utilities. (✅ active)
- [dsh-balance](https://github.com/crazywoola/dsh-balance) ⭐23 — DeepSeek Harness balance plugin for the Settings page. (✅ active)
- [dsh-plugin-better-sidebar-plugin-office](https://github.com/HuanLinOTO/dsh-plugin-better-sidebar-plugin-office) ⭐23 — Office-suite preview (.docx/.xlsx/.pptx) for the Better Sidebar, as a standalone slim bundle. (✅ active)
- [dsh-focus-chat](https://github.com/dingyi222666/dsh-focus-chat) ⭐21 — 为 dsh 提供新的「聚焦会话」精简会话视图，更轻松易于阅读，只关注最终产出结果。 (✅ active)
- [dsh-plugin-pet-rs](https://github.com/HuanLinOTO/dsh-plugin-pet-rs) ⭐21 — Rust desktop pet: 5-state whale with dual SSE real-time push, transparent always-on-top window and system tray. (✅ active)
- [dsh-stickers](https://github.com/william-jin-cmu/dsh-stickers) ⭐21 — DSH WebUI sticker plugin for bidirectional user and agent reactions (✅ active)
- [dsh-web-ui-notify](https://github.com/bill9109/dsh-web-ui-notify) ⭐21 — Adds desktop notification reminders to DSH. (✅ active)
- [dsh-drag-and-drop](https://github.com/bill9109/dsh-drag-and-drop) ⭐20 — Cross-platform drag & drop for DSH Web UI with original-path insertion, no file copying. (✅ active)
- [dsh-agy](https://github.com/chaos-03x/dsh-agy) ⭐19 — Google Antigravity (agy) OAuth auth + model access plugin for DeepSeek Harness: multi-account pool, 429 rotation, device fingerprinting, CLI and web login. (✅ active)
- [dsh-balance-meter](https://github.com/Ghost011118/dsh-balance-meter) ⭐19 — DeepSeek account balance and session cost readout for the DeepSeek Harness Web GUI (✅ active)
- [dsh-skin](https://github.com/KinGao294/dsh-skin) ⭐19 — Codex-style skin switcher plus custom translucent wallpaper with opacity/blur controls. (✅ active)
- [dsh-theme-plugin](https://github.com/nevertoday/dsh-theme-plugin) ⭐19 — Chinese traditional colors as a DeepSeek Harness theme pack. (✅ active)
- [compass](https://github.com/dshakes/compass) ⭐18 — 🧭 Let your coding agent off the leash — not off the rails. Guardrails, a hard budget cap & a self-fixing PR loop for Claude Code / Codex / Gemini. Eval-gated 100/100, you always merge. (✅ active)
- [dsh-milestone](https://github.com/SnowCrescenter-tech/dsh-milestone) ⭐18 — Git-style milestone timeline rail: hover for metadata, click to jump to any message. (✅ active)
- [dsh-recommend](https://github.com/zp-home/dsh-recommend) ⭐18 — Transparent plugin rankings and recommendations: daily auto-fetched dsh-plugin topic data with an open scoring model. (✅ active)
- [touhou-hakurei](https://github.com/xiake595/touhou-hakurei) ⭐18 — 灵梦（Reimu）·博丽神社（东方Project）美化版皮肤：神社昼夜实景背景、灵梦立绘、画框侧边栏与输入框、纸白透明界面 — DeepSeek Harness Web GUI skin (✅ active)
- [webdsh](https://github.com/futrime/webdsh) ⭐18 — Running DeepSeek Harness on web (✅ active)
- [DeepSeek-Harness-Web-Tools](https://github.com/tonyd2wild/DeepSeek-Harness-Web-Tools) ⭐17 — Free, keyless web_search and web_fetch for DSH, DuckDuckGo-backed with no signup. (✅ active)
- [dsh-context-doctor](https://github.com/Zhenyu98/dsh-context-doctor) ⭐17 — Audits what actually enters every model request: token cost of AGENTS.md chains, skill catalogs and tool schemas, with duplicate/conflict detection. (✅ active)
- [dsh-group-photo](https://github.com/SenmuuuuW/dsh-group-photo) ⭐17 — DSH 内测收官合影墙：GitHub OAuth 零权限登录 + 冻结白名单校验的拍立得合影站（含 DSH Skill 包装） (✅ active)
- [dsh-passwords](https://github.com/slywalker2006/dsh-passwords) ⭐17 — dsh-passwords: DeepSeek Harness login gateway - first-run setup, at-rest encryption, brute-force lockout, audit log, HTTPS (✅ active)
- [dsh-plugin-writing-guard](https://github.com/xmutfyh/dsh-plugin-writing-guard) ⭐17 — DeepSeek Harness (DSH) academic writing guard for papers — 论文去AI味 / AI-writing style detection, evidence preservation, journal-fit calibration, manuscript proofreading, writing_audit & automatic checks. Local, zero network, zero LLM. (✅ active)
- [dsh-side-panel](https://github.com/ccq1/dsh-side-panel) ⭐16 — Compact side panel with a file browser, terminal and Git review. (💤 inactive)
- [dsh-stock-market](https://github.com/AnacondaKC/dsh-stock-market) ⭐15 — Stock market data plugin (joke: fixes the bug where your account loses money while you code). (✅ active)
- [dsh-web-review](https://github.com/CanglongCl/dsh-web-review) ⭐15 — DeepSeek Harness Web GUI 的网页预览与元素批注插件，让 AI 根据可视化反馈直接修改前端源码。 (✅ active)
- [deepseek-harness-zh_pro](https://github.com/magian1127/deepseek-harness-zh_pro) ⭐14 — Chinese enhancement plugin for DeepSeek Harness (DSH) - DSH 中文增强插件 (✅ active)
- [dsh-gomoku](https://github.com/omdsh-dev/dsh-gomoku) ⭐14 — Play Gomoku with AI inside DSH, or let two AIs battle to compare models. (✅ active)
- [dsh-plugin](https://github.com/loongsuite/dsh-plugin) ⭐14 — OpenTelemetry tracing for DeepSeek Harness (dsh): turns each agent turn into a GenAI span tree — steps, LLM calls with TTFT, tool executions, token usage — exported over standard OTLP to Jaeger, Grafana Tempo, SigNoz, Langfuse, or any compatible backend. (✅ active)
- [dsh-deepcel](https://github.com/Small-tailqwq/dsh-deepcel) ⭐13 — Spreadsheet-style skin for DSH, mimicking Excel. (✅ active)
- [dsh-nested-followups](https://github.com/sluminositys/dsh-nested-followups) ⭐13 — Ask a follow-up on any past answer in an isolated branch, keeping your main conversation clean. 针对任意历史回答发起追问，新问题在独立分支中展开，主对话保持干净。A conversation-tree plugin for DeepSeek Harness / DeepSeek Harness 会话树插件。 (✅ active)
- [dsh-opencode-go-usage](https://github.com/Xenia0922/dsh-opencode-go-usage) ⭐13 — DeepSeek Harness 插件:OpenCode Go 用量与花费悬浮仪表盘(配额、逐请求成本、模型/来源分布) (✅ active)
- [dsh-pet](https://github.com/FlytoMAYDAY80/dsh-pet) ⭐13 — 🐋 DSH 有声桌宠：悬浮桌面的 DeepSeek 小鲸鱼，不打开 DSH 也能实时感知会话状态（需要确认/工作中/完成/空闲/离线），支持音效提醒与零代码定制素材 (✅ active)
- [dsh-plugin-aigc-canvas](https://github.com/HuanLinOTO/dsh-plugin-aigc-canvas) ⭐13 — provider-agnostic AIGC HTTP 桥 + 无限画布 + ffmpeg 后处理，13 个工具含画布连边/reroll/媒体编辑 | Provider-agnostic AIGC HTTP bridge + infinite canvas + ffmpeg post-processing; 13 tools incl. canvas linking/reroll/media-edit (✅ active)
- [dsh-security-audit](https://github.com/omdsh-dev/dsh-security-audit) ⭐13 — DSH 本机安全审计插件：配置/插件来源/会话/网络暴露面，只读脱敏风险报告 (✅ active)
- [DeepSeek-Harness-Vision-Tools](https://github.com/tonyd2wild/DeepSeek-Harness-Vision-Tools) ⭐12 — Vision proxy for chat: give DSH eyes with any text model plus any vision model. (✅ active)
- [dsh-surfing-plugin](https://github.com/cyijun/dsh-surfing-plugin) ⭐12 — SearXNG search and Crawl4AI fetch providers for DeepSeek Harness (✅ active)
- [dsh-trading](https://github.com/maddogfinance/dsh-trading) ⭐12 — Research-only trading workbench for DSH: typed market-data seam (BYO provider), multi-timeframe indicator snapshots, interactive chart cards with provenance-gated annotations, and a risk-guard denying execution-shaped tool calls. No execution seam by construction. (✅ active)
- [weshop-dsh-plugin](https://github.com/weshopai/weshop-dsh-plugin) ⭐12 — Native WeShop Cordis plugin for DeepSeek Harness. Allow you to use infinite canvas with infinite creative skills. (✅ active)
- [dsh-file-mentions](https://github.com/a903067276-rgb/dsh-file-mentions) ⭐11 — Clickable file paths in DSH replies: inline open, reveal in file manager and a mentioned-files chip list. (✅ active)
- [dsh-file-mount](https://github.com/acefun29/dsh-file-mount) ⭐11 — Incremental file mounting with line-range deduplication: identical file contents are never re-sent to the model. (✅ active)
- [dsh-plugin-ya-workspace-sidebar](https://github.com/HuanLinOTO/dsh-plugin-ya-workspace-sidebar) ⭐11 — DSH Web 工作区侧栏替代，顶部全局最近会话 + Workspace→Session 二级菜单 + 面包屑 | DSH Web workspace sidebar replacement: top global recent sessions + Workspace→Session two-level menu + breadcrumbs (✅ active)
- [dsh-sdk-platform-rs](https://github.com/kpn-dsh/dsh-sdk-platform-rs) ⭐11 — A Rust SDK to interact with the DSH Platform. This library provides convenient building blocks for services that need to connect to DSH Kafka, fetch tokens for various protocols, manage Prometheus metrics, and more. (✅ active)
- [dsh-sticky-note](https://github.com/Meredith2328/dsh-sticky-note) ⭐11 — 左下角便签：随手记点子/感想/TODO，实时保存到归档目录，清单+悬浮归档 (✅ active)
- [oh-my-dsh](https://github.com/NoWint/Oh-My-DSH) ⭐11 — 🐋 Oh-My-DSH — DeepSeek Harness Plugin Ecosystem【每一小时更新】 (✅ active)
- [context-vista](https://github.com/GooodWei/context-vista) ⭐10 — Live context/token monitor: floating panel + /context command with donut charts of token usage, allocation and estimated cost. (✅ active)
- [dsh-plugin-anti-ads](https://github.com/HuanLinOTO/dsh-plugin-anti-ads) ⭐10 — DSH Web 广告拦截器，四层独立防御拦截 dsh-ads 插件的所有广告位 | DSH Web ad blocker with four independent defense layers targeting the dsh-ads plugin (✅ active)
- [dsh-ui-appearance](https://github.com/TQSY114514/dsh-ui-appearance) ⭐10 — Appearance customization plugin for DeepSeek Harness: theme color palette, background image, opacity/blur, glass effect (✅ active)
- [dsh-usage-chart](https://github.com/Max-Samson/dsh-usage-chart) ⭐10 — A DeepSeek Harness Web plugin for real-time Token usage, cost estimates, per-round charts, and DeepSeek API balance. (✅ active)
- [dsh-web-billing](https://github.com/bpc-oss/dsh-web-billing) ⭐10 — RMB/USD token billing for the DSH web: official-policy auto pricing with peak/off-peak hours and per-message cost ledger. (✅ active)
- [DeepSeek-Harness-billing-plugin](https://github.com/WilliamLIiii/DeepSeek-Harness-billing-plugin) ⭐9 — Account balance plus per-model remaining-task estimator with a session cost ledger. (✅ active)
- [dsh-awiki](https://github.com/AgentConnect/dsh-awiki) ⭐9 — AWiki identity and messaging plugin for DeepSeek Harness (✅ active)
- [dsh-hud](https://github.com/a903067276-rgb/dsh-hud) ⭐9 — HUD status panel: git status, MCP servers, skills, model and token usage in a floating side panel. (✅ active)
- [dsh-paste-input](https://github.com/lhh010/dsh-paste-input) ⭐9 — WebUI file input enhancement: Ctrl+V paste, drag & drop and file picker, copied into the session workspace. (✅ active)
- [dsh-plugin-auto-blame](https://github.com/HuanLinOTO/dsh-plugin-auto-blame) ⭐9 — 模型回合结束后用 LLM 生成 3 条批判性跟进建议，点击即发送 | After a model turn, an LLM generates 3 critical follow-up suggestions shown as click-to-send chips (✅ active)
- [dsh-plugin-interpreters](https://github.com/HuanLinOTO/dsh-plugin-interpreters) ⭐9 — Expose run_python/run_node tools that execute code via stdin and return stdout/stderr/exit code. (✅ active)
- [dsh-spotlight](https://github.com/0xsline/dsh-spotlight) ⭐9 — Keyboard-first command palette for DeepSeek Harness Web. (✅ active)
- [deepseek-harness-SupportVisionModel](https://github.com/TryDing-T/deepseek-harness-SupportVisionModel) ⭐8 — Secondary development of deepseek-harness supporting a separately configured vision model for reading images. (✅ active)
- [dsh-plugin-d399](https://github.com/HuanLinOTO/dsh-plugin-d399) ⭐8 — Mini-game menu (Wordle, match-3, 192 parameterized games) that pops up while the model generates. (✅ active)
- [dsh-session-health](https://github.com/omdsh-dev/dsh-session-health) ⭐8 — Frame-level diagnostics for multi-frame zstd session files: torn/corrupted/empty session detection, zero-dependency read-only. (✅ active)
- [dsh-usage-dashboard](https://github.com/Cassius0924/dsh-usage-dashboard) ⭐8 — DeepSeek 额度与用量仪表盘 — DSH (DeepSeek Harness) 动态 Cordis 插件 (✅ active)
- [dsh-browser](https://github.com/anweat/dsh-browser) ⭐7 — Self-contained browser runtime plugin for DeepSeek Harness — bundles Playwright (chromium) and OpenCLI as plugin-local dependencies, exposes a browser service and interactive browser tools. (✅ active)
- [dsh-builtin-toggles](https://github.com/Starfie1d1272/dsh-builtin-toggles) ⭐7 — Human-readable catalog of official DSH Web built-ins with safe GUI toggles. (✅ active)
- [dsh-director-toolkit](https://github.com/lhmd/dsh-director-toolkit) ⭐7 — DSH Director Toolkit is a DeepSeek Harness plugin for 3D artists, technical designers, and creative coders. Paste a half-formed idea, a reference note, or a portfolio caption and get a compact direction pack for Blender, Three.js, Houdini, or C4D. (✅ active)
- [dsh-git-identity](https://github.com/LoserFox/dsh-git-identity) ⭐7 — DSH 插件：git 提交固定使用环境自身作者身份（优先 gh CLI 登录账号，GitHub noreply 邮箱），GIT_AUTHOR_*/GIT_COMMITTER_* 环境变量注入压过一切 git config (✅ active)
- [dsh-landscape](https://github.com/cyanseek/dsh-landscape) ⭐7 — Agent-first DeepSeek Harness plugin intelligence: verify existing plugins, identify missing capabilities, and generate build-ready briefs. (✅ active)
- [dsh-pdf](https://github.com/sunshine-lang/dsh-pdf) ⭐7 — PDF toolbox: extract text, metadata and page ranges via pdfjs-dist, local with no API key. (✅ active)
- [dsh-plugin-diff-review](https://github.com/Civitasv/dsh-plugin-diff-review) ⭐7 — Diff Review Plugin for DeepSeek Harness (✅ active)
- [dsh-spend](https://github.com/nonewind/dsh-spend) ⭐7 — Token usage and estimated spend: floating panel with per-model/day/session stats and auto-detected billing plans. (✅ active)
- [dsh-token-panel](https://github.com/juhe291/dsh-token-panel) ⭐7 — A corner HUD for DeepSeek Harness that shows your session's token pressure, per-model cost, and daily/monthly usage at a glance — with an editable budget & balance that tracks spending for you. 右下角常驻的 Token 仪表盘：实时查看会话压力、按模型估算花费，预算和余额点一下就能改，每天每月用了多少都有记录。 (✅ active)
- [dsh-weather](https://github.com/sunshine-lang/dsh-weather) ⭐7 — Weather tool: current conditions and multi-day forecasts via Open-Meteo, free with no API key. (✅ active)
- [dskin](https://github.com/dancingmemory/dskin) ⭐7 — Cartoon pixel skin plugin for DSH Web GUI: pixel pets that walk, blink and jump over the original interface. (✅ active)
- [dsh-cue-plugin](https://github.com/unnnnoooo/dsh-cue-plugin) ⭐6 — DeepSeek Harness 的跨会话引用(cue)插件 (✅ active)
- [dsh-email](https://github.com/STARDUSTLC666/dsh-email) ⭐6 — DeepSeek Harness 邮件插件：email_list/read/search/send/folders/attachment 六工具，内置 QQ/163/126/新浪/阿里/Gmail/Outlook/iCloud 八个预设，多账号、附件收发、Web 设置页配置，纯 Node 全平台。· IMAP/SMTP email tools for DeepSeek Harness agents. (✅ active)
- [dsh-file-claim](https://github.com/Nwflower/dsh-file-claim) ⭐6 — File ownership/claim system for parallel agent sessions on the same project: claim/release, heartbeat stale takeover and async 3-way merge. (✅ active)
- [dsh-island](https://github.com/cdxiaodong/dsh-island) ⭐6 — Bridge DSH agent sessions, tool calls, and approvals to the CodeIsland macOS notch panel over a Unix socket, with in-panel allow/deny. (✅ active)
- [dsh-ohos-patch](https://github.com/shenjackyuanjie/dsh-ohos-patch) ⭐6 — 让deepseek harness能在 ohos上跑！ (✅ active)
- [dsh-plugin-anydoc](https://github.com/beancookie/dsh-plugin-anydoc) ⭐6 — Convert Word, PPT, Excel, PDF, EPUB and CSV documents to GitHub-Flavored Markdown via @firecrawl/anydoc. (✅ active)
- [dsh-plugin-installer](https://github.com/Toukaiteio/dsh-plugin-installer) ⭐6 — Marketplace plugin that integrates DeepSeek Harness with the GitHub plugin ecosystem. (✅ active)
- [dsh-plugin-manager](https://github.com/2768651338/dsh-plugin-manager) ⭐6 — DeepSeek Harness 的图形化插件管理插件：在 设置 → 插件 里新增「插件管家」标签页，用中文名和说明展示每个插件是做什么的，并提供一键启停开关与内置备注编辑——启停写入全局层补丁并实时热生效，备注保存到本地覆盖文件长期生效。 (✅ active)
- [dsh-restart](https://github.com/anweat/dsh-restart) ⭐6 — Restart DSH: configurable restart method (Node native / legacy PowerShell), post-restart continue prompt, optional watchdog auto-relaunch. (✅ active)
- [dsh-tdai-memory](https://github.com/Scorp1o117/dsh-tdai-memory) ⭐6 — Agent memory for DeepSeek Harness | DeepSeek Harness 记忆插件 (✅ active)
- [dsh-web-search-exa](https://github.com/TonyDua/dsh-web-search-exa) ⭐6 — Zero-config Exa web search provider: keyless anonymous MCP fallback plus keyed REST search. (✅ active)
- [dsh-calculator](https://github.com/bobcat848/dsh-calculator) ⭐5 — Calculate the real-time cost of DeepSeek API calls made by DeepSeek Harness. (✅ active)
- [dsh-cost-plugin](https://github.com/RoxsLee/dsh-cost-plugin) ⭐5 — DSH 费用/余额读数插件：在输入框统计行旁实时显示「本次 ≈¥x · 会话 ≈¥x · 余额 ¥x」，内置 DeepSeek 官方价目表，支持 2026-08-17 起生效的峰谷定价（按节点时间戳自动选档），余额经官方 /user/balance 实时查询，失败静默降级。 (✅ active)
- [dsh-notify-windows](https://github.com/SeverusZh/dsh-notify-windows) ⭐5 — Windows notifications for DSH, zero dependencies. (✅ active)
- [dsh-session-cleaner](https://github.com/fountunt/dsh-session-cleaner) ⭐5 — 为 DeepSeek Harness 提供会话删除能力，支持侧边栏 ⋮ 菜单入口 (✅ active)
- [dsh-split-panes](https://github.com/lehhair/dsh-split-panes) ⭐5 — Split panes. (✅ active)
- [dsh-status-bar](https://github.com/Starlight-bananice/dsh-status-bar) ⭐5 — Know what your agent is doing at a glance — 17-segment configurable status bar for DeepSeek Harness: status/model/context/tokens/TPS/cost/jobs. 一眼看清你的 agent 正在做什么：17 段可配置 DSH 会话状态栏。 (✅ active)
- [dsh-web-attention-badge](https://github.com/Luaphes/dsh-web-attention-badge) ⭐5 — Attention reminders for the DeepSeek Harness Web UI: frame badge, (N) tab title and whale-favicon recolor for sessions waiting for input or finished unopened. (✅ active)
- [nowledge-mem-deepseek-harness](https://github.com/nowledge-co/nowledge-mem-deepseek-harness) ⭐5 — Community plugin bundle integrating the Nowledge Mem memory service with DeepSeek Harness. (✅ active)
- [zotero-harvest](https://github.com/Fisfzy/zotero-harvest) ⭐5 — Zotero 文献采集入库插件（DSH external plugin）：多源检索（OpenAlex/arXiv/Crossref/Europe PMC/Semantic Scholar）+ OA 下载链接解析（Unpaywall）+ 充分性审计 + 入库本地 Zotero + 触发 zotero-wave-rag 重建 (✅ active)
- [codex-eyes-hands](https://github.com/651002/codex-eyes-hands) ⭐4 — 专为 DeepSeek Harness 打造：把本机 Codex CLI 变成纯文本 AI agent 的眼睛和手——看图/读文件/画图/监督执行/双通道容灾 (✅ active)
- [dsh-approval-gate](https://github.com/moon09300731/dsh-approval-gate) ⭐4 — Risk-gated approval automation for DeepSeek Harness: flash pre-classifies whether a write/command is irreversible — safe operations are auto-approved, dangerous ones are escalated to human approval (fail-safe). (✅ active)
- [dsh-auxiliary](https://github.com/dsh-plugins/dsh-auxiliary) ⭐4 — Auxiliary models for DeepSeek Harness: vision understanding and context compression through dedicated model routes. DeepSeek Harness 辅助模型插件：为视觉理解、上下文压缩、审批审查、子代理、会话标题与图片生成提供独立的模型路由、工具与系统提示，全程不触碰主对话模型。 (✅ active)
- [dsh-deepseek-quota](https://github.com/yingjunnan/dsh-deepseek-quota) ⭐4 — DeepSeek API quota (balance) widget for the DSH web GUI: a floating bottom-right card showing remaining DeepSeek API balance. (✅ active)
- [dsh-ffmpeg](https://github.com/STARDUSTLC666/dsh-ffmpeg) ⭐4 — DeepSeek Harness 视频处理插件：ffmpeg_probe/cut/concat/encode/subtitle/extract/gif 七工具，走官方 subprocess 服务、argv 数组无 shell 注入、零运行时依赖；纯 Node 全平台。· Video processing tools for DeepSeek Harness agents. (✅ active)
- [dsh-guardian](https://github.com/cdxiaodong/dsh-guardian) ⭐4 — Agent security guardrail: intercepts and audits every tool call, requiring human confirmation on sensitive operations. (✅ active)
- [dsh-input-history](https://github.com/lhh010/dsh-input-history) ⭐4 — Terminal-style input history: Ctrl+Up/Ctrl+Down to recall and switch sent messages. (✅ active)
- [dsh-notebooks](https://github.com/havingautism/dsh-notebooks) ⭐4 — Notebooks plugin (cordis). (✅ active)
- [dsh-plugin-deepeye](https://github.com/Favio8/dsh-plugin-deepeye) ⭐4 — DeepEye vision plugin for DeepSeek Harness (DSH): image description, OCR, VQA, UI layout, and clipboard analysis. (✅ active)
- [dsh-rss](https://github.com/STARDUSTLC666/dsh-rss) ⭐4 — DeepSeek Harness RSS 订阅插件：rss_list/add/remove/fetch/check 五工具，RSS 0.9x/1.0/2.0 与 Atom 归一化解析，订阅列表持久化到 settings，proxyUrl 特殊代理支持；纯 Node 全平台。· RSS/Atom subscription tools for DeepSeek Harness agents. (✅ active)
- [dsh-skill-hub](https://github.com/cheshireez/dsh-skill-hub) ⭐4 — In-GUI skill manager for DeepSeek Harness: browse, search, toggle, inspect, diagnose and scaffold local skills from the official ctx.skills registry, plus a skill market with tracked source sync and one-click update-all. (✅ active)
- [dsh-tool-git](https://github.com/lxj808624/dsh-tool-git) ⭐4 — Structured safe Git tools: status/diff/log/branch/stage/commit/stash/show with a destructive-command guard. (✅ active)
- [dsh-verification-receipt](https://github.com/030611/dsh-verification-receipt) ⭐4 — Privacy-minimal heuristic per-turn verification summaries for DeepSeek Harness (✅ active)
- [dsh-wordbox](https://github.com/arcmosin/dsh-wordbox) ⭐4 — Persistent common-word panel beside the composer with global/project buckets and one-click insert. (✅ active)
- [dsh-workspace-search](https://github.com/tsonglew/dsh-workspace-search) ⭐4 — VS Code-style workspace keyword search: a Search tab for the Better Sidebar ecosystem. (✅ active)
- [deepseek-harness-plugin-manager](https://github.com/hrhgit/deepseek-harness-plugin-manager) ⭐3 — Web plugin manager for DeepSeek Harness (DSH): inspect, search, group, enable, and disable Cordis plugins. (✅ active)
- [dsh-agentmemory](https://github.com/elementor-i/dsh-agentmemory) ⭐3 — agentmemory for DeepSeek Harness (dsh): full memory_* tools, capture hooks, and context injection over the local REST server (✅ active)
- [dsh-calendar](https://github.com/STARDUSTLC666/dsh-calendar) ⭐3 — DeepSeek Harness 日历插件：calendar_list/create/update/delete/search 五工具，CalDAV 协议支持 Google/iCloud/Nextcloud/自定义端点，RRULE 重复事件自动展开，插件级 proxyUrl 代理，配置缺失不崩启动；纯 Node 全平台。· CalDAV calendar tools for DeepSeek Harness agents. (✅ active)
- [dsh-diagram](https://github.com/hanzhangzzz/dsh-diagram) ⭐3 — Turn articles in DeepSeek Harness into editable Excalidraw canvases. (✅ active)
- [dsh-docker](https://github.com/STARDUSTLC666/dsh-docker) ⭐3 — DeepSeek Harness 容器管理插件：docker_ps/logs/inspect/exec/manage 五工具，官方 subprocess 服务、argv 无 shell 注入、exec 审批门、零运行时依赖。· Containers for DeepSeek Harness agents. (✅ active)
- [dsh-doctor](https://github.com/astra3294/dsh-doctor) ⭐3 — Deterministic diagnostics and recovery for DeepSeek Harness (✅ active)
- [dsh-file-uploads](https://github.com/l541402398/dsh-file-uploads) ⭐3 — Upload arbitrary local files from the Web composer with pending cards, managed in Settings. (✅ active)
- [dsh-llm-inspector](https://github.com/cdxiaodong/dsh-llm-inspector) ⭐3 — Unified LLM request/response inspector: reasoning-effort tuning, external-think export, traffic & bundle analysis. (✅ active)
- [dsh-memory](https://github.com/flymysql/dsh-memory) ⭐3 — Cross-session memory vault: memory_remember / memory_recall / memory_forget tools with a Settings page. (🧪 experimental)
- [dsh-memory-evidence](https://github.com/LeslieWylie/dsh-memory-evidence) ⭐3 — Git-first memory navigation and bounded evidence tools for DeepSeek Harness. (💤 inactive)
- [dsh-plugin-meta-memory](https://github.com/YYTbit/dsh-plugin-meta-memory) ⭐3 — Structured long-term memory system for DeepSeek Harness (✅ active)
- [dsh-plugin.github.io](https://github.com/dsh-plugin/dsh-plugin.github.io) ⭐3 — DeepSeek Harness community plugin workshop and directory (✅ active)
- [dsh-plugins-raincode](https://github.com/rainforest888/dsh-plugins-raincode) ⭐3 — dsh plugin: DeepSeek Harness 的模型层 = raincode(模型池/缓存/重试) + /skills 浏览 (✅ active)
- [dsh-prompt-stash](https://github.com/Wine-Red/dsh-prompt-stash) ⭐3 — Local, per-session prompt stash for DeepSeek Harness Web | 本地、分对话的提示词输入暂存工具。写了一半的长提示词，临时需要先问一个短问题？ 同时准备多个方案，但尚未决定发哪一个？将未完成的想法放入草稿架中，准备好后再继续完成 (✅ active)
- [dsh-prompt-studio](https://github.com/Moeblack/dsh-prompt-studio) ⭐3 — Edit user and built-in system-prompt sections with live preview. (✅ active)
- [dsh-suggested-replies](https://github.com/Anionex/dsh-suggested-replies) ⭐3 — Predicted next-message candidates above the DSH Web composer, one click to fill the draft. (✅ active)
- [dsh-telemetry-redactor](https://github.com/030611/dsh-telemetry-redactor) ⭐3 — Fail-closed export-copy redaction for DeepSeek Harness session telemetry (✅ active)
- [dsh-tool-search](https://github.com/vibeinging/dsh-tool-search) ⭐3 — Per-agent on-demand tool discovery and progressive schema disclosure. (✅ active)
- [dsh-ultra-ui](https://github.com/havingautism/dsh-ultra-ui) ⭐3 — Ultra UI plugin (cordis). (✅ active)
- [dsh-usage-plugin](https://github.com/Yihong89/dsh-usage-plugin) ⭐3 — DeepSeek Harness (DSH) plugins. First: dsh-usage-report — per-session token usage & estimated cost (/usage + usage_report), priced from the DeepSeek pricing table. (✅ active)
- [dsh-vision-tools](https://github.com/moon09300731/dsh-vision-tools) ⭐3 — Full vision-capability bundle for DeepSeek Harness: a vision_understand tool (OpenAI-compatible vision APIs, free Zhipu GLM-4V-Flash by default) plus paste/drag-and-drop/button entry points for image recognition. (✅ active)
- [dsh-webbridge](https://github.com/bill9109/dsh-webbridge) ⭐3 — DSH combined with Kimi WebBridge for real browser control. (✅ active)
- [mistymoon-dsh](https://github.com/mianyoubiaoqing/MistyMoon-DSH) ⭐3 — Local-first long-term companion plugin suite for DeepSeek Harness (✅ active)
- [URL Manager](https://github.com/Piccolo123/url-manager) ⭐3 — Agent-first URL and knowledge collection system: auto-categorize, tag, full-text search and shared collections. (✅ active)
- [zotero-wave-rag](https://github.com/Fisfzy/zotero-wave-rag) ⭐3 — 面向 Zotero 论文库的浪潮式 RAG 细节检索系统 —— DSH 外部插件。移植 VCPToolBox 浪潮语义动力学思想（标签河道图传播/虫洞跳转/钟型阻尼/Ω重排），配 BM25+RRF 混合检索、claim-evidence 忠实度校验、两级增量索引 (✅ active)
- [DSH Composer Layout](https://github.com/lavapapa/dsh-composer-layout) ⭐2 — Lets you read a long answer while drafting the next detailed prompt beside it in DSH Web. (✅ active)
- [dsh-adb](https://github.com/SamXiaBing/dsh-adb) ⭐2 — ADB device & bench operations: device discovery, structured logcat (background streaming), apk install, file pull/push, dumpsys performance snapshots. (✅ active)
- [dsh-cost-meter](https://github.com/Sttrevens/dsh-cost-meter) ⭐2 — dsh plugin: per-turn USD cost badge in the Web UI (session total + per-message footer, hover breakdown) from token usage x a configurable pricing table. (✅ active)
- [dsh-memoria](https://github.com/jiayan-xu/dsh-memoria) ⭐2 — Vector + graph memory backend with namespace isolation, automatic observation, recall, importance handling and hot reload. (🧪 experimental)
- [dsh-memory (Jesse-njx)](https://github.com/Jesse-njx/dsh-memory) ⭐2 — Cited memory over DSH's lossless session log: distilled, human-auditable facts with citations. (✅ active)
- [dsh-pin-recall](https://github.com/kerwin2046/dsh-pin-recall) ⭐2 — Pin assistant replies from the action strip and recall them into the next model turn (/pin /recall). (✅ active)
- [dsh-plugin-description](https://github.com/MysaDC/dsh-plugin-description) ⭐2 — mount one row in the composition and every plugin card on the Web Settings plugin list page gets a bilingual (zh/en) description; it also publishes the pluginDescriptions service so other plugins can register their own descriptions. (✅ active)
- [dsh-plugin-radar](https://github.com/dshplugin-me/dsh-plugin-radar) ⭐2 — Find DSH plugins by asking in plain language, then security-scan them before install (✅ active)
- [dsh-review-loop](https://github.com/wuxiangru915/dsh-review-loop) ⭐2 — Incremental diff reviewer: checkpoint-based review queue with a Web UI panel and /review command. (✅ active)
- [dsh-scout](https://github.com/omdsh-dev/dsh-scout) ⭐2 — 面向 DeepSeek Harness 的只读环境探测插件，为智能体提供运行环境、软件版本、系统资源、端口、服务、硬件及工作区信息。 (✅ active)
- [dsh-session-search](https://github.com/Tieboyh/dsh-session-search) ⭐2 — Index-free cross-agent session search for DeepSeek Harness. (✅ active)
- [dsh-test-runner](https://github.com/suimi8/dsh-test-runner) ⭐2 — Structured test runner tool: auto-detect vitest/jest/pytest/node:test, run tests and parse failure summaries for the model. (✅ active)
- [dsh-turn-navigator](https://github.com/vibeinging/dsh-turn-navigator) ⭐2 — Private DSH Web turn navigation plugin (✅ active)
- [dsh-view-modes](https://github.com/NigelYao/dsh-view-modes) ⭐2 — Output modes with Verbose, Normal and Summary views plus semantic grouping for tool calls and thinking. (✅ active)
- [dsh-what-changed](https://github.com/sjh9714/dsh-what-changed) ⭐2 — Session-wide file change review in the session header. Lists every file the agent wrote this session with its hunks, counts refused writes separately from changes, and folds from a session projection rather than the on-disk log. (✅ active)
- [visual-review](https://github.com/wang-bool/visual-review) ⭐2 — Renders pasted/uploaded images inline in the DSH Web chat and gives text-only models vision: cloud multimodal API first, local Qwen3-VL fallback. (✅ active)
- [dsh-computer-use](https://github.com/xiaoheizi1212/dsh-computer-use) ⭐1 — Model-agnostic Computer Use for DSH: isolated browser, Windows native helper and third-party bridges. (✅ active)
- [dsh-doctor](https://github.com/asdf17128/dsh-doctor) ⭐1 — Find what your DeepSeek Harness (dsh) patches silently broke — dead patches, config fields dropped by whole-config replacement, unmaintained plugins. Read-only, zero deps. (✅ active)
- [dsh-humanizer](https://github.com/lynote-ai/dsh-humanizer) ⭐1 — Writing tool for the agent: removes AI-sounding patterns and clones your personal voice. 8 deterministic tools scan text, build a style fingerprint from your samples, and return rewrite briefs. (🧪 experimental)
- [dsh-news-plugin](https://github.com/canghai666x/dsh-news-plugin) ⭐1 — RSS/news ingestion returning structured title/link/source/date/summary for downstream model ranking and briefing. (✅ active)
- [dsh-payload-capture](https://github.com/Moeblack/dsh-payload-capture) ⭐1 — Captures every upstream model API payload to JSON for debugging and observability. (✅ active)
- [dsh-plugin-evaluation-standards](https://github.com/dsh-plugin-evaluation/dsh-plugin-evaluation-standards) ⭐1 — Open evaluation datasets, test cases, and metrics for DSH plugins. (✅ active)
- [dsh-plugin-manager-registry](https://github.com/Jesse-njx/dsh-plugin-manager-registry) ⭐1 — @dsh-pm/registry — discover dsh plugins by merging the awesome-dsh-plugin list, GitHub dsh-plugin-topic search, and npm keyword search into one deduped, offline-tolerant registry (the discovery engine of dsh pm) (✅ active)
- [dsh-plugin-quote-reply](https://github.com/yangYzc/dsh-plugin-quote-reply) ⭐1 — DSH plugin: select text in a conversation, then quote it into the composer or reply in a new window. / DeepSeek Harness 划词引用插件：选中文字一键引用回复或新窗口回复。 (✅ active)
- [dsh-plugin-radar](https://github.com/DshMarketPlace/dsh-plugin-radar) ⭐1 — Userscript: marks DeepSeek Harness plugins on GitHub and npm, with the install command that actually works (✅ active)
- [dsh-repo-setup](https://github.com/gongyijie85/dsh-repo-setup) ⭐1 — Read-only repo bootstrap scanner (repo_setup_scan tool): detects stack/tests/docs/git/db and recommends plugins, MCP servers and hygiene files (claude-code-setup counterpart). (✅ active)
- [dsh-turn-index](https://github.com/Simon314620/dsh-turn-index) ⭐1 — Turn-index sidebar: one entry per user turn, click to jump with scroll-spy highlighting. (✅ active)
- [dsh-voice-webspeech](https://github.com/anweat/dsh-voice-webspeech) ⭐1 — Browser Web Speech API voice input for DSH: zero server, zero keys, zero model downloads (Edge=Azure, Chrome=Google speech). (✅ active)
- [dshp](https://github.com/asdf17128/dshp) ⭐1 — Manage DeepSeek Harness profiles — list, create, clone, diff, and share a whole dsh setup as one portable file. (✅ active)
- [dsh-client-auto-retry](https://github.com/Frog755/dsh-client-auto-retry)  — Auto-resumes interrupted DSH turns: sends a queued 继续 after error/interrupted/max-tokens turn-end, with grace period, cooldown, consecutive cap, boot scan and a settings card; never switches models or providers. (✅ active)
- [dsh-deepseek-balance](https://github.com/dshiq04/dsh-deepseek-balance)  — 面向deepseek harness的余额查看插件 (✅ active)
- [dsh-evoforge](https://github.com/deepseek-harness-evoforge/dsh-evoforge)  — Evidence-driven, cache-stable extensions for DeepSeek Harness (✅ active)
- [dsh-fork-to-preset](https://github.com/bpc-oss/dsh-fork-to-preset)  — Fork any session into a different agent preset from the conversation header: a preset-picker button that creates a new child session mounted on the chosen preset, inheriting the source session completed turns. (✅ active)
- [dsh-git-branch-switcher](https://github.com/mixin-ai/dsh-git-branch-switcher)  — Session-header git branch pill: shows the workspace branch and switches it from the Web UI. (✅ active)
- [dsh-llm-local-token](https://github.com/tianxia--/dsh-llm-local-token)  — DeepSeek Harness provider routes that reuse local Codex CLI and Claude Code OAuth tokens instead of API keys. (✅ active)
- [dsh-plugin](https://github.com/dsh-plugin-dev/dsh-plugin)  — Build your own coding agent with Pi dsh-plugin (✅ active)
- [dsh-plugin-cost](https://github.com/yweilai77-dev/dsh-plugin-cost)  — Session cost estimate in the DSH Web composer dock (tokenUsage × configurable price table, one-click official-price refresh). (✅ active)
- [dsh-precedent](https://github.com/dshplugin-me/dsh-precedent)  — Evidence-backed working memory for DeepSeek Harness: a cited ledger of what already worked in this workspace, built from the session log you already have. No index, no model, no capture step. (✅ active)
- [dsh-routed-subagent](https://github.com/bpc-oss/dsh-routed-subagent)  — Run a one-shot subagent fully mounted on any agent preset from any session, with per-call model/provider override, a model-availability pre-check, and external CLI engines (codex / claude / codebuddy) with background jobs, live progress, kill, and continuable sessions. (✅ active)
- [dsh-session-cleaner-cli](https://github.com/ChenChen913/dsh-session-cleaner-cli)  — 深度清理 DeepSeek Harness (DSH) 工作区会话的离线 CLI：按工作区列出/删除/恢复会话，自动同步工作区账目与投影缓存。Offline session cleaner for DeepSeek Harness: list, delete (trash+restore) and prune ghost sessions across workspaces. (✅ active)

### Skills


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [memos](https://github.com/MemTensor/MemOS) | ⭐10,873 | Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings and DeepSeek Harness support. | ✅ active |
| 2 | [easyeda-agent](https://github.com/zhoushoujianwork/easyeda-agent) | ⭐274 | EasyEDA Pro automation: Go daemon + in-app connector + agent skill + stdio MCP server for typed schematic/PCB actions, workflow gates, and DRC. | ✅ active |
| 3 | [dsh-skill-viewer](https://github.com/Fishquito7/dsh-skill-viewer) | ⭐88 | DSH Web UI plugin: Skills settings section with hot enable/disable, delete and add. | ✅ active |
| 4 | [dsh-reverse-skill](https://github.com/dhicoc/dsh-reverse-skill) | ⭐58 | Complete reverse-skill (85 SKILL.md) as a DeepSeek Harness (dsh) Cordis plugin — reverse engineering, authorized pentesting and security research skill pack. | ✅ active |
| 5 | [dsh-science](https://github.com/biociao/dsh-science) | ⭐24 | Claude Science-style research workbench: ReAct research-loop engine (research_* tools), versioned artifacts with provenance (artifact_* tools), and 10 science skills for genomics/pathogens/bioinformatics. | ✅ active |
| 6 | [dsh-plugin-development](https://github.com/w2112515/dsh-plugin-development) | ⭐14 | Portable Agent Skill for developing and auditing DeepSeek Harness plugins, with an optional profile-installable DSH bundle adapter. | ✅ active |
| 7 | [dsh_plugin_swift_cycle](https://github.com/Solismuchengxue/dsh_plugin_swift_cycle) | ⭐14 | Swift Cycle governance skill adapter for DeepSeek Harness; user-invoked, version-pinned, and offline-verifiable. | ✅ active |
| 8 | [dsh-plugin-dev](https://github.com/omdsh-dev/dsh-plugin-dev) | ⭐13 | Field-tested plugin development playbook (skill + docs): cordis dual copies, tsconfig triplets, Windows junctions and multi-frame zstd. | ✅ active |
| 9 | [dsh-plugin-skills](https://github.com/omdsh-dev/dsh-plugin-skills) | ⭐11 | Agent skills for building and testing DeepSeek Harness plugins, from scaffolding a package to publishing. | ✅ active |
| 10 | [dsh-godot-skill](https://github.com/akira399/dsh-godot-skill) | ⭐9 | Godot Engine 4.x full-stack game development skill plugin for DSH. | ✅ active |

#### Complete list (30)

- [memos](https://github.com/MemTensor/MemOS) ⭐10,873 — Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings and DeepSeek Harness support. (✅ active)
- [easyeda-agent](https://github.com/zhoushoujianwork/easyeda-agent) ⭐274 — EasyEDA Pro automation: Go daemon + in-app connector + agent skill + stdio MCP server for typed schematic/PCB actions, workflow gates, and DRC. (✅ active)
- [dsh-skill-viewer](https://github.com/Fishquito7/dsh-skill-viewer) ⭐88 — DSH Web UI plugin: Skills settings section with hot enable/disable, delete and add. (✅ active)
- [dsh-reverse-skill](https://github.com/dhicoc/dsh-reverse-skill) ⭐58 — Complete reverse-skill (85 SKILL.md) as a DeepSeek Harness (dsh) Cordis plugin — reverse engineering, authorized pentesting and security research skill pack. (✅ active)
- [dsh-science](https://github.com/biociao/dsh-science) ⭐24 — Claude Science-style research workbench: ReAct research-loop engine (research_* tools), versioned artifacts with provenance (artifact_* tools), and 10 science skills for genomics/pathogens/bioinformatics. (✅ active)
- [dsh-plugin-development](https://github.com/w2112515/dsh-plugin-development) ⭐14 — Portable Agent Skill for developing and auditing DeepSeek Harness plugins, with an optional profile-installable DSH bundle adapter. (✅ active)
- [dsh_plugin_swift_cycle](https://github.com/Solismuchengxue/dsh_plugin_swift_cycle) ⭐14 — Swift Cycle governance skill adapter for DeepSeek Harness; user-invoked, version-pinned, and offline-verifiable. (✅ active)
- [dsh-plugin-dev](https://github.com/omdsh-dev/dsh-plugin-dev) ⭐13 — Field-tested plugin development playbook (skill + docs): cordis dual copies, tsconfig triplets, Windows junctions and multi-frame zstd. (✅ active)
- [dsh-plugin-skills](https://github.com/omdsh-dev/dsh-plugin-skills) ⭐11 — Agent skills for building and testing DeepSeek Harness plugins, from scaffolding a package to publishing. (✅ active)
- [dsh-godot-skill](https://github.com/akira399/dsh-godot-skill) ⭐9 — Godot Engine 4.x full-stack game development skill plugin for DSH. (✅ active)
- [dsh-codex-port](https://github.com/STARDUSTLC666/dsh-codex-port) ⭐8 — DeepSeek Harness 技能移植插件：把 ~/.codex 的 Codex 官方插件（186+ 个、583+ 技能）一键移植为 DSH 技能（codex_list/port/status），frontmatter 自动转换、幂等跳过。· Batch-port the Codex plugin family into DSH skills. (✅ active)
- [dsh-book2skill](https://github.com/omdsh-dev/dsh-book2skill) ⭐4 — Book-to-skill plugin: a 5-stage long task that fetches, parses, understands, generates and installs a skill. (✅ active)
- [dsh-remotion](https://github.com/STARDUSTLC666/dsh-remotion) ⭐4 — DSH 视频创作技能插件：注册 Remotion 官方移植技能（React 编程式视频，38 个规则文件），安装即用。· Remotion skill plugin for DeepSeek Harness. (✅ active)
- [dsh-ecc](https://github.com/gongyijie85/dsh-ecc) ⭐3 — 273 ECC skills (95.8% of the 227k-star operator system) ported to DSH in four batches. (✅ active)
- [dsh-find-skill](https://github.com/Moximxxx/dsh-find-skill) ⭐3 — Bridges the vercel-labs/skills ecosystem: LLM-driven skill search, install and management. (✅ active)
- [dsh-humanize](https://github.com/zevorn/dsh-humanize) ⭐3 — De-AI writing skill: rewrite agent output to sound more human. (✅ active)
- [dsh-memoryhub](https://github.com/solknight48/dsh-memoryhub) ⭐3 — MemoryHub (mh) plugin for DeepSeek Harness (dsh): auto-loads checkpoint memory on session start, adds mh_* tools and the mh skill, and a Memory tab in the web UI (✅ active)
- [dsh-skillradar](https://github.com/hellosky983/dsh-skillradar) ⭐3 — Scans session-visible skills and ranks them by relevance to the recent conversation. (✅ active)
- [dsh-web-novel-research](https://github.com/canghai666x/dsh-web-novel-research) ⭐3 — Chinese web-novel plot lookup skill: free mirror-site workflow with GBK decoding and duplicate-chapter disambiguation. (✅ active)
- [deepseek-harness-skillx](https://github.com/drowned-fish1/deepseek-harness-skillx) ⭐2 — Skill collection for DeepSeek Harness workflows. (✅ active)
- [dsh-kb-sieve](https://github.com/omdsh-dev/dsh-kb-sieve) ⭐2 — DSH knowledge-base plugin: build audit-able KB packs (references + SQLite FTS5) from md/txt/docx/pdf, deterministic retrieval (kb_query) and original-text reading (kb_read), zero-script generated skills. Apache-2.0. (✅ active)
- [dsh-ponytail](https://github.com/gongyijie85/dsh-ponytail) ⭐2 — Ponytail lazy senior dev mode: 6 skills (ponytail, ponytail-audit, ponytail-debt, ponytail-gain, ponytail-help, ponytail-review) adapted from DietrichGebert/ponytail. (✅ active)
- [dsh-review-skills](https://github.com/ben7am1n/dsh-review-skills) ⭐2 — Code review skill pack for DeepSeek Harness. (✅ active)
- [dsh-skill-pack-security](https://github.com/PerryLink/dsh-skill-pack-security) ⭐2 — Security-audit skill pack: 5 agent skills covering secret scan, dependency audit and more. (✅ active)
- [dsh-skillport](https://github.com/Jesse-njx/dsh-skillport) ⭐2 — Every skill you already have — Claude Code, Codex, Cursor, Gemini CLI — works in DSH. (✅ active)
- [mattpocock-skills-dsh](https://github.com/gongyijie85/mattpocock-skills-dsh) ⭐2 — Matt Pocock full promoted skill set (25 SKILL.md: grilling, writing-for-agents, wait-what, TDD, code review, wayfinder, ask-matt router) ported to DSH. (✅ active)
- [howto-dsh](https://github.com/dshworks/howto-dsh) ⭐1 — Verified field notes for DeepSeek Harness (dsh): traps, skills, hooks, profiles. Every claim dated against a dsh version, with source paths to re-verify. Not affiliated with DeepSeek. (✅ active)
- [mattpocock-skills-dsh-zh](https://github.com/gongyijie85/mattpocock-skills-dsh-zh) ⭐1 — Matt Pocock's 25 skills fully translated to Chinese (technical terms kept in English with glosses). (✅ active)
- [dsh-news-briefing](https://github.com/canghai666x/dsh-news-briefing)  — News briefing skill: multi-dimensional story scoring, anti-clickbait rules, content prioritization and Chinese editorial style. (✅ active)
- [mstar-workflow](https://github.com/btspoony/mstar-workflow)  — A Skill-driven Harness/Loop Engineering Workflow Agent Plugin (💤 inactive)

### Workflows & Automation


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [tongflow](https://github.com/tong-io/tongflow) | ⭐902 | TongFlow — multimodal workflow studio and engine (canvas + Python plugin engine) and dsh-tongflow, the DeepSeek Harness studio plugin | ✅ active |
| 2 | [dsh_workflow](https://github.com/omdsh-dev/dsh_workflow) | ⭐92 | 把Claude Code的UltraCode模式带给DSH，把 DSH 的一次性多 Agent 调度，升级为可生成、可保存、可治理、可观察、可恢复的 Workflow 层 | ✅ active |
| 3 | [dsh_workflow](https://github.com/icetomoyo/dsh_workflow) | ⭐92 | Brings Claude Code's UltraCode mode to DSH: upgrade one-shot multi-agent dispatch into a generatable, saveable, governable, observable, recoverable workflow layer. | ✅ active |
| 4 | [dsh-plugin-agent-workflow](https://github.com/xuanyuanzhifeng/dsh-plugin-agent-workflow) | ⭐78 | DeepSeek Harness Agent Workflow | ✅ active |
| 5 | [dsh-automation](https://github.com/titanwings/dsh-automation) | ⭐70 | Run coding tasks on a schedule in fresh Agent sessions, managed by the user or the agent itself. | ✅ active |
| 6 | [mstar-harness](https://github.com/btspoony/mstar-harness) | ⭐52 | Skill-driven harness/loop engineering workflow agent: tune agent loops as a first-class workflow. | ✅ active |
| 7 | [dsh-plans](https://github.com/Optim-Agent/dsh-plans) | ⭐42 | Human-in-the-loop planning preset adapted from prime-plans: researched, reviewed, executed. | ✅ active |
| 8 | [dsh-auto-continue](https://github.com/HsiangNianian/dsh-auto-continue) | ⭐33 | Auto-resumes interrupted DSH Web requests: failure classification, adaptive retry, configurable continue message and browser notifications. | ✅ active |
| 9 | [dsh-deep-research](https://github.com/omdsh-dev/dsh-deep-research) | ⭐18 | Adaptive deep-research orchestrator built on the official workflow engine. | ✅ active |
| 10 | [dsh-harness-ops](https://github.com/fakechris/dsh-harness-ops) | ⭐11 | Ops toolbox: A/B dual-slot daily snapshot rotation with atomic switch and one-click rollback, plus a 10s watchdog. | ✅ active |

#### Complete list (26)

- [tongflow](https://github.com/tong-io/tongflow) ⭐902 — TongFlow — multimodal workflow studio and engine (canvas + Python plugin engine) and dsh-tongflow, the DeepSeek Harness studio plugin (✅ active)
- [dsh_workflow](https://github.com/omdsh-dev/dsh_workflow) ⭐92 — 把Claude Code的UltraCode模式带给DSH，把 DSH 的一次性多 Agent 调度，升级为可生成、可保存、可治理、可观察、可恢复的 Workflow 层 (✅ active)
- [dsh_workflow](https://github.com/icetomoyo/dsh_workflow) ⭐92 — Brings Claude Code's UltraCode mode to DSH: upgrade one-shot multi-agent dispatch into a generatable, saveable, governable, observable, recoverable workflow layer. (✅ active)
- [dsh-plugin-agent-workflow](https://github.com/xuanyuanzhifeng/dsh-plugin-agent-workflow) ⭐78 — DeepSeek Harness Agent Workflow (✅ active)
- [dsh-automation](https://github.com/titanwings/dsh-automation) ⭐70 — Run coding tasks on a schedule in fresh Agent sessions, managed by the user or the agent itself. (✅ active)
- [mstar-harness](https://github.com/btspoony/mstar-harness) ⭐52 — Skill-driven harness/loop engineering workflow agent: tune agent loops as a first-class workflow. (✅ active)
- [dsh-plans](https://github.com/Optim-Agent/dsh-plans) ⭐42 — Human-in-the-loop planning preset adapted from prime-plans: researched, reviewed, executed. (✅ active)
- [dsh-auto-continue](https://github.com/HsiangNianian/dsh-auto-continue) ⭐33 — Auto-resumes interrupted DSH Web requests: failure classification, adaptive retry, configurable continue message and browser notifications. (✅ active)
- [dsh-deep-research](https://github.com/omdsh-dev/dsh-deep-research) ⭐18 — Adaptive deep-research orchestrator built on the official workflow engine. (✅ active)
- [dsh-harness-ops](https://github.com/fakechris/dsh-harness-ops) ⭐11 — Ops toolbox: A/B dual-slot daily snapshot rotation with atomic switch and one-click rollback, plus a 10s watchdog. (✅ active)
- [dsh-deepresearch](https://github.com/havingautism/dsh-deepresearch) ⭐9 — DeepResearch plugin (cordis) for the Harness. (🧪 experimental)
- [dsh-inspect](https://github.com/omdsh-dev/dsh-inspect) ⭐6 — Adversarial checkup → fix → review loop built on the official workflow engine. (✅ active)
- [dsh-plugin-spur](https://github.com/HuanLinOTO/dsh-plugin-spur) ⭐6 — Hang a whip in the chat stream: flick it (>2.0 px/ms) to send the agent a 'go work' message. (✅ active)
- [dsh-task-dag](https://github.com/LeemanCheung/dsh-task-dag) ⭐6 — Persistent live DAG visualization of workflow runs, subagents, status and dependencies. (✅ active)
- [dsh-track](https://github.com/fakechris/dsh-track) ⭐6 — Embedded task-management engine: decision-point protocol, thought-capture wall and Linear-style issue storage. (✅ active)
- [engineer-software](https://github.com/KirschBluteX/engineer-software) ⭐6 — Runtime-neutral, evidence-driven software engineering workflow for Codex and DeepSeek Harness. (✅ active)
- [dsh-companion](https://github.com/william-jin-cmu/dsh-companion) ⭐5 — Resident desktop assistant: global hotkey, scheduled automation, quick replies and a plugin market. (💤 inactive)
- [dsh-continual-harness](https://github.com/jasen215/dsh-continual-harness) ⭐4 — DeepSeek Harness plugin for continual self-evolution: persistent memory, periodic review-and-refine, cross-session shared knowledge, and automatic rollback — a plan→validate→apply→rollback loop driven by a model-callable harness_refine tool. (✅ active)
- [dsh-doublecheck](https://github.com/PerryLink/dsh-doublecheck) ⭐4 — Engineering-discipline loop: requirement grilling before edits, red/green test-evidence gates and adversarial delivery review. (✅ active)
- [dsh-prime-agent](https://github.com/yoke233/dsh-prime-agent) ⭐4 — Prime Agent-inspired persistent RLM control plane for DSH Code Mode. (✅ active)
- [dsh-agent-orchestration](https://github.com/LeslieWylie/dsh-agent-orchestration) ⭐3 — Evidence-first multi-agent workflow planning, handoff validation, and Loop Guard skills for DeepSeek Harness. (💤 inactive)
- [dsh-eval](https://github.com/hccccc01333/dsh-eval) ⭐1 — Agent evaluation platform: benchmark YAML, headless dsh runs, trace-based metrics, scripted grading and run comparison. (✅ active)
- [dsh-governance](https://github.com/tappass/dsh-governance) ⭐1 — Authority layer for agentic AI as a DSH plugin: governs every tool call against your policies. (✅ active)
- [dsh-report-studio](https://github.com/ciceroyang/dsh-report-studio) ⭐1 — Turn a DSH session into deliverable work reports (daily/weekly/handoff/article) with verifiable receipts. (✅ active)
- [dsh-trajectory-debug](https://github.com/devmom/dsh-trajectory-debug) ⭐1 — Trajectory waterfall, deterministic replay, breakpoints, edit-and-rerun, fork compare and performance analytics. (✅ active)
- [dsh-plugin-skill](https://github.com/dsh-io/dsh-plugin-skill)  — Agent skill (SKILL.md) for creating DeepSeek Harness (dsh) plugins: authoritative defineTool API, schema rules, project layout and workflow — works with Claude Code, Codex, Cursor, Gemini CLI, opencode (✅ active)

### Agents & Multi-Agent


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [openbiliclaw](https://github.com/whiteguo233/OpenBiliClaw) | ⭐2,971 | 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin） | ✅ active |
| 2 | [dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) | ⭐746 | Multi-agent team-oriented extensions for DSH. | ✅ active |
| 3 | [dsh-agent-rp](https://github.com/hewzhew/dsh-agent-rp) | ⭐169 | SillyTavern migration and next-generation Agent roleplay for DSH. | ✅ active |
| 4 | [dsh-data-agent](https://github.com/omdsh-dev/dsh-data-agent) | ⭐104 | Session-scoped database connections with a dedicated data agent: let the model connect to databases and write SQL. | ✅ active |
| 5 | [dsh-openbiliclaw](https://github.com/whiteguo233/dsh-openbiliclaw) | ⭐48 | OpenBiliClaw 是本地运行的跨平台个性化内容推荐 Agent，持续理解你的兴趣并主动找内容。本仓库是它的 DeepSeek Harness 插件：DSH 界面常驻第四栏（推荐/内容库/对话/画像/设置），注册 22 个 Agent Bridge 工具，让 Agent 也能读推荐、答探测、闭环学习。 | ✅ active |
| 6 | [allinluna](https://github.com/zenx0x/allinluna) | ⭐41 | Resource-aware multi-agent orchestration for Codex and DeepSeek Harness (All in Flash DSH plugin). | ✅ active |
| 7 | [dsh-tianshu-build](https://github.com/huiliyi37/dsh-tianshu-build) | ⭐36 | DeepSeek X Tianshu  Harness build 是一款完全体开源 coding agent:在 dsh harness 基础之上带视觉、跨会话记忆、验证门、agent 路由、语义 + 图谱代码检索、文件回滚和全屏终端 UI——全部以插件组合。  它是 DeepSeek Harness(dsh)的友好 MIT fork, 它保留了上游一切皆插件的架构，并将以harness最佳形态和架构往下演进。 | ✅ active |
| 8 | [dsh-interconnect](https://github.com/Chinesezjc/dsh-interconnect) | ⭐34 | Cross-instance message/event handoff plugins (interconnect service + tools). | ✅ active |
| 9 | [dsh-plugin-cc](https://github.com/cpj-dev/dsh-plugin-cc) | ⭐29 | Bridge DeepSeek Harness into Claude Code for review, critique, delegation and session import. | ✅ active |
| 10 | [kixparadigm](https://github.com/olicesx/kixparadigm) | ⭐23 | kixparadigm — AI self-orchestrated minimal paradigm (resident cognition layer) + kixpower multi-agent orchestration · one-command import into DeepSeek Harness (npm i -g) / AI 自编排最小范式（认知层常驻）× kixpower 多智能体编排 · npm 一键导入 DeepSeek Harness | ✅ active |

#### Complete list (24)

- [openbiliclaw](https://github.com/whiteguo233/OpenBiliClaw) ⭐2,971 — 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin） (✅ active)
- [dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) ⭐746 — Multi-agent team-oriented extensions for DSH. (✅ active)
- [dsh-agent-rp](https://github.com/hewzhew/dsh-agent-rp) ⭐169 — SillyTavern migration and next-generation Agent roleplay for DSH. (✅ active)
- [dsh-data-agent](https://github.com/omdsh-dev/dsh-data-agent) ⭐104 — Session-scoped database connections with a dedicated data agent: let the model connect to databases and write SQL. (✅ active)
- [dsh-openbiliclaw](https://github.com/whiteguo233/dsh-openbiliclaw) ⭐48 — OpenBiliClaw 是本地运行的跨平台个性化内容推荐 Agent，持续理解你的兴趣并主动找内容。本仓库是它的 DeepSeek Harness 插件：DSH 界面常驻第四栏（推荐/内容库/对话/画像/设置），注册 22 个 Agent Bridge 工具，让 Agent 也能读推荐、答探测、闭环学习。 (✅ active)
- [allinluna](https://github.com/zenx0x/allinluna) ⭐41 — Resource-aware multi-agent orchestration for Codex and DeepSeek Harness (All in Flash DSH plugin). (✅ active)
- [dsh-tianshu-build](https://github.com/huiliyi37/dsh-tianshu-build) ⭐36 — DeepSeek X Tianshu  Harness build 是一款完全体开源 coding agent:在 dsh harness 基础之上带视觉、跨会话记忆、验证门、agent 路由、语义 + 图谱代码检索、文件回滚和全屏终端 UI——全部以插件组合。  它是 DeepSeek Harness(dsh)的友好 MIT fork, 它保留了上游一切皆插件的架构，并将以harness最佳形态和架构往下演进。 (✅ active)
- [dsh-interconnect](https://github.com/Chinesezjc/dsh-interconnect) ⭐34 — Cross-instance message/event handoff plugins (interconnect service + tools). (✅ active)
- [dsh-plugin-cc](https://github.com/cpj-dev/dsh-plugin-cc) ⭐29 — Bridge DeepSeek Harness into Claude Code for review, critique, delegation and session import. (✅ active)
- [kixparadigm](https://github.com/olicesx/kixparadigm) ⭐23 — kixparadigm — AI self-orchestrated minimal paradigm (resident cognition layer) + kixpower multi-agent orchestration · one-command import into DeepSeek Harness (npm i -g) / AI 自编排最小范式（认知层常驻）× kixpower 多智能体编排 · npm 一键导入 DeepSeek Harness (✅ active)
- [dsh-plugin-product-subagents](https://github.com/shaokeyibb/dsh-plugin-product-subagents) ⭐17 — Role-based Codex/Claude Code/ACP subagent providers: continuable children with durable state. (✅ active)
- [dsh-advisor](https://github.com/omdsh-dev/dsh-advisor) ⭐15 — Pair a second model that passively reviews each turn and injects notes. (✅ active)
- [dsh-llm-fallbacks](https://github.com/omdsh-dev/dsh-llm-fallbacks) ⭐13 — Role-based LLM retry and fallback strategy plugin. (✅ active)
- [dsh-plugin-yet-another-subagent](https://github.com/HuanLinOTO/dsh-plugin-yet-another-subagent) ⭐12 — Configurable subagent profile system: a single subagent tool with profile parameters, Web UI settings and live progress. (✅ active)
- [dsh-sidechain](https://github.com/omdsh-dev/dsh-sidechain) ⭐10 — Side sessions: persistent /side sessions (Codex style) and one-off /btw questions (Claude style) in temporary forks. (✅ active)
- [dsh-plugin-claude-bridge](https://github.com/YYTbit/dsh-plugin-claude-bridge) ⭐9 — Bridge Claude Code memory, skills and config into DeepSeek Harness. (✅ active)
- [Task Passport](https://github.com/dongsheng123132/task-passport) ⭐9 — Open task handoff protocol for DeepSeek Harness, WorkBuddy, Claude Code and Codex: verified state, not chat logs. (✅ active)
- [dsh-a2a](https://github.com/dpskh/dsh-a2a) ⭐6 — Agent2Agent mesh for the Harness. (✅ active)
- [dsh-agent-messaging](https://github.com/happyren/dsh-agent-messaging) ⭐5 — Cross-session agent-to-agent messaging: address another session by name. (✅ active)
- [dsh-crosstalk](https://github.com/Jesse-njx/dsh-crosstalk) ⭐2 — Cross-session messaging: DSH sessions on the same machine can discover, message and coordinate with each other. (✅ active)
- [dsh-slice-agent-loop](https://github.com/TT-Wang/dsh-slice-agent-loop) ⭐2 — Drop-in agent loop whose context engine is a bounded slice instead of a growing transcript. (✅ active)
- [dsh-subagent-tools](https://github.com/lynx-gt/dsh-subagent-tools) ⭐2 — Per-call model/provider/persona/toolFilter overrides for subagent delegation with @preset references. (✅ active)
- [dsh-cross-session](https://github.com/Wha1eChai/dsh-cross-session) ⭐1 — Same-runtime cross-session discovery and communication for DeepSeek Harness. (✅ active)
- [dsh-supervisor](https://github.com/Wha1eChai/dsh-supervisor) ⭐1 — Same-runtime cross-session discovery and communication for DeepSeek Harness. (✅ active)

### Clients (Desktop & TUI)


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [open-design](https://github.com/nexu-io/open-design) | ⭐90,033 | 🎨 The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode / Hermes & 20+ CLIs via BYOK. | ✅ active |
| 2 | [deepseek-harness-desktop (Anywhere Labs)](https://github.com/anywhere-labs/deepseek-harness-desktop) | ⭐17,280 | Modern desktop experience built for the DeepSeek Harness ecosystem (plugin). | ✅ active |
| 3 | [desktop-cc-gui](https://github.com/zhukunpenglinyutong/desktop-cc-gui) | ⭐4,058 | Multi-engine AI coding desktop client (Tauri). Claude Code, Codex, Gemini, OpenCode, DeepSeek Harness and more in one GUI. | ✅ active |
| 4 | [echobird](https://github.com/edison7009/EchoBird) | ⭐3,105 | One-click install + model switch:Claude Code,Codex CLI (OpenAI), Grok Build (xAI), DeepSeek Harness, Kimi Code (Moonshot) ,Qwen Code,Aider,OpenCode,MiMo Code (Xiaomi),ZCode (Z.AI),OpenClaw,Pi,OpenScience,Vibe-Trading,Claude Desktop (3P profile),ChatGPT desktop,OpenCode Desktop, | ✅ active |
| 5 | [dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) | ⭐2,249 | Claude Code-style full-screen terminal plugin: pixel-whale top bar, live status line, streaming thoughts, double-Esc rollback, context progress bar and TPS meter. | ✅ active |
| 6 | [dsh-desktop (DataElement)](https://github.com/dataelement/dsh-desktop) | ⭐1,511 | Desktop app for DeepSeek Harness. | ✅ active |
| 7 | [deepseek-harness-eac](https://github.com/zouyuxuan122/Deepseek-Harness-EAC) | ⭐1,067 | DeepSeek Harness (dsh) Windows desktop client - bundled Node.js + dsh CLI, one-click launch, 10 built-in UI skins. EAC: Embracing All Creation 揽尽万象 | ✅ active |
| 8 | [deepseek-harness-desktop (hairyf)](https://github.com/hairyf/deepseek-harness-desktop) | ⭐814 | One-click desktop app: fully local with self-healing core updates, zero environment setup. Windows/macOS/Linux. | ✅ active |
| 9 | [deepseek-harness-desktop-app](https://github.com/vibeinging/deepseek-harness-desktop-app) | ⭐610 | DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts. | ✅ active |
| 10 | [dsh-work](https://github.com/vibeinging/dsh-work) | ⭐610 | Local-first AI workbench for DSH Plugins, combining Agent sessions, project files, data analysis, web research, MCP, and Office artifacts in an Electron desktop app. | ✅ active |

#### Complete list (71)

- [open-design](https://github.com/nexu-io/open-design) ⭐90,033 — 🎨 The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode / Hermes & 20+ CLIs via BYOK. (✅ active)
- [deepseek-harness-desktop (Anywhere Labs)](https://github.com/anywhere-labs/deepseek-harness-desktop) ⭐17,280 — Modern desktop experience built for the DeepSeek Harness ecosystem (plugin). (✅ active)
- [desktop-cc-gui](https://github.com/zhukunpenglinyutong/desktop-cc-gui) ⭐4,058 — Multi-engine AI coding desktop client (Tauri). Claude Code, Codex, Gemini, OpenCode, DeepSeek Harness and more in one GUI. (✅ active)
- [echobird](https://github.com/edison7009/EchoBird) ⭐3,105 — One-click install + model switch:Claude Code,Codex CLI (OpenAI), Grok Build (xAI), DeepSeek Harness, Kimi Code (Moonshot) ,Qwen Code,Aider,OpenCode,MiMo Code (Xiaomi),ZCode (Z.AI),OpenClaw,Pi,OpenScience,Vibe-Trading,Claude Desktop (3P profile),ChatGPT desktop,OpenCode Desktop, (✅ active)
- [dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) ⭐2,249 — Claude Code-style full-screen terminal plugin: pixel-whale top bar, live status line, streaming thoughts, double-Esc rollback, context progress bar and TPS meter. (✅ active)
- [dsh-desktop (DataElement)](https://github.com/dataelement/dsh-desktop) ⭐1,511 — Desktop app for DeepSeek Harness. (✅ active)
- [deepseek-harness-eac](https://github.com/zouyuxuan122/Deepseek-Harness-EAC) ⭐1,067 — DeepSeek Harness (dsh) Windows desktop client - bundled Node.js + dsh CLI, one-click launch, 10 built-in UI skins. EAC: Embracing All Creation 揽尽万象 (✅ active)
- [deepseek-harness-desktop (hairyf)](https://github.com/hairyf/deepseek-harness-desktop) ⭐814 — One-click desktop app: fully local with self-healing core updates, zero environment setup. Windows/macOS/Linux. (✅ active)
- [deepseek-harness-desktop-app](https://github.com/vibeinging/deepseek-harness-desktop-app) ⭐610 — DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts. (✅ active)
- [dsh-work](https://github.com/vibeinging/dsh-work) ⭐610 — Local-first AI workbench for DSH Plugins, combining Agent sessions, project files, data analysis, web research, MCP, and Office artifacts in an Electron desktop app. (✅ active)
- [dsh_desktop](https://github.com/myYangyunfan/dsh_desktop) ⭐521 — DeepSeek Harness (dsh) Windows desktop client - bundled Node.js + dsh CLI, one-click launch (✅ active)
- [deepseek-harness-studio](https://github.com/fufankeji/deepseek-harness-studio) ⭐426 — DeepSeek Harness 零代码桌面端｜一键启动，支持 Windows 与 macOS；内置插件发现、热点插件推送、一键安装与管理、AI 智能推荐和视觉增强。 (✅ active)
- [ai-novel-writer](https://github.com/EthanYoQ/AI-Novel-Writer) ⭐422 — 本地优先 AI 小说创作工作台，提供 Windows/macOS 桌面版与 DeepSeek Harness 插件开发预览，支持角色、大纲、章节蓝图、审稿修稿和本地模型。 (✅ active)
- [oh-dsh](https://github.com/hust-open-atom-club/oh-dsh) ⭐256 — One-stop community distribution: TUI, desktop and Web UI in a unified experience with layered installation. (✅ active)
- [dsh-tianshu-tui](https://github.com/huiliyi37/dsh-tianshu-tui) ⭐226 — Interactive terminal UI plugin for DSH with added TDD, evidence gates and vision modules. (✅ active)
- [dsh-launcher](https://github.com/Ruler4396/dsh-launcher) ⭐165 — Lightweight Windows launcher: silent autostart at logon plus a minimal WebView2 window. (✅ active)
- [deepseek-harness-desktop (ningbainb)](https://github.com/ningbainb/deepseek-harness-desktop) ⭐157 — Lossless Windows desktop app with the complete DSH Web UI, plugins, skins and skill dock. (✅ active)
- [deepseek-harness-desktop (steven-kid)](https://github.com/steven-kid/deepseek-harness-desktop) ⭐157 — Minimal cross-platform desktop wrapper: no config, out of the box. (✅ active)
- [deepseek-harness-desktop (salathleizhang)](https://github.com/salathleizhang/deepseek-harness-desktop) ⭐138 — Desktop wrapper for DeepSeek Harness. (✅ active)
- [Deepseek-Harness-Desktop (ChisaAlter)](https://github.com/ChisaAlter/Deepseek-Harness-Desktop) ⭐131 — Electron desktop shell with theme and background-image customization. (✅ active)
- [dshcode](https://github.com/whitelonng/dshcode) ⭐126 — Community desktop companion for DeepSeek Harness — one-click Electron app for macOS and Windows (✅ active)
- [dsh-launcher](https://github.com/MarcoG-h/DSH-Launcher) ⭐125 — 最全面的DeepSeek Harness🐋桌面启动器&第三方插件管理   | 离线部署 | 一键启动 | 插件管理 | API切换 | (✅ active)
- [dsh-mobile](https://github.com/saya-ch/dsh-mobile) ⭐79 — DeepSeek Harness 移动端适配与安全局域网访问插件，支持 Android App 和手机浏览器。 (✅ active)
- [DeepSeekHarnessDesktop (wess09)](https://github.com/wess09/DeepSeekHarnessDesktop) ⭐66 — Desktop packaging for DeepSeek Harness. (✅ active)
- [dsh-desktop (bruc3van)](https://github.com/bruc3van/dsh-desktop) ⭐66 — Third-party desktop client loading the official Web UI: reuses a running official instance or a bundled dsh runtime. (✅ active)
- [dsh-multica-runtime](https://github.com/multica-ai/dsh-multica-runtime) ⭐53 — Support the dsh runtime on Multica. (✅ active)
- [beauticode](https://github.com/starsstreaming/beautiCode) ⭐51 — 面向 AI 编程客户端的动态、可响应环境——视频背景、氛围场景与主题，适用于 DeepSeek Harness 与 Codex Desktop。 (✅ active)
- [deepseek-harness-desktop (xiincs)](https://github.com/xiincs/deepseek-harness-desktop) ⭐49 — Native desktop built on Tauri 2 with bundled Node.js runtime, tray residency and auto-update. (✅ active)
- [DeepSeek Harness TUI (openma-ai)](https://github.com/openma-ai/deepseek-harness-tui) ⭐46 — Rust/Ratatui terminal client speaking the DSH SDK JSON-RPC protocol directly; runs standalone or as a profile bundle. (✅ active)
- [dsh-plugin-dev-skills](https://github.com/zimodzh/dsh-plugin-dev-skills) ⭐38 — An Agent Skills skill for developing DeepSeek Harness (DSH) plugins（开发 DSH 插件的 Agent Skill）——插件/服务/事件/工具/LLM 适配器/打包安装的标准。Works with Claude Code, Codex, DSH, VS Code Copilot & any compatible agent. (✅ active)
- [deepseek-harness-desktop (hongfeiyucode)](https://github.com/hongfeiyucode/deepseek-harness-desktop) ⭐37 — Desktop wrapper for DeepSeek Harness. (✅ active)
- [deepseek-harness-termux](https://github.com/Vengisk/deepseek-harness-termux) ⭐37 — Run @deepseek-ai/dsh on Android/Termux. (✅ active)
- [dsh-usage-plugin](https://github.com/feiyang-dev/dsh-usage-plugin) ⭐33 — DeepSeek Harness 用量与消耗插件（dsh-usage）—— 每次调用的 token 用量/缓存命中统计、峰谷计费、余额查询、CSV/JSON/PNG 导出，可经桌面端一键安装或命令行 dsh plugin add 安装。 (✅ active)
- [deepseek-harness-app (ipfred)](https://github.com/ipfred/deepseek-harness-app) ⭐29 — Desktop app for DeepSeek Harness. (✅ active)
- [dsh-plugin-session-delete](https://github.com/lsz-asd/dsh-plugin-session-delete) ⭐26 — Delete DeepSeek Harness sessions from the UI: header danger button + sidebar session-row menu item (no conversation jump), risk-consent dialog with session name/id, stops running agents first, in-place list refresh without page reload. Works in web and the desktop client. (✅ active)
- [dsh-tui](https://github.com/dsh-tui/dsh-tui) ⭐24 — Claude Code-style terminal UI for DeepSeek Harness agents, as an out-of-tree dsh plugin bundle (✅ active)
- [dsh-mobile](https://github.com/lehhair/dsh-mobile) ⭐21 — Mobile client plugin (cordis + dsh.plugin.json). (✅ active)
- [deepseek-harness-desktop (cc1252)](https://github.com/cc1252/deepseek-harness-desktop) ⭐19 — Unofficial open-source Windows Electron wrapper for DeepSeek Harness. (✅ active)
- [DeepSeek-Harness-Desktop (sleep2agi)](https://github.com/sleep2agi/DeepSeek-Harness-Desktop) ⭐19 — Unofficial community desktop shell for the public dsh runtime. (✅ active)
- [deepseek-harness-fnos](https://github.com/techysy/deepseek-harness-fnos) ⭐18 — DeepSeek Harness (DeepSeek 官方 agent 浏览器 UI) fnOS 应用 — 本地常驻服务, 官方统一网关接入 (✅ active)
- [dsh-melody-launcher](https://github.com/rirko/dsh-melody-launcher) ⭐16 — dsh-旋律启动器：DeepSeek Harness 桌面启动器与插件管理器 (✅ active)
- [dshcockpit](https://github.com/Lxiayu/DshCockpit) ⭐16 — DshCockpit — DeepSeek Harness 桌面驾驶舱 (desktop cockpit)：运行时自动更新、成本控制、全局快捷问询、定时任务、会话全文检索、数据安全。自动更新 / 成本中心 / Quick Ask / 定时任务 / 会话搜索 (✅ active)
- [dsh-mobile-for-android](https://github.com/Hongtwenfive1226/DSH-Mobile-for-Android) ⭐12 — The Android mobile version of DeepSeek Harness that relies on Tailscale. (✅ active)
- [dsh-grok-tui](https://github.com/chen-001/dsh-grok-tui) ⭐11 — TUI built with grok-build. (✅ active)
- [awesome-deepseek-harness-desktop (ADHD)](https://github.com/omdsh-dev/awesome-deepseek-harness-desktop) ⭐10 — ADHD — out-of-the-box Electron desktop wrapper for DeepSeek Harness. (✅ active)
- [deepseek-harness-desktop](https://github.com/qyqy-1109/deepseek-harness-desktop) ⭐10 — DeepSeek Harness Desktop: self-contained Windows desktop shell (Electron) that auto-starts dsh web, plus a subtle Codex-flavored theme plugin. (✅ active)
- [deepseek-harness-desktop (chyra-moon)](https://github.com/chyra-moon/deepseek-harness-desktop) ⭐10 — Native Windows desktop shell: 1:1 official web UI with embedded server, tray and auto-recovery. (✅ active)
- [deepseek-harness-tui (boxeryao)](https://github.com/boxeryao/deepseek-harness-tui) ⭐10 — Lightweight fast terminal plugin connected directly to the DSH runtime. (✅ active)
- [dsh-desktop](https://github.com/foolgry/dsh-desktop) ⭐10 — Download-and-run desktop build of DeepSeek Harness — Electron shell with embedded Node, no npm required. (✅ active)
- [agentpocket](https://github.com/npu-chenlin/AgentPocket) ⭐9 — Android 客户端：通过 Tailscale 在手机上使用 Kimi Code / DeepSeek Harness 等编码 Agent 的 Web 服务 (✅ active)
- [deepseek-harness-desktop](https://github.com/baiyuscc13724-max/deepseek-harness-desktop) ⭐9 — Windows desktop app for DeepSeek Harness: installer, themes, in-app plugin marketplace, model routing, and updates. (✅ active)
- [deepseek-harness-desktop](https://github.com/omdsh-dev/deepseek-harness-desktop) ⭐8 — DSH 桌面应用打包器 (✅ active)
- [deepseek-harness-desktop](https://github.com/RZX00/deepseek-harness-desktop) ⭐7 — DeepSeek Harness with a Windows desktop build: an Electron shell over the dsh web profile, packaged as an installer (✅ active)
- [deepseek-harness-tui (gxinxing)](https://github.com/gxinxing/deepseek-harness-tui) ⭐7 — Terminal-native interactive TUI built with Ink (React for terminals). (✅ active)
- [star-deepseek-harness-desktop](https://github.com/dabaicai001/star-deepseek-harness-desktop) ⭐7 — Star-deepseek-harness-desktop — DeepSeek Harness,一站式桌面运维台。Harness 自动规划并调用数据库 / SSH / SFTP / Docker 执行。本地优先、跨平台。本项目由自研的starhub 做的再次改进，现在改进中... 尽情期待吧，如果想使用老版本可以下载 0.6X.X 版本 (✅ active)
- [deepseek-harness-cli](https://github.com/Richard-Yang0130/deepseek-harness-cli) ⭐6 — Claude Code-style terminal interface for DeepSeek Harness (✅ active)
- [deepseek-harness-desktop](https://github.com/HaoyueQin/deepseek-harness-desktop) ⭐6 — A desktop shell for DeepSeek Harness — the pluggable AI agent harness from DeepSeek. Wrap the official dsh web UI into a native-feeling, always-on desktop app. / 为 DeepSeek Harness（DeepSeek 开源的可插拔 AI Agent harness）打造的桌面应用壳，把官方 dsh web 界面包装成原生质感、常驻后台的桌面应用。 (✅ active)
- [dsh-desk-pet](https://github.com/anneheartrecord/dsh-desk-pet) ⭐5 — Always-on-top DeepSeek Harness desktop pet. Default whale, four skins, four silent states. (✅ active)
- [dsh-desktop-electron](https://github.com/Void0312Aurora/dsh-desktop-electron) ⭐5 — Cross-platform Electron shell for the DSH Web GUI: tray-resident standalone window. (✅ active)
- [deepseek-harness-for-android](https://github.com/standtrain/deepseek-harness-for-android) ⭐4 — 该程序是一个独立的 Capacitor Android 应用，用于管理本机 DeepSeek Harness Ubuntu 用户空间。它提供运行时安装与重置、Ubuntu 终端、可选的 Shizuku 设备 Shell 访问、设置，以及仅限回环地址的内嵌 Harness Web 界面。 (✅ active)
- [dsh-closerai](https://github.com/sb1733831438-maker/DSH-closerAI) ⭐4 — CloserAI - a local-first, model-agnostic, permission-transparent desktop AI workbench built on DeepSeek Harness. (✅ active)
- [dsh-launcher-android](https://github.com/qawse110/dsh-launcher-android) ⭐4 — DshLauncher: single-APK Android launcher for DeepSeek Harness with embedded Node runtime (✅ active)
- [deepseek-harness-desktop](https://github.com/Easyhoov/deepseek-harness-desktop-windows) ⭐3 — Unofficial in-process desktop app for DeepSeek Harness: the host composition boots inside the Electron main process with zero ports and an IPC bridge. Not affiliated with DeepSeek. (✅ active)
- [deepseek-harness-workbench](https://github.com/xuan-ao-1/deepseek-harness-workbench) ⭐3 — DeepSeek Harness 官方架构的 Windows 桌面发行版 (Desktop distribution of the official DeepSeek Harness) (✅ active)
- [dsh-vault](https://github.com/feiyang-dev/dsh-vault) ⭐3 — DeepSeek Harness 数据保险箱插件（dsh-vault）—— 自动备份、清空检测、一键恢复，保护聊天记录与工作区数据；可经桌面端一键安装或命令行 dsh plugin add 安装。 (✅ active)
- [dsh-pi-tui](https://github.com/lqhl/dsh-pi-tui) ⭐2 — Pi TUI front end: streaming markdown, thinking collapse, tool cards, slash commands and approval overlays. (✅ active)
- [dsh-portable-launcher](https://github.com/15828148/dsh-portable-launcher) ⭐2 — One-click portable launcher for DeepSeek Harness (dsh) Web UI on Windows. Auto-installs Node.js and dsh with China mirror fallback, 3-stage progress with retries and resume, zero-download fast path when ready. No admin needed. (✅ active)
- [dsh-desktop](https://github.com/xiaowei2025cqu23phy/dsh-desktop) ⭐1 — Desktop client for DeepSeek Harness: AI screensaver, phone PWA remote control (LAN pairing), QQ/Telegram bot channels with approval/question buttons, mode prompts (assistant/friend), wallpapers and more. (✅ active)
- [dsh-desktop-launcher](https://github.com/becomeless/dsh-desktop-launcher)  — Windows/macOS desktop launcher for DeepSeek Harness: double-click to launch, zero console windows, auto-stop on close | 双击图标一键启动 DeepSeek Harness 的桌面启动器（Windows / macOS） (✅ active)
- [dsh-quickstart](https://github.com/qzhqzh/dsh-quickstart)  — Desktop launcher for DeepSeek Harness - start dsh web with no console window and auto-open the browser. Tested on Windows; macOS/Linux in progress. (✅ active)
- [dsh-start](https://github.com/zhengjy01/dsh-start)  — One-click start/stop launcher for the DSH Web GUI on macOS: foreground/daemon start, stop, status, duplicate-launch guard, auto browser open, plus a Dock-able DSH.app built by script. (✅ active)

### MCP & Integrations


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [Coding Tools MCP](https://github.com/xyTom/coding-tools-mcp) | ⭐846 | Coding-oriented MCP tool collection that appears in the emerging DSH ecosystem: give any AI agent the ability to code. | ✅ active |
| 2 | [memtrace-public](https://github.com/syncable-dev/memtrace-public) | ⭐459 | Structural memory for AI coding agents. Bi-temporal graph, MCP-native, zero LLM calls. Cursor · Claude Code · Codex · DeepSeek Harness · Hermes · VS Code · Windsurf. | ✅ active |
| 3 | [dsh-openpencil](https://github.com/ZSeven-W/dsh-openpencil) | ⭐135 | OpenPencil design preview and editing integration. | ✅ active |
| 4 | [dsh-super-injector](https://github.com/yjh051108/dsh-super-injector) | ⭐133 | Super-injector plugin (cordis) for context injection. | ✅ active |
| 5 | [dsh-qqbot](https://github.com/tencent-connect/dsh-qqbot) | ⭐70 | 让 QQ 机器人接入 DeepSeek Harness（dsh）的官方插件 | ✅ active |
| 6 | [dsh-lark](https://github.com/omdsh-dev/dsh-lark) | ⭐41 | Lark/Feishu IM bot channel for DeepSeek Harness | 飞书 DeepSeek Harness 插件 | ✅ active |
| 7 | [deepseek-harness-docker](https://github.com/runzhliu/deepseek-harness-docker) | ⭐27 | Community Docker and Kubernetes packaging for @deepseek-ai/dsh with a hardened image. | ✅ active |
| 8 | [dsh-mcp-panel](https://github.com/PerryLink/dsh-mcp-panel) | ⭐26 | Read-only runtime management panel for the official DSH MCP client: /mcp command and a Settings tab. | ✅ active |
| 9 | [deepseek-harness-vsc-extension](https://github.com/weinibuliu/deepseek-harness-vsc-extension) | ⭐24 | DeepSeek Harness for VS Code as extension | 💤 inactive |
| 10 | [dsh-ide](https://github.com/chenw2759-wq/dsh-IDE) | ⭐24 | dsh-IDE 把 DeepSeek Harness（DSH）网页版升级成一站式 IDE：JupyterLab 式文件树、带语法高亮的代码编辑、多格式预览、Trae 风格红绿 diff 和内置终端，再加上「本地大脑、远程手脚」的 SSH 远程工作区，让 AI 直接在本机操控远程服务器，全程零配置文件改动。 | ✅ active |

#### Complete list (50)

- [Coding Tools MCP](https://github.com/xyTom/coding-tools-mcp) ⭐846 — Coding-oriented MCP tool collection that appears in the emerging DSH ecosystem: give any AI agent the ability to code. (✅ active)
- [memtrace-public](https://github.com/syncable-dev/memtrace-public) ⭐459 — Structural memory for AI coding agents. Bi-temporal graph, MCP-native, zero LLM calls. Cursor · Claude Code · Codex · DeepSeek Harness · Hermes · VS Code · Windsurf. (✅ active)
- [dsh-openpencil](https://github.com/ZSeven-W/dsh-openpencil) ⭐135 — OpenPencil design preview and editing integration. (✅ active)
- [dsh-super-injector](https://github.com/yjh051108/dsh-super-injector) ⭐133 — Super-injector plugin (cordis) for context injection. (✅ active)
- [dsh-qqbot](https://github.com/tencent-connect/dsh-qqbot) ⭐70 — 让 QQ 机器人接入 DeepSeek Harness（dsh）的官方插件 (✅ active)
- [dsh-lark](https://github.com/omdsh-dev/dsh-lark) ⭐41 — Lark/Feishu IM bot channel for DeepSeek Harness | 飞书 DeepSeek Harness 插件 (✅ active)
- [deepseek-harness-docker](https://github.com/runzhliu/deepseek-harness-docker) ⭐27 — Community Docker and Kubernetes packaging for @deepseek-ai/dsh with a hardened image. (✅ active)
- [dsh-mcp-panel](https://github.com/PerryLink/dsh-mcp-panel) ⭐26 — Read-only runtime management panel for the official DSH MCP client: /mcp command and a Settings tab. (✅ active)
- [deepseek-harness-vsc-extension](https://github.com/weinibuliu/deepseek-harness-vsc-extension) ⭐24 — DeepSeek Harness for VS Code as extension (💤 inactive)
- [dsh-ide](https://github.com/chenw2759-wq/dsh-IDE) ⭐24 — dsh-IDE 把 DeepSeek Harness（DSH）网页版升级成一站式 IDE：JupyterLab 式文件树、带语法高亮的代码编辑、多格式预览、Trae 风格红绿 diff 和内置终端，再加上「本地大脑、远程手脚」的 SSH 远程工作区，让 AI 直接在本机操控远程服务器，全程零配置文件改动。 (✅ active)
- [chatccc](https://github.com/wzj998/ChatCCC) ⭐22 — 飞书（Lark）或微信（WeChat）聊天控制 DeepSeek Harness / Claude Code / Cursor / Codex / CCC Agent (✅ active)
- [dsh-vscode](https://github.com/Lixxx1/dsh-vscode) ⭐14 — DSH Sidebar — a Claude Code/Codex-style VS Code sidebar for DeepSeek Harness. 像 Claude Code、Codex 一样，在 VS Code 侧边栏中使用 DSH。 (✅ active)
- [deepseek-harness-action](https://github.com/Lixiaoyiao/deepseek-harness-action) ⭐13 — Community GitHub Action: AI code review, CI diagnosis, auto-fix and issue-to-PR implementation. (✅ active)
- [dsh-git-graph](https://github.com/1841220388zzzcccxxx-star/dsh-git-graph) ⭐13 — Embedded git repository graph visualizer for the DeepSeek Harness Web GUI | 嵌入式 Git 仓库图谱可视化插件（提交历史图 / 分支过滤 / 文件 diff / VSCode 式未提交改动） (✅ active)
- [deepseek-harness-acp](https://github.com/openma-ai/deepseek-harness-acp) ⭐12 — ACP server implementation for DeepSeek Harness: exposes the full DSH agent to ACP clients while reusing credentials and sessions. (✅ active)
- [dsh-search-mcp](https://github.com/gxpppp/dsh-search-mcp) ⭐12 — Replace DSH's built-in web search with search MCP servers (Tavily/Brave/Exa/Perplexity/DuckDuckGo). (✅ active)
- [dsh-vision-proxy](https://github.com/Flyvhidbwo/dsh-vision-proxy) ⭐12 — DeepSeek Harness 插件：DeepSeek 大脑 + 自动识图。GUI 附加图片自动经 OpenAI 兼容 VLM 转译成文字后交给 DeepSeek 作答；支持百炼/智谱/OpenRouter 等任意 OpenAI 兼容端点（默认 qwen3.7-flash），无 key 自动探测本地 Ollama（图片不出本机）；安装时有一问式确认 (✅ active)
- [ikanban](https://github.com/isomoes/ikanban) ⭐12 — Monorepo for the iKanban browser-surface fork for DeepSeek Harness. (✅ active)
- [dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) ⭐10 — MCP server manager: Settings page with OAuth (PKCE + dynamic client registration) or static-token auth. (✅ active)
- [deepseek-acp](https://github.com/xintaofei/deepseek-acp) ⭐9 — 把 DeepSeek Harness 接成一个面向编辑器的完整编码 Agent， 通过 Agent Client Protocol（ACP）与客户端通话。 (✅ active)
- [dsh-harness-mcp-server](https://github.com/chushixixin/dsh-harness-mcp-server) ⭐9 — Expose DeepSeek Harness agent capabilities as an MCP server (brain=Hermes, arms=Harness). (✅ active)
- [dsh-lan-access](https://github.com/Leon0555/dsh-lan-access) ⭐9 — LAN access for the Web GUI: 0.0.0.0 bind plus a crypto.randomUUID polyfill for non-secure contexts. (✅ active)
- [dsh-oauth-mcp-client](https://github.com/springbrand-lab/dsh-oauth-mcp-client) ⭐9 — OAuth 2.1 Streamable HTTP MCP client plugin for DeepSeek Harness. (✅ active)
- [dsh-browser](https://github.com/xylt369/dsh-browser) ⭐8 — Browser capability for DeepSeek Harness: headed Edge/Playwright provider, SSRF-safe navigation, a11y-ref clicking, permission gate with auto-remember, gated evaluate (✅ active)
- [dsh-telegram-channel](https://github.com/hi-wenw/dsh-telegram-channel) ⭐8 — Telegram mobile remote for live DSH Web sessions: session picker, bind/unbind, same trajectory as desktop. (✅ active)
- [telegram](https://github.com/LoserFox/telegram) ⭐7 — Telegram Bot API 桥接插件：长轮询、per-chat 会话、HTML 格式化 (✅ active)
- [DSH Telegram Relay](https://github.com/congchuanling-dot/DSH-Telegram-Relay) ⭐6 — Relay that turns Telegram into a remote conversation channel for DSH with notifications. (✅ active)
- [dsh-agentlink](https://github.com/hootandy321/dsh-Agentlink) ⭐6 — Caller-side bridge from Codex and other agent frameworks to DeepSeek Harness, with observable sessions, follow-up, cancellation, and human-gated approvals. (✅ active)
- [dsh-subscription-auth](https://github.com/Khellendros97/dsh-subscription-auth) ⭐5 — dsh对接openai、grok、anthropic、kimi订阅渠道 (✅ active)
- [dsh4vscode](https://github.com/DoggyHU/dsh4vscode) ⭐5 — VS Code chat windows backed by the DSH agent: OpenCode-style independent sessions with model auto-routing. (✅ active)
- [dsh-slack](https://github.com/STARDUSTLC666/dsh-slack) ⭐4 — DeepSeek Harness Slack 插件：slack_notify/channels/inbox/reply 四工具，Socket Mode 免公网回调收消息，收件箱队列 + 线程回复，支持自定义 slackApiUrl 对接代理网关；内置假 Slack 服务器做协议级验收测试。· Two-way Slack messaging for DeepSeek Harness agents. (✅ active)
- [kimi-tide](https://github.com/tafcear/kimi-tide) ⭐4 — 月汐 — Kimi Code (Moonshot) 接入 DeepSeek Harness 的完整方案：标准 DSH 插件 + Kimi CLI 桥接维护 fork + Agent 协作闭环方法论 (✅ active)
- [PicGo DSH Plugin](https://github.com/PicGo/dsh-plugin) ⭐4 — Official PicGo plugin: upload images/files to your image host from DSH and get public URLs. (✅ active)
- [dsh-dingtalk](https://github.com/STARDUSTLC666/dsh-dingtalk) ⭐3 — DeepSeek Harness 钉钉群机器人通知插件：dingtalk_notify/dingtalk_text 两工具，自定义机器人 webhook + HMAC 加签安全模式，手写签名实现、零运行时依赖；纯 Node 全平台。· DingTalk group-robot notifications for DeepSeek Harness agents. (✅ active)
- [dsh-mcp-manager](https://github.com/Nichts0v0/dsh-mcp-manager) ⭐3 — 在 DeepSeek Harness 设置页管理 MCP 服务器：运行时添加/编辑/启停/重连/删除，实时状态、自动重连，中英双语界面。MCP server manager for DeepSeek Harness — add, edit, enable/disable, reconnect & delete MCP servers from the web settings page, with live status and auto-reconnect. (✅ active)
- [dsh-plugin-vision](https://github.com/tdf1995/dsh-plugin-vision) ⭐3 — Vision for text-only LLMs in DeepSeek Harness (DSH): describe images / OCR / VQA via free Gemini & GLM vision APIs (✅ active)
- [dsh-subagent-cwd](https://github.com/lynx-gt/dsh-subagent-cwd) ⭐3 — DeepSeek Harness subagent delegation enhancement (✅ active)
- [dsh-watch](https://github.com/dshworks/dsh-watch) ⭐3 — Put a watch on a stream: background listeners that wake the DeepSeek Harness agent with new matching lines — and a daemon host so a watcher runs unattended for weeks, with no task and no browser. Not affiliated with DeepSeek. (✅ active)
- [shopline-ai-toolkit-dsh](https://github.com/lunw/shopline-ai-toolkit-dsh) ⭐3 — SHOPLINE AI Toolkit for DeepSeek Harness (dsh-plugin): official SHOPLINE Developer MCP bridge + SHOPLINE agent skills, mirroring the Shopify AI Toolkit architecture. dsh-plugin (✅ active)
- [vscode-deepseek-harness](https://github.com/kalynnka/vscode-deepseek-harness) ⭐3 — Unofficial: drive your own dsh as a native VS Code chat agent. (✅ active)
- [dsh-github-integration](https://github.com/omdsh-dev/dsh-github-integration) ⭐2 — GitHub integration plugin for DSH. (✅ active)
- [dsh-meow-cat](https://github.com/dsh-pub/dsh-meow-cat) ⭐2 — A cat runs across the bottom of the DeepSeek Harness web UI with a synthesized meow every time a conversation turn ends. (✅ active)
- [dsh-plugin-acn](https://github.com/acnlabs/dsh-plugin-acn) ⭐2 — DeepSeek Harness plugin: join ACN so this agent can discover, message, and collaborate with other agents. Defaults to the China region. (✅ active)
- [deepseek-harness-rs](https://github.com/Tokimorphling/deepseek-harness-rs) ⭐1 — A Rust port of DeepSeek Harness. (🧪 experimental)
- [dsh-chrome](https://github.com/YJSoooooo/dsh-chrome) ⭐1 — Chrome profile bridge: control an existing signed-in Chrome profile through Chrome DevTools Protocol. (✅ active)
- [mcp_guard](https://github.com/dshoneys/mcp_guard) ⭐1 — 本机 MCP / Agent 口扫描、监视与审计（loopback 未鉴权 tools/list、CORS）。DeepSeek Honeys. (✅ active)
- [dsh-docker](https://github.com/dshoneys/dsh-docker)  — 隔离的 DeepSeek Harness 插件安装沙箱，并对本机 MCP 口做防御性探测。 (✅ active)
- [dsh-wechat-bridge](https://github.com/lanbaolu/dsh-wechat-bridge)  — Personal WeChat bridge for DeepSeek Harness: scan QR to bind, then chat with your local DSH agent directly inside WeChat (text/image/voice/file, streamed replies, persisted sessions). (✅ active)
- [opendsh](https://github.com/TheChengXi/opendsh)  — Open the DeepSeek Harness Web UI inside VS Code with one-command start/stop. (✅ active)
- [URL Manager MCP](https://github.com/Piccolo123/url-manager-mcp)  — MCP companion for URL Manager: 21 tools for save/search/categorize/share with magic-link delivery. (✅ active)

### Examples & Starters


#### 🔥 Top 9

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [hello-dsh](https://github.com/pingfanfan/hello-dsh) | ⭐79 | Zero-to-plugin tutorial: understand 'everything is a plugin' with 22 Chinese skill examples. | ✅ active |
| 2 | [dsh-plugin-template](https://github.com/bugmaker2/dsh-plugin-template) | ⭐13 | Template for DeepSeek Harness plugin development. | ✅ active |
| 3 | [plugin-template (omdsh-dev)](https://github.com/omdsh-dev/plugin-template) | ⭐12 | Plugin template repository derived from the original turtle-ui official repo. | ✅ active |
| 4 | [turtle-ui](https://github.com/turtle1999/turtle-ui) | ⭐8 | Official UI plugin reference implementation. | ✅ active |
| 5 | [dsh-plugin-template (sunshine-lang)](https://github.com/sunshine-lang/dsh-plugin-template) | ⭐6 | Ready-to-publish plugin skeleton: bundle format, tool DSL, config and tests. | ✅ active |
| 6 | [dsh-101](https://github.com/bill9109/dsh-101) | ⭐5 | DSH documentation reading mode. | ✅ active |
| 7 | [InfiniteDSH](https://github.com/vdnight89/InfiniteDSH) | ⭐3 | 诸天万界DSH: one DSH session is one book — a cover-card picker opens 19 realms, a prose-only preset locks the model to fiction, keyword worldbook lore grounds each turn, and /export-story typesets the session into a Markdown novel. | ✅ active |
| 8 | [Living-Dream-DSH](https://github.com/alllllllllli/Living-Dream-DSH) | ⭐2 | Complete DSH desktop config framework: 8+ MCP servers, free model channels (CNB proxy, AMD Radeon Cloud), mobile remote via Tailscale, vision patches, one-click installer. | ✅ active |
| 9 | [dsh-plugin-hello](https://github.com/xu1132/dsh-plugin-hello) |  | Hello-world style starter plugin for DSH. | ✅ active |

#### Complete list (9)

- [hello-dsh](https://github.com/pingfanfan/hello-dsh) ⭐79 — Zero-to-plugin tutorial: understand 'everything is a plugin' with 22 Chinese skill examples. (✅ active)
- [dsh-plugin-template](https://github.com/bugmaker2/dsh-plugin-template) ⭐13 — Template for DeepSeek Harness plugin development. (✅ active)
- [plugin-template (omdsh-dev)](https://github.com/omdsh-dev/plugin-template) ⭐12 — Plugin template repository derived from the original turtle-ui official repo. (✅ active)
- [turtle-ui](https://github.com/turtle1999/turtle-ui) ⭐8 — Official UI plugin reference implementation. (✅ active)
- [dsh-plugin-template (sunshine-lang)](https://github.com/sunshine-lang/dsh-plugin-template) ⭐6 — Ready-to-publish plugin skeleton: bundle format, tool DSL, config and tests. (✅ active)
- [dsh-101](https://github.com/bill9109/dsh-101) ⭐5 — DSH documentation reading mode. (✅ active)
- [InfiniteDSH](https://github.com/vdnight89/InfiniteDSH) ⭐3 — 诸天万界DSH: one DSH session is one book — a cover-card picker opens 19 realms, a prose-only preset locks the model to fiction, keyword worldbook lore grounds each turn, and /export-story typesets the session into a Markdown novel. (✅ active)
- [Living-Dream-DSH](https://github.com/alllllllllli/Living-Dream-DSH) ⭐2 — Complete DSH desktop config framework: 8+ MCP servers, free model channels (CNB proxy, AMD Radeon Cloud), mobile remote via Tailscale, vision patches, one-click installer. (✅ active)
- [dsh-plugin-hello](https://github.com/xu1132/dsh-plugin-hello)  — Hello-world style starter plugin for DSH. (✅ active)

### Tutorials & Learning


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [DeepSeek Harness Orange Book](https://github.com/alchaincyf/deepseek-harness-orange-book) | ⭐1,118 | Community Orange Book: complete system prompts, a 129-line startup checklist and three raw session logs — first-hand testing the official docs lack. Free PDF/EPUB/HTML. | ✅ active |
| 2 | [dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) | ⭐604 | From 0 to 1 handbook: installation, plugin development, performance tuning, real-world cases and same-model multi-agent comparisons (CN + EN PDF). | ✅ active |
| 3 | [dshfind](https://github.com/hikariming/dshfind) | ⭐200 | Learn DSH principles, plugin marketplace and best practices — from chapter-by-chapter Cordis paper reading to an auto-aggregated plugin market. | ✅ active |
| 4 | [deepseek-harness-tutorial](https://github.com/ht426/deepseek-harness-tutorial) | ⭐182 | Detailed Chinese learning tutorial for DeepSeek Harness. | ✅ active |
| 5 | [dsh-harness-tutorial](https://github.com/yanhua1010/dsh-harness-tutorial) | ⭐54 | DeepSeek Harness Agent 的原理与实现：从零到一实现一个 AI Agent —— 一切皆插件的中文教程（VitePress 站点 + 8 个 Demo + mini-harness 教学项目） | ✅ active |
| 6 | [deepseek-harness-handbook](https://github.com/sandbaseai/deepseek-harness-handbook) | ⭐36 | Independent, source-backed handbook for DeepSeek AI's official DeepSeek Harness (dsh): agents, plugins, security, troubleshooting, and runbooks. | ✅ active |
| 7 | [dsh-explain](https://github.com/yuezengwu/dsh-explain) | ⭐11 | Local-first learning mode: cross-session global learning threads, explain-by-source, ExplainContext and compression. | ✅ active |
| 8 | [deepseek-harness-learning](https://github.com/Lucky2024-pllove/deepseek-harness-learning) | ⭐7 | Learning website built from a systematic breakdown of the deepseek-harness repository, for developers curious how AI agent frameworks work. | ✅ active |
| 9 | [deepseek-harness-prompts](https://github.com/demouo/deepseek-harness-prompts) | ⭐6 | DeepSeek Harness prompts for different modes. | ✅ active |
| 10 | [dsh-book-deepseek-harness](https://github.com/LaplaceYoung/dsh-book-deepseek-harness) | ⭐6 | 'Deep Dive into DeepSeek Harness' — source-level architecture book: 37 chapter files, PDF, Mermaid diagrams and writing conventions. | ✅ active |

#### Complete list (13)

- [DeepSeek Harness Orange Book](https://github.com/alchaincyf/deepseek-harness-orange-book) ⭐1,118 — Community Orange Book: complete system prompts, a 129-line startup checklist and three raw session logs — first-hand testing the official docs lack. Free PDF/EPUB/HTML. (✅ active)
- [dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) ⭐604 — From 0 to 1 handbook: installation, plugin development, performance tuning, real-world cases and same-model multi-agent comparisons (CN + EN PDF). (✅ active)
- [dshfind](https://github.com/hikariming/dshfind) ⭐200 — Learn DSH principles, plugin marketplace and best practices — from chapter-by-chapter Cordis paper reading to an auto-aggregated plugin market. (✅ active)
- [deepseek-harness-tutorial](https://github.com/ht426/deepseek-harness-tutorial) ⭐182 — Detailed Chinese learning tutorial for DeepSeek Harness. (✅ active)
- [dsh-harness-tutorial](https://github.com/yanhua1010/dsh-harness-tutorial) ⭐54 — DeepSeek Harness Agent 的原理与实现：从零到一实现一个 AI Agent —— 一切皆插件的中文教程（VitePress 站点 + 8 个 Demo + mini-harness 教学项目） (✅ active)
- [deepseek-harness-handbook](https://github.com/sandbaseai/deepseek-harness-handbook) ⭐36 — Independent, source-backed handbook for DeepSeek AI's official DeepSeek Harness (dsh): agents, plugins, security, troubleshooting, and runbooks. (✅ active)
- [dsh-explain](https://github.com/yuezengwu/dsh-explain) ⭐11 — Local-first learning mode: cross-session global learning threads, explain-by-source, ExplainContext and compression. (✅ active)
- [deepseek-harness-learning](https://github.com/Lucky2024-pllove/deepseek-harness-learning) ⭐7 — Learning website built from a systematic breakdown of the deepseek-harness repository, for developers curious how AI agent frameworks work. (✅ active)
- [deepseek-harness-prompts](https://github.com/demouo/deepseek-harness-prompts) ⭐6 — DeepSeek Harness prompts for different modes. (✅ active)
- [dsh-book-deepseek-harness](https://github.com/LaplaceYoung/dsh-book-deepseek-harness) ⭐6 — 'Deep Dive into DeepSeek Harness' — source-level architecture book: 37 chapter files, PDF, Mermaid diagrams and writing conventions. (✅ active)
- [dsh-learn-everything](https://github.com/cendaifeng/dsh-learn-everything) ⭐5 — Feynman learning-mode plugin: teach → teach-back → judge → re-explain loop rendered as rich HTML lesson cards. (✅ active)
- [gitlearnos](https://github.com/Guojiz/gitlearnos) ⭐4 — Git-native AI learning OS with a GitLearnOS-exclusive DeepSeek Harness panel, targeted practice, local RAG, and learner-owned memory. (✅ active)
- [deepseek-protocol-doctor](https://github.com/Whning0513/deepseek-protocol-doctor) ⭐2 — Checks DeepSeek tool loops, reasoning_content, strict schemas and captured SSE; also works as a DSH plugin. (✅ active)

### Awesome Lists & Registries


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [awesome-deepseek-integration](https://github.com/deepseek-ai/awesome-deepseek-integration) | ⭐38,897 | Integrate the DeepSeek API into popular software | ✅ active |
| 2 | [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | ⭐11,012 | Large curated list of installable DSH plugins (bilingual). | ✅ active |
| 3 | [awesome-deepseek-agent (official)](https://github.com/deepseek-ai/awesome-deepseek-agent) | ⭐5,966 | Official curated guides for integrating DeepSeek models into agent/coding-assistant tools (AstrBot, Cherry Studio, Claude Code, Codex, DeepSeek-TUI, Reasonix and more). | ✅ active |
| 4 | [awesome-harness-engineering](https://github.com/walkinglabs/awesome-harness-engineering) | ⭐3,887 | 🛠️ Awesome tools & guides for harness engineering. | ✅ active |
| 5 | [awesome-dsh-plugins (Radar)](https://github.com/AdamPlatin123/awesome-dsh-plugins) | ⭐1,309 | Radar index repo: auto-scanning all discovered dsh plugin candidates with an evidence-based compatibility matrix. | ✅ active |
| 6 | [awesome-deepseek-harness](https://github.com/Anil-matcha/awesome-deepseek-harness) | ⭐966 | Curated guide to DeepSeek Harness (dsh) and its best community plugins | ✅ active |
| 7 | [awesome-dsh-plugin](https://github.com/Anil-matcha/awesome-dsh-plugin) | ⭐966 | A curated list of plugins for DeepSeek Harness (dsh) - DeepSeek Harness plugin ecosystem | ✅ active |
| 8 | [awesome-deepseek-coder](https://github.com/deepseek-ai/awesome-deepseek-coder) | ⭐811 | A curated list of open-source projects related to DeepSeek Coder | ✅ active |
| 9 | [awesome-deepseek-harness (0xsline)](https://github.com/0xsline/awesome-deepseek-harness) | ⭐788 | Curated DSH ecosystem directory: plugins, tools and infrastructure from dsh-external/hub and the public dsh-plugin topic. | ✅ active |
| 10 | [awesome-dsh-plugin (bruc3van)](https://github.com/bruc3van/awesome-dsh-plugin) | ⭐261 | Find the right DSH plugin in 30 seconds: what problem each plugin solves, who it is for and where to start. | ✅ active |

#### Complete list (71)

- [awesome-deepseek-integration](https://github.com/deepseek-ai/awesome-deepseek-integration) ⭐38,897 — Integrate the DeepSeek API into popular software (✅ active)
- [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) ⭐11,012 — Large curated list of installable DSH plugins (bilingual). (✅ active)
- [awesome-deepseek-agent (official)](https://github.com/deepseek-ai/awesome-deepseek-agent) ⭐5,966 — Official curated guides for integrating DeepSeek models into agent/coding-assistant tools (AstrBot, Cherry Studio, Claude Code, Codex, DeepSeek-TUI, Reasonix and more). (✅ active)
- [awesome-harness-engineering](https://github.com/walkinglabs/awesome-harness-engineering) ⭐3,887 — 🛠️ Awesome tools & guides for harness engineering. (✅ active)
- [awesome-dsh-plugins (Radar)](https://github.com/AdamPlatin123/awesome-dsh-plugins) ⭐1,309 — Radar index repo: auto-scanning all discovered dsh plugin candidates with an evidence-based compatibility matrix. (✅ active)
- [awesome-deepseek-harness](https://github.com/Anil-matcha/awesome-deepseek-harness) ⭐966 — Curated guide to DeepSeek Harness (dsh) and its best community plugins (✅ active)
- [awesome-dsh-plugin](https://github.com/Anil-matcha/awesome-dsh-plugin) ⭐966 — A curated list of plugins for DeepSeek Harness (dsh) - DeepSeek Harness plugin ecosystem (✅ active)
- [awesome-deepseek-coder](https://github.com/deepseek-ai/awesome-deepseek-coder) ⭐811 — A curated list of open-source projects related to DeepSeek Coder (✅ active)
- [awesome-deepseek-harness (0xsline)](https://github.com/0xsline/awesome-deepseek-harness) ⭐788 — Curated DSH ecosystem directory: plugins, tools and infrastructure from dsh-external/hub and the public dsh-plugin topic. (✅ active)
- [awesome-dsh-plugin (bruc3van)](https://github.com/bruc3van/awesome-dsh-plugin) ⭐261 — Find the right DSH plugin in 30 seconds: what problem each plugin solves, who it is for and where to start. (✅ active)
- [Awesome-DeepSeek-Harness-Plugins](https://github.com/Zhiyuan-Fan/Awesome-DeepSeek-Harness-Plugins) ⭐240 — Curated list of DeepSeek Harness plugins. (✅ active)
- [awesome-deepseek-harness (libukai)](https://github.com/libukai/awesome-deepseek-harness) ⭐175 — Ultimate guide: quick start, resources, curated plugins and practical tools. (✅ active)
- [awesome-deepseek-harness (Dominic789654)](https://github.com/Dominic789654/awesome-deepseek-harness) ⭐174 — Curated list of plugins, skills, MCP servers, patch/profile layers, orchestrators and UIs for DeepSeek Harness. (✅ active)
- [notes (zhaoolee)](https://github.com/zhaoolee/notes) ⭐149 — Open-source Smartisan Notes clone: Docker private deployment, skill invocation, dsh plugin support and one-click WeChat-format export. (✅ active)
- [awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) ⭐145 — Curated community plugin directory and live marketplace for DeepSeek Harness. (✅ active)
- [awesome-dsh-plugin](https://github.com/beancookie/awesome-dsh-plugin) ⭐93 — Awesome DeepSeek Harness (DSH) Plugin (✅ active)
- [awesome-DSH-plugin (Alex-Yanggg)](https://github.com/Alex-Yanggg/awesome-DSH-plugin) ⭐77 — Meticulously curated list of plugins, extensions, tools and development resources for DSH. (✅ active)
- [zat-dsh-engine](https://github.com/mishibeikejie/zat-dsh-engine) ⭐76 — Visual plugin marketplace for DeepSeek Harness — browse, search and install community plugins (✅ active)
- [oh-my-dsh](https://github.com/like-study1/Oh-My-DSH) ⭐68 — 🐳 DeepSeek Harness 插件聚合社区 — 自动同步 dsh-plugin 生态 · 精选目录 · 每 8 小时自动维护 | Oh-My-DSH: a community-maintained catalog of DeepSeek Harness plugins, auto-synced from the dsh-plugin topic (✅ active)
- [plugin-registry](https://github.com/vlln/plugin-registry) ⭐57 — DSH plugin ecosystem infrastructure: thin console to manage official repository plugins (0 patch) plus the make-dsh-plugin skill. (✅ active)
- [oh-my-dsh](https://github.com/LaplaceYoung/oh-my-dsh) ⭐51 — Plugin ecosystem for DSH: 700+ plugins registered only through extension seams, without modifying the agent-loop skeleton. (✅ active)
- [awesome-harness-engineering](https://github.com/jiji262/awesome-harness-engineering) ⭐49 — Awesome lists of Harness Engineering and AI Native Engineering resources. (✅ active)
- [dsh-market](https://github.com/2BingLing/dsh-market) ⭐46 — DeepSeek Harness 插件市场 · 持续收录 500+ DSH 插件：中文搜索 + 实用五维评分 + 一键安装。Web 版与 DSH 侧边栏插件双形态。Plugin marketplace for DeepSeek Harness: 500+ plugins, Chinese search, 5-dim scoring, one-click install. (✅ active)
- [dsh-suite](https://github.com/whyihaveyou/dsh-suite) ⭐43 — Living DSH plugin directory (785+ plugins, refreshed hourly) with daily compatibility CI, a bilingual catalog site and an in-app plugin store. (✅ active)
- [awesome-deepseek-harness-plugins](https://github.com/web-casa/Awesome-DeepSeek-Harness-Plugins) ⭐33 — Awesome DSH Cordis Plugins — the official, auto-generated list of DeepSeek Harness Cordis plugins, curated by cordis.run 由 cordis.run 精选维护的 DeepSeek Harness Cordis 插件官方自动生成列表。 (✅ active)
- [sandbase-skills](https://github.com/sandbaseai/sandbase-skills) ⭐31 — 88 installable open-source Agent Skills for research, social intelligence, marketing, and business workflows—compatible with Codex, Claude Code, Cursor, Gemini CLI, and DeepSeek Harness. (✅ active)
- [dsh-meme-hub](https://github.com/the-beating-light-of-the-nail/dsh-meme-hub) ⭐30 — Curated navigation of community meme plugins (skins, desktop pets, mini-games), bilingual. (✅ active)
- [dsh-plugin-marketplace](https://github.com/AwesomeHou/dsh-plugin-marketplace) ⭐27 — Plugin marketplace for DeepSeek Harness — live-syncs the GitHub dsh-plugin topic (1800+ repos) into a searchable, paginated settings tab with one-click install and agent tools (market_search / market_install). (✅ active)
- [deepseek-plugin-store](https://github.com/Ericwong5021/deepseek-plugin-store) ⭐24 — DeepSeek Harness 独立社区插件商店：发现、安装并提交经过验证的插件、工具与扩展。 | Independent community plugin directory. (✅ active)
- [awesome-dsh-plugins (kejixiaoliang)](https://github.com/kejixiaoliang/awesome-dsh-plugins) ⭐22 — Curated DSH plugin catalog: 14 categories, 280+ community plugins covering MCP/Skill/TUI/multi-agent/context memory/UI skins. (✅ active)
- [dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) ⭐20 — Verified plugin marketplace and autonomous registry for DeepSeek Harness (✅ active)
- [dsh-plugin-hub](https://github.com/cclank/dsh-plugin-hub) ⭐17 — DeepSeek Harness community plugin registry with evidence-based screening (✅ active)
- [dsh-plugin-hub](https://github.com/dshplugin/dsh-plugin-hub) ⭐16 — DeepSeek Harness 社区内置插件市场（dsh-plugin）— 搜索插件、下载并安装 4000+ 人工精选社区插件，每日更新、完全免费。内置在 Harness「设置 → 插件中心」，无需离开应用即可浏览、搜索、安装各类 AI 插件。 (✅ active)
- [deepseek-harness-awesome-top-500](https://github.com/weekend-project-space/deepseek-harness-awesome-top-500) ⭐15 — deepseek-harness plugins 、resource 、use ; dsh top 500 (✅ active)
- [awesome-deepseek-harness (jiji262)](https://github.com/jiji262/awesome-deepseek-harness) ⭐13 — Curated DeepSeek Harness resources. (✅ active)
- [awesome-dsh-plugins (white0dew)](https://github.com/white0dew/awesome-dsh-plugins) ⭐13 — Public GitHub directory for DSH plugins with install commands. (✅ active)
- [awesome-dsh-plugin (billLiao)](https://github.com/billLiao/awesome-dsh-plugin) ⭐12 — Curated list of plugins for DeepSeek Harness. (✅ active)
- [dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) ⭐12 — DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 | https://dsh-plugin-hub.hupc.site (✅ active)
- [dsh-plugin-marketplace](https://github.com/w2112515/dsh-plugin-marketplace) ⭐12 — Out-of-tree installable plugin marketplace bundle for DeepSeek Harness (✅ active)
- [awesome-deepseek-harness-plugins](https://github.com/vvlife/awesome-deepseek-harness-plugins) ⭐10 — A curated list of plugins, tools, skins, and extensions for DeepSeek Harness (DSH). (✅ active)
- [awesome-deepseek-harness-plugins](https://github.com/walkinglabs/awesome-deepseek-harness-plugins) ⭐9 — A curated, bilingual list of verified plugins, tools, design workflows, and learning resources for DeepSeek Harness (DSH). (✅ active)
- [awesome-dsh-bridges](https://github.com/YYTbit/awesome-dsh-bridges) ⭐6 — Bridge your favorite AI coding tools into DeepSeek Harness (✅ active)
- [awesome-dsh-plugins](https://github.com/cccakeee/awesome-dsh-plugins) ⭐6 — A curated, evidence-led directory of DeepSeek Harness (DSH) plugins: verified loadable extensions, skills, and permission-aware installation guidance. (✅ active)
- [dsh-plugins](https://github.com/Sakana-yuyu/dsh-plugins) ⭐6 — DeepSeek Harness (DSH) 插件目录：官方包 + 社区插件按 GitHub stars 排名，GitHub Pages 可访问。 (✅ active)
- [awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) ⭐5 — Spam-filtered, open-data registry of DeepSeek Harness (dsh) plugins, bundles, and skills. (✅ active)
- [dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) ⭐5 — DeepSeek Harness plugin market - browse, search & install dsh-plugin topic plugins (dsh 插件市场：浏览/搜索/安装插件) (✅ active)
- [dsh-plugins](https://github.com/HackSing/dsh-plugins) ⭐5 — A bilingual, continuously maintained directory of plugins for DeepSeek Harness (DSH). (✅ active)
- [awesome-dsh-skills](https://github.com/hackerFish/awesome-dsh-skills) ⭐4 — 实测可用的 DeepSeek Harness 技能库：每个 SKILL.md 都通过格式校验与加载冒烟，复制即用（中文优先） (✅ active)
- [dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) ⭐4 — DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令） (✅ active)
- [awesome-deepseek-harness](https://github.com/XiaomingX/awesome-deepseek-harness) ⭐3 — Curated DeepSeek Harness (DSH) ecosystem catalog — plugins, tools & infrastructure. Filtered, multilingual (ZH/EN/KO/JA), with design patterns worth borrowing. (✅ active)
- [awesome-dsh-plugins](https://github.com/dongsheng123132/awesome-dsh-plugins) ⭐3 — Evidence-backed DeepSeek Harness plugin radar and 2Origin plugin lab (✅ active)
- [awesome-dsh-plugins-2026](https://github.com/Herdeny/awesome-dsh-plugins-2026) ⭐3 — Curated list of DeepSeek Harness (DSH) plugins for 2026, with quality check. (✅ active)
- [awesome-dsh-themes](https://github.com/dshworks/awesome-dsh-themes) ⭐3 — Registry of DeepSeek Harness (dsh) themes and --dsw-* token skins. Not affiliated with DeepSeek. (✅ active)
- [dsh-marketplace](https://github.com/ouyangyipeng/dsh-marketplace) ⭐3 — A safe, live plugin marketplace for DeepSeek Harness (✅ active)
- [dsh-plugins](https://github.com/lwmxiaobei/dsh-plugins) ⭐3 — DeepSeek Harness 社区插件目录，自动汇总并基础校验 GitHub 插件，支持搜索、筛选、双语详情与最新版本安装命令复制。Community directory for DeepSeek Harness plugins with automated discovery, basic validation, search, filters, bilingual details, and latest version install commands. (✅ active)
- [dsh-plugins-store](https://github.com/DshMarketPlace/dsh-plugins-store) ⭐3 — Browse and install DSH plugins from inside DeepSeek Harness. /store, a settings tab, and agent tools — bilingual. (✅ active)
- [awesome-dsh-plugin](https://github.com/wgd753/awesome-dsh-plugin) ⭐2 — Awesome dsh plugin list — automated DeepSeek Harness plugin directory. Daily GitHub Actions crawl of topic:dsh-plugin / topic:deepseek-harness, bilingual README + machine-readable JSON/CSV (✅ active)
- [awesome-dsh-plugins](https://github.com/coolbat/awesome-dsh-plugins) ⭐2 — Evidence-led bilingual directory of DeepSeek Harness plugins, reviewed at immutable commits. (✅ active)
- [awesome-dsh-plugins](https://github.com/jqueryscript/awesome-dsh-plugins) ⭐2 — Verified, star-ranked community plugins for DeepSeek Harness (dsh). (✅ active)
- [awesome-dshoneys](https://github.com/dshoneys/awesome-dshoneys) ⭐2 — DeepSeek Honeys 认证插件目录 — 安全检测报告 + 插件需求墙 + 每周精选 (✅ active)
- [dshmarketplace](https://github.com/DshMarketPlace/dshmarketplace) ⭐2 — Bilingual directory of DeepSeek Harness (DSH) plugins — 3,400+ listings, sandbox-verified install commands, written detail pages, public API. Next.js on Cloudflare Workers. (✅ active)
- [awesome-deepseek-harness](https://github.com/Harris1121/awesome-deepseek-harness) ⭐1 — Find the right DeepSeek Harness tools faster — see what’s popular, rising and worth using. (✅ active)
- [awesome-deepseek-harness-plugins](https://github.com/SihanTeng/awesome-deepseek-harness-plugins) ⭐1 — A curated collection of plugins, tools, and integrations for the DeepSeek Harness agent runtime (✅ active)
- [awesome-dsh-list](https://github.com/kingselyjoe/awesome-dsh-list) ⭐1 — 🐳 DeepSeek Harness（DSH）工具全量清单——GitHub topic:dsh-plugin 生态 1000+ 仓库按 star 排序。Awesome list for DeepSeek Harness tools. (✅ active)
- [awesome-dsh-plugins](https://github.com/oslook/awesome-dsh-plugins) ⭐1 — Deekseek Harness Plugins (✅ active)
- [awesome-dsh-presets](https://github.com/hackerFish/awesome-dsh-presets) ⭐1 — 实测可用的 DeepSeek Harness 预设与规则合集：官方派生 + 原创组合，每个预设通过结构与包存在性校验（中文优先） (✅ active)
- [awesome-deepseek-harness](https://github.com/Rodert/awesome-deepSeek-harness)  — deepSeek harness plugin DeepSeek Harness 组件 (✅ active)
- [awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness)  — Awesome DeepSeek Harness (dsh) — curated plugins, tools, skills & resources. Everything is a plugin. (✅ active)
- [dsh-plugin-registry](https://github.com/dshplugin-app/dsh-plugin-registry)  — Discover and compare DeepSeek Harness plugins directly inside DSH. (✅ active)
- [dshthemes](https://github.com/dshworks/dshthemes)  — dshthemes.com — every DeepSeek Harness theme, in its own colours. A reader of dshworks/awesome-dsh-themes. (✅ active)
- [plugins](https://github.com/dsh-universe/plugins)  — DeepSeek Harness plugin & skill directory — DSH Universe official marketplace (duink.com) (✅ active)

### Related Agent Harnesses


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [DeerFlow](https://github.com/bytedance/deer-flow) | ⭐80,462 | Open-source long-horizon SuperAgent harness by ByteDance: skills, memory, sandboxes, subagents, tools and a message gateway. | ✅ active |
| 2 | [CodeWhale](https://github.com/Hmbown/CodeWhale) | ⭐40,830 | Open-source, community-driven agent harness. | ✅ active |
| 3 | [agentmemory](https://github.com/rohitg00/agentmemory) | ⭐27,233 | Persistent memory for AI coding agents based on real-world benchmarks (upstream of DSH agentmemory ports). | ✅ active |
| 4 | [Cordis](https://github.com/cordiverse/cordis) | ⭐6,867 | Meta-Framework of Spatiotemporal Composability — the plugin runtime DeepSeek Harness is built on. | ✅ active |
| 5 | [deeptide](https://github.com/paean-ai/deeptide) | ⭐1,091 | Swift-native macOS coding agent built by DeepSeek, for DeepSeek. | ✅ active |
| 6 | [sandbase-harness](https://github.com/sandbaseai/sandbase-harness) | ⭐628 | Open-source CMA-compatible agent runtime for any model: MCP tools, sandboxed sessions, audit, replay. | ✅ active |
| 7 | [mnemon](https://github.com/mnemon-dev/mnemon) | ⭐500 | LLM-supervised persistent memory for AI agents: graph-based recall and cross-session knowledge in a single binary. | ✅ active |
| 8 | [claude-paper](https://github.com/alaliqing/claude-paper) | ⭐324 | Cross-agent research paper toolkit for Claude Code, Codex, OpenCode and DeepSeek Harness: quick summaries and deep dives. | ✅ active |
| 9 | [open-managed-agents](https://github.com/openma-ai/open-managed-agents) | ⭐243 | Open-source Claude Managed Agents API implementation and self-hosted Claude Tag-style agent runtime. | ✅ active |
| 10 | [Axern](https://github.com/cofy-x/axern) | ⭐57 | Open-source sandboxes for AI agents: untrusted code execution and durable services. | ✅ active |

#### Complete list (11)

- [DeerFlow](https://github.com/bytedance/deer-flow) ⭐80,462 — Open-source long-horizon SuperAgent harness by ByteDance: skills, memory, sandboxes, subagents, tools and a message gateway. (✅ active)
- [CodeWhale](https://github.com/Hmbown/CodeWhale) ⭐40,830 — Open-source, community-driven agent harness. (✅ active)
- [agentmemory](https://github.com/rohitg00/agentmemory) ⭐27,233 — Persistent memory for AI coding agents based on real-world benchmarks (upstream of DSH agentmemory ports). (✅ active)
- [Cordis](https://github.com/cordiverse/cordis) ⭐6,867 — Meta-Framework of Spatiotemporal Composability — the plugin runtime DeepSeek Harness is built on. (✅ active)
- [deeptide](https://github.com/paean-ai/deeptide) ⭐1,091 — Swift-native macOS coding agent built by DeepSeek, for DeepSeek. (✅ active)
- [sandbase-harness](https://github.com/sandbaseai/sandbase-harness) ⭐628 — Open-source CMA-compatible agent runtime for any model: MCP tools, sandboxed sessions, audit, replay. (✅ active)
- [mnemon](https://github.com/mnemon-dev/mnemon) ⭐500 — LLM-supervised persistent memory for AI agents: graph-based recall and cross-session knowledge in a single binary. (✅ active)
- [claude-paper](https://github.com/alaliqing/claude-paper) ⭐324 — Cross-agent research paper toolkit for Claude Code, Codex, OpenCode and DeepSeek Harness: quick summaries and deep dives. (✅ active)
- [open-managed-agents](https://github.com/openma-ai/open-managed-agents) ⭐243 — Open-source Claude Managed Agents API implementation and self-hosted Claude Tag-style agent runtime. (✅ active)
- [Axern](https://github.com/cofy-x/axern) ⭐57 — Open-source sandboxes for AI agents: untrusted code execution and durable services. (✅ active)
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
| 1 | [voyager](https://github.com/Nagi-ovo/voyager) | ⭐19,755 | Enhancement suite for Gemini, AI Studio, Claude & ChatGPT — plus a prompt manager for any web UI, DeepSeek Harness included. / 面向 Gemini、AI Studio、Claude 与 ChatGPT 的增强套件；提示词管理器可用于任意 Web UI，含 DeepSeek Harness。 | ✅ active |
| 2 | [dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | ⭐5,349 | Large plugin and skin collection for DSH Web: task board, git graph, side panels, remote/mobile UI, pets, token stats and themes. | ✅ active |
| 3 | [petdex](https://github.com/crafter-station/petdex) | ⭐3,945 | A public gallery of animated pets for Codex, Claude Code, DeepSeek Harness, Hermes, OpenCode, Gemini CLI, and more. | ✅ active |
| 4 | [dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) | ⭐3,697 | Two-phase DeepSeek Harness preset: Minimal-aligned bootstrap, then full Standard tools (Project2 98/99) | ✅ active |
| 5 | [modlens](https://github.com/liustack/modlens) | ⭐3,495 | The first vision plugin for DeepSeek Harness and the vision bridge for every text-only coding agent: paste an image and it works. | ✅ active |
| 6 | [DSH Better Sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) | ⭐2,552 | Workbench-style sidebar: file viewer/editor, terminal, Git, subagents and plugin-extensible tabs. | ✅ active |
| 7 | [dsh-market](https://github.com/dsh-market/dsh-market) | ⭐1,582 | Visual plugin market inside DeepSeek Harness: browse, search and one-click install. | ✅ active |
| 8 | [dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) | ⭐1,548 | Whale-girl skin series for DSH Web (CC BY-NC-SA 4.0). | ✅ active |
| 9 | [TokenTracker](https://github.com/xiufengsun/TokenTracker) | ⭐1,395 | Local-first AI token usage & cost tracker for 31 coding tools including Claude Code, Codex, Cursor, Gemini & DeepSeek Harness. | ✅ active |
| 10 | [dsh-vision-router](https://github.com/ysr666/dsh-vision-router) | ⭐927 | Eyes for text-only agents: built-in free keyless vision chain plus pixel-level tools (Q&A, grounding, crop, OCR, SVG trace). | ✅ active |

#### Complete list (263)

- [voyager](https://github.com/Nagi-ovo/voyager) ⭐19,755 — Enhancement suite for Gemini, AI Studio, Claude & ChatGPT — plus a prompt manager for any web UI, DeepSeek Harness included. / 面向 Gemini、AI Studio、Claude 与 ChatGPT 的增强套件；提示词管理器可用于任意 Web UI，含 DeepSeek Harness。 (✅ active)
- [dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) ⭐5,349 — Large plugin and skin collection for DSH Web: task board, git graph, side panels, remote/mobile UI, pets, token stats and themes. (✅ active)
- [petdex](https://github.com/crafter-station/petdex) ⭐3,945 — A public gallery of animated pets for Codex, Claude Code, DeepSeek Harness, Hermes, OpenCode, Gemini CLI, and more. (✅ active)
- [dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) ⭐3,697 — Two-phase DeepSeek Harness preset: Minimal-aligned bootstrap, then full Standard tools (Project2 98/99) (✅ active)
- [modlens](https://github.com/liustack/modlens) ⭐3,495 — The first vision plugin for DeepSeek Harness and the vision bridge for every text-only coding agent: paste an image and it works. (✅ active)
- [DSH Better Sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) ⭐2,552 — Workbench-style sidebar: file viewer/editor, terminal, Git, subagents and plugin-extensible tabs. (✅ active)
- [dsh-market](https://github.com/dsh-market/dsh-market) ⭐1,582 — Visual plugin market inside DeepSeek Harness: browse, search and one-click install. (✅ active)
- [dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) ⭐1,548 — Whale-girl skin series for DSH Web (CC BY-NC-SA 4.0). (✅ active)
- [TokenTracker](https://github.com/xiufengsun/TokenTracker) ⭐1,395 — Local-first AI token usage & cost tracker for 31 coding tools including Claude Code, Codex, Cursor, Gemini & DeepSeek Harness. (✅ active)
- [dsh-vision-router](https://github.com/ysr666/dsh-vision-router) ⭐927 — Eyes for text-only agents: built-in free keyless vision chain plus pixel-level tools (Q&A, grounding, crop, OCR, SVG trace). (✅ active)
- [dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) ⭐802 — Vision toolkit for text-only models: intent-aware image Q&A, long-screenshot OCR, UI restoration, grounding and pixel diff. (✅ active)
- [dsh-context](https://github.com/bowenliang123/dsh-context) ⭐666 — A DeepSeek Harness plugin for  Context insight dashboard — showing what the model's context window is made of and how it evolves. (✅ active)
- [museai](https://github.com/yejiming/MuseAI) ⭐595 — 创建你的 AI 角色，进入你的故事世界。和角色聊天、冒险、穿书，让每一次互动都留下羁绊（支持 DeepSeek Harness 插件，欢迎使用） (✅ active)
- [graph-memory](https://github.com/adoresever/graph-memory) ⭐564 — Deepseek Harness、Openclaw知识图谱记忆插件。2026年4月受邀发布在清华大学讨论会。Knowledge Graph + Memory；Knowledge Graph Context Engine for OpenClaw — extracts structured triples from conversations, compresses context 75%, enables cross-session experience reuse (✅ active)
- [dsh-ads](https://github.com/Nagi-ovo/dsh-ads) ⭐525 — Joke plugin: 2005 Chinese-web-style ad layer with sidebar banners, in-chat feed ads and corner popups. (✅ active)
- [v4-flash-godmode-opencode-go](https://github.com/SheberDavid/v4-flash-godmode-opencode-go) ⭐494 — V4 Flash 神模式 (opencode-go)：让 opencode-go 的 DeepSeek V4 Flash 从鬼模式切换到神模式的 dsh agent preset (✅ active)
- [dsh-at-file](https://github.com/omdsh-dev/dsh-at-file) ⭐445 — Codex-style @file mentions inside the DSH composer: search workspace files and attach their contents to prompts. (✅ active)
- [dsh-browser](https://github.com/Lum1104/dsh-browser) ⭐366 — Chrome sidebar extension that lets DSH operate your browser directly, no vision capabilities required. (✅ active)
- [dsh-transparent-ui-plugin](https://github.com/WYH66666666/DSH-Transparent-UI-Plugin) ⭐355 — 是一层高自由度的玻璃质感主题，套在 DeepSeek Harness 网页端。顶栏、侧边栏、输入框、统计行、轨迹视图都成了磨砂玻璃片。玻璃模糊度、磨砂度、背景（流体或自定义壁纸，壁纸还能单独调模糊和磨砂）全都能在设置卡片里自由调节。关掉开关就回到原生界面，不改 DSH 任何一行源码。 (✅ active)
- [flowix](https://github.com/text2future/flowix) ⭐338 — Notes for you, Memory for your agents. / 内置 Deepseek harness Agent / 适用 办公 & 写作 & Coding (✅ active)
- [dsh-genui](https://github.com/omdsh-dev/dsh-genui) ⭐282 — Generative UI inside conversations: layouts, charts, forms, quizzes, Mermaid and interactive events rendered inline. (✅ active)
- [dsh-pet](https://github.com/PC2005-cloud/dsh-pet) ⭐274 — DeepSeek Harness 桌面宠物插件 + 完整素材生成链：AI 提示词 → 绿幕视频 → 透明动画 → 可安装插件，从零到宠物全流程可复现 (✅ active)
- [whale-girl](https://github.com/vlln/whale-girl) ⭐260 — Desktop pet plugin (QQ-pet style) floating at the bottom-right of the DSH Web GUI: draggable, feedable and playable. (✅ active)
- [dsh-plugin-subscriptions](https://github.com/V1ki/dsh-plugin-subscriptions) ⭐216 — Use ChatGPT (Codex), Claude, and Grok (X Premium) subscriptions as DeepSeek Harness LLM providers — OAuth login in the web UI, no API keys (✅ active)
- [dsh-memory-evolve](https://github.com/csyangwen/dsh-memory-evolve) ⭐211 — Cross-session long-term memory + background self-evolution: five-track memory, git-branch awareness, in-turn self-review and skill evolution. (✅ active)
- [modsearch](https://github.com/liustack/modsearch) ⭐207 — Web plugin for DSH and the search bridge for every model without native web access. (✅ active)
- [dsh-visualize](https://github.com/Nagi-ovo/dsh-visualize) ⭐196 — Interactive HTML UI rendered directly in conversation with streaming preview and sandbox rendering. (✅ active)
- [Open Sea Skin](https://github.com/d-dev0101/open-sea-skin) ⭐185 — Realtime WebGPU ocean skin with controls for waves, daylight, glass opacity and automatic day cycling. (✅ active)
- [anysearch-dsh](https://github.com/anysearch-team/anysearch-dsh) ⭐174 — AnySearch web search provider and advanced search tools for DeepSeek Harness. (✅ active)
- [dsh-find-plugins](https://github.com/Nagi-ovo/dsh-find-plugins) ⭐162 — Plugin discovery utility for the DSH ecosystem. (✅ active)
- [anime-find](https://github.com/cocofhu/anime-find) ⭐157 — DeepSeek Harness 搜番插件：对话内多源搜索番剧，卡片展示 Bangumi 评分与详情，支持复制磁力。 (✅ active)
- [dsh-mnemon](https://github.com/omdsh-dev/dsh-mnemon) ⭐156 — Three-tier local memory: runtime hot memory, project documents and long-term memory spaces, with supervised writeback. (✅ active)
- [dsh-cost-meter](https://github.com/Han-1413141/dsh-cost-meter) ⭐139 — DeepSeek Harness 会话费用统计插件:本会话费用、当日费用、历史记录与官方价格同步 (✅ active)
- [dsh-gitbash-preset](https://github.com/liceses/dsh-gitbash-preset) ⭐136 — DeepSeek Harness 插件：一键安装「极简模式 (Git Bash)」agent preset —— 把 DSH 自带极简模式中的 bash 调用映射到 Git for Windows 的 bash（MSYS），让 Windows 上的极简模式真正可用。 (✅ active)
- [DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) ⭐132 — Browse, install and update every GitHub topic:dsh-plugin plugin from the DSH Web GUI. (✅ active)
- [tokenledger](https://github.com/zh667/TokenLedger) ⭐126 — Token usage accounting for DeepSeek Harness, reconciled against New API and Sub2API relay-site billing (✅ active)
- [dsh-auto-mode](https://github.com/NanmiCoder/dsh-auto-mode) ⭐115 — Safe automatic permissions for DeepSeek Harness. (✅ active)
- [dsh-undo-plugin](https://github.com/lire1131/dsh-undo-plugin) ⭐108 — DSH plugin: snapshot & rollback your plugin/skin/settings configs. Auto-save on change, undo/redo stack, snapshot manager panel, keyboard shortcuts, plus an offline PowerShell CLI & GUI that work even when DSH won't boot. (✅ active)
- [dsh-usage-stats](https://github.com/Ychris12138/dsh-usage-stats) ⭐98 — Token usage heatmap, per-model breakdowns, and DeepSeek account balance for the DeepSeek Harness Web GUI (dsh web). (✅ active)
- [dsh-reasoning-effort](https://github.com/HanaAyane/dsh-reasoning-effort) ⭐97 — DSH适用的Codex风格的思考强度滑块，以及大肥鱼跑步滑块。Codex-style model and reasoning-effort slider for DeepSeek Harness (✅ active)
- [dsh-webui-market-plugin](https://github.com/Sanqi-normal/dsh-webui-market-plugin) ⭐96 — Community plugin market in the Web GUI: browse the awesome-dsh-plugin.com catalog and install/uninstall to a profile. (✅ active)
- [dsh-turn-rewind](https://github.com/Anionex/dsh-turn-rewind) ⭐94 — Rewind conversation and workspace state, powered by a persistent change ledger. (✅ active)
- [dsh-plugin](https://github.com/Tabbit-Browser/dsh-plugin) ⭐91 — Tabbit Broser plugins for Deepseek Harness (✅ active)
- [dsh-annotation](https://github.com/omdsh-dev/dsh-annotation) ⭐87 — Select text in DSH Web, annotate it and send the annotation with your message; replies cross-reference each annotation. (✅ active)
- [dsh-chat-import](https://github.com/Nwflower/dsh-chat-import) ⭐87 — Import conversation history from Claude Code, Codex, ChatGPT, Cursor, Gemini, Reasonix and OpenCode into resumable DSH sessions. (✅ active)
- [dsh-commandcode-provider](https://github.com/Mars-Sea/dsh-commandcode-provider) ⭐83 — Unofficial DeepSeek Harness LLM provider plugin for Command Code: live model catalog, reasoning-effort support, Models-page card. Ported from pi-commandcode-provider (MIT). (✅ active)
- [dsh-kun-like-pet](https://github.com/liyupi/dsh-kun-like-pet) ⭐80 — Kun Like 桌宠 —— DeepSeek Harness 桌面宠物插件：右下角小坤宠随 Agent 工作状态切换 9 种动作，任务完成播放「你干嘛~哎哟」 (✅ active)
- [dockyard-dsh](https://github.com/AITabby/dockyard-dsh) ⭐73 — A macOS-only native account-pool and provider plugin for DeepSeek Harness. (✅ active)
- [dsh-dream-skin](https://github.com/RevolutionLA/dsh-dream-skin) ⭐73 — One-command skinning for DSH Web: 8 original themes, wallpaper (opacity/blur/gradient/URL), per-user accent, shareable theme packs, favorites and surprise-me — purely native on DSH's token system. (✅ active)
- [dsh-find-plugin](https://github.com/awesome-dsh-plugin/dsh-find-plugin) ⭐73 — Agent-assisted plugin discovery: search the live GitHub dsh-plugin topic from inside DSH. (✅ active)
- [dsh-notification](https://github.com/omdsh-dev/dsh-notification) ⭐70 — Desktop notifications for turn completions with per-outcome controls and include/exclude keyword filters. (✅ active)
- [dsh-plugin-hub](https://github.com/Noob-stupid/dsh-plugin-hub) ⭐64 — Plugin management panel: enable/disable installed plugins plus a GitHub dsh-plugin marketplace with one-click install. (✅ active)
- [dsh-plugins-store](https://github.com/ZASENJC/dsh-plugins-store) ⭐62 — Static directory site that automatically collects and categorizes GitHub dsh-plugin topic projects. (✅ active)
- [dsh-web-plugin-manager](https://github.com/LX2000WASD/dsh-web-plugin-manager) ⭐62 — Manage plugins from the Web UI: view, live enable/disable, install/uninstall, env management and plugin market. (✅ active)
- [deepseek-harness-control-center](https://github.com/feibi-mochi/deepseek-harness-control-center) ⭐61 — DeepSeek Harness account monitoring, usage accounting, completion alerts, official recharge, flexible layout, and agent-assisted session controls. / 账户监控、提醒、充值与会话控制中心 (✅ active)
- [dsh-claude-ux](https://github.com/eri64/dsh-claude-ux) ⭐60 — DSH plugin: Claude-style Chinese risk control & conversation autonomy for DeepSeek Harness web (✅ active)
- [dsh-memento](https://github.com/PerryLink/dsh-memento) ⭐59 — Bounded, layered, approval-gated and auditable cross-session memory with frozen snapshot injection. (✅ active)
- [dsh-open-in-vscode](https://github.com/omdsh-dev/dsh-open-in-vscode) ⭐53 — Open DSH workspace directories/files directly in VS Code from the web GUI. (✅ active)
- [dsh-navbar](https://github.com/vlln/dsh-navbar) ⭐52 — DSH 插件：对话节点导航条（右缘节点串快速跳转 user 消息）。官方 bundle 插件，dsh plugin --profile web add 安装 (✅ active)
- [deepseek-harness-skin](https://github.com/HeiGeAi/deepseek-harness-skin) ⭐49 — Skin system with 21 built-in themes plus one-image custom skin generation, contrast-validated at build time. (✅ active)
- [dsh-plugins](https://github.com/Ephemeral-AI-Lab/dsh-plugins) ⭐45 — Make Deepseek Harness Great (✅ active)
- [dsh-smooth-stream](https://github.com/Laplace-bit/dsh-smooth-stream) ⭐45 — Silky streaming reveal for the Web UI: text appears at the model's arrival rate, new lines glide in, no flicker; follow stays with the user and respects prefers-reduced-motion. (✅ active)
- [dsh-status-rotator](https://github.com/01Virex/dsh-status-rotator) ⭐42 — Replaces the 'Deep diving…' turn-status label with phase-aware typewriter messages. (✅ active)
- [dsh-trace-compare](https://github.com/lamost423/dsh-trace-compare) ⭐41 — Trace Compare & Live Maze for DeepSeek Harness: visualize agent exploration (main path, detours, backtracks) from session logs or live sessions (✅ active)
- [xgone/dsh-remote](https://github.com/xgone/dsh-remote) ⭐41 — Remote access & authentication for DeepSeek Harness web UI: account/password login gate, MFA (TOTP), signed session cookies, role-based access, in-browser directory picker, and a Settings page for account management. (🧪 experimental)
- [dsh-prompt-enhancer](https://github.com/Fishsb/dsh-prompt-enhancer) ⭐39 — DeepSeek Harness DSH 提示词增强插件：✨ 一键优化草稿，增强提示词。 (✅ active)
- [ui-status-label](https://github.com/alingalingling/ui-status-label) ⭐39 — Customize the whale's 'Deep diving' status label into anything you want. (✅ active)
- [dsh-free-search](https://github.com/DDDMUC/dsh-free-search) ⭐38 — Free web search provider for DeepSeek Harness - DuckDuckGo backend, no API key needed (✅ active)
- [dsh-plugin-mineru](https://github.com/HuanLinOTO/dsh-plugin-mineru) ⭐38 — Expose MinerU document parsing to the model: PDF/images/DOCX/PPTX/XLSX to structured Markdown/JSON. (✅ active)
- [dsh-expression](https://github.com/yyh-001/dsh-expression) ⭐36 — DeepSeek Harness 的表情包插件——找得到、发得出、学得会 (✅ active)
- [dsh-vision (william-jin-cmu)](https://github.com/william-jin-cmu/dsh-vision) ⭐36 — Vision bridge: view_image tool over any OpenAI-compatible VLM, defaulting to Zhipu's free tier. (✅ active)
- [dsh-message-edit](https://github.com/Moeblack/dsh-message-edit) ⭐35 — Branch-based message editing, reroll, retry and version timeline. (✅ active)
- [dsh-codex-connect](https://github.com/franksong2702/dsh-codex-connect) ⭐34 — ChatGPT OAuth and Codex models for DeepSeek Harness. (✅ active)
- [dsh-emoji](https://github.com/hellodigua/dsh-emoji) ⭐34 — Let AI replies add custom emoji reactions. (✅ active)
- [dsh-omi-voice](https://github.com/PolinniZhong/dsh-omi-voice) ⭐34 — Immersive voice reading plugin: in-chat read/pause/resume with Doubao TTS natural voices (BYOK), reads only the final answer, filters code/tables/graphics. (✅ active)
- [billion-context-dsh](https://github.com/Tyan66666/billion-context-dsh) ⭐33 — Model-driven context compression (Active Context Pruning): the model decides when and what to compress. (✅ active)
- [dsh-mneme](https://github.com/modusensus/dsh-mneme) ⭐31 — Local cross-session memory with memory sovereignty: SQLite + human-editable Markdown mirror and background autoDream consolidation. (✅ active)
- [dsh-remote](https://github.com/flymysql/dsh-remote) ⭐31 — Remote workspace: connect a host over SSH and operate a remote directory with rw_* tools. (✅ active)
- [dsh-share](https://github.com/hellodigua/dsh-share) ⭐29 — One-click conversation sharing for DSH. (✅ active)
- [dsh-ui-whale](https://github.com/lhh010/dsh-ui-whale) ⭐29 — Hand-drawn pixel whale companion in the session title bar: blinks, wags its tail, spouts water when a turn completes. (✅ active)
- [dsh-web-search-pro](https://github.com/anweat/dsh-web-search-pro) ⭐29 — Multi-engine persistent search: DeepSeek/Exa/DDG/Bing/Jina + GitHub/Bilibili/YouTube/V2EX/XHS/Twitter/Reddit/RSS, with SQLite+LRU cache and Playwright rendering. (✅ active)
- [ego-browser](https://github.com/Fisfzy/ego-browser) ⭐29 — Bring the ego-lite agent browser (Chromium for AI agents) into DSH with 13 structured tools. (✅ active)
- [deepseek-harness-snowsalt](https://github.com/KYZHXL/deepseek-harness-snowsalt) ⭐28 — Snow-salt themed skin for DeepSeek Harness. (✅ active)
- [dsh-plugin-guard](https://github.com/lxzy-7/dsh-plugin-guard) ⭐28 — Install safety net for DeepSeek Harness: pre-install snapshots, one-click/automatic rollback, guarded boot, and incident reports that auto-trigger agent analysis. 中文: DeepSeek Harness 插件安装安全网（安装前自动快照、一键/自动回退、守护启动、事故报告自动触发 Agent 分析）。 (✅ active)
- [dsh-plugin-check](https://github.com/omdsh-dev/dsh-plugin-check) ⭐27 — Plugin health checks: manifest protocol, patch format, build pitfalls and hub listing status, zero-dependency read-only. (✅ active)
- [dsh-computer-use](https://github.com/Anionex/dsh-computer-use) ⭐26 — 为 DeepSeek Harness 提供电脑控制插件：新鲜 Accessibility 观测、过期状态拒绝、作用域权限与安全输入（目前支持macos）｜Accessibility-first macOS Computer Use bundle for DSH with fresh observations, stale-state rejection, scoped permissions, and safe input. (✅ active)
- [dsh-auto-memory](https://github.com/Aik358/dsh-auto-memory) ⭐25 — DSH 自动记忆插件:三层记忆(用户级/项目笔记/每日日志)自动注入与检索、每日反思、可视化面板与设置页,支持继承其他 AI 工具的历史记忆。An auto-memory plugin for the DeepSeek Harness Web GUI: three-layer memory (user-level / project notes / daily logs) with automatic injection and retrieval, daily reflections, a visual panel and settings page, and inheritance of memories from other AI tools. (✅ active)
- [dsh-minigames](https://github.com/lhh010/dsh-minigames) ⭐25 — DSH Web UI 右侧小游戏面板：18 款离线小游戏（恐龙跳一跳 / 俄罗斯方块 / 坦克大战 / 扫雷 / 2048 / 数独 / 吃豆人 / 跟枪练习等），可扩展游戏注册表，等待模型回复或修 bug 时的摸鱼神器 (✅ active)
- [dsh-plugin-workshop](https://github.com/yyyyukari/dsh-plugin-workshop) ⭐25 — Steam Workshop-style plugin browser for the DSH Web UI: zero-server, GitHub-powered search and one-click install. (✅ active)
- [dsh-custom-tool](https://github.com/omdsh-dev/dsh-custom-tool) ⭐24 — Create and manage sandboxed JavaScript tools for DSH with a Monaco editor and model-driven tool lists. (✅ active)
- [dsh-diff-viewer](https://github.com/lehhair/dsh-diff-viewer) ⭐24 — PiUI-style Web diff viewer replacing the default diff view. (✅ active)
- [dsh-recall-plugin](https://github.com/limbo947/dsh-recall-plugin) ⭐24 — DSH 消息撤回插件：回到发送该消息时的状态 DSH Message Recall Plugin: Return to the state when the message was sent (✅ active)
- [dsh-toolkit](https://github.com/omdsh-dev/dsh-toolkit) ⭐24 — Zero-dependency tool suite: calculator, CSV, diff, encoding, JSON, Markdown, regex and time utilities. (✅ active)
- [dsh-balance](https://github.com/crazywoola/dsh-balance) ⭐23 — DeepSeek Harness balance plugin for the Settings page. (✅ active)
- [dsh-plugin-better-sidebar-plugin-office](https://github.com/HuanLinOTO/dsh-plugin-better-sidebar-plugin-office) ⭐23 — Office-suite preview (.docx/.xlsx/.pptx) for the Better Sidebar, as a standalone slim bundle. (✅ active)
- [dsh-focus-chat](https://github.com/dingyi222666/dsh-focus-chat) ⭐21 — 为 dsh 提供新的「聚焦会话」精简会话视图，更轻松易于阅读，只关注最终产出结果。 (✅ active)
- [dsh-plugin-pet-rs](https://github.com/HuanLinOTO/dsh-plugin-pet-rs) ⭐21 — Rust desktop pet: 5-state whale with dual SSE real-time push, transparent always-on-top window and system tray. (✅ active)
- [dsh-stickers](https://github.com/william-jin-cmu/dsh-stickers) ⭐21 — DSH WebUI sticker plugin for bidirectional user and agent reactions (✅ active)
- [dsh-web-ui-notify](https://github.com/bill9109/dsh-web-ui-notify) ⭐21 — Adds desktop notification reminders to DSH. (✅ active)
- [dsh-drag-and-drop](https://github.com/bill9109/dsh-drag-and-drop) ⭐20 — Cross-platform drag & drop for DSH Web UI with original-path insertion, no file copying. (✅ active)
- [dsh-agy](https://github.com/chaos-03x/dsh-agy) ⭐19 — Google Antigravity (agy) OAuth auth + model access plugin for DeepSeek Harness: multi-account pool, 429 rotation, device fingerprinting, CLI and web login. (✅ active)
- [dsh-balance-meter](https://github.com/Ghost011118/dsh-balance-meter) ⭐19 — DeepSeek account balance and session cost readout for the DeepSeek Harness Web GUI (✅ active)
- [dsh-skin](https://github.com/KinGao294/dsh-skin) ⭐19 — Codex-style skin switcher plus custom translucent wallpaper with opacity/blur controls. (✅ active)
- [dsh-theme-plugin](https://github.com/nevertoday/dsh-theme-plugin) ⭐19 — Chinese traditional colors as a DeepSeek Harness theme pack. (✅ active)
- [compass](https://github.com/dshakes/compass) ⭐18 — 🧭 Let your coding agent off the leash — not off the rails. Guardrails, a hard budget cap & a self-fixing PR loop for Claude Code / Codex / Gemini. Eval-gated 100/100, you always merge. (✅ active)
- [dsh-milestone](https://github.com/SnowCrescenter-tech/dsh-milestone) ⭐18 — Git-style milestone timeline rail: hover for metadata, click to jump to any message. (✅ active)
- [dsh-recommend](https://github.com/zp-home/dsh-recommend) ⭐18 — Transparent plugin rankings and recommendations: daily auto-fetched dsh-plugin topic data with an open scoring model. (✅ active)
- [touhou-hakurei](https://github.com/xiake595/touhou-hakurei) ⭐18 — 灵梦（Reimu）·博丽神社（东方Project）美化版皮肤：神社昼夜实景背景、灵梦立绘、画框侧边栏与输入框、纸白透明界面 — DeepSeek Harness Web GUI skin (✅ active)
- [webdsh](https://github.com/futrime/webdsh) ⭐18 — Running DeepSeek Harness on web (✅ active)
- [DeepSeek-Harness-Web-Tools](https://github.com/tonyd2wild/DeepSeek-Harness-Web-Tools) ⭐17 — Free, keyless web_search and web_fetch for DSH, DuckDuckGo-backed with no signup. (✅ active)
- [dsh-context-doctor](https://github.com/Zhenyu98/dsh-context-doctor) ⭐17 — Audits what actually enters every model request: token cost of AGENTS.md chains, skill catalogs and tool schemas, with duplicate/conflict detection. (✅ active)
- [dsh-group-photo](https://github.com/SenmuuuuW/dsh-group-photo) ⭐17 — DSH 内测收官合影墙：GitHub OAuth 零权限登录 + 冻结白名单校验的拍立得合影站（含 DSH Skill 包装） (✅ active)
- [dsh-passwords](https://github.com/slywalker2006/dsh-passwords) ⭐17 — dsh-passwords: DeepSeek Harness login gateway - first-run setup, at-rest encryption, brute-force lockout, audit log, HTTPS (✅ active)
- [dsh-plugin-writing-guard](https://github.com/xmutfyh/dsh-plugin-writing-guard) ⭐17 — DeepSeek Harness (DSH) academic writing guard for papers — 论文去AI味 / AI-writing style detection, evidence preservation, journal-fit calibration, manuscript proofreading, writing_audit & automatic checks. Local, zero network, zero LLM. (✅ active)
- [dsh-side-panel](https://github.com/ccq1/dsh-side-panel) ⭐16 — Compact side panel with a file browser, terminal and Git review. (💤 inactive)
- [dsh-stock-market](https://github.com/AnacondaKC/dsh-stock-market) ⭐15 — Stock market data plugin (joke: fixes the bug where your account loses money while you code). (✅ active)
- [dsh-web-review](https://github.com/CanglongCl/dsh-web-review) ⭐15 — DeepSeek Harness Web GUI 的网页预览与元素批注插件，让 AI 根据可视化反馈直接修改前端源码。 (✅ active)
- [deepseek-harness-zh_pro](https://github.com/magian1127/deepseek-harness-zh_pro) ⭐14 — Chinese enhancement plugin for DeepSeek Harness (DSH) - DSH 中文增强插件 (✅ active)
- [dsh-gomoku](https://github.com/omdsh-dev/dsh-gomoku) ⭐14 — Play Gomoku with AI inside DSH, or let two AIs battle to compare models. (✅ active)
- [dsh-plugin](https://github.com/loongsuite/dsh-plugin) ⭐14 — OpenTelemetry tracing for DeepSeek Harness (dsh): turns each agent turn into a GenAI span tree — steps, LLM calls with TTFT, tool executions, token usage — exported over standard OTLP to Jaeger, Grafana Tempo, SigNoz, Langfuse, or any compatible backend. (✅ active)
- [dsh-deepcel](https://github.com/Small-tailqwq/dsh-deepcel) ⭐13 — Spreadsheet-style skin for DSH, mimicking Excel. (✅ active)
- [dsh-nested-followups](https://github.com/sluminositys/dsh-nested-followups) ⭐13 — Ask a follow-up on any past answer in an isolated branch, keeping your main conversation clean. 针对任意历史回答发起追问，新问题在独立分支中展开，主对话保持干净。A conversation-tree plugin for DeepSeek Harness / DeepSeek Harness 会话树插件。 (✅ active)
- [dsh-opencode-go-usage](https://github.com/Xenia0922/dsh-opencode-go-usage) ⭐13 — DeepSeek Harness 插件:OpenCode Go 用量与花费悬浮仪表盘(配额、逐请求成本、模型/来源分布) (✅ active)
- [dsh-pet](https://github.com/FlytoMAYDAY80/dsh-pet) ⭐13 — 🐋 DSH 有声桌宠：悬浮桌面的 DeepSeek 小鲸鱼，不打开 DSH 也能实时感知会话状态（需要确认/工作中/完成/空闲/离线），支持音效提醒与零代码定制素材 (✅ active)
- [dsh-plugin-aigc-canvas](https://github.com/HuanLinOTO/dsh-plugin-aigc-canvas) ⭐13 — provider-agnostic AIGC HTTP 桥 + 无限画布 + ffmpeg 后处理，13 个工具含画布连边/reroll/媒体编辑 | Provider-agnostic AIGC HTTP bridge + infinite canvas + ffmpeg post-processing; 13 tools incl. canvas linking/reroll/media-edit (✅ active)
- [dsh-security-audit](https://github.com/omdsh-dev/dsh-security-audit) ⭐13 — DSH 本机安全审计插件：配置/插件来源/会话/网络暴露面，只读脱敏风险报告 (✅ active)
- [DeepSeek-Harness-Vision-Tools](https://github.com/tonyd2wild/DeepSeek-Harness-Vision-Tools) ⭐12 — Vision proxy for chat: give DSH eyes with any text model plus any vision model. (✅ active)
- [dsh-surfing-plugin](https://github.com/cyijun/dsh-surfing-plugin) ⭐12 — SearXNG search and Crawl4AI fetch providers for DeepSeek Harness (✅ active)
- [dsh-trading](https://github.com/maddogfinance/dsh-trading) ⭐12 — Research-only trading workbench for DSH: typed market-data seam (BYO provider), multi-timeframe indicator snapshots, interactive chart cards with provenance-gated annotations, and a risk-guard denying execution-shaped tool calls. No execution seam by construction. (✅ active)
- [weshop-dsh-plugin](https://github.com/weshopai/weshop-dsh-plugin) ⭐12 — Native WeShop Cordis plugin for DeepSeek Harness. Allow you to use infinite canvas with infinite creative skills. (✅ active)
- [dsh-file-mentions](https://github.com/a903067276-rgb/dsh-file-mentions) ⭐11 — Clickable file paths in DSH replies: inline open, reveal in file manager and a mentioned-files chip list. (✅ active)
- [dsh-file-mount](https://github.com/acefun29/dsh-file-mount) ⭐11 — Incremental file mounting with line-range deduplication: identical file contents are never re-sent to the model. (✅ active)
- [dsh-plugin-ya-workspace-sidebar](https://github.com/HuanLinOTO/dsh-plugin-ya-workspace-sidebar) ⭐11 — DSH Web 工作区侧栏替代，顶部全局最近会话 + Workspace→Session 二级菜单 + 面包屑 | DSH Web workspace sidebar replacement: top global recent sessions + Workspace→Session two-level menu + breadcrumbs (✅ active)
- [dsh-sdk-platform-rs](https://github.com/kpn-dsh/dsh-sdk-platform-rs) ⭐11 — A Rust SDK to interact with the DSH Platform. This library provides convenient building blocks for services that need to connect to DSH Kafka, fetch tokens for various protocols, manage Prometheus metrics, and more. (✅ active)
- [dsh-sticky-note](https://github.com/Meredith2328/dsh-sticky-note) ⭐11 — 左下角便签：随手记点子/感想/TODO，实时保存到归档目录，清单+悬浮归档 (✅ active)
- [oh-my-dsh](https://github.com/NoWint/Oh-My-DSH) ⭐11 — 🐋 Oh-My-DSH — DeepSeek Harness Plugin Ecosystem【每一小时更新】 (✅ active)
- [context-vista](https://github.com/GooodWei/context-vista) ⭐10 — Live context/token monitor: floating panel + /context command with donut charts of token usage, allocation and estimated cost. (✅ active)
- [dsh-plugin-anti-ads](https://github.com/HuanLinOTO/dsh-plugin-anti-ads) ⭐10 — DSH Web 广告拦截器，四层独立防御拦截 dsh-ads 插件的所有广告位 | DSH Web ad blocker with four independent defense layers targeting the dsh-ads plugin (✅ active)
- [dsh-ui-appearance](https://github.com/TQSY114514/dsh-ui-appearance) ⭐10 — Appearance customization plugin for DeepSeek Harness: theme color palette, background image, opacity/blur, glass effect (✅ active)
- [dsh-usage-chart](https://github.com/Max-Samson/dsh-usage-chart) ⭐10 — A DeepSeek Harness Web plugin for real-time Token usage, cost estimates, per-round charts, and DeepSeek API balance. (✅ active)
- [dsh-web-billing](https://github.com/bpc-oss/dsh-web-billing) ⭐10 — RMB/USD token billing for the DSH web: official-policy auto pricing with peak/off-peak hours and per-message cost ledger. (✅ active)
- [DeepSeek-Harness-billing-plugin](https://github.com/WilliamLIiii/DeepSeek-Harness-billing-plugin) ⭐9 — Account balance plus per-model remaining-task estimator with a session cost ledger. (✅ active)
- [dsh-awiki](https://github.com/AgentConnect/dsh-awiki) ⭐9 — AWiki identity and messaging plugin for DeepSeek Harness (✅ active)
- [dsh-hud](https://github.com/a903067276-rgb/dsh-hud) ⭐9 — HUD status panel: git status, MCP servers, skills, model and token usage in a floating side panel. (✅ active)
- [dsh-paste-input](https://github.com/lhh010/dsh-paste-input) ⭐9 — WebUI file input enhancement: Ctrl+V paste, drag & drop and file picker, copied into the session workspace. (✅ active)
- [dsh-plugin-auto-blame](https://github.com/HuanLinOTO/dsh-plugin-auto-blame) ⭐9 — 模型回合结束后用 LLM 生成 3 条批判性跟进建议，点击即发送 | After a model turn, an LLM generates 3 critical follow-up suggestions shown as click-to-send chips (✅ active)
- [dsh-plugin-interpreters](https://github.com/HuanLinOTO/dsh-plugin-interpreters) ⭐9 — Expose run_python/run_node tools that execute code via stdin and return stdout/stderr/exit code. (✅ active)
- [dsh-spotlight](https://github.com/0xsline/dsh-spotlight) ⭐9 — Keyboard-first command palette for DeepSeek Harness Web. (✅ active)
- [deepseek-harness-SupportVisionModel](https://github.com/TryDing-T/deepseek-harness-SupportVisionModel) ⭐8 — Secondary development of deepseek-harness supporting a separately configured vision model for reading images. (✅ active)
- [dsh-plugin-d399](https://github.com/HuanLinOTO/dsh-plugin-d399) ⭐8 — Mini-game menu (Wordle, match-3, 192 parameterized games) that pops up while the model generates. (✅ active)
- [dsh-session-health](https://github.com/omdsh-dev/dsh-session-health) ⭐8 — Frame-level diagnostics for multi-frame zstd session files: torn/corrupted/empty session detection, zero-dependency read-only. (✅ active)
- [dsh-usage-dashboard](https://github.com/Cassius0924/dsh-usage-dashboard) ⭐8 — DeepSeek 额度与用量仪表盘 — DSH (DeepSeek Harness) 动态 Cordis 插件 (✅ active)
- [dsh-browser](https://github.com/anweat/dsh-browser) ⭐7 — Self-contained browser runtime plugin for DeepSeek Harness — bundles Playwright (chromium) and OpenCLI as plugin-local dependencies, exposes a browser service and interactive browser tools. (✅ active)
- [dsh-builtin-toggles](https://github.com/Starfie1d1272/dsh-builtin-toggles) ⭐7 — Human-readable catalog of official DSH Web built-ins with safe GUI toggles. (✅ active)
- [dsh-director-toolkit](https://github.com/lhmd/dsh-director-toolkit) ⭐7 — DSH Director Toolkit is a DeepSeek Harness plugin for 3D artists, technical designers, and creative coders. Paste a half-formed idea, a reference note, or a portfolio caption and get a compact direction pack for Blender, Three.js, Houdini, or C4D. (✅ active)
- [dsh-git-identity](https://github.com/LoserFox/dsh-git-identity) ⭐7 — DSH 插件：git 提交固定使用环境自身作者身份（优先 gh CLI 登录账号，GitHub noreply 邮箱），GIT_AUTHOR_*/GIT_COMMITTER_* 环境变量注入压过一切 git config (✅ active)
- [dsh-landscape](https://github.com/cyanseek/dsh-landscape) ⭐7 — Agent-first DeepSeek Harness plugin intelligence: verify existing plugins, identify missing capabilities, and generate build-ready briefs. (✅ active)
- [dsh-pdf](https://github.com/sunshine-lang/dsh-pdf) ⭐7 — PDF toolbox: extract text, metadata and page ranges via pdfjs-dist, local with no API key. (✅ active)
- [dsh-plugin-diff-review](https://github.com/Civitasv/dsh-plugin-diff-review) ⭐7 — Diff Review Plugin for DeepSeek Harness (✅ active)
- [dsh-spend](https://github.com/nonewind/dsh-spend) ⭐7 — Token usage and estimated spend: floating panel with per-model/day/session stats and auto-detected billing plans. (✅ active)
- [dsh-token-panel](https://github.com/juhe291/dsh-token-panel) ⭐7 — A corner HUD for DeepSeek Harness that shows your session's token pressure, per-model cost, and daily/monthly usage at a glance — with an editable budget & balance that tracks spending for you. 右下角常驻的 Token 仪表盘：实时查看会话压力、按模型估算花费，预算和余额点一下就能改，每天每月用了多少都有记录。 (✅ active)
- [dsh-weather](https://github.com/sunshine-lang/dsh-weather) ⭐7 — Weather tool: current conditions and multi-day forecasts via Open-Meteo, free with no API key. (✅ active)
- [dskin](https://github.com/dancingmemory/dskin) ⭐7 — Cartoon pixel skin plugin for DSH Web GUI: pixel pets that walk, blink and jump over the original interface. (✅ active)
- [dsh-cue-plugin](https://github.com/unnnnoooo/dsh-cue-plugin) ⭐6 — DeepSeek Harness 的跨会话引用(cue)插件 (✅ active)
- [dsh-email](https://github.com/STARDUSTLC666/dsh-email) ⭐6 — DeepSeek Harness 邮件插件：email_list/read/search/send/folders/attachment 六工具，内置 QQ/163/126/新浪/阿里/Gmail/Outlook/iCloud 八个预设，多账号、附件收发、Web 设置页配置，纯 Node 全平台。· IMAP/SMTP email tools for DeepSeek Harness agents. (✅ active)
- [dsh-file-claim](https://github.com/Nwflower/dsh-file-claim) ⭐6 — File ownership/claim system for parallel agent sessions on the same project: claim/release, heartbeat stale takeover and async 3-way merge. (✅ active)
- [dsh-island](https://github.com/cdxiaodong/dsh-island) ⭐6 — Bridge DSH agent sessions, tool calls, and approvals to the CodeIsland macOS notch panel over a Unix socket, with in-panel allow/deny. (✅ active)
- [dsh-ohos-patch](https://github.com/shenjackyuanjie/dsh-ohos-patch) ⭐6 — 让deepseek harness能在 ohos上跑！ (✅ active)
- [dsh-plugin-anydoc](https://github.com/beancookie/dsh-plugin-anydoc) ⭐6 — Convert Word, PPT, Excel, PDF, EPUB and CSV documents to GitHub-Flavored Markdown via @firecrawl/anydoc. (✅ active)
- [dsh-plugin-installer](https://github.com/Toukaiteio/dsh-plugin-installer) ⭐6 — Marketplace plugin that integrates DeepSeek Harness with the GitHub plugin ecosystem. (✅ active)
- [dsh-plugin-manager](https://github.com/2768651338/dsh-plugin-manager) ⭐6 — DeepSeek Harness 的图形化插件管理插件：在 设置 → 插件 里新增「插件管家」标签页，用中文名和说明展示每个插件是做什么的，并提供一键启停开关与内置备注编辑——启停写入全局层补丁并实时热生效，备注保存到本地覆盖文件长期生效。 (✅ active)
- [dsh-restart](https://github.com/anweat/dsh-restart) ⭐6 — Restart DSH: configurable restart method (Node native / legacy PowerShell), post-restart continue prompt, optional watchdog auto-relaunch. (✅ active)
- [dsh-tdai-memory](https://github.com/Scorp1o117/dsh-tdai-memory) ⭐6 — Agent memory for DeepSeek Harness | DeepSeek Harness 记忆插件 (✅ active)
- [dsh-web-search-exa](https://github.com/TonyDua/dsh-web-search-exa) ⭐6 — Zero-config Exa web search provider: keyless anonymous MCP fallback plus keyed REST search. (✅ active)
- [dsh-calculator](https://github.com/bobcat848/dsh-calculator) ⭐5 — Calculate the real-time cost of DeepSeek API calls made by DeepSeek Harness. (✅ active)
- [dsh-cost-plugin](https://github.com/RoxsLee/dsh-cost-plugin) ⭐5 — DSH 费用/余额读数插件：在输入框统计行旁实时显示「本次 ≈¥x · 会话 ≈¥x · 余额 ¥x」，内置 DeepSeek 官方价目表，支持 2026-08-17 起生效的峰谷定价（按节点时间戳自动选档），余额经官方 /user/balance 实时查询，失败静默降级。 (✅ active)
- [dsh-notify-windows](https://github.com/SeverusZh/dsh-notify-windows) ⭐5 — Windows notifications for DSH, zero dependencies. (✅ active)
- [dsh-session-cleaner](https://github.com/fountunt/dsh-session-cleaner) ⭐5 — 为 DeepSeek Harness 提供会话删除能力，支持侧边栏 ⋮ 菜单入口 (✅ active)
- [dsh-split-panes](https://github.com/lehhair/dsh-split-panes) ⭐5 — Split panes. (✅ active)
- [dsh-status-bar](https://github.com/Starlight-bananice/dsh-status-bar) ⭐5 — Know what your agent is doing at a glance — 17-segment configurable status bar for DeepSeek Harness: status/model/context/tokens/TPS/cost/jobs. 一眼看清你的 agent 正在做什么：17 段可配置 DSH 会话状态栏。 (✅ active)
- [dsh-web-attention-badge](https://github.com/Luaphes/dsh-web-attention-badge) ⭐5 — Attention reminders for the DeepSeek Harness Web UI: frame badge, (N) tab title and whale-favicon recolor for sessions waiting for input or finished unopened. (✅ active)
- [nowledge-mem-deepseek-harness](https://github.com/nowledge-co/nowledge-mem-deepseek-harness) ⭐5 — Community plugin bundle integrating the Nowledge Mem memory service with DeepSeek Harness. (✅ active)
- [zotero-harvest](https://github.com/Fisfzy/zotero-harvest) ⭐5 — Zotero 文献采集入库插件（DSH external plugin）：多源检索（OpenAlex/arXiv/Crossref/Europe PMC/Semantic Scholar）+ OA 下载链接解析（Unpaywall）+ 充分性审计 + 入库本地 Zotero + 触发 zotero-wave-rag 重建 (✅ active)
- [codex-eyes-hands](https://github.com/651002/codex-eyes-hands) ⭐4 — 专为 DeepSeek Harness 打造：把本机 Codex CLI 变成纯文本 AI agent 的眼睛和手——看图/读文件/画图/监督执行/双通道容灾 (✅ active)
- [dsh-approval-gate](https://github.com/moon09300731/dsh-approval-gate) ⭐4 — Risk-gated approval automation for DeepSeek Harness: flash pre-classifies whether a write/command is irreversible — safe operations are auto-approved, dangerous ones are escalated to human approval (fail-safe). (✅ active)
- [dsh-auxiliary](https://github.com/dsh-plugins/dsh-auxiliary) ⭐4 — Auxiliary models for DeepSeek Harness: vision understanding and context compression through dedicated model routes. DeepSeek Harness 辅助模型插件：为视觉理解、上下文压缩、审批审查、子代理、会话标题与图片生成提供独立的模型路由、工具与系统提示，全程不触碰主对话模型。 (✅ active)
- [dsh-deepseek-quota](https://github.com/yingjunnan/dsh-deepseek-quota) ⭐4 — DeepSeek API quota (balance) widget for the DSH web GUI: a floating bottom-right card showing remaining DeepSeek API balance. (✅ active)
- [dsh-ffmpeg](https://github.com/STARDUSTLC666/dsh-ffmpeg) ⭐4 — DeepSeek Harness 视频处理插件：ffmpeg_probe/cut/concat/encode/subtitle/extract/gif 七工具，走官方 subprocess 服务、argv 数组无 shell 注入、零运行时依赖；纯 Node 全平台。· Video processing tools for DeepSeek Harness agents. (✅ active)
- [dsh-guardian](https://github.com/cdxiaodong/dsh-guardian) ⭐4 — Agent security guardrail: intercepts and audits every tool call, requiring human confirmation on sensitive operations. (✅ active)
- [dsh-input-history](https://github.com/lhh010/dsh-input-history) ⭐4 — Terminal-style input history: Ctrl+Up/Ctrl+Down to recall and switch sent messages. (✅ active)
- [dsh-notebooks](https://github.com/havingautism/dsh-notebooks) ⭐4 — Notebooks plugin (cordis). (✅ active)
- [dsh-plugin-deepeye](https://github.com/Favio8/dsh-plugin-deepeye) ⭐4 — DeepEye vision plugin for DeepSeek Harness (DSH): image description, OCR, VQA, UI layout, and clipboard analysis. (✅ active)
- [dsh-rss](https://github.com/STARDUSTLC666/dsh-rss) ⭐4 — DeepSeek Harness RSS 订阅插件：rss_list/add/remove/fetch/check 五工具，RSS 0.9x/1.0/2.0 与 Atom 归一化解析，订阅列表持久化到 settings，proxyUrl 特殊代理支持；纯 Node 全平台。· RSS/Atom subscription tools for DeepSeek Harness agents. (✅ active)
- [dsh-skill-hub](https://github.com/cheshireez/dsh-skill-hub) ⭐4 — In-GUI skill manager for DeepSeek Harness: browse, search, toggle, inspect, diagnose and scaffold local skills from the official ctx.skills registry, plus a skill market with tracked source sync and one-click update-all. (✅ active)
- [dsh-tool-git](https://github.com/lxj808624/dsh-tool-git) ⭐4 — Structured safe Git tools: status/diff/log/branch/stage/commit/stash/show with a destructive-command guard. (✅ active)
- [dsh-verification-receipt](https://github.com/030611/dsh-verification-receipt) ⭐4 — Privacy-minimal heuristic per-turn verification summaries for DeepSeek Harness (✅ active)
- [dsh-wordbox](https://github.com/arcmosin/dsh-wordbox) ⭐4 — Persistent common-word panel beside the composer with global/project buckets and one-click insert. (✅ active)
- [dsh-workspace-search](https://github.com/tsonglew/dsh-workspace-search) ⭐4 — VS Code-style workspace keyword search: a Search tab for the Better Sidebar ecosystem. (✅ active)
- [deepseek-harness-plugin-manager](https://github.com/hrhgit/deepseek-harness-plugin-manager) ⭐3 — Web plugin manager for DeepSeek Harness (DSH): inspect, search, group, enable, and disable Cordis plugins. (✅ active)
- [dsh-agentmemory](https://github.com/elementor-i/dsh-agentmemory) ⭐3 — agentmemory for DeepSeek Harness (dsh): full memory_* tools, capture hooks, and context injection over the local REST server (✅ active)
- [dsh-calendar](https://github.com/STARDUSTLC666/dsh-calendar) ⭐3 — DeepSeek Harness 日历插件：calendar_list/create/update/delete/search 五工具，CalDAV 协议支持 Google/iCloud/Nextcloud/自定义端点，RRULE 重复事件自动展开，插件级 proxyUrl 代理，配置缺失不崩启动；纯 Node 全平台。· CalDAV calendar tools for DeepSeek Harness agents. (✅ active)
- [dsh-diagram](https://github.com/hanzhangzzz/dsh-diagram) ⭐3 — Turn articles in DeepSeek Harness into editable Excalidraw canvases. (✅ active)
- [dsh-docker](https://github.com/STARDUSTLC666/dsh-docker) ⭐3 — DeepSeek Harness 容器管理插件：docker_ps/logs/inspect/exec/manage 五工具，官方 subprocess 服务、argv 无 shell 注入、exec 审批门、零运行时依赖。· Containers for DeepSeek Harness agents. (✅ active)
- [dsh-doctor](https://github.com/astra3294/dsh-doctor) ⭐3 — Deterministic diagnostics and recovery for DeepSeek Harness (✅ active)
- [dsh-file-uploads](https://github.com/l541402398/dsh-file-uploads) ⭐3 — Upload arbitrary local files from the Web composer with pending cards, managed in Settings. (✅ active)
- [dsh-llm-inspector](https://github.com/cdxiaodong/dsh-llm-inspector) ⭐3 — Unified LLM request/response inspector: reasoning-effort tuning, external-think export, traffic & bundle analysis. (✅ active)
- [dsh-memory](https://github.com/flymysql/dsh-memory) ⭐3 — Cross-session memory vault: memory_remember / memory_recall / memory_forget tools with a Settings page. (🧪 experimental)
- [dsh-memory-evidence](https://github.com/LeslieWylie/dsh-memory-evidence) ⭐3 — Git-first memory navigation and bounded evidence tools for DeepSeek Harness. (💤 inactive)
- [dsh-plugin-meta-memory](https://github.com/YYTbit/dsh-plugin-meta-memory) ⭐3 — Structured long-term memory system for DeepSeek Harness (✅ active)
- [dsh-plugin.github.io](https://github.com/dsh-plugin/dsh-plugin.github.io) ⭐3 — DeepSeek Harness community plugin workshop and directory (✅ active)
- [dsh-plugins-raincode](https://github.com/rainforest888/dsh-plugins-raincode) ⭐3 — dsh plugin: DeepSeek Harness 的模型层 = raincode(模型池/缓存/重试) + /skills 浏览 (✅ active)
- [dsh-prompt-stash](https://github.com/Wine-Red/dsh-prompt-stash) ⭐3 — Local, per-session prompt stash for DeepSeek Harness Web | 本地、分对话的提示词输入暂存工具。写了一半的长提示词，临时需要先问一个短问题？ 同时准备多个方案，但尚未决定发哪一个？将未完成的想法放入草稿架中，准备好后再继续完成 (✅ active)
- [dsh-prompt-studio](https://github.com/Moeblack/dsh-prompt-studio) ⭐3 — Edit user and built-in system-prompt sections with live preview. (✅ active)
- [dsh-suggested-replies](https://github.com/Anionex/dsh-suggested-replies) ⭐3 — Predicted next-message candidates above the DSH Web composer, one click to fill the draft. (✅ active)
- [dsh-telemetry-redactor](https://github.com/030611/dsh-telemetry-redactor) ⭐3 — Fail-closed export-copy redaction for DeepSeek Harness session telemetry (✅ active)
- [dsh-tool-search](https://github.com/vibeinging/dsh-tool-search) ⭐3 — Per-agent on-demand tool discovery and progressive schema disclosure. (✅ active)
- [dsh-ultra-ui](https://github.com/havingautism/dsh-ultra-ui) ⭐3 — Ultra UI plugin (cordis). (✅ active)
- [dsh-usage-plugin](https://github.com/Yihong89/dsh-usage-plugin) ⭐3 — DeepSeek Harness (DSH) plugins. First: dsh-usage-report — per-session token usage & estimated cost (/usage + usage_report), priced from the DeepSeek pricing table. (✅ active)
- [dsh-vision-tools](https://github.com/moon09300731/dsh-vision-tools) ⭐3 — Full vision-capability bundle for DeepSeek Harness: a vision_understand tool (OpenAI-compatible vision APIs, free Zhipu GLM-4V-Flash by default) plus paste/drag-and-drop/button entry points for image recognition. (✅ active)
- [dsh-webbridge](https://github.com/bill9109/dsh-webbridge) ⭐3 — DSH combined with Kimi WebBridge for real browser control. (✅ active)
- [mistymoon-dsh](https://github.com/mianyoubiaoqing/MistyMoon-DSH) ⭐3 — Local-first long-term companion plugin suite for DeepSeek Harness (✅ active)
- [URL Manager](https://github.com/Piccolo123/url-manager) ⭐3 — Agent-first URL and knowledge collection system: auto-categorize, tag, full-text search and shared collections. (✅ active)
- [zotero-wave-rag](https://github.com/Fisfzy/zotero-wave-rag) ⭐3 — 面向 Zotero 论文库的浪潮式 RAG 细节检索系统 —— DSH 外部插件。移植 VCPToolBox 浪潮语义动力学思想（标签河道图传播/虫洞跳转/钟型阻尼/Ω重排），配 BM25+RRF 混合检索、claim-evidence 忠实度校验、两级增量索引 (✅ active)
- [DSH Composer Layout](https://github.com/lavapapa/dsh-composer-layout) ⭐2 — Lets you read a long answer while drafting the next detailed prompt beside it in DSH Web. (✅ active)
- [dsh-adb](https://github.com/SamXiaBing/dsh-adb) ⭐2 — ADB device & bench operations: device discovery, structured logcat (background streaming), apk install, file pull/push, dumpsys performance snapshots. (✅ active)
- [dsh-cost-meter](https://github.com/Sttrevens/dsh-cost-meter) ⭐2 — dsh plugin: per-turn USD cost badge in the Web UI (session total + per-message footer, hover breakdown) from token usage x a configurable pricing table. (✅ active)
- [dsh-memoria](https://github.com/jiayan-xu/dsh-memoria) ⭐2 — Vector + graph memory backend with namespace isolation, automatic observation, recall, importance handling and hot reload. (🧪 experimental)
- [dsh-memory (Jesse-njx)](https://github.com/Jesse-njx/dsh-memory) ⭐2 — Cited memory over DSH's lossless session log: distilled, human-auditable facts with citations. (✅ active)
- [dsh-pin-recall](https://github.com/kerwin2046/dsh-pin-recall) ⭐2 — Pin assistant replies from the action strip and recall them into the next model turn (/pin /recall). (✅ active)
- [dsh-plugin-description](https://github.com/MysaDC/dsh-plugin-description) ⭐2 — mount one row in the composition and every plugin card on the Web Settings plugin list page gets a bilingual (zh/en) description; it also publishes the pluginDescriptions service so other plugins can register their own descriptions. (✅ active)
- [dsh-plugin-radar](https://github.com/dshplugin-me/dsh-plugin-radar) ⭐2 — Find DSH plugins by asking in plain language, then security-scan them before install (✅ active)
- [dsh-review-loop](https://github.com/wuxiangru915/dsh-review-loop) ⭐2 — Incremental diff reviewer: checkpoint-based review queue with a Web UI panel and /review command. (✅ active)
- [dsh-scout](https://github.com/omdsh-dev/dsh-scout) ⭐2 — 面向 DeepSeek Harness 的只读环境探测插件，为智能体提供运行环境、软件版本、系统资源、端口、服务、硬件及工作区信息。 (✅ active)
- [dsh-session-search](https://github.com/Tieboyh/dsh-session-search) ⭐2 — Index-free cross-agent session search for DeepSeek Harness. (✅ active)
- [dsh-test-runner](https://github.com/suimi8/dsh-test-runner) ⭐2 — Structured test runner tool: auto-detect vitest/jest/pytest/node:test, run tests and parse failure summaries for the model. (✅ active)
- [dsh-turn-navigator](https://github.com/vibeinging/dsh-turn-navigator) ⭐2 — Private DSH Web turn navigation plugin (✅ active)
- [dsh-view-modes](https://github.com/NigelYao/dsh-view-modes) ⭐2 — Output modes with Verbose, Normal and Summary views plus semantic grouping for tool calls and thinking. (✅ active)
- [dsh-what-changed](https://github.com/sjh9714/dsh-what-changed) ⭐2 — Session-wide file change review in the session header. Lists every file the agent wrote this session with its hunks, counts refused writes separately from changes, and folds from a session projection rather than the on-disk log. (✅ active)
- [visual-review](https://github.com/wang-bool/visual-review) ⭐2 — Renders pasted/uploaded images inline in the DSH Web chat and gives text-only models vision: cloud multimodal API first, local Qwen3-VL fallback. (✅ active)
- [dsh-computer-use](https://github.com/xiaoheizi1212/dsh-computer-use) ⭐1 — Model-agnostic Computer Use for DSH: isolated browser, Windows native helper and third-party bridges. (✅ active)
- [dsh-doctor](https://github.com/asdf17128/dsh-doctor) ⭐1 — Find what your DeepSeek Harness (dsh) patches silently broke — dead patches, config fields dropped by whole-config replacement, unmaintained plugins. Read-only, zero deps. (✅ active)
- [dsh-humanizer](https://github.com/lynote-ai/dsh-humanizer) ⭐1 — Writing tool for the agent: removes AI-sounding patterns and clones your personal voice. 8 deterministic tools scan text, build a style fingerprint from your samples, and return rewrite briefs. (🧪 experimental)
- [dsh-news-plugin](https://github.com/canghai666x/dsh-news-plugin) ⭐1 — RSS/news ingestion returning structured title/link/source/date/summary for downstream model ranking and briefing. (✅ active)
- [dsh-payload-capture](https://github.com/Moeblack/dsh-payload-capture) ⭐1 — Captures every upstream model API payload to JSON for debugging and observability. (✅ active)
- [dsh-plugin-evaluation-standards](https://github.com/dsh-plugin-evaluation/dsh-plugin-evaluation-standards) ⭐1 — Open evaluation datasets, test cases, and metrics for DSH plugins. (✅ active)
- [dsh-plugin-manager-registry](https://github.com/Jesse-njx/dsh-plugin-manager-registry) ⭐1 — @dsh-pm/registry — discover dsh plugins by merging the awesome-dsh-plugin list, GitHub dsh-plugin-topic search, and npm keyword search into one deduped, offline-tolerant registry (the discovery engine of dsh pm) (✅ active)
- [dsh-plugin-quote-reply](https://github.com/yangYzc/dsh-plugin-quote-reply) ⭐1 — DSH plugin: select text in a conversation, then quote it into the composer or reply in a new window. / DeepSeek Harness 划词引用插件：选中文字一键引用回复或新窗口回复。 (✅ active)
- [dsh-plugin-radar](https://github.com/DshMarketPlace/dsh-plugin-radar) ⭐1 — Userscript: marks DeepSeek Harness plugins on GitHub and npm, with the install command that actually works (✅ active)
- [dsh-repo-setup](https://github.com/gongyijie85/dsh-repo-setup) ⭐1 — Read-only repo bootstrap scanner (repo_setup_scan tool): detects stack/tests/docs/git/db and recommends plugins, MCP servers and hygiene files (claude-code-setup counterpart). (✅ active)
- [dsh-turn-index](https://github.com/Simon314620/dsh-turn-index) ⭐1 — Turn-index sidebar: one entry per user turn, click to jump with scroll-spy highlighting. (✅ active)
- [dsh-voice-webspeech](https://github.com/anweat/dsh-voice-webspeech) ⭐1 — Browser Web Speech API voice input for DSH: zero server, zero keys, zero model downloads (Edge=Azure, Chrome=Google speech). (✅ active)
- [dshp](https://github.com/asdf17128/dshp) ⭐1 — Manage DeepSeek Harness profiles — list, create, clone, diff, and share a whole dsh setup as one portable file. (✅ active)
- [dsh-client-auto-retry](https://github.com/Frog755/dsh-client-auto-retry)  — Auto-resumes interrupted DSH turns: sends a queued 继续 after error/interrupted/max-tokens turn-end, with grace period, cooldown, consecutive cap, boot scan and a settings card; never switches models or providers. (✅ active)
- [dsh-deepseek-balance](https://github.com/dshiq04/dsh-deepseek-balance)  — 面向deepseek harness的余额查看插件 (✅ active)
- [dsh-evoforge](https://github.com/deepseek-harness-evoforge/dsh-evoforge)  — Evidence-driven, cache-stable extensions for DeepSeek Harness (✅ active)
- [dsh-fork-to-preset](https://github.com/bpc-oss/dsh-fork-to-preset)  — Fork any session into a different agent preset from the conversation header: a preset-picker button that creates a new child session mounted on the chosen preset, inheriting the source session completed turns. (✅ active)
- [dsh-git-branch-switcher](https://github.com/mixin-ai/dsh-git-branch-switcher)  — Session-header git branch pill: shows the workspace branch and switches it from the Web UI. (✅ active)
- [dsh-llm-local-token](https://github.com/tianxia--/dsh-llm-local-token)  — DeepSeek Harness provider routes that reuse local Codex CLI and Claude Code OAuth tokens instead of API keys. (✅ active)
- [dsh-plugin](https://github.com/dsh-plugin-dev/dsh-plugin)  — Build your own coding agent with Pi dsh-plugin (✅ active)
- [dsh-plugin-cost](https://github.com/yweilai77-dev/dsh-plugin-cost)  — Session cost estimate in the DSH Web composer dock (tokenUsage × configurable price table, one-click official-price refresh). (✅ active)
- [dsh-precedent](https://github.com/dshplugin-me/dsh-precedent)  — Evidence-backed working memory for DeepSeek Harness: a cited ledger of what already worked in this workspace, built from the session log you already have. No index, no model, no capture step. (✅ active)
- [dsh-routed-subagent](https://github.com/bpc-oss/dsh-routed-subagent)  — Run a one-shot subagent fully mounted on any agent preset from any session, with per-call model/provider override, a model-availability pre-check, and external CLI engines (codex / claude / codebuddy) with background jobs, live progress, kill, and continuable sessions. (✅ active)
- [dsh-session-cleaner-cli](https://github.com/ChenChen913/dsh-session-cleaner-cli)  — 深度清理 DeepSeek Harness (DSH) 工作区会话的离线 CLI：按工作区列出/删除/恢复会话，自动同步工作区账目与投影缓存。Offline session cleaner for DeepSeek Harness: list, delete (trash+restore) and prune ghost sessions across workspaces. (✅ active)

### Skills


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [memos](https://github.com/MemTensor/MemOS) | ⭐10,873 | Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings and DeepSeek Harness support. | ✅ active |
| 2 | [easyeda-agent](https://github.com/zhoushoujianwork/easyeda-agent) | ⭐274 | EasyEDA Pro automation: Go daemon + in-app connector + agent skill + stdio MCP server for typed schematic/PCB actions, workflow gates, and DRC. | ✅ active |
| 3 | [dsh-skill-viewer](https://github.com/Fishquito7/dsh-skill-viewer) | ⭐88 | DSH Web UI plugin: Skills settings section with hot enable/disable, delete and add. | ✅ active |
| 4 | [dsh-reverse-skill](https://github.com/dhicoc/dsh-reverse-skill) | ⭐58 | Complete reverse-skill (85 SKILL.md) as a DeepSeek Harness (dsh) Cordis plugin — reverse engineering, authorized pentesting and security research skill pack. | ✅ active |
| 5 | [dsh-science](https://github.com/biociao/dsh-science) | ⭐24 | Claude Science-style research workbench: ReAct research-loop engine (research_* tools), versioned artifacts with provenance (artifact_* tools), and 10 science skills for genomics/pathogens/bioinformatics. | ✅ active |
| 6 | [dsh-plugin-development](https://github.com/w2112515/dsh-plugin-development) | ⭐14 | Portable Agent Skill for developing and auditing DeepSeek Harness plugins, with an optional profile-installable DSH bundle adapter. | ✅ active |
| 7 | [dsh_plugin_swift_cycle](https://github.com/Solismuchengxue/dsh_plugin_swift_cycle) | ⭐14 | Swift Cycle governance skill adapter for DeepSeek Harness; user-invoked, version-pinned, and offline-verifiable. | ✅ active |
| 8 | [dsh-plugin-dev](https://github.com/omdsh-dev/dsh-plugin-dev) | ⭐13 | Field-tested plugin development playbook (skill + docs): cordis dual copies, tsconfig triplets, Windows junctions and multi-frame zstd. | ✅ active |
| 9 | [dsh-plugin-skills](https://github.com/omdsh-dev/dsh-plugin-skills) | ⭐11 | Agent skills for building and testing DeepSeek Harness plugins, from scaffolding a package to publishing. | ✅ active |
| 10 | [dsh-godot-skill](https://github.com/akira399/dsh-godot-skill) | ⭐9 | Godot Engine 4.x full-stack game development skill plugin for DSH. | ✅ active |

#### Complete list (30)

- [memos](https://github.com/MemTensor/MemOS) ⭐10,873 — Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings and DeepSeek Harness support. (✅ active)
- [easyeda-agent](https://github.com/zhoushoujianwork/easyeda-agent) ⭐274 — EasyEDA Pro automation: Go daemon + in-app connector + agent skill + stdio MCP server for typed schematic/PCB actions, workflow gates, and DRC. (✅ active)
- [dsh-skill-viewer](https://github.com/Fishquito7/dsh-skill-viewer) ⭐88 — DSH Web UI plugin: Skills settings section with hot enable/disable, delete and add. (✅ active)
- [dsh-reverse-skill](https://github.com/dhicoc/dsh-reverse-skill) ⭐58 — Complete reverse-skill (85 SKILL.md) as a DeepSeek Harness (dsh) Cordis plugin — reverse engineering, authorized pentesting and security research skill pack. (✅ active)
- [dsh-science](https://github.com/biociao/dsh-science) ⭐24 — Claude Science-style research workbench: ReAct research-loop engine (research_* tools), versioned artifacts with provenance (artifact_* tools), and 10 science skills for genomics/pathogens/bioinformatics. (✅ active)
- [dsh-plugin-development](https://github.com/w2112515/dsh-plugin-development) ⭐14 — Portable Agent Skill for developing and auditing DeepSeek Harness plugins, with an optional profile-installable DSH bundle adapter. (✅ active)
- [dsh_plugin_swift_cycle](https://github.com/Solismuchengxue/dsh_plugin_swift_cycle) ⭐14 — Swift Cycle governance skill adapter for DeepSeek Harness; user-invoked, version-pinned, and offline-verifiable. (✅ active)
- [dsh-plugin-dev](https://github.com/omdsh-dev/dsh-plugin-dev) ⭐13 — Field-tested plugin development playbook (skill + docs): cordis dual copies, tsconfig triplets, Windows junctions and multi-frame zstd. (✅ active)
- [dsh-plugin-skills](https://github.com/omdsh-dev/dsh-plugin-skills) ⭐11 — Agent skills for building and testing DeepSeek Harness plugins, from scaffolding a package to publishing. (✅ active)
- [dsh-godot-skill](https://github.com/akira399/dsh-godot-skill) ⭐9 — Godot Engine 4.x full-stack game development skill plugin for DSH. (✅ active)
- [dsh-codex-port](https://github.com/STARDUSTLC666/dsh-codex-port) ⭐8 — DeepSeek Harness 技能移植插件：把 ~/.codex 的 Codex 官方插件（186+ 个、583+ 技能）一键移植为 DSH 技能（codex_list/port/status），frontmatter 自动转换、幂等跳过。· Batch-port the Codex plugin family into DSH skills. (✅ active)
- [dsh-book2skill](https://github.com/omdsh-dev/dsh-book2skill) ⭐4 — Book-to-skill plugin: a 5-stage long task that fetches, parses, understands, generates and installs a skill. (✅ active)
- [dsh-remotion](https://github.com/STARDUSTLC666/dsh-remotion) ⭐4 — DSH 视频创作技能插件：注册 Remotion 官方移植技能（React 编程式视频，38 个规则文件），安装即用。· Remotion skill plugin for DeepSeek Harness. (✅ active)
- [dsh-ecc](https://github.com/gongyijie85/dsh-ecc) ⭐3 — 273 ECC skills (95.8% of the 227k-star operator system) ported to DSH in four batches. (✅ active)
- [dsh-find-skill](https://github.com/Moximxxx/dsh-find-skill) ⭐3 — Bridges the vercel-labs/skills ecosystem: LLM-driven skill search, install and management. (✅ active)
- [dsh-humanize](https://github.com/zevorn/dsh-humanize) ⭐3 — De-AI writing skill: rewrite agent output to sound more human. (✅ active)
- [dsh-memoryhub](https://github.com/solknight48/dsh-memoryhub) ⭐3 — MemoryHub (mh) plugin for DeepSeek Harness (dsh): auto-loads checkpoint memory on session start, adds mh_* tools and the mh skill, and a Memory tab in the web UI (✅ active)
- [dsh-skillradar](https://github.com/hellosky983/dsh-skillradar) ⭐3 — Scans session-visible skills and ranks them by relevance to the recent conversation. (✅ active)
- [dsh-web-novel-research](https://github.com/canghai666x/dsh-web-novel-research) ⭐3 — Chinese web-novel plot lookup skill: free mirror-site workflow with GBK decoding and duplicate-chapter disambiguation. (✅ active)
- [deepseek-harness-skillx](https://github.com/drowned-fish1/deepseek-harness-skillx) ⭐2 — Skill collection for DeepSeek Harness workflows. (✅ active)
- [dsh-kb-sieve](https://github.com/omdsh-dev/dsh-kb-sieve) ⭐2 — DSH knowledge-base plugin: build audit-able KB packs (references + SQLite FTS5) from md/txt/docx/pdf, deterministic retrieval (kb_query) and original-text reading (kb_read), zero-script generated skills. Apache-2.0. (✅ active)
- [dsh-ponytail](https://github.com/gongyijie85/dsh-ponytail) ⭐2 — Ponytail lazy senior dev mode: 6 skills (ponytail, ponytail-audit, ponytail-debt, ponytail-gain, ponytail-help, ponytail-review) adapted from DietrichGebert/ponytail. (✅ active)
- [dsh-review-skills](https://github.com/ben7am1n/dsh-review-skills) ⭐2 — Code review skill pack for DeepSeek Harness. (✅ active)
- [dsh-skill-pack-security](https://github.com/PerryLink/dsh-skill-pack-security) ⭐2 — Security-audit skill pack: 5 agent skills covering secret scan, dependency audit and more. (✅ active)
- [dsh-skillport](https://github.com/Jesse-njx/dsh-skillport) ⭐2 — Every skill you already have — Claude Code, Codex, Cursor, Gemini CLI — works in DSH. (✅ active)
- [mattpocock-skills-dsh](https://github.com/gongyijie85/mattpocock-skills-dsh) ⭐2 — Matt Pocock full promoted skill set (25 SKILL.md: grilling, writing-for-agents, wait-what, TDD, code review, wayfinder, ask-matt router) ported to DSH. (✅ active)
- [howto-dsh](https://github.com/dshworks/howto-dsh) ⭐1 — Verified field notes for DeepSeek Harness (dsh): traps, skills, hooks, profiles. Every claim dated against a dsh version, with source paths to re-verify. Not affiliated with DeepSeek. (✅ active)
- [mattpocock-skills-dsh-zh](https://github.com/gongyijie85/mattpocock-skills-dsh-zh) ⭐1 — Matt Pocock's 25 skills fully translated to Chinese (technical terms kept in English with glosses). (✅ active)
- [dsh-news-briefing](https://github.com/canghai666x/dsh-news-briefing)  — News briefing skill: multi-dimensional story scoring, anti-clickbait rules, content prioritization and Chinese editorial style. (✅ active)
- [mstar-workflow](https://github.com/btspoony/mstar-workflow)  — A Skill-driven Harness/Loop Engineering Workflow Agent Plugin (💤 inactive)

### Workflows & Automation


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [tongflow](https://github.com/tong-io/tongflow) | ⭐902 | TongFlow — multimodal workflow studio and engine (canvas + Python plugin engine) and dsh-tongflow, the DeepSeek Harness studio plugin | ✅ active |
| 2 | [dsh_workflow](https://github.com/omdsh-dev/dsh_workflow) | ⭐92 | 把Claude Code的UltraCode模式带给DSH，把 DSH 的一次性多 Agent 调度，升级为可生成、可保存、可治理、可观察、可恢复的 Workflow 层 | ✅ active |
| 3 | [dsh_workflow](https://github.com/icetomoyo/dsh_workflow) | ⭐92 | Brings Claude Code's UltraCode mode to DSH: upgrade one-shot multi-agent dispatch into a generatable, saveable, governable, observable, recoverable workflow layer. | ✅ active |
| 4 | [dsh-plugin-agent-workflow](https://github.com/xuanyuanzhifeng/dsh-plugin-agent-workflow) | ⭐78 | DeepSeek Harness Agent Workflow | ✅ active |
| 5 | [dsh-automation](https://github.com/titanwings/dsh-automation) | ⭐70 | Run coding tasks on a schedule in fresh Agent sessions, managed by the user or the agent itself. | ✅ active |
| 6 | [mstar-harness](https://github.com/btspoony/mstar-harness) | ⭐52 | Skill-driven harness/loop engineering workflow agent: tune agent loops as a first-class workflow. | ✅ active |
| 7 | [dsh-plans](https://github.com/Optim-Agent/dsh-plans) | ⭐42 | Human-in-the-loop planning preset adapted from prime-plans: researched, reviewed, executed. | ✅ active |
| 8 | [dsh-auto-continue](https://github.com/HsiangNianian/dsh-auto-continue) | ⭐33 | Auto-resumes interrupted DSH Web requests: failure classification, adaptive retry, configurable continue message and browser notifications. | ✅ active |
| 9 | [dsh-deep-research](https://github.com/omdsh-dev/dsh-deep-research) | ⭐18 | Adaptive deep-research orchestrator built on the official workflow engine. | ✅ active |
| 10 | [dsh-harness-ops](https://github.com/fakechris/dsh-harness-ops) | ⭐11 | Ops toolbox: A/B dual-slot daily snapshot rotation with atomic switch and one-click rollback, plus a 10s watchdog. | ✅ active |

#### Complete list (26)

- [tongflow](https://github.com/tong-io/tongflow) ⭐902 — TongFlow — multimodal workflow studio and engine (canvas + Python plugin engine) and dsh-tongflow, the DeepSeek Harness studio plugin (✅ active)
- [dsh_workflow](https://github.com/omdsh-dev/dsh_workflow) ⭐92 — 把Claude Code的UltraCode模式带给DSH，把 DSH 的一次性多 Agent 调度，升级为可生成、可保存、可治理、可观察、可恢复的 Workflow 层 (✅ active)
- [dsh_workflow](https://github.com/icetomoyo/dsh_workflow) ⭐92 — Brings Claude Code's UltraCode mode to DSH: upgrade one-shot multi-agent dispatch into a generatable, saveable, governable, observable, recoverable workflow layer. (✅ active)
- [dsh-plugin-agent-workflow](https://github.com/xuanyuanzhifeng/dsh-plugin-agent-workflow) ⭐78 — DeepSeek Harness Agent Workflow (✅ active)
- [dsh-automation](https://github.com/titanwings/dsh-automation) ⭐70 — Run coding tasks on a schedule in fresh Agent sessions, managed by the user or the agent itself. (✅ active)
- [mstar-harness](https://github.com/btspoony/mstar-harness) ⭐52 — Skill-driven harness/loop engineering workflow agent: tune agent loops as a first-class workflow. (✅ active)
- [dsh-plans](https://github.com/Optim-Agent/dsh-plans) ⭐42 — Human-in-the-loop planning preset adapted from prime-plans: researched, reviewed, executed. (✅ active)
- [dsh-auto-continue](https://github.com/HsiangNianian/dsh-auto-continue) ⭐33 — Auto-resumes interrupted DSH Web requests: failure classification, adaptive retry, configurable continue message and browser notifications. (✅ active)
- [dsh-deep-research](https://github.com/omdsh-dev/dsh-deep-research) ⭐18 — Adaptive deep-research orchestrator built on the official workflow engine. (✅ active)
- [dsh-harness-ops](https://github.com/fakechris/dsh-harness-ops) ⭐11 — Ops toolbox: A/B dual-slot daily snapshot rotation with atomic switch and one-click rollback, plus a 10s watchdog. (✅ active)
- [dsh-deepresearch](https://github.com/havingautism/dsh-deepresearch) ⭐9 — DeepResearch plugin (cordis) for the Harness. (🧪 experimental)
- [dsh-inspect](https://github.com/omdsh-dev/dsh-inspect) ⭐6 — Adversarial checkup → fix → review loop built on the official workflow engine. (✅ active)
- [dsh-plugin-spur](https://github.com/HuanLinOTO/dsh-plugin-spur) ⭐6 — Hang a whip in the chat stream: flick it (>2.0 px/ms) to send the agent a 'go work' message. (✅ active)
- [dsh-task-dag](https://github.com/LeemanCheung/dsh-task-dag) ⭐6 — Persistent live DAG visualization of workflow runs, subagents, status and dependencies. (✅ active)
- [dsh-track](https://github.com/fakechris/dsh-track) ⭐6 — Embedded task-management engine: decision-point protocol, thought-capture wall and Linear-style issue storage. (✅ active)
- [engineer-software](https://github.com/KirschBluteX/engineer-software) ⭐6 — Runtime-neutral, evidence-driven software engineering workflow for Codex and DeepSeek Harness. (✅ active)
- [dsh-companion](https://github.com/william-jin-cmu/dsh-companion) ⭐5 — Resident desktop assistant: global hotkey, scheduled automation, quick replies and a plugin market. (💤 inactive)
- [dsh-continual-harness](https://github.com/jasen215/dsh-continual-harness) ⭐4 — DeepSeek Harness plugin for continual self-evolution: persistent memory, periodic review-and-refine, cross-session shared knowledge, and automatic rollback — a plan→validate→apply→rollback loop driven by a model-callable harness_refine tool. (✅ active)
- [dsh-doublecheck](https://github.com/PerryLink/dsh-doublecheck) ⭐4 — Engineering-discipline loop: requirement grilling before edits, red/green test-evidence gates and adversarial delivery review. (✅ active)
- [dsh-prime-agent](https://github.com/yoke233/dsh-prime-agent) ⭐4 — Prime Agent-inspired persistent RLM control plane for DSH Code Mode. (✅ active)
- [dsh-agent-orchestration](https://github.com/LeslieWylie/dsh-agent-orchestration) ⭐3 — Evidence-first multi-agent workflow planning, handoff validation, and Loop Guard skills for DeepSeek Harness. (💤 inactive)
- [dsh-eval](https://github.com/hccccc01333/dsh-eval) ⭐1 — Agent evaluation platform: benchmark YAML, headless dsh runs, trace-based metrics, scripted grading and run comparison. (✅ active)
- [dsh-governance](https://github.com/tappass/dsh-governance) ⭐1 — Authority layer for agentic AI as a DSH plugin: governs every tool call against your policies. (✅ active)
- [dsh-report-studio](https://github.com/ciceroyang/dsh-report-studio) ⭐1 — Turn a DSH session into deliverable work reports (daily/weekly/handoff/article) with verifiable receipts. (✅ active)
- [dsh-trajectory-debug](https://github.com/devmom/dsh-trajectory-debug) ⭐1 — Trajectory waterfall, deterministic replay, breakpoints, edit-and-rerun, fork compare and performance analytics. (✅ active)
- [dsh-plugin-skill](https://github.com/dsh-io/dsh-plugin-skill)  — Agent skill (SKILL.md) for creating DeepSeek Harness (dsh) plugins: authoritative defineTool API, schema rules, project layout and workflow — works with Claude Code, Codex, Cursor, Gemini CLI, opencode (✅ active)

### Agents & Multi-Agent


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [openbiliclaw](https://github.com/whiteguo233/OpenBiliClaw) | ⭐2,971 | 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin） | ✅ active |
| 2 | [dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) | ⭐746 | Multi-agent team-oriented extensions for DSH. | ✅ active |
| 3 | [dsh-agent-rp](https://github.com/hewzhew/dsh-agent-rp) | ⭐169 | SillyTavern migration and next-generation Agent roleplay for DSH. | ✅ active |
| 4 | [dsh-data-agent](https://github.com/omdsh-dev/dsh-data-agent) | ⭐104 | Session-scoped database connections with a dedicated data agent: let the model connect to databases and write SQL. | ✅ active |
| 5 | [dsh-openbiliclaw](https://github.com/whiteguo233/dsh-openbiliclaw) | ⭐48 | OpenBiliClaw 是本地运行的跨平台个性化内容推荐 Agent，持续理解你的兴趣并主动找内容。本仓库是它的 DeepSeek Harness 插件：DSH 界面常驻第四栏（推荐/内容库/对话/画像/设置），注册 22 个 Agent Bridge 工具，让 Agent 也能读推荐、答探测、闭环学习。 | ✅ active |
| 6 | [allinluna](https://github.com/zenx0x/allinluna) | ⭐41 | Resource-aware multi-agent orchestration for Codex and DeepSeek Harness (All in Flash DSH plugin). | ✅ active |
| 7 | [dsh-tianshu-build](https://github.com/huiliyi37/dsh-tianshu-build) | ⭐36 | DeepSeek X Tianshu  Harness build 是一款完全体开源 coding agent:在 dsh harness 基础之上带视觉、跨会话记忆、验证门、agent 路由、语义 + 图谱代码检索、文件回滚和全屏终端 UI——全部以插件组合。  它是 DeepSeek Harness(dsh)的友好 MIT fork, 它保留了上游一切皆插件的架构，并将以harness最佳形态和架构往下演进。 | ✅ active |
| 8 | [dsh-interconnect](https://github.com/Chinesezjc/dsh-interconnect) | ⭐34 | Cross-instance message/event handoff plugins (interconnect service + tools). | ✅ active |
| 9 | [dsh-plugin-cc](https://github.com/cpj-dev/dsh-plugin-cc) | ⭐29 | Bridge DeepSeek Harness into Claude Code for review, critique, delegation and session import. | ✅ active |
| 10 | [kixparadigm](https://github.com/olicesx/kixparadigm) | ⭐23 | kixparadigm — AI self-orchestrated minimal paradigm (resident cognition layer) + kixpower multi-agent orchestration · one-command import into DeepSeek Harness (npm i -g) / AI 自编排最小范式（认知层常驻）× kixpower 多智能体编排 · npm 一键导入 DeepSeek Harness | ✅ active |

#### Complete list (24)

- [openbiliclaw](https://github.com/whiteguo233/OpenBiliClaw) ⭐2,971 — 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin） (✅ active)
- [dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) ⭐746 — Multi-agent team-oriented extensions for DSH. (✅ active)
- [dsh-agent-rp](https://github.com/hewzhew/dsh-agent-rp) ⭐169 — SillyTavern migration and next-generation Agent roleplay for DSH. (✅ active)
- [dsh-data-agent](https://github.com/omdsh-dev/dsh-data-agent) ⭐104 — Session-scoped database connections with a dedicated data agent: let the model connect to databases and write SQL. (✅ active)
- [dsh-openbiliclaw](https://github.com/whiteguo233/dsh-openbiliclaw) ⭐48 — OpenBiliClaw 是本地运行的跨平台个性化内容推荐 Agent，持续理解你的兴趣并主动找内容。本仓库是它的 DeepSeek Harness 插件：DSH 界面常驻第四栏（推荐/内容库/对话/画像/设置），注册 22 个 Agent Bridge 工具，让 Agent 也能读推荐、答探测、闭环学习。 (✅ active)
- [allinluna](https://github.com/zenx0x/allinluna) ⭐41 — Resource-aware multi-agent orchestration for Codex and DeepSeek Harness (All in Flash DSH plugin). (✅ active)
- [dsh-tianshu-build](https://github.com/huiliyi37/dsh-tianshu-build) ⭐36 — DeepSeek X Tianshu  Harness build 是一款完全体开源 coding agent:在 dsh harness 基础之上带视觉、跨会话记忆、验证门、agent 路由、语义 + 图谱代码检索、文件回滚和全屏终端 UI——全部以插件组合。  它是 DeepSeek Harness(dsh)的友好 MIT fork, 它保留了上游一切皆插件的架构，并将以harness最佳形态和架构往下演进。 (✅ active)
- [dsh-interconnect](https://github.com/Chinesezjc/dsh-interconnect) ⭐34 — Cross-instance message/event handoff plugins (interconnect service + tools). (✅ active)
- [dsh-plugin-cc](https://github.com/cpj-dev/dsh-plugin-cc) ⭐29 — Bridge DeepSeek Harness into Claude Code for review, critique, delegation and session import. (✅ active)
- [kixparadigm](https://github.com/olicesx/kixparadigm) ⭐23 — kixparadigm — AI self-orchestrated minimal paradigm (resident cognition layer) + kixpower multi-agent orchestration · one-command import into DeepSeek Harness (npm i -g) / AI 自编排最小范式（认知层常驻）× kixpower 多智能体编排 · npm 一键导入 DeepSeek Harness (✅ active)
- [dsh-plugin-product-subagents](https://github.com/shaokeyibb/dsh-plugin-product-subagents) ⭐17 — Role-based Codex/Claude Code/ACP subagent providers: continuable children with durable state. (✅ active)
- [dsh-advisor](https://github.com/omdsh-dev/dsh-advisor) ⭐15 — Pair a second model that passively reviews each turn and injects notes. (✅ active)
- [dsh-llm-fallbacks](https://github.com/omdsh-dev/dsh-llm-fallbacks) ⭐13 — Role-based LLM retry and fallback strategy plugin. (✅ active)
- [dsh-plugin-yet-another-subagent](https://github.com/HuanLinOTO/dsh-plugin-yet-another-subagent) ⭐12 — Configurable subagent profile system: a single subagent tool with profile parameters, Web UI settings and live progress. (✅ active)
- [dsh-sidechain](https://github.com/omdsh-dev/dsh-sidechain) ⭐10 — Side sessions: persistent /side sessions (Codex style) and one-off /btw questions (Claude style) in temporary forks. (✅ active)
- [dsh-plugin-claude-bridge](https://github.com/YYTbit/dsh-plugin-claude-bridge) ⭐9 — Bridge Claude Code memory, skills and config into DeepSeek Harness. (✅ active)
- [Task Passport](https://github.com/dongsheng123132/task-passport) ⭐9 — Open task handoff protocol for DeepSeek Harness, WorkBuddy, Claude Code and Codex: verified state, not chat logs. (✅ active)
- [dsh-a2a](https://github.com/dpskh/dsh-a2a) ⭐6 — Agent2Agent mesh for the Harness. (✅ active)
- [dsh-agent-messaging](https://github.com/happyren/dsh-agent-messaging) ⭐5 — Cross-session agent-to-agent messaging: address another session by name. (✅ active)
- [dsh-crosstalk](https://github.com/Jesse-njx/dsh-crosstalk) ⭐2 — Cross-session messaging: DSH sessions on the same machine can discover, message and coordinate with each other. (✅ active)
- [dsh-slice-agent-loop](https://github.com/TT-Wang/dsh-slice-agent-loop) ⭐2 — Drop-in agent loop whose context engine is a bounded slice instead of a growing transcript. (✅ active)
- [dsh-subagent-tools](https://github.com/lynx-gt/dsh-subagent-tools) ⭐2 — Per-call model/provider/persona/toolFilter overrides for subagent delegation with @preset references. (✅ active)
- [dsh-cross-session](https://github.com/Wha1eChai/dsh-cross-session) ⭐1 — Same-runtime cross-session discovery and communication for DeepSeek Harness. (✅ active)
- [dsh-supervisor](https://github.com/Wha1eChai/dsh-supervisor) ⭐1 — Same-runtime cross-session discovery and communication for DeepSeek Harness. (✅ active)

### Clients (Desktop & TUI)


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [open-design](https://github.com/nexu-io/open-design) | ⭐90,033 | 🎨 The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode / Hermes & 20+ CLIs via BYOK. | ✅ active |
| 2 | [deepseek-harness-desktop (Anywhere Labs)](https://github.com/anywhere-labs/deepseek-harness-desktop) | ⭐17,280 | Modern desktop experience built for the DeepSeek Harness ecosystem (plugin). | ✅ active |
| 3 | [desktop-cc-gui](https://github.com/zhukunpenglinyutong/desktop-cc-gui) | ⭐4,058 | Multi-engine AI coding desktop client (Tauri). Claude Code, Codex, Gemini, OpenCode, DeepSeek Harness and more in one GUI. | ✅ active |
| 4 | [echobird](https://github.com/edison7009/EchoBird) | ⭐3,105 | One-click install + model switch:Claude Code,Codex CLI (OpenAI), Grok Build (xAI), DeepSeek Harness, Kimi Code (Moonshot) ,Qwen Code,Aider,OpenCode,MiMo Code (Xiaomi),ZCode (Z.AI),OpenClaw,Pi,OpenScience,Vibe-Trading,Claude Desktop (3P profile),ChatGPT desktop,OpenCode Desktop, | ✅ active |
| 5 | [dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) | ⭐2,249 | Claude Code-style full-screen terminal plugin: pixel-whale top bar, live status line, streaming thoughts, double-Esc rollback, context progress bar and TPS meter. | ✅ active |
| 6 | [dsh-desktop (DataElement)](https://github.com/dataelement/dsh-desktop) | ⭐1,511 | Desktop app for DeepSeek Harness. | ✅ active |
| 7 | [deepseek-harness-eac](https://github.com/zouyuxuan122/Deepseek-Harness-EAC) | ⭐1,067 | DeepSeek Harness (dsh) Windows desktop client - bundled Node.js + dsh CLI, one-click launch, 10 built-in UI skins. EAC: Embracing All Creation 揽尽万象 | ✅ active |
| 8 | [deepseek-harness-desktop (hairyf)](https://github.com/hairyf/deepseek-harness-desktop) | ⭐814 | One-click desktop app: fully local with self-healing core updates, zero environment setup. Windows/macOS/Linux. | ✅ active |
| 9 | [deepseek-harness-desktop-app](https://github.com/vibeinging/deepseek-harness-desktop-app) | ⭐610 | DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts. | ✅ active |
| 10 | [dsh-work](https://github.com/vibeinging/dsh-work) | ⭐610 | Local-first AI workbench for DSH Plugins, combining Agent sessions, project files, data analysis, web research, MCP, and Office artifacts in an Electron desktop app. | ✅ active |

#### Complete list (71)

- [open-design](https://github.com/nexu-io/open-design) ⭐90,033 — 🎨 The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode / Hermes & 20+ CLIs via BYOK. (✅ active)
- [deepseek-harness-desktop (Anywhere Labs)](https://github.com/anywhere-labs/deepseek-harness-desktop) ⭐17,280 — Modern desktop experience built for the DeepSeek Harness ecosystem (plugin). (✅ active)
- [desktop-cc-gui](https://github.com/zhukunpenglinyutong/desktop-cc-gui) ⭐4,058 — Multi-engine AI coding desktop client (Tauri). Claude Code, Codex, Gemini, OpenCode, DeepSeek Harness and more in one GUI. (✅ active)
- [echobird](https://github.com/edison7009/EchoBird) ⭐3,105 — One-click install + model switch:Claude Code,Codex CLI (OpenAI), Grok Build (xAI), DeepSeek Harness, Kimi Code (Moonshot) ,Qwen Code,Aider,OpenCode,MiMo Code (Xiaomi),ZCode (Z.AI),OpenClaw,Pi,OpenScience,Vibe-Trading,Claude Desktop (3P profile),ChatGPT desktop,OpenCode Desktop, (✅ active)
- [dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) ⭐2,249 — Claude Code-style full-screen terminal plugin: pixel-whale top bar, live status line, streaming thoughts, double-Esc rollback, context progress bar and TPS meter. (✅ active)
- [dsh-desktop (DataElement)](https://github.com/dataelement/dsh-desktop) ⭐1,511 — Desktop app for DeepSeek Harness. (✅ active)
- [deepseek-harness-eac](https://github.com/zouyuxuan122/Deepseek-Harness-EAC) ⭐1,067 — DeepSeek Harness (dsh) Windows desktop client - bundled Node.js + dsh CLI, one-click launch, 10 built-in UI skins. EAC: Embracing All Creation 揽尽万象 (✅ active)
- [deepseek-harness-desktop (hairyf)](https://github.com/hairyf/deepseek-harness-desktop) ⭐814 — One-click desktop app: fully local with self-healing core updates, zero environment setup. Windows/macOS/Linux. (✅ active)
- [deepseek-harness-desktop-app](https://github.com/vibeinging/deepseek-harness-desktop-app) ⭐610 — DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts. (✅ active)
- [dsh-work](https://github.com/vibeinging/dsh-work) ⭐610 — Local-first AI workbench for DSH Plugins, combining Agent sessions, project files, data analysis, web research, MCP, and Office artifacts in an Electron desktop app. (✅ active)
- [dsh_desktop](https://github.com/myYangyunfan/dsh_desktop) ⭐521 — DeepSeek Harness (dsh) Windows desktop client - bundled Node.js + dsh CLI, one-click launch (✅ active)
- [deepseek-harness-studio](https://github.com/fufankeji/deepseek-harness-studio) ⭐426 — DeepSeek Harness 零代码桌面端｜一键启动，支持 Windows 与 macOS；内置插件发现、热点插件推送、一键安装与管理、AI 智能推荐和视觉增强。 (✅ active)
- [ai-novel-writer](https://github.com/EthanYoQ/AI-Novel-Writer) ⭐422 — 本地优先 AI 小说创作工作台，提供 Windows/macOS 桌面版与 DeepSeek Harness 插件开发预览，支持角色、大纲、章节蓝图、审稿修稿和本地模型。 (✅ active)
- [oh-dsh](https://github.com/hust-open-atom-club/oh-dsh) ⭐256 — One-stop community distribution: TUI, desktop and Web UI in a unified experience with layered installation. (✅ active)
- [dsh-tianshu-tui](https://github.com/huiliyi37/dsh-tianshu-tui) ⭐226 — Interactive terminal UI plugin for DSH with added TDD, evidence gates and vision modules. (✅ active)
- [dsh-launcher](https://github.com/Ruler4396/dsh-launcher) ⭐165 — Lightweight Windows launcher: silent autostart at logon plus a minimal WebView2 window. (✅ active)
- [deepseek-harness-desktop (ningbainb)](https://github.com/ningbainb/deepseek-harness-desktop) ⭐157 — Lossless Windows desktop app with the complete DSH Web UI, plugins, skins and skill dock. (✅ active)
- [deepseek-harness-desktop (steven-kid)](https://github.com/steven-kid/deepseek-harness-desktop) ⭐157 — Minimal cross-platform desktop wrapper: no config, out of the box. (✅ active)
- [deepseek-harness-desktop (salathleizhang)](https://github.com/salathleizhang/deepseek-harness-desktop) ⭐138 — Desktop wrapper for DeepSeek Harness. (✅ active)
- [Deepseek-Harness-Desktop (ChisaAlter)](https://github.com/ChisaAlter/Deepseek-Harness-Desktop) ⭐131 — Electron desktop shell with theme and background-image customization. (✅ active)
- [dshcode](https://github.com/whitelonng/dshcode) ⭐126 — Community desktop companion for DeepSeek Harness — one-click Electron app for macOS and Windows (✅ active)
- [dsh-launcher](https://github.com/MarcoG-h/DSH-Launcher) ⭐125 — 最全面的DeepSeek Harness🐋桌面启动器&第三方插件管理   | 离线部署 | 一键启动 | 插件管理 | API切换 | (✅ active)
- [dsh-mobile](https://github.com/saya-ch/dsh-mobile) ⭐79 — DeepSeek Harness 移动端适配与安全局域网访问插件，支持 Android App 和手机浏览器。 (✅ active)
- [DeepSeekHarnessDesktop (wess09)](https://github.com/wess09/DeepSeekHarnessDesktop) ⭐66 — Desktop packaging for DeepSeek Harness. (✅ active)
- [dsh-desktop (bruc3van)](https://github.com/bruc3van/dsh-desktop) ⭐66 — Third-party desktop client loading the official Web UI: reuses a running official instance or a bundled dsh runtime. (✅ active)
- [dsh-multica-runtime](https://github.com/multica-ai/dsh-multica-runtime) ⭐53 — Support the dsh runtime on Multica. (✅ active)
- [beauticode](https://github.com/starsstreaming/beautiCode) ⭐51 — 面向 AI 编程客户端的动态、可响应环境——视频背景、氛围场景与主题，适用于 DeepSeek Harness 与 Codex Desktop。 (✅ active)
- [deepseek-harness-desktop (xiincs)](https://github.com/xiincs/deepseek-harness-desktop) ⭐49 — Native desktop built on Tauri 2 with bundled Node.js runtime, tray residency and auto-update. (✅ active)
- [DeepSeek Harness TUI (openma-ai)](https://github.com/openma-ai/deepseek-harness-tui) ⭐46 — Rust/Ratatui terminal client speaking the DSH SDK JSON-RPC protocol directly; runs standalone or as a profile bundle. (✅ active)
- [dsh-plugin-dev-skills](https://github.com/zimodzh/dsh-plugin-dev-skills) ⭐38 — An Agent Skills skill for developing DeepSeek Harness (DSH) plugins（开发 DSH 插件的 Agent Skill）——插件/服务/事件/工具/LLM 适配器/打包安装的标准。Works with Claude Code, Codex, DSH, VS Code Copilot & any compatible agent. (✅ active)
- [deepseek-harness-desktop (hongfeiyucode)](https://github.com/hongfeiyucode/deepseek-harness-desktop) ⭐37 — Desktop wrapper for DeepSeek Harness. (✅ active)
- [deepseek-harness-termux](https://github.com/Vengisk/deepseek-harness-termux) ⭐37 — Run @deepseek-ai/dsh on Android/Termux. (✅ active)
- [dsh-usage-plugin](https://github.com/feiyang-dev/dsh-usage-plugin) ⭐33 — DeepSeek Harness 用量与消耗插件（dsh-usage）—— 每次调用的 token 用量/缓存命中统计、峰谷计费、余额查询、CSV/JSON/PNG 导出，可经桌面端一键安装或命令行 dsh plugin add 安装。 (✅ active)
- [deepseek-harness-app (ipfred)](https://github.com/ipfred/deepseek-harness-app) ⭐29 — Desktop app for DeepSeek Harness. (✅ active)
- [dsh-plugin-session-delete](https://github.com/lsz-asd/dsh-plugin-session-delete) ⭐26 — Delete DeepSeek Harness sessions from the UI: header danger button + sidebar session-row menu item (no conversation jump), risk-consent dialog with session name/id, stops running agents first, in-place list refresh without page reload. Works in web and the desktop client. (✅ active)
- [dsh-tui](https://github.com/dsh-tui/dsh-tui) ⭐24 — Claude Code-style terminal UI for DeepSeek Harness agents, as an out-of-tree dsh plugin bundle (✅ active)
- [dsh-mobile](https://github.com/lehhair/dsh-mobile) ⭐21 — Mobile client plugin (cordis + dsh.plugin.json). (✅ active)
- [deepseek-harness-desktop (cc1252)](https://github.com/cc1252/deepseek-harness-desktop) ⭐19 — Unofficial open-source Windows Electron wrapper for DeepSeek Harness. (✅ active)
- [DeepSeek-Harness-Desktop (sleep2agi)](https://github.com/sleep2agi/DeepSeek-Harness-Desktop) ⭐19 — Unofficial community desktop shell for the public dsh runtime. (✅ active)
- [deepseek-harness-fnos](https://github.com/techysy/deepseek-harness-fnos) ⭐18 — DeepSeek Harness (DeepSeek 官方 agent 浏览器 UI) fnOS 应用 — 本地常驻服务, 官方统一网关接入 (✅ active)
- [dsh-melody-launcher](https://github.com/rirko/dsh-melody-launcher) ⭐16 — dsh-旋律启动器：DeepSeek Harness 桌面启动器与插件管理器 (✅ active)
- [dshcockpit](https://github.com/Lxiayu/DshCockpit) ⭐16 — DshCockpit — DeepSeek Harness 桌面驾驶舱 (desktop cockpit)：运行时自动更新、成本控制、全局快捷问询、定时任务、会话全文检索、数据安全。自动更新 / 成本中心 / Quick Ask / 定时任务 / 会话搜索 (✅ active)
- [dsh-mobile-for-android](https://github.com/Hongtwenfive1226/DSH-Mobile-for-Android) ⭐12 — The Android mobile version of DeepSeek Harness that relies on Tailscale. (✅ active)
- [dsh-grok-tui](https://github.com/chen-001/dsh-grok-tui) ⭐11 — TUI built with grok-build. (✅ active)
- [awesome-deepseek-harness-desktop (ADHD)](https://github.com/omdsh-dev/awesome-deepseek-harness-desktop) ⭐10 — ADHD — out-of-the-box Electron desktop wrapper for DeepSeek Harness. (✅ active)
- [deepseek-harness-desktop](https://github.com/qyqy-1109/deepseek-harness-desktop) ⭐10 — DeepSeek Harness Desktop: self-contained Windows desktop shell (Electron) that auto-starts dsh web, plus a subtle Codex-flavored theme plugin. (✅ active)
- [deepseek-harness-desktop (chyra-moon)](https://github.com/chyra-moon/deepseek-harness-desktop) ⭐10 — Native Windows desktop shell: 1:1 official web UI with embedded server, tray and auto-recovery. (✅ active)
- [deepseek-harness-tui (boxeryao)](https://github.com/boxeryao/deepseek-harness-tui) ⭐10 — Lightweight fast terminal plugin connected directly to the DSH runtime. (✅ active)
- [dsh-desktop](https://github.com/foolgry/dsh-desktop) ⭐10 — Download-and-run desktop build of DeepSeek Harness — Electron shell with embedded Node, no npm required. (✅ active)
- [agentpocket](https://github.com/npu-chenlin/AgentPocket) ⭐9 — Android 客户端：通过 Tailscale 在手机上使用 Kimi Code / DeepSeek Harness 等编码 Agent 的 Web 服务 (✅ active)
- [deepseek-harness-desktop](https://github.com/baiyuscc13724-max/deepseek-harness-desktop) ⭐9 — Windows desktop app for DeepSeek Harness: installer, themes, in-app plugin marketplace, model routing, and updates. (✅ active)
- [deepseek-harness-desktop](https://github.com/omdsh-dev/deepseek-harness-desktop) ⭐8 — DSH 桌面应用打包器 (✅ active)
- [deepseek-harness-desktop](https://github.com/RZX00/deepseek-harness-desktop) ⭐7 — DeepSeek Harness with a Windows desktop build: an Electron shell over the dsh web profile, packaged as an installer (✅ active)
- [deepseek-harness-tui (gxinxing)](https://github.com/gxinxing/deepseek-harness-tui) ⭐7 — Terminal-native interactive TUI built with Ink (React for terminals). (✅ active)
- [star-deepseek-harness-desktop](https://github.com/dabaicai001/star-deepseek-harness-desktop) ⭐7 — Star-deepseek-harness-desktop — DeepSeek Harness,一站式桌面运维台。Harness 自动规划并调用数据库 / SSH / SFTP / Docker 执行。本地优先、跨平台。本项目由自研的starhub 做的再次改进，现在改进中... 尽情期待吧，如果想使用老版本可以下载 0.6X.X 版本 (✅ active)
- [deepseek-harness-cli](https://github.com/Richard-Yang0130/deepseek-harness-cli) ⭐6 — Claude Code-style terminal interface for DeepSeek Harness (✅ active)
- [deepseek-harness-desktop](https://github.com/HaoyueQin/deepseek-harness-desktop) ⭐6 — A desktop shell for DeepSeek Harness — the pluggable AI agent harness from DeepSeek. Wrap the official dsh web UI into a native-feeling, always-on desktop app. / 为 DeepSeek Harness（DeepSeek 开源的可插拔 AI Agent harness）打造的桌面应用壳，把官方 dsh web 界面包装成原生质感、常驻后台的桌面应用。 (✅ active)
- [dsh-desk-pet](https://github.com/anneheartrecord/dsh-desk-pet) ⭐5 — Always-on-top DeepSeek Harness desktop pet. Default whale, four skins, four silent states. (✅ active)
- [dsh-desktop-electron](https://github.com/Void0312Aurora/dsh-desktop-electron) ⭐5 — Cross-platform Electron shell for the DSH Web GUI: tray-resident standalone window. (✅ active)
- [deepseek-harness-for-android](https://github.com/standtrain/deepseek-harness-for-android) ⭐4 — 该程序是一个独立的 Capacitor Android 应用，用于管理本机 DeepSeek Harness Ubuntu 用户空间。它提供运行时安装与重置、Ubuntu 终端、可选的 Shizuku 设备 Shell 访问、设置，以及仅限回环地址的内嵌 Harness Web 界面。 (✅ active)
- [dsh-closerai](https://github.com/sb1733831438-maker/DSH-closerAI) ⭐4 — CloserAI - a local-first, model-agnostic, permission-transparent desktop AI workbench built on DeepSeek Harness. (✅ active)
- [dsh-launcher-android](https://github.com/qawse110/dsh-launcher-android) ⭐4 — DshLauncher: single-APK Android launcher for DeepSeek Harness with embedded Node runtime (✅ active)
- [deepseek-harness-desktop](https://github.com/Easyhoov/deepseek-harness-desktop-windows) ⭐3 — Unofficial in-process desktop app for DeepSeek Harness: the host composition boots inside the Electron main process with zero ports and an IPC bridge. Not affiliated with DeepSeek. (✅ active)
- [deepseek-harness-workbench](https://github.com/xuan-ao-1/deepseek-harness-workbench) ⭐3 — DeepSeek Harness 官方架构的 Windows 桌面发行版 (Desktop distribution of the official DeepSeek Harness) (✅ active)
- [dsh-vault](https://github.com/feiyang-dev/dsh-vault) ⭐3 — DeepSeek Harness 数据保险箱插件（dsh-vault）—— 自动备份、清空检测、一键恢复，保护聊天记录与工作区数据；可经桌面端一键安装或命令行 dsh plugin add 安装。 (✅ active)
- [dsh-pi-tui](https://github.com/lqhl/dsh-pi-tui) ⭐2 — Pi TUI front end: streaming markdown, thinking collapse, tool cards, slash commands and approval overlays. (✅ active)
- [dsh-portable-launcher](https://github.com/15828148/dsh-portable-launcher) ⭐2 — One-click portable launcher for DeepSeek Harness (dsh) Web UI on Windows. Auto-installs Node.js and dsh with China mirror fallback, 3-stage progress with retries and resume, zero-download fast path when ready. No admin needed. (✅ active)
- [dsh-desktop](https://github.com/xiaowei2025cqu23phy/dsh-desktop) ⭐1 — Desktop client for DeepSeek Harness: AI screensaver, phone PWA remote control (LAN pairing), QQ/Telegram bot channels with approval/question buttons, mode prompts (assistant/friend), wallpapers and more. (✅ active)
- [dsh-desktop-launcher](https://github.com/becomeless/dsh-desktop-launcher)  — Windows/macOS desktop launcher for DeepSeek Harness: double-click to launch, zero console windows, auto-stop on close | 双击图标一键启动 DeepSeek Harness 的桌面启动器（Windows / macOS） (✅ active)
- [dsh-quickstart](https://github.com/qzhqzh/dsh-quickstart)  — Desktop launcher for DeepSeek Harness - start dsh web with no console window and auto-open the browser. Tested on Windows; macOS/Linux in progress. (✅ active)
- [dsh-start](https://github.com/zhengjy01/dsh-start)  — One-click start/stop launcher for the DSH Web GUI on macOS: foreground/daemon start, stop, status, duplicate-launch guard, auto browser open, plus a Dock-able DSH.app built by script. (✅ active)

### MCP & Integrations


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [Coding Tools MCP](https://github.com/xyTom/coding-tools-mcp) | ⭐846 | Coding-oriented MCP tool collection that appears in the emerging DSH ecosystem: give any AI agent the ability to code. | ✅ active |
| 2 | [memtrace-public](https://github.com/syncable-dev/memtrace-public) | ⭐459 | Structural memory for AI coding agents. Bi-temporal graph, MCP-native, zero LLM calls. Cursor · Claude Code · Codex · DeepSeek Harness · Hermes · VS Code · Windsurf. | ✅ active |
| 3 | [dsh-openpencil](https://github.com/ZSeven-W/dsh-openpencil) | ⭐135 | OpenPencil design preview and editing integration. | ✅ active |
| 4 | [dsh-super-injector](https://github.com/yjh051108/dsh-super-injector) | ⭐133 | Super-injector plugin (cordis) for context injection. | ✅ active |
| 5 | [dsh-qqbot](https://github.com/tencent-connect/dsh-qqbot) | ⭐70 | 让 QQ 机器人接入 DeepSeek Harness（dsh）的官方插件 | ✅ active |
| 6 | [dsh-lark](https://github.com/omdsh-dev/dsh-lark) | ⭐41 | Lark/Feishu IM bot channel for DeepSeek Harness | 飞书 DeepSeek Harness 插件 | ✅ active |
| 7 | [deepseek-harness-docker](https://github.com/runzhliu/deepseek-harness-docker) | ⭐27 | Community Docker and Kubernetes packaging for @deepseek-ai/dsh with a hardened image. | ✅ active |
| 8 | [dsh-mcp-panel](https://github.com/PerryLink/dsh-mcp-panel) | ⭐26 | Read-only runtime management panel for the official DSH MCP client: /mcp command and a Settings tab. | ✅ active |
| 9 | [deepseek-harness-vsc-extension](https://github.com/weinibuliu/deepseek-harness-vsc-extension) | ⭐24 | DeepSeek Harness for VS Code as extension | 💤 inactive |
| 10 | [dsh-ide](https://github.com/chenw2759-wq/dsh-IDE) | ⭐24 | dsh-IDE 把 DeepSeek Harness（DSH）网页版升级成一站式 IDE：JupyterLab 式文件树、带语法高亮的代码编辑、多格式预览、Trae 风格红绿 diff 和内置终端，再加上「本地大脑、远程手脚」的 SSH 远程工作区，让 AI 直接在本机操控远程服务器，全程零配置文件改动。 | ✅ active |

#### Complete list (50)

- [Coding Tools MCP](https://github.com/xyTom/coding-tools-mcp) ⭐846 — Coding-oriented MCP tool collection that appears in the emerging DSH ecosystem: give any AI agent the ability to code. (✅ active)
- [memtrace-public](https://github.com/syncable-dev/memtrace-public) ⭐459 — Structural memory for AI coding agents. Bi-temporal graph, MCP-native, zero LLM calls. Cursor · Claude Code · Codex · DeepSeek Harness · Hermes · VS Code · Windsurf. (✅ active)
- [dsh-openpencil](https://github.com/ZSeven-W/dsh-openpencil) ⭐135 — OpenPencil design preview and editing integration. (✅ active)
- [dsh-super-injector](https://github.com/yjh051108/dsh-super-injector) ⭐133 — Super-injector plugin (cordis) for context injection. (✅ active)
- [dsh-qqbot](https://github.com/tencent-connect/dsh-qqbot) ⭐70 — 让 QQ 机器人接入 DeepSeek Harness（dsh）的官方插件 (✅ active)
- [dsh-lark](https://github.com/omdsh-dev/dsh-lark) ⭐41 — Lark/Feishu IM bot channel for DeepSeek Harness | 飞书 DeepSeek Harness 插件 (✅ active)
- [deepseek-harness-docker](https://github.com/runzhliu/deepseek-harness-docker) ⭐27 — Community Docker and Kubernetes packaging for @deepseek-ai/dsh with a hardened image. (✅ active)
- [dsh-mcp-panel](https://github.com/PerryLink/dsh-mcp-panel) ⭐26 — Read-only runtime management panel for the official DSH MCP client: /mcp command and a Settings tab. (✅ active)
- [deepseek-harness-vsc-extension](https://github.com/weinibuliu/deepseek-harness-vsc-extension) ⭐24 — DeepSeek Harness for VS Code as extension (💤 inactive)
- [dsh-ide](https://github.com/chenw2759-wq/dsh-IDE) ⭐24 — dsh-IDE 把 DeepSeek Harness（DSH）网页版升级成一站式 IDE：JupyterLab 式文件树、带语法高亮的代码编辑、多格式预览、Trae 风格红绿 diff 和内置终端，再加上「本地大脑、远程手脚」的 SSH 远程工作区，让 AI 直接在本机操控远程服务器，全程零配置文件改动。 (✅ active)
- [chatccc](https://github.com/wzj998/ChatCCC) ⭐22 — 飞书（Lark）或微信（WeChat）聊天控制 DeepSeek Harness / Claude Code / Cursor / Codex / CCC Agent (✅ active)
- [dsh-vscode](https://github.com/Lixxx1/dsh-vscode) ⭐14 — DSH Sidebar — a Claude Code/Codex-style VS Code sidebar for DeepSeek Harness. 像 Claude Code、Codex 一样，在 VS Code 侧边栏中使用 DSH。 (✅ active)
- [deepseek-harness-action](https://github.com/Lixiaoyiao/deepseek-harness-action) ⭐13 — Community GitHub Action: AI code review, CI diagnosis, auto-fix and issue-to-PR implementation. (✅ active)
- [dsh-git-graph](https://github.com/1841220388zzzcccxxx-star/dsh-git-graph) ⭐13 — Embedded git repository graph visualizer for the DeepSeek Harness Web GUI | 嵌入式 Git 仓库图谱可视化插件（提交历史图 / 分支过滤 / 文件 diff / VSCode 式未提交改动） (✅ active)
- [deepseek-harness-acp](https://github.com/openma-ai/deepseek-harness-acp) ⭐12 — ACP server implementation for DeepSeek Harness: exposes the full DSH agent to ACP clients while reusing credentials and sessions. (✅ active)
- [dsh-search-mcp](https://github.com/gxpppp/dsh-search-mcp) ⭐12 — Replace DSH's built-in web search with search MCP servers (Tavily/Brave/Exa/Perplexity/DuckDuckGo). (✅ active)
- [dsh-vision-proxy](https://github.com/Flyvhidbwo/dsh-vision-proxy) ⭐12 — DeepSeek Harness 插件：DeepSeek 大脑 + 自动识图。GUI 附加图片自动经 OpenAI 兼容 VLM 转译成文字后交给 DeepSeek 作答；支持百炼/智谱/OpenRouter 等任意 OpenAI 兼容端点（默认 qwen3.7-flash），无 key 自动探测本地 Ollama（图片不出本机）；安装时有一问式确认 (✅ active)
- [ikanban](https://github.com/isomoes/ikanban) ⭐12 — Monorepo for the iKanban browser-surface fork for DeepSeek Harness. (✅ active)
- [dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) ⭐10 — MCP server manager: Settings page with OAuth (PKCE + dynamic client registration) or static-token auth. (✅ active)
- [deepseek-acp](https://github.com/xintaofei/deepseek-acp) ⭐9 — 把 DeepSeek Harness 接成一个面向编辑器的完整编码 Agent， 通过 Agent Client Protocol（ACP）与客户端通话。 (✅ active)
- [dsh-harness-mcp-server](https://github.com/chushixixin/dsh-harness-mcp-server) ⭐9 — Expose DeepSeek Harness agent capabilities as an MCP server (brain=Hermes, arms=Harness). (✅ active)
- [dsh-lan-access](https://github.com/Leon0555/dsh-lan-access) ⭐9 — LAN access for the Web GUI: 0.0.0.0 bind plus a crypto.randomUUID polyfill for non-secure contexts. (✅ active)
- [dsh-oauth-mcp-client](https://github.com/springbrand-lab/dsh-oauth-mcp-client) ⭐9 — OAuth 2.1 Streamable HTTP MCP client plugin for DeepSeek Harness. (✅ active)
- [dsh-browser](https://github.com/xylt369/dsh-browser) ⭐8 — Browser capability for DeepSeek Harness: headed Edge/Playwright provider, SSRF-safe navigation, a11y-ref clicking, permission gate with auto-remember, gated evaluate (✅ active)
- [dsh-telegram-channel](https://github.com/hi-wenw/dsh-telegram-channel) ⭐8 — Telegram mobile remote for live DSH Web sessions: session picker, bind/unbind, same trajectory as desktop. (✅ active)
- [telegram](https://github.com/LoserFox/telegram) ⭐7 — Telegram Bot API 桥接插件：长轮询、per-chat 会话、HTML 格式化 (✅ active)
- [DSH Telegram Relay](https://github.com/congchuanling-dot/DSH-Telegram-Relay) ⭐6 — Relay that turns Telegram into a remote conversation channel for DSH with notifications. (✅ active)
- [dsh-agentlink](https://github.com/hootandy321/dsh-Agentlink) ⭐6 — Caller-side bridge from Codex and other agent frameworks to DeepSeek Harness, with observable sessions, follow-up, cancellation, and human-gated approvals. (✅ active)
- [dsh-subscription-auth](https://github.com/Khellendros97/dsh-subscription-auth) ⭐5 — dsh对接openai、grok、anthropic、kimi订阅渠道 (✅ active)
- [dsh4vscode](https://github.com/DoggyHU/dsh4vscode) ⭐5 — VS Code chat windows backed by the DSH agent: OpenCode-style independent sessions with model auto-routing. (✅ active)
- [dsh-slack](https://github.com/STARDUSTLC666/dsh-slack) ⭐4 — DeepSeek Harness Slack 插件：slack_notify/channels/inbox/reply 四工具，Socket Mode 免公网回调收消息，收件箱队列 + 线程回复，支持自定义 slackApiUrl 对接代理网关；内置假 Slack 服务器做协议级验收测试。· Two-way Slack messaging for DeepSeek Harness agents. (✅ active)
- [kimi-tide](https://github.com/tafcear/kimi-tide) ⭐4 — 月汐 — Kimi Code (Moonshot) 接入 DeepSeek Harness 的完整方案：标准 DSH 插件 + Kimi CLI 桥接维护 fork + Agent 协作闭环方法论 (✅ active)
- [PicGo DSH Plugin](https://github.com/PicGo/dsh-plugin) ⭐4 — Official PicGo plugin: upload images/files to your image host from DSH and get public URLs. (✅ active)
- [dsh-dingtalk](https://github.com/STARDUSTLC666/dsh-dingtalk) ⭐3 — DeepSeek Harness 钉钉群机器人通知插件：dingtalk_notify/dingtalk_text 两工具，自定义机器人 webhook + HMAC 加签安全模式，手写签名实现、零运行时依赖；纯 Node 全平台。· DingTalk group-robot notifications for DeepSeek Harness agents. (✅ active)
- [dsh-mcp-manager](https://github.com/Nichts0v0/dsh-mcp-manager) ⭐3 — 在 DeepSeek Harness 设置页管理 MCP 服务器：运行时添加/编辑/启停/重连/删除，实时状态、自动重连，中英双语界面。MCP server manager for DeepSeek Harness — add, edit, enable/disable, reconnect & delete MCP servers from the web settings page, with live status and auto-reconnect. (✅ active)
- [dsh-plugin-vision](https://github.com/tdf1995/dsh-plugin-vision) ⭐3 — Vision for text-only LLMs in DeepSeek Harness (DSH): describe images / OCR / VQA via free Gemini & GLM vision APIs (✅ active)
- [dsh-subagent-cwd](https://github.com/lynx-gt/dsh-subagent-cwd) ⭐3 — DeepSeek Harness subagent delegation enhancement (✅ active)
- [dsh-watch](https://github.com/dshworks/dsh-watch) ⭐3 — Put a watch on a stream: background listeners that wake the DeepSeek Harness agent with new matching lines — and a daemon host so a watcher runs unattended for weeks, with no task and no browser. Not affiliated with DeepSeek. (✅ active)
- [shopline-ai-toolkit-dsh](https://github.com/lunw/shopline-ai-toolkit-dsh) ⭐3 — SHOPLINE AI Toolkit for DeepSeek Harness (dsh-plugin): official SHOPLINE Developer MCP bridge + SHOPLINE agent skills, mirroring the Shopify AI Toolkit architecture. dsh-plugin (✅ active)
- [vscode-deepseek-harness](https://github.com/kalynnka/vscode-deepseek-harness) ⭐3 — Unofficial: drive your own dsh as a native VS Code chat agent. (✅ active)
- [dsh-github-integration](https://github.com/omdsh-dev/dsh-github-integration) ⭐2 — GitHub integration plugin for DSH. (✅ active)
- [dsh-meow-cat](https://github.com/dsh-pub/dsh-meow-cat) ⭐2 — A cat runs across the bottom of the DeepSeek Harness web UI with a synthesized meow every time a conversation turn ends. (✅ active)
- [dsh-plugin-acn](https://github.com/acnlabs/dsh-plugin-acn) ⭐2 — DeepSeek Harness plugin: join ACN so this agent can discover, message, and collaborate with other agents. Defaults to the China region. (✅ active)
- [deepseek-harness-rs](https://github.com/Tokimorphling/deepseek-harness-rs) ⭐1 — A Rust port of DeepSeek Harness. (🧪 experimental)
- [dsh-chrome](https://github.com/YJSoooooo/dsh-chrome) ⭐1 — Chrome profile bridge: control an existing signed-in Chrome profile through Chrome DevTools Protocol. (✅ active)
- [mcp_guard](https://github.com/dshoneys/mcp_guard) ⭐1 — 本机 MCP / Agent 口扫描、监视与审计（loopback 未鉴权 tools/list、CORS）。DeepSeek Honeys. (✅ active)
- [dsh-docker](https://github.com/dshoneys/dsh-docker)  — 隔离的 DeepSeek Harness 插件安装沙箱，并对本机 MCP 口做防御性探测。 (✅ active)
- [dsh-wechat-bridge](https://github.com/lanbaolu/dsh-wechat-bridge)  — Personal WeChat bridge for DeepSeek Harness: scan QR to bind, then chat with your local DSH agent directly inside WeChat (text/image/voice/file, streamed replies, persisted sessions). (✅ active)
- [opendsh](https://github.com/TheChengXi/opendsh)  — Open the DeepSeek Harness Web UI inside VS Code with one-command start/stop. (✅ active)
- [URL Manager MCP](https://github.com/Piccolo123/url-manager-mcp)  — MCP companion for URL Manager: 21 tools for save/search/categorize/share with magic-link delivery. (✅ active)

### Examples & Starters


#### 🔥 Top 9

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [hello-dsh](https://github.com/pingfanfan/hello-dsh) | ⭐79 | Zero-to-plugin tutorial: understand 'everything is a plugin' with 22 Chinese skill examples. | ✅ active |
| 2 | [dsh-plugin-template](https://github.com/bugmaker2/dsh-plugin-template) | ⭐13 | Template for DeepSeek Harness plugin development. | ✅ active |
| 3 | [plugin-template (omdsh-dev)](https://github.com/omdsh-dev/plugin-template) | ⭐12 | Plugin template repository derived from the original turtle-ui official repo. | ✅ active |
| 4 | [turtle-ui](https://github.com/turtle1999/turtle-ui) | ⭐8 | Official UI plugin reference implementation. | ✅ active |
| 5 | [dsh-plugin-template (sunshine-lang)](https://github.com/sunshine-lang/dsh-plugin-template) | ⭐6 | Ready-to-publish plugin skeleton: bundle format, tool DSL, config and tests. | ✅ active |
| 6 | [dsh-101](https://github.com/bill9109/dsh-101) | ⭐5 | DSH documentation reading mode. | ✅ active |
| 7 | [InfiniteDSH](https://github.com/vdnight89/InfiniteDSH) | ⭐3 | 诸天万界DSH: one DSH session is one book — a cover-card picker opens 19 realms, a prose-only preset locks the model to fiction, keyword worldbook lore grounds each turn, and /export-story typesets the session into a Markdown novel. | ✅ active |
| 8 | [Living-Dream-DSH](https://github.com/alllllllllli/Living-Dream-DSH) | ⭐2 | Complete DSH desktop config framework: 8+ MCP servers, free model channels (CNB proxy, AMD Radeon Cloud), mobile remote via Tailscale, vision patches, one-click installer. | ✅ active |
| 9 | [dsh-plugin-hello](https://github.com/xu1132/dsh-plugin-hello) |  | Hello-world style starter plugin for DSH. | ✅ active |

#### Complete list (9)

- [hello-dsh](https://github.com/pingfanfan/hello-dsh) ⭐79 — Zero-to-plugin tutorial: understand 'everything is a plugin' with 22 Chinese skill examples. (✅ active)
- [dsh-plugin-template](https://github.com/bugmaker2/dsh-plugin-template) ⭐13 — Template for DeepSeek Harness plugin development. (✅ active)
- [plugin-template (omdsh-dev)](https://github.com/omdsh-dev/plugin-template) ⭐12 — Plugin template repository derived from the original turtle-ui official repo. (✅ active)
- [turtle-ui](https://github.com/turtle1999/turtle-ui) ⭐8 — Official UI plugin reference implementation. (✅ active)
- [dsh-plugin-template (sunshine-lang)](https://github.com/sunshine-lang/dsh-plugin-template) ⭐6 — Ready-to-publish plugin skeleton: bundle format, tool DSL, config and tests. (✅ active)
- [dsh-101](https://github.com/bill9109/dsh-101) ⭐5 — DSH documentation reading mode. (✅ active)
- [InfiniteDSH](https://github.com/vdnight89/InfiniteDSH) ⭐3 — 诸天万界DSH: one DSH session is one book — a cover-card picker opens 19 realms, a prose-only preset locks the model to fiction, keyword worldbook lore grounds each turn, and /export-story typesets the session into a Markdown novel. (✅ active)
- [Living-Dream-DSH](https://github.com/alllllllllli/Living-Dream-DSH) ⭐2 — Complete DSH desktop config framework: 8+ MCP servers, free model channels (CNB proxy, AMD Radeon Cloud), mobile remote via Tailscale, vision patches, one-click installer. (✅ active)
- [dsh-plugin-hello](https://github.com/xu1132/dsh-plugin-hello)  — Hello-world style starter plugin for DSH. (✅ active)

### Tutorials & Learning


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [DeepSeek Harness Orange Book](https://github.com/alchaincyf/deepseek-harness-orange-book) | ⭐1,118 | Community Orange Book: complete system prompts, a 129-line startup checklist and three raw session logs — first-hand testing the official docs lack. Free PDF/EPUB/HTML. | ✅ active |
| 2 | [dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) | ⭐604 | From 0 to 1 handbook: installation, plugin development, performance tuning, real-world cases and same-model multi-agent comparisons (CN + EN PDF). | ✅ active |
| 3 | [dshfind](https://github.com/hikariming/dshfind) | ⭐200 | Learn DSH principles, plugin marketplace and best practices — from chapter-by-chapter Cordis paper reading to an auto-aggregated plugin market. | ✅ active |
| 4 | [deepseek-harness-tutorial](https://github.com/ht426/deepseek-harness-tutorial) | ⭐182 | Detailed Chinese learning tutorial for DeepSeek Harness. | ✅ active |
| 5 | [dsh-harness-tutorial](https://github.com/yanhua1010/dsh-harness-tutorial) | ⭐54 | DeepSeek Harness Agent 的原理与实现：从零到一实现一个 AI Agent —— 一切皆插件的中文教程（VitePress 站点 + 8 个 Demo + mini-harness 教学项目） | ✅ active |
| 6 | [deepseek-harness-handbook](https://github.com/sandbaseai/deepseek-harness-handbook) | ⭐36 | Independent, source-backed handbook for DeepSeek AI's official DeepSeek Harness (dsh): agents, plugins, security, troubleshooting, and runbooks. | ✅ active |
| 7 | [dsh-explain](https://github.com/yuezengwu/dsh-explain) | ⭐11 | Local-first learning mode: cross-session global learning threads, explain-by-source, ExplainContext and compression. | ✅ active |
| 8 | [deepseek-harness-learning](https://github.com/Lucky2024-pllove/deepseek-harness-learning) | ⭐7 | Learning website built from a systematic breakdown of the deepseek-harness repository, for developers curious how AI agent frameworks work. | ✅ active |
| 9 | [deepseek-harness-prompts](https://github.com/demouo/deepseek-harness-prompts) | ⭐6 | DeepSeek Harness prompts for different modes. | ✅ active |
| 10 | [dsh-book-deepseek-harness](https://github.com/LaplaceYoung/dsh-book-deepseek-harness) | ⭐6 | 'Deep Dive into DeepSeek Harness' — source-level architecture book: 37 chapter files, PDF, Mermaid diagrams and writing conventions. | ✅ active |

#### Complete list (13)

- [DeepSeek Harness Orange Book](https://github.com/alchaincyf/deepseek-harness-orange-book) ⭐1,118 — Community Orange Book: complete system prompts, a 129-line startup checklist and three raw session logs — first-hand testing the official docs lack. Free PDF/EPUB/HTML. (✅ active)
- [dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) ⭐604 — From 0 to 1 handbook: installation, plugin development, performance tuning, real-world cases and same-model multi-agent comparisons (CN + EN PDF). (✅ active)
- [dshfind](https://github.com/hikariming/dshfind) ⭐200 — Learn DSH principles, plugin marketplace and best practices — from chapter-by-chapter Cordis paper reading to an auto-aggregated plugin market. (✅ active)
- [deepseek-harness-tutorial](https://github.com/ht426/deepseek-harness-tutorial) ⭐182 — Detailed Chinese learning tutorial for DeepSeek Harness. (✅ active)
- [dsh-harness-tutorial](https://github.com/yanhua1010/dsh-harness-tutorial) ⭐54 — DeepSeek Harness Agent 的原理与实现：从零到一实现一个 AI Agent —— 一切皆插件的中文教程（VitePress 站点 + 8 个 Demo + mini-harness 教学项目） (✅ active)
- [deepseek-harness-handbook](https://github.com/sandbaseai/deepseek-harness-handbook) ⭐36 — Independent, source-backed handbook for DeepSeek AI's official DeepSeek Harness (dsh): agents, plugins, security, troubleshooting, and runbooks. (✅ active)
- [dsh-explain](https://github.com/yuezengwu/dsh-explain) ⭐11 — Local-first learning mode: cross-session global learning threads, explain-by-source, ExplainContext and compression. (✅ active)
- [deepseek-harness-learning](https://github.com/Lucky2024-pllove/deepseek-harness-learning) ⭐7 — Learning website built from a systematic breakdown of the deepseek-harness repository, for developers curious how AI agent frameworks work. (✅ active)
- [deepseek-harness-prompts](https://github.com/demouo/deepseek-harness-prompts) ⭐6 — DeepSeek Harness prompts for different modes. (✅ active)
- [dsh-book-deepseek-harness](https://github.com/LaplaceYoung/dsh-book-deepseek-harness) ⭐6 — 'Deep Dive into DeepSeek Harness' — source-level architecture book: 37 chapter files, PDF, Mermaid diagrams and writing conventions. (✅ active)
- [dsh-learn-everything](https://github.com/cendaifeng/dsh-learn-everything) ⭐5 — Feynman learning-mode plugin: teach → teach-back → judge → re-explain loop rendered as rich HTML lesson cards. (✅ active)
- [gitlearnos](https://github.com/Guojiz/gitlearnos) ⭐4 — Git-native AI learning OS with a GitLearnOS-exclusive DeepSeek Harness panel, targeted practice, local RAG, and learner-owned memory. (✅ active)
- [deepseek-protocol-doctor](https://github.com/Whning0513/deepseek-protocol-doctor) ⭐2 — Checks DeepSeek tool loops, reasoning_content, strict schemas and captured SSE; also works as a DSH plugin. (✅ active)

### Awesome Lists & Registries


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [awesome-deepseek-integration](https://github.com/deepseek-ai/awesome-deepseek-integration) | ⭐38,897 | Integrate the DeepSeek API into popular software | ✅ active |
| 2 | [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | ⭐11,012 | Large curated list of installable DSH plugins (bilingual). | ✅ active |
| 3 | [awesome-deepseek-agent (official)](https://github.com/deepseek-ai/awesome-deepseek-agent) | ⭐5,966 | Official curated guides for integrating DeepSeek models into agent/coding-assistant tools (AstrBot, Cherry Studio, Claude Code, Codex, DeepSeek-TUI, Reasonix and more). | ✅ active |
| 4 | [awesome-harness-engineering](https://github.com/walkinglabs/awesome-harness-engineering) | ⭐3,887 | 🛠️ Awesome tools & guides for harness engineering. | ✅ active |
| 5 | [awesome-dsh-plugins (Radar)](https://github.com/AdamPlatin123/awesome-dsh-plugins) | ⭐1,309 | Radar index repo: auto-scanning all discovered dsh plugin candidates with an evidence-based compatibility matrix. | ✅ active |
| 6 | [awesome-deepseek-harness](https://github.com/Anil-matcha/awesome-deepseek-harness) | ⭐966 | Curated guide to DeepSeek Harness (dsh) and its best community plugins | ✅ active |
| 7 | [awesome-dsh-plugin](https://github.com/Anil-matcha/awesome-dsh-plugin) | ⭐966 | A curated list of plugins for DeepSeek Harness (dsh) - DeepSeek Harness plugin ecosystem | ✅ active |
| 8 | [awesome-deepseek-coder](https://github.com/deepseek-ai/awesome-deepseek-coder) | ⭐811 | A curated list of open-source projects related to DeepSeek Coder | ✅ active |
| 9 | [awesome-deepseek-harness (0xsline)](https://github.com/0xsline/awesome-deepseek-harness) | ⭐788 | Curated DSH ecosystem directory: plugins, tools and infrastructure from dsh-external/hub and the public dsh-plugin topic. | ✅ active |
| 10 | [awesome-dsh-plugin (bruc3van)](https://github.com/bruc3van/awesome-dsh-plugin) | ⭐261 | Find the right DSH plugin in 30 seconds: what problem each plugin solves, who it is for and where to start. | ✅ active |

#### Complete list (71)

- [awesome-deepseek-integration](https://github.com/deepseek-ai/awesome-deepseek-integration) ⭐38,897 — Integrate the DeepSeek API into popular software (✅ active)
- [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) ⭐11,012 — Large curated list of installable DSH plugins (bilingual). (✅ active)
- [awesome-deepseek-agent (official)](https://github.com/deepseek-ai/awesome-deepseek-agent) ⭐5,966 — Official curated guides for integrating DeepSeek models into agent/coding-assistant tools (AstrBot, Cherry Studio, Claude Code, Codex, DeepSeek-TUI, Reasonix and more). (✅ active)
- [awesome-harness-engineering](https://github.com/walkinglabs/awesome-harness-engineering) ⭐3,887 — 🛠️ Awesome tools & guides for harness engineering. (✅ active)
- [awesome-dsh-plugins (Radar)](https://github.com/AdamPlatin123/awesome-dsh-plugins) ⭐1,309 — Radar index repo: auto-scanning all discovered dsh plugin candidates with an evidence-based compatibility matrix. (✅ active)
- [awesome-deepseek-harness](https://github.com/Anil-matcha/awesome-deepseek-harness) ⭐966 — Curated guide to DeepSeek Harness (dsh) and its best community plugins (✅ active)
- [awesome-dsh-plugin](https://github.com/Anil-matcha/awesome-dsh-plugin) ⭐966 — A curated list of plugins for DeepSeek Harness (dsh) - DeepSeek Harness plugin ecosystem (✅ active)
- [awesome-deepseek-coder](https://github.com/deepseek-ai/awesome-deepseek-coder) ⭐811 — A curated list of open-source projects related to DeepSeek Coder (✅ active)
- [awesome-deepseek-harness (0xsline)](https://github.com/0xsline/awesome-deepseek-harness) ⭐788 — Curated DSH ecosystem directory: plugins, tools and infrastructure from dsh-external/hub and the public dsh-plugin topic. (✅ active)
- [awesome-dsh-plugin (bruc3van)](https://github.com/bruc3van/awesome-dsh-plugin) ⭐261 — Find the right DSH plugin in 30 seconds: what problem each plugin solves, who it is for and where to start. (✅ active)
- [Awesome-DeepSeek-Harness-Plugins](https://github.com/Zhiyuan-Fan/Awesome-DeepSeek-Harness-Plugins) ⭐240 — Curated list of DeepSeek Harness plugins. (✅ active)
- [awesome-deepseek-harness (libukai)](https://github.com/libukai/awesome-deepseek-harness) ⭐175 — Ultimate guide: quick start, resources, curated plugins and practical tools. (✅ active)
- [awesome-deepseek-harness (Dominic789654)](https://github.com/Dominic789654/awesome-deepseek-harness) ⭐174 — Curated list of plugins, skills, MCP servers, patch/profile layers, orchestrators and UIs for DeepSeek Harness. (✅ active)
- [notes (zhaoolee)](https://github.com/zhaoolee/notes) ⭐149 — Open-source Smartisan Notes clone: Docker private deployment, skill invocation, dsh plugin support and one-click WeChat-format export. (✅ active)
- [awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) ⭐145 — Curated community plugin directory and live marketplace for DeepSeek Harness. (✅ active)
- [awesome-dsh-plugin](https://github.com/beancookie/awesome-dsh-plugin) ⭐93 — Awesome DeepSeek Harness (DSH) Plugin (✅ active)
- [awesome-DSH-plugin (Alex-Yanggg)](https://github.com/Alex-Yanggg/awesome-DSH-plugin) ⭐77 — Meticulously curated list of plugins, extensions, tools and development resources for DSH. (✅ active)
- [zat-dsh-engine](https://github.com/mishibeikejie/zat-dsh-engine) ⭐76 — Visual plugin marketplace for DeepSeek Harness — browse, search and install community plugins (✅ active)
- [oh-my-dsh](https://github.com/like-study1/Oh-My-DSH) ⭐68 — 🐳 DeepSeek Harness 插件聚合社区 — 自动同步 dsh-plugin 生态 · 精选目录 · 每 8 小时自动维护 | Oh-My-DSH: a community-maintained catalog of DeepSeek Harness plugins, auto-synced from the dsh-plugin topic (✅ active)
- [plugin-registry](https://github.com/vlln/plugin-registry) ⭐57 — DSH plugin ecosystem infrastructure: thin console to manage official repository plugins (0 patch) plus the make-dsh-plugin skill. (✅ active)
- [oh-my-dsh](https://github.com/LaplaceYoung/oh-my-dsh) ⭐51 — Plugin ecosystem for DSH: 700+ plugins registered only through extension seams, without modifying the agent-loop skeleton. (✅ active)
- [awesome-harness-engineering](https://github.com/jiji262/awesome-harness-engineering) ⭐49 — Awesome lists of Harness Engineering and AI Native Engineering resources. (✅ active)
- [dsh-market](https://github.com/2BingLing/dsh-market) ⭐46 — DeepSeek Harness 插件市场 · 持续收录 500+ DSH 插件：中文搜索 + 实用五维评分 + 一键安装。Web 版与 DSH 侧边栏插件双形态。Plugin marketplace for DeepSeek Harness: 500+ plugins, Chinese search, 5-dim scoring, one-click install. (✅ active)
- [dsh-suite](https://github.com/whyihaveyou/dsh-suite) ⭐43 — Living DSH plugin directory (785+ plugins, refreshed hourly) with daily compatibility CI, a bilingual catalog site and an in-app plugin store. (✅ active)
- [awesome-deepseek-harness-plugins](https://github.com/web-casa/Awesome-DeepSeek-Harness-Plugins) ⭐33 — Awesome DSH Cordis Plugins — the official, auto-generated list of DeepSeek Harness Cordis plugins, curated by cordis.run 由 cordis.run 精选维护的 DeepSeek Harness Cordis 插件官方自动生成列表。 (✅ active)
- [sandbase-skills](https://github.com/sandbaseai/sandbase-skills) ⭐31 — 88 installable open-source Agent Skills for research, social intelligence, marketing, and business workflows—compatible with Codex, Claude Code, Cursor, Gemini CLI, and DeepSeek Harness. (✅ active)
- [dsh-meme-hub](https://github.com/the-beating-light-of-the-nail/dsh-meme-hub) ⭐30 — Curated navigation of community meme plugins (skins, desktop pets, mini-games), bilingual. (✅ active)
- [dsh-plugin-marketplace](https://github.com/AwesomeHou/dsh-plugin-marketplace) ⭐27 — Plugin marketplace for DeepSeek Harness — live-syncs the GitHub dsh-plugin topic (1800+ repos) into a searchable, paginated settings tab with one-click install and agent tools (market_search / market_install). (✅ active)
- [deepseek-plugin-store](https://github.com/Ericwong5021/deepseek-plugin-store) ⭐24 — DeepSeek Harness 独立社区插件商店：发现、安装并提交经过验证的插件、工具与扩展。 | Independent community plugin directory. (✅ active)
- [awesome-dsh-plugins (kejixiaoliang)](https://github.com/kejixiaoliang/awesome-dsh-plugins) ⭐22 — Curated DSH plugin catalog: 14 categories, 280+ community plugins covering MCP/Skill/TUI/multi-agent/context memory/UI skins. (✅ active)
- [dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) ⭐20 — Verified plugin marketplace and autonomous registry for DeepSeek Harness (✅ active)
- [dsh-plugin-hub](https://github.com/cclank/dsh-plugin-hub) ⭐17 — DeepSeek Harness community plugin registry with evidence-based screening (✅ active)
- [dsh-plugin-hub](https://github.com/dshplugin/dsh-plugin-hub) ⭐16 — DeepSeek Harness 社区内置插件市场（dsh-plugin）— 搜索插件、下载并安装 4000+ 人工精选社区插件，每日更新、完全免费。内置在 Harness「设置 → 插件中心」，无需离开应用即可浏览、搜索、安装各类 AI 插件。 (✅ active)
- [deepseek-harness-awesome-top-500](https://github.com/weekend-project-space/deepseek-harness-awesome-top-500) ⭐15 — deepseek-harness plugins 、resource 、use ; dsh top 500 (✅ active)
- [awesome-deepseek-harness (jiji262)](https://github.com/jiji262/awesome-deepseek-harness) ⭐13 — Curated DeepSeek Harness resources. (✅ active)
- [awesome-dsh-plugins (white0dew)](https://github.com/white0dew/awesome-dsh-plugins) ⭐13 — Public GitHub directory for DSH plugins with install commands. (✅ active)
- [awesome-dsh-plugin (billLiao)](https://github.com/billLiao/awesome-dsh-plugin) ⭐12 — Curated list of plugins for DeepSeek Harness. (✅ active)
- [dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) ⭐12 — DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 | https://dsh-plugin-hub.hupc.site (✅ active)
- [dsh-plugin-marketplace](https://github.com/w2112515/dsh-plugin-marketplace) ⭐12 — Out-of-tree installable plugin marketplace bundle for DeepSeek Harness (✅ active)
- [awesome-deepseek-harness-plugins](https://github.com/vvlife/awesome-deepseek-harness-plugins) ⭐10 — A curated list of plugins, tools, skins, and extensions for DeepSeek Harness (DSH). (✅ active)
- [awesome-deepseek-harness-plugins](https://github.com/walkinglabs/awesome-deepseek-harness-plugins) ⭐9 — A curated, bilingual list of verified plugins, tools, design workflows, and learning resources for DeepSeek Harness (DSH). (✅ active)
- [awesome-dsh-bridges](https://github.com/YYTbit/awesome-dsh-bridges) ⭐6 — Bridge your favorite AI coding tools into DeepSeek Harness (✅ active)
- [awesome-dsh-plugins](https://github.com/cccakeee/awesome-dsh-plugins) ⭐6 — A curated, evidence-led directory of DeepSeek Harness (DSH) plugins: verified loadable extensions, skills, and permission-aware installation guidance. (✅ active)
- [dsh-plugins](https://github.com/Sakana-yuyu/dsh-plugins) ⭐6 — DeepSeek Harness (DSH) 插件目录：官方包 + 社区插件按 GitHub stars 排名，GitHub Pages 可访问。 (✅ active)
- [awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) ⭐5 — Spam-filtered, open-data registry of DeepSeek Harness (dsh) plugins, bundles, and skills. (✅ active)
- [dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) ⭐5 — DeepSeek Harness plugin market - browse, search & install dsh-plugin topic plugins (dsh 插件市场：浏览/搜索/安装插件) (✅ active)
- [dsh-plugins](https://github.com/HackSing/dsh-plugins) ⭐5 — A bilingual, continuously maintained directory of plugins for DeepSeek Harness (DSH). (✅ active)
- [awesome-dsh-skills](https://github.com/hackerFish/awesome-dsh-skills) ⭐4 — 实测可用的 DeepSeek Harness 技能库：每个 SKILL.md 都通过格式校验与加载冒烟，复制即用（中文优先） (✅ active)
- [dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) ⭐4 — DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令） (✅ active)
- [awesome-deepseek-harness](https://github.com/XiaomingX/awesome-deepseek-harness) ⭐3 — Curated DeepSeek Harness (DSH) ecosystem catalog — plugins, tools & infrastructure. Filtered, multilingual (ZH/EN/KO/JA), with design patterns worth borrowing. (✅ active)
- [awesome-dsh-plugins](https://github.com/dongsheng123132/awesome-dsh-plugins) ⭐3 — Evidence-backed DeepSeek Harness plugin radar and 2Origin plugin lab (✅ active)
- [awesome-dsh-plugins-2026](https://github.com/Herdeny/awesome-dsh-plugins-2026) ⭐3 — Curated list of DeepSeek Harness (DSH) plugins for 2026, with quality check. (✅ active)
- [awesome-dsh-themes](https://github.com/dshworks/awesome-dsh-themes) ⭐3 — Registry of DeepSeek Harness (dsh) themes and --dsw-* token skins. Not affiliated with DeepSeek. (✅ active)
- [dsh-marketplace](https://github.com/ouyangyipeng/dsh-marketplace) ⭐3 — A safe, live plugin marketplace for DeepSeek Harness (✅ active)
- [dsh-plugins](https://github.com/lwmxiaobei/dsh-plugins) ⭐3 — DeepSeek Harness 社区插件目录，自动汇总并基础校验 GitHub 插件，支持搜索、筛选、双语详情与最新版本安装命令复制。Community directory for DeepSeek Harness plugins with automated discovery, basic validation, search, filters, bilingual details, and latest version install commands. (✅ active)
- [dsh-plugins-store](https://github.com/DshMarketPlace/dsh-plugins-store) ⭐3 — Browse and install DSH plugins from inside DeepSeek Harness. /store, a settings tab, and agent tools — bilingual. (✅ active)
- [awesome-dsh-plugin](https://github.com/wgd753/awesome-dsh-plugin) ⭐2 — Awesome dsh plugin list — automated DeepSeek Harness plugin directory. Daily GitHub Actions crawl of topic:dsh-plugin / topic:deepseek-harness, bilingual README + machine-readable JSON/CSV (✅ active)
- [awesome-dsh-plugins](https://github.com/coolbat/awesome-dsh-plugins) ⭐2 — Evidence-led bilingual directory of DeepSeek Harness plugins, reviewed at immutable commits. (✅ active)
- [awesome-dsh-plugins](https://github.com/jqueryscript/awesome-dsh-plugins) ⭐2 — Verified, star-ranked community plugins for DeepSeek Harness (dsh). (✅ active)
- [awesome-dshoneys](https://github.com/dshoneys/awesome-dshoneys) ⭐2 — DeepSeek Honeys 认证插件目录 — 安全检测报告 + 插件需求墙 + 每周精选 (✅ active)
- [dshmarketplace](https://github.com/DshMarketPlace/dshmarketplace) ⭐2 — Bilingual directory of DeepSeek Harness (DSH) plugins — 3,400+ listings, sandbox-verified install commands, written detail pages, public API. Next.js on Cloudflare Workers. (✅ active)
- [awesome-deepseek-harness](https://github.com/Harris1121/awesome-deepseek-harness) ⭐1 — Find the right DeepSeek Harness tools faster — see what’s popular, rising and worth using. (✅ active)
- [awesome-deepseek-harness-plugins](https://github.com/SihanTeng/awesome-deepseek-harness-plugins) ⭐1 — A curated collection of plugins, tools, and integrations for the DeepSeek Harness agent runtime (✅ active)
- [awesome-dsh-list](https://github.com/kingselyjoe/awesome-dsh-list) ⭐1 — 🐳 DeepSeek Harness（DSH）工具全量清单——GitHub topic:dsh-plugin 生态 1000+ 仓库按 star 排序。Awesome list for DeepSeek Harness tools. (✅ active)
- [awesome-dsh-plugins](https://github.com/oslook/awesome-dsh-plugins) ⭐1 — Deekseek Harness Plugins (✅ active)
- [awesome-dsh-presets](https://github.com/hackerFish/awesome-dsh-presets) ⭐1 — 实测可用的 DeepSeek Harness 预设与规则合集：官方派生 + 原创组合，每个预设通过结构与包存在性校验（中文优先） (✅ active)
- [awesome-deepseek-harness](https://github.com/Rodert/awesome-deepSeek-harness)  — deepSeek harness plugin DeepSeek Harness 组件 (✅ active)
- [awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness)  — Awesome DeepSeek Harness (dsh) — curated plugins, tools, skills & resources. Everything is a plugin. (✅ active)
- [dsh-plugin-registry](https://github.com/dshplugin-app/dsh-plugin-registry)  — Discover and compare DeepSeek Harness plugins directly inside DSH. (✅ active)
- [dshthemes](https://github.com/dshworks/dshthemes)  — dshthemes.com — every DeepSeek Harness theme, in its own colours. A reader of dshworks/awesome-dsh-themes. (✅ active)
- [plugins](https://github.com/dsh-universe/plugins)  — DeepSeek Harness plugin & skill directory — DSH Universe official marketplace (duink.com) (✅ active)

### Related Agent Harnesses


#### 🔥 Top 10

| # | Project | Stars | Description | Status |
|---|---|---|---|---|
| 1 | [DeerFlow](https://github.com/bytedance/deer-flow) | ⭐80,462 | Open-source long-horizon SuperAgent harness by ByteDance: skills, memory, sandboxes, subagents, tools and a message gateway. | ✅ active |
| 2 | [CodeWhale](https://github.com/Hmbown/CodeWhale) | ⭐40,830 | Open-source, community-driven agent harness. | ✅ active |
| 3 | [agentmemory](https://github.com/rohitg00/agentmemory) | ⭐27,233 | Persistent memory for AI coding agents based on real-world benchmarks (upstream of DSH agentmemory ports). | ✅ active |
| 4 | [Cordis](https://github.com/cordiverse/cordis) | ⭐6,867 | Meta-Framework of Spatiotemporal Composability — the plugin runtime DeepSeek Harness is built on. | ✅ active |
| 5 | [deeptide](https://github.com/paean-ai/deeptide) | ⭐1,091 | Swift-native macOS coding agent built by DeepSeek, for DeepSeek. | ✅ active |
| 6 | [sandbase-harness](https://github.com/sandbaseai/sandbase-harness) | ⭐628 | Open-source CMA-compatible agent runtime for any model: MCP tools, sandboxed sessions, audit, replay. | ✅ active |
| 7 | [mnemon](https://github.com/mnemon-dev/mnemon) | ⭐500 | LLM-supervised persistent memory for AI agents: graph-based recall and cross-session knowledge in a single binary. | ✅ active |
| 8 | [claude-paper](https://github.com/alaliqing/claude-paper) | ⭐324 | Cross-agent research paper toolkit for Claude Code, Codex, OpenCode and DeepSeek Harness: quick summaries and deep dives. | ✅ active |
| 9 | [open-managed-agents](https://github.com/openma-ai/open-managed-agents) | ⭐243 | Open-source Claude Managed Agents API implementation and self-hosted Claude Tag-style agent runtime. | ✅ active |
| 10 | [Axern](https://github.com/cofy-x/axern) | ⭐57 | Open-source sandboxes for AI agents: untrusted code execution and durable services. | ✅ active |

#### Complete list (11)

- [DeerFlow](https://github.com/bytedance/deer-flow) ⭐80,462 — Open-source long-horizon SuperAgent harness by ByteDance: skills, memory, sandboxes, subagents, tools and a message gateway. (✅ active)
- [CodeWhale](https://github.com/Hmbown/CodeWhale) ⭐40,830 — Open-source, community-driven agent harness. (✅ active)
- [agentmemory](https://github.com/rohitg00/agentmemory) ⭐27,233 — Persistent memory for AI coding agents based on real-world benchmarks (upstream of DSH agentmemory ports). (✅ active)
- [Cordis](https://github.com/cordiverse/cordis) ⭐6,867 — Meta-Framework of Spatiotemporal Composability — the plugin runtime DeepSeek Harness is built on. (✅ active)
- [deeptide](https://github.com/paean-ai/deeptide) ⭐1,091 — Swift-native macOS coding agent built by DeepSeek, for DeepSeek. (✅ active)
- [sandbase-harness](https://github.com/sandbaseai/sandbase-harness) ⭐628 — Open-source CMA-compatible agent runtime for any model: MCP tools, sandboxed sessions, audit, replay. (✅ active)
- [mnemon](https://github.com/mnemon-dev/mnemon) ⭐500 — LLM-supervised persistent memory for AI agents: graph-based recall and cross-session knowledge in a single binary. (✅ active)
- [claude-paper](https://github.com/alaliqing/claude-paper) ⭐324 — Cross-agent research paper toolkit for Claude Code, Codex, OpenCode and DeepSeek Harness: quick summaries and deep dives. (✅ active)
- [open-managed-agents](https://github.com/openma-ai/open-managed-agents) ⭐243 — Open-source Claude Managed Agents API implementation and self-hosted Claude Tag-style agent runtime. (✅ active)
- [Axern](https://github.com/cofy-x/axern) ⭐57 — Open-source sandboxes for AI agents: untrusted code execution and durable services. (✅ active)
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
