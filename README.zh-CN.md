# Awesome DeepSeek Harness 🐋

> 官方 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 生态精选：
> **插件 · 技能 · 工作流 · 智能体 · 客户端 · 工具 · 示例 · 教程**。

[English](README.md) · [MkDocs 站点](https://deepseekserver.com)

DeepSeek Harness（`dsh`）是 DeepSeek AI 开源的智能体 Harness，围绕一个简单理念构建：

> **一切皆插件（Everything is a Plugin）。**

本仓库收录围绕官方 `deepseek-ai/deepseek-harness` 项目的完整生态——不只是插件，而是**整个 Harness 生态**：

**插件 · 技能 · 工作流 · 智能体 · 工具 · 桌面端 · 终端 · 集成 · 示例 · 教程**

**✨ 自带特性：** 🔥 **Trending 热度榜**（每类自动排序 Top 10 + 全网 Top 20）· 🧮 机器可读注册表（`data/*.json`）· ✅ 链接实时核验 · 🌐 中英双语 · 📊 每周自动刷新

> ⚠️ DeepSeek Harness 目前处于开发者预览阶段，迭代极快，兼容性可能随时变化。安装前请务必查看对应仓库。
>
> 本列表为**社区维护、独立验证**——许多旧注册表（如前 `dsh-external` 组织）已含大量死链。本目录中每条资源均于 2026-08-14 通过 GitHub API 实时核验。

---

## 目录

- [官方资源](#官方资源)
- [快速开始](#快速开始)
- [🔥 热门](#-热门)
- [插件](#插件)
- [技能](#技能)
- [工作流与自动化](#工作流与自动化)
- [智能体与多智能体](#智能体与多智能体)
- [客户端（桌面与终端）](#客户端桌面与终端)
- [MCP 与集成](#mcp-与集成)
- [示例与模板](#示例与模板)
- [教程与学习](#教程与学习)
- [精选列表与注册表](#精选列表与注册表)
- [相关 Agent Harness](#相关-agent-harness)
- [研究](#研究)
- [项目结构](#项目结构)
- [质量等级](#质量等级)
- [提交项目](#提交项目)
- [并非同一项目](#并非同一项目)
- [路线图](#路线图)
- [贡献](#贡献)
- [免责声明](#免责声明)

---

# 官方资源

### DeepSeek Harness

**仓库** — https://github.com/deepseek-ai/deepseek-harness

DeepSeek AI 官方开源的智能体 Harness。MIT 协议，基于 [Cordis](https://github.com/cordiverse/cordis) 构建。

### 安装

```bash
npx @deepseek-ai/dsh web
```

从源码运行：

```bash
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness

pnpm install
pnpm run build
pnpm dsh web
```

默认 Web UI：

```text
http://127.0.0.1:3080
```

### 插件发现

官方生态约定——为你的插件仓库添加主题标签：

```text
GitHub topic: dsh-plugin
```

浏览：https://github.com/topics/dsh-plugin

### 架构

DeepSeek Harness 基于 **Cordis**（时空可组合性元框架）构建。核心概念包括：

* 插件化架构 · Profiles · Bundles · 工具 · 模型适配器
* 会话 · Agent 循环 · 沙箱 · 后台任务 · 子代理
* Web UI · 无头执行

---

# 快速开始

## 运行 DSH

```bash
npx @deepseek-ai/dsh web
```

## 安装插件

```bash
dsh plugin --profile web add <package>
```

如需重启 profile：

```bash
dsh web
```

想要成为 DSH 活跃 Bundle 的插件应暴露对应的 `dsh.bundle` 元数据。已装插件可在 **设置 → 插件** 中管理。

---

# 🔥 热门

> **✨ 自带 Trending 热度榜。** 这不是一份静态列表——它内置了实时排序引擎：

> * **🔥 每类 Top 10** —— 下文每个分类都会按 GitHub 实时星数自动排序，一眼看清社区最关注什么
> * **🌍 全网 Top 20** —— 覆盖整个生态的排行榜，见 [文档站点](https://deepseekserver.com) 首页
> * **♻️ 自动刷新** —— 星数与状态自动更新（`scripts/update-metadata.py` + 每周 GitHub Action），每次构建都会重算排序
> * **🧭 信号路线图** —— 计划推出 trending（星数增长/提交/发布）、popular（长期采纳）、new（新发现）与 verified 多维度排序，见[路线图](#路线图)

> 当前热门项目（按星数，截至 2026-08-14）：

| # | 项目 | ⭐ | 亮点 |
|---|---|---|---|
| 1 | [dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | 1.7k | 最大的插件/皮肤合集：任务看板、Git 图、宠物、Token 统计 |
| 2 | [dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) | 793 | Claude Code 风格全屏终端插件 |
| 3 | [DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) | 684 | 工作台式侧边栏：文件、终端、Git、子代理 |
| 4 | [dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) | 506 | 鲸鱼娘皮肤系列 |
| 5 | [DeepSeek Harness 橙皮书](https://github.com/alchaincyf/deepseek-harness-orange-book) | 465 | 社区一手实测：系统提示词、启动清单、原始日志 |
| 6 | [dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) | 302 | 纯文本模型的视觉工具箱：图片问答、OCR、UI 还原 |
| 7 | [dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) | 222 | 多智能体团队扩展 |
| 8 | [dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) | 167 | 从 0 到 1 深度手册（中英 PDF） |
| 9 | [oh-dsh](https://github.com/hust-open-atom-club/oh-dsh) | 160 | 一站式社区发行版（TUI + 桌面 + Web UI） |
| 10 | [dsh-at-file](https://github.com/omdsh-dev/dsh-at-file) | 116 | Codex 风格 `@file` 提及 |

---

# 插件

> DSH 插件生态是 Harness 的心脏。下面按类别整理了 111 个精选插件，组内按星数排序。插件提供**运行时能力**；技能提供可复用的知识（见[技能](#技能)）。

<!-- AUTO:resources:START -->
### Plugins


#### 🔥 Top 10

| # | 项目 | 星数 | 说明 | 状态 |
|---|---|---|---|---|
| 1 | [voyager](https://github.com/Nagi-ovo/voyager) | ⭐19,755 | Enhancement suite for Gemini, AI Studio, Claude & ChatGPT — plus a prompt manager for any web UI, DeepSeek Harness included. / 面向 Gemini、AI Studio、Claude 与 ChatGPT 的增强套件；提示词管理器可用于任意 Web UI，含 DeepSeek Harness。 | ✅ 活跃 |
| 2 | [dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | ⭐5,349 | DSH Web 大型插件与皮肤集合：任务看板、Git 图、侧栏、远程/移动 UI、宠物、Token 统计与主题。 | ✅ 活跃 |
| 3 | [petdex](https://github.com/crafter-station/petdex) | ⭐3,945 | A public gallery of animated pets for Codex, Claude Code, DeepSeek Harness, Hermes, OpenCode, Gemini CLI, and more. | ✅ 活跃 |
| 4 | [dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) | ⭐3,697 | Two-phase DeepSeek Harness preset: Minimal-aligned bootstrap, then full Standard tools (Project2 98/99) | ✅ 活跃 |
| 5 | [modlens](https://github.com/liustack/modlens) | ⭐3,495 | DSH 首个视觉插件，也是所有纯文本编码 Agent 的视觉桥梁：粘贴图片即可用。 | ✅ 活跃 |
| 6 | [DSH Better Sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) | ⭐2,552 | 工作台式侧边栏：文件渲染/编辑、终端、Git、子代理，支持三方扩展 Tab。 | ✅ 活跃 |
| 7 | [dsh-market](https://github.com/dsh-market/dsh-market) | ⭐1,582 | DSH 内置可视化插件市场：浏览、搜索、一键安装。 | ✅ 活跃 |
| 8 | [dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) | ⭐1,548 | DSH Web 鲸鱼娘皮肤系列（CC BY-NC-SA 4.0）。 | ✅ 活跃 |
| 9 | [TokenTracker](https://github.com/xiufengsun/TokenTracker) | ⭐1,395 | 本地优先的 AI Token 用量与费用追踪器，支持 31 款编码工具（含 Claude Code、Codex、Cursor、Gemini 与 DeepSeek Harness）。 | ✅ 活跃 |
| 10 | [dsh-vision-router](https://github.com/ysr666/dsh-vision-router) | ⭐927 | 纯文本 Agent 的眼睛：内置免费免密钥视觉链路 + 像素级工具（问答、grounding、裁剪、OCR、SVG 描摹）。 | ✅ 活跃 |

#### 完整列表（434）

- [voyager](https://github.com/Nagi-ovo/voyager) ⭐19,755 — Enhancement suite for Gemini, AI Studio, Claude & ChatGPT — plus a prompt manager for any web UI, DeepSeek Harness included. / 面向 Gemini、AI Studio、Claude 与 ChatGPT 的增强套件；提示词管理器可用于任意 Web UI，含 DeepSeek Harness。（✅ 活跃）
- [dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) ⭐5,349 — DSH Web 大型插件与皮肤集合：任务看板、Git 图、侧栏、远程/移动 UI、宠物、Token 统计与主题。（✅ 活跃）
- [petdex](https://github.com/crafter-station/petdex) ⭐3,945 — A public gallery of animated pets for Codex, Claude Code, DeepSeek Harness, Hermes, OpenCode, Gemini CLI, and more.（✅ 活跃）
- [dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) ⭐3,697 — Two-phase DeepSeek Harness preset: Minimal-aligned bootstrap, then full Standard tools (Project2 98/99)（✅ 活跃）
- [modlens](https://github.com/liustack/modlens) ⭐3,495 — DSH 首个视觉插件，也是所有纯文本编码 Agent 的视觉桥梁：粘贴图片即可用。（✅ 活跃）
- [DSH Better Sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) ⭐2,552 — 工作台式侧边栏：文件渲染/编辑、终端、Git、子代理，支持三方扩展 Tab。（✅ 活跃）
- [dsh-market](https://github.com/dsh-market/dsh-market) ⭐1,582 — DSH 内置可视化插件市场：浏览、搜索、一键安装。（✅ 活跃）
- [dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) ⭐1,548 — DSH Web 鲸鱼娘皮肤系列（CC BY-NC-SA 4.0）。（✅ 活跃）
- [TokenTracker](https://github.com/xiufengsun/TokenTracker) ⭐1,395 — 本地优先的 AI Token 用量与费用追踪器，支持 31 款编码工具（含 Claude Code、Codex、Cursor、Gemini 与 DeepSeek Harness）。（✅ 活跃）
- [dsh-vision-router](https://github.com/ysr666/dsh-vision-router) ⭐927 — 纯文本 Agent 的眼睛：内置免费免密钥视觉链路 + 像素级工具（问答、grounding、裁剪、OCR、SVG 描摹）。（✅ 活跃）
- [dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) ⭐802 — 让纯文本模型更好的视觉工具箱：带意图图片问答、长截图 OCR、UI 还原、grounding、像素 diff。（✅ 活跃）
- [dsh-pocket](https://github.com/shaobeichen/dsh-pocket) ⭐796 — 把 DeepSeek Harness 装进你的口袋：电脑上跑 dsh web，手机扫码即同步访问（局域网 + 公网，实时同屏）Put DeepSeek Harness in your pocket: run dsh web on your computer and access it synchronously by scanning a QR code on your phone (LAN + public network, real‑time screen mirroring)（✅ 活跃）
- [dsh-context](https://github.com/bowenliang123/dsh-context) ⭐666 — A DeepSeek Harness plugin for  Context insight dashboard — showing what the model's context window is made of and how it evolves.（✅ 活跃）
- [museai](https://github.com/yejiming/MuseAI) ⭐595 — 创建你的 AI 角色，进入你的故事世界。和角色聊天、冒险、穿书，让每一次互动都留下羁绊（支持 DeepSeek Harness 插件，欢迎使用）（✅ 活跃）
- [graph-memory](https://github.com/adoresever/graph-memory) ⭐564 — Deepseek Harness、Openclaw知识图谱记忆插件。2026年4月受邀发布在清华大学讨论会。Knowledge Graph + Memory；Knowledge Graph Context Engine for OpenClaw — extracts structured triples from conversations, compresses context 75%, enables cross-session experience reuse（✅ 活跃）
- [dsh-ads](https://github.com/Nagi-ovo/dsh-ads) ⭐525 — 整活插件：2005 中文站点风格广告层，侧栏广告/对话内信息流/角落弹窗。（✅ 活跃）
- [v4-flash-godmode-opencode-go](https://github.com/SheberDavid/v4-flash-godmode-opencode-go) ⭐494 — V4 Flash 神模式 (opencode-go)：让 opencode-go 的 DeepSeek V4 Flash 从鬼模式切换到神模式的 dsh agent preset（✅ 活跃）
- [dsh-at-file](https://github.com/omdsh-dev/dsh-at-file) ⭐445 — Codex 风格 @file 提及：在 DSH 输入框中搜索工作区文件并附加内容到提示词。（✅ 活跃）
- [dsh-browser](https://github.com/Lum1104/dsh-browser) ⭐366 — Chrome 侧栏扩展：让 DSH 直接操控你的浏览器，无需视觉能力。（✅ 活跃）
- [dsh-transparent-ui-plugin](https://github.com/WYH66666666/DSH-Transparent-UI-Plugin) ⭐355 — 是一层高自由度的玻璃质感主题，套在 DeepSeek Harness 网页端。顶栏、侧边栏、输入框、统计行、轨迹视图都成了磨砂玻璃片。玻璃模糊度、磨砂度、背景（流体或自定义壁纸，壁纸还能单独调模糊和磨砂）全都能在设置卡片里自由调节。关掉开关就回到原生界面，不改 DSH 任何一行源码。（✅ 活跃）
- [flowix](https://github.com/text2future/flowix) ⭐338 — Notes for you, Memory for your agents. / 内置 Deepseek harness Agent / 适用 办公 & 写作 & Coding（✅ 活跃）
- [dsh-pentest](https://github.com/howmp/dsh-pentest) ⭐314 — 面向 DeepSeek Harness（dsh）的渗透测试模式  @CloverSecLabs（✅ 活跃）
- [dsh-genui](https://github.com/omdsh-dev/dsh-genui) ⭐282 — 对话内生成式 UI：布局、图表、表单、测验、Mermaid 与交互事件内联渲染。（✅ 活跃）
- [dsh-image-gen](https://github.com/shanliuling/dsh-image-gen) ⭐277 — Generate images directly in DeepSeek Harness chats（✅ 活跃）
- [dsh-pet](https://github.com/PC2005-cloud/dsh-pet) ⭐274 — DeepSeek Harness 桌面宠物插件 + 完整素材生成链：AI 提示词 → 绿幕视频 → 透明动画 → 可安装插件，从零到宠物全流程可复现（✅ 活跃）
- [whale-girl](https://github.com/vlln/whale-girl) ⭐260 — QQ 宠物形态桌面宠物：DSH Web 右下角悬浮，可拖拽/投喂/玩耍。（✅ 活跃）
- [dsh-synapse](https://github.com/liangmianya/dsh-synapse) ⭐250 — A visual, non-linear conversation workspace plugin for DeepSeek Harness ; A canvas-based session explorer and branching workspace for DeepSeek Harness.（✅ 活跃）
- [dsh-plugin-subscriptions](https://github.com/V1ki/dsh-plugin-subscriptions) ⭐216 — Use ChatGPT (Codex), Claude, and Grok (X Premium) subscriptions as DeepSeek Harness LLM providers — OAuth login in the web UI, no API keys（✅ 活跃）
- [dsh-memory-evolve](https://github.com/csyangwen/dsh-memory-evolve) ⭐211 — 跨会话长期记忆 + 后台自我进化：五轨记忆、git 分支感知、回合内自我审查、技能自我进化。（✅ 活跃）
- [modsearch](https://github.com/liustack/modsearch) ⭐207 — DSH 网页插件：为没有原生联网能力的模型提供搜索桥梁。（✅ 活跃）
- [dsh-wallpaper-engine](https://github.com/elysia395/dsh-wallpaper-engine) ⭐204 — 把本机 Wallpaper Engine 的壁纸变成 DSH 网页界面的背景：Video 动态播放、Web 以 iframe 加载、Scene 壁纸提取主纹理作为静态帧；iOS 液态玻璃设置窗口（配色 / 玻璃颜色 / 透明度）、内容分级与类型过滤、自定义壁纸上传、紧凑 CD 架布局、黑胶唱片展示、隐藏 / 恢复、倍速 / 翻转与自动轮播。感谢 Jerry 维护 macOS 版。（✅ 活跃）
- [dsh-visualize](https://github.com/Nagi-ovo/dsh-visualize) ⭐196 — 对话内交互式 HTML UI：流式预览与沙箱渲染。（✅ 活跃）
- [Open Sea Skin](https://github.com/d-dev0101/open-sea-skin) ⭐185 — 实时 WebGPU 海洋皮肤，可调节波浪、日光、玻璃不透明度和自动昼夜循环。（✅ 活跃）
- [anysearch-dsh](https://github.com/anysearch-team/anysearch-dsh) ⭐174 — AnySearch 网页搜索 provider 与高级搜索工具。（✅ 活跃）
- [dsh-find-plugins](https://github.com/Nagi-ovo/dsh-find-plugins) ⭐162 — DSH 生态插件发现工具。（✅ 活跃）
- [anime-find](https://github.com/cocofhu/anime-find) ⭐157 — DeepSeek Harness 搜番插件：对话内多源搜索番剧，卡片展示 Bangumi 评分与详情，支持复制磁力。（✅ 活跃）
- [dsh-mnemon](https://github.com/omdsh-dev/dsh-mnemon) ⭐156 — 三层本地记忆系统：运行时热记忆、项目文档、长期记忆空间，监督式写回。（✅ 活跃）
- [dsh-liang-skin](https://github.com/kingOfSoySauce/dsh-liang-skin) ⭐148 — DeepSeek Harness 滑动变阻器皮肤（✅ 活跃）
- [dsh-cost-meter](https://github.com/Han-1413141/dsh-cost-meter) ⭐139 — DeepSeek Harness 会话费用统计插件:本会话费用、当日费用、历史记录与官方价格同步（✅ 活跃）
- [dsh-gitbash-preset](https://github.com/liceses/dsh-gitbash-preset) ⭐136 — DeepSeek Harness 插件：一键安装「极简模式 (Git Bash)」agent preset —— 把 DSH 自带极简模式中的 bash 调用映射到 Git for Windows 的 bash（MSYS），让 Windows 上的极简模式真正可用。（✅ 活跃）
- [dsh-undo-savepoint](https://github.com/lire1131/dsh-undo-savepoint) ⭐134 — DSH crash-rescue plugin: undo config & plugin-code changes, secret-safe snapshots, one-click SAFE MODE, plus offline CLI/GUI that work even when DSH won't boot.（✅ 活跃）
- [DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) ⭐132 — 在 DSH Web GUI 中一键浏览、安装与更新全部 GitHub dsh-plugin 插件。（✅ 活跃）
- [dsh-noema](https://github.com/ZSeven-W/dsh-noema) ⭐128 — Noema long-term memory plugin for DSH: durable, inspectable agent memory with recall tools and a settings page.（✅ 活跃）
- [tokenledger](https://github.com/zh667/TokenLedger) ⭐126 — Token usage accounting for DeepSeek Harness, reconciled against New API and Sub2API relay-site billing（✅ 活跃）
- [dsh-auto-mode](https://github.com/NanmiCoder/dsh-auto-mode) ⭐115 — Safe automatic permissions for DeepSeek Harness.（✅ 活跃）
- [dsh-undo-plugin](https://github.com/lire1131/dsh-undo-plugin) ⭐108 — DSH plugin: snapshot & rollback your plugin/skin/settings configs. Auto-save on change, undo/redo stack, snapshot manager panel, keyboard shortcuts, plus an offline PowerShell CLI & GUI that work even when DSH won't boot.（✅ 活跃）
- [dsh-authinone](https://github.com/Stormycry-cryp/dsh-AuthInOne) ⭐105 — Self-contained DeepSeek Harness (DSH) plugin for Provider/Auth login, model switching, image fallback, token/cost analytics, and same-port Web restart. Useful? A star helps.（✅ 活跃）
- [dsh-usage-stats](https://github.com/Ychris12138/dsh-usage-stats) ⭐98 — Token usage heatmap, per-model breakdowns, and DeepSeek account balance for the DeepSeek Harness Web GUI (dsh web).（✅ 活跃）
- [dsh-reasoning-effort](https://github.com/HanaAyane/dsh-reasoning-effort) ⭐97 — DSH适用的Codex风格的思考强度滑块，以及大肥鱼跑步滑块。Codex-style model and reasoning-effort slider for DeepSeek Harness（✅ 活跃）
- [dsh-webui-market-plugin](https://github.com/Sanqi-normal/dsh-webui-market-plugin) ⭐96 — dsh Web GUI 社区插件市场：浏览 awesome-dsh-plugin.com 目录，一键安装/卸载到 profile。（✅ 活跃）
- [dsh-turn-rewind](https://github.com/Anionex/dsh-turn-rewind) ⭐94 — 对话与代码状态回退插件，基于持久化变更账本。（✅ 活跃）
- [dsh-plugin](https://github.com/Tabbit-Browser/dsh-plugin) ⭐91 — Tabbit Broser plugins for Deepseek Harness（✅ 活跃）
- [dsh-vision](https://github.com/oil-oil/dsh-vision) ⭐88 — Near-native image understanding for DeepSeek Harness（✅ 活跃）
- [dsh-annotation](https://github.com/omdsh-dev/dsh-annotation) ⭐87 — DSH Web 选中批注：选文字→批注→随消息发送，回复按批注逐条对照。（✅ 活跃）
- [dsh-chat-import](https://github.com/Nwflower/dsh-chat-import) ⭐87 — 从 Claude Code、Codex、ChatGPT、Cursor、Gemini、Reasonix、OpenCode 导入历史消息并在 DSH 中继续对话。（✅ 活跃）
- [dsh-commandcode-provider](https://github.com/Mars-Sea/dsh-commandcode-provider) ⭐83 — Unofficial DeepSeek Harness LLM provider plugin for Command Code: live model catalog, reasoning-effort support, Models-page card. Ported from pi-commandcode-provider (MIT).（✅ 活跃）
- [dsh-kun-like-pet](https://github.com/liyupi/dsh-kun-like-pet) ⭐80 — Kun Like 桌宠 —— DeepSeek Harness 桌面宠物插件：右下角小坤宠随 Agent 工作状态切换 9 种动作，任务完成播放「你干嘛~哎哟」（✅ 活跃）
- [dsh-notifier](https://github.com/THEWOLFWALKER/dsh-notifier) ⭐79 — Unified notification and remote-control plugin for DeepSeek Harness (DSH): one zero-dependency notify() API across 27 channels, with phone-friendly approvals/questions, six inbound control channels, and a loopback web console.（✅ 活跃）
- [dockyard-dsh](https://github.com/AITabby/dockyard-dsh) ⭐73 — A macOS-only native account-pool and provider plugin for DeepSeek Harness.（✅ 活跃）
- [dsh-dream-skin](https://github.com/RevolutionLA/dsh-dream-skin) ⭐73 — DSH Web 一键换肤插件：8 套原创主题、背景壁纸（透明度/模糊/渐变/URL）、每用户强调色、主题包导入导出与分享链接、收藏与随机，纯原生 token 系统。（✅ 活跃）
- [dsh-find-plugin](https://github.com/awesome-dsh-plugin/dsh-find-plugin) ⭐73 — 会话内插件发现：直接在 DSH 中搜索 GitHub dsh-plugin 主题的实时插件。（✅ 活跃）
- [dsh-notification](https://github.com/omdsh-dev/dsh-notification) ⭐70 — 回合完成桌面通知，按结果分控 + 关键词包含/排除过滤。（✅ 活跃）
- [dsh-stock-watch](https://github.com/Awu12277/dsh-stock-watch) ⭐68 — A股自选股实时行情盯盘插件 - DeepSeek Harness Web 右上角可折叠弹窗（✅ 活跃）
- [dsh-web-mobile](https://github.com/mexiaosqwq/dsh-web-mobile) ⭐68 — DSH Web UI 移动端适配：窄屏好用，宽屏适用（✅ 活跃）
- [dsh-permission-rules](https://github.com/PerryLink/dsh-permission-rules) ⭐65 — Claude Code-style declarative permission rules for DeepSeek Harness: ordered allow/deny/ask rules with tool-name, argument (glob/regex), and workspace-path matching on the tools/pre-execute waterfall, session-log audit, and HMR reload.（✅ 活跃）
- [dsh-plugin-hub](https://github.com/Noob-stupid/dsh-plugin-hub) ⭐64 — 插件管理面板：一键启停已装插件 + GitHub dsh-plugin 市场，带详情与一键安装。（✅ 活跃）
- [dsh-toy](https://github.com/c3ll256/dsh-toy) ⭐64 — Toy Control Protocol for DSH（✅ 活跃）
- [dsh-plugins-store](https://github.com/ZASENJC/dsh-plugins-store) ⭐62 — 自动收录与分类 GitHub dsh-plugin Topic 项目的静态目录网站。（✅ 活跃）
- [dsh-web-plugin-manager](https://github.com/LX2000WASD/dsh-web-plugin-manager) ⭐62 — Web UI 中一键管理 DSH 插件：查看、实时启停、安装/卸载、环境管理、插件市场。（✅ 活跃）
- [deepseek-harness-control-center](https://github.com/feibi-mochi/deepseek-harness-control-center) ⭐61 — DeepSeek Harness account monitoring, usage accounting, completion alerts, official recharge, flexible layout, and agent-assisted session controls. / 账户监控、提醒、充值与会话控制中心（✅ 活跃）
- [dsh-claude-ux](https://github.com/eri64/dsh-claude-ux) ⭐60 — DSH plugin: Claude-style Chinese risk control & conversation autonomy for DeepSeek Harness web（✅ 活跃）
- [dsh-memento](https://github.com/PerryLink/dsh-memento) ⭐59 — 有界分层、审批门控、可审计的跨会话记忆，支持冻结快照注入。（✅ 活跃）
- [dsh-balance-plugin](https://github.com/yxxbc/dsh-balance-plugin) ⭐57 — deepSeek 余额监控与用量统计（DSH 动态 Cordis 插件）：余额监控 · 官方充值入口 · 用量统计 · 三方插件管理（✅ 活跃）
- [dsh-open-in-vscode](https://github.com/omdsh-dev/dsh-open-in-vscode) ⭐53 — 从 Web GUI 直接在工作区中打开 VS Code 目录/文件。（✅ 活跃）
- [dsh-navbar](https://github.com/vlln/dsh-navbar) ⭐52 — DSH 插件：对话节点导航条（右缘节点串快速跳转 user 消息）。官方 bundle 插件，dsh plugin --profile web add 安装（✅ 活跃）
- [dsh-codex](https://github.com/Yan-Zero/dsh-codex) ⭐51 — Use your ChatGPT subscription in DeepSeek Harness through OpenAI's Codex sign-in flow（✅ 活跃）
- [deepseek-harness-skin](https://github.com/HeiGeAi/deepseek-harness-skin) ⭐49 — 换肤系统：21 套内置皮肤 + 一张图生成整套配色，构建期校验可读性。（✅ 活跃）
- [dsh-plugins](https://github.com/Ephemeral-AI-Lab/dsh-plugins) ⭐45 — Make Deepseek Harness Great（✅ 活跃）
- [dsh-smooth-stream](https://github.com/Laplace-bit/dsh-smooth-stream) ⭐45 — 丝滑流式渲染：字跟着模型到达走、换行滑入、不闪，滚动归用户，尊重 prefers-reduced-motion。（✅ 活跃）
- [dsh-status-rotator](https://github.com/01Virex/dsh-status-rotator) ⭐42 — 将 'Deep diving…' 状态替换为阶段感知的打字机消息。（✅ 活跃）
- [dsh-deepread](https://github.com/xiehuan123/dsh-deepread) ⭐41 — Evidence-first deep reading for AI agents — trace claims, evidence, confidence and knowledge maps across articles, books and PDFs.（✅ 活跃）
- [dsh-trace-compare](https://github.com/lamost423/dsh-trace-compare) ⭐41 — Trace Compare & Live Maze for DeepSeek Harness: visualize agent exploration (main path, detours, backtracks) from session logs or live sessions（✅ 活跃）
- [xgone/dsh-remote](https://github.com/xgone/dsh-remote) ⭐41 — 让 DeepSeek Harness 可以被安全地远程访问：账号密码认证 + MFA（TOTP）登录门禁、签名会话 Cookie、角色权限、浏览器内目录选择器、账号管理设置页。（🧪 实验性）
- [dsh-prompt-enhancer](https://github.com/Fishsb/dsh-prompt-enhancer) ⭐39 — DeepSeek Harness DSH 提示词增强插件：✨ 一键优化草稿，增强提示词。（✅ 活跃）
- [ui-status-label](https://github.com/alingalingling/ui-status-label) ⭐39 — 把鲸鱼娘思考时的 deep diving 状态自定义成任意文字。（✅ 活跃）
- [dsh-free-search](https://github.com/DDDMUC/dsh-free-search) ⭐38 — Free web search provider for DeepSeek Harness - DuckDuckGo backend, no API key needed（✅ 活跃）
- [dsh-plugin-mineru](https://github.com/HuanLinOTO/dsh-plugin-mineru) ⭐38 — 向模型暴露 MinerU 文档解析：PDF/图片/DOCX/PPTX/XLSX 转结构化 Markdown/JSON。（✅ 活跃）
- [dsh-expression](https://github.com/yyh-001/dsh-expression) ⭐36 — DeepSeek Harness 的表情包插件——找得到、发得出、学得会（✅ 活跃）
- [dsh-vision (william-jin-cmu)](https://github.com/william-jin-cmu/dsh-vision) ⭐36 — 视觉桥接：view_image 工具桥接任意 OpenAI 兼容 VLM，默认智谱免费档。（✅ 活跃）
- [dsh-message-edit](https://github.com/Moeblack/dsh-message-edit) ⭐35 — 分支式消息编辑、重掷、重试与版本时间线。（✅ 活跃）
- [dsh-codex-connect](https://github.com/franksong2702/dsh-codex-connect) ⭐34 — ChatGPT OAuth and Codex models for DeepSeek Harness.（✅ 活跃）
- [dsh-emoji](https://github.com/hellodigua/dsh-emoji) ⭐34 — 让 AI 回复加入自定义表情。（✅ 活跃）
- [dsh-omi-voice](https://github.com/PolinniZhong/dsh-omi-voice) ⭐34 — 沉浸式听朗读插件：对话内点读/暂停/继续，豆包 TTS 自然音色（BYOK），只读最终回答并过滤代码/表格/图形。（✅ 活跃）
- [billion-context-dsh](https://github.com/Tyan66666/billion-context-dsh) ⭐33 — 模型驱动的上下文管理（Active Context Pruning）：由模型决定何时压缩、压缩什么。（✅ 活跃）
- [dsh-mneme](https://github.com/modusensus/dsh-mneme) ⭐31 — 记忆主权归用户的本地跨会话记忆：SQLite + 可人工编辑的 Markdown 镜像，autoDream 后台巩固。（✅ 活跃）
- [dsh-remote](https://github.com/flymysql/dsh-remote) ⭐31 — 远程工作区：SSH 连接远程主机，用 rw_pick_workspace/rw_read_file/rw_exec 等工具远程操作。（✅ 活跃）
- [dsh-remote](https://github.com/Blank-not-black/dsh-Remote) ⭐31 — DSH Remote · 口袋里的 DSH 控制台 会话 · 审批 · 提问 · 文件传输，局域网 / Tailscale 直连 多服务器自动选优，聊天记录离线可看 带 Token 鉴权，数据只在你的设备之间流动 Sessions · approvals · questions · file transfer over LAN / Tailscale. Automatic fastest-server selection. Chat history available offline. Token-authenticated — your data flows only between your devices.（✅ 活跃）
- [dsh-whale-report](https://github.com/SenmuuuuW/dsh-whale-report) ⭐31 — 深迹 DeepTrace — Your Agent, in numbers. DSH 插件：从会话事件日志生成日报/周报/月报/年报/自定义区间，确定性洞察与协作复盘，只读、不改写历史。（✅ 活跃）
- [deepseek-harness-workbench-plugin](https://github.com/loadingvx/deepseek-harness-workbench-plugin) ⭐29 — Deepseek-harness-workbench-plugin（✅ 活跃）
- [dsh-full-remote](https://github.com/JUANWANG-BUAA/dsh-full-remote) ⭐29 — Auditable, token-gated DeepSeek Harness remote gateway: mobile QR access, per-device sessions, Host/Origin rewrite, settings/credentials/directory support.（✅ 活跃）
- [dsh-share](https://github.com/hellodigua/dsh-share) ⭐29 — DSH 对话一键分享。（✅ 活跃）
- [dsh-ui-whale](https://github.com/lhh010/dsh-ui-whale) ⭐29 — 会话标题栏全手绘像素鲸鱼伙伴：眨眼、摆尾、回合完成喷水，零核心改动。（✅ 活跃）
- [dsh-web-search-pro](https://github.com/anweat/dsh-web-search-pro) ⭐29 — 多引擎持久搜索：DeepSeek/Exa/DDG/Bing/Jina + GitHub/B站/YouTube/V2EX/小红书/推特/Reddit/RSS，SQLite+LRU 缓存 + Playwright 渲染。（✅ 活跃）
- [ego-browser](https://github.com/Fisfzy/ego-browser) ⭐29 — 把 ego-lite 智能体浏览器（为 AI Agent 打造的 Chromium）接入 DSH，13 个结构化工具。（✅ 活跃）
- [deepseek-harness-snowsalt](https://github.com/KYZHXL/deepseek-harness-snowsalt) ⭐28 — 雪盐主题皮肤。（✅ 活跃）
- [dsh-files](https://github.com/taxueseek/dsh-files) ⭐28 — DeepSeek Harness dual-face plugin: session-isolated file upload with colorful composer cards + read_document tool (text/PDF/DOCX/XLSX) with content sniffing and LRU caching（✅ 活跃）
- [dsh-openmaic](https://github.com/THU-MAIC/dsh-openmaic) ⭐28 — OpenMAIC for DeepSeek Harness: classrooms, slides, interactive widgets, and Socratic teaching（✅ 活跃）
- [dsh-plugin-guard](https://github.com/lxzy-7/dsh-plugin-guard) ⭐28 — Install safety net for DeepSeek Harness: pre-install snapshots, one-click/automatic rollback, guarded boot, and incident reports that auto-trigger agent analysis. 中文: DeepSeek Harness 插件安装安全网（安装前自动快照、一键/自动回退、守护启动、事故报告自动触发 Agent 分析）。（✅ 活跃）
- [dsh-plugin-check](https://github.com/omdsh-dev/dsh-plugin-check) ⭐27 — 插件健康检查：清单协议、patch 格式、构建陷阱与 hub 收录状态，零依赖只读。（✅ 活跃）
- [dsh-codex-subscription](https://github.com/WSL043/dsh-codex-subscription) ⭐26 — ChatGPT/Codex subscription provider for DeepSeek Harness with OAuth, models, quota, search, and image tools—no API key or Codex CLI.（✅ 活跃）
- [dsh-computer-use](https://github.com/Anionex/dsh-computer-use) ⭐26 — 为 DeepSeek Harness 提供电脑控制插件：新鲜 Accessibility 观测、过期状态拒绝、作用域权限与安全输入（目前支持macos）｜Accessibility-first macOS Computer Use bundle for DSH with fresh observations, stale-state rejection, scoped permissions, and safe input.（✅ 活跃）
- [dsh-quant](https://github.com/pengpengyi92/dsh-quant) ⭐26 — "🐳 Dsh-Quant: The Everything-Plugin Ai native Quant OS "（✅ 活跃）
- [dsh-theme-cyberpunk2077](https://github.com/Tommy00748/dsh-theme-cyberpunk2077) ⭐26 — Cyberpunk 2077 / Night City theme for the DeepSeek Harness Web UI — CRT scanlines, Kiroshi lock-on, typewriter SFX, Relic glitch & easter eggs（✅ 活跃）
- [dsh-web-lan-access](https://github.com/AcidGr/dsh-web-lan-access) ⭐26 — DeepSeek Harness (dsh) Web plugin（✅ 活跃）
- [dsh-auto-memory](https://github.com/Aik358/dsh-auto-memory) ⭐25 — DSH 自动记忆插件:三层记忆(用户级/项目笔记/每日日志)自动注入与检索、每日反思、可视化面板与设置页,支持继承其他 AI 工具的历史记忆。An auto-memory plugin for the DeepSeek Harness Web GUI: three-layer memory (user-level / project notes / daily logs) with automatic injection and retrieval, daily reflections, a visual panel and settings page, and inheritance of memories from other AI tools.（✅ 活跃）
- [dsh-maid-whale-webui](https://github.com/yunxiiQwQ/dsh-maid-whale-webUI) ⭐25 — DeepSeek Harness Web UI 鲸鱼女仆主题插件（✅ 活跃）
- [dsh-minigames](https://github.com/lhh010/dsh-minigames) ⭐25 — DSH Web UI 右侧小游戏面板：18 款离线小游戏（恐龙跳一跳 / 俄罗斯方块 / 坦克大战 / 扫雷 / 2048 / 数独 / 吃豆人 / 跟枪练习等），可扩展游戏注册表，等待模型回复或修 bug 时的摸鱼神器（✅ 活跃）
- [dsh-plugin-workshop](https://github.com/yyyyukari/dsh-plugin-workshop) ⭐25 — Steam 创意工坊风格插件浏览器：零服务器、GitHub 驱动搜索、一键安装。（✅ 活跃）
- [dsh-scholar](https://github.com/lzszq/dsh-scholar) ⭐25 — dsh-scholar（✅ 活跃）
- [dsh-win32](https://github.com/sjh9714/dsh-win32) ⭐25 — Fix and diagnose DeepSeek Harness on native Windows. Official PowerShell, Workspace Write, shortcuts, and legacy preset repair. No WSL.（✅ 活跃）
- [dsh-custom-tool](https://github.com/omdsh-dev/dsh-custom-tool) ⭐24 — 用 Monaco 编辑器创建和管理 DSH 沙箱化 JavaScript 工具，模型驱动工具列表。（✅ 活跃）
- [dsh-diff-viewer](https://github.com/lehhair/dsh-diff-viewer) ⭐24 — PiUI 风格 Web diff 查看器，替代默认 diff 视图。（✅ 活跃）
- [dsh-qq2006](https://github.com/LaplaceYoung/dsh-qq2006) ⭐24 — DSH (DeepSeek Harness) 的 QQ2006 皮肤插件：注册 qq2006 主题、镜像 body[data-ds-skin]、全局皮肤表与完整素材（✅ 活跃）
- [dsh-recall-plugin](https://github.com/limbo947/dsh-recall-plugin) ⭐24 — DSH 消息撤回插件：回到发送该消息时的状态 DSH Message Recall Plugin: Return to the state when the message was sent（✅ 活跃）
- [dsh-toolkit](https://github.com/omdsh-dev/dsh-toolkit) ⭐24 — 零依赖工具包：计算器、CSV、diff、编码、JSON、Markdown、正则、时间。（✅ 活跃）
- [dsh-balance](https://github.com/crazywoola/dsh-balance) ⭐23 — 设置页余额插件。（✅ 活跃）
- [dsh-plugin-better-sidebar-plugin-office](https://github.com/HuanLinOTO/dsh-plugin-better-sidebar-plugin-office) ⭐23 — 为 better-sidebar 提供 Office 三件套预览（.docx/.xlsx/.pptx），独立瘦身 bundle。（✅ 活跃）
- [dsh-xiaoyao-skins](https://github.com/147228/dsh-xiaoyao-skins) ⭐23 — 夕小瑶 × DeepSeek Harness Web 皮肤合集、安装器与社区创作工具链（✅ 活跃）
- [dsh-catppuccin-theme](https://github.com/NoNameLeGo/dsh-catppuccin-theme) ⭐22 — DeepSeek Harness Web GUI 的 Catppuccin 主题插件：Latte / Frappé / Macchiato / Mocha 四种主题一键切换，内置可开关的玻璃质感（Glassmorphism）（✅ 活跃）
- [dsh-focus-chat](https://github.com/dingyi222666/dsh-focus-chat) ⭐21 — 为 dsh 提供新的「聚焦会话」精简会话视图，更轻松易于阅读，只关注最终产出结果。（✅ 活跃）
- [dsh-plugin-pet-rs](https://github.com/HuanLinOTO/dsh-plugin-pet-rs) ⭐21 — Rust 桌宠：5 态鲸鱼 + 双 SSE 实时推送 + 透明置顶窗 + 系统托盘，三端支持。（✅ 活跃）
- [dsh-solo-thinking](https://github.com/fredalxin/dsh-solo-thinking) ⭐21 — Solo-style isolated brainstorm branches and Handoffs for DeepSeek Harness（✅ 活跃）
- [dsh-stickers](https://github.com/william-jin-cmu/dsh-stickers) ⭐21 — DSH WebUI sticker plugin for bidirectional user and agent reactions（✅ 活跃）
- [dsh-web-ui-notify](https://github.com/bill9109/dsh-web-ui-notify) ⭐21 — 为 DSH 增加桌面通知提醒。（✅ 活跃）
- [dsh-any-background](https://github.com/Tkingxiao/dsh-any-background) ⭐20 — Deepseek Harness 自定义主题插件，支持自定义图片/视频壁纸，对话框，侧边栏等透明度模糊度调整，全局主题色的色轮调整插件（✅ 活跃）
- [dsh-clawrouter](https://github.com/BlockRunAI/dsh-clawrouter) ⭐20 — A safety gate for DeepSeek Harness: a stronger model reviews dangerous tool calls before they run. Plus vision and BlockRun's full model catalog from one wallet, paid per request over x402.（✅ 活跃）
- [dsh-drag-and-drop](https://github.com/bill9109/dsh-drag-and-drop) ⭐20 — DSH Web UI 跨平台文件拖拽与原始路径插入，无需复制文件。（✅ 活跃）
- [dsh-file-upload](https://github.com/HongMing-Huang/dsh-file-upload) ⭐20 — DeepSeek Harness (dsh) file-message plugin: Claude-style drag-and-drop / paperclip upload, content sniffing, document-to-Markdown via Microsoft MarkItDown (with built-in JS fallback), text inlining, read_document tool for agents.（✅ 活跃）
- [dsh-llm-fallbacks](https://github.com/omdsh-dev/dsh-llm-fallbacks) ⭐20 — An dsh plugin for role-based LLM retry&fallback strategy. 基于角色的模型重试备用策略插件（✅ 活跃）
- [dsh-agy](https://github.com/chaos-03x/dsh-agy) ⭐19 — Google Antigravity (agy) OAuth auth + model access plugin for DeepSeek Harness: multi-account pool, 429 rotation, device fingerprinting, CLI and web login.（✅ 活跃）
- [dsh-balance-meter](https://github.com/Ghost011118/dsh-balance-meter) ⭐19 — DeepSeek account balance and session cost readout for the DeepSeek Harness Web GUI（✅ 活跃）
- [dsh-better-edit](https://github.com/Rianico/dsh-better-edit) ⭐19 — Hash-anchored read/edit/undo_last_edit tools for DeepSeek Harness (dsh), fewer token consumption, lower cost.（✅ 活跃）
- [dsh-skin](https://github.com/KinGao294/dsh-skin) ⭐19 — Codex 风格皮肤切换器 + 自定义半透明壁纸，支持透明度/模糊控制。（✅ 活跃）
- [dsh-theme-plugin](https://github.com/nevertoday/dsh-theme-plugin) ⭐19 — Chinese traditional colors as a DeepSeek Harness theme pack.（✅ 活跃）
- [dsh-user-experience](https://github.com/DietCokewithSugar/dsh-user-experience) ⭐19 — Persona-driven UX walkthrough plugin for DeepSeek Harness (DSH) - scans React + TypeScript source code for UX issues, pinpoints them, and suggests fixes.（✅ 活跃）
- [dsh-whale-galgame](https://github.com/JAdpp/dsh-whale-galgame) ⭐19 — 工作推gal两不误~面向DeepSeek Harness的跨会话事件感知Galgame引擎与界面插件，支持鲸鱼娘/GPT/Claude/Grok/Gemini/Kimi多位模型娘角色（✅ 活跃）
- [compass](https://github.com/dshakes/compass) ⭐18 — 🧭 Let your coding agent off the leash — not off the rails. Guardrails, a hard budget cap & a self-fixing PR loop for Claude Code / Codex / Gemini. Eval-gated 100/100, you always merge.（✅ 活跃）
- [dsh-milestone](https://github.com/SnowCrescenter-tech/dsh-milestone) ⭐18 — Git 风格里程碑时间线：悬停查看元数据，点击跳转任意消息。（✅ 活跃）
- [dsh-outline](https://github.com/urzeye/dsh-outline) ⭐18 — DeepSeek Harness（DSH）Web GUI 的实时大纲插件，移植自 Ophel Atlas（✅ 活跃）
- [dsh-provider-model-configurator](https://github.com/LiangYin233/dsh-provider-model-configurator) ⭐18 — DSH 模型 Pro:为 DSH WebUI 提供将 pi-ai 预设或任意已配置提供商的模型上下文、输出上限、推理档位与兼容开关一键应用到目标提供商,并集中查看、新建、编辑、复制与删除各提供商模型条目的能力。（✅ 活跃）
- [dsh-recommend](https://github.com/zp-home/dsh-recommend) ⭐18 — 透明插件排行榜与推荐：每日自动抓取 dsh-plugin 主题数据，开放评分模型。（✅ 活跃）
- [touhou-hakurei](https://github.com/xiake595/touhou-hakurei) ⭐18 — 灵梦（Reimu）·博丽神社（东方Project）美化版皮肤：神社昼夜实景背景、灵梦立绘、画框侧边栏与输入框、纸白透明界面 — DeepSeek Harness Web GUI skin（✅ 活跃）
- [webdsh](https://github.com/futrime/webdsh) ⭐18 — Running DeepSeek Harness on web（✅ 活跃）
- [DeepSeek-Harness-Web-Tools](https://github.com/tonyd2wild/DeepSeek-Harness-Web-Tools) ⭐17 — 免费免密钥的 web_search/web_fetch，DuckDuckGo 驱动，无需注册。（✅ 活跃）
- [dsh-computer-use](https://github.com/988hj7tczd-oss/dsh-computer-use) ⭐17 — Computer Use 插件：虚拟鼠标真人操作 for DeepSeek Harness（screen_observe + computer_click 等 11 个模型友好工具，跨平台 cua-driver 引擎）（✅ 活跃）
- [dsh-context-doctor](https://github.com/Zhenyu98/dsh-context-doctor) ⭐17 — 上下文注入审计插件：统计 AGENTS.md 指令链/技能目录/工具 schema 的 token 成本，检测重复与冲突。（✅ 活跃）
- [dsh-group-photo](https://github.com/SenmuuuuW/dsh-group-photo) ⭐17 — DSH 内测收官合影墙：GitHub OAuth 零权限登录 + 冻结白名单校验的拍立得合影站（含 DSH Skill 包装）（✅ 活跃）
- [dsh-gui-customization](https://github.com/LAN-TINA-WS/dsh-gui-customization) ⭐17 — DeepSeek Harness 时装工坊：给 DSH 界面换装——更改主题配色/自定义背景图/自定义视频背景/可调节氛围灯，中英双语 ·DSH Web UI 时装工坊。（✅ 活跃）
- [dsh-passwords](https://github.com/slywalker2006/dsh-passwords) ⭐17 — dsh-passwords: DeepSeek Harness login gateway - first-run setup, at-rest encryption, brute-force lockout, audit log, HTTPS（✅ 活跃）
- [dsh-plugin-writing-guard](https://github.com/xmutfyh/dsh-plugin-writing-guard) ⭐17 — DeepSeek Harness (DSH) academic writing guard for papers — 论文去AI味 / AI-writing style detection, evidence preservation, journal-fit calibration, manuscript proofreading, writing_audit & automatic checks. Local, zero network, zero LLM.（✅ 活跃）
- [dsh-advisor](https://github.com/omdsh-dev/dsh-advisor) ⭐16 — Advisor - Pair a second model that passively reviews each turn and injects notes.  搭配一个会在每轮对话被动注入见解和审查的副模型。（✅ 活跃）
- [dsh-continual-evolve](https://github.com/ZK-Andy/dsh-continual-evolve) ⭐16 — Continual self-evolution plugin for DeepSeek Harness: versioned, auditable, rollback-safe harness state refined from session trajectories, with a benchmark-driven validation loop.（✅ 活跃）
- [dsh-session-notification](https://github.com/dingyi222666/dsh-session-notification) ⭐16 — 提供会话完成等四种状态的通知响应，支持浏览器提示和提示词（✅ 活跃）
- [dsh-side-panel](https://github.com/ccq1/dsh-side-panel) ⭐16 — 紧凑侧边栏：文件浏览器、终端与 Git 审查。（💤 停更）
- [dsh-codex-oauth](https://github.com/WNJXYK/dsh-codex-oauth) ⭐15 — Use your OpenAI subscription with DeepSeek Harness to access GPT models, image generation, and web search.（✅ 活跃）
- [dsh-md-notes](https://github.com/XieZongChen/dsh-md-notes) ⭐15 — A note-taking plugin for DeepSeek Harness (DSH). It provides a full MD notes manager and MD notes editor, letting you quickly capture conversation content into notes. Notes can be maintained by syncing to a Git repository（✅ 活跃）
- [dsh-sentinel](https://github.com/fuhefei/dsh-sentinel) ⭐15 — Condition-driven wakeup for DeepSeek Harness: durable file/command/http/process/webhook watches that wake the agent, with dock, sidebar branch, and a global dashboard.（✅ 活跃）
- [dsh-stock-market](https://github.com/AnacondaKC/dsh-stock-market) ⭐15 — 股票行情插件（整活：有效解决了写代码时账户不能同时亏钱的 BUG）。（✅ 活跃）
- [dsh-web-review](https://github.com/CanglongCl/dsh-web-review) ⭐15 — DeepSeek Harness Web GUI 的网页预览与元素批注插件，让 AI 根据可视化反馈直接修改前端源码。（✅ 活跃）
- [deepseek-harness-zh_pro](https://github.com/magian1127/deepseek-harness-zh_pro) ⭐14 — Chinese enhancement plugin for DeepSeek Harness (DSH) - DSH 中文增强插件（✅ 活跃）
- [dsh-ai4scholar](https://github.com/literaf/dsh-ai4scholar) ⭐14 — AI4Scholar for DeepSeek Harness (dsh): 38 native academic tools — Semantic Scholar, PubMed, Google Scholar, arXiv, bioRxiv/medRxiv, DOI, full text, auto-cite, figures, unified search. Powered by ai4scholar.net（✅ 活跃）
- [dsh-gomoku](https://github.com/omdsh-dev/dsh-gomoku) ⭐14 — 在 DSH 中与 AI 下五子棋，也可以让 AI 对局比试模型强弱。（✅ 活跃）
- [dsh-live2d-pets](https://github.com/cyanfish-x/dsh-live2d-pets) ⭐14 — Live2D 桌宠插件 for DeepSeek Harness：Agent 状态镜像 + 互动陪伴，内置宽松许可预设模型 / Live2D pet plugin: agent state mirror + interactive companion with curated permissive-license presets（✅ 活跃）
- [dsh-plugin](https://github.com/loongsuite/dsh-plugin) ⭐14 — OpenTelemetry tracing for DeepSeek Harness (dsh): turns each agent turn into a GenAI span tree — steps, LLM calls with TTFT, tool executions, token usage — exported over standard OTLP to Jaeger, Grafana Tempo, SigNoz, Langfuse, or any compatible backend.（✅ 活跃）
- [dsh-codex-auth](https://github.com/suntianc/dsh-codex-auth) ⭐13 — DeepSeek Harness plugin that reuses the local Codex CLI ChatGPT login and adds a native GPT Auth settings card（✅ 活跃）
- [dsh-compaction-instant](https://github.com/TsFreddie/dsh-compaction-instant) ⭐13 — LLM-free lossless* compaction engine for DeepSeek Harness（✅ 活跃）
- [dsh-deepcel](https://github.com/Small-tailqwq/dsh-deepcel) ⭐13 — Excel 风格电子表格皮肤。（✅ 活跃）
- [dsh-nested-followups](https://github.com/sluminositys/dsh-nested-followups) ⭐13 — Ask a follow-up on any past answer in an isolated branch, keeping your main conversation clean. 针对任意历史回答发起追问，新问题在独立分支中展开，主对话保持干净。A conversation-tree plugin for DeepSeek Harness / DeepSeek Harness 会话树插件。（✅ 活跃）
- [dsh-opencode-go-usage](https://github.com/Xenia0922/dsh-opencode-go-usage) ⭐13 — DeepSeek Harness 插件:OpenCode Go 用量与花费悬浮仪表盘(配额、逐请求成本、模型/来源分布)（✅ 活跃）
- [dsh-pet](https://github.com/FlytoMAYDAY80/dsh-pet) ⭐13 — 🐋 DSH 有声桌宠：悬浮桌面的 DeepSeek 小鲸鱼，不打开 DSH 也能实时感知会话状态（需要确认/工作中/完成/空闲/离线），支持音效提醒与零代码定制素材（✅ 活跃）
- [dsh-plugin-aigc-canvas](https://github.com/HuanLinOTO/dsh-plugin-aigc-canvas) ⭐13 — provider-agnostic AIGC HTTP 桥 + 无限画布 + ffmpeg 后处理，13 个工具含画布连边/reroll/媒体编辑 | Provider-agnostic AIGC HTTP bridge + infinite canvas + ffmpeg post-processing; 13 tools incl. canvas linking/reroll/media-edit（✅ 活跃）
- [dsh-security-audit](https://github.com/omdsh-dev/dsh-security-audit) ⭐13 — DSH 本机安全审计插件：配置/插件来源/会话/网络暴露面，只读脱敏风险报告（✅ 活跃）
- [dsh-token-usage](https://github.com/LeemanCheung/dsh-token-usage) ⭐13 — Persistent token usage records and dashboard for DeepSeek Harness（✅ 活跃）
- [dsh-update-checker](https://github.com/Airmetro/dsh-update-checker) ⭐13 — DeepSeek Harness 主程序与插件更新管理：npm/GitHub 双源 semver 比对、多语言横幅、一键更新（主程序自动备份/校验/回滚，插件临时目录安装）、更新后看门狗重启。Update management for DeepSeek Harness and its plugins: dual-source semver checks, locale banner, one-click updates with backup/rollback, watchdog restart.（✅ 活跃）
- [dsh-vision-opencode](https://github.com/poiuyjie/dsh-vision-opencode) ⭐13 — DSH plugin: Auto-convert images to text for pure-text LLMs (DeepSeek etc.) via any vision model. No need to switch your main model.（✅ 活跃）
- [DeepSeek-Harness-Vision-Tools](https://github.com/tonyd2wild/DeepSeek-Harness-Vision-Tools) ⭐12 — 视觉代理：任意文本模型 + 任意视觉模型即可让 DSH 看图。（✅ 活跃）
- [dsh-cyber-particle](https://github.com/AKS1st/dsh-cyber-particle) ⭐12 — 为 DeepSeek Harness Web 界面添加动态粒子网络背景 | Particle-network background plugin for DeepSeek Harness web（✅ 活跃）
- [dsh-eval-harness](https://github.com/BiBoyang/dsh-eval-harness) ⭐12 — DSH 插件评测工具：YAML 用例驱动真实 agent 回归评测 + baseline 对比 PASS/WARN/FAIL 门禁｜Regression eval harness for DeepSeek Harness plugins（✅ 活跃）
- [dsh-evolve](https://github.com/william-jin-cmu/dsh-evolve) ⭐12 — 自进化插件：agent 在 session 内随对话给自己长出/剪掉能力 —— evolve_add 热挂载持久化 cordis 插件（下一 step 工具即可见），evolve_remove 可逆卸载，重启自动恢复（✅ 活跃）
- [dsh-openai-codex-auth](https://github.com/yoke233/dsh-openai-codex-auth) ⭐12 — OpenAI Codex OAuth login and usage card plugin for DeepSeek Harness（✅ 活跃）
- [dsh-side-chat](https://github.com/heartmove/dsh-side-chat) ⭐12 — 一个 DSH 网页插件，Codex 式侧边聊天的强化版本： 在右侧面板提供按主会话隔离的独立聊天，具备 Codex 式的智能体能力——继承主会话的 工具集、模型、思考难度与权限预设，能感知所在工作目录；选中对话内容即可提问，AI 回复 也能带回主会话（直接带回或摘要后带回，写入草稿或注入为折叠提示行）。  在 Codex 式能力之上，它额外支持：当主会话的智能体弹出问题弹框向你提问时，可以 把问题与各个选项带入侧边聊天、让 AI 帮你分析，不必打断当前流程——想清楚后把答案 带回，再回答弹框即可。（✅ 活跃）
- [dsh-surfing-plugin](https://github.com/cyijun/dsh-surfing-plugin) ⭐12 — SearXNG search and Crawl4AI fetch providers for DeepSeek Harness（✅ 活跃）
- [dsh-trading](https://github.com/maddogfinance/dsh-trading) ⭐12 — 纯研究型交易工作台插件：类型化行情数据缝（自带 provider）、多周期指标快照、带溯源门控标注的交互图表卡片，以及拒绝执行型工具调用的风险护栏——架构上不提供执行能力。（✅ 活跃）
- [weshop-dsh-plugin](https://github.com/weshopai/weshop-dsh-plugin) ⭐12 — Native WeShop Cordis plugin for DeepSeek Harness. Allow you to use infinite canvas with infinite creative skills.（✅ 活跃）
- [dsh-balance](https://github.com/TwotwoPiggy/dsh-balance) ⭐11 — dsh余额插件. A DeepSeek Harness plugin for real-time token tracking and highly accurate session cost estimation, featuring dynamic peak/off-peak pricing support.（✅ 活跃）
- [dsh-chat-imagine](https://github.com/corrinehu/dsh-chat-imagine) ⭐11 — 在 DSH 聊天窗口自动调用生图工具（API 渠道，或本机 CLI：已支持mmx / codex / agy）并展示图片，也支持利用对应 CLI 识别图片。（✅ 活跃）
- [dsh-client-ui-skins](https://github.com/caoyiwei850/dsh-client-ui-skins) ⭐11 — DSH Web skin plugin with built-in themes and custom image skins（✅ 活跃）
- [dsh-expert-mode](https://github.com/Asher-2000/dsh-expert-mode) ⭐11 — DSH (DeepSeek Harness) 专家模式 agent preset — 首席协调官 + 17位领域专家子代理 Expert-mode preset for DeepSeek Harness（✅ 活跃）
- [dsh-file-mentions](https://github.com/a903067276-rgb/dsh-file-mentions) ⭐11 — 回复中文件路径可点击：内联打开、文件管理器揭示、提及文件芯片列表。（✅ 活跃）
- [dsh-file-mount](https://github.com/acefun29/dsh-file-mount) ⭐11 — 增量文件挂载 + 行区间去重：相同文件内容不再重复发送给模型。（✅ 活跃）
- [dsh-lsp-actions](https://github.com/PerryLink/dsh-lsp-actions) ⭐11 — LSP action surface for DeepSeek Harness: diagnostics, formatting, completion, code actions, symbols, signature help, inlay hints, and rename tools over language servers（✅ 活跃）
- [dsh-mermaid](https://github.com/AKS1st/dsh-mermaid) ⭐11 — 在 DSH Web 会话中把 Mermaid 代码围栏渲染为 SVG 图表 | Render Mermaid code fences as SVG diagrams in DSH Web messages（✅ 活跃）
- [dsh-plugin-integration](https://github.com/MutaLucem/dsh-plugin-integration) ⭐11 — DeepSeek Harness (DSH) 插件整合中心：动态发现、打标分类、重叠/兼容检测、一键启停与失效检测（✅ 活跃）
- [dsh-plugin-ya-workspace-sidebar](https://github.com/HuanLinOTO/dsh-plugin-ya-workspace-sidebar) ⭐11 — DSH Web 工作区侧栏替代，顶部全局最近会话 + Workspace→Session 二级菜单 + 面包屑 | DSH Web workspace sidebar replacement: top global recent sessions + Workspace→Session two-level menu + breadcrumbs（✅ 活跃）
- [dsh-ramify](https://github.com/yanglongyun/ramify-dsh) ⭐11 — Ramify 是 DeepSeek Harness 的创意分支画布插件，用树状工作区生成、对比和迭代多个可交互方案。（✅ 活跃）
- [dsh-sdk-platform-rs](https://github.com/kpn-dsh/dsh-sdk-platform-rs) ⭐11 — A Rust SDK to interact with the DSH Platform. This library provides convenient building blocks for services that need to connect to DSH Kafka, fetch tokens for various protocols, manage Prometheus metrics, and more.（✅ 活跃）
- [dsh-sticky-note](https://github.com/Meredith2328/dsh-sticky-note) ⭐11 — 左下角便签：随手记点子/感想/TODO，实时保存到归档目录，清单+悬浮归档（✅ 活跃）
- [oh-my-dsh](https://github.com/NoWint/Oh-My-DSH) ⭐11 — 🐋 Oh-My-DSH — DeepSeek Harness Plugin Ecosystem【每一小时更新】（✅ 活跃）
- [context-vista](https://github.com/GooodWei/context-vista) ⭐10 — 上下文/Token 实时监控：悬浮面板 + /context 命令，环形图展示用量、分配与估算费用。（✅ 活跃）
- [dsh-balance-monitor](https://github.com/jelly-000/dsh-balance-monitor) ⭐10 — Multi-provider AI balance, quota, and token usage for the dsh sidebar, with a daily heatmap.（✅ 活跃）
- [dsh-latex-tools](https://github.com/liuup/dsh-latex-tools) ⭐10 — ♾️ Copy and export the LaTeX in DeepSeek Harness 悬停任意 LaTeX 公式即可复制 TeX 源码或导出为独立的 SVG 文件（✅ 活跃）
- [dsh-plugin-anti-ads](https://github.com/HuanLinOTO/dsh-plugin-anti-ads) ⭐10 — DSH Web 广告拦截器，四层独立防御拦截 dsh-ads 插件的所有广告位 | DSH Web ad blocker with four independent defense layers targeting the dsh-ads plugin（✅ 活跃）
- [dsh-ui-appearance](https://github.com/TQSY114514/dsh-ui-appearance) ⭐10 — Appearance customization plugin for DeepSeek Harness: theme color palette, background image, opacity/blur, glass effect（✅ 活跃）
- [dsh-usage-chart](https://github.com/Max-Samson/dsh-usage-chart) ⭐10 — A DeepSeek Harness Web plugin for real-time Token usage, cost estimates, per-round charts, and DeepSeek API balance.（✅ 活跃）
- [dsh-web-billing](https://github.com/bpc-oss/dsh-web-billing) ⭐10 — DSH Web 中英文金额 Token 计费：官方策略自动定价（含高峰/低谷），逐条消息费用台账。（✅ 活跃）
- [DeepSeek-Harness-billing-plugin](https://github.com/WilliamLIiii/DeepSeek-Harness-billing-plugin) ⭐9 — 账户余额 + 按模型剩余任务估算，带会话费用台账。（✅ 活跃）
- [dsh-awiki](https://github.com/AgentConnect/dsh-awiki) ⭐9 — AWiki identity and messaging plugin for DeepSeek Harness（✅ 活跃）
- [dsh-bash-win](https://github.com/zimzaza4/dsh-bash-win) ⭐9 — 在 Windows 环境中为 DeepSeek Harness 提供 Git Bash 与 WSL 2 bash 工具,含 bwrap 沙箱、审批模式、后台任务（✅ 活跃）
- [dsh-client-ui-skin-claude](https://github.com/PAKIKNOWLEDGE/dsh-client-ui-skin-claude) ⭐9 — Claude-style skin for DeepSeek Harness (dsh) Web GUI — warm-black canvas, Anthropic clay accent, serif UI（✅ 活跃）
- [dsh-explorer](https://github.com/No-PRM/dsh-explorer) ⭐9 — DSH plugin: VS Code-style file-tree explorer (git decorations, preview, diff, drag-to-reference); install via dsh plugin --profile web add.（✅ 活跃）
- [dsh-hud](https://github.com/a903067276-rgb/dsh-hud) ⭐9 — HUD 状态面板：浮动侧栏展示 git 状态、MCP 服务器、技能、模型与 token 用量。（✅ 活跃）
- [dsh-paste-input](https://github.com/lhh010/dsh-paste-input) ⭐9 — DSH WebUI 文件输入增强：Ctrl+V 粘贴、拖拽、选择文件，发送时复制进会话工作区。（✅ 活跃）
- [dsh-plugin-auto-blame](https://github.com/HuanLinOTO/dsh-plugin-auto-blame) ⭐9 — 模型回合结束后用 LLM 生成 3 条批判性跟进建议，点击即发送 | After a model turn, an LLM generates 3 critical follow-up suggestions shown as click-to-send chips（✅ 活跃）
- [dsh-plugin-interpreters](https://github.com/HuanLinOTO/dsh-plugin-interpreters) ⭐9 — 暴露 run_python/run_node 工具，通过 stdin 执行代码返回 stdout/stderr/exit。（✅ 活跃）
- [dsh-plugin-smooth-stream](https://github.com/SpookySandwich/dsh-plugin-smooth-stream) ⭐9 — DSH 流式渲染插件：按段落分批呈现、8 种入场动画、平滑滚动、设置面板。DeepSeek Harness: paragraph-batched streaming reveals, 8 designed animations, smooth scroll-follow and a settings panel.（✅ 活跃）
- [dsh-spotlight](https://github.com/0xsline/dsh-spotlight) ⭐9 — DSH Web 键盘优先命令面板。（✅ 活跃）
- [dsh-web-archive](https://github.com/renat3u/dsh-web-archive) ⭐9 — 折叠对话当中众多的“无用消息”，例如Think、Bash等（✅ 活跃）
- [dsh-webui-auth](https://github.com/Yuuz12/dsh-webui-auth) ⭐9 — WebUI 身份认证：HTTP/传输层强制登录（资源、插件 bundle、/api、WebSocket 四层防护），服务端会话 + HttpOnly Cookie。（✅ 活跃）
- [deepseek-harness-SupportVisionModel](https://github.com/TryDing-T/deepseek-harness-SupportVisionModel) ⭐8 — 基于 deepseek-harness 二次开发：支持单独配置视觉模型读图。（✅ 活跃）
- [dsh-api-balance](https://github.com/02Muller25/dsh-api-balance) ⭐8 — 安装在deepseek的插件，能够实时显示当前api的余额，30秒自动刷新一次（✅ 活跃）
- [dsh-approval-llm](https://github.com/Letter2025/dsh-approval-llm) ⭐8 — Model-based permission approval (approve-for-me) for DeepSeek Harness: an approval/request answerer backed by a separate reviewer model（✅ 活跃）
- [dsh-balance-tide](https://github.com/huanyuLv/dsh-balance-tide) ⭐8 — DeepSeek Harness (DSH) Web 插件: 余额 + 峰谷计价潮汐提示。显示 DeepSeek 账户余额与本会话花费, 并在余额前提示当前峰/谷价格档位、距切换倒计时与使用建议。（✅ 活跃）
- [dsh-bash-encoding](https://github.com/lhh010/dsh-bash-encoding) ⭐8 — DSH bash 输出编码自动识别插件：替换 ctx.bash，自管 spawn 收集原始字节，自动检测 UTF-16LE/UTF-8/GBK 等编码并正确解码，修复 WSL/Windows 下 bash 工具的中文乱码。（✅ 活跃）
- [dsh-deepseek-vision](https://github.com/siegfly/dsh-deepseek-vision) ⭐8 — Vision-language gateway plugin for DeepSeek Harness - paste an image, DeepSeek sees text（✅ 活跃）
- [dsh-opencodego-usage](https://github.com/BeiZi6/dsh-opencodego-usage) ⭐8 — DSH Web GUI plugin: OpenCodeGo quota breathing light + liquid-glass panel with rolling/weekly/monthly progress bars (作者 Xu Yuanshan)（✅ 活跃）
- [dsh-plugin-d399](https://github.com/HuanLinOTO/dsh-plugin-d399) ⭐8 — 模型生成时右下角弹出小游戏菜单：Wordle/消消乐/192 款参数化小游戏。（✅ 活跃）
- [dsh-session-health](https://github.com/omdsh-dev/dsh-session-health) ⭐8 — 多帧 zstd 会话文件的帧级扫描诊断：撕裂/损坏/空会话检测，零依赖只读。（✅ 活跃）
- [dsh-ssh](https://github.com/UynajGI/dsh-ssh) ⭐8 — SSH remote-execution plugin for DeepSeek Harness: ProxyJump chain, SFTP filesystem, subprocess and PTY over ssh2（✅ 活跃）
- [dsh-tool-calculator](https://github.com/omdsh-dev/dsh-tool-calculator) ⭐8 — DSH 计算器工具插件：安全的数学表达式求值器，零依赖递归下降解析器（✅ 活跃）
- [dsh-ui-progress](https://github.com/lhh010/dsh-ui-progress) ⭐8 — DSH Web UI 会话进度插件：输入框停靠区常驻会话进度条（todos 真实进度 / 实时 token 生成速率 / 中断橘红态 / 待办提醒），零核心改动（✅ 活跃）
- [dsh-usage-dashboard](https://github.com/Cassius0924/dsh-usage-dashboard) ⭐8 — DeepSeek 额度与用量仪表盘 — DSH (DeepSeek Harness) 动态 Cordis 插件（✅ 活跃）
- [dsh-browser](https://github.com/anweat/dsh-browser) ⭐7 — Self-contained browser runtime plugin for DeepSeek Harness — bundles Playwright (chromium) and OpenCLI as plugin-local dependencies, exposes a browser service and interactive browser tools.（✅ 活跃）
- [dsh-builtin-toggles](https://github.com/Starfie1d1272/dsh-builtin-toggles) ⭐7 — 官方 DSH Web 内置功能可读目录 + 安全 UI 开关。（✅ 活跃）
- [dsh-director-toolkit](https://github.com/lhmd/dsh-director-toolkit) ⭐7 — DSH Director Toolkit is a DeepSeek Harness plugin for 3D artists, technical designers, and creative coders. Paste a half-formed idea, a reference note, or a portfolio caption and get a compact direction pack for Blender, Three.js, Houdini, or C4D.（✅ 活跃）
- [dsh-git-identity](https://github.com/LoserFox/dsh-git-identity) ⭐7 — DSH 插件：git 提交固定使用环境自身作者身份（优先 gh CLI 登录账号，GitHub noreply 邮箱），GIT_AUTHOR_*/GIT_COMMITTER_* 环境变量注入压过一切 git config（✅ 活跃）
- [dsh-landscape](https://github.com/cyanseek/dsh-landscape) ⭐7 — Agent-first DeepSeek Harness plugin intelligence: verify existing plugins, identify missing capabilities, and generate build-ready briefs.（✅ 活跃）
- [dsh-lark-meeting-notifier](https://github.com/yeruizhi/dsh-lark-meeting-notifier) ⭐7 — 一个只有副作用的DeepSeekHarness插件：在你跟 AI 聊得神魂颠倒时，提醒你「该去跟碳基生命开会了」。（✅ 活跃）
- [dsh-pdf](https://github.com/sunshine-lang/dsh-pdf) ⭐7 — PDF 工具箱：pdfjs-dist 本地提取文本、元数据与页区间，无需 API Key。（✅ 活跃）
- [dsh-plugin-diff-review](https://github.com/Civitasv/dsh-plugin-diff-review) ⭐7 — Diff Review Plugin for DeepSeek Harness（✅ 活跃）
- [dsh-spend](https://github.com/nonewind/dsh-spend) ⭐7 — Token 用量与费用估算：悬浮面板，按模型/天/会话统计，自动识别计费套餐。（✅ 活跃）
- [dsh-token-panel](https://github.com/juhe291/dsh-token-panel) ⭐7 — A corner HUD for DeepSeek Harness that shows your session's token pressure, per-model cost, and daily/monthly usage at a glance — with an editable budget & balance that tracks spending for you. 右下角常驻的 Token 仪表盘：实时查看会话压力、按模型估算花费，预算和余额点一下就能改，每天每月用了多少都有记录。（✅ 活跃）
- [dsh-tool-turbo](https://github.com/Electricitysheep/dsh-tool-turbo) ⭐7 — Per-round reasoning_effort optimizer for DeepSeek Harness (dsh): auto-downgrades tool-call reasoning for simple tool chains, lifting back for heavy work. Cuts thinking time between tool calls.（✅ 活跃）
- [dsh-weather](https://github.com/sunshine-lang/dsh-weather) ⭐7 — 天气工具：Open-Meteo 当前天气与多日预报，免费免密钥。（✅ 活跃）
- [dsh-worktree](https://github.com/FlashingChen/dsh-worktree) ⭐7 — Codex-style permanent git worktrees for DeepSeek Harness: worktree_create/list/remove agent tools, a /worktree chat command, and durable per-repo manifests.（✅ 活跃）
- [dskin](https://github.com/dancingmemory/dskin) ⭐7 — 卡通像素皮肤插件：原始界面不动，像素宠物散步、眨眼、跳跃。（✅ 活跃）
- [deepseek-harness-themes](https://github.com/orxz/deepseek-harness-themes) ⭐6 — A collection of UI themes for deepseek-harness.（✅ 活跃）
- [dsh-agent-message](https://github.com/GengDaPeng/dsh-agent-message) ⭐6 — DeepSeek Harness 跨会话 Agent 通信插件｜Cross-session agent-to-agent messaging with offline delivery, receipts and session navigation for DeepSeek Harness.（✅ 活跃）
- [dsh-blue-whale-maid](https://github.com/yuxino/dsh-blue-whale-maid) ⭐6 — DeepSeek Harness Web 的蓝鲸女仆桌宠，任务有动静时会在页面边上提醒你。（✅ 活跃）
- [dsh-claude-cli](https://github.com/katsos/dsh-claude-cli) ⭐6 — DeepSeek Harness LLM provider that runs your installed Claude Code CLI as the model backend — no API key.（✅ 活跃）
- [dsh-composer-expand](https://github.com/13071301808/dsh-composer-expand) ⭐6 — Composer expand/collapse toggle for DeepSeek Harness (dsh): a ⬆/⬇ button in the composer tool row grows the input to a tall 70vh writing view for long drafts.（✅ 活跃）
- [dsh-cue-plugin](https://github.com/unnnnoooo/dsh-cue-plugin) ⭐6 — DeepSeek Harness 的跨会话引用(cue)插件（✅ 活跃）
- [dsh-douyin](https://github.com/AnacondaKC/dsh-douyin) ⭐6 — DSH WebUI 侧栏短视频插件：原生播放器、系列导航、直链解析与精确历史回放（✅ 活跃）
- [dsh-email](https://github.com/STARDUSTLC666/dsh-email) ⭐6 — DeepSeek Harness 邮件插件：email_list/read/search/send/folders/attachment 六工具，内置 QQ/163/126/新浪/阿里/Gmail/Outlook/iCloud 八个预设，多账号、附件收发、Web 设置页配置，纯 Node 全平台。· IMAP/SMTP email tools for DeepSeek Harness agents.（✅ 活跃）
- [dsh-excel-chat](https://github.com/hccccc01333/dsh-excel-chat) ⭐6 — dsh-excel-chat — talk to Excel in DeepSeek Harness: create, edit, repair, and verify spreadsheets by conversation (cells, formulas, styles, filters, tables, charts); every edit is auto-validated.（✅ 活跃）
- [dsh-file-claim](https://github.com/Nwflower/dsh-file-claim) ⭐6 — 并行 Agent 会话的文件归属/认领系统：认领/释放、心跳过期接管、异步三路合并。（✅ 活跃）
- [dsh-island](https://github.com/cdxiaodong/dsh-island) ⭐6 — 通过 Unix socket 把 DSH agent 的会话、工具调用与审批实时桥接到 CodeIsland macOS 刘海面板，可直接在面板上批准/拒绝。（✅ 活跃）
- [dsh-neu-theme](https://github.com/Lhy723/dsh-neu-theme) ⭐6 — DeepSeek Harness Web 的轻拟物与磨砂玻璃主题插件，提供浅色/深色主题、环境光、材质纹理和细腻微交互。Neumorphism + glassmorphism theme plugin for DeepSeek Harness Web with warm light/dark palettes, ambient lighting, grain texture, and subtle micro-interactions.（✅ 活跃）
- [dsh-ohos-patch](https://github.com/shenjackyuanjie/dsh-ohos-patch) ⭐6 — 让deepseek harness能在 ohos上跑！（✅ 活跃）
- [dsh-plugin-anydoc](https://github.com/beancookie/dsh-plugin-anydoc) ⭐6 — 基于 @firecrawl/anydoc 将 Word/PPT/Excel/PDF/EPUB/CSV 等文档转换为 GFM Markdown。（✅ 活跃）
- [dsh-plugin-call-me](https://github.com/radres/dsh-plugin-call-me) ⭐6 — Your DeepSeek Harness agent rings your actual phone: it asks out loud, you answer out loud, and what you said steers the run.（✅ 活跃）
- [dsh-plugin-installer](https://github.com/Toukaiteio/dsh-plugin-installer) ⭐6 — 将 DSH 接入 GitHub 插件生态的市场插件。（✅ 活跃）
- [dsh-plugin-manager](https://github.com/2768651338/dsh-plugin-manager) ⭐6 — DeepSeek Harness 的图形化插件管理插件：在 设置 → 插件 里新增「插件管家」标签页，用中文名和说明展示每个插件是做什么的，并提供一键启停开关与内置备注编辑——启停写入全局层补丁并实时热生效，备注保存到本地覆盖文件长期生效。（✅ 活跃）
- [dsh-plugin-session-import](https://github.com/huguangyu666/dsh-plugin-session-import) ⭐6 — DeepSeek Harness plugin: import claude-code / codex / reasonix / zcode sessions（✅ 活跃）
- [dsh-plugin-workbench](https://github.com/Pasumao/dsh-plugin-workbench) ⭐6 — VS Code-style workspace file explorer with editable preview for the DSH web GUI（✅ 活跃）
- [dsh-restart](https://github.com/anweat/dsh-restart) ⭐6 — Restart DSH: configurable restart method (Node native / legacy PowerShell), post-restart continue prompt, optional watchdog auto-relaunch.（✅ 活跃）
- [dsh-tdai-memory](https://github.com/Scorp1o117/dsh-tdai-memory) ⭐6 — Agent memory for DeepSeek Harness | DeepSeek Harness 记忆插件（✅ 活跃）
- [dsh-tool-stat](https://github.com/omdsh-dev/dsh-tool-stat) ⭐6 — DSH 统计工具插件：描述统计/百分位数/频数分布/相关性，零依赖纯函数确定性（✅ 活跃）
- [dsh-voice-input-plugin](https://github.com/Zhangbo-cn/dsh-voice-input-plugin) ⭐6 — Composer mic for DeepSeek Harness Web: tap-to-monitor live transcription and hold-to-talk, with host Edge TTS reply reading that streams while the model generates, echo-pause during reading, and tap-to-stop.（✅ 活跃）
- [dsh-web-restart](https://github.com/1123762794/dsh-web-restart) ⭐6 — One-click restart button for the DeepSeek Harness Web UI: sidebar footer button, single click restarts the dsh web process. / DSH Web 界面一键重启按钮。（✅ 活跃）
- [dsh-web-search-exa](https://github.com/TonyDua/dsh-web-search-exa) ⭐6 — 零配置 Exa 网页搜索：免密钥匿名 MCP 回退 + API Key REST 搜索。（✅ 活跃）
- [dsh-calculator](https://github.com/bobcat848/dsh-calculator) ⭐5 — Calculate the real-time cost of DeepSeek API calls made by DeepSeek Harness.（✅ 活跃）
- [dsh-cost-plugin](https://github.com/RoxsLee/dsh-cost-plugin) ⭐5 — DSH 费用/余额读数插件：在输入框统计行旁实时显示「本次 ≈¥x · 会话 ≈¥x · 余额 ¥x」，内置 DeepSeek 官方价目表，支持 2026-08-17 起生效的峰谷定价（按节点时间戳自动选档），余额经官方 /user/balance 实时查询，失败静默降级。（✅ 活跃）
- [dsh-deepseek-billing](https://github.com/Jolly-J/dsh-deepseek-billing) ⭐5 — DSH WebUI 插件:DeepSeek 余额显示与按会话费用估算（✅ 活跃）
- [dsh-defend](https://github.com/PerryLink/dsh-defend) ⭐5 — Prompt-injection, jailbreak, and secret-leak defense for DeepSeek Harness: Aho-Corasick detection with allow/ask/block interception and sanitized audit events（✅ 活跃）
- [dsh-desktop-pet](https://github.com/FenyxHuang/dsh-desktop-pet) ⭐5 — DeepSeek Harness 桌面宠物:鲸鱼实时反应 agent 状态(思考冒泡/工作中工具/出错),API 余额渲染为圆形海平面,点击触发跳跃或 40% 转体跳水,带随机台词。（🧪 实验性）
- [dsh-github-login](https://github.com/Noob-stupid/dsh-github-login) ⭐5 — DeepSeek Harness 生态的 GitHub 可视化登录工具（零终端）：设备码流程，令牌同步 gh CLI | Visual GitHub login for the DSH ecosystem - no terminal needed（✅ 活跃）
- [dsh-notify-windows](https://github.com/SeverusZh/dsh-notify-windows) ⭐5 — DSH Windows 原生通知，零依赖。（✅ 活跃）
- [dsh-session-cleaner](https://github.com/fountunt/dsh-session-cleaner) ⭐5 — 为 DeepSeek Harness 提供会话删除能力，支持侧边栏 ⋮ 菜单入口（✅ 活跃）
- [dsh-session-timeline](https://github.com/XiLuovo/dsh-session-timeline) ⭐5 — DeepSeek Harness 会话时间轴插件：横短横线波浪、当前消息定位、点击跳转、圆角预览 tooltip、可收起/展开（✅ 活跃）
- [dsh-split-panes](https://github.com/lehhair/dsh-split-panes) ⭐5 — Split panes.（✅ 活跃）
- [dsh-status-bar](https://github.com/Starlight-bananice/dsh-status-bar) ⭐5 — Know what your agent is doing at a glance — 17-segment configurable status bar for DeepSeek Harness: status/model/context/tokens/TPS/cost/jobs. 一眼看清你的 agent 正在做什么：17 段可配置 DSH 会话状态栏。（✅ 活跃）
- [dsh-stream-rules](https://github.com/jiesou/dsh-stream-rules) ⭐5 — 模式匹配自动注入 steering rules，不占系统上下文 - Inject rules when needed, without wasting context. Similar to oh-my-pi's "Time-traveling stream rules", but with a very simple and compact code implementation.（✅ 活跃）
- [dsh-web-attention-badge](https://github.com/Luaphes/dsh-web-attention-badge) ⭐5 — Attention reminders for the DeepSeek Harness Web UI: frame badge, (N) tab title and whale-favicon recolor for sessions waiting for input or finished unopened.（✅ 活跃）
- [nowledge-mem-deepseek-harness](https://github.com/nowledge-co/nowledge-mem-deepseek-harness) ⭐5 — 将 Nowledge Mem 记忆服务接入 DeepSeek Harness 的社区插件包。（✅ 活跃）
- [zotero-harvest](https://github.com/Fisfzy/zotero-harvest) ⭐5 — Zotero 文献采集入库插件（DSH external plugin）：多源检索（OpenAlex/arXiv/Crossref/Europe PMC/Semantic Scholar）+ OA 下载链接解析（Unpaywall）+ 充分性审计 + 入库本地 Zotero + 触发 zotero-wave-rag 重建（✅ 活跃）
- [codex-eyes-hands](https://github.com/651002/codex-eyes-hands) ⭐4 — 专为 DeepSeek Harness 打造：把本机 Codex CLI 变成纯文本 AI agent 的眼睛和手——看图/读文件/画图/监督执行/双通道容灾（✅ 活跃）
- [dsh-approval-gate](https://github.com/moon09300731/dsh-approval-gate) ⭐4 — DeepSeek Harness 自动审批门控：Flash 预判写入/命令是否不可回补，安全操作自动批准、危险操作转人工（fail-safe）。（✅ 活跃）
- [dsh-archive-viewer](https://github.com/keepermttl/dsh-archive-viewer) ⭐4 — DeepSeek Harness 归档会话管理插件：查看/恢复已归档会话（回到原工作区分组）+ 右上角一键关闭 dsh。MIT 许可，欢迎收录到任何插件合集，注明出处即可。（✅ 活跃）
- [dsh-auxiliary](https://github.com/dsh-plugins/dsh-auxiliary) ⭐4 — Auxiliary models for DeepSeek Harness: vision understanding and context compression through dedicated model routes. DeepSeek Harness 辅助模型插件：为视觉理解、上下文压缩、审批审查、子代理、会话标题与图片生成提供独立的模型路由、工具与系统提示，全程不触碰主对话模型。（✅ 活跃）
- [dsh-bell-notify](https://github.com/Laplace-bit/dsh-bell-notify) ⭐4 — Configurable, unobtrusive Web Audio lifecycle notifications for DeepSeek Harness (dsh): 10 events, custom sounds, offline playback.（✅ 活跃）
- [dsh-black-whale](https://github.com/147228/dsh-black-whale) ⭐4 — DeepSeek Harness 黑鲸实验室主题：官网黑鲸 × 夕小瑶 IP，真实 profile 可安装的 Web UI 插件（✅ 活跃）
- [dsh-companion](https://github.com/beijingwahw/dsh-companion) ⭐4 — DeepSeek Companion — DeepSeek Harness 官方伴侣插件：对话导出/交接摘要/成本优化/全局检索 + 执行轨迹分析、Prompt 工程工作台、多模型竞技场、任务编排、安全与审计（E–J 九大模块，Cordis 插件化）。（✅ 活跃）
- [dsh-deeplink](https://github.com/qyw233/dsh-deeplink) ⭐4 — DSH WebUI 深链插件：?session=/?workspace= 直接打开指定项目对话（✅ 活跃）
- [dsh-deepseek-quota](https://github.com/yingjunnan/dsh-deepseek-quota) ⭐4 — DeepSeek API quota (balance) widget for the DSH web GUI: a floating bottom-right card showing remaining DeepSeek API balance.（✅ 活跃）
- [dsh-ffmpeg](https://github.com/STARDUSTLC666/dsh-ffmpeg) ⭐4 — DeepSeek Harness 视频处理插件：ffmpeg_probe/cut/concat/encode/subtitle/extract/gif 七工具，走官方 subprocess 服务、argv 数组无 shell 注入、零运行时依赖；纯 Node 全平台。· Video processing tools for DeepSeek Harness agents.（✅ 活跃）
- [dsh-git-status](https://github.com/Wongzexu/dsh-git-status) ⭐4 — Git status (Git Graph) plugin for DSH: commit DAG lane graph + uncommitted changes/stash + inline diffs + branch operations. DSH 插件：Git 状态浮窗（泳道图/未提交/stash/diff/分支操作）。（✅ 活跃）
- [dsh-guardian](https://github.com/cdxiaodong/dsh-guardian) ⭐4 — Agent 安全护栏：拦截并审计所有工具调用，命中敏感操作就要求人工确认。（✅ 活跃）
- [dsh-heatmap](https://github.com/283Gawin/dsh-heatmap) ⭐4 — DSH Web GUI activity heatmap plugin: GitHub-style commit/token/spend heatmap in the sidebar with per-model cost estimation（✅ 活跃）
- [dsh-input-history](https://github.com/lhh010/dsh-input-history) ⭐4 — 终端风格输入历史：Ctrl+Up/Down 召回与切换已发送消息。（✅ 活跃）
- [dsh-library](https://github.com/PerryLink/dsh-library) ⭐4 — Local document knowledge base for DeepSeek Harness: library_add/remove/list, hybrid semantic+keyword library_search with diversity re-ranking, relevance filtering and lost-in-the-middle avoidance, citation-aware injection, library_cite_check and library_diagnose — SQLite-backed index via the storage domain, local embedding, zero model downloads.（✅ 活跃）
- [dsh-llm-verifier](https://github.com/Web0926/dsh-llm-verifier) ⭐4 — 运行 3 或 5 个隔离的编程代理候选，验证其补丁，用 LLM 对通过验证的候选排序，并仅在用户批准后应用获胜补丁。（✅ 活跃）
- [dsh-neo-skin](https://github.com/0nt-one/dsh-neo-skin) ⭐4 — Neo-brutalism skin for the DeepSeek Harness Web UI — hard borders, high contrast, two switchable schemes (Blue Command / Aged Newspaper), works in light and dark themes.（✅ 活跃）
- [dsh-notebooks](https://github.com/havingautism/dsh-notebooks) ⭐4 — Notebooks plugin (cordis).（✅ 活跃）
- [dsh-output-styles](https://github.com/PerryLink/dsh-output-styles) ⭐4 — Claude Code outputStyles for DeepSeek Harness - session-scoped, durable, runtime-switchable model output styles (/style command, output_style storage domain, systemPrompt injection)（✅ 活跃）
- [dsh-plugin-deepeye](https://github.com/Favio8/dsh-plugin-deepeye) ⭐4 — DeepEye vision plugin for DeepSeek Harness (DSH): image description, OCR, VQA, UI layout, and clipboard analysis.（✅ 活跃）
- [dsh-polyglot](https://github.com/Jesse-njx/dsh-polyglot) ⭐4 — dsh-polyglot — the model switch for DSH: generic OpenAI-compatible ctx.llm adapter, curated free/cheap DeepSeek presets, automatic provider fallback on rate limits（✅ 活跃）
- [dsh-pomodoro](https://github.com/causebefore/dsh-pomodoro) ⭐4 — DeepSeek Harness Web 番茄钟插件：可配置专注与休息时长，提供侧栏入口和可拖动浮动面板（✅ 活跃）
- [dsh-revive](https://github.com/omdsh-dev/dsh-revive) ⭐4 — DSH 一键复活：重启后给所有被打断的会话自动发送「继续」指令（/revive 命令 + revive_sessions 工具 + 浏览器一键按钮）（✅ 活跃）
- [dsh-rss](https://github.com/STARDUSTLC666/dsh-rss) ⭐4 — DeepSeek Harness RSS 订阅插件：rss_list/add/remove/fetch/check 五工具，RSS 0.9x/1.0/2.0 与 Atom 归一化解析，订阅列表持久化到 settings，proxyUrl 特殊代理支持；纯 Node 全平台。· RSS/Atom subscription tools for DeepSeek Harness agents.（✅ 活跃）
- [dsh-skill-hub](https://github.com/cheshireez/dsh-skill-hub) ⭐4 — DSH Web GUI 技能中枢：基于官方 ctx.skills 注册表浏览、搜索、启停、查看、诊断并新建本地技能，附技能市场：来源快照跟踪、一键全量更新。（✅ 活跃）
- [dsh-skin-switcher](https://github.com/zhtx2024/dsh-skin-switcher) ⭐4 — DeepSeek Harness Web GUI 皮肤切换插件：设置界面一键切换已安装皮肤（✅ 活跃）
- [dsh-tool-csv](https://github.com/omdsh-dev/dsh-tool-csv) ⭐4 — DSH CSV 数据工具插件：解析/查询/统计/转换 CSV 文本（RFC 4180），零依赖状态机解析器，注册 csv 工具（✅ 活跃）
- [dsh-tool-diff](https://github.com/omdsh-dev/dsh-tool-diff) ⭐4 — DSH Diff 工具插件：文本/JSON/CSV/Markdown 结构化比较与 unified diff，零依赖只读，注册 diff 工具（✅ 活跃）
- [dsh-tool-git](https://github.com/lxj808624/dsh-tool-git) ⭐4 — 结构化安全 Git 工具：status/diff/log/branch/stage/commit/stash/show，带破坏性命令防护。（✅ 活跃）
- [dsh-tool-markdown](https://github.com/omdsh-dev/dsh-tool-markdown) ⭐4 — DSH Markdown 工具插件：HTML↔Markdown 转换、GFM 表格规范化、目录生成，零依赖轻量解析器，注册 markdown 工具（✅ 活跃）
- [dsh-trajectory-governance](https://github.com/dfycaly98931680/dsh-trajectory-governance) ⭐4 — Agent trajectory governance & anomaly diagnosis plugin for DeepSeek Harness (dsh): multi-branch trajectory trees, loop-deadlock / invalid-retry / goal-drift detection, cost attribution, alerts, one-click interrupt & breakpoint fork, independent GUI tab. Zero kernel modification.（✅ 活跃）
- [dsh-verification-receipt](https://github.com/030611/dsh-verification-receipt) ⭐4 — Privacy-minimal heuristic per-turn verification summaries for DeepSeek Harness（✅ 活跃）
- [dsh-wallpaper](https://github.com/chinaRXQ/dsh-wallpaper) ⭐4 — Wallpaper skin for the DeepSeek Harness (dsh) web UI: image background with opacity, mask and blur controls.（✅ 活跃）
- [dsh-win-notify](https://github.com/MuziIsabel/dsh-win-notify) ⭐4 — DSH 插件：代理任务完成时弹出带声音的 Windows Toast 通知，点击通知即可直接切回并前台显示 DSH 标签页（✅ 活跃）
- [dsh-wordbox](https://github.com/arcmosin/dsh-wordbox) ⭐4 — 输入框旁常用词箱：全局/项目词桶，一键插入。（✅ 活跃）
- [dsh-workspace-search](https://github.com/tsonglew/dsh-workspace-search) ⭐4 — VS Code 风格工作区关键词搜索：Better Sidebar 生态的搜索 Tab。（✅ 活跃）
- [deepseek-harness-plugin-manager](https://github.com/hrhgit/deepseek-harness-plugin-manager) ⭐3 — Web plugin manager for DeepSeek Harness (DSH): inspect, search, group, enable, and disable Cordis plugins.（✅ 活跃）
- [dsh-agentmemory](https://github.com/elementor-i/dsh-agentmemory) ⭐3 — agentmemory for DeepSeek Harness (dsh): full memory_* tools, capture hooks, and context injection over the local REST server（✅ 活跃）
- [dsh-auto-chess](https://github.com/omdsh-dev/dsh-auto-chess) ⭐3 — DSH Web里的自走棋插件：人机对战或双AI对弈（✅ 活跃）
- [dsh-bill](https://github.com/Jannchie/dsh-bill) ⭐3 — DSH (DeepSeek Harness) plugin: per-session cost line + cost attribution report, priced by llm-pricing（✅ 活跃）
- [dsh-budget](https://github.com/PerryLink/dsh-budget) ⭐3 — Cost governance for DeepSeek Harness: aggregated token/cost metering per model, session and day, budget caps with threshold alerts and over-limit policies, carbon footprint estimation, per-model latency benchmarks, a Settings budget tab, and the /budget command（✅ 活跃）
- [dsh-calendar](https://github.com/STARDUSTLC666/dsh-calendar) ⭐3 — DeepSeek Harness 日历插件：calendar_list/create/update/delete/search 五工具，CalDAV 协议支持 Google/iCloud/Nextcloud/自定义端点，RRULE 重复事件自动展开，插件级 proxyUrl 代理，配置缺失不崩启动；纯 Node 全平台。· CalDAV calendar tools for DeepSeek Harness agents.（✅ 活跃）
- [dsh-conversation-share](https://github.com/bill9109/dsh-conversation-share) ⭐3 — 分享任意段落的 DSH 对话（✅ 活跃）
- [dsh-deepseek-balance](https://github.com/CN-Leo/dsh-deepseek-balance) ⭐3 — deepseek-harness 插件，实时查询deepseek账号余额（✅ 活跃）
- [dsh-diagram](https://github.com/hanzhangzzz/dsh-diagram) ⭐3 — Turn articles in DeepSeek Harness into editable Excalidraw canvases.（✅ 活跃）
- [dsh-docker](https://github.com/STARDUSTLC666/dsh-docker) ⭐3 — DeepSeek Harness 容器管理插件：docker_ps/logs/inspect/exec/manage 五工具，官方 subprocess 服务、argv 无 shell 注入、exec 审批门、零运行时依赖。· Containers for DeepSeek Harness agents.（✅ 活跃）
- [dsh-doctor](https://github.com/astra3294/dsh-doctor) ⭐3 — Deterministic diagnostics and recovery for DeepSeek Harness（✅ 活跃）
- [dsh-everything-oauth](https://github.com/kam74515-boop/dsh-everything-oauth) ⭐3 — Import local Codex / Grok / Claude / OpenCode / CC Switch logins into DeepSeek Harness（✅ 活跃）
- [dsh-file-uploads](https://github.com/l541402398/dsh-file-uploads) ⭐3 — 从 Web 输入框上传任意本地文件，待传卡片显示，设置页统一管理。（✅ 活跃）
- [dsh-fun-typewriter](https://github.com/omdsh-dev/dsh-fun-typewriter) ⭐3 — DSH Typewriter: WebAudio typing ambience with a plugin-owned settings API and zero audio assets（✅ 活跃）
- [dsh-llm-inspector](https://github.com/cdxiaodong/dsh-llm-inspector) ⭐3 — 统一 LLM 请求/响应检查器：调 reasoning effort、外部思考(think)导出、流量与包分析。（✅ 活跃）
- [dsh-llm-ollama](https://github.com/NOirBRight/dsh-llm-ollama) ⭐3 — Native Ollama Cloud provider and Web configuration plugin for DeepSeek Harness（✅ 活跃）
- [dsh-memory](https://github.com/flymysql/dsh-memory) ⭐3 — 跨会话记忆库：memory_remember / memory_recall / memory_forget 工具 + 设置页。（🧪 实验性）
- [dsh-memory-evidence](https://github.com/LeslieWylie/dsh-memory-evidence) ⭐3 — Git-first memory navigation and bounded evidence tools for DeepSeek Harness.（💤 停更）
- [dsh-observe](https://github.com/PerryLink/dsh-observe) ⭐3 — OpenTelemetry and Langfuse observability exporter for DeepSeek Harness: turn/step/tool/LLM spans, token and cost metrics, sanitized prompt/completion capture, async batching, bounded offline buffering, retry with backoff（✅ 活跃）
- [dsh-pet-corner](https://github.com/omdsh-dev/dsh-pet-corner) ⭐3 — DSH Pet Corner: a floating pet, keyless pet-image proxy, favorites, and plugin-owned settings API（✅ 活跃）
- [dsh-plugin-meta-memory](https://github.com/YYTbit/dsh-plugin-meta-memory) ⭐3 — Structured long-term memory system for DeepSeek Harness（✅ 活跃）
- [dsh-plugin.github.io](https://github.com/dsh-plugin/dsh-plugin.github.io) ⭐3 — DeepSeek Harness community plugin workshop and directory（✅ 活跃）
- [dsh-plugins-raincode](https://github.com/rainforest888/dsh-plugins-raincode) ⭐3 — dsh plugin: DeepSeek Harness 的模型层 = raincode(模型池/缓存/重试) + /skills 浏览（✅ 活跃）
- [dsh-prompt-stash](https://github.com/Wine-Red/dsh-prompt-stash) ⭐3 — Local, per-session prompt stash for DeepSeek Harness Web | 本地、分对话的提示词输入暂存工具。写了一半的长提示词，临时需要先问一个短问题？ 同时准备多个方案，但尚未决定发哪一个？将未完成的想法放入草稿架中，准备好后再继续完成（✅ 活跃）
- [dsh-prompt-studio](https://github.com/Moeblack/dsh-prompt-studio) ⭐3 — 带实时预览编辑用户与内置系统提示词片段。（✅ 活跃）
- [dsh-session-pin](https://github.com/PerryLink/dsh-session-pin) ⭐3 — Pin sessions and workspaces to the top of the DeepSeek Harness sidebar with per-pin row colors - a dual-face (host + client) dsh plugin.（✅ 活跃）
- [dsh-shortcuts](https://github.com/Ricketts-Guo/dsh-shortcuts) ⭐3 — DeepSeek Harness WebUI 键盘快捷键插件（34 个预置功能、一键录制自定义、静默权限切换）— Fully customizable keyboard shortcuts for the DSH WebUI.（✅ 活跃）
- [dsh-skill-studio](https://github.com/zhengjy01/dsh-skill-studio) ⭐3 — DSH skill 可视化与管理插件：设置面板列出全部 skill（含来源、嵌套标记与调用状态）、查看并编辑 SKILL.md 正文、一键启用/禁用模型与用户调用，并提供 skillmgr_list/get/save/policy 工具。（✅ 活跃）
- [dsh-specflow](https://github.com/lonelymoon87/dsh-specflow) ⭐3 — Specification-driven development toolkit for DeepSeek Harness.（✅ 活跃）
- [dsh-sticky-disclosure](https://github.com/Han-1413141/dsh-sticky-disclosure) ⭐3 — DSH Web client plugin: collapse every expanded section (Think / tool cards) in the conversation in one click, with a customizable hotkey.（✅ 活跃）
- [dsh-suggested-replies](https://github.com/Anionex/dsh-suggested-replies) ⭐3 — DSH Web 预测回复插件：AI 回复后在输入框上方生成可点击填入草稿的候选。（✅ 活跃）
- [dsh-sysmon](https://github.com/AKS1st/dsh-sysmon) ⭐3 — DSH Web 系统状态悬浮窗：实时 CPU/内存/磁盘占用率 | System-status overlay showing live CPU, memory and disk usage for DSH Web（✅ 活跃）
- [dsh-telemetry-redactor](https://github.com/030611/dsh-telemetry-redactor) ⭐3 — Fail-closed export-copy redaction for DeepSeek Harness session telemetry（✅ 活跃）
- [dsh-theme-plugin](https://github.com/BeiZi6/dsh-theme-plugin) ⭐3 — DSH Web GUI theme studio: presets + per-mode customization (accent, background, foreground, fonts, translucent sidebar, contrast) via the official webServer.tapIndex seam（✅ 活跃）
- [dsh-tool-encoding](https://github.com/omdsh-dev/dsh-tool-encoding) ⭐3 — DSH 编码/哈希工具插件：base64/base64url/url/hex 编解码、md5/sha1/sha256/sha512 哈希、UUID 生成，零依赖（✅ 活跃）
- [dsh-tool-json](https://github.com/omdsh-dev/dsh-tool-json) ⭐3 — DSH JSON 查询工具插件：JMESPath 子集查询，零依赖递归下降解析器（✅ 活跃）
- [dsh-tool-regex](https://github.com/omdsh-dev/dsh-tool-regex) ⭐3 — DSH 正则工具插件：测试匹配/提取捕获组/安全替换/静态解释正则（不执行代码），零依赖，注册 regex 工具（✅ 活跃）
- [dsh-tool-schema](https://github.com/omdsh-dev/dsh-tool-schema) ⭐3 — DSH JSON Schema 验证工具插件：validate/paths/explain/normalize，零网络零动态执行（✅ 活跃）
- [dsh-tool-search](https://github.com/vibeinging/dsh-tool-search) ⭐3 — 按 Agent 按需工具发现与渐进式 schema 披露。（✅ 活跃）
- [dsh-ultra-ui](https://github.com/havingautism/dsh-ultra-ui) ⭐3 — Ultra UI plugin (cordis).（✅ 活跃）
- [dsh-usage-plugin](https://github.com/Yihong89/dsh-usage-plugin) ⭐3 — DeepSeek Harness (DSH) plugins. First: dsh-usage-report — per-session token usage & estimated cost (/usage + usage_report), priced from the DeepSeek pricing table.（✅ 活跃）
- [dsh-vision-tools](https://github.com/moon09300731/dsh-vision-tools) ⭐3 — DeepSeek Harness 视觉能力全家桶：vision_understand 工具（OpenAI 兼容视觉 API，默认免费智谱 GLM-4V-Flash）+ 粘贴/拖拽/按钮三入口识图。（✅ 活跃）
- [dsh-webbridge](https://github.com/bill9109/dsh-webbridge) ⭐3 — DSH 结合 Kimi WebBridge 操控真实浏览器。（✅ 活跃）
- [mistymoon-dsh](https://github.com/mianyoubiaoqing/MistyMoon-DSH) ⭐3 — Local-first long-term companion plugin suite for DeepSeek Harness（✅ 活跃）
- [URL Manager](https://github.com/Piccolo123/url-manager) ⭐3 — Agent 优先的 URL 与知识收集系统：自动分类、标签、全文检索与共享收藏。（✅ 活跃）
- [zotero-wave-rag](https://github.com/Fisfzy/zotero-wave-rag) ⭐3 — 面向 Zotero 论文库的浪潮式 RAG 细节检索系统 —— DSH 外部插件。移植 VCPToolBox 浪潮语义动力学思想（标签河道图传播/虫洞跳转/钟型阻尼/Ω重排），配 BM25+RRF 混合检索、claim-evidence 忠实度校验、两级增量索引（✅ 活跃）
- [dsh-adb](https://github.com/SamXiaBing/dsh-adb) ⭐2 — ADB device & bench operations: device discovery, structured logcat (background streaming), apk install, file pull/push, dumpsys performance snapshots.（✅ 活跃）
- [dsh-agent-budget](https://github.com/vibeinging/dsh-agent-budget) ⭐2 — Native Harness agent-tree token budget plugin（✅ 活跃）
- [dsh-cost-meter](https://github.com/Sttrevens/dsh-cost-meter) ⭐2 — dsh plugin: per-turn USD cost badge in the Web UI (session total + per-message footer, hover breakdown) from token usage x a configurable pricing table.（✅ 活跃）
- [dsh-fork-graph](https://github.com/chouyong/dsh-fork-graph) ⭐2 — See your DSH conversation's fork history as a git graph — coloured branch lanes in the session header, click to jump. A pure-derivation DeepSeek Harness Web plugin.（✅ 活跃）
- [dsh-gitflow](https://github.com/lonelymoon87/dsh-gitflow) ⭐2 — Git status, diff, log, commit, branch, and optional Change Ledger tools for DeepSeek Harness.（✅ 活跃）
- [dsh-memoria](https://github.com/jiayan-xu/dsh-memoria) ⭐2 — 向量 + 图记忆后端：命名空间隔离、自动观察、召回、重要性处理与热重载。（🧪 实验性）
- [dsh-memory (Jesse-njx)](https://github.com/Jesse-njx/dsh-memory) ⭐2 — 基于 DSH 无损会话日志的引用式记忆：可人工审计的蒸馏事实，带引用来源。（✅ 活跃）
- [dsh-pin-recall](https://github.com/kerwin2046/dsh-pin-recall) ⭐2 — 从操作条固定助手回复，并在下一轮召回（/pin /recall）。（✅ 活跃）
- [dsh-plugin-choice-refresh](https://github.com/Pasumao/dsh-plugin-choice-refresh) ⭐2 — DSH 选择增强插件：「重新生成选项」/「更多选项」按钮。Choice refresh (regenerate / more options) for DeepSeek Harness (dsh).（✅ 活跃）
- [dsh-plugin-description](https://github.com/MysaDC/dsh-plugin-description) ⭐2 — mount one row in the composition and every plugin card on the Web Settings plugin list page gets a bilingual (zh/en) description; it also publishes the pluginDescriptions service so other plugins can register their own descriptions.（✅ 活跃）
- [dsh-plugin-quota-monitor](https://github.com/DoggyHU/dsh-plugin-quota-monitor) ⭐2 — DSH sidebar footer quota & balance monitor: DeepSeek Rage + OpenCode Go HP/MP/SP + SCNet (国家超算) Credits local estimate. 设置→插件管理可配置数据源与费率表。（✅ 活跃）
- [dsh-plugin-radar](https://github.com/dshplugin-me/dsh-plugin-radar) ⭐2 — Find DSH plugins by asking in plain language, then security-scan them before install（✅ 活跃）
- [dsh-review-loop](https://github.com/wuxiangru915/dsh-review-loop) ⭐2 — 增量代码审查：基于检查点的审查队列 + Web UI 面板 + /review 命令。（✅ 活跃）
- [dsh-scout](https://github.com/omdsh-dev/dsh-scout) ⭐2 — 面向 DeepSeek Harness 的只读环境探测插件，为智能体提供运行环境、软件版本、系统资源、端口、服务、硬件及工作区信息。（✅ 活跃）
- [dsh-session-search](https://github.com/Tieboyh/dsh-session-search) ⭐2 — 免索引跨 Agent 会话搜索。（✅ 活跃）
- [dsh-sub2api](https://github.com/GodD6366/dsh-sub2api) ⭐2 — Connect your sub2api gateway to DeepSeek Harness: OpenAI-compatible multi-provider routes (OpenAI / Claude / Grok / Gemini) behind one base URL, with per-key model discovery, usage lookup, and a settings page.（✅ 活跃）
- [dsh-test-drive](https://github.com/PerryLink/dsh-test-drive) ⭐2 — Isolated install-and-smoke test drives for DeepSeek Harness plugins: installs a repo or npm package into a throwaway DSH_HOME profile, verifies the bundle patch layer and boot logs, records a structured pass/fail result matrix (JSON/Markdown) for scoring pipelines, and quarantines every temp directory it owns（✅ 活跃）
- [dsh-test-runner](https://github.com/suimi8/dsh-test-runner) ⭐2 — 结构化测试运行工具：自动识别 vitest/jest/pytest/node:test，运行并解析失败摘要。（✅ 活跃）
- [dsh-trace](https://github.com/vibeinging/dsh-trace) ⭐2 — DeepSeek Harness telemetry backend that exports turns, model steps, and tool calls to yiTrace over HTTP.（✅ 活跃）
- [dsh-translate](https://github.com/PerryLink/dsh-translate) ⭐2 — Vendor parameter translation and deterministic JSON repair for DeepSeek Harness: /translate maps temperature/top_p/max_tokens/stop/system across 11 vendors, and the post-execute repair layer (plus fix_json) fixes broken JSON tool output without ever fabricating data（✅ 活跃）
- [dsh-turn-navigator](https://github.com/vibeinging/dsh-turn-navigator) ⭐2 — Private DSH Web turn navigation plugin（✅ 活跃）
- [dsh-usage-vendor-stats](https://github.com/kirigayakazima/dsh-usage-vendor-stats) ⭐2 — DeepSeek Harness usage stats by vendor (subscription / official API) × KPI: 53-week heatmap, trend chart, model drilldown, CSV export, and health cards.（✅ 活跃）
- [dsh-view-modes](https://github.com/NigelYao/dsh-view-modes) ⭐2 — Verbose/Normal/Summary 三种输出模式，工具调用与思考语义分组。（✅ 活跃）
- [dsh-what-changed](https://github.com/sjh9714/dsh-what-changed) ⭐2 — 会话顶栏的整会话改动审阅。列出本次会话 Agent 写过的每个文件与逐处改动，被权限拒绝的写入单独计数不算改动，数据来自 session projection 而非磁盘日志。（✅ 活跃）
- [dsh-workspace-menu](https://github.com/0imzero/dsh-workspace-menu) ⭐2 — DSH workspace/chat enhancement menu: pin, rename, open in file explorer, archive, fork, copy, new window. Settings integrated into General.（✅ 活跃）
- [visual-review](https://github.com/wang-bool/visual-review) ⭐2 — 在 DSH Web 聊天界面内联渲染粘贴/上传的图片，让纯文本模型获得视觉：云端多模态 API 优先，本机 Qwen3-VL 兜底。（✅ 活跃）
- [dsh-code-intel](https://github.com/lonelymoon87/dsh-code-intel) ⭐1 — Symbol-aware code indexing and hybrid search for DeepSeek Harness.（✅ 活跃）
- [dsh-computer-use](https://github.com/xiaoheizi1212/dsh-computer-use) ⭐1 — 模型无关的 Computer Use：隔离浏览器、Windows 原生助手与第三方桥接。（✅ 活跃）
- [dsh-doctor](https://github.com/asdf17128/dsh-doctor) ⭐1 — Find what your DeepSeek Harness (dsh) patches silently broke — dead patches, config fields dropped by whole-config replacement, unmaintained plugins. Read-only, zero deps.（✅ 活跃）
- [dsh-event-auditor](https://github.com/qing3a/dsh-event-auditor) ⭐1 — DeepSeek Harness 事件流审计面板插件：观察事件类型/分发模式/计数/最近事件，帮助插件作者理解 harness 内部（✅ 活跃）
- [dsh-humanizer](https://github.com/lynote-ai/dsh-humanizer) ⭐1 — 写作工具：去除 AI 腔并贴合个人文风。8 个确定性工具扫描文本、从样本提取文风指纹，并返回改写 brief。（🧪 实验性）
- [dsh-news-plugin](https://github.com/canghai666x/dsh-news-plugin) ⭐1 — RSS/新闻摄入插件：返回结构化的标题/链接/来源/日期/摘要，供模型排序与简报。（✅ 活跃）
- [dsh-payload-capture](https://github.com/Moeblack/dsh-payload-capture) ⭐1 — 捕捉每次上行模型 API payload，JSON 落盘，用于调试与可观测性。（✅ 活跃）
- [dsh-plugin-evaluation-standards](https://github.com/dsh-plugin-evaluation/dsh-plugin-evaluation-standards) ⭐1 — Open evaluation datasets, test cases, and metrics for DSH plugins.（✅ 活跃）
- [dsh-plugin-image-tools](https://github.com/Pasumao/dsh-plugin-image-tools) ⭐1 — DSH 图片插件：图片选择卡 + 回复内嵌图片 + 盲模型收图（✅ 活跃）
- [dsh-plugin-manager-registry](https://github.com/Jesse-njx/dsh-plugin-manager-registry) ⭐1 — @dsh-pm/registry — discover dsh plugins by merging the awesome-dsh-plugin list, GitHub dsh-plugin-topic search, and npm keyword search into one deduped, offline-tolerant registry (the discovery engine of dsh pm)（✅ 活跃）
- [dsh-plugin-quote-reply](https://github.com/yangYzc/dsh-plugin-quote-reply) ⭐1 — DSH plugin: select text in a conversation, then quote it into the composer or reply in a new window. / DeepSeek Harness 划词引用插件：选中文字一键引用回复或新窗口回复。（✅ 活跃）
- [dsh-plugin-radar](https://github.com/DshMarketPlace/dsh-plugin-radar) ⭐1 — Userscript: marks DeepSeek Harness plugins on GitHub and npm, with the install command that actually works（✅ 活跃）
- [dsh-repo-setup](https://github.com/gongyijie85/dsh-repo-setup) ⭐1 — 只读仓库体检引导工具（repo_setup_scan）：识别技术栈/测试/文档/git/数据库线索，给出插件、MCP 与卫生文件的安装建议（claude-code-setup 对应版）。（✅ 活跃）
- [dsh-routines](https://github.com/Jesse-njx/dsh-routines) ⭐1 — dsh-routines — scheduled agents for DSH: run a prompt on a cron, get the digest where you already are (file digests, chatnode delivery, unattended-safe)（✅ 活跃）
- [dsh-tool-approval](https://github.com/ilharp/dsh-tool-approval) ⭐1 — Manual approval for Deepseek Harness (aka "Manual Mode"/"Ask Mode")（✅ 活跃）
- [dsh-tps](https://github.com/Small-tailqwq/dsh-tps) ⭐1 — 只是一个 tps 插件（✅ 活跃）
- [dsh-turn-index](https://github.com/Simon314620/dsh-turn-index) ⭐1 — 回合索引侧栏：每个用户回合一条，点击跳转，滚动监听高亮。（✅ 活跃）
- [dsh-voice-webspeech](https://github.com/anweat/dsh-voice-webspeech) ⭐1 — Browser Web Speech API voice input for DSH: zero server, zero keys, zero model downloads (Edge=Azure, Chrome=Google speech).（✅ 活跃）
- [dshp](https://github.com/asdf17128/dshp) ⭐1 — Manage DeepSeek Harness profiles — list, create, clone, diff, and share a whole dsh setup as one portable file.（✅ 活跃）
- [dsh-client-auto-retry](https://github.com/Frog755/dsh-client-auto-retry)  — 回合中断自动续跑：turn/end 因 error/interrupted/max-tokens 结束时自动发送「继续」，支持宽限期、冷却、连发上限、启动扫描与设置卡片；不切换模型/provider。（✅ 活跃）
- [dsh-deepseek-balance](https://github.com/dshiq04/dsh-deepseek-balance)  — 面向deepseek harness的余额查看插件（✅ 活跃）
- [dsh-evoforge](https://github.com/deepseek-harness-evoforge/dsh-evoforge)  — Evidence-driven, cache-stable extensions for DeepSeek Harness（✅ 活跃）
- [dsh-fork-to-preset](https://github.com/bpc-oss/dsh-fork-to-preset)  — 在会话 Header 上一键把当前会话分叉到任意 agent preset：选择 preset 后创建挂载到该 preset 的新子会话，并继承源会话的已完成轮次。（✅ 活跃）
- [dsh-git-branch-switcher](https://github.com/mixin-ai/dsh-git-branch-switcher)  — 会话头部 git 分支胶囊：显示并在 Web UI 中切换工作区分支。（✅ 活跃）
- [dsh-llm-local-token](https://github.com/tianxia--/dsh-llm-local-token)  — 复用本机 Codex CLI 与 Claude Code OAuth 凭据的 DSH 模型提供方路由，无需另配 API Key。（✅ 活跃）
- [dsh-plugin](https://github.com/dsh-plugin-dev/dsh-plugin)  — Build your own coding agent with Pi dsh-plugin（✅ 活跃）
- [dsh-plugin-cost](https://github.com/yweilai77-dev/dsh-plugin-cost)  — Session cost estimate in the DSH Web composer dock (tokenUsage × configurable price table, one-click official-price refresh).（✅ 活跃）
- [dsh-precedent](https://github.com/dshplugin-me/dsh-precedent)  — Evidence-backed working memory for DeepSeek Harness: a cited ledger of what already worked in this workspace, built from the session log you already have. No index, no model, no capture step.（✅ 活跃）
- [dsh-routed-subagent](https://github.com/bpc-oss/dsh-routed-subagent)  — 从任意会话派发一个完整挂载到任意 agent preset 的一次性子代理，支持按次指定模型/provider、模型可用性预检，以及外部 CLI 引擎（codex / claude / codebuddy），支持后台任务、实时进度、终止与可续会话。（✅ 活跃）
- [dsh-session-cleaner-cli](https://github.com/ChenChen913/dsh-session-cleaner-cli)  — 深度清理 DeepSeek Harness (DSH) 工作区会话的离线 CLI：按工作区列出/删除/恢复会话，自动同步工作区账目与投影缓存。Offline session cleaner for DeepSeek Harness: list, delete (trash+restore) and prune ghost sessions across workspaces.（✅ 活跃）
- [dsh-upload](https://github.com/Ei-Ayw/dsh-upload)  — DSH Web 的上传按钮:点 📎 选本地文件,字节落盘到会话工作区 .uploads/<会话ID>/,绝对路径追加进输入框(可见可编辑),AI 用自带 fs 工具直接读取。零依赖。（✅ 活跃）

### Skills


#### 🔥 Top 10

| # | 项目 | 星数 | 说明 | 状态 |
|---|---|---|---|---|
| 1 | [memos](https://github.com/MemTensor/MemOS) | ⭐10,873 | Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings and DeepSeek Harness support. | ✅ 活跃 |
| 2 | [dsh-routing-suite](https://github.com/yjh051108/dsh-routing-suite) | ⭐6,940 | dsh-routing-suite — injector + router-standard kit: install the runtime injector first, then the task-aware reasoning-mode router preset (measured P1-P23). | ✅ 活跃 |
| 3 | [easyeda-agent](https://github.com/zhoushoujianwork/easyeda-agent) | ⭐274 | EasyEDA Pro automation: Go daemon + in-app connector + agent skill + stdio MCP server for typed schematic/PCB actions, workflow gates, and DRC. | ✅ 活跃 |
| 4 | [dsh-taskboard](https://github.com/shengsheng90/DSH-taskboard) | ⭐195 | Native local Taskboard plugin for DeepSeek Harness. SQLite-backed projects, Agent claim/review, and a native Web UI — no iframe, no second chat runtime. | ✅ 活跃 |
| 5 | [deepseek-harness-genui](https://github.com/pengyue-polaron/deepseek-harness-genui) | ⭐107 | Task-specific React apps for DeepSeek Harness with state carried into the next Agent turn | ✅ 活跃 |
| 6 | [dsh-skill-viewer](https://github.com/Fishquito7/dsh-skill-viewer) | ⭐88 | DSH Web 技能设置区：热启停、删除与新增。 | ✅ 活跃 |
| 7 | [dsh-reverse-skill](https://github.com/dhicoc/dsh-reverse-skill) | ⭐58 | Complete reverse-skill (85 SKILL.md) as a DeepSeek Harness (dsh) Cordis plugin — reverse engineering, authorized pentesting and security research skill pack. | ✅ 活跃 |
| 8 | [dsh-save-money](https://github.com/zhu168/dsh-save-money) | ⭐35 | Save-money plugin for DSH (DeepSeek Harness) — define your own "pause / resume" time windows; at pause time running long tasks are paused (not stopped) automatically, and they resume when the window ends. | ✅ 活跃 |
| 9 | [dsh-skill-picker](https://github.com/a735624258/dsh-skill-picker) | ⭐25 | DSH 实现 workbuddy 同款选择 skill 功能 | WorkBuddy-style skill picker for DeepSeek Harness: pick a skill in the composer, insert the official /skill-name gesture, and DSH loads it with your message. | ✅ 活跃 |
| 10 | [dsh-science](https://github.com/biociao/dsh-science) | ⭐24 | Claude Science-style research workbench: ReAct research-loop engine (research_* tools), versioned artifacts with provenance (artifact_* tools), and 10 science skills for genomics/pathogens/bioinformatics. | ✅ 活跃 |

#### 完整列表（44）

- [memos](https://github.com/MemTensor/MemOS) ⭐10,873 — Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings and DeepSeek Harness support.（✅ 活跃）
- [dsh-routing-suite](https://github.com/yjh051108/dsh-routing-suite) ⭐6,940 — dsh-routing-suite — injector + router-standard kit: install the runtime injector first, then the task-aware reasoning-mode router preset (measured P1-P23).（✅ 活跃）
- [easyeda-agent](https://github.com/zhoushoujianwork/easyeda-agent) ⭐274 — EasyEDA Pro automation: Go daemon + in-app connector + agent skill + stdio MCP server for typed schematic/PCB actions, workflow gates, and DRC.（✅ 活跃）
- [dsh-taskboard](https://github.com/shengsheng90/DSH-taskboard) ⭐195 — Native local Taskboard plugin for DeepSeek Harness. SQLite-backed projects, Agent claim/review, and a native Web UI — no iframe, no second chat runtime.（✅ 活跃）
- [deepseek-harness-genui](https://github.com/pengyue-polaron/deepseek-harness-genui) ⭐107 — Task-specific React apps for DeepSeek Harness with state carried into the next Agent turn（✅ 活跃）
- [dsh-skill-viewer](https://github.com/Fishquito7/dsh-skill-viewer) ⭐88 — DSH Web 技能设置区：热启停、删除与新增。（✅ 活跃）
- [dsh-reverse-skill](https://github.com/dhicoc/dsh-reverse-skill) ⭐58 — Complete reverse-skill (85 SKILL.md) as a DeepSeek Harness (dsh) Cordis plugin — reverse engineering, authorized pentesting and security research skill pack.（✅ 活跃）
- [dsh-save-money](https://github.com/zhu168/dsh-save-money) ⭐35 — Save-money plugin for DSH (DeepSeek Harness) — define your own "pause / resume" time windows; at pause time running long tasks are paused (not stopped) automatically, and they resume when the window ends.（✅ 活跃）
- [dsh-skill-picker](https://github.com/a735624258/dsh-skill-picker) ⭐25 — DSH 实现 workbuddy 同款选择 skill 功能 | WorkBuddy-style skill picker for DeepSeek Harness: pick a skill in the composer, insert the official /skill-name gesture, and DSH loads it with your message.（✅ 活跃）
- [dsh-science](https://github.com/biociao/dsh-science) ⭐24 — Claude Science-style research workbench: ReAct research-loop engine (research_* tools), versioned artifacts with provenance (artifact_* tools), and 10 science skills for genomics/pathogens/bioinformatics.（✅ 活跃）
- [dsh-media-skills](https://github.com/MJorgin/dsh-media-skills) ⭐19 — Free image reading & generation for DeepSeek Harness (rc.7 / rc.8 / v0.1.1-rc.1 / rc.2) — paste-image reading with auto vision transcription, DeepSeek-V4-Flash-Vision-Exp / GLM-4V-Flash / SenseNova / Gemini failover, Kolors + U1 Fast generation. No keys in repo.（✅ 活跃）
- [dsh-opencode-palette](https://github.com/FeatherHunter/dsh-opencode-palette) ⭐18 — 🎨 看腻了 DSH 默认皮肤？34 款 opencode 经典配色一键换上——tokyonight、dracula、gruvbox、matrix、rose-pine……即点即换，重启不丢。34 opencode themes for DeepSeek Harness, one click, persisted. More by @FeatherHunter: ⚡ dsh-prompt · 🧠 dsh-mattpocock-skills-deck（✅ 活跃）
- [dsh-directorx](https://github.com/LaplaceYoung/dsh-directorx) ⭐16 — DirectorX as a DeepSeek Harness plugin: AI video/image/audio skills, knowledge corpus, and configurable vision/image/video/audio model tools.（✅ 活跃）
- [dsh-evoresearch](https://github.com/Karbo123/DSH-EvoResearch) ⭐14 — 自进化科研工作流（✅ 活跃）
- [dsh-plugin-development](https://github.com/w2112515/dsh-plugin-development) ⭐14 — Portable Agent Skill for developing and auditing DeepSeek Harness plugins, with an optional profile-installable DSH bundle adapter.（✅ 活跃）
- [dsh_plugin_swift_cycle](https://github.com/Solismuchengxue/dsh_plugin_swift_cycle) ⭐14 — Swift Cycle governance skill adapter for DeepSeek Harness; user-invoked, version-pinned, and offline-verifiable.（✅ 活跃）
- [dsh-plugin-dev](https://github.com/omdsh-dev/dsh-plugin-dev) ⭐13 — 插件开发踩坑与做法档案（skill + 文档）：cordis 双副本、tsconfig 三件套、Windows junction、多帧 zstd 实测。（✅ 活跃）
- [dsh-claude-move](https://github.com/PerryLink/dsh-claude-move) ⭐11 — Four-source migration wizard for DeepSeek Harness: move Claude Code, Codex, OpenCode and Hermes sessions, memories, skills, instructions and slash commands into DSH (/move wizard + resumable sessions, approval-gated, idempotent).（✅ 活跃）
- [dsh-plugin-skills](https://github.com/omdsh-dev/dsh-plugin-skills) ⭐11 — 构建与测试 DSH 插件的 Agent 技能：从脚手架到发布。（✅ 活跃）
- [dsh-fail-logger](https://github.com/Areium/dsh-fail-logger) ⭐9 — DeepSeek Harness（DSH）插件：自动记录所有执行模式（原生工具 / PTC run_code / 代码内嵌工具调用）的工具失败错因，去重、计数、确定性排序后沉淀进 skill 的机器维护实录区段——让 Agent 越用越少错。（✅ 活跃）
- [dsh-godot-skill](https://github.com/akira399/dsh-godot-skill) ⭐9 — Godot Engine 4.x 全栈游戏开发技能插件。（✅ 活跃）
- [dsh-task-status](https://github.com/vlln/dsh-task-status) ⭐9 — DSH 插件：后台任务状态条（对话页任务进度 + 实时输出 tail）。官方 bundle 插件，dsh plugin --profile web add 安装（✅ 活跃）
- [dsh-codex-port](https://github.com/STARDUSTLC666/dsh-codex-port) ⭐8 — DeepSeek Harness 技能移植插件：把 ~/.codex 的 Codex 官方插件（186+ 个、583+ 技能）一键移植为 DSH 技能（codex_list/port/status），frontmatter 自动转换、幂等跳过。· Batch-port the Codex plugin family into DSH skills.（✅ 活跃）
- [dsh-book2skill](https://github.com/omdsh-dev/dsh-book2skill) ⭐4 — 书转技能插件：获取→解析→理解→生成→安装的五阶段长任务。（✅ 活跃）
- [dsh-capability-receipt](https://github.com/dongsheng123132/dsh-capability-receipt) ⭐4 — Content-addressed receipts for skills actually loaded by DeepSeek Harness（✅ 活跃）
- [dsh-remotion](https://github.com/STARDUSTLC666/dsh-remotion) ⭐4 — DSH 视频创作技能插件：注册 Remotion 官方移植技能（React 编程式视频，38 个规则文件），安装即用。· Remotion skill plugin for DeepSeek Harness.（✅ 活跃）
- [dsh-ecc](https://github.com/gongyijie85/dsh-ecc) ⭐3 — ECC（227k⭐ 操作员系统）273 个技能（95.8%）分四批移植到 DSH。（✅ 活跃）
- [dsh-find-skill](https://github.com/Moximxxx/dsh-find-skill) ⭐3 — 桥接 vercel-labs/skills 生态：LLM 驱动技能搜索、安装与管理。（✅ 活跃）
- [dsh-humanize](https://github.com/zevorn/dsh-humanize) ⭐3 — 去 AI 味写作技能：让 Agent 输出更自然。（✅ 活跃）
- [dsh-local-ai](https://github.com/PerryLink/dsh-local-ai) ⭐3 — Local-model (Ollama) integration for DeepSeek Harness: discover, pull, remove, and inspect local models, route requests to them by task type or keyword with automatic fallback to the cloud, and get a one-shot status overview via /ollama.（✅ 活跃）
- [dsh-memoryhub](https://github.com/solknight48/dsh-memoryhub) ⭐3 — MemoryHub (mh) plugin for DeepSeek Harness (dsh): auto-loads checkpoint memory on session start, adds mh_* tools and the mh skill, and a Memory tab in the web UI（✅ 活跃）
- [dsh-skillradar](https://github.com/hellosky983/dsh-skillradar) ⭐3 — 扫描会话可见技能，按与近期对话的相关度排序。（✅ 活跃）
- [dsh-web-novel-research](https://github.com/canghai666x/dsh-web-novel-research) ⭐3 — 中文网文情节查证技能：免费镜像站流程，GBK 解码与跨卷重复章节消歧。（✅ 活跃）
- [deepseek-harness-skillx](https://github.com/drowned-fish1/deepseek-harness-skillx) ⭐2 — DSH 工作流技能合集。（✅ 活跃）
- [dsh-kb-sieve](https://github.com/omdsh-dev/dsh-kb-sieve) ⭐2 — DSH knowledge-base plugin: build audit-able KB packs (references + SQLite FTS5) from md/txt/docx/pdf, deterministic retrieval (kb_query) and original-text reading (kb_read), zero-script generated skills. Apache-2.0.（✅ 活跃）
- [dsh-ponytail](https://github.com/gongyijie85/dsh-ponytail) ⭐2 — Ponytail 最懒资深工程师模式：6 个技能，改编自 DietrichGebert/ponytail。（✅ 活跃）
- [dsh-review-skills](https://github.com/ben7am1n/dsh-review-skills) ⭐2 — DSH 代码评审技能集。（✅ 活跃）
- [dsh-skill-pack-security](https://github.com/PerryLink/dsh-skill-pack-security) ⭐2 — 安全审计技能包：5 个 Agent 技能，覆盖密钥扫描、依赖审计等。（✅ 活跃）
- [dsh-skillport](https://github.com/Jesse-njx/dsh-skillport) ⭐2 — 让 Claude Code、Codex、Cursor、Gemini CLI 已有的技能在 DSH 中直接可用。（✅ 活跃）
- [mattpocock-skills-dsh](https://github.com/gongyijie85/mattpocock-skills-dsh) ⭐2 — Matt Pocock 完整发布技能集（25 个 SKILL.md：grilling、writing-for-agents、wait-what、TDD、code-review、wayfinder、ask-matt 路由等）的 DSH 移植。（✅ 活跃）
- [howto-dsh](https://github.com/dshworks/howto-dsh) ⭐1 — Verified field notes for DeepSeek Harness (dsh): traps, skills, hooks, profiles. Every claim dated against a dsh version, with source paths to re-verify. Not affiliated with DeepSeek.（✅ 活跃）
- [mattpocock-skills-dsh-zh](https://github.com/gongyijie85/mattpocock-skills-dsh-zh) ⭐1 — Matt Pocock 25 个技能正文全译中文（技术术语保留英文并附注释）。（✅ 活跃）
- [dsh-news-briefing](https://github.com/canghai666x/dsh-news-briefing)  — 新闻简报技能：多维故事评分、反标题党规则、内容优先级与中文编辑风格。（✅ 活跃）
- [mstar-workflow](https://github.com/btspoony/mstar-workflow)  — A Skill-driven Harness/Loop Engineering Workflow Agent Plugin（💤 停更）

### Workflows & Automation


#### 🔥 Top 10

| # | 项目 | 星数 | 说明 | 状态 |
|---|---|---|---|---|
| 1 | [tongflow](https://github.com/tong-io/tongflow) | ⭐902 | TongFlow — multimodal workflow studio and engine (canvas + Python plugin engine) and dsh-tongflow, the DeepSeek Harness studio plugin | ✅ 活跃 |
| 2 | [dsh-agent-team-gui](https://github.com/toolclub/dsh-agent-team-gui) | ⭐159 | Persistent multi-model workflow teams for DeepSeek Harness — dynamic lead planning, bounded DAGs, per-agent model/tools, Run Center and Token insights. | ✅ 活跃 |
| 3 | [dsh_workflow](https://github.com/omdsh-dev/dsh_workflow) | ⭐92 | 把Claude Code的UltraCode模式带给DSH，把 DSH 的一次性多 Agent 调度，升级为可生成、可保存、可治理、可观察、可恢复的 Workflow 层 | ✅ 活跃 |
| 4 | [dsh_workflow](https://github.com/icetomoyo/dsh_workflow) | ⭐92 | 把 Claude Code 的 UltraCode 模式带给 DSH：将一次性多 Agent 调度升级为可生成、可保存、可治理、可观察、可恢复的 Workflow 层。 | ✅ 活跃 |
| 5 | [dsh-plugin-agent-workflow](https://github.com/xuanyuanzhifeng/dsh-plugin-agent-workflow) | ⭐78 | DeepSeek Harness Agent Workflow | ✅ 活跃 |
| 6 | [dsh-automation](https://github.com/titanwings/dsh-automation) | ⭐70 | 让 Coding 任务按计划在全新 Agent Session 中运行，由用户或 Agent 创建和管理定时任务。 | ✅ 活跃 |
| 7 | [mstar-harness](https://github.com/btspoony/mstar-harness) | ⭐52 | 技能驱动的 Harness/Loop 工程工作流 Agent：把 Agent 循环调优作为一等工作流。 | ✅ 活跃 |
| 8 | [dsh-plans](https://github.com/Optim-Agent/dsh-plans) | ⭐42 | 从 prime-plans 移植的人机协同规划预设：调研、评审、执行。 | ✅ 活跃 |
| 9 | [dsh-auto-continue](https://github.com/HsiangNianian/dsh-auto-continue) | ⭐33 | 自动恢复中断的请求：失败分类、自适应退避重试、可配置续写消息与浏览器通知。 | ✅ 活跃 |
| 10 | [dsh-deep-research](https://github.com/omdsh-dev/dsh-deep-research) | ⭐18 | 基于官方 workflow 引擎的自适应深度研究编排器。 | ✅ 活跃 |

#### 完整列表（30）

- [tongflow](https://github.com/tong-io/tongflow) ⭐902 — TongFlow — multimodal workflow studio and engine (canvas + Python plugin engine) and dsh-tongflow, the DeepSeek Harness studio plugin（✅ 活跃）
- [dsh-agent-team-gui](https://github.com/toolclub/dsh-agent-team-gui) ⭐159 — Persistent multi-model workflow teams for DeepSeek Harness — dynamic lead planning, bounded DAGs, per-agent model/tools, Run Center and Token insights.（✅ 活跃）
- [dsh_workflow](https://github.com/omdsh-dev/dsh_workflow) ⭐92 — 把Claude Code的UltraCode模式带给DSH，把 DSH 的一次性多 Agent 调度，升级为可生成、可保存、可治理、可观察、可恢复的 Workflow 层（✅ 活跃）
- [dsh_workflow](https://github.com/icetomoyo/dsh_workflow) ⭐92 — 把 Claude Code 的 UltraCode 模式带给 DSH：将一次性多 Agent 调度升级为可生成、可保存、可治理、可观察、可恢复的 Workflow 层。（✅ 活跃）
- [dsh-plugin-agent-workflow](https://github.com/xuanyuanzhifeng/dsh-plugin-agent-workflow) ⭐78 — DeepSeek Harness Agent Workflow（✅ 活跃）
- [dsh-automation](https://github.com/titanwings/dsh-automation) ⭐70 — 让 Coding 任务按计划在全新 Agent Session 中运行，由用户或 Agent 创建和管理定时任务。（✅ 活跃）
- [mstar-harness](https://github.com/btspoony/mstar-harness) ⭐52 — 技能驱动的 Harness/Loop 工程工作流 Agent：把 Agent 循环调优作为一等工作流。（✅ 活跃）
- [dsh-plans](https://github.com/Optim-Agent/dsh-plans) ⭐42 — 从 prime-plans 移植的人机协同规划预设：调研、评审、执行。（✅ 活跃）
- [dsh-auto-continue](https://github.com/HsiangNianian/dsh-auto-continue) ⭐33 — 自动恢复中断的请求：失败分类、自适应退避重试、可配置续写消息与浏览器通知。（✅ 活跃）
- [dsh-deep-research](https://github.com/omdsh-dev/dsh-deep-research) ⭐18 — 基于官方 workflow 引擎的自适应深度研究编排器。（✅ 活跃）
- [dsh-harness-ops](https://github.com/fakechris/dsh-harness-ops) ⭐11 — 运维工具箱：官方每日快照 A/B 双槽轮换、原子切换、一键回滚、守护进程自动拉起。（✅ 活跃）
- [dsh-plannotator](https://github.com/titanwings/dsh-plannotator) ⭐10 — DSH 计划批注插件：选中计划原文、逐条批注，并把结构化反馈送回 Agent。 / A DSH plan-review plugin for anchored annotations and structured Agent feedback.（✅ 活跃）
- [dsh-deepresearch](https://github.com/havingautism/dsh-deepresearch) ⭐9 — 面向 Harness 的 DeepResearch 插件（cordis）。（🧪 实验性）
- [dsh-inspect](https://github.com/omdsh-dev/dsh-inspect) ⭐6 — 发现问题(checkup) → 修复交付(fix) → 质量复查(review) 的对抗式闭环。（✅ 活跃）
- [dsh-plugin-spur](https://github.com/HuanLinOTO/dsh-plugin-spur) ⭐6 — 聊天流中悬挂皮鞭：甩动鞭梢即向 agent 发送 go work 消息（整活）。（✅ 活跃）
- [dsh-task-dag](https://github.com/LeemanCheung/dsh-task-dag) ⭐6 — 工作流运行、子代理、状态与依赖的持久化实时 DAG 可视化。（✅ 活跃）
- [dsh-track](https://github.com/fakechris/dsh-track) ⭐6 — 嵌入式任务管理引擎：决策点协议、念头捕获墙、Linear 形 issue 存储。（✅ 活跃）
- [engineer-software](https://github.com/KirschBluteX/engineer-software) ⭐6 — 与运行时无关、证据驱动的软件工程工作流，适用于 Codex 与 DeepSeek Harness。（✅ 活跃）
- [dsh-companion](https://github.com/william-jin-cmu/dsh-companion) ⭐5 — 常驻桌面助手：全局唤起、定时自动化、快捷回复、插件市场。（💤 停更）
- [dsh-loop](https://github.com/vlln/dsh-loop) ⭐5 — DSH 插件：定时循环（/loop 命令 + loop 工具 + 活动状态条）。官方 bundle 插件，dsh plugin --profile web add 安装（✅ 活跃）
- [dsh-continual-harness](https://github.com/jasen215/dsh-continual-harness) ⭐4 — DeepSeek Harness plugin for continual self-evolution: persistent memory, periodic review-and-refine, cross-session shared knowledge, and automatic rollback — a plan→validate→apply→rollback loop driven by a model-callable harness_refine tool.（✅ 活跃）
- [dsh-doublecheck](https://github.com/PerryLink/dsh-doublecheck) ⭐4 — 工程纪律循环：编辑前需求拷问、红/绿测试证据门、对抗式交付审查。（✅ 活跃）
- [dsh-prime-agent](https://github.com/yoke233/dsh-prime-agent) ⭐4 — Prime Agent 启发的持久 RLM 控制平面，面向 DSH Code 模式。（✅ 活跃）
- [dsh-tool-time](https://github.com/omdsh-dev/dsh-tool-time) ⭐4 — DSH 时间工具插件：严格 ISO 8601 解析、IANA 时区转换、UTC 日历运算、固定时长差，零依赖（✅ 活跃）
- [dsh-agent-orchestration](https://github.com/LeslieWylie/dsh-agent-orchestration) ⭐3 — Evidence-first multi-agent workflow planning, handoff validation, and Loop Guard skills for DeepSeek Harness.（💤 停更）
- [dsh-eval](https://github.com/hccccc01333/dsh-eval) ⭐1 — Agent 评测平台：benchmark YAML、无头 dsh 运行、基于 trace 的指标、脚本评分与运行对比。（✅ 活跃）
- [dsh-governance](https://github.com/tappass/dsh-governance) ⭐1 — Agentic AI 的权威层插件：按你的策略治理每次工具调用。（✅ 活跃）
- [dsh-report-studio](https://github.com/ciceroyang/dsh-report-studio) ⭐1 — 把 DSH 会话变成可交付工作报告（日报/周报/交接/文章），带可验证凭证。（✅ 活跃）
- [dsh-trajectory-debug](https://github.com/devmom/dsh-trajectory-debug) ⭐1 — 轨迹瀑布流、确定性回放、断点、编辑重跑、fork 对比与性能分析。（✅ 活跃）
- [dsh-plugin-skill](https://github.com/dsh-io/dsh-plugin-skill)  — Agent skill (SKILL.md) for creating DeepSeek Harness (dsh) plugins: authoritative defineTool API, schema rules, project layout and workflow — works with Claude Code, Codex, Cursor, Gemini CLI, opencode（✅ 活跃）

### Agents & Multi-Agent


#### 🔥 Top 10

| # | 项目 | 星数 | 说明 | 状态 |
|---|---|---|---|---|
| 1 | [openbiliclaw](https://github.com/whiteguo233/OpenBiliClaw) | ⭐2,971 | 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin） | ✅ 活跃 |
| 2 | [dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) | ⭐746 | 面向团队的 DSH 多 Agent 扩展。 | ✅ 活跃 |
| 3 | [dsh-univer-office](https://github.com/dream-num/dsh-univer-office) | ⭐191 | Give DeepSeek Harness a real office environment.  Univer Office Plugin brings spreadsheets, docs, slides, canvases, relational tables, and more into one runtime — with connected data, validation, versioned changes, and isolated worktrees for multi-agent collaboration. | ✅ 活跃 |
| 4 | [dsh-agent-rp](https://github.com/hewzhew/dsh-agent-rp) | ⭐169 | SillyTavern 迁移与下一代 Agent 角色扮演。 | ✅ 活跃 |
| 5 | [dsh-auto-review](https://github.com/PerryLink/dsh-auto-review) | ⭐116 | Second-model AI auto-review for DeepSeek Harness approval requests: a read-only reviewer subagent returns structured allow/deny verdicts with reasons, fail-closed by default, fully auditable from the session log (approval/asked -> autoReview/verdict -> approval/decided). | ✅ 活跃 |
| 6 | [dsh-data-agent](https://github.com/omdsh-dev/dsh-data-agent) | ⭐104 | 会话级数据库连接 + 专用数据 Agent：让模型连数据库、写 SQL。 | ✅ 活跃 |
| 7 | [dsh-openbiliclaw](https://github.com/whiteguo233/dsh-openbiliclaw) | ⭐48 | OpenBiliClaw 是本地运行的跨平台个性化内容推荐 Agent，持续理解你的兴趣并主动找内容。本仓库是它的 DeepSeek Harness 插件：DSH 界面常驻第四栏（推荐/内容库/对话/画像/设置），注册 22 个 Agent Bridge 工具，让 Agent 也能读推荐、答探测、闭环学习。 | ✅ 活跃 |
| 8 | [allinluna](https://github.com/zenx0x/allinluna) | ⭐41 | 面向 Codex 与 DeepSeek Harness 的资源感知多 Agent 编排。 | ✅ 活跃 |
| 9 | [dsh-tianshu-build](https://github.com/huiliyi37/dsh-tianshu-build) | ⭐36 | DeepSeek X Tianshu  Harness build 是一款完全体开源 coding agent:在 dsh harness 基础之上带视觉、跨会话记忆、验证门、agent 路由、语义 + 图谱代码检索、文件回滚和全屏终端 UI——全部以插件组合。  它是 DeepSeek Harness(dsh)的友好 MIT fork, 它保留了上游一切皆插件的架构，并将以harness最佳形态和架构往下演进。 | ✅ 活跃 |
| 10 | [dsh-interconnect](https://github.com/Chinesezjc/dsh-interconnect) | ⭐34 | 跨实例消息/事件交接插件（interconnect 服务 + 工具）。 | ✅ 活跃 |

#### 完整列表（28）

- [openbiliclaw](https://github.com/whiteguo233/OpenBiliClaw) ⭐2,971 — 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin）（✅ 活跃）
- [dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) ⭐746 — 面向团队的 DSH 多 Agent 扩展。（✅ 活跃）
- [dsh-univer-office](https://github.com/dream-num/dsh-univer-office) ⭐191 — Give DeepSeek Harness a real office environment.  Univer Office Plugin brings spreadsheets, docs, slides, canvases, relational tables, and more into one runtime — with connected data, validation, versioned changes, and isolated worktrees for multi-agent collaboration.（✅ 活跃）
- [dsh-agent-rp](https://github.com/hewzhew/dsh-agent-rp) ⭐169 — SillyTavern 迁移与下一代 Agent 角色扮演。（✅ 活跃）
- [dsh-auto-review](https://github.com/PerryLink/dsh-auto-review) ⭐116 — Second-model AI auto-review for DeepSeek Harness approval requests: a read-only reviewer subagent returns structured allow/deny verdicts with reasons, fail-closed by default, fully auditable from the session log (approval/asked -> autoReview/verdict -> approval/decided).（✅ 活跃）
- [dsh-data-agent](https://github.com/omdsh-dev/dsh-data-agent) ⭐104 — 会话级数据库连接 + 专用数据 Agent：让模型连数据库、写 SQL。（✅ 活跃）
- [dsh-openbiliclaw](https://github.com/whiteguo233/dsh-openbiliclaw) ⭐48 — OpenBiliClaw 是本地运行的跨平台个性化内容推荐 Agent，持续理解你的兴趣并主动找内容。本仓库是它的 DeepSeek Harness 插件：DSH 界面常驻第四栏（推荐/内容库/对话/画像/设置），注册 22 个 Agent Bridge 工具，让 Agent 也能读推荐、答探测、闭环学习。（✅ 活跃）
- [allinluna](https://github.com/zenx0x/allinluna) ⭐41 — 面向 Codex 与 DeepSeek Harness 的资源感知多 Agent 编排。（✅ 活跃）
- [dsh-tianshu-build](https://github.com/huiliyi37/dsh-tianshu-build) ⭐36 — DeepSeek X Tianshu  Harness build 是一款完全体开源 coding agent:在 dsh harness 基础之上带视觉、跨会话记忆、验证门、agent 路由、语义 + 图谱代码检索、文件回滚和全屏终端 UI——全部以插件组合。  它是 DeepSeek Harness(dsh)的友好 MIT fork, 它保留了上游一切皆插件的架构，并将以harness最佳形态和架构往下演进。（✅ 活跃）
- [dsh-interconnect](https://github.com/Chinesezjc/dsh-interconnect) ⭐34 — 跨实例消息/事件交接插件（interconnect 服务 + 工具）。（✅ 活跃）
- [dsh-plugin-cc](https://github.com/cpj-dev/dsh-plugin-cc) ⭐29 — 将 DSH 桥接到 Claude Code：审查、批判、委托与会话导入。（✅ 活跃）
- [kixparadigm](https://github.com/olicesx/kixparadigm) ⭐23 — kixparadigm — AI self-orchestrated minimal paradigm (resident cognition layer) + kixpower multi-agent orchestration · one-command import into DeepSeek Harness (npm i -g) / AI 自编排最小范式（认知层常驻）× kixpower 多智能体编排 · npm 一键导入 DeepSeek Harness（✅ 活跃）
- [dsh-plugin-product-subagents](https://github.com/shaokeyibb/dsh-plugin-product-subagents) ⭐17 — 基于角色的 Codex/Claude Code/ACP 子代理提供方：可延续的子任务，带持久状态。（✅ 活跃）
- [dsh-plugin-yet-another-subagent](https://github.com/HuanLinOTO/dsh-plugin-yet-another-subagent) ⭐12 — 可配置子代理 profile 系统：单一 subagent 工具 + profile 参数，含 Web UI 设置与实时进度。（✅ 活跃）
- [dsh-sidechain](https://github.com/omdsh-dev/dsh-sidechain) ⭐10 — 侧会话：/side 持续性侧会话（Codex 风格）与 /btw 一次性侧问（Claude 风格），临时 fork 中运行。（✅ 活跃）
- [dsh-plugin-claude-bridge](https://github.com/YYTbit/dsh-plugin-claude-bridge) ⭐9 — 把 Claude Code 的记忆、技能与配置桥接到 DSH。（✅ 活跃）
- [Task Passport](https://github.com/dongsheng123132/task-passport) ⭐9 — 跨编码 Agent 环境的开放任务交接协议：交接可验证的状态而非聊天记录。（✅ 活跃）
- [dsh-background-agents](https://github.com/PerryLink/dsh-background-agents) ⭐7 — Interactive long-session background agents for DeepSeek Harness: start a durable continuable child agent, watch its progress in the Web UI sidebar, message it any time, and interrupt it - all through the official subagent seam.（✅ 活跃）
- [dsh-ha-orchestrator](https://github.com/Saktawdi/dsh-ha-orchestrator) ⭐7 — DeepSeek Harness（dsh）动态 Cordis 插件：模型高可用回退 + 五种模式子智能体编排（fanout / pipeline / supervisor / map-reduce / router）（✅ 活跃）
- [dsh-a2a](https://github.com/dpskh/dsh-a2a) ⭐6 — 面向 Harness 的 Agent2Agent 网状网络。（✅ 活跃）
- [dsh-reasoning-settings](https://github.com/JuneLearn/dsh-reasoning-settings) ⭐6 — 让 DeepSeek Harness 的第三方 API 支持低、中、高等推理强度，并可为每次子 Agent 调用选择模型｜Add Low, Medium, High, and other reasoning levels to third-party APIs, with model selection for each subagent call（✅ 活跃）
- [dsh-agent-messaging](https://github.com/happyren/dsh-agent-messaging) ⭐5 — 跨会话 Agent 互发消息：按名称寻址其他会话。（✅ 活跃）
- [dsh-crosstalk](https://github.com/Jesse-njx/dsh-crosstalk) ⭐2 — 跨会话消息：同机 DSH 会话之间可发现、互发消息并协同。（✅ 活跃）
- [dsh-slice-agent-loop](https://github.com/TT-Wang/dsh-slice-agent-loop) ⭐2 — 可替换的 Agent 循环：上下文引擎是有界切片而非不断增长的记录。（✅ 活跃）
- [dsh-subagent-tools](https://github.com/lynx-gt/dsh-subagent-tools) ⭐2 — 子代理委托的逐调用模型/provider/persona/toolFilter 覆盖，支持 @preset 引用。（✅ 活跃）
- [dsh-swarm-router](https://github.com/r600a-code/dsh-swarm-router) ⭐2 — DSH plugin: sub-agent matrix swarm — routes heterogeneous tasks to the most suitable model (OpenRouter-like + cfgpu.com/llm/square), dispatches each via in-process subagents. 32/32 benchmark green.（✅ 活跃）
- [dsh-cross-session](https://github.com/Wha1eChai/dsh-cross-session) ⭐1 — 同运行时跨会话发现与通信。（✅ 活跃）
- [dsh-supervisor](https://github.com/Wha1eChai/dsh-supervisor) ⭐1 — 同运行时跨会话发现与通信。（✅ 活跃）

### Clients (Desktop & TUI)


#### 🔥 Top 10

| # | 项目 | 星数 | 说明 | 状态 |
|---|---|---|---|---|
| 1 | [open-design](https://github.com/nexu-io/open-design) | ⭐90,033 | 🎨 The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode / Hermes & 20+ CLIs via BYOK. | ✅ 活跃 |
| 2 | [deepseek-harness-desktop (Anywhere Labs)](https://github.com/anywhere-labs/deepseek-harness-desktop) | ⭐17,280 | 为 DeepSeek Harness 生态打造的现代化桌面端体验（插件）。 | ✅ 活跃 |
| 3 | [desktop-cc-gui](https://github.com/zhukunpenglinyutong/desktop-cc-gui) | ⭐4,058 | Multi-engine AI coding desktop client (Tauri). Claude Code, Codex, Gemini, OpenCode, DeepSeek Harness and more in one GUI. | ✅ 活跃 |
| 4 | [echobird](https://github.com/edison7009/EchoBird) | ⭐3,105 | One-click install + model switch:Claude Code,Codex CLI (OpenAI), Grok Build (xAI), DeepSeek Harness, Kimi Code (Moonshot) ,Qwen Code,Aider,OpenCode,MiMo Code (Xiaomi),ZCode (Z.AI),OpenClaw,Pi,OpenScience,Vibe-Trading,Claude Desktop (3P profile),ChatGPT desktop,OpenCode Desktop, | ✅ 活跃 |
| 5 | [dsh-cc-tui](https://github.com/ccch1mneyyy/dsh-TUI) | ⭐2,680 | DSH 官方公众号收录的 TUI 补位插件：Claude Code 风，鲸鱼顶栏/实时状态/流式思考/双击 Esc 回滚/上下文进度+TPS。npm 一键装。  DSH official WeChat featured TUI plugin — Claude Code style: whale bar, live status, streaming thoughts, double-Esc rollback, context bar + TPS. npm one-click. | ✅ 活跃 |
| 6 | [dsh-desktop (DataElement)](https://github.com/dataelement/dsh-desktop) | ⭐1,511 | DeepSeek Harness 桌面应用。 | ✅ 活跃 |
| 7 | [deepseek-harness-eac](https://github.com/zouyuxuan122/Deepseek-Harness-EAC) | ⭐1,067 | DeepSeek Harness (dsh) Windows desktop client - bundled Node.js + dsh CLI, one-click launch, 10 built-in UI skins. EAC: Embracing All Creation 揽尽万象 | ✅ 活跃 |
| 8 | [deepseek-harness-desktop (hairyf)](https://github.com/hairyf/deepseek-harness-desktop) | ⭐814 | 一键桌面应用：全本地运行，核心自愈更新，零环境配置。Win/macOS/Linux。 | ✅ 活跃 |
| 9 | [deepseek-harness-desktop-app](https://github.com/vibeinging/deepseek-harness-desktop-app) | ⭐610 | DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts. | ✅ 活跃 |
| 10 | [dsh-work](https://github.com/vibeinging/dsh-work) | ⭐610 | Local-first AI workbench for DSH Plugins, combining Agent sessions, project files, data analysis, web research, MCP, and Office artifacts in an Electron desktop app. | ✅ 活跃 |

#### 完整列表（81）

- [open-design](https://github.com/nexu-io/open-design) ⭐90,033 — 🎨 The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode / Hermes & 20+ CLIs via BYOK.（✅ 活跃）
- [deepseek-harness-desktop (Anywhere Labs)](https://github.com/anywhere-labs/deepseek-harness-desktop) ⭐17,280 — 为 DeepSeek Harness 生态打造的现代化桌面端体验（插件）。（✅ 活跃）
- [desktop-cc-gui](https://github.com/zhukunpenglinyutong/desktop-cc-gui) ⭐4,058 — Multi-engine AI coding desktop client (Tauri). Claude Code, Codex, Gemini, OpenCode, DeepSeek Harness and more in one GUI.（✅ 活跃）
- [echobird](https://github.com/edison7009/EchoBird) ⭐3,105 — One-click install + model switch:Claude Code,Codex CLI (OpenAI), Grok Build (xAI), DeepSeek Harness, Kimi Code (Moonshot) ,Qwen Code,Aider,OpenCode,MiMo Code (Xiaomi),ZCode (Z.AI),OpenClaw,Pi,OpenScience,Vibe-Trading,Claude Desktop (3P profile),ChatGPT desktop,OpenCode Desktop,（✅ 活跃）
- [dsh-cc-tui](https://github.com/ccch1mneyyy/dsh-TUI) ⭐2,680 — DSH 官方公众号收录的 TUI 补位插件：Claude Code 风，鲸鱼顶栏/实时状态/流式思考/双击 Esc 回滚/上下文进度+TPS。npm 一键装。  DSH official WeChat featured TUI plugin — Claude Code style: whale bar, live status, streaming thoughts, double-Esc rollback, context bar + TPS. npm one-click.（✅ 活跃）
- [dsh-desktop (DataElement)](https://github.com/dataelement/dsh-desktop) ⭐1,511 — DeepSeek Harness 桌面应用。（✅ 活跃）
- [deepseek-harness-eac](https://github.com/zouyuxuan122/Deepseek-Harness-EAC) ⭐1,067 — DeepSeek Harness (dsh) Windows desktop client - bundled Node.js + dsh CLI, one-click launch, 10 built-in UI skins. EAC: Embracing All Creation 揽尽万象（✅ 活跃）
- [deepseek-harness-desktop (hairyf)](https://github.com/hairyf/deepseek-harness-desktop) ⭐814 — 一键桌面应用：全本地运行，核心自愈更新，零环境配置。Win/macOS/Linux。（✅ 活跃）
- [deepseek-harness-desktop-app](https://github.com/vibeinging/deepseek-harness-desktop-app) ⭐610 — DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts.（✅ 活跃）
- [dsh-work](https://github.com/vibeinging/dsh-work) ⭐610 — Local-first AI workbench for DSH Plugins, combining Agent sessions, project files, data analysis, web research, MCP, and Office artifacts in an Electron desktop app.（✅ 活跃）
- [dsh_desktop](https://github.com/myYangyunfan/dsh_desktop) ⭐521 — DeepSeek Harness (dsh) Windows desktop client - bundled Node.js + dsh CLI, one-click launch（✅ 活跃）
- [deepseek-harness-studio](https://github.com/fufankeji/deepseek-harness-studio) ⭐426 — DeepSeek Harness 零代码桌面端｜一键启动，支持 Windows 与 macOS；内置插件发现、热点插件推送、一键安装与管理、AI 智能推荐和视觉增强。（✅ 活跃）
- [ai-novel-writer](https://github.com/EthanYoQ/AI-Novel-Writer) ⭐422 — 本地优先 AI 小说创作工作台，提供 Windows/macOS 桌面版与 DeepSeek Harness 插件开发预览，支持角色、大纲、章节蓝图、审稿修稿和本地模型。（✅ 活跃）
- [dsh-dafeiyu](https://github.com/QCYTSN/dsh-dafeiyu) ⭐272 — Desktop-native BigFish companion for DeepSeek Harness — real Agent status, always on top on Windows.（✅ 活跃）
- [oh-dsh](https://github.com/hust-open-atom-club/oh-dsh) ⭐256 — 一站式社区发行版：TUI、桌面端与 Web UI 三种形态统一体验，分层安装。（✅ 活跃）
- [dsh-tianshu-tui](https://github.com/huiliyi37/dsh-tianshu-tui) ⭐226 — DSH 交互式终端 UI 插件：在官方基础上增加 TDD、证据门、视觉图像模块等工作流。（✅ 活跃）
- [dsh-launcher](https://github.com/Ruler4396/dsh-launcher) ⭐165 — 轻量 Windows 启动器：登录静默自启 + 极简 WebView2 窗口。（✅ 活跃）
- [deepseek-harness-desktop (ningbainb)](https://github.com/ningbainb/deepseek-harness-desktop) ⭐157 — 无损 Windows 桌面应用：完整 DSH Web UI、插件、皮肤与技能停靠栏。（✅ 活跃）
- [deepseek-harness-desktop (steven-kid)](https://github.com/steven-kid/deepseek-harness-desktop) ⭐157 — 极简跨平台桌面端：免配置，开箱即用。（✅ 活跃）
- [deepseek-harness-desktop (salathleizhang)](https://github.com/salathleizhang/deepseek-harness-desktop) ⭐138 — DeepSeek Harness 桌面封装。（✅ 活跃）
- [Deepseek-Harness-Desktop (ChisaAlter)](https://github.com/ChisaAlter/Deepseek-Harness-Desktop) ⭐131 — Electron 桌面壳：支持主题与背景图等多种个性化配置。（✅ 活跃）
- [dshcode](https://github.com/whitelonng/dshcode) ⭐126 — Community desktop companion for DeepSeek Harness — one-click Electron app for macOS and Windows（✅ 活跃）
- [dsh-launcher](https://github.com/MarcoG-h/DSH-Launcher) ⭐125 — 最全面的DeepSeek Harness🐋桌面启动器&第三方插件管理   | 离线部署 | 一键启动 | 插件管理 | API切换 |（✅ 活跃）
- [deepseek-harness-remote](https://github.com/liguobao/deepseek-harness-remote) ⭐124 — 基于 DeepSeek Harness 插件机制的多端远程访问方案，让桌面端与 Android 端安全连接并操作远程 Harness。（A multi-device remote access solution built on the DeepSeek Harness plugin system, enabling desktop and Android clients to securely connect to and operate a remote Harness.）（✅ 活跃）
- [dsh-mobile](https://github.com/saya-ch/dsh-mobile) ⭐79 — DeepSeek Harness 移动端适配与安全局域网访问插件，支持 Android App 和手机浏览器。（✅ 活跃）
- [DeepSeekHarnessDesktop (wess09)](https://github.com/wess09/DeepSeekHarnessDesktop) ⭐66 — DeepSeek Harness 桌面端打包。（✅ 活跃）
- [dsh-desktop (bruc3van)](https://github.com/bruc3van/dsh-desktop) ⭐66 — 第三方桌面客户端：直接加载官方 Web UI，可复用本机实例或内置 dsh 运行时。（✅ 活跃）
- [Martty](https://github.com/openma-ai/Martty) ⭐66 — 面向 DeepSeek Harness 的 Rust/ratatui Agent TUI，支持流式工具调用、子代理、持久会话和可扩展的 Cordis 客户端界面（deepseek-harness-tui 的继任者）。（✅ 活跃）
- [dsh-multica-runtime](https://github.com/multica-ai/dsh-multica-runtime) ⭐53 — 在 Multica 上支持 dsh 运行时。（✅ 活跃）
- [beauticode](https://github.com/starsstreaming/beautiCode) ⭐51 — 面向 AI 编程客户端的动态、可响应环境——视频背景、氛围场景与主题，适用于 DeepSeek Harness 与 Codex Desktop。（✅ 活跃）
- [deepseek-harness-desktop (xiincs)](https://github.com/xiincs/deepseek-harness-desktop) ⭐49 — 基于 Tauri 2 的原生桌面版：内置 Node.js 运行时，托盘常驻，自动更新。（✅ 活跃）
- [DeepSeek Harness TUI (openma-ai)](https://github.com/openma-ai/deepseek-harness-tui) ⭐46 — Rust/Ratatui 终端客户端，直接与 DSH 的 SDK JSON-RPC 协议通信。（✅ 活跃）
- [dsh-plugin-dev-skills](https://github.com/zimodzh/dsh-plugin-dev-skills) ⭐38 — An Agent Skills skill for developing DeepSeek Harness (DSH) plugins（开发 DSH 插件的 Agent Skill）——插件/服务/事件/工具/LLM 适配器/打包安装的标准。Works with Claude Code, Codex, DSH, VS Code Copilot & any compatible agent.（✅ 活跃）
- [deepseek-harness-desktop (hongfeiyucode)](https://github.com/hongfeiyucode/deepseek-harness-desktop) ⭐37 — DeepSeek Harness 桌面封装。（✅ 活跃）
- [deepseek-harness-termux](https://github.com/Vengisk/deepseek-harness-termux) ⭐37 — 在 Android/Termux 上运行 DeepSeek Harness。（✅ 活跃）
- [dsh-usage-plugin](https://github.com/feiyang-dev/dsh-usage-plugin) ⭐33 — DeepSeek Harness 用量与消耗插件（dsh-usage）—— 每次调用的 token 用量/缓存命中统计、峰谷计费、余额查询、CSV/JSON/PNG 导出，可经桌面端一键安装或命令行 dsh plugin add 安装。（✅ 活跃）
- [deepseek-harness-app (ipfred)](https://github.com/ipfred/deepseek-harness-app) ⭐29 — DeepSeek Harness 桌面应用。（✅ 活跃）
- [dsh-plugin-session-delete](https://github.com/lsz-asd/dsh-plugin-session-delete) ⭐26 — Delete DeepSeek Harness sessions from the UI: header danger button + sidebar session-row menu item (no conversation jump), risk-consent dialog with session name/id, stops running agents first, in-place list refresh without page reload. Works in web and the desktop client.（✅ 活跃）
- [dsh-tui](https://github.com/dsh-tui/dsh-tui) ⭐24 — Claude Code-style terminal UI for DeepSeek Harness agents, as an out-of-tree dsh plugin bundle（✅ 活跃）
- [dsh-mobile](https://github.com/lehhair/dsh-mobile) ⭐21 — Mobile client plugin (cordis + dsh.plugin.json).（✅ 活跃）
- [dsh-studio](https://github.com/Moresyl/dsh-studio) ⭐20 — DeepSeek Harness 原生桌面端 · Linux / macOS / Windows · Rust + Tauri（✅ 活跃）
- [deepseek-harness-desktop (cc1252)](https://github.com/cc1252/deepseek-harness-desktop) ⭐19 — 非官方 Windows Electron 封装。（✅ 活跃）
- [DeepSeek-Harness-Desktop (sleep2agi)](https://github.com/sleep2agi/DeepSeek-Harness-Desktop) ⭐19 — 社区桌面壳。（✅ 活跃）
- [deepseek-harness-fnos](https://github.com/techysy/deepseek-harness-fnos) ⭐18 — DeepSeek Harness (DeepSeek 官方 agent 浏览器 UI) fnOS 应用 — 本地常驻服务, 官方统一网关接入（✅ 活跃）
- [dsh-melody-launcher](https://github.com/rirko/dsh-melody-launcher) ⭐16 — dsh-旋律启动器：DeepSeek Harness 桌面启动器与插件管理器（✅ 活跃）
- [dshcockpit](https://github.com/Lxiayu/DshCockpit) ⭐16 — DshCockpit — DeepSeek Harness 桌面驾驶舱 (desktop cockpit)：运行时自动更新、成本控制、全局快捷问询、定时任务、会话全文检索、数据安全。自动更新 / 成本中心 / Quick Ask / 定时任务 / 会话搜索（✅ 活跃）
- [dsh-mobile-for-android](https://github.com/Hongtwenfive1226/DSH-Mobile-for-Android) ⭐12 — The Android mobile version of DeepSeek Harness that relies on Tailscale.（✅ 活跃）
- [dsh-grok-tui](https://github.com/chen-001/dsh-grok-tui) ⭐11 — 基于 grok-build 构建的 TUI。（✅ 活跃）
- [awesome-deepseek-harness-desktop (ADHD)](https://github.com/omdsh-dev/awesome-deepseek-harness-desktop) ⭐10 — ADHD — 开箱即用的 Electron 桌面封装。（✅ 活跃）
- [deepseek-harness-desktop](https://github.com/qyqy-1109/deepseek-harness-desktop) ⭐10 — DeepSeek Harness Desktop: self-contained Windows desktop shell (Electron) that auto-starts dsh web, plus a subtle Codex-flavored theme plugin.（✅ 活跃）
- [deepseek-harness-desktop (chyra-moon)](https://github.com/chyra-moon/deepseek-harness-desktop) ⭐10 — Windows 原生桌面壳：官方 Web UI 1:1 复刻，内置服务、托盘与自动恢复。（✅ 活跃）
- [deepseek-harness-tui (boxeryao)](https://github.com/boxeryao/deepseek-harness-tui) ⭐10 — 轻量快速终端插件，直连 DSH 运行时。（✅ 活跃）
- [dsh-desktop](https://github.com/foolgry/dsh-desktop) ⭐10 — Download-and-run desktop build of DeepSeek Harness — Electron shell with embedded Node, no npm required.（✅ 活跃）
- [dsh-record-replay](https://github.com/humblebanana/dsh-record-replay) ⭐10 — DeepSeek Harness record macOS desktop workflows by demonstration and turn them into agent skills (open-record-replay skill + orr_* tools)（✅ 活跃）
- [agentpocket](https://github.com/npu-chenlin/AgentPocket) ⭐9 — Android 客户端：通过 Tailscale 在手机上使用 Kimi Code / DeepSeek Harness 等编码 Agent 的 Web 服务（✅ 活跃）
- [deepseek-harness-desktop](https://github.com/baiyuscc13724-max/deepseek-harness-desktop) ⭐9 — Windows desktop app for DeepSeek Harness: installer, themes, in-app plugin marketplace, model routing, and updates.（✅ 活跃）
- [dsh-mobile-gui-agent](https://github.com/kunjinkao-os/dsh-mobile-gui-agent) ⭐9 — Android Mobile GUI Agent plugin for DeepSeek Harness with ADB control, iterative verification, approvals, and a Web mobile view（✅ 活跃）
- [deepseek-harness-desktop](https://github.com/omdsh-dev/deepseek-harness-desktop) ⭐8 — DSH 桌面应用打包器（✅ 活跃）
- [dsh-ux](https://github.com/jiangnanquan/dsh-ux) ⭐8 — DSH web UI 增强插件 + 无边框 Electron 桌面壳（✅ 活跃）
- [deepseek-harness-desktop](https://github.com/RZX00/deepseek-harness-desktop) ⭐7 — DeepSeek Harness with a Windows desktop build: an Electron shell over the dsh web profile, packaged as an installer（✅ 活跃）
- [deepseek-harness-pet](https://github.com/minybear/DeepSeek-Harness-Pet) ⭐7 — Codex-style desktop pet plugin for DeepSeek Harness（✅ 活跃）
- [deepseek-harness-tui (gxinxing)](https://github.com/gxinxing/deepseek-harness-tui) ⭐7 — 基于 Ink（终端 React）构建的终端原生交互 TUI。（✅ 活跃）
- [star-deepseek-harness-desktop](https://github.com/dabaicai001/star-deepseek-harness-desktop) ⭐7 — Star-deepseek-harness-desktop — DeepSeek Harness,一站式桌面运维台。Harness 自动规划并调用数据库 / SSH / SFTP / Docker 执行。本地优先、跨平台。本项目由自研的starhub 做的再次改进，现在改进中... 尽情期待吧，如果想使用老版本可以下载 0.6X.X 版本（✅ 活跃）
- [deepseek-harness-cli](https://github.com/Richard-Yang0130/deepseek-harness-cli) ⭐6 — Claude Code-style terminal interface for DeepSeek Harness（✅ 活跃）
- [deepseek-harness-desktop](https://github.com/HaoyueQin/deepseek-harness-desktop) ⭐6 — A desktop shell for DeepSeek Harness — the pluggable AI agent harness from DeepSeek. Wrap the official dsh web UI into a native-feeling, always-on desktop app. / 为 DeepSeek Harness（DeepSeek 开源的可插拔 AI Agent harness）打造的桌面应用壳，把官方 dsh web 界面包装成原生质感、常驻后台的桌面应用。（✅ 活跃）
- [dsh-codex-pet](https://github.com/skr311/dsh-codex-pet) ⭐6 — dsh-codex-pet · DSH 桌面宠物插件 — 导入精灵图序列帧宠物，悬浮浮层渲染 + Agent 状态联动（✅ 活跃）
- [dsh-desk-pet](https://github.com/anneheartrecord/dsh-desk-pet) ⭐5 — Always-on-top DeepSeek Harness desktop pet. Default whale, four skins, four silent states.（✅ 活跃）
- [dsh-desktop-electron](https://github.com/Void0312Aurora/dsh-desktop-electron) ⭐5 — 跨平台 Electron 桌面壳：托盘常驻独立窗口。（✅ 活跃）
- [deepseek-harness-for-android](https://github.com/standtrain/deepseek-harness-for-android) ⭐4 — 该程序是一个独立的 Capacitor Android 应用，用于管理本机 DeepSeek Harness Ubuntu 用户空间。它提供运行时安装与重置、Ubuntu 终端、可选的 Shizuku 设备 Shell 访问、设置，以及仅限回环地址的内嵌 Harness Web 界面。（✅ 活跃）
- [dsh-closerai](https://github.com/sb1733831438-maker/DSH-closerAI) ⭐4 — CloserAI - a local-first, model-agnostic, permission-transparent desktop AI workbench built on DeepSeek Harness.（✅ 活跃）
- [dsh-launcher-android](https://github.com/qawse110/dsh-launcher-android) ⭐4 — DshLauncher: single-APK Android launcher for DeepSeek Harness with embedded Node runtime（✅ 活跃）
- [dsh-tui](https://github.com/orriduck/dsh-tui) ⭐4 — A small, session-aware terminal UI for DeepSeek Harness（✅ 活跃）
- [deepseek-harness-desktop](https://github.com/Easyhoov/deepseek-harness-desktop-windows) ⭐3 — Unofficial in-process desktop app for DeepSeek Harness: the host composition boots inside the Electron main process with zero ports and an IPC bridge. Not affiliated with DeepSeek.（✅ 活跃）
- [deepseek-harness-workbench](https://github.com/xuan-ao-1/deepseek-harness-workbench) ⭐3 — DeepSeek Harness 官方架构的 Windows 桌面发行版 (Desktop distribution of the official DeepSeek Harness)（✅ 活跃）
- [dsh-vault](https://github.com/feiyang-dev/dsh-vault) ⭐3 — DeepSeek Harness 数据保险箱插件（dsh-vault）—— 自动备份、清空检测、一键恢复，保护聊天记录与工作区数据；可经桌面端一键安装或命令行 dsh plugin add 安装。（✅ 活跃）
- [dsh-pi-tui](https://github.com/lqhl/dsh-pi-tui) ⭐2 — Pi TUI 前端：流式 Markdown、思考折叠、工具卡片、斜杠命令与审批浮层。（✅ 活跃）
- [dsh-portable-launcher](https://github.com/15828148/dsh-portable-launcher) ⭐2 — One-click portable launcher for DeepSeek Harness (dsh) Web UI on Windows. Auto-installs Node.js and dsh with China mirror fallback, 3-stage progress with retries and resume, zero-download fast path when ready. No admin needed.（✅ 活跃）
- [dsh-desktop](https://github.com/xiaowei2025cqu23phy/dsh-desktop) ⭐1 — DeepSeek Harness 桌面客户端:AI 屏保、手机 PWA 遥控(扫码配对)、QQ/Telegram 机器人通道(审批/提问按钮)、模式提示词(工作助手/对话朋友)、壁纸美化等。（✅ 活跃）
- [dsh-desktop-launcher](https://github.com/becomeless/dsh-desktop-launcher)  — Windows/macOS desktop launcher for DeepSeek Harness: double-click to launch, zero console windows, auto-stop on close | 双击图标一键启动 DeepSeek Harness 的桌面启动器（Windows / macOS）（✅ 活跃）
- [dsh-quickstart](https://github.com/qzhqzh/dsh-quickstart)  — Desktop launcher for DeepSeek Harness - start dsh web with no console window and auto-open the browser. Tested on Windows; macOS/Linux in progress.（✅ 活跃）
- [dsh-start](https://github.com/zhengjy01/dsh-start)  — macOS 上 DSH Web GUI 的一键启停启动器：前台/后台启动、停止、状态、防重复启动、自动打开浏览器，并可用脚本构建程序坞版 DSH.app。（✅ 活跃）

### MCP & Integrations


#### 🔥 Top 10

| # | 项目 | 星数 | 说明 | 状态 |
|---|---|---|---|---|
| 1 | [Coding Tools MCP](https://github.com/xyTom/coding-tools-mcp) | ⭐846 | 面向编码的 MCP 工具集：让任何 AI Agent 获得编码能力。 | ✅ 活跃 |
| 2 | [memtrace-public](https://github.com/syncable-dev/memtrace-public) | ⭐459 | Structural memory for AI coding agents. Bi-temporal graph, MCP-native, zero LLM calls. Cursor · Claude Code · Codex · DeepSeek Harness · Hermes · VS Code · Windsurf. | ✅ 活跃 |
| 3 | [dsh-plugin-bridge](https://github.com/Totoro-qaq/dsh-plugin-bridge) | ⭐163 | DeepSeek Harness plugin for previewable cross-preset session migration. Fixed-schema handoffs preserve state, source-model intent, and unresolved images; the original session stays untouched. | ✅ 活跃 |
| 4 | [dsh-openpencil](https://github.com/ZSeven-W/dsh-openpencil) | ⭐135 | OpenPencil 设计预览与编辑集成。 | ✅ 活跃 |
| 5 | [dsh-super-injector](https://github.com/yjh051108/dsh-super-injector) | ⭐133 | 上下文注入增强插件（cordis）。 | ✅ 活跃 |
| 6 | [dsh-crew](https://github.com/ZSeven-W/dsh-crew) | ⭐119 | DeepSeek Harness (DSH) plugin: dispatch work to DSH agents from Claude Code / Codex — native subagent progress, in-host worker sessions with per-tier presets, and a multimodal bridge that lends the text-only harness vision and image generation. | ✅ 活跃 |
| 7 | [dsh-skill-mcp-panel](https://github.com/Fishquito7/dsh-skill-mcp-panel) | ⭐111 | DSH Web UI plugin: skill and MCP management（Web界面的skill/MCP管理工具） | ✅ 活跃 |
| 8 | [dsh-tabbit](https://github.com/Tabbit-Browser/dsh-tabbit) | ⭐96 | Tabbit Browser plugins for Deepseek Harness | ✅ 活跃 |
| 9 | [dsh-qqbot](https://github.com/tencent-connect/dsh-qqbot) | ⭐70 | 让 QQ 机器人接入 DeepSeek Harness（dsh）的官方插件 | ✅ 活跃 |
| 10 | [dsh-lark](https://github.com/omdsh-dev/dsh-lark) | ⭐41 | Lark/Feishu IM bot channel for DeepSeek Harness | 飞书 DeepSeek Harness 插件 | ✅ 活跃 |

#### 完整列表（86）

- [Coding Tools MCP](https://github.com/xyTom/coding-tools-mcp) ⭐846 — 面向编码的 MCP 工具集：让任何 AI Agent 获得编码能力。（✅ 活跃）
- [memtrace-public](https://github.com/syncable-dev/memtrace-public) ⭐459 — Structural memory for AI coding agents. Bi-temporal graph, MCP-native, zero LLM calls. Cursor · Claude Code · Codex · DeepSeek Harness · Hermes · VS Code · Windsurf.（✅ 活跃）
- [dsh-plugin-bridge](https://github.com/Totoro-qaq/dsh-plugin-bridge) ⭐163 — DeepSeek Harness plugin for previewable cross-preset session migration. Fixed-schema handoffs preserve state, source-model intent, and unresolved images; the original session stays untouched.（✅ 活跃）
- [dsh-openpencil](https://github.com/ZSeven-W/dsh-openpencil) ⭐135 — OpenPencil 设计预览与编辑集成。（✅ 活跃）
- [dsh-super-injector](https://github.com/yjh051108/dsh-super-injector) ⭐133 — 上下文注入增强插件（cordis）。（✅ 活跃）
- [dsh-crew](https://github.com/ZSeven-W/dsh-crew) ⭐119 — DeepSeek Harness (DSH) plugin: dispatch work to DSH agents from Claude Code / Codex — native subagent progress, in-host worker sessions with per-tier presets, and a multimodal bridge that lends the text-only harness vision and image generation.（✅ 活跃）
- [dsh-skill-mcp-panel](https://github.com/Fishquito7/dsh-skill-mcp-panel) ⭐111 — DSH Web UI plugin: skill and MCP management（Web界面的skill/MCP管理工具）（✅ 活跃）
- [dsh-tabbit](https://github.com/Tabbit-Browser/dsh-tabbit) ⭐96 — Tabbit Browser plugins for Deepseek Harness（✅ 活跃）
- [dsh-qqbot](https://github.com/tencent-connect/dsh-qqbot) ⭐70 — 让 QQ 机器人接入 DeepSeek Harness（dsh）的官方插件（✅ 活跃）
- [dsh-lark](https://github.com/omdsh-dev/dsh-lark) ⭐41 — Lark/Feishu IM bot channel for DeepSeek Harness | 飞书 DeepSeek Harness 插件（✅ 活跃）
- [dsh-browser](https://github.com/wqty123/dsh-browser) ⭐37 — Shared real browser plugin for DeepSeek Harness（✅ 活跃）
- [dsh-lark-bot](https://github.com/PlutoKeating/dsh-lark-bot) ⭐37 — DeepSeek Harness (dsh) 接入飞书/Lark bot，扫码即用：流式卡片、项目工作区、并行任务、多角色 Agent、跨会话通知、对话内模型/密钥管理与安全网守护（dsh 崩溃后飞书仍可自救）。A scan-to-connect bridge bot connecting DeepSeek Harness (dsh) into Feishu/Lark: streaming cards, workspaces, parallel tasks, multi-role agents, cross-session notify, in-chat model/key management, and a safety-net guardian.（✅ 活跃）
- [dsh-plugin-guide](https://github.com/PerryLink/dsh-plugin-guide) ⭐32 — Installable DSH bundle: the dsh-plugin-guide plugin-development knowledge base as an on-demand agent skill. Official docs archive (EN/ZH), Cordis primer, 114-repo community archive, 1654 archived Discussions, 20+ battle-tested pitfalls.（✅ 活跃）
- [dsh-lark-link](https://github.com/amlyczz/dsh-lark-link) ⭐30 — High-reliability Feishu/Lark bridge for DeepSeek Harness — QR one-click auth, multi-mode agents, card-based commands, zero-loss outbox, media in/out, session-log doctor, reusable DSH Web GUI（✅ 活跃）
- [deepseek-harness-docker](https://github.com/runzhliu/deepseek-harness-docker) ⭐27 — @deepseek-ai/dsh 的社区 Docker/K8s 打包，加固镜像。（✅ 活跃）
- [dsh-bottom-info-bar](https://github.com/songoao25/dsh-bottom-info-bar) ⭐26 — Bottom Info Bar — an information bar plugin for DeepSeek Harness: provider/model, live balance, peak/off-peak pricing with countdown, and real persisted per-session spend in a single line.（✅ 活跃）
- [dsh-feishu](https://github.com/PGZXB/dsh-feishu) ⭐26 — The Feishu UI for DeepSeek Harness  — a panel-driven control console: every slash command a button on the ⚙️ control-panel card, in-card approvals & questions, live streaming cards, one-QR setup. | DeepSeek Harness 的飞书 UI：面板驱动控制台——每个命令都是卡片按钮，卡内审批与提问，流式卡片，扫码一键配置。（✅ 活跃）
- [dsh-mcp-panel](https://github.com/PerryLink/dsh-mcp-panel) ⭐26 — 官方 DSH MCP 客户端的只读运行时管理面板：/mcp 命令 + 设置 Tab。（✅ 活跃）
- [deepseek-harness-vsc-extension](https://github.com/weinibuliu/deepseek-harness-vsc-extension) ⭐24 — DeepSeek Harness for VS Code as extension（💤 停更）
- [dsh-computer-use](https://github.com/ZRui-C/dsh-computer-use) ⭐24 — Text-first browser & background macOS control for DeepSeek Harness (DSH): target the right process and window without taking the user's pointer. 为 DSH 提供文本优先的电脑控制：后台操作 Chromium 与 macOS，不抢前台、不移动鼠标。（✅ 活跃）
- [dsh-ide](https://github.com/chenw2759-wq/dsh-IDE) ⭐24 — dsh-IDE 把 DeepSeek Harness（DSH）网页版升级成一站式 IDE：JupyterLab 式文件树、带语法高亮的代码编辑、多格式预览、Trae 风格红绿 diff 和内置终端，再加上「本地大脑、远程手脚」的 SSH 远程工作区，让 AI 直接在本机操控远程服务器，全程零配置文件改动。（✅ 活跃）
- [chatccc](https://github.com/wzj998/ChatCCC) ⭐22 — 飞书（Lark）或微信（WeChat）聊天控制 DeepSeek Harness / Claude Code / Cursor / Codex / CCC Agent（✅ 活跃）
- [dsh-mcp-manager](https://github.com/Js2Hou/dsh-mcp-manager) ⭐17 — 用于 DeepSeek Harness 的 MCP 可视化管理插件：在「设置 → MCP」中查看已安装/启用的 MCP 服务器，支持增删、启用/停用，并实时查看连接状态。（✅ 活跃）
- [dsh-hdc-bridge](https://github.com/1na-ko/dsh-hdc-bridge) ⭐16 — DSH 原生鸿蒙开发助手：hdc 设备闭环调试 + 设备面板（官方 client 插件形态）+ 离线官方知识层（Tier-1 随包）+ DevEco CLI 构建/签名/模拟器控制 / DSH-native HarmonyOS dev assistant: hdc device loop, live device panel, offline official knowledge, DevEco CLI build/sign/emulator（✅ 活跃）
- [dsh-movein](https://github.com/sjh9714/dsh-movein) ⭐15 — Migrate Claude Code setup into DeepSeek Harness. Import skills, commands, agents, hooks, permission rules, and MCP config. Codex and OpenCode supported.（✅ 活跃）
- [dsh-chatgpt-bridge](https://github.com/jiezeng2004-design/dsh-chatgpt-bridge) ⭐14 — MCP bridge that lets ChatGPT web create, view, continue, and control DeepSeek Harness (DSH) agent sessions.（✅ 活跃）
- [dsh-vscode](https://github.com/Lixxx1/dsh-vscode) ⭐14 — DSH Sidebar — a Claude Code/Codex-style VS Code sidebar for DeepSeek Harness. 像 Claude Code、Codex 一样，在 VS Code 侧边栏中使用 DSH。（✅ 活跃）
- [deepseek-harness-action](https://github.com/Lixiaoyiao/deepseek-harness-action) ⭐13 — 社区 GitHub Action：AI 代码审查、CI 诊断、自动修复、Issue 转 PR。（✅ 活跃）
- [dsh-git-graph](https://github.com/1841220388zzzcccxxx-star/dsh-git-graph) ⭐13 — Embedded git repository graph visualizer for the DeepSeek Harness Web GUI | 嵌入式 Git 仓库图谱可视化插件（提交历史图 / 分支过滤 / 文件 diff / VSCode 式未提交改动）（✅ 活跃）
- [deepseek-harness-acp](https://github.com/openma-ai/deepseek-harness-acp) ⭐12 — DeepSeek Harness 的 ACP 服务器实现：复用凭据与会话，将完整 DSH Agent 暴露给 ACP 客户端。（✅ 活跃）
- [dsh-search-mcp](https://github.com/gxpppp/dsh-search-mcp) ⭐12 — 用搜索 MCP 服务器（Tavily/Brave/Exa/Perplexity/DDG）替换 DSH 内置搜索。（✅ 活跃）
- [dsh-vision-proxy](https://github.com/Flyvhidbwo/dsh-vision-proxy) ⭐12 — DeepSeek Harness 插件：DeepSeek 大脑 + 自动识图。GUI 附加图片自动经 OpenAI 兼容 VLM 转译成文字后交给 DeepSeek 作答；支持百炼/智谱/OpenRouter 等任意 OpenAI 兼容端点（默认 qwen3.7-flash），无 key 自动探测本地 Ollama（图片不出本机）；安装时有一问式确认（✅ 活跃）
- [ikanban](https://github.com/isomoes/ikanban) ⭐12 — Monorepo for the iKanban browser-surface fork for DeepSeek Harness.（✅ 活跃）
- [dsh-annotate](https://github.com/BrambleXu/dsh-annotate) ⭐11 — Visual browser element annotation for DeepSeek Harness, capturing DOM, styles, accessibility data, comments, and viewport screenshots. DeepSeek Harness 浏览器元素标注插件，捕获 DOM、样式、可访问性数据、评论和视口截图。（✅ 活跃）
- [dsh-acp-for-bitfun](https://github.com/bobleer/dsh-acp-for-bitfun) ⭐10 — BitFun 与 DSH ACP 交互对接 插件（✅ 活跃）
- [dsh-better-browser](https://github.com/titanwings/dsh-better-browser) ⭐10 — DSH 真实浏览器插件：通过 Kimi WebBridge 让 Agent 操作用户已登录的浏览器，并提供 13 个 webbridge_* 工具。 / Let DSH Agents use your signed-in browser through thirteen Kimi WebBridge tools.（✅ 活跃）
- [dsh-feishu](https://github.com/xmanrui/dsh-feishu) ⭐10 — 通过扫码把飞书机器人接入DeepSeek Harness（✅ 活跃）
- [dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) ⭐10 — MCP 服务器管理器：设置页 OAuth（PKCE + 动态客户端注册）或静态 Token 认证。（✅ 活跃）
- [deepseek-acp](https://github.com/xintaofei/deepseek-acp) ⭐9 — 把 DeepSeek Harness 接成一个面向编辑器的完整编码 Agent， 通过 Agent Client Protocol（ACP）与客户端通话。（✅ 活跃）
- [dsh-harness-mcp-server](https://github.com/chushixixin/dsh-harness-mcp-server) ⭐9 — 将 DSH Agent 能力暴露为 MCP 服务器（大脑=Hermes，双手=Harness）。（✅ 活跃）
- [dsh-im-bridge](https://github.com/BiBoyang/dsh-im-bridge) ⭐9 — DSH 插件：把 DeepSeek Harness 桥接到 IM（v0.1 微信/iLink；钉钉/飞书/Telegram 预留）。turn/approval 推送 + 远程批准/注入，持久去重/收敛分段/合并窗口。（✅ 活跃）
- [dsh-lan-access](https://github.com/Leon0555/dsh-lan-access) ⭐9 — Web GUI 局域网访问：0.0.0.0 绑定 + 非安全上下文 polyfill。（✅ 活跃）
- [dsh-oauth-mcp-client](https://github.com/springbrand-lab/dsh-oauth-mcp-client) ⭐9 — OAuth 2.1 Streamable HTTP MCP 客户端插件。（✅ 活跃）
- [dsh-browser](https://github.com/xylt369/dsh-browser) ⭐8 — Browser capability for DeepSeek Harness: headed Edge/Playwright provider, SSRF-safe navigation, a11y-ref clicking, permission gate with auto-remember, gated evaluate（✅ 活跃）
- [dsh-telegram-channel](https://github.com/hi-wenw/dsh-telegram-channel) ⭐8 — Telegram 手机远程控制 DSH 实时会话：会话选择、绑定/解绑，轨迹与桌面一致。（✅ 活跃）
- [dsh-vision](https://github.com/54xkeee/dsh-vision) ⭐8 — Vision for DeepSeek Harness: Doubao Web by default (zero-cost, no API key), Antigravity IDE quota (flash/pro), any IDE CLI, Gemini — auto detail escalation, evidence memory（✅ 活跃）
- [dsh-chatnode-wechat](https://github.com/Jesse-njx/dsh-chatnode-wechat) ⭐7 — Chat with, monitor, and approve your DSH agents from WeChat — an iLink gateway + conversation node bundle for DeepSeek Harness（✅ 活跃）
- [dsh-lark-bridge](https://github.com/imetn/dsh-lark-bridge) ⭐7 — Bidirectional Lark/Feishu controller for DeepSeek Harness（✅ 活跃）
- [dsh-message-preview](https://github.com/asukasec/dsh-message-preview) ⭐7 — Right-side user-message navigator for the DeepSeek Harness Web UI.（✅ 活跃）
- [telegram](https://github.com/LoserFox/telegram) ⭐7 — Telegram Bot API 桥接插件：长轮询、per-chat 会话、HTML 格式化（✅ 活跃）
- [DSH Telegram Relay](https://github.com/congchuanling-dot/DSH-Telegram-Relay) ⭐6 — 把 Telegram 变成 DSH 远程对话渠道并接收通知。（✅ 活跃）
- [dsh-acp-plugin](https://github.com/agentic-control-plane/dsh-acp-plugin) ⭐6 — Agentic Control Plane for DeepSeek Harness — policy-check every tool call before it runs（✅ 活跃）
- [dsh-agentlink](https://github.com/hootandy321/dsh-Agentlink) ⭐6 — Caller-side bridge from Codex and other agent frameworks to DeepSeek Harness, with observable sessions, follow-up, cancellation, and human-gated approvals.（✅ 活跃）
- [dsh-mcp-lens](https://github.com/labmimors/dsh-mcp-lens) ⭐6 — DeepSeek Harness MCP tool search for large catalogs: 1,000 MCP tools behind 2 MCP-facing schemas, exact-schema calls, allow/deny controls, and a local calculator.（✅ 活跃）
- [dsh-cowork](https://github.com/Jesse-njx/dsh-cowork) ⭐5 — READ + WRITE for office documents & notebooks in DeepSeek Harness — doc_read/doc_write tools (xlsx, pdf, docx, pptx, ipynb) plus MCP server and CLI（✅ 活跃）
- [dsh-feishu-bridge](https://github.com/wz-heng/dsh-feishu-bridge) ⭐5 — Fail-closed Feishu (Lark) channel bridge for DeepSeek Harness (dsh) — chat with a bot, get agent turns back. Opt-in human-in-the-loop bash approval (Allow/Deny cards, fail-closed timeout), one-message /pair onboarding, webhook signature/timestamp/replay verification, daily latest-SDK canary. Community plugin, not DeepSeek-official.（✅ 活跃）
- [dsh-subscription-auth](https://github.com/Khellendros97/dsh-subscription-auth) ⭐5 — dsh对接openai、grok、anthropic、kimi订阅渠道（✅ 活跃）
- [dsh-talk](https://github.com/PerryLink/dsh-talk) ⭐5 — Voice-first session loop for DeepSeek Harness: a composer microphone button with browser/local speech-to-text (Web Speech, FunASR, whisper.cpp), a speak tool for text-to-speech replies (browser, edge-tts, piper), event announcements with mute, and speak-to-interrupt.（✅ 活跃）
- [dsh4vscode](https://github.com/DoggyHU/dsh4vscode) ⭐5 — 由 DSH Agent 驱动的 VS Code 聊天窗口：OpenCode 风格独立会话，模型自动路由。（✅ 活跃）
- [dsh-plugin-opencode-bridge](https://github.com/YYTbit/dsh-plugin-opencode-bridge) ⭐4 — Bridge opencode skills and config into DeepSeek Harness（✅ 活跃）
- [dsh-session-hub](https://github.com/Asaiuta/dsh-session-hub) ⭐4 — Aggregate and natively control multiple remote DeepSeek Harness (DSH) servers' sessions from one official Web UI — hub gateway + official-UI bridge. 多服务器 DSH 会话聚合与原生操控（✅ 活跃）
- [dsh-session-sync](https://github.com/PerryLink/dsh-session-sync) ⭐4 — Cross-device DeepSeek Harness session sync: a dedicated git mirror with append-only keep-both conflict resolution (fork files, never silently overwritten), /sync command and sync_* tools（✅ 活跃）
- [dsh-slack](https://github.com/STARDUSTLC666/dsh-slack) ⭐4 — DeepSeek Harness Slack 插件：slack_notify/channels/inbox/reply 四工具，Socket Mode 免公网回调收消息，收件箱队列 + 线程回复，支持自定义 slackApiUrl 对接代理网关；内置假 Slack 服务器做协议级验收测试。· Two-way Slack messaging for DeepSeek Harness agents.（✅ 活跃）
- [kimi-tide](https://github.com/tafcear/kimi-tide) ⭐4 — 月汐 — Kimi Code (Moonshot) 接入 DeepSeek Harness 的完整方案：标准 DSH 插件 + Kimi CLI 桥接维护 fork + Agent 协作闭环方法论（✅ 活跃）
- [PicGo DSH Plugin](https://github.com/PicGo/dsh-plugin) ⭐4 — PicGo 官方插件：从 DSH 上传图片/文件到图床并获取公网 URL。（✅ 活跃）
- [deepseek-harness-plugin-mcp](https://github.com/bobleer/deepseek-harness-plugin-mcp) ⭐3 — MCP server that lets any agent discover, install, and run DeepSeek Harness plugins (topic: dsh-plugin).（✅ 活跃）
- [dsh-dingtalk](https://github.com/STARDUSTLC666/dsh-dingtalk) ⭐3 — DeepSeek Harness 钉钉群机器人通知插件：dingtalk_notify/dingtalk_text 两工具，自定义机器人 webhook + HMAC 加签安全模式，手写签名实现、零运行时依赖；纯 Node 全平台。· DingTalk group-robot notifications for DeepSeek Harness agents.（✅ 活跃）
- [dsh-github](https://github.com/PerryLink/dsh-github) ⭐3 — Official-grade GitHub CI for DeepSeek Harness: composite action.yml, PR review bot with idempotent inline comments and a status-check gate, plus PR/issues tools with every write gated by human approval (Apache-2.0, dsh-plugin).（✅ 活跃）
- [dsh-mcp-manager](https://github.com/Nichts0v0/dsh-mcp-manager) ⭐3 — 在 DeepSeek Harness 设置页管理 MCP 服务器：运行时添加/编辑/启停/重连/删除，实时状态、自动重连，中英双语界面。MCP server manager for DeepSeek Harness — add, edit, enable/disable, reconnect & delete MCP servers from the web settings page, with live status and auto-reconnect.（✅ 活跃）
- [dsh-plugin-vision](https://github.com/tdf1995/dsh-plugin-vision) ⭐3 — Vision for text-only LLMs in DeepSeek Harness (DSH): describe images / OCR / VQA via free Gemini & GLM vision APIs（✅ 活跃）
- [dsh-subagent-cwd](https://github.com/lynx-gt/dsh-subagent-cwd) ⭐3 — DeepSeek Harness subagent delegation enhancement（✅ 活跃）
- [dsh-watch](https://github.com/dshworks/dsh-watch) ⭐3 — Put a watch on a stream: background listeners that wake the DeepSeek Harness agent with new matching lines — and a daemon host so a watcher runs unattended for weeks, with no task and no browser. Not affiliated with DeepSeek.（✅ 活跃）
- [shopline-ai-toolkit-dsh](https://github.com/lunw/shopline-ai-toolkit-dsh) ⭐3 — SHOPLINE AI Toolkit for DeepSeek Harness (dsh-plugin): official SHOPLINE Developer MCP bridge + SHOPLINE agent skills, mirroring the Shopify AI Toolkit architecture. dsh-plugin（✅ 活跃）
- [vscode-deepseek-harness](https://github.com/kalynnka/vscode-deepseek-harness) ⭐3 — 非官方：把 dsh 作为 VS Code 原生聊天 Agent 使用。（✅ 活跃）
- [dsh-github-integration](https://github.com/omdsh-dev/dsh-github-integration) ⭐2 — DSH 的 GitHub 集成插件。（✅ 活跃）
- [dsh-meow-cat](https://github.com/dsh-pub/dsh-meow-cat) ⭐2 — A cat runs across the bottom of the DeepSeek Harness web UI with a synthesized meow every time a conversation turn ends.（✅ 活跃）
- [dsh-plugin-acn](https://github.com/acnlabs/dsh-plugin-acn) ⭐2 — DeepSeek Harness plugin: join ACN so this agent can discover, message, and collaborate with other agents. Defaults to the China region.（✅ 活跃）
- [dsh-plugin-codex-bridge](https://github.com/YYTbit/dsh-plugin-codex-bridge) ⭐2 — Bridge codex skills and config into DeepSeek Harness（✅ 活跃）
- [dsh-plugin-pi-bridge](https://github.com/YYTbit/dsh-plugin-pi-bridge) ⭐2 — Bridge pi skills and config into DeepSeek Harness（✅ 活跃）
- [deepseek-harness-rs](https://github.com/Tokimorphling/deepseek-harness-rs) ⭐1 — DeepSeek Harness 的 Rust 移植。（🧪 实验性）
- [dsh-chrome](https://github.com/YJSoooooo/dsh-chrome) ⭐1 — Chrome 配置档桥接：通过 CDP 操控已登录的 Chrome。（✅ 活跃）
- [mcp_guard](https://github.com/dshoneys/mcp_guard) ⭐1 — 本机 MCP / Agent 口扫描、监视与审计（loopback 未鉴权 tools/list、CORS）。DeepSeek Honeys.（✅ 活跃）
- [dsh-docker](https://github.com/dshoneys/dsh-docker)  — 隔离的 DeepSeek Harness 插件安装沙箱，并对本机 MCP 口做防御性探测。（✅ 活跃）
- [dsh-wechat-bridge](https://github.com/lanbaolu/dsh-wechat-bridge)  — 个人微信桥接插件：扫码绑定后直接在微信里与本机 DeepSeek Harness Agent 对话（文字/图片/语音/文件、流式回复、会话持久化、三端通用）。（✅ 活跃）
- [opendsh](https://github.com/TheChengXi/opendsh)  — 在 VS Code 内打开 DSH Web UI，一键启停。（✅ 活跃）
- [URL Manager MCP](https://github.com/Piccolo123/url-manager-mcp)  — URL Manager 的 MCP 伴生服务器：21 个工具用于保存/搜索/分类/共享与魔法链接投递。（✅ 活跃）

### Examples & Starters


#### 🔥 Top 9

| # | 项目 | 星数 | 说明 | 状态 |
|---|---|---|---|---|
| 1 | [hello-dsh](https://github.com/pingfanfan/hello-dsh) | ⭐79 | 从零开始看懂「万物皆可插件」：零基础插件开发教程，含 22 个中文技能实例。 | ✅ 活跃 |
| 2 | [dsh-plugin-template](https://github.com/bugmaker2/dsh-plugin-template) | ⭐13 | DeepSeek Harness 插件开发模板。 | ✅ 活跃 |
| 3 | [plugin-template (omdsh-dev)](https://github.com/omdsh-dev/plugin-template) | ⭐12 | 基于原 turtle-ui 官方仓库创建的插件模板。 | ✅ 活跃 |
| 4 | [turtle-ui](https://github.com/turtle1999/turtle-ui) | ⭐8 | 官方 UI 插件参考实现。 | ✅ 活跃 |
| 5 | [dsh-plugin-template (sunshine-lang)](https://github.com/sunshine-lang/dsh-plugin-template) | ⭐6 | 可直接发布的插件骨架：bundle 格式、工具 DSL、配置与测试。 | ✅ 活跃 |
| 6 | [dsh-101](https://github.com/bill9109/dsh-101) | ⭐5 | DSH 文档阅读模式。 | ✅ 活跃 |
| 7 | [InfiniteDSH](https://github.com/vdnight89/InfiniteDSH) | ⭐3 | 诸天万界DSH：一个会话就是一本书。封面开书十九界，文学预设只写正文，规则书按关键词注入，/export-story 誊成 Markdown 小说。 | ✅ 活跃 |
| 8 | [Living-Dream-DSH](https://github.com/alllllllllli/Living-Dream-DSH) | ⭐2 | DSH 桌面配置框架：8+ MCP 服务器、免费模型渠道（CNB 代理、AMD Radeon Cloud）、Tailscale 手机远程、视觉补丁、一键安装。 | ✅ 活跃 |
| 9 | [dsh-plugin-hello](https://github.com/xu1132/dsh-plugin-hello) |  | Hello-world 风格 DSH 起步插件。 | ✅ 活跃 |

#### 完整列表（9）

- [hello-dsh](https://github.com/pingfanfan/hello-dsh) ⭐79 — 从零开始看懂「万物皆可插件」：零基础插件开发教程，含 22 个中文技能实例。（✅ 活跃）
- [dsh-plugin-template](https://github.com/bugmaker2/dsh-plugin-template) ⭐13 — DeepSeek Harness 插件开发模板。（✅ 活跃）
- [plugin-template (omdsh-dev)](https://github.com/omdsh-dev/plugin-template) ⭐12 — 基于原 turtle-ui 官方仓库创建的插件模板。（✅ 活跃）
- [turtle-ui](https://github.com/turtle1999/turtle-ui) ⭐8 — 官方 UI 插件参考实现。（✅ 活跃）
- [dsh-plugin-template (sunshine-lang)](https://github.com/sunshine-lang/dsh-plugin-template) ⭐6 — 可直接发布的插件骨架：bundle 格式、工具 DSL、配置与测试。（✅ 活跃）
- [dsh-101](https://github.com/bill9109/dsh-101) ⭐5 — DSH 文档阅读模式。（✅ 活跃）
- [InfiniteDSH](https://github.com/vdnight89/InfiniteDSH) ⭐3 — 诸天万界DSH：一个会话就是一本书。封面开书十九界，文学预设只写正文，规则书按关键词注入，/export-story 誊成 Markdown 小说。（✅ 活跃）
- [Living-Dream-DSH](https://github.com/alllllllllli/Living-Dream-DSH) ⭐2 — DSH 桌面配置框架：8+ MCP 服务器、免费模型渠道（CNB 代理、AMD Radeon Cloud）、Tailscale 手机远程、视觉补丁、一键安装。（✅ 活跃）
- [dsh-plugin-hello](https://github.com/xu1132/dsh-plugin-hello)  — Hello-world 风格 DSH 起步插件。（✅ 活跃）

### Tutorials & Learning


#### 🔥 Top 10

| # | 项目 | 星数 | 说明 | 状态 |
|---|---|---|---|---|
| 1 | [DeepSeek Harness Orange Book](https://github.com/alchaincyf/deepseek-harness-orange-book) | ⭐1,118 | 《DeepSeek Harness 橙皮书》：完整系统提示词、129 行启动清单、三份原始会话日志——官方文档没有的一手实测。PDF/EPUB/HTML 免费下载。 | ✅ 活跃 |
| 2 | [dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) | ⭐604 | 从 0 到 1 深度手册：安装/插件开发/性能调优/实测案例/同模型多 Agent 实测对比（中文 + 英文 PDF）。 | ✅ 活跃 |
| 3 | [dshfind](https://github.com/hikariming/dshfind) | ⭐200 | DSH 原理学习、插件市场与最佳实践：从 Cordis 论文逐章精读到插件自动聚合市场。 | ✅ 活跃 |
| 4 | [deepseek-harness-tutorial](https://github.com/ht426/deepseek-harness-tutorial) | ⭐182 | DeepSeek Harness 中文详细学习教程。 | ✅ 活跃 |
| 5 | [dsh-memory](https://github.com/FuRongJun-1999/dsh-memory) | ⭐66 | 白箱AGI架构探索：元认知（自我认知循环）、持续学习（知识飞轮）、世界模型（条件空间+语义时空图）、自我改进（自举纪律）、零LLM白箱管线与可审计信任护栏。 | ✅ 活跃 |
| 6 | [dsh-harness-tutorial](https://github.com/yanhua1010/dsh-harness-tutorial) | ⭐54 | DeepSeek Harness Agent 的原理与实现：从零到一实现一个 AI Agent —— 一切皆插件的中文教程（VitePress 站点 + 8 个 Demo + mini-harness 教学项目） | ✅ 活跃 |
| 7 | [deepseek-harness-handbook](https://github.com/sandbaseai/deepseek-harness-handbook) | ⭐36 | Independent, source-backed handbook for DeepSeek AI's official DeepSeek Harness (dsh): agents, plugins, security, troubleshooting, and runbooks. | ✅ 活跃 |
| 8 | [dsh-explain](https://github.com/yuezengwu/dsh-explain) | ⭐11 | 本地优先学习模式：跨会话全局学习线程、按来源讲解、ExplainContext、压缩与可诊断设置。 | ✅ 活跃 |
| 9 | [deepseek-harness-learning](https://github.com/Lucky2024-pllove/deepseek-harness-learning) | ⭐7 | 基于 deepseek-harness 仓库系统化拆解的学习网站：面向想了解 AI Agent 框架如何工作的开发者。 | ✅ 活跃 |
| 10 | [deepseek-harness-prompts](https://github.com/demouo/deepseek-harness-prompts) | ⭐6 | 不同模式下的 DeepSeek Harness 提示词集。 | ✅ 活跃 |

#### 完整列表（15）

- [DeepSeek Harness Orange Book](https://github.com/alchaincyf/deepseek-harness-orange-book) ⭐1,118 — 《DeepSeek Harness 橙皮书》：完整系统提示词、129 行启动清单、三份原始会话日志——官方文档没有的一手实测。PDF/EPUB/HTML 免费下载。（✅ 活跃）
- [dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) ⭐604 — 从 0 到 1 深度手册：安装/插件开发/性能调优/实测案例/同模型多 Agent 实测对比（中文 + 英文 PDF）。（✅ 活跃）
- [dshfind](https://github.com/hikariming/dshfind) ⭐200 — DSH 原理学习、插件市场与最佳实践：从 Cordis 论文逐章精读到插件自动聚合市场。（✅ 活跃）
- [deepseek-harness-tutorial](https://github.com/ht426/deepseek-harness-tutorial) ⭐182 — DeepSeek Harness 中文详细学习教程。（✅ 活跃）
- [dsh-memory](https://github.com/FuRongJun-1999/dsh-memory) ⭐66 — 白箱AGI架构探索：元认知（自我认知循环）、持续学习（知识飞轮）、世界模型（条件空间+语义时空图）、自我改进（自举纪律）、零LLM白箱管线与可审计信任护栏。（✅ 活跃）
- [dsh-harness-tutorial](https://github.com/yanhua1010/dsh-harness-tutorial) ⭐54 — DeepSeek Harness Agent 的原理与实现：从零到一实现一个 AI Agent —— 一切皆插件的中文教程（VitePress 站点 + 8 个 Demo + mini-harness 教学项目）（✅ 活跃）
- [deepseek-harness-handbook](https://github.com/sandbaseai/deepseek-harness-handbook) ⭐36 — Independent, source-backed handbook for DeepSeek AI's official DeepSeek Harness (dsh): agents, plugins, security, troubleshooting, and runbooks.（✅ 活跃）
- [dsh-explain](https://github.com/yuezengwu/dsh-explain) ⭐11 — 本地优先学习模式：跨会话全局学习线程、按来源讲解、ExplainContext、压缩与可诊断设置。（✅ 活跃）
- [deepseek-harness-learning](https://github.com/Lucky2024-pllove/deepseek-harness-learning) ⭐7 — 基于 deepseek-harness 仓库系统化拆解的学习网站：面向想了解 AI Agent 框架如何工作的开发者。（✅ 活跃）
- [deepseek-harness-prompts](https://github.com/demouo/deepseek-harness-prompts) ⭐6 — 不同模式下的 DeepSeek Harness 提示词集。（✅ 活跃）
- [dsh-book-deepseek-harness](https://github.com/LaplaceYoung/dsh-book-deepseek-harness) ⭐6 — 《深入理解 DeepSeek Harness：一切皆插件的 Agent 架构》——源码级架构拆解科普书：37 个章节文件、PDF、Mermaid 图。（✅ 活跃）
- [dsh-learn-everything](https://github.com/cendaifeng/dsh-learn-everything) ⭐5 — 费曼学习模式：教→复述→评判→重讲循环，渲染为富 HTML 课程卡片。（✅ 活跃）
- [gitlearnos](https://github.com/Guojiz/gitlearnos) ⭐4 — Git-native AI learning OS with a GitLearnOS-exclusive DeepSeek Harness panel, targeted practice, local RAG, and learner-owned memory.（✅ 活跃）
- [deepseek-protocol-doctor](https://github.com/Whning0513/deepseek-protocol-doctor) ⭐2 — 检查 DeepSeek 工具循环、reasoning_content、严格 schema 与捕获的 SSE，也可作为 DSH 插件。（✅ 活跃）
- [DeepSeek Harness Brain](https://github.com/AgriciDaniel/deepseek-harness-brain)  — 带来源引用的 Obsidian 知识库，包含浅显指南、架构笔记、可安装助手技能，以及 DeepSeek Harness 可移植性指南。（✅ 活跃）

### Awesome Lists & Registries


#### 🔥 Top 10

| # | 项目 | 星数 | 说明 | 状态 |
|---|---|---|---|---|
| 1 | [awesome-deepseek-integration](https://github.com/deepseek-ai/awesome-deepseek-integration) | ⭐38,897 | 官方：DeepSeek 生态集成目录 | ✅ 活跃 |
| 2 | [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | ⭐11,012 | 大型 DSH 插件精选目录（双语）。 | ✅ 活跃 |
| 3 | [awesome-deepseek-agent (official)](https://github.com/deepseek-ai/awesome-deepseek-agent) | ⭐5,966 | 官方精选：将 DeepSeek 模型集成到主流 Agent/编码助手工具的指南（AstrBot、Cherry Studio、Claude Code、Codex、DeepSeek-TUI、Reasonix 等）。 | ✅ 活跃 |
| 4 | [awesome-harness-engineering](https://github.com/walkinglabs/awesome-harness-engineering) | ⭐3,887 | Harness 工程精选（跨生态） | ✅ 活跃 |
| 5 | [awesome-dsh-plugins (Radar)](https://github.com/AdamPlatin123/awesome-dsh-plugins) | ⭐1,309 | 雷达索引仓库：自动扫描发现的所有 dsh 插件候选，带证据驱动的兼容性矩阵。 | ✅ 活跃 |
| 6 | [awesome-deepseek-harness](https://github.com/Anil-matcha/awesome-deepseek-harness) | ⭐966 | Curated guide to DeepSeek Harness (dsh) and its best community plugins | ✅ 活跃 |
| 7 | [awesome-dsh-plugin](https://github.com/Anil-matcha/awesome-dsh-plugin) | ⭐966 | A curated list of plugins for DeepSeek Harness (dsh) - DeepSeek Harness plugin ecosystem | ✅ 活跃 |
| 8 | [awesome-deepseek-coder](https://github.com/deepseek-ai/awesome-deepseek-coder) | ⭐811 | 官方：DeepSeek 编码资源 | ✅ 活跃 |
| 9 | [awesome-deepseek-harness (0xsline)](https://github.com/0xsline/awesome-deepseek-harness) | ⭐788 | DSH 生态目录：来自 dsh-external/hub 与公开 dsh-plugin 主题的插件、工具与基础设施精选。 | ✅ 活跃 |
| 10 | [awesome-dsh-plugin (bruc3van)](https://github.com/bruc3van/awesome-dsh-plugin) | ⭐261 | 用 30 秒找到适合你的 DSH 插件：不仅列仓库，还说明插件解决什么问题、适合谁、从哪开始。 | ✅ 活跃 |

#### 完整列表（82）

- [awesome-deepseek-integration](https://github.com/deepseek-ai/awesome-deepseek-integration) ⭐38,897 — 官方：DeepSeek 生态集成目录（✅ 活跃）
- [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) ⭐11,012 — 大型 DSH 插件精选目录（双语）。（✅ 活跃）
- [awesome-deepseek-agent (official)](https://github.com/deepseek-ai/awesome-deepseek-agent) ⭐5,966 — 官方精选：将 DeepSeek 模型集成到主流 Agent/编码助手工具的指南（AstrBot、Cherry Studio、Claude Code、Codex、DeepSeek-TUI、Reasonix 等）。（✅ 活跃）
- [awesome-harness-engineering](https://github.com/walkinglabs/awesome-harness-engineering) ⭐3,887 — Harness 工程精选（跨生态）（✅ 活跃）
- [awesome-dsh-plugins (Radar)](https://github.com/AdamPlatin123/awesome-dsh-plugins) ⭐1,309 — 雷达索引仓库：自动扫描发现的所有 dsh 插件候选，带证据驱动的兼容性矩阵。（✅ 活跃）
- [awesome-deepseek-harness](https://github.com/Anil-matcha/awesome-deepseek-harness) ⭐966 — Curated guide to DeepSeek Harness (dsh) and its best community plugins（✅ 活跃）
- [awesome-dsh-plugin](https://github.com/Anil-matcha/awesome-dsh-plugin) ⭐966 — A curated list of plugins for DeepSeek Harness (dsh) - DeepSeek Harness plugin ecosystem（✅ 活跃）
- [awesome-deepseek-coder](https://github.com/deepseek-ai/awesome-deepseek-coder) ⭐811 — 官方：DeepSeek 编码资源（✅ 活跃）
- [awesome-deepseek-harness (0xsline)](https://github.com/0xsline/awesome-deepseek-harness) ⭐788 — DSH 生态目录：来自 dsh-external/hub 与公开 dsh-plugin 主题的插件、工具与基础设施精选。（✅ 活跃）
- [awesome-dsh-plugin (bruc3van)](https://github.com/bruc3van/awesome-dsh-plugin) ⭐261 — 用 30 秒找到适合你的 DSH 插件：不仅列仓库，还说明插件解决什么问题、适合谁、从哪开始。（✅ 活跃）
- [Awesome-DeepSeek-Harness-Plugins](https://github.com/Zhiyuan-Fan/Awesome-DeepSeek-Harness-Plugins) ⭐240 — DeepSeek Harness 插件精选列表。（✅ 活跃）
- [awesome-deepseek-harness (libukai)](https://github.com/libukai/awesome-deepseek-harness) ⭐175 — 终极指南：快速入门、资源推荐、精选插件与实用工具。（✅ 活跃）
- [awesome-deepseek-harness (Dominic789654)](https://github.com/Dominic789654/awesome-deepseek-harness) ⭐174 — DSH 插件、技能、MCP 服务器、patch/profile 层、编排器与 UI 精选列表。（✅ 活跃）
- [notes (zhaoolee)](https://github.com/zhaoolee/notes) ⭐149 — 开源版锤子便签：一键 Docker 私有化部署、skill 调用、dsh plugin 支持、一键生成公众号格式。（✅ 活跃）
- [awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) ⭐145 — Curated community plugin directory and live marketplace for DeepSeek Harness.（✅ 活跃）
- [dsh-skin-market](https://github.com/kingOfSoySauce/dsh-skin-market) ⭐105 — DeepSeek Harness skin market 皮肤市场 已收录200+DSH 皮肤 完善评分系统加人工审核，有便捷的社区收录入口；有在线页面方便在线浏览，也有插件方便管理本地皮肤（✅ 活跃）
- [awesome-dsh-plugin](https://github.com/beancookie/awesome-dsh-plugin) ⭐93 — Awesome DeepSeek Harness (DSH) Plugin（✅ 活跃）
- [awesome-DSH-plugin (Alex-Yanggg)](https://github.com/Alex-Yanggg/awesome-DSH-plugin) ⭐77 — 精心整理的 DSH 插件、扩展、工具与开发资源列表。（✅ 活跃）
- [zat-dsh-engine](https://github.com/mishibeikejie/zat-dsh-engine) ⭐76 — Visual plugin marketplace for DeepSeek Harness — browse, search and install community plugins（✅ 活跃）
- [oh-my-dsh](https://github.com/like-study1/Oh-My-DSH) ⭐68 — 🐳 DeepSeek Harness 插件聚合社区 — 自动同步 dsh-plugin 生态 · 精选目录 · 每 8 小时自动维护 | Oh-My-DSH: a community-maintained catalog of DeepSeek Harness plugins, auto-synced from the dsh-plugin topic（✅ 活跃）
- [dsh-meow-memory](https://github.com/Phant0Meow/dsh-meow-memory) ⭐58 — Cross-session memory plugin for DeepSeek Harness: seven-layer SQLite store (soul/user/project/fact/lesson/topic/rules), BM25 retrieval, per-window dream consolidation. 跨会话七层长期记忆插件。（✅ 活跃）
- [plugin-registry](https://github.com/vlln/plugin-registry) ⭐57 — DSH 插件生态基建：薄控制台管理官方 repository 插件（0 patch）+ make-dsh-plugin 技能。（✅ 活跃）
- [dsh-session-manager](https://github.com/dream12347/dsh-session-manager) ⭐54 — DSH 会话管理插件：删除（回收站恢复/彻底清除）、统计、继续/暂停、打开日志目录、对话顶部抽屉、工作区分组与排序、上下文压缩阈值设置。DSH session manager: delete with trash/restore/purge, stats, continue/pause, log folder, header drawer, workspace grouping, context compaction threshold.（✅ 活跃）
- [oh-my-dsh](https://github.com/LaplaceYoung/oh-my-dsh) ⭐51 — 面向 DSH 的插件生态：700+ 插件，只通过扩展接缝注册，不修改 agent-loop 骨架。（✅ 活跃）
- [awesome-harness-engineering](https://github.com/jiji262/awesome-harness-engineering) ⭐49 — Harness 工程精选（中文）（✅ 活跃）
- [dsh-config-manager](https://github.com/xiajiajun516/dsh-config-manager) ⭐48 — DeepSeek Harness (DSH) backup & restore plugin — export, import, migrate and sync your complete DSH configuration, plugins, MCP servers, skills and workspace. One-click migration to another machine.（✅ 活跃）
- [dsh-market](https://github.com/2BingLing/dsh-market) ⭐46 — DeepSeek Harness 插件市场 · 持续收录 500+ DSH 插件：中文搜索 + 实用五维评分 + 一键安装。Web 版与 DSH 侧边栏插件双形态。Plugin marketplace for DeepSeek Harness: 500+ plugins, Chinese search, 5-dim scoring, one-click install.（✅ 活跃）
- [dsh-suite](https://github.com/whyihaveyou/dsh-suite) ⭐43 — 活体插件目录（785+ 插件，每小时刷新）：每日兼容性 CI、双语目录站与应用内插件商店。（✅ 活跃）
- [awesome-deepseek-harness-plugins](https://github.com/web-casa/Awesome-DeepSeek-Harness-Plugins) ⭐33 — DeepSeek Harness 插件精选（✅ 活跃）
- [sandbase-skills](https://github.com/sandbaseai/sandbase-skills) ⭐31 — 88 installable open-source Agent Skills for research, social intelligence, marketing, and business workflows—compatible with Codex, Claude Code, Cursor, Gemini CLI, and DeepSeek Harness.（✅ 活跃）
- [dsh-meme-hub](https://github.com/the-beating-light-of-the-nail/dsh-meme-hub) ⭐30 — 社区整活插件导航（皮肤、桌宠、小游戏），双语。（✅ 活跃）
- [dsh-plugin-marketplace](https://github.com/AwesomeHou/dsh-plugin-marketplace) ⭐27 — Plugin marketplace for DeepSeek Harness — live-syncs the GitHub dsh-plugin topic (1800+ repos) into a searchable, paginated settings tab with one-click install and agent tools (market_search / market_install).（✅ 活跃）
- [deepseek-plugin-store](https://github.com/Ericwong5021/deepseek-plugin-store) ⭐24 — DeepSeek Harness 独立社区插件商店：发现、安装并提交经过验证的插件、工具与扩展。 | Independent community plugin directory.（✅ 活跃）
- [awesome-dsh-plugins (kejixiaoliang)](https://github.com/kejixiaoliang/awesome-dsh-plugins) ⭐22 — DSH 插件精选目录：14 类 280+ 个社区插件，覆盖 MCP/Skill/TUI/多 Agent/上下文记忆/UI 皮肤。（✅ 活跃）
- [dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) ⭐20 — Verified plugin marketplace and autonomous registry for DeepSeek Harness（✅ 活跃）
- [dsh-plugin-hub](https://github.com/cclank/dsh-plugin-hub) ⭐17 — DeepSeek Harness community plugin registry with evidence-based screening（✅ 活跃）
- [dsh-plugin-hub](https://github.com/dshplugin/dsh-plugin-hub) ⭐16 — DeepSeek Harness 社区内置插件市场（dsh-plugin）— 搜索插件、下载并安装 4000+ 人工精选社区插件，每日更新、完全免费。内置在 Harness「设置 → 插件中心」，无需离开应用即可浏览、搜索、安装各类 AI 插件。（✅ 活跃）
- [deepseek-harness-awesome-top-500](https://github.com/weekend-project-space/deepseek-harness-awesome-top-500) ⭐15 — DeepSeek Harness Top 500 资源索引（✅ 活跃）
- [dsh-backup](https://github.com/xiaoyuyu6420/dsh-backup) ⭐14 — One command backs up & restores all of ~/.dsh for DeepSeek Harness: /backup, scheduled auto-backup, upgrade snapshots, session-log doctor & repair, out-of-process rescue console, credential redaction, GitHub sync. 一条命令备份/恢复 DSH 全部数据：升级快照、会话日志体检修复、起不来也能自救的救援通道、凭据脱敏。（✅ 活跃）
- [awesome-deepseek-harness (jiji262)](https://github.com/jiji262/awesome-deepseek-harness) ⭐13 — DeepSeek Harness 资源精选。（✅ 活跃）
- [awesome-dsh-plugins (white0dew)](https://github.com/white0dew/awesome-dsh-plugins) ⭐13 — DSH 插件公开目录，含安装命令。（✅ 活跃）
- [awesome-dsh-plugin (billLiao)](https://github.com/billLiao/awesome-dsh-plugin) ⭐12 — DeepSeek Harness 插件精选列表。（✅ 活跃）
- [dsh-checkpoint-rewind](https://github.com/PerryLink/dsh-checkpoint-rewind) ⭐12 — Claude Code /rewind for DeepSeek Harness — git-first workspace snapshots before every mutation, turn-boundary session forks, one-shot /rewind restore. A dsh-plugin capability seam.（✅ 活跃）
- [dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) ⭐12 — DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 | https://dsh-plugin-hub.hupc.site（✅ 活跃）
- [dsh-plugin-marketplace](https://github.com/w2112515/dsh-plugin-marketplace) ⭐12 — Out-of-tree installable plugin marketplace bundle for DeepSeek Harness（✅ 活跃）
- [awesome-deepseek-harness-plugins](https://github.com/vvlife/awesome-deepseek-harness-plugins) ⭐10 — DeepSeek Harness 插件目录（✅ 活跃）
- [awesome-deepseek-harness-plugins](https://github.com/walkinglabs/awesome-deepseek-harness-plugins) ⭐9 — A curated, bilingual list of verified plugins, tools, design workflows, and learning resources for DeepSeek Harness (DSH).（✅ 活跃）
- [dsh-composer-history](https://github.com/PerryLink/dsh-composer-history) ⭐8 — Terminal-style input history for the DeepSeek Harness web composer: edge-first arrows with exact draft/caret restore, browser-local persisted history, Ctrl+R reverse search, workspace recall - and sliding-context awareness (compaction summaries in recall/search, compaction notice with one-click /compact fill).（✅ 活跃）
- [dsh-us-stocks](https://github.com/Realyujie/dsh-us-stocks) ⭐8 — US stock market data tools for DeepSeek Harness, powered by yahoo-finance2（✅ 活跃）
- [awesome-dsh-bridges](https://github.com/YYTbit/awesome-dsh-bridges) ⭐6 — DSH 桥接集成目录（✅ 活跃）
- [awesome-dsh-plugins](https://github.com/cccakeee/awesome-dsh-plugins) ⭐6 — DSH 插件列表（✅ 活跃）
- [dsh-plugins](https://github.com/Sakana-yuyu/dsh-plugins) ⭐6 — DeepSeek Harness (DSH) 插件目录：官方包 + 社区插件按 GitHub stars 排名，GitHub Pages 可访问。（✅ 活跃）
- [awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) ⭐5 — DSH 插件目录（垃圾过滤开放数据）（✅ 活跃）
- [dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) ⭐5 — DeepSeek Harness plugin market - browse, search & install dsh-plugin topic plugins (dsh 插件市场：浏览/搜索/安装插件)（✅ 活跃）
- [dsh-plugins](https://github.com/HackSing/dsh-plugins) ⭐5 — A bilingual, continuously maintained directory of plugins for DeepSeek Harness (DSH).（✅ 活跃）
- [awesome-dsh-skills](https://github.com/hackerFish/awesome-dsh-skills) ⭐4 — DSH 技能目录（✅ 活跃）
- [dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) ⭐4 — DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）（✅ 活跃）
- [dsh-plugin-store](https://github.com/sandbaseai/dsh-plugin-store) ⭐4 — Native plugin marketplace for DeepSeek Harness: discover, filter, install, and manage 4,000+ community plugin packages.（✅ 活跃）
- [dsh-undo](https://github.com/LingLambda/dsh-undo) ⭐4 — Context undo/redo plugin for DeepSeek Harness (dsh): roll the model context back to the last completed step and restore it again.（✅ 活跃）
- [awesome-deepseek-harness](https://github.com/XiaomingX/awesome-deepseek-harness) ⭐3 — DeepSeek Harness 资源列表（✅ 活跃）
- [awesome-dsh-plugins](https://github.com/dongsheng123132/awesome-dsh-plugins) ⭐3 — DSH 插件精选（✅ 活跃）
- [awesome-dsh-plugins-2026](https://github.com/Herdeny/awesome-dsh-plugins-2026) ⭐3 — 2026 DSH 插件列表（✅ 活跃）
- [awesome-dsh-themes](https://github.com/dshworks/awesome-dsh-themes) ⭐3 — DSH 主题/皮肤注册表（✅ 活跃）
- [dsh-marketplace](https://github.com/ouyangyipeng/dsh-marketplace) ⭐3 — A safe, live plugin marketplace for DeepSeek Harness（✅ 活跃）
- [dsh-mask](https://github.com/PerryLink/dsh-mask) ⭐3 — PII masking middleware for DeepSeek Harness: anonymize names, phones, emails, ID cards, bank cards, keys, and addresses to placeholders before they reach the model, restore them at the display layer, keep the restore table only in memory and a controlled storage domain, never log plaintext, and expose /mask and the mask_test tool（✅ 活跃）
- [dsh-plugins](https://github.com/lwmxiaobei/dsh-plugins) ⭐3 — DeepSeek Harness 社区插件目录，自动汇总并基础校验 GitHub 插件，支持搜索、筛选、双语详情与最新版本安装命令复制。Community directory for DeepSeek Harness plugins with automated discovery, basic validation, search, filters, bilingual details, and latest version install commands.（✅ 活跃）
- [dsh-plugins-store](https://github.com/DshMarketPlace/dsh-plugins-store) ⭐3 — Browse and install DSH plugins from inside DeepSeek Harness. /store, a settings tab, and agent tools — bilingual.（✅ 活跃）
- [awesome-dsh-plugin](https://github.com/wgd753/awesome-dsh-plugin) ⭐2 — DSH 插件大集合（2000+ 链接）（✅ 活跃）
- [awesome-dsh-plugins](https://github.com/coolbat/awesome-dsh-plugins) ⭐2 — DSH 插件大目录（500+ 链接）（✅ 活跃）
- [awesome-dsh-plugins](https://github.com/jqueryscript/awesome-dsh-plugins) ⭐2 — DSH 插件列表（✅ 活跃）
- [awesome-dshoneys](https://github.com/dshoneys/awesome-dshoneys) ⭐2 — DeepSeek Honeys 认证插件目录 — 安全检测报告 + 插件需求墙 + 每周精选（✅ 活跃）
- [dshmarketplace](https://github.com/DshMarketPlace/dshmarketplace) ⭐2 — Bilingual directory of DeepSeek Harness (DSH) plugins — 3,400+ listings, sandbox-verified install commands, written detail pages, public API. Next.js on Cloudflare Workers.（✅ 活跃）
- [awesome-deepseek-harness](https://github.com/Harris1121/awesome-deepseek-harness) ⭐1 — DeepSeek Harness 资源精选（✅ 活跃）
- [awesome-deepseek-harness-plugins](https://github.com/SihanTeng/awesome-deepseek-harness-plugins) ⭐1 — DeepSeek Harness 插件精选（✅ 活跃）
- [awesome-dsh-list](https://github.com/kingselyjoe/awesome-dsh-list) ⭐1 — DSH 综合资源列表（1000+ 链接）（✅ 活跃）
- [awesome-dsh-plugins](https://github.com/oslook/awesome-dsh-plugins) ⭐1 — DSH 插件精选列表（✅ 活跃）
- [awesome-dsh-presets](https://github.com/hackerFish/awesome-dsh-presets) ⭐1 — DSH 预设目录（✅ 活跃）
- [awesome-deepseek-harness](https://github.com/Rodert/awesome-deepSeek-harness)  — DeepSeek Harness 精选资源（✅ 活跃）
- [awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness)  — DSH 社区目录（✅ 活跃）
- [dsh-plugin-registry](https://github.com/dshplugin-app/dsh-plugin-registry)  — Discover and compare DeepSeek Harness plugins directly inside DSH.（✅ 活跃）
- [dshthemes](https://github.com/dshworks/dshthemes)  — dshthemes.com — every DeepSeek Harness theme, in its own colours. A reader of dshworks/awesome-dsh-themes.（✅ 活跃）
- [plugins](https://github.com/dsh-universe/plugins)  — DeepSeek Harness plugin & skill directory — DSH Universe official marketplace (duink.com)（✅ 活跃）

### Related Agent Harnesses


#### 🔥 Top 10

| # | 项目 | 星数 | 说明 | 状态 |
|---|---|---|---|---|
| 1 | [DeerFlow](https://github.com/bytedance/deer-flow) | ⭐80,462 | 字节跳动开源的长时间跨度 SuperAgent harness：技能、记忆、沙箱、子代理、工具与消息网关。 | ✅ 活跃 |
| 2 | [CodeWhale](https://github.com/Hmbown/CodeWhale) | ⭐40,830 | 开源、社区驱动的 Agent Harness。 | ✅ 活跃 |
| 3 | [agentmemory](https://github.com/rohitg00/agentmemory) | ⭐27,233 | 基于真实基准的 AI 编码 Agent 持久记忆（DSH agentmemory 移植的上游项目）。 | ✅ 活跃 |
| 4 | [Cordis](https://github.com/cordiverse/cordis) | ⭐6,867 | 时空可组合性元框架——DeepSeek Harness 底层的插件运行时。 | ✅ 活跃 |
| 5 | [deeptide](https://github.com/paean-ai/deeptide) | ⭐1,091 | DeepSeek 官方出品的 Swift 原生 macOS 编码 Agent。 | ✅ 活跃 |
| 6 | [sandbase-harness](https://github.com/sandbaseai/sandbase-harness) | ⭐628 | 开源 CMA 兼容的任意模型 Agent 运行时：MCP 工具、沙箱会话、审计与回放。 | ✅ 活跃 |
| 7 | [mnemon](https://github.com/mnemon-dev/mnemon) | ⭐500 | LLM 监督的 Agent 持久记忆：图召回与跨会话知识，单二进制。 | ✅ 活跃 |
| 8 | [claude-paper](https://github.com/alaliqing/claude-paper) | ⭐324 | 跨 Agent 论文研究工具包：快速摘要与深度精读，支持 Claude Code/Codex/OpenCode/DSH。 | ✅ 活跃 |
| 9 | [open-managed-agents](https://github.com/openma-ai/open-managed-agents) | ⭐243 | 开源 Claude Managed Agents API 实现与自托管 Claude Tag 风格 Agent 运行时。 | ✅ 活跃 |
| 10 | [Axern](https://github.com/cofy-x/axern) | ⭐57 | 面向 AI Agent 的开源沙箱：不可信代码执行与持久服务。 | ✅ 活跃 |

#### 完整列表（11）

- [DeerFlow](https://github.com/bytedance/deer-flow) ⭐80,462 — 字节跳动开源的长时间跨度 SuperAgent harness：技能、记忆、沙箱、子代理、工具与消息网关。（✅ 活跃）
- [CodeWhale](https://github.com/Hmbown/CodeWhale) ⭐40,830 — 开源、社区驱动的 Agent Harness。（✅ 活跃）
- [agentmemory](https://github.com/rohitg00/agentmemory) ⭐27,233 — 基于真实基准的 AI 编码 Agent 持久记忆（DSH agentmemory 移植的上游项目）。（✅ 活跃）
- [Cordis](https://github.com/cordiverse/cordis) ⭐6,867 — 时空可组合性元框架——DeepSeek Harness 底层的插件运行时。（✅ 活跃）
- [deeptide](https://github.com/paean-ai/deeptide) ⭐1,091 — DeepSeek 官方出品的 Swift 原生 macOS 编码 Agent。（✅ 活跃）
- [sandbase-harness](https://github.com/sandbaseai/sandbase-harness) ⭐628 — 开源 CMA 兼容的任意模型 Agent 运行时：MCP 工具、沙箱会话、审计与回放。（✅ 活跃）
- [mnemon](https://github.com/mnemon-dev/mnemon) ⭐500 — LLM 监督的 Agent 持久记忆：图召回与跨会话知识，单二进制。（✅ 活跃）
- [claude-paper](https://github.com/alaliqing/claude-paper) ⭐324 — 跨 Agent 论文研究工具包：快速摘要与深度精读，支持 Claude Code/Codex/OpenCode/DSH。（✅ 活跃）
- [open-managed-agents](https://github.com/openma-ai/open-managed-agents) ⭐243 — 开源 Claude Managed Agents API 实现与自托管 Claude Tag 风格 Agent 运行时。（✅ 活跃）
- [Axern](https://github.com/cofy-x/axern) ⭐57 — 面向 AI Agent 的开源沙箱：不可信代码执行与持久服务。（✅ 活跃）
- [deepseek-auto-evolving-harness](https://github.com/liuchen6667/deepseek-auto-evolving-harness) ⭐28 — 自进化 LLM Agent Harness：通过 Claude Code 与 self_evolution.md 指南进行基准驱动进化。（✅ 活跃）
<!-- AUTO:resources:END -->

---

# 技能

DeepSeek Harness 技能生态仍在发展。本目录同时收录原生 DSH 技能与兼容 Harness 工作流的可复用 Agent 流程。

> 我们刻意区分**插件**与**技能**：插件提供运行时能力；技能主要提供可复用的知识、指令、流程或任务方法论。

**技能发现：** 查找包含 `SKILL.md` 的仓库，或同时涉及 `DeepSeek Harness + skills + workflow` 的项目。

---

# 工作流与自动化

这是 DSH 生态最有前景的部分之一。深度研究编排器、计划 → 执行模式、任务 DAG 与自动续跑工具均列于上文[工作流与自动化](#工作流与自动化)分区。

> **dsh-plan-execute（概念）：** 双模型计划/执行架构（规划模型思考、执行模型行动）目前尚无独立仓库——该模式存在于 [dsh-deep-research](https://github.com/omdsh-dev/dsh-deep-research) 与 [mstar-harness](https://github.com/btspoony/mstar-harness) 中。

---

# 示例

我们强烈鼓励"几分钟即可运行"而非"仅可阅读"的项目。除上文模板外，以下示例类别值得构建或寻找：

- **基础：** `01-hello-harness` · `02-custom-model` · `03-custom-tool` · `04-custom-plugin` · `05-custom-profile`
- **编码：** `06-code-review-agent` · `07-github-issue-agent` · `08-bug-fixing-agent` · `09-test-generator` · `10-frontend-builder`
- **研究：** `11-deep-research` · `12-web-research` · `13-paper-research` · `14-competitor-research` · `15-news-research`
- **多智能体：** `16-agent-team` · `17-planner-executor` · `18-parallel-research` · `19-reviewer-agent` · `20-agent-crosstalk`
- **工作流：** `21-product-launch` · `22-security-audit` · `23-seo-research` · `24-reddit-research` · `25-content-pipeline`
- **记忆与上下文：** `26-long-term-memory` · `27-context-compression` · `28-cross-session-memory` · `29-session-search` · `30-context-audit`

---

# 研究

**Agent Harness** 正日益被作为独立的优化层来研究。

### Harness 工程

任务分解、工作流结构、工具策略、重试预算与执行指引如何影响 Agent 性能。

### Harness 进化

与其保持 Harness 固定不变——`Harness v1 → 执行 → 评估 → 修改 → Harness v2`。这开启了未来方向：

* Harness 基准 · 工作流评估 · 自动化技能优化
* 工具集优化 · 自改进 Agent · 跨 Harness 可移植性

---

# 项目结构

```text
awesome-deepseek-harness/
│
├── README.md            ← 表格由生成器产出（见下）
├── README.zh-CN.md      ← 简体中文版
├── CONTRIBUTING.md
├── LICENSE
│
├── data/                ← 机器可读的唯一数据源
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
├── scripts/             ← 零依赖 Python（无需构建）
│   ├── validate.py
│   ├── check-links.py
│   ├── discover-github.py
│   ├── update-metadata.py
│   ├── generate-readme.py
│   └── generate-docs.py
│
├── docs/                ← MkDocs 站点（en/ + zh/，自动生成）
├── mkdocs.yml
│
└── .github/
    ├── workflows/
    │   ├── validate.yml
    │   └── discover.yml
    └── ISSUE_TEMPLATE/
        └── submit-project.yml
```

**README 由 `data/` 生成**——`<!-- AUTO:resources:START -->
### Plugins


#### 🔥 Top 10

| # | 项目 | 星数 | 说明 | 状态 |
|---|---|---|---|---|
| 1 | [voyager](https://github.com/Nagi-ovo/voyager) | ⭐19,755 | Enhancement suite for Gemini, AI Studio, Claude & ChatGPT — plus a prompt manager for any web UI, DeepSeek Harness included. / 面向 Gemini、AI Studio、Claude 与 ChatGPT 的增强套件；提示词管理器可用于任意 Web UI，含 DeepSeek Harness。 | ✅ 活跃 |
| 2 | [dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | ⭐5,349 | DSH Web 大型插件与皮肤集合：任务看板、Git 图、侧栏、远程/移动 UI、宠物、Token 统计与主题。 | ✅ 活跃 |
| 3 | [petdex](https://github.com/crafter-station/petdex) | ⭐3,945 | A public gallery of animated pets for Codex, Claude Code, DeepSeek Harness, Hermes, OpenCode, Gemini CLI, and more. | ✅ 活跃 |
| 4 | [dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) | ⭐3,697 | Two-phase DeepSeek Harness preset: Minimal-aligned bootstrap, then full Standard tools (Project2 98/99) | ✅ 活跃 |
| 5 | [modlens](https://github.com/liustack/modlens) | ⭐3,495 | DSH 首个视觉插件，也是所有纯文本编码 Agent 的视觉桥梁：粘贴图片即可用。 | ✅ 活跃 |
| 6 | [DSH Better Sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) | ⭐2,552 | 工作台式侧边栏：文件渲染/编辑、终端、Git、子代理，支持三方扩展 Tab。 | ✅ 活跃 |
| 7 | [dsh-market](https://github.com/dsh-market/dsh-market) | ⭐1,582 | DSH 内置可视化插件市场：浏览、搜索、一键安装。 | ✅ 活跃 |
| 8 | [dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) | ⭐1,548 | DSH Web 鲸鱼娘皮肤系列（CC BY-NC-SA 4.0）。 | ✅ 活跃 |
| 9 | [TokenTracker](https://github.com/xiufengsun/TokenTracker) | ⭐1,395 | 本地优先的 AI Token 用量与费用追踪器，支持 31 款编码工具（含 Claude Code、Codex、Cursor、Gemini 与 DeepSeek Harness）。 | ✅ 活跃 |
| 10 | [dsh-vision-router](https://github.com/ysr666/dsh-vision-router) | ⭐927 | 纯文本 Agent 的眼睛：内置免费免密钥视觉链路 + 像素级工具（问答、grounding、裁剪、OCR、SVG 描摹）。 | ✅ 活跃 |

#### 完整列表（434）

- [voyager](https://github.com/Nagi-ovo/voyager) ⭐19,755 — Enhancement suite for Gemini, AI Studio, Claude & ChatGPT — plus a prompt manager for any web UI, DeepSeek Harness included. / 面向 Gemini、AI Studio、Claude 与 ChatGPT 的增强套件；提示词管理器可用于任意 Web UI，含 DeepSeek Harness。（✅ 活跃）
- [dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) ⭐5,349 — DSH Web 大型插件与皮肤集合：任务看板、Git 图、侧栏、远程/移动 UI、宠物、Token 统计与主题。（✅ 活跃）
- [petdex](https://github.com/crafter-station/petdex) ⭐3,945 — A public gallery of animated pets for Codex, Claude Code, DeepSeek Harness, Hermes, OpenCode, Gemini CLI, and more.（✅ 活跃）
- [dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) ⭐3,697 — Two-phase DeepSeek Harness preset: Minimal-aligned bootstrap, then full Standard tools (Project2 98/99)（✅ 活跃）
- [modlens](https://github.com/liustack/modlens) ⭐3,495 — DSH 首个视觉插件，也是所有纯文本编码 Agent 的视觉桥梁：粘贴图片即可用。（✅ 活跃）
- [DSH Better Sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) ⭐2,552 — 工作台式侧边栏：文件渲染/编辑、终端、Git、子代理，支持三方扩展 Tab。（✅ 活跃）
- [dsh-market](https://github.com/dsh-market/dsh-market) ⭐1,582 — DSH 内置可视化插件市场：浏览、搜索、一键安装。（✅ 活跃）
- [dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) ⭐1,548 — DSH Web 鲸鱼娘皮肤系列（CC BY-NC-SA 4.0）。（✅ 活跃）
- [TokenTracker](https://github.com/xiufengsun/TokenTracker) ⭐1,395 — 本地优先的 AI Token 用量与费用追踪器，支持 31 款编码工具（含 Claude Code、Codex、Cursor、Gemini 与 DeepSeek Harness）。（✅ 活跃）
- [dsh-vision-router](https://github.com/ysr666/dsh-vision-router) ⭐927 — 纯文本 Agent 的眼睛：内置免费免密钥视觉链路 + 像素级工具（问答、grounding、裁剪、OCR、SVG 描摹）。（✅ 活跃）
- [dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) ⭐802 — 让纯文本模型更好的视觉工具箱：带意图图片问答、长截图 OCR、UI 还原、grounding、像素 diff。（✅ 活跃）
- [dsh-pocket](https://github.com/shaobeichen/dsh-pocket) ⭐796 — 把 DeepSeek Harness 装进你的口袋：电脑上跑 dsh web，手机扫码即同步访问（局域网 + 公网，实时同屏）Put DeepSeek Harness in your pocket: run dsh web on your computer and access it synchronously by scanning a QR code on your phone (LAN + public network, real‑time screen mirroring)（✅ 活跃）
- [dsh-context](https://github.com/bowenliang123/dsh-context) ⭐666 — A DeepSeek Harness plugin for  Context insight dashboard — showing what the model's context window is made of and how it evolves.（✅ 活跃）
- [museai](https://github.com/yejiming/MuseAI) ⭐595 — 创建你的 AI 角色，进入你的故事世界。和角色聊天、冒险、穿书，让每一次互动都留下羁绊（支持 DeepSeek Harness 插件，欢迎使用）（✅ 活跃）
- [graph-memory](https://github.com/adoresever/graph-memory) ⭐564 — Deepseek Harness、Openclaw知识图谱记忆插件。2026年4月受邀发布在清华大学讨论会。Knowledge Graph + Memory；Knowledge Graph Context Engine for OpenClaw — extracts structured triples from conversations, compresses context 75%, enables cross-session experience reuse（✅ 活跃）
- [dsh-ads](https://github.com/Nagi-ovo/dsh-ads) ⭐525 — 整活插件：2005 中文站点风格广告层，侧栏广告/对话内信息流/角落弹窗。（✅ 活跃）
- [v4-flash-godmode-opencode-go](https://github.com/SheberDavid/v4-flash-godmode-opencode-go) ⭐494 — V4 Flash 神模式 (opencode-go)：让 opencode-go 的 DeepSeek V4 Flash 从鬼模式切换到神模式的 dsh agent preset（✅ 活跃）
- [dsh-at-file](https://github.com/omdsh-dev/dsh-at-file) ⭐445 — Codex 风格 @file 提及：在 DSH 输入框中搜索工作区文件并附加内容到提示词。（✅ 活跃）
- [dsh-browser](https://github.com/Lum1104/dsh-browser) ⭐366 — Chrome 侧栏扩展：让 DSH 直接操控你的浏览器，无需视觉能力。（✅ 活跃）
- [dsh-transparent-ui-plugin](https://github.com/WYH66666666/DSH-Transparent-UI-Plugin) ⭐355 — 是一层高自由度的玻璃质感主题，套在 DeepSeek Harness 网页端。顶栏、侧边栏、输入框、统计行、轨迹视图都成了磨砂玻璃片。玻璃模糊度、磨砂度、背景（流体或自定义壁纸，壁纸还能单独调模糊和磨砂）全都能在设置卡片里自由调节。关掉开关就回到原生界面，不改 DSH 任何一行源码。（✅ 活跃）
- [flowix](https://github.com/text2future/flowix) ⭐338 — Notes for you, Memory for your agents. / 内置 Deepseek harness Agent / 适用 办公 & 写作 & Coding（✅ 活跃）
- [dsh-pentest](https://github.com/howmp/dsh-pentest) ⭐314 — 面向 DeepSeek Harness（dsh）的渗透测试模式  @CloverSecLabs（✅ 活跃）
- [dsh-genui](https://github.com/omdsh-dev/dsh-genui) ⭐282 — 对话内生成式 UI：布局、图表、表单、测验、Mermaid 与交互事件内联渲染。（✅ 活跃）
- [dsh-image-gen](https://github.com/shanliuling/dsh-image-gen) ⭐277 — Generate images directly in DeepSeek Harness chats（✅ 活跃）
- [dsh-pet](https://github.com/PC2005-cloud/dsh-pet) ⭐274 — DeepSeek Harness 桌面宠物插件 + 完整素材生成链：AI 提示词 → 绿幕视频 → 透明动画 → 可安装插件，从零到宠物全流程可复现（✅ 活跃）
- [whale-girl](https://github.com/vlln/whale-girl) ⭐260 — QQ 宠物形态桌面宠物：DSH Web 右下角悬浮，可拖拽/投喂/玩耍。（✅ 活跃）
- [dsh-synapse](https://github.com/liangmianya/dsh-synapse) ⭐250 — A visual, non-linear conversation workspace plugin for DeepSeek Harness ; A canvas-based session explorer and branching workspace for DeepSeek Harness.（✅ 活跃）
- [dsh-plugin-subscriptions](https://github.com/V1ki/dsh-plugin-subscriptions) ⭐216 — Use ChatGPT (Codex), Claude, and Grok (X Premium) subscriptions as DeepSeek Harness LLM providers — OAuth login in the web UI, no API keys（✅ 活跃）
- [dsh-memory-evolve](https://github.com/csyangwen/dsh-memory-evolve) ⭐211 — 跨会话长期记忆 + 后台自我进化：五轨记忆、git 分支感知、回合内自我审查、技能自我进化。（✅ 活跃）
- [modsearch](https://github.com/liustack/modsearch) ⭐207 — DSH 网页插件：为没有原生联网能力的模型提供搜索桥梁。（✅ 活跃）
- [dsh-wallpaper-engine](https://github.com/elysia395/dsh-wallpaper-engine) ⭐204 — 把本机 Wallpaper Engine 的壁纸变成 DSH 网页界面的背景：Video 动态播放、Web 以 iframe 加载、Scene 壁纸提取主纹理作为静态帧；iOS 液态玻璃设置窗口（配色 / 玻璃颜色 / 透明度）、内容分级与类型过滤、自定义壁纸上传、紧凑 CD 架布局、黑胶唱片展示、隐藏 / 恢复、倍速 / 翻转与自动轮播。感谢 Jerry 维护 macOS 版。（✅ 活跃）
- [dsh-visualize](https://github.com/Nagi-ovo/dsh-visualize) ⭐196 — 对话内交互式 HTML UI：流式预览与沙箱渲染。（✅ 活跃）
- [Open Sea Skin](https://github.com/d-dev0101/open-sea-skin) ⭐185 — 实时 WebGPU 海洋皮肤，可调节波浪、日光、玻璃不透明度和自动昼夜循环。（✅ 活跃）
- [anysearch-dsh](https://github.com/anysearch-team/anysearch-dsh) ⭐174 — AnySearch 网页搜索 provider 与高级搜索工具。（✅ 活跃）
- [dsh-find-plugins](https://github.com/Nagi-ovo/dsh-find-plugins) ⭐162 — DSH 生态插件发现工具。（✅ 活跃）
- [anime-find](https://github.com/cocofhu/anime-find) ⭐157 — DeepSeek Harness 搜番插件：对话内多源搜索番剧，卡片展示 Bangumi 评分与详情，支持复制磁力。（✅ 活跃）
- [dsh-mnemon](https://github.com/omdsh-dev/dsh-mnemon) ⭐156 — 三层本地记忆系统：运行时热记忆、项目文档、长期记忆空间，监督式写回。（✅ 活跃）
- [dsh-liang-skin](https://github.com/kingOfSoySauce/dsh-liang-skin) ⭐148 — DeepSeek Harness 滑动变阻器皮肤（✅ 活跃）
- [dsh-cost-meter](https://github.com/Han-1413141/dsh-cost-meter) ⭐139 — DeepSeek Harness 会话费用统计插件:本会话费用、当日费用、历史记录与官方价格同步（✅ 活跃）
- [dsh-gitbash-preset](https://github.com/liceses/dsh-gitbash-preset) ⭐136 — DeepSeek Harness 插件：一键安装「极简模式 (Git Bash)」agent preset —— 把 DSH 自带极简模式中的 bash 调用映射到 Git for Windows 的 bash（MSYS），让 Windows 上的极简模式真正可用。（✅ 活跃）
- [dsh-undo-savepoint](https://github.com/lire1131/dsh-undo-savepoint) ⭐134 — DSH crash-rescue plugin: undo config & plugin-code changes, secret-safe snapshots, one-click SAFE MODE, plus offline CLI/GUI that work even when DSH won't boot.（✅ 活跃）
- [DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) ⭐132 — 在 DSH Web GUI 中一键浏览、安装与更新全部 GitHub dsh-plugin 插件。（✅ 活跃）
- [dsh-noema](https://github.com/ZSeven-W/dsh-noema) ⭐128 — Noema long-term memory plugin for DSH: durable, inspectable agent memory with recall tools and a settings page.（✅ 活跃）
- [tokenledger](https://github.com/zh667/TokenLedger) ⭐126 — Token usage accounting for DeepSeek Harness, reconciled against New API and Sub2API relay-site billing（✅ 活跃）
- [dsh-auto-mode](https://github.com/NanmiCoder/dsh-auto-mode) ⭐115 — Safe automatic permissions for DeepSeek Harness.（✅ 活跃）
- [dsh-undo-plugin](https://github.com/lire1131/dsh-undo-plugin) ⭐108 — DSH plugin: snapshot & rollback your plugin/skin/settings configs. Auto-save on change, undo/redo stack, snapshot manager panel, keyboard shortcuts, plus an offline PowerShell CLI & GUI that work even when DSH won't boot.（✅ 活跃）
- [dsh-authinone](https://github.com/Stormycry-cryp/dsh-AuthInOne) ⭐105 — Self-contained DeepSeek Harness (DSH) plugin for Provider/Auth login, model switching, image fallback, token/cost analytics, and same-port Web restart. Useful? A star helps.（✅ 活跃）
- [dsh-usage-stats](https://github.com/Ychris12138/dsh-usage-stats) ⭐98 — Token usage heatmap, per-model breakdowns, and DeepSeek account balance for the DeepSeek Harness Web GUI (dsh web).（✅ 活跃）
- [dsh-reasoning-effort](https://github.com/HanaAyane/dsh-reasoning-effort) ⭐97 — DSH适用的Codex风格的思考强度滑块，以及大肥鱼跑步滑块。Codex-style model and reasoning-effort slider for DeepSeek Harness（✅ 活跃）
- [dsh-webui-market-plugin](https://github.com/Sanqi-normal/dsh-webui-market-plugin) ⭐96 — dsh Web GUI 社区插件市场：浏览 awesome-dsh-plugin.com 目录，一键安装/卸载到 profile。（✅ 活跃）
- [dsh-turn-rewind](https://github.com/Anionex/dsh-turn-rewind) ⭐94 — 对话与代码状态回退插件，基于持久化变更账本。（✅ 活跃）
- [dsh-plugin](https://github.com/Tabbit-Browser/dsh-plugin) ⭐91 — Tabbit Broser plugins for Deepseek Harness（✅ 活跃）
- [dsh-vision](https://github.com/oil-oil/dsh-vision) ⭐88 — Near-native image understanding for DeepSeek Harness（✅ 活跃）
- [dsh-annotation](https://github.com/omdsh-dev/dsh-annotation) ⭐87 — DSH Web 选中批注：选文字→批注→随消息发送，回复按批注逐条对照。（✅ 活跃）
- [dsh-chat-import](https://github.com/Nwflower/dsh-chat-import) ⭐87 — 从 Claude Code、Codex、ChatGPT、Cursor、Gemini、Reasonix、OpenCode 导入历史消息并在 DSH 中继续对话。（✅ 活跃）
- [dsh-commandcode-provider](https://github.com/Mars-Sea/dsh-commandcode-provider) ⭐83 — Unofficial DeepSeek Harness LLM provider plugin for Command Code: live model catalog, reasoning-effort support, Models-page card. Ported from pi-commandcode-provider (MIT).（✅ 活跃）
- [dsh-kun-like-pet](https://github.com/liyupi/dsh-kun-like-pet) ⭐80 — Kun Like 桌宠 —— DeepSeek Harness 桌面宠物插件：右下角小坤宠随 Agent 工作状态切换 9 种动作，任务完成播放「你干嘛~哎哟」（✅ 活跃）
- [dsh-notifier](https://github.com/THEWOLFWALKER/dsh-notifier) ⭐79 — Unified notification and remote-control plugin for DeepSeek Harness (DSH): one zero-dependency notify() API across 27 channels, with phone-friendly approvals/questions, six inbound control channels, and a loopback web console.（✅ 活跃）
- [dockyard-dsh](https://github.com/AITabby/dockyard-dsh) ⭐73 — A macOS-only native account-pool and provider plugin for DeepSeek Harness.（✅ 活跃）
- [dsh-dream-skin](https://github.com/RevolutionLA/dsh-dream-skin) ⭐73 — DSH Web 一键换肤插件：8 套原创主题、背景壁纸（透明度/模糊/渐变/URL）、每用户强调色、主题包导入导出与分享链接、收藏与随机，纯原生 token 系统。（✅ 活跃）
- [dsh-find-plugin](https://github.com/awesome-dsh-plugin/dsh-find-plugin) ⭐73 — 会话内插件发现：直接在 DSH 中搜索 GitHub dsh-plugin 主题的实时插件。（✅ 活跃）
- [dsh-notification](https://github.com/omdsh-dev/dsh-notification) ⭐70 — 回合完成桌面通知，按结果分控 + 关键词包含/排除过滤。（✅ 活跃）
- [dsh-stock-watch](https://github.com/Awu12277/dsh-stock-watch) ⭐68 — A股自选股实时行情盯盘插件 - DeepSeek Harness Web 右上角可折叠弹窗（✅ 活跃）
- [dsh-web-mobile](https://github.com/mexiaosqwq/dsh-web-mobile) ⭐68 — DSH Web UI 移动端适配：窄屏好用，宽屏适用（✅ 活跃）
- [dsh-permission-rules](https://github.com/PerryLink/dsh-permission-rules) ⭐65 — Claude Code-style declarative permission rules for DeepSeek Harness: ordered allow/deny/ask rules with tool-name, argument (glob/regex), and workspace-path matching on the tools/pre-execute waterfall, session-log audit, and HMR reload.（✅ 活跃）
- [dsh-plugin-hub](https://github.com/Noob-stupid/dsh-plugin-hub) ⭐64 — 插件管理面板：一键启停已装插件 + GitHub dsh-plugin 市场，带详情与一键安装。（✅ 活跃）
- [dsh-toy](https://github.com/c3ll256/dsh-toy) ⭐64 — Toy Control Protocol for DSH（✅ 活跃）
- [dsh-plugins-store](https://github.com/ZASENJC/dsh-plugins-store) ⭐62 — 自动收录与分类 GitHub dsh-plugin Topic 项目的静态目录网站。（✅ 活跃）
- [dsh-web-plugin-manager](https://github.com/LX2000WASD/dsh-web-plugin-manager) ⭐62 — Web UI 中一键管理 DSH 插件：查看、实时启停、安装/卸载、环境管理、插件市场。（✅ 活跃）
- [deepseek-harness-control-center](https://github.com/feibi-mochi/deepseek-harness-control-center) ⭐61 — DeepSeek Harness account monitoring, usage accounting, completion alerts, official recharge, flexible layout, and agent-assisted session controls. / 账户监控、提醒、充值与会话控制中心（✅ 活跃）
- [dsh-claude-ux](https://github.com/eri64/dsh-claude-ux) ⭐60 — DSH plugin: Claude-style Chinese risk control & conversation autonomy for DeepSeek Harness web（✅ 活跃）
- [dsh-memento](https://github.com/PerryLink/dsh-memento) ⭐59 — 有界分层、审批门控、可审计的跨会话记忆，支持冻结快照注入。（✅ 活跃）
- [dsh-balance-plugin](https://github.com/yxxbc/dsh-balance-plugin) ⭐57 — deepSeek 余额监控与用量统计（DSH 动态 Cordis 插件）：余额监控 · 官方充值入口 · 用量统计 · 三方插件管理（✅ 活跃）
- [dsh-open-in-vscode](https://github.com/omdsh-dev/dsh-open-in-vscode) ⭐53 — 从 Web GUI 直接在工作区中打开 VS Code 目录/文件。（✅ 活跃）
- [dsh-navbar](https://github.com/vlln/dsh-navbar) ⭐52 — DSH 插件：对话节点导航条（右缘节点串快速跳转 user 消息）。官方 bundle 插件，dsh plugin --profile web add 安装（✅ 活跃）
- [dsh-codex](https://github.com/Yan-Zero/dsh-codex) ⭐51 — Use your ChatGPT subscription in DeepSeek Harness through OpenAI's Codex sign-in flow（✅ 活跃）
- [deepseek-harness-skin](https://github.com/HeiGeAi/deepseek-harness-skin) ⭐49 — 换肤系统：21 套内置皮肤 + 一张图生成整套配色，构建期校验可读性。（✅ 活跃）
- [dsh-plugins](https://github.com/Ephemeral-AI-Lab/dsh-plugins) ⭐45 — Make Deepseek Harness Great（✅ 活跃）
- [dsh-smooth-stream](https://github.com/Laplace-bit/dsh-smooth-stream) ⭐45 — 丝滑流式渲染：字跟着模型到达走、换行滑入、不闪，滚动归用户，尊重 prefers-reduced-motion。（✅ 活跃）
- [dsh-status-rotator](https://github.com/01Virex/dsh-status-rotator) ⭐42 — 将 'Deep diving…' 状态替换为阶段感知的打字机消息。（✅ 活跃）
- [dsh-deepread](https://github.com/xiehuan123/dsh-deepread) ⭐41 — Evidence-first deep reading for AI agents — trace claims, evidence, confidence and knowledge maps across articles, books and PDFs.（✅ 活跃）
- [dsh-trace-compare](https://github.com/lamost423/dsh-trace-compare) ⭐41 — Trace Compare & Live Maze for DeepSeek Harness: visualize agent exploration (main path, detours, backtracks) from session logs or live sessions（✅ 活跃）
- [xgone/dsh-remote](https://github.com/xgone/dsh-remote) ⭐41 — 让 DeepSeek Harness 可以被安全地远程访问：账号密码认证 + MFA（TOTP）登录门禁、签名会话 Cookie、角色权限、浏览器内目录选择器、账号管理设置页。（🧪 实验性）
- [dsh-prompt-enhancer](https://github.com/Fishsb/dsh-prompt-enhancer) ⭐39 — DeepSeek Harness DSH 提示词增强插件：✨ 一键优化草稿，增强提示词。（✅ 活跃）
- [ui-status-label](https://github.com/alingalingling/ui-status-label) ⭐39 — 把鲸鱼娘思考时的 deep diving 状态自定义成任意文字。（✅ 活跃）
- [dsh-free-search](https://github.com/DDDMUC/dsh-free-search) ⭐38 — Free web search provider for DeepSeek Harness - DuckDuckGo backend, no API key needed（✅ 活跃）
- [dsh-plugin-mineru](https://github.com/HuanLinOTO/dsh-plugin-mineru) ⭐38 — 向模型暴露 MinerU 文档解析：PDF/图片/DOCX/PPTX/XLSX 转结构化 Markdown/JSON。（✅ 活跃）
- [dsh-expression](https://github.com/yyh-001/dsh-expression) ⭐36 — DeepSeek Harness 的表情包插件——找得到、发得出、学得会（✅ 活跃）
- [dsh-vision (william-jin-cmu)](https://github.com/william-jin-cmu/dsh-vision) ⭐36 — 视觉桥接：view_image 工具桥接任意 OpenAI 兼容 VLM，默认智谱免费档。（✅ 活跃）
- [dsh-message-edit](https://github.com/Moeblack/dsh-message-edit) ⭐35 — 分支式消息编辑、重掷、重试与版本时间线。（✅ 活跃）
- [dsh-codex-connect](https://github.com/franksong2702/dsh-codex-connect) ⭐34 — ChatGPT OAuth and Codex models for DeepSeek Harness.（✅ 活跃）
- [dsh-emoji](https://github.com/hellodigua/dsh-emoji) ⭐34 — 让 AI 回复加入自定义表情。（✅ 活跃）
- [dsh-omi-voice](https://github.com/PolinniZhong/dsh-omi-voice) ⭐34 — 沉浸式听朗读插件：对话内点读/暂停/继续，豆包 TTS 自然音色（BYOK），只读最终回答并过滤代码/表格/图形。（✅ 活跃）
- [billion-context-dsh](https://github.com/Tyan66666/billion-context-dsh) ⭐33 — 模型驱动的上下文管理（Active Context Pruning）：由模型决定何时压缩、压缩什么。（✅ 活跃）
- [dsh-mneme](https://github.com/modusensus/dsh-mneme) ⭐31 — 记忆主权归用户的本地跨会话记忆：SQLite + 可人工编辑的 Markdown 镜像，autoDream 后台巩固。（✅ 活跃）
- [dsh-remote](https://github.com/flymysql/dsh-remote) ⭐31 — 远程工作区：SSH 连接远程主机，用 rw_pick_workspace/rw_read_file/rw_exec 等工具远程操作。（✅ 活跃）
- [dsh-remote](https://github.com/Blank-not-black/dsh-Remote) ⭐31 — DSH Remote · 口袋里的 DSH 控制台 会话 · 审批 · 提问 · 文件传输，局域网 / Tailscale 直连 多服务器自动选优，聊天记录离线可看 带 Token 鉴权，数据只在你的设备之间流动 Sessions · approvals · questions · file transfer over LAN / Tailscale. Automatic fastest-server selection. Chat history available offline. Token-authenticated — your data flows only between your devices.（✅ 活跃）
- [dsh-whale-report](https://github.com/SenmuuuuW/dsh-whale-report) ⭐31 — 深迹 DeepTrace — Your Agent, in numbers. DSH 插件：从会话事件日志生成日报/周报/月报/年报/自定义区间，确定性洞察与协作复盘，只读、不改写历史。（✅ 活跃）
- [deepseek-harness-workbench-plugin](https://github.com/loadingvx/deepseek-harness-workbench-plugin) ⭐29 — Deepseek-harness-workbench-plugin（✅ 活跃）
- [dsh-full-remote](https://github.com/JUANWANG-BUAA/dsh-full-remote) ⭐29 — Auditable, token-gated DeepSeek Harness remote gateway: mobile QR access, per-device sessions, Host/Origin rewrite, settings/credentials/directory support.（✅ 活跃）
- [dsh-share](https://github.com/hellodigua/dsh-share) ⭐29 — DSH 对话一键分享。（✅ 活跃）
- [dsh-ui-whale](https://github.com/lhh010/dsh-ui-whale) ⭐29 — 会话标题栏全手绘像素鲸鱼伙伴：眨眼、摆尾、回合完成喷水，零核心改动。（✅ 活跃）
- [dsh-web-search-pro](https://github.com/anweat/dsh-web-search-pro) ⭐29 — 多引擎持久搜索：DeepSeek/Exa/DDG/Bing/Jina + GitHub/B站/YouTube/V2EX/小红书/推特/Reddit/RSS，SQLite+LRU 缓存 + Playwright 渲染。（✅ 活跃）
- [ego-browser](https://github.com/Fisfzy/ego-browser) ⭐29 — 把 ego-lite 智能体浏览器（为 AI Agent 打造的 Chromium）接入 DSH，13 个结构化工具。（✅ 活跃）
- [deepseek-harness-snowsalt](https://github.com/KYZHXL/deepseek-harness-snowsalt) ⭐28 — 雪盐主题皮肤。（✅ 活跃）
- [dsh-files](https://github.com/taxueseek/dsh-files) ⭐28 — DeepSeek Harness dual-face plugin: session-isolated file upload with colorful composer cards + read_document tool (text/PDF/DOCX/XLSX) with content sniffing and LRU caching（✅ 活跃）
- [dsh-openmaic](https://github.com/THU-MAIC/dsh-openmaic) ⭐28 — OpenMAIC for DeepSeek Harness: classrooms, slides, interactive widgets, and Socratic teaching（✅ 活跃）
- [dsh-plugin-guard](https://github.com/lxzy-7/dsh-plugin-guard) ⭐28 — Install safety net for DeepSeek Harness: pre-install snapshots, one-click/automatic rollback, guarded boot, and incident reports that auto-trigger agent analysis. 中文: DeepSeek Harness 插件安装安全网（安装前自动快照、一键/自动回退、守护启动、事故报告自动触发 Agent 分析）。（✅ 活跃）
- [dsh-plugin-check](https://github.com/omdsh-dev/dsh-plugin-check) ⭐27 — 插件健康检查：清单协议、patch 格式、构建陷阱与 hub 收录状态，零依赖只读。（✅ 活跃）
- [dsh-codex-subscription](https://github.com/WSL043/dsh-codex-subscription) ⭐26 — ChatGPT/Codex subscription provider for DeepSeek Harness with OAuth, models, quota, search, and image tools—no API key or Codex CLI.（✅ 活跃）
- [dsh-computer-use](https://github.com/Anionex/dsh-computer-use) ⭐26 — 为 DeepSeek Harness 提供电脑控制插件：新鲜 Accessibility 观测、过期状态拒绝、作用域权限与安全输入（目前支持macos）｜Accessibility-first macOS Computer Use bundle for DSH with fresh observations, stale-state rejection, scoped permissions, and safe input.（✅ 活跃）
- [dsh-quant](https://github.com/pengpengyi92/dsh-quant) ⭐26 — "🐳 Dsh-Quant: The Everything-Plugin Ai native Quant OS "（✅ 活跃）
- [dsh-theme-cyberpunk2077](https://github.com/Tommy00748/dsh-theme-cyberpunk2077) ⭐26 — Cyberpunk 2077 / Night City theme for the DeepSeek Harness Web UI — CRT scanlines, Kiroshi lock-on, typewriter SFX, Relic glitch & easter eggs（✅ 活跃）
- [dsh-web-lan-access](https://github.com/AcidGr/dsh-web-lan-access) ⭐26 — DeepSeek Harness (dsh) Web plugin（✅ 活跃）
- [dsh-auto-memory](https://github.com/Aik358/dsh-auto-memory) ⭐25 — DSH 自动记忆插件:三层记忆(用户级/项目笔记/每日日志)自动注入与检索、每日反思、可视化面板与设置页,支持继承其他 AI 工具的历史记忆。An auto-memory plugin for the DeepSeek Harness Web GUI: three-layer memory (user-level / project notes / daily logs) with automatic injection and retrieval, daily reflections, a visual panel and settings page, and inheritance of memories from other AI tools.（✅ 活跃）
- [dsh-maid-whale-webui](https://github.com/yunxiiQwQ/dsh-maid-whale-webUI) ⭐25 — DeepSeek Harness Web UI 鲸鱼女仆主题插件（✅ 活跃）
- [dsh-minigames](https://github.com/lhh010/dsh-minigames) ⭐25 — DSH Web UI 右侧小游戏面板：18 款离线小游戏（恐龙跳一跳 / 俄罗斯方块 / 坦克大战 / 扫雷 / 2048 / 数独 / 吃豆人 / 跟枪练习等），可扩展游戏注册表，等待模型回复或修 bug 时的摸鱼神器（✅ 活跃）
- [dsh-plugin-workshop](https://github.com/yyyyukari/dsh-plugin-workshop) ⭐25 — Steam 创意工坊风格插件浏览器：零服务器、GitHub 驱动搜索、一键安装。（✅ 活跃）
- [dsh-scholar](https://github.com/lzszq/dsh-scholar) ⭐25 — dsh-scholar（✅ 活跃）
- [dsh-win32](https://github.com/sjh9714/dsh-win32) ⭐25 — Fix and diagnose DeepSeek Harness on native Windows. Official PowerShell, Workspace Write, shortcuts, and legacy preset repair. No WSL.（✅ 活跃）
- [dsh-custom-tool](https://github.com/omdsh-dev/dsh-custom-tool) ⭐24 — 用 Monaco 编辑器创建和管理 DSH 沙箱化 JavaScript 工具，模型驱动工具列表。（✅ 活跃）
- [dsh-diff-viewer](https://github.com/lehhair/dsh-diff-viewer) ⭐24 — PiUI 风格 Web diff 查看器，替代默认 diff 视图。（✅ 活跃）
- [dsh-qq2006](https://github.com/LaplaceYoung/dsh-qq2006) ⭐24 — DSH (DeepSeek Harness) 的 QQ2006 皮肤插件：注册 qq2006 主题、镜像 body[data-ds-skin]、全局皮肤表与完整素材（✅ 活跃）
- [dsh-recall-plugin](https://github.com/limbo947/dsh-recall-plugin) ⭐24 — DSH 消息撤回插件：回到发送该消息时的状态 DSH Message Recall Plugin: Return to the state when the message was sent（✅ 活跃）
- [dsh-toolkit](https://github.com/omdsh-dev/dsh-toolkit) ⭐24 — 零依赖工具包：计算器、CSV、diff、编码、JSON、Markdown、正则、时间。（✅ 活跃）
- [dsh-balance](https://github.com/crazywoola/dsh-balance) ⭐23 — 设置页余额插件。（✅ 活跃）
- [dsh-plugin-better-sidebar-plugin-office](https://github.com/HuanLinOTO/dsh-plugin-better-sidebar-plugin-office) ⭐23 — 为 better-sidebar 提供 Office 三件套预览（.docx/.xlsx/.pptx），独立瘦身 bundle。（✅ 活跃）
- [dsh-xiaoyao-skins](https://github.com/147228/dsh-xiaoyao-skins) ⭐23 — 夕小瑶 × DeepSeek Harness Web 皮肤合集、安装器与社区创作工具链（✅ 活跃）
- [dsh-catppuccin-theme](https://github.com/NoNameLeGo/dsh-catppuccin-theme) ⭐22 — DeepSeek Harness Web GUI 的 Catppuccin 主题插件：Latte / Frappé / Macchiato / Mocha 四种主题一键切换，内置可开关的玻璃质感（Glassmorphism）（✅ 活跃）
- [dsh-focus-chat](https://github.com/dingyi222666/dsh-focus-chat) ⭐21 — 为 dsh 提供新的「聚焦会话」精简会话视图，更轻松易于阅读，只关注最终产出结果。（✅ 活跃）
- [dsh-plugin-pet-rs](https://github.com/HuanLinOTO/dsh-plugin-pet-rs) ⭐21 — Rust 桌宠：5 态鲸鱼 + 双 SSE 实时推送 + 透明置顶窗 + 系统托盘，三端支持。（✅ 活跃）
- [dsh-solo-thinking](https://github.com/fredalxin/dsh-solo-thinking) ⭐21 — Solo-style isolated brainstorm branches and Handoffs for DeepSeek Harness（✅ 活跃）
- [dsh-stickers](https://github.com/william-jin-cmu/dsh-stickers) ⭐21 — DSH WebUI sticker plugin for bidirectional user and agent reactions（✅ 活跃）
- [dsh-web-ui-notify](https://github.com/bill9109/dsh-web-ui-notify) ⭐21 — 为 DSH 增加桌面通知提醒。（✅ 活跃）
- [dsh-any-background](https://github.com/Tkingxiao/dsh-any-background) ⭐20 — Deepseek Harness 自定义主题插件，支持自定义图片/视频壁纸，对话框，侧边栏等透明度模糊度调整，全局主题色的色轮调整插件（✅ 活跃）
- [dsh-clawrouter](https://github.com/BlockRunAI/dsh-clawrouter) ⭐20 — A safety gate for DeepSeek Harness: a stronger model reviews dangerous tool calls before they run. Plus vision and BlockRun's full model catalog from one wallet, paid per request over x402.（✅ 活跃）
- [dsh-drag-and-drop](https://github.com/bill9109/dsh-drag-and-drop) ⭐20 — DSH Web UI 跨平台文件拖拽与原始路径插入，无需复制文件。（✅ 活跃）
- [dsh-file-upload](https://github.com/HongMing-Huang/dsh-file-upload) ⭐20 — DeepSeek Harness (dsh) file-message plugin: Claude-style drag-and-drop / paperclip upload, content sniffing, document-to-Markdown via Microsoft MarkItDown (with built-in JS fallback), text inlining, read_document tool for agents.（✅ 活跃）
- [dsh-llm-fallbacks](https://github.com/omdsh-dev/dsh-llm-fallbacks) ⭐20 — An dsh plugin for role-based LLM retry&fallback strategy. 基于角色的模型重试备用策略插件（✅ 活跃）
- [dsh-agy](https://github.com/chaos-03x/dsh-agy) ⭐19 — Google Antigravity (agy) OAuth auth + model access plugin for DeepSeek Harness: multi-account pool, 429 rotation, device fingerprinting, CLI and web login.（✅ 活跃）
- [dsh-balance-meter](https://github.com/Ghost011118/dsh-balance-meter) ⭐19 — DeepSeek account balance and session cost readout for the DeepSeek Harness Web GUI（✅ 活跃）
- [dsh-better-edit](https://github.com/Rianico/dsh-better-edit) ⭐19 — Hash-anchored read/edit/undo_last_edit tools for DeepSeek Harness (dsh), fewer token consumption, lower cost.（✅ 活跃）
- [dsh-skin](https://github.com/KinGao294/dsh-skin) ⭐19 — Codex 风格皮肤切换器 + 自定义半透明壁纸，支持透明度/模糊控制。（✅ 活跃）
- [dsh-theme-plugin](https://github.com/nevertoday/dsh-theme-plugin) ⭐19 — Chinese traditional colors as a DeepSeek Harness theme pack.（✅ 活跃）
- [dsh-user-experience](https://github.com/DietCokewithSugar/dsh-user-experience) ⭐19 — Persona-driven UX walkthrough plugin for DeepSeek Harness (DSH) - scans React + TypeScript source code for UX issues, pinpoints them, and suggests fixes.（✅ 活跃）
- [dsh-whale-galgame](https://github.com/JAdpp/dsh-whale-galgame) ⭐19 — 工作推gal两不误~面向DeepSeek Harness的跨会话事件感知Galgame引擎与界面插件，支持鲸鱼娘/GPT/Claude/Grok/Gemini/Kimi多位模型娘角色（✅ 活跃）
- [compass](https://github.com/dshakes/compass) ⭐18 — 🧭 Let your coding agent off the leash — not off the rails. Guardrails, a hard budget cap & a self-fixing PR loop for Claude Code / Codex / Gemini. Eval-gated 100/100, you always merge.（✅ 活跃）
- [dsh-milestone](https://github.com/SnowCrescenter-tech/dsh-milestone) ⭐18 — Git 风格里程碑时间线：悬停查看元数据，点击跳转任意消息。（✅ 活跃）
- [dsh-outline](https://github.com/urzeye/dsh-outline) ⭐18 — DeepSeek Harness（DSH）Web GUI 的实时大纲插件，移植自 Ophel Atlas（✅ 活跃）
- [dsh-provider-model-configurator](https://github.com/LiangYin233/dsh-provider-model-configurator) ⭐18 — DSH 模型 Pro:为 DSH WebUI 提供将 pi-ai 预设或任意已配置提供商的模型上下文、输出上限、推理档位与兼容开关一键应用到目标提供商,并集中查看、新建、编辑、复制与删除各提供商模型条目的能力。（✅ 活跃）
- [dsh-recommend](https://github.com/zp-home/dsh-recommend) ⭐18 — 透明插件排行榜与推荐：每日自动抓取 dsh-plugin 主题数据，开放评分模型。（✅ 活跃）
- [touhou-hakurei](https://github.com/xiake595/touhou-hakurei) ⭐18 — 灵梦（Reimu）·博丽神社（东方Project）美化版皮肤：神社昼夜实景背景、灵梦立绘、画框侧边栏与输入框、纸白透明界面 — DeepSeek Harness Web GUI skin（✅ 活跃）
- [webdsh](https://github.com/futrime/webdsh) ⭐18 — Running DeepSeek Harness on web（✅ 活跃）
- [DeepSeek-Harness-Web-Tools](https://github.com/tonyd2wild/DeepSeek-Harness-Web-Tools) ⭐17 — 免费免密钥的 web_search/web_fetch，DuckDuckGo 驱动，无需注册。（✅ 活跃）
- [dsh-computer-use](https://github.com/988hj7tczd-oss/dsh-computer-use) ⭐17 — Computer Use 插件：虚拟鼠标真人操作 for DeepSeek Harness（screen_observe + computer_click 等 11 个模型友好工具，跨平台 cua-driver 引擎）（✅ 活跃）
- [dsh-context-doctor](https://github.com/Zhenyu98/dsh-context-doctor) ⭐17 — 上下文注入审计插件：统计 AGENTS.md 指令链/技能目录/工具 schema 的 token 成本，检测重复与冲突。（✅ 活跃）
- [dsh-group-photo](https://github.com/SenmuuuuW/dsh-group-photo) ⭐17 — DSH 内测收官合影墙：GitHub OAuth 零权限登录 + 冻结白名单校验的拍立得合影站（含 DSH Skill 包装）（✅ 活跃）
- [dsh-gui-customization](https://github.com/LAN-TINA-WS/dsh-gui-customization) ⭐17 — DeepSeek Harness 时装工坊：给 DSH 界面换装——更改主题配色/自定义背景图/自定义视频背景/可调节氛围灯，中英双语 ·DSH Web UI 时装工坊。（✅ 活跃）
- [dsh-passwords](https://github.com/slywalker2006/dsh-passwords) ⭐17 — dsh-passwords: DeepSeek Harness login gateway - first-run setup, at-rest encryption, brute-force lockout, audit log, HTTPS（✅ 活跃）
- [dsh-plugin-writing-guard](https://github.com/xmutfyh/dsh-plugin-writing-guard) ⭐17 — DeepSeek Harness (DSH) academic writing guard for papers — 论文去AI味 / AI-writing style detection, evidence preservation, journal-fit calibration, manuscript proofreading, writing_audit & automatic checks. Local, zero network, zero LLM.（✅ 活跃）
- [dsh-advisor](https://github.com/omdsh-dev/dsh-advisor) ⭐16 — Advisor - Pair a second model that passively reviews each turn and injects notes.  搭配一个会在每轮对话被动注入见解和审查的副模型。（✅ 活跃）
- [dsh-continual-evolve](https://github.com/ZK-Andy/dsh-continual-evolve) ⭐16 — Continual self-evolution plugin for DeepSeek Harness: versioned, auditable, rollback-safe harness state refined from session trajectories, with a benchmark-driven validation loop.（✅ 活跃）
- [dsh-session-notification](https://github.com/dingyi222666/dsh-session-notification) ⭐16 — 提供会话完成等四种状态的通知响应，支持浏览器提示和提示词（✅ 活跃）
- [dsh-side-panel](https://github.com/ccq1/dsh-side-panel) ⭐16 — 紧凑侧边栏：文件浏览器、终端与 Git 审查。（💤 停更）
- [dsh-codex-oauth](https://github.com/WNJXYK/dsh-codex-oauth) ⭐15 — Use your OpenAI subscription with DeepSeek Harness to access GPT models, image generation, and web search.（✅ 活跃）
- [dsh-md-notes](https://github.com/XieZongChen/dsh-md-notes) ⭐15 — A note-taking plugin for DeepSeek Harness (DSH). It provides a full MD notes manager and MD notes editor, letting you quickly capture conversation content into notes. Notes can be maintained by syncing to a Git repository（✅ 活跃）
- [dsh-sentinel](https://github.com/fuhefei/dsh-sentinel) ⭐15 — Condition-driven wakeup for DeepSeek Harness: durable file/command/http/process/webhook watches that wake the agent, with dock, sidebar branch, and a global dashboard.（✅ 活跃）
- [dsh-stock-market](https://github.com/AnacondaKC/dsh-stock-market) ⭐15 — 股票行情插件（整活：有效解决了写代码时账户不能同时亏钱的 BUG）。（✅ 活跃）
- [dsh-web-review](https://github.com/CanglongCl/dsh-web-review) ⭐15 — DeepSeek Harness Web GUI 的网页预览与元素批注插件，让 AI 根据可视化反馈直接修改前端源码。（✅ 活跃）
- [deepseek-harness-zh_pro](https://github.com/magian1127/deepseek-harness-zh_pro) ⭐14 — Chinese enhancement plugin for DeepSeek Harness (DSH) - DSH 中文增强插件（✅ 活跃）
- [dsh-ai4scholar](https://github.com/literaf/dsh-ai4scholar) ⭐14 — AI4Scholar for DeepSeek Harness (dsh): 38 native academic tools — Semantic Scholar, PubMed, Google Scholar, arXiv, bioRxiv/medRxiv, DOI, full text, auto-cite, figures, unified search. Powered by ai4scholar.net（✅ 活跃）
- [dsh-gomoku](https://github.com/omdsh-dev/dsh-gomoku) ⭐14 — 在 DSH 中与 AI 下五子棋，也可以让 AI 对局比试模型强弱。（✅ 活跃）
- [dsh-live2d-pets](https://github.com/cyanfish-x/dsh-live2d-pets) ⭐14 — Live2D 桌宠插件 for DeepSeek Harness：Agent 状态镜像 + 互动陪伴，内置宽松许可预设模型 / Live2D pet plugin: agent state mirror + interactive companion with curated permissive-license presets（✅ 活跃）
- [dsh-plugin](https://github.com/loongsuite/dsh-plugin) ⭐14 — OpenTelemetry tracing for DeepSeek Harness (dsh): turns each agent turn into a GenAI span tree — steps, LLM calls with TTFT, tool executions, token usage — exported over standard OTLP to Jaeger, Grafana Tempo, SigNoz, Langfuse, or any compatible backend.（✅ 活跃）
- [dsh-codex-auth](https://github.com/suntianc/dsh-codex-auth) ⭐13 — DeepSeek Harness plugin that reuses the local Codex CLI ChatGPT login and adds a native GPT Auth settings card（✅ 活跃）
- [dsh-compaction-instant](https://github.com/TsFreddie/dsh-compaction-instant) ⭐13 — LLM-free lossless* compaction engine for DeepSeek Harness（✅ 活跃）
- [dsh-deepcel](https://github.com/Small-tailqwq/dsh-deepcel) ⭐13 — Excel 风格电子表格皮肤。（✅ 活跃）
- [dsh-nested-followups](https://github.com/sluminositys/dsh-nested-followups) ⭐13 — Ask a follow-up on any past answer in an isolated branch, keeping your main conversation clean. 针对任意历史回答发起追问，新问题在独立分支中展开，主对话保持干净。A conversation-tree plugin for DeepSeek Harness / DeepSeek Harness 会话树插件。（✅ 活跃）
- [dsh-opencode-go-usage](https://github.com/Xenia0922/dsh-opencode-go-usage) ⭐13 — DeepSeek Harness 插件:OpenCode Go 用量与花费悬浮仪表盘(配额、逐请求成本、模型/来源分布)（✅ 活跃）
- [dsh-pet](https://github.com/FlytoMAYDAY80/dsh-pet) ⭐13 — 🐋 DSH 有声桌宠：悬浮桌面的 DeepSeek 小鲸鱼，不打开 DSH 也能实时感知会话状态（需要确认/工作中/完成/空闲/离线），支持音效提醒与零代码定制素材（✅ 活跃）
- [dsh-plugin-aigc-canvas](https://github.com/HuanLinOTO/dsh-plugin-aigc-canvas) ⭐13 — provider-agnostic AIGC HTTP 桥 + 无限画布 + ffmpeg 后处理，13 个工具含画布连边/reroll/媒体编辑 | Provider-agnostic AIGC HTTP bridge + infinite canvas + ffmpeg post-processing; 13 tools incl. canvas linking/reroll/media-edit（✅ 活跃）
- [dsh-security-audit](https://github.com/omdsh-dev/dsh-security-audit) ⭐13 — DSH 本机安全审计插件：配置/插件来源/会话/网络暴露面，只读脱敏风险报告（✅ 活跃）
- [dsh-token-usage](https://github.com/LeemanCheung/dsh-token-usage) ⭐13 — Persistent token usage records and dashboard for DeepSeek Harness（✅ 活跃）
- [dsh-update-checker](https://github.com/Airmetro/dsh-update-checker) ⭐13 — DeepSeek Harness 主程序与插件更新管理：npm/GitHub 双源 semver 比对、多语言横幅、一键更新（主程序自动备份/校验/回滚，插件临时目录安装）、更新后看门狗重启。Update management for DeepSeek Harness and its plugins: dual-source semver checks, locale banner, one-click updates with backup/rollback, watchdog restart.（✅ 活跃）
- [dsh-vision-opencode](https://github.com/poiuyjie/dsh-vision-opencode) ⭐13 — DSH plugin: Auto-convert images to text for pure-text LLMs (DeepSeek etc.) via any vision model. No need to switch your main model.（✅ 活跃）
- [DeepSeek-Harness-Vision-Tools](https://github.com/tonyd2wild/DeepSeek-Harness-Vision-Tools) ⭐12 — 视觉代理：任意文本模型 + 任意视觉模型即可让 DSH 看图。（✅ 活跃）
- [dsh-cyber-particle](https://github.com/AKS1st/dsh-cyber-particle) ⭐12 — 为 DeepSeek Harness Web 界面添加动态粒子网络背景 | Particle-network background plugin for DeepSeek Harness web（✅ 活跃）
- [dsh-eval-harness](https://github.com/BiBoyang/dsh-eval-harness) ⭐12 — DSH 插件评测工具：YAML 用例驱动真实 agent 回归评测 + baseline 对比 PASS/WARN/FAIL 门禁｜Regression eval harness for DeepSeek Harness plugins（✅ 活跃）
- [dsh-evolve](https://github.com/william-jin-cmu/dsh-evolve) ⭐12 — 自进化插件：agent 在 session 内随对话给自己长出/剪掉能力 —— evolve_add 热挂载持久化 cordis 插件（下一 step 工具即可见），evolve_remove 可逆卸载，重启自动恢复（✅ 活跃）
- [dsh-openai-codex-auth](https://github.com/yoke233/dsh-openai-codex-auth) ⭐12 — OpenAI Codex OAuth login and usage card plugin for DeepSeek Harness（✅ 活跃）
- [dsh-side-chat](https://github.com/heartmove/dsh-side-chat) ⭐12 — 一个 DSH 网页插件，Codex 式侧边聊天的强化版本： 在右侧面板提供按主会话隔离的独立聊天，具备 Codex 式的智能体能力——继承主会话的 工具集、模型、思考难度与权限预设，能感知所在工作目录；选中对话内容即可提问，AI 回复 也能带回主会话（直接带回或摘要后带回，写入草稿或注入为折叠提示行）。  在 Codex 式能力之上，它额外支持：当主会话的智能体弹出问题弹框向你提问时，可以 把问题与各个选项带入侧边聊天、让 AI 帮你分析，不必打断当前流程——想清楚后把答案 带回，再回答弹框即可。（✅ 活跃）
- [dsh-surfing-plugin](https://github.com/cyijun/dsh-surfing-plugin) ⭐12 — SearXNG search and Crawl4AI fetch providers for DeepSeek Harness（✅ 活跃）
- [dsh-trading](https://github.com/maddogfinance/dsh-trading) ⭐12 — 纯研究型交易工作台插件：类型化行情数据缝（自带 provider）、多周期指标快照、带溯源门控标注的交互图表卡片，以及拒绝执行型工具调用的风险护栏——架构上不提供执行能力。（✅ 活跃）
- [weshop-dsh-plugin](https://github.com/weshopai/weshop-dsh-plugin) ⭐12 — Native WeShop Cordis plugin for DeepSeek Harness. Allow you to use infinite canvas with infinite creative skills.（✅ 活跃）
- [dsh-balance](https://github.com/TwotwoPiggy/dsh-balance) ⭐11 — dsh余额插件. A DeepSeek Harness plugin for real-time token tracking and highly accurate session cost estimation, featuring dynamic peak/off-peak pricing support.（✅ 活跃）
- [dsh-chat-imagine](https://github.com/corrinehu/dsh-chat-imagine) ⭐11 — 在 DSH 聊天窗口自动调用生图工具（API 渠道，或本机 CLI：已支持mmx / codex / agy）并展示图片，也支持利用对应 CLI 识别图片。（✅ 活跃）
- [dsh-client-ui-skins](https://github.com/caoyiwei850/dsh-client-ui-skins) ⭐11 — DSH Web skin plugin with built-in themes and custom image skins（✅ 活跃）
- [dsh-expert-mode](https://github.com/Asher-2000/dsh-expert-mode) ⭐11 — DSH (DeepSeek Harness) 专家模式 agent preset — 首席协调官 + 17位领域专家子代理 Expert-mode preset for DeepSeek Harness（✅ 活跃）
- [dsh-file-mentions](https://github.com/a903067276-rgb/dsh-file-mentions) ⭐11 — 回复中文件路径可点击：内联打开、文件管理器揭示、提及文件芯片列表。（✅ 活跃）
- [dsh-file-mount](https://github.com/acefun29/dsh-file-mount) ⭐11 — 增量文件挂载 + 行区间去重：相同文件内容不再重复发送给模型。（✅ 活跃）
- [dsh-lsp-actions](https://github.com/PerryLink/dsh-lsp-actions) ⭐11 — LSP action surface for DeepSeek Harness: diagnostics, formatting, completion, code actions, symbols, signature help, inlay hints, and rename tools over language servers（✅ 活跃）
- [dsh-mermaid](https://github.com/AKS1st/dsh-mermaid) ⭐11 — 在 DSH Web 会话中把 Mermaid 代码围栏渲染为 SVG 图表 | Render Mermaid code fences as SVG diagrams in DSH Web messages（✅ 活跃）
- [dsh-plugin-integration](https://github.com/MutaLucem/dsh-plugin-integration) ⭐11 — DeepSeek Harness (DSH) 插件整合中心：动态发现、打标分类、重叠/兼容检测、一键启停与失效检测（✅ 活跃）
- [dsh-plugin-ya-workspace-sidebar](https://github.com/HuanLinOTO/dsh-plugin-ya-workspace-sidebar) ⭐11 — DSH Web 工作区侧栏替代，顶部全局最近会话 + Workspace→Session 二级菜单 + 面包屑 | DSH Web workspace sidebar replacement: top global recent sessions + Workspace→Session two-level menu + breadcrumbs（✅ 活跃）
- [dsh-ramify](https://github.com/yanglongyun/ramify-dsh) ⭐11 — Ramify 是 DeepSeek Harness 的创意分支画布插件，用树状工作区生成、对比和迭代多个可交互方案。（✅ 活跃）
- [dsh-sdk-platform-rs](https://github.com/kpn-dsh/dsh-sdk-platform-rs) ⭐11 — A Rust SDK to interact with the DSH Platform. This library provides convenient building blocks for services that need to connect to DSH Kafka, fetch tokens for various protocols, manage Prometheus metrics, and more.（✅ 活跃）
- [dsh-sticky-note](https://github.com/Meredith2328/dsh-sticky-note) ⭐11 — 左下角便签：随手记点子/感想/TODO，实时保存到归档目录，清单+悬浮归档（✅ 活跃）
- [oh-my-dsh](https://github.com/NoWint/Oh-My-DSH) ⭐11 — 🐋 Oh-My-DSH — DeepSeek Harness Plugin Ecosystem【每一小时更新】（✅ 活跃）
- [context-vista](https://github.com/GooodWei/context-vista) ⭐10 — 上下文/Token 实时监控：悬浮面板 + /context 命令，环形图展示用量、分配与估算费用。（✅ 活跃）
- [dsh-balance-monitor](https://github.com/jelly-000/dsh-balance-monitor) ⭐10 — Multi-provider AI balance, quota, and token usage for the dsh sidebar, with a daily heatmap.（✅ 活跃）
- [dsh-latex-tools](https://github.com/liuup/dsh-latex-tools) ⭐10 — ♾️ Copy and export the LaTeX in DeepSeek Harness 悬停任意 LaTeX 公式即可复制 TeX 源码或导出为独立的 SVG 文件（✅ 活跃）
- [dsh-plugin-anti-ads](https://github.com/HuanLinOTO/dsh-plugin-anti-ads) ⭐10 — DSH Web 广告拦截器，四层独立防御拦截 dsh-ads 插件的所有广告位 | DSH Web ad blocker with four independent defense layers targeting the dsh-ads plugin（✅ 活跃）
- [dsh-ui-appearance](https://github.com/TQSY114514/dsh-ui-appearance) ⭐10 — Appearance customization plugin for DeepSeek Harness: theme color palette, background image, opacity/blur, glass effect（✅ 活跃）
- [dsh-usage-chart](https://github.com/Max-Samson/dsh-usage-chart) ⭐10 — A DeepSeek Harness Web plugin for real-time Token usage, cost estimates, per-round charts, and DeepSeek API balance.（✅ 活跃）
- [dsh-web-billing](https://github.com/bpc-oss/dsh-web-billing) ⭐10 — DSH Web 中英文金额 Token 计费：官方策略自动定价（含高峰/低谷），逐条消息费用台账。（✅ 活跃）
- [DeepSeek-Harness-billing-plugin](https://github.com/WilliamLIiii/DeepSeek-Harness-billing-plugin) ⭐9 — 账户余额 + 按模型剩余任务估算，带会话费用台账。（✅ 活跃）
- [dsh-awiki](https://github.com/AgentConnect/dsh-awiki) ⭐9 — AWiki identity and messaging plugin for DeepSeek Harness（✅ 活跃）
- [dsh-bash-win](https://github.com/zimzaza4/dsh-bash-win) ⭐9 — 在 Windows 环境中为 DeepSeek Harness 提供 Git Bash 与 WSL 2 bash 工具,含 bwrap 沙箱、审批模式、后台任务（✅ 活跃）
- [dsh-client-ui-skin-claude](https://github.com/PAKIKNOWLEDGE/dsh-client-ui-skin-claude) ⭐9 — Claude-style skin for DeepSeek Harness (dsh) Web GUI — warm-black canvas, Anthropic clay accent, serif UI（✅ 活跃）
- [dsh-explorer](https://github.com/No-PRM/dsh-explorer) ⭐9 — DSH plugin: VS Code-style file-tree explorer (git decorations, preview, diff, drag-to-reference); install via dsh plugin --profile web add.（✅ 活跃）
- [dsh-hud](https://github.com/a903067276-rgb/dsh-hud) ⭐9 — HUD 状态面板：浮动侧栏展示 git 状态、MCP 服务器、技能、模型与 token 用量。（✅ 活跃）
- [dsh-paste-input](https://github.com/lhh010/dsh-paste-input) ⭐9 — DSH WebUI 文件输入增强：Ctrl+V 粘贴、拖拽、选择文件，发送时复制进会话工作区。（✅ 活跃）
- [dsh-plugin-auto-blame](https://github.com/HuanLinOTO/dsh-plugin-auto-blame) ⭐9 — 模型回合结束后用 LLM 生成 3 条批判性跟进建议，点击即发送 | After a model turn, an LLM generates 3 critical follow-up suggestions shown as click-to-send chips（✅ 活跃）
- [dsh-plugin-interpreters](https://github.com/HuanLinOTO/dsh-plugin-interpreters) ⭐9 — 暴露 run_python/run_node 工具，通过 stdin 执行代码返回 stdout/stderr/exit。（✅ 活跃）
- [dsh-plugin-smooth-stream](https://github.com/SpookySandwich/dsh-plugin-smooth-stream) ⭐9 — DSH 流式渲染插件：按段落分批呈现、8 种入场动画、平滑滚动、设置面板。DeepSeek Harness: paragraph-batched streaming reveals, 8 designed animations, smooth scroll-follow and a settings panel.（✅ 活跃）
- [dsh-spotlight](https://github.com/0xsline/dsh-spotlight) ⭐9 — DSH Web 键盘优先命令面板。（✅ 活跃）
- [dsh-web-archive](https://github.com/renat3u/dsh-web-archive) ⭐9 — 折叠对话当中众多的“无用消息”，例如Think、Bash等（✅ 活跃）
- [dsh-webui-auth](https://github.com/Yuuz12/dsh-webui-auth) ⭐9 — WebUI 身份认证：HTTP/传输层强制登录（资源、插件 bundle、/api、WebSocket 四层防护），服务端会话 + HttpOnly Cookie。（✅ 活跃）
- [deepseek-harness-SupportVisionModel](https://github.com/TryDing-T/deepseek-harness-SupportVisionModel) ⭐8 — 基于 deepseek-harness 二次开发：支持单独配置视觉模型读图。（✅ 活跃）
- [dsh-api-balance](https://github.com/02Muller25/dsh-api-balance) ⭐8 — 安装在deepseek的插件，能够实时显示当前api的余额，30秒自动刷新一次（✅ 活跃）
- [dsh-approval-llm](https://github.com/Letter2025/dsh-approval-llm) ⭐8 — Model-based permission approval (approve-for-me) for DeepSeek Harness: an approval/request answerer backed by a separate reviewer model（✅ 活跃）
- [dsh-balance-tide](https://github.com/huanyuLv/dsh-balance-tide) ⭐8 — DeepSeek Harness (DSH) Web 插件: 余额 + 峰谷计价潮汐提示。显示 DeepSeek 账户余额与本会话花费, 并在余额前提示当前峰/谷价格档位、距切换倒计时与使用建议。（✅ 活跃）
- [dsh-bash-encoding](https://github.com/lhh010/dsh-bash-encoding) ⭐8 — DSH bash 输出编码自动识别插件：替换 ctx.bash，自管 spawn 收集原始字节，自动检测 UTF-16LE/UTF-8/GBK 等编码并正确解码，修复 WSL/Windows 下 bash 工具的中文乱码。（✅ 活跃）
- [dsh-deepseek-vision](https://github.com/siegfly/dsh-deepseek-vision) ⭐8 — Vision-language gateway plugin for DeepSeek Harness - paste an image, DeepSeek sees text（✅ 活跃）
- [dsh-opencodego-usage](https://github.com/BeiZi6/dsh-opencodego-usage) ⭐8 — DSH Web GUI plugin: OpenCodeGo quota breathing light + liquid-glass panel with rolling/weekly/monthly progress bars (作者 Xu Yuanshan)（✅ 活跃）
- [dsh-plugin-d399](https://github.com/HuanLinOTO/dsh-plugin-d399) ⭐8 — 模型生成时右下角弹出小游戏菜单：Wordle/消消乐/192 款参数化小游戏。（✅ 活跃）
- [dsh-session-health](https://github.com/omdsh-dev/dsh-session-health) ⭐8 — 多帧 zstd 会话文件的帧级扫描诊断：撕裂/损坏/空会话检测，零依赖只读。（✅ 活跃）
- [dsh-ssh](https://github.com/UynajGI/dsh-ssh) ⭐8 — SSH remote-execution plugin for DeepSeek Harness: ProxyJump chain, SFTP filesystem, subprocess and PTY over ssh2（✅ 活跃）
- [dsh-tool-calculator](https://github.com/omdsh-dev/dsh-tool-calculator) ⭐8 — DSH 计算器工具插件：安全的数学表达式求值器，零依赖递归下降解析器（✅ 活跃）
- [dsh-ui-progress](https://github.com/lhh010/dsh-ui-progress) ⭐8 — DSH Web UI 会话进度插件：输入框停靠区常驻会话进度条（todos 真实进度 / 实时 token 生成速率 / 中断橘红态 / 待办提醒），零核心改动（✅ 活跃）
- [dsh-usage-dashboard](https://github.com/Cassius0924/dsh-usage-dashboard) ⭐8 — DeepSeek 额度与用量仪表盘 — DSH (DeepSeek Harness) 动态 Cordis 插件（✅ 活跃）
- [dsh-browser](https://github.com/anweat/dsh-browser) ⭐7 — Self-contained browser runtime plugin for DeepSeek Harness — bundles Playwright (chromium) and OpenCLI as plugin-local dependencies, exposes a browser service and interactive browser tools.（✅ 活跃）
- [dsh-builtin-toggles](https://github.com/Starfie1d1272/dsh-builtin-toggles) ⭐7 — 官方 DSH Web 内置功能可读目录 + 安全 UI 开关。（✅ 活跃）
- [dsh-director-toolkit](https://github.com/lhmd/dsh-director-toolkit) ⭐7 — DSH Director Toolkit is a DeepSeek Harness plugin for 3D artists, technical designers, and creative coders. Paste a half-formed idea, a reference note, or a portfolio caption and get a compact direction pack for Blender, Three.js, Houdini, or C4D.（✅ 活跃）
- [dsh-git-identity](https://github.com/LoserFox/dsh-git-identity) ⭐7 — DSH 插件：git 提交固定使用环境自身作者身份（优先 gh CLI 登录账号，GitHub noreply 邮箱），GIT_AUTHOR_*/GIT_COMMITTER_* 环境变量注入压过一切 git config（✅ 活跃）
- [dsh-landscape](https://github.com/cyanseek/dsh-landscape) ⭐7 — Agent-first DeepSeek Harness plugin intelligence: verify existing plugins, identify missing capabilities, and generate build-ready briefs.（✅ 活跃）
- [dsh-lark-meeting-notifier](https://github.com/yeruizhi/dsh-lark-meeting-notifier) ⭐7 — 一个只有副作用的DeepSeekHarness插件：在你跟 AI 聊得神魂颠倒时，提醒你「该去跟碳基生命开会了」。（✅ 活跃）
- [dsh-pdf](https://github.com/sunshine-lang/dsh-pdf) ⭐7 — PDF 工具箱：pdfjs-dist 本地提取文本、元数据与页区间，无需 API Key。（✅ 活跃）
- [dsh-plugin-diff-review](https://github.com/Civitasv/dsh-plugin-diff-review) ⭐7 — Diff Review Plugin for DeepSeek Harness（✅ 活跃）
- [dsh-spend](https://github.com/nonewind/dsh-spend) ⭐7 — Token 用量与费用估算：悬浮面板，按模型/天/会话统计，自动识别计费套餐。（✅ 活跃）
- [dsh-token-panel](https://github.com/juhe291/dsh-token-panel) ⭐7 — A corner HUD for DeepSeek Harness that shows your session's token pressure, per-model cost, and daily/monthly usage at a glance — with an editable budget & balance that tracks spending for you. 右下角常驻的 Token 仪表盘：实时查看会话压力、按模型估算花费，预算和余额点一下就能改，每天每月用了多少都有记录。（✅ 活跃）
- [dsh-tool-turbo](https://github.com/Electricitysheep/dsh-tool-turbo) ⭐7 — Per-round reasoning_effort optimizer for DeepSeek Harness (dsh): auto-downgrades tool-call reasoning for simple tool chains, lifting back for heavy work. Cuts thinking time between tool calls.（✅ 活跃）
- [dsh-weather](https://github.com/sunshine-lang/dsh-weather) ⭐7 — 天气工具：Open-Meteo 当前天气与多日预报，免费免密钥。（✅ 活跃）
- [dsh-worktree](https://github.com/FlashingChen/dsh-worktree) ⭐7 — Codex-style permanent git worktrees for DeepSeek Harness: worktree_create/list/remove agent tools, a /worktree chat command, and durable per-repo manifests.（✅ 活跃）
- [dskin](https://github.com/dancingmemory/dskin) ⭐7 — 卡通像素皮肤插件：原始界面不动，像素宠物散步、眨眼、跳跃。（✅ 活跃）
- [deepseek-harness-themes](https://github.com/orxz/deepseek-harness-themes) ⭐6 — A collection of UI themes for deepseek-harness.（✅ 活跃）
- [dsh-agent-message](https://github.com/GengDaPeng/dsh-agent-message) ⭐6 — DeepSeek Harness 跨会话 Agent 通信插件｜Cross-session agent-to-agent messaging with offline delivery, receipts and session navigation for DeepSeek Harness.（✅ 活跃）
- [dsh-blue-whale-maid](https://github.com/yuxino/dsh-blue-whale-maid) ⭐6 — DeepSeek Harness Web 的蓝鲸女仆桌宠，任务有动静时会在页面边上提醒你。（✅ 活跃）
- [dsh-claude-cli](https://github.com/katsos/dsh-claude-cli) ⭐6 — DeepSeek Harness LLM provider that runs your installed Claude Code CLI as the model backend — no API key.（✅ 活跃）
- [dsh-composer-expand](https://github.com/13071301808/dsh-composer-expand) ⭐6 — Composer expand/collapse toggle for DeepSeek Harness (dsh): a ⬆/⬇ button in the composer tool row grows the input to a tall 70vh writing view for long drafts.（✅ 活跃）
- [dsh-cue-plugin](https://github.com/unnnnoooo/dsh-cue-plugin) ⭐6 — DeepSeek Harness 的跨会话引用(cue)插件（✅ 活跃）
- [dsh-douyin](https://github.com/AnacondaKC/dsh-douyin) ⭐6 — DSH WebUI 侧栏短视频插件：原生播放器、系列导航、直链解析与精确历史回放（✅ 活跃）
- [dsh-email](https://github.com/STARDUSTLC666/dsh-email) ⭐6 — DeepSeek Harness 邮件插件：email_list/read/search/send/folders/attachment 六工具，内置 QQ/163/126/新浪/阿里/Gmail/Outlook/iCloud 八个预设，多账号、附件收发、Web 设置页配置，纯 Node 全平台。· IMAP/SMTP email tools for DeepSeek Harness agents.（✅ 活跃）
- [dsh-excel-chat](https://github.com/hccccc01333/dsh-excel-chat) ⭐6 — dsh-excel-chat — talk to Excel in DeepSeek Harness: create, edit, repair, and verify spreadsheets by conversation (cells, formulas, styles, filters, tables, charts); every edit is auto-validated.（✅ 活跃）
- [dsh-file-claim](https://github.com/Nwflower/dsh-file-claim) ⭐6 — 并行 Agent 会话的文件归属/认领系统：认领/释放、心跳过期接管、异步三路合并。（✅ 活跃）
- [dsh-island](https://github.com/cdxiaodong/dsh-island) ⭐6 — 通过 Unix socket 把 DSH agent 的会话、工具调用与审批实时桥接到 CodeIsland macOS 刘海面板，可直接在面板上批准/拒绝。（✅ 活跃）
- [dsh-neu-theme](https://github.com/Lhy723/dsh-neu-theme) ⭐6 — DeepSeek Harness Web 的轻拟物与磨砂玻璃主题插件，提供浅色/深色主题、环境光、材质纹理和细腻微交互。Neumorphism + glassmorphism theme plugin for DeepSeek Harness Web with warm light/dark palettes, ambient lighting, grain texture, and subtle micro-interactions.（✅ 活跃）
- [dsh-ohos-patch](https://github.com/shenjackyuanjie/dsh-ohos-patch) ⭐6 — 让deepseek harness能在 ohos上跑！（✅ 活跃）
- [dsh-plugin-anydoc](https://github.com/beancookie/dsh-plugin-anydoc) ⭐6 — 基于 @firecrawl/anydoc 将 Word/PPT/Excel/PDF/EPUB/CSV 等文档转换为 GFM Markdown。（✅ 活跃）
- [dsh-plugin-call-me](https://github.com/radres/dsh-plugin-call-me) ⭐6 — Your DeepSeek Harness agent rings your actual phone: it asks out loud, you answer out loud, and what you said steers the run.（✅ 活跃）
- [dsh-plugin-installer](https://github.com/Toukaiteio/dsh-plugin-installer) ⭐6 — 将 DSH 接入 GitHub 插件生态的市场插件。（✅ 活跃）
- [dsh-plugin-manager](https://github.com/2768651338/dsh-plugin-manager) ⭐6 — DeepSeek Harness 的图形化插件管理插件：在 设置 → 插件 里新增「插件管家」标签页，用中文名和说明展示每个插件是做什么的，并提供一键启停开关与内置备注编辑——启停写入全局层补丁并实时热生效，备注保存到本地覆盖文件长期生效。（✅ 活跃）
- [dsh-plugin-session-import](https://github.com/huguangyu666/dsh-plugin-session-import) ⭐6 — DeepSeek Harness plugin: import claude-code / codex / reasonix / zcode sessions（✅ 活跃）
- [dsh-plugin-workbench](https://github.com/Pasumao/dsh-plugin-workbench) ⭐6 — VS Code-style workspace file explorer with editable preview for the DSH web GUI（✅ 活跃）
- [dsh-restart](https://github.com/anweat/dsh-restart) ⭐6 — Restart DSH: configurable restart method (Node native / legacy PowerShell), post-restart continue prompt, optional watchdog auto-relaunch.（✅ 活跃）
- [dsh-tdai-memory](https://github.com/Scorp1o117/dsh-tdai-memory) ⭐6 — Agent memory for DeepSeek Harness | DeepSeek Harness 记忆插件（✅ 活跃）
- [dsh-tool-stat](https://github.com/omdsh-dev/dsh-tool-stat) ⭐6 — DSH 统计工具插件：描述统计/百分位数/频数分布/相关性，零依赖纯函数确定性（✅ 活跃）
- [dsh-voice-input-plugin](https://github.com/Zhangbo-cn/dsh-voice-input-plugin) ⭐6 — Composer mic for DeepSeek Harness Web: tap-to-monitor live transcription and hold-to-talk, with host Edge TTS reply reading that streams while the model generates, echo-pause during reading, and tap-to-stop.（✅ 活跃）
- [dsh-web-restart](https://github.com/1123762794/dsh-web-restart) ⭐6 — One-click restart button for the DeepSeek Harness Web UI: sidebar footer button, single click restarts the dsh web process. / DSH Web 界面一键重启按钮。（✅ 活跃）
- [dsh-web-search-exa](https://github.com/TonyDua/dsh-web-search-exa) ⭐6 — 零配置 Exa 网页搜索：免密钥匿名 MCP 回退 + API Key REST 搜索。（✅ 活跃）
- [dsh-calculator](https://github.com/bobcat848/dsh-calculator) ⭐5 — Calculate the real-time cost of DeepSeek API calls made by DeepSeek Harness.（✅ 活跃）
- [dsh-cost-plugin](https://github.com/RoxsLee/dsh-cost-plugin) ⭐5 — DSH 费用/余额读数插件：在输入框统计行旁实时显示「本次 ≈¥x · 会话 ≈¥x · 余额 ¥x」，内置 DeepSeek 官方价目表，支持 2026-08-17 起生效的峰谷定价（按节点时间戳自动选档），余额经官方 /user/balance 实时查询，失败静默降级。（✅ 活跃）
- [dsh-deepseek-billing](https://github.com/Jolly-J/dsh-deepseek-billing) ⭐5 — DSH WebUI 插件:DeepSeek 余额显示与按会话费用估算（✅ 活跃）
- [dsh-defend](https://github.com/PerryLink/dsh-defend) ⭐5 — Prompt-injection, jailbreak, and secret-leak defense for DeepSeek Harness: Aho-Corasick detection with allow/ask/block interception and sanitized audit events（✅ 活跃）
- [dsh-desktop-pet](https://github.com/FenyxHuang/dsh-desktop-pet) ⭐5 — DeepSeek Harness 桌面宠物:鲸鱼实时反应 agent 状态(思考冒泡/工作中工具/出错),API 余额渲染为圆形海平面,点击触发跳跃或 40% 转体跳水,带随机台词。（🧪 实验性）
- [dsh-github-login](https://github.com/Noob-stupid/dsh-github-login) ⭐5 — DeepSeek Harness 生态的 GitHub 可视化登录工具（零终端）：设备码流程，令牌同步 gh CLI | Visual GitHub login for the DSH ecosystem - no terminal needed（✅ 活跃）
- [dsh-notify-windows](https://github.com/SeverusZh/dsh-notify-windows) ⭐5 — DSH Windows 原生通知，零依赖。（✅ 活跃）
- [dsh-session-cleaner](https://github.com/fountunt/dsh-session-cleaner) ⭐5 — 为 DeepSeek Harness 提供会话删除能力，支持侧边栏 ⋮ 菜单入口（✅ 活跃）
- [dsh-session-timeline](https://github.com/XiLuovo/dsh-session-timeline) ⭐5 — DeepSeek Harness 会话时间轴插件：横短横线波浪、当前消息定位、点击跳转、圆角预览 tooltip、可收起/展开（✅ 活跃）
- [dsh-split-panes](https://github.com/lehhair/dsh-split-panes) ⭐5 — Split panes.（✅ 活跃）
- [dsh-status-bar](https://github.com/Starlight-bananice/dsh-status-bar) ⭐5 — Know what your agent is doing at a glance — 17-segment configurable status bar for DeepSeek Harness: status/model/context/tokens/TPS/cost/jobs. 一眼看清你的 agent 正在做什么：17 段可配置 DSH 会话状态栏。（✅ 活跃）
- [dsh-stream-rules](https://github.com/jiesou/dsh-stream-rules) ⭐5 — 模式匹配自动注入 steering rules，不占系统上下文 - Inject rules when needed, without wasting context. Similar to oh-my-pi's "Time-traveling stream rules", but with a very simple and compact code implementation.（✅ 活跃）
- [dsh-web-attention-badge](https://github.com/Luaphes/dsh-web-attention-badge) ⭐5 — Attention reminders for the DeepSeek Harness Web UI: frame badge, (N) tab title and whale-favicon recolor for sessions waiting for input or finished unopened.（✅ 活跃）
- [nowledge-mem-deepseek-harness](https://github.com/nowledge-co/nowledge-mem-deepseek-harness) ⭐5 — 将 Nowledge Mem 记忆服务接入 DeepSeek Harness 的社区插件包。（✅ 活跃）
- [zotero-harvest](https://github.com/Fisfzy/zotero-harvest) ⭐5 — Zotero 文献采集入库插件（DSH external plugin）：多源检索（OpenAlex/arXiv/Crossref/Europe PMC/Semantic Scholar）+ OA 下载链接解析（Unpaywall）+ 充分性审计 + 入库本地 Zotero + 触发 zotero-wave-rag 重建（✅ 活跃）
- [codex-eyes-hands](https://github.com/651002/codex-eyes-hands) ⭐4 — 专为 DeepSeek Harness 打造：把本机 Codex CLI 变成纯文本 AI agent 的眼睛和手——看图/读文件/画图/监督执行/双通道容灾（✅ 活跃）
- [dsh-approval-gate](https://github.com/moon09300731/dsh-approval-gate) ⭐4 — DeepSeek Harness 自动审批门控：Flash 预判写入/命令是否不可回补，安全操作自动批准、危险操作转人工（fail-safe）。（✅ 活跃）
- [dsh-archive-viewer](https://github.com/keepermttl/dsh-archive-viewer) ⭐4 — DeepSeek Harness 归档会话管理插件：查看/恢复已归档会话（回到原工作区分组）+ 右上角一键关闭 dsh。MIT 许可，欢迎收录到任何插件合集，注明出处即可。（✅ 活跃）
- [dsh-auxiliary](https://github.com/dsh-plugins/dsh-auxiliary) ⭐4 — Auxiliary models for DeepSeek Harness: vision understanding and context compression through dedicated model routes. DeepSeek Harness 辅助模型插件：为视觉理解、上下文压缩、审批审查、子代理、会话标题与图片生成提供独立的模型路由、工具与系统提示，全程不触碰主对话模型。（✅ 活跃）
- [dsh-bell-notify](https://github.com/Laplace-bit/dsh-bell-notify) ⭐4 — Configurable, unobtrusive Web Audio lifecycle notifications for DeepSeek Harness (dsh): 10 events, custom sounds, offline playback.（✅ 活跃）
- [dsh-black-whale](https://github.com/147228/dsh-black-whale) ⭐4 — DeepSeek Harness 黑鲸实验室主题：官网黑鲸 × 夕小瑶 IP，真实 profile 可安装的 Web UI 插件（✅ 活跃）
- [dsh-companion](https://github.com/beijingwahw/dsh-companion) ⭐4 — DeepSeek Companion — DeepSeek Harness 官方伴侣插件：对话导出/交接摘要/成本优化/全局检索 + 执行轨迹分析、Prompt 工程工作台、多模型竞技场、任务编排、安全与审计（E–J 九大模块，Cordis 插件化）。（✅ 活跃）
- [dsh-deeplink](https://github.com/qyw233/dsh-deeplink) ⭐4 — DSH WebUI 深链插件：?session=/?workspace= 直接打开指定项目对话（✅ 活跃）
- [dsh-deepseek-quota](https://github.com/yingjunnan/dsh-deepseek-quota) ⭐4 — DeepSeek API quota (balance) widget for the DSH web GUI: a floating bottom-right card showing remaining DeepSeek API balance.（✅ 活跃）
- [dsh-ffmpeg](https://github.com/STARDUSTLC666/dsh-ffmpeg) ⭐4 — DeepSeek Harness 视频处理插件：ffmpeg_probe/cut/concat/encode/subtitle/extract/gif 七工具，走官方 subprocess 服务、argv 数组无 shell 注入、零运行时依赖；纯 Node 全平台。· Video processing tools for DeepSeek Harness agents.（✅ 活跃）
- [dsh-git-status](https://github.com/Wongzexu/dsh-git-status) ⭐4 — Git status (Git Graph) plugin for DSH: commit DAG lane graph + uncommitted changes/stash + inline diffs + branch operations. DSH 插件：Git 状态浮窗（泳道图/未提交/stash/diff/分支操作）。（✅ 活跃）
- [dsh-guardian](https://github.com/cdxiaodong/dsh-guardian) ⭐4 — Agent 安全护栏：拦截并审计所有工具调用，命中敏感操作就要求人工确认。（✅ 活跃）
- [dsh-heatmap](https://github.com/283Gawin/dsh-heatmap) ⭐4 — DSH Web GUI activity heatmap plugin: GitHub-style commit/token/spend heatmap in the sidebar with per-model cost estimation（✅ 活跃）
- [dsh-input-history](https://github.com/lhh010/dsh-input-history) ⭐4 — 终端风格输入历史：Ctrl+Up/Down 召回与切换已发送消息。（✅ 活跃）
- [dsh-library](https://github.com/PerryLink/dsh-library) ⭐4 — Local document knowledge base for DeepSeek Harness: library_add/remove/list, hybrid semantic+keyword library_search with diversity re-ranking, relevance filtering and lost-in-the-middle avoidance, citation-aware injection, library_cite_check and library_diagnose — SQLite-backed index via the storage domain, local embedding, zero model downloads.（✅ 活跃）
- [dsh-llm-verifier](https://github.com/Web0926/dsh-llm-verifier) ⭐4 — 运行 3 或 5 个隔离的编程代理候选，验证其补丁，用 LLM 对通过验证的候选排序，并仅在用户批准后应用获胜补丁。（✅ 活跃）
- [dsh-neo-skin](https://github.com/0nt-one/dsh-neo-skin) ⭐4 — Neo-brutalism skin for the DeepSeek Harness Web UI — hard borders, high contrast, two switchable schemes (Blue Command / Aged Newspaper), works in light and dark themes.（✅ 活跃）
- [dsh-notebooks](https://github.com/havingautism/dsh-notebooks) ⭐4 — Notebooks plugin (cordis).（✅ 活跃）
- [dsh-output-styles](https://github.com/PerryLink/dsh-output-styles) ⭐4 — Claude Code outputStyles for DeepSeek Harness - session-scoped, durable, runtime-switchable model output styles (/style command, output_style storage domain, systemPrompt injection)（✅ 活跃）
- [dsh-plugin-deepeye](https://github.com/Favio8/dsh-plugin-deepeye) ⭐4 — DeepEye vision plugin for DeepSeek Harness (DSH): image description, OCR, VQA, UI layout, and clipboard analysis.（✅ 活跃）
- [dsh-polyglot](https://github.com/Jesse-njx/dsh-polyglot) ⭐4 — dsh-polyglot — the model switch for DSH: generic OpenAI-compatible ctx.llm adapter, curated free/cheap DeepSeek presets, automatic provider fallback on rate limits（✅ 活跃）
- [dsh-pomodoro](https://github.com/causebefore/dsh-pomodoro) ⭐4 — DeepSeek Harness Web 番茄钟插件：可配置专注与休息时长，提供侧栏入口和可拖动浮动面板（✅ 活跃）
- [dsh-revive](https://github.com/omdsh-dev/dsh-revive) ⭐4 — DSH 一键复活：重启后给所有被打断的会话自动发送「继续」指令（/revive 命令 + revive_sessions 工具 + 浏览器一键按钮）（✅ 活跃）
- [dsh-rss](https://github.com/STARDUSTLC666/dsh-rss) ⭐4 — DeepSeek Harness RSS 订阅插件：rss_list/add/remove/fetch/check 五工具，RSS 0.9x/1.0/2.0 与 Atom 归一化解析，订阅列表持久化到 settings，proxyUrl 特殊代理支持；纯 Node 全平台。· RSS/Atom subscription tools for DeepSeek Harness agents.（✅ 活跃）
- [dsh-skill-hub](https://github.com/cheshireez/dsh-skill-hub) ⭐4 — DSH Web GUI 技能中枢：基于官方 ctx.skills 注册表浏览、搜索、启停、查看、诊断并新建本地技能，附技能市场：来源快照跟踪、一键全量更新。（✅ 活跃）
- [dsh-skin-switcher](https://github.com/zhtx2024/dsh-skin-switcher) ⭐4 — DeepSeek Harness Web GUI 皮肤切换插件：设置界面一键切换已安装皮肤（✅ 活跃）
- [dsh-tool-csv](https://github.com/omdsh-dev/dsh-tool-csv) ⭐4 — DSH CSV 数据工具插件：解析/查询/统计/转换 CSV 文本（RFC 4180），零依赖状态机解析器，注册 csv 工具（✅ 活跃）
- [dsh-tool-diff](https://github.com/omdsh-dev/dsh-tool-diff) ⭐4 — DSH Diff 工具插件：文本/JSON/CSV/Markdown 结构化比较与 unified diff，零依赖只读，注册 diff 工具（✅ 活跃）
- [dsh-tool-git](https://github.com/lxj808624/dsh-tool-git) ⭐4 — 结构化安全 Git 工具：status/diff/log/branch/stage/commit/stash/show，带破坏性命令防护。（✅ 活跃）
- [dsh-tool-markdown](https://github.com/omdsh-dev/dsh-tool-markdown) ⭐4 — DSH Markdown 工具插件：HTML↔Markdown 转换、GFM 表格规范化、目录生成，零依赖轻量解析器，注册 markdown 工具（✅ 活跃）
- [dsh-trajectory-governance](https://github.com/dfycaly98931680/dsh-trajectory-governance) ⭐4 — Agent trajectory governance & anomaly diagnosis plugin for DeepSeek Harness (dsh): multi-branch trajectory trees, loop-deadlock / invalid-retry / goal-drift detection, cost attribution, alerts, one-click interrupt & breakpoint fork, independent GUI tab. Zero kernel modification.（✅ 活跃）
- [dsh-verification-receipt](https://github.com/030611/dsh-verification-receipt) ⭐4 — Privacy-minimal heuristic per-turn verification summaries for DeepSeek Harness（✅ 活跃）
- [dsh-wallpaper](https://github.com/chinaRXQ/dsh-wallpaper) ⭐4 — Wallpaper skin for the DeepSeek Harness (dsh) web UI: image background with opacity, mask and blur controls.（✅ 活跃）
- [dsh-win-notify](https://github.com/MuziIsabel/dsh-win-notify) ⭐4 — DSH 插件：代理任务完成时弹出带声音的 Windows Toast 通知，点击通知即可直接切回并前台显示 DSH 标签页（✅ 活跃）
- [dsh-wordbox](https://github.com/arcmosin/dsh-wordbox) ⭐4 — 输入框旁常用词箱：全局/项目词桶，一键插入。（✅ 活跃）
- [dsh-workspace-search](https://github.com/tsonglew/dsh-workspace-search) ⭐4 — VS Code 风格工作区关键词搜索：Better Sidebar 生态的搜索 Tab。（✅ 活跃）
- [deepseek-harness-plugin-manager](https://github.com/hrhgit/deepseek-harness-plugin-manager) ⭐3 — Web plugin manager for DeepSeek Harness (DSH): inspect, search, group, enable, and disable Cordis plugins.（✅ 活跃）
- [dsh-agentmemory](https://github.com/elementor-i/dsh-agentmemory) ⭐3 — agentmemory for DeepSeek Harness (dsh): full memory_* tools, capture hooks, and context injection over the local REST server（✅ 活跃）
- [dsh-auto-chess](https://github.com/omdsh-dev/dsh-auto-chess) ⭐3 — DSH Web里的自走棋插件：人机对战或双AI对弈（✅ 活跃）
- [dsh-bill](https://github.com/Jannchie/dsh-bill) ⭐3 — DSH (DeepSeek Harness) plugin: per-session cost line + cost attribution report, priced by llm-pricing（✅ 活跃）
- [dsh-budget](https://github.com/PerryLink/dsh-budget) ⭐3 — Cost governance for DeepSeek Harness: aggregated token/cost metering per model, session and day, budget caps with threshold alerts and over-limit policies, carbon footprint estimation, per-model latency benchmarks, a Settings budget tab, and the /budget command（✅ 活跃）
- [dsh-calendar](https://github.com/STARDUSTLC666/dsh-calendar) ⭐3 — DeepSeek Harness 日历插件：calendar_list/create/update/delete/search 五工具，CalDAV 协议支持 Google/iCloud/Nextcloud/自定义端点，RRULE 重复事件自动展开，插件级 proxyUrl 代理，配置缺失不崩启动；纯 Node 全平台。· CalDAV calendar tools for DeepSeek Harness agents.（✅ 活跃）
- [dsh-conversation-share](https://github.com/bill9109/dsh-conversation-share) ⭐3 — 分享任意段落的 DSH 对话（✅ 活跃）
- [dsh-deepseek-balance](https://github.com/CN-Leo/dsh-deepseek-balance) ⭐3 — deepseek-harness 插件，实时查询deepseek账号余额（✅ 活跃）
- [dsh-diagram](https://github.com/hanzhangzzz/dsh-diagram) ⭐3 — Turn articles in DeepSeek Harness into editable Excalidraw canvases.（✅ 活跃）
- [dsh-docker](https://github.com/STARDUSTLC666/dsh-docker) ⭐3 — DeepSeek Harness 容器管理插件：docker_ps/logs/inspect/exec/manage 五工具，官方 subprocess 服务、argv 无 shell 注入、exec 审批门、零运行时依赖。· Containers for DeepSeek Harness agents.（✅ 活跃）
- [dsh-doctor](https://github.com/astra3294/dsh-doctor) ⭐3 — Deterministic diagnostics and recovery for DeepSeek Harness（✅ 活跃）
- [dsh-everything-oauth](https://github.com/kam74515-boop/dsh-everything-oauth) ⭐3 — Import local Codex / Grok / Claude / OpenCode / CC Switch logins into DeepSeek Harness（✅ 活跃）
- [dsh-file-uploads](https://github.com/l541402398/dsh-file-uploads) ⭐3 — 从 Web 输入框上传任意本地文件，待传卡片显示，设置页统一管理。（✅ 活跃）
- [dsh-fun-typewriter](https://github.com/omdsh-dev/dsh-fun-typewriter) ⭐3 — DSH Typewriter: WebAudio typing ambience with a plugin-owned settings API and zero audio assets（✅ 活跃）
- [dsh-llm-inspector](https://github.com/cdxiaodong/dsh-llm-inspector) ⭐3 — 统一 LLM 请求/响应检查器：调 reasoning effort、外部思考(think)导出、流量与包分析。（✅ 活跃）
- [dsh-llm-ollama](https://github.com/NOirBRight/dsh-llm-ollama) ⭐3 — Native Ollama Cloud provider and Web configuration plugin for DeepSeek Harness（✅ 活跃）
- [dsh-memory](https://github.com/flymysql/dsh-memory) ⭐3 — 跨会话记忆库：memory_remember / memory_recall / memory_forget 工具 + 设置页。（🧪 实验性）
- [dsh-memory-evidence](https://github.com/LeslieWylie/dsh-memory-evidence) ⭐3 — Git-first memory navigation and bounded evidence tools for DeepSeek Harness.（💤 停更）
- [dsh-observe](https://github.com/PerryLink/dsh-observe) ⭐3 — OpenTelemetry and Langfuse observability exporter for DeepSeek Harness: turn/step/tool/LLM spans, token and cost metrics, sanitized prompt/completion capture, async batching, bounded offline buffering, retry with backoff（✅ 活跃）
- [dsh-pet-corner](https://github.com/omdsh-dev/dsh-pet-corner) ⭐3 — DSH Pet Corner: a floating pet, keyless pet-image proxy, favorites, and plugin-owned settings API（✅ 活跃）
- [dsh-plugin-meta-memory](https://github.com/YYTbit/dsh-plugin-meta-memory) ⭐3 — Structured long-term memory system for DeepSeek Harness（✅ 活跃）
- [dsh-plugin.github.io](https://github.com/dsh-plugin/dsh-plugin.github.io) ⭐3 — DeepSeek Harness community plugin workshop and directory（✅ 活跃）
- [dsh-plugins-raincode](https://github.com/rainforest888/dsh-plugins-raincode) ⭐3 — dsh plugin: DeepSeek Harness 的模型层 = raincode(模型池/缓存/重试) + /skills 浏览（✅ 活跃）
- [dsh-prompt-stash](https://github.com/Wine-Red/dsh-prompt-stash) ⭐3 — Local, per-session prompt stash for DeepSeek Harness Web | 本地、分对话的提示词输入暂存工具。写了一半的长提示词，临时需要先问一个短问题？ 同时准备多个方案，但尚未决定发哪一个？将未完成的想法放入草稿架中，准备好后再继续完成（✅ 活跃）
- [dsh-prompt-studio](https://github.com/Moeblack/dsh-prompt-studio) ⭐3 — 带实时预览编辑用户与内置系统提示词片段。（✅ 活跃）
- [dsh-session-pin](https://github.com/PerryLink/dsh-session-pin) ⭐3 — Pin sessions and workspaces to the top of the DeepSeek Harness sidebar with per-pin row colors - a dual-face (host + client) dsh plugin.（✅ 活跃）
- [dsh-shortcuts](https://github.com/Ricketts-Guo/dsh-shortcuts) ⭐3 — DeepSeek Harness WebUI 键盘快捷键插件（34 个预置功能、一键录制自定义、静默权限切换）— Fully customizable keyboard shortcuts for the DSH WebUI.（✅ 活跃）
- [dsh-skill-studio](https://github.com/zhengjy01/dsh-skill-studio) ⭐3 — DSH skill 可视化与管理插件：设置面板列出全部 skill（含来源、嵌套标记与调用状态）、查看并编辑 SKILL.md 正文、一键启用/禁用模型与用户调用，并提供 skillmgr_list/get/save/policy 工具。（✅ 活跃）
- [dsh-specflow](https://github.com/lonelymoon87/dsh-specflow) ⭐3 — Specification-driven development toolkit for DeepSeek Harness.（✅ 活跃）
- [dsh-sticky-disclosure](https://github.com/Han-1413141/dsh-sticky-disclosure) ⭐3 — DSH Web client plugin: collapse every expanded section (Think / tool cards) in the conversation in one click, with a customizable hotkey.（✅ 活跃）
- [dsh-suggested-replies](https://github.com/Anionex/dsh-suggested-replies) ⭐3 — DSH Web 预测回复插件：AI 回复后在输入框上方生成可点击填入草稿的候选。（✅ 活跃）
- [dsh-sysmon](https://github.com/AKS1st/dsh-sysmon) ⭐3 — DSH Web 系统状态悬浮窗：实时 CPU/内存/磁盘占用率 | System-status overlay showing live CPU, memory and disk usage for DSH Web（✅ 活跃）
- [dsh-telemetry-redactor](https://github.com/030611/dsh-telemetry-redactor) ⭐3 — Fail-closed export-copy redaction for DeepSeek Harness session telemetry（✅ 活跃）
- [dsh-theme-plugin](https://github.com/BeiZi6/dsh-theme-plugin) ⭐3 — DSH Web GUI theme studio: presets + per-mode customization (accent, background, foreground, fonts, translucent sidebar, contrast) via the official webServer.tapIndex seam（✅ 活跃）
- [dsh-tool-encoding](https://github.com/omdsh-dev/dsh-tool-encoding) ⭐3 — DSH 编码/哈希工具插件：base64/base64url/url/hex 编解码、md5/sha1/sha256/sha512 哈希、UUID 生成，零依赖（✅ 活跃）
- [dsh-tool-json](https://github.com/omdsh-dev/dsh-tool-json) ⭐3 — DSH JSON 查询工具插件：JMESPath 子集查询，零依赖递归下降解析器（✅ 活跃）
- [dsh-tool-regex](https://github.com/omdsh-dev/dsh-tool-regex) ⭐3 — DSH 正则工具插件：测试匹配/提取捕获组/安全替换/静态解释正则（不执行代码），零依赖，注册 regex 工具（✅ 活跃）
- [dsh-tool-schema](https://github.com/omdsh-dev/dsh-tool-schema) ⭐3 — DSH JSON Schema 验证工具插件：validate/paths/explain/normalize，零网络零动态执行（✅ 活跃）
- [dsh-tool-search](https://github.com/vibeinging/dsh-tool-search) ⭐3 — 按 Agent 按需工具发现与渐进式 schema 披露。（✅ 活跃）
- [dsh-ultra-ui](https://github.com/havingautism/dsh-ultra-ui) ⭐3 — Ultra UI plugin (cordis).（✅ 活跃）
- [dsh-usage-plugin](https://github.com/Yihong89/dsh-usage-plugin) ⭐3 — DeepSeek Harness (DSH) plugins. First: dsh-usage-report — per-session token usage & estimated cost (/usage + usage_report), priced from the DeepSeek pricing table.（✅ 活跃）
- [dsh-vision-tools](https://github.com/moon09300731/dsh-vision-tools) ⭐3 — DeepSeek Harness 视觉能力全家桶：vision_understand 工具（OpenAI 兼容视觉 API，默认免费智谱 GLM-4V-Flash）+ 粘贴/拖拽/按钮三入口识图。（✅ 活跃）
- [dsh-webbridge](https://github.com/bill9109/dsh-webbridge) ⭐3 — DSH 结合 Kimi WebBridge 操控真实浏览器。（✅ 活跃）
- [mistymoon-dsh](https://github.com/mianyoubiaoqing/MistyMoon-DSH) ⭐3 — Local-first long-term companion plugin suite for DeepSeek Harness（✅ 活跃）
- [URL Manager](https://github.com/Piccolo123/url-manager) ⭐3 — Agent 优先的 URL 与知识收集系统：自动分类、标签、全文检索与共享收藏。（✅ 活跃）
- [zotero-wave-rag](https://github.com/Fisfzy/zotero-wave-rag) ⭐3 — 面向 Zotero 论文库的浪潮式 RAG 细节检索系统 —— DSH 外部插件。移植 VCPToolBox 浪潮语义动力学思想（标签河道图传播/虫洞跳转/钟型阻尼/Ω重排），配 BM25+RRF 混合检索、claim-evidence 忠实度校验、两级增量索引（✅ 活跃）
- [dsh-adb](https://github.com/SamXiaBing/dsh-adb) ⭐2 — ADB device & bench operations: device discovery, structured logcat (background streaming), apk install, file pull/push, dumpsys performance snapshots.（✅ 活跃）
- [dsh-agent-budget](https://github.com/vibeinging/dsh-agent-budget) ⭐2 — Native Harness agent-tree token budget plugin（✅ 活跃）
- [dsh-cost-meter](https://github.com/Sttrevens/dsh-cost-meter) ⭐2 — dsh plugin: per-turn USD cost badge in the Web UI (session total + per-message footer, hover breakdown) from token usage x a configurable pricing table.（✅ 活跃）
- [dsh-fork-graph](https://github.com/chouyong/dsh-fork-graph) ⭐2 — See your DSH conversation's fork history as a git graph — coloured branch lanes in the session header, click to jump. A pure-derivation DeepSeek Harness Web plugin.（✅ 活跃）
- [dsh-gitflow](https://github.com/lonelymoon87/dsh-gitflow) ⭐2 — Git status, diff, log, commit, branch, and optional Change Ledger tools for DeepSeek Harness.（✅ 活跃）
- [dsh-memoria](https://github.com/jiayan-xu/dsh-memoria) ⭐2 — 向量 + 图记忆后端：命名空间隔离、自动观察、召回、重要性处理与热重载。（🧪 实验性）
- [dsh-memory (Jesse-njx)](https://github.com/Jesse-njx/dsh-memory) ⭐2 — 基于 DSH 无损会话日志的引用式记忆：可人工审计的蒸馏事实，带引用来源。（✅ 活跃）
- [dsh-pin-recall](https://github.com/kerwin2046/dsh-pin-recall) ⭐2 — 从操作条固定助手回复，并在下一轮召回（/pin /recall）。（✅ 活跃）
- [dsh-plugin-choice-refresh](https://github.com/Pasumao/dsh-plugin-choice-refresh) ⭐2 — DSH 选择增强插件：「重新生成选项」/「更多选项」按钮。Choice refresh (regenerate / more options) for DeepSeek Harness (dsh).（✅ 活跃）
- [dsh-plugin-description](https://github.com/MysaDC/dsh-plugin-description) ⭐2 — mount one row in the composition and every plugin card on the Web Settings plugin list page gets a bilingual (zh/en) description; it also publishes the pluginDescriptions service so other plugins can register their own descriptions.（✅ 活跃）
- [dsh-plugin-quota-monitor](https://github.com/DoggyHU/dsh-plugin-quota-monitor) ⭐2 — DSH sidebar footer quota & balance monitor: DeepSeek Rage + OpenCode Go HP/MP/SP + SCNet (国家超算) Credits local estimate. 设置→插件管理可配置数据源与费率表。（✅ 活跃）
- [dsh-plugin-radar](https://github.com/dshplugin-me/dsh-plugin-radar) ⭐2 — Find DSH plugins by asking in plain language, then security-scan them before install（✅ 活跃）
- [dsh-review-loop](https://github.com/wuxiangru915/dsh-review-loop) ⭐2 — 增量代码审查：基于检查点的审查队列 + Web UI 面板 + /review 命令。（✅ 活跃）
- [dsh-scout](https://github.com/omdsh-dev/dsh-scout) ⭐2 — 面向 DeepSeek Harness 的只读环境探测插件，为智能体提供运行环境、软件版本、系统资源、端口、服务、硬件及工作区信息。（✅ 活跃）
- [dsh-session-search](https://github.com/Tieboyh/dsh-session-search) ⭐2 — 免索引跨 Agent 会话搜索。（✅ 活跃）
- [dsh-sub2api](https://github.com/GodD6366/dsh-sub2api) ⭐2 — Connect your sub2api gateway to DeepSeek Harness: OpenAI-compatible multi-provider routes (OpenAI / Claude / Grok / Gemini) behind one base URL, with per-key model discovery, usage lookup, and a settings page.（✅ 活跃）
- [dsh-test-drive](https://github.com/PerryLink/dsh-test-drive) ⭐2 — Isolated install-and-smoke test drives for DeepSeek Harness plugins: installs a repo or npm package into a throwaway DSH_HOME profile, verifies the bundle patch layer and boot logs, records a structured pass/fail result matrix (JSON/Markdown) for scoring pipelines, and quarantines every temp directory it owns（✅ 活跃）
- [dsh-test-runner](https://github.com/suimi8/dsh-test-runner) ⭐2 — 结构化测试运行工具：自动识别 vitest/jest/pytest/node:test，运行并解析失败摘要。（✅ 活跃）
- [dsh-trace](https://github.com/vibeinging/dsh-trace) ⭐2 — DeepSeek Harness telemetry backend that exports turns, model steps, and tool calls to yiTrace over HTTP.（✅ 活跃）
- [dsh-translate](https://github.com/PerryLink/dsh-translate) ⭐2 — Vendor parameter translation and deterministic JSON repair for DeepSeek Harness: /translate maps temperature/top_p/max_tokens/stop/system across 11 vendors, and the post-execute repair layer (plus fix_json) fixes broken JSON tool output without ever fabricating data（✅ 活跃）
- [dsh-turn-navigator](https://github.com/vibeinging/dsh-turn-navigator) ⭐2 — Private DSH Web turn navigation plugin（✅ 活跃）
- [dsh-usage-vendor-stats](https://github.com/kirigayakazima/dsh-usage-vendor-stats) ⭐2 — DeepSeek Harness usage stats by vendor (subscription / official API) × KPI: 53-week heatmap, trend chart, model drilldown, CSV export, and health cards.（✅ 活跃）
- [dsh-view-modes](https://github.com/NigelYao/dsh-view-modes) ⭐2 — Verbose/Normal/Summary 三种输出模式，工具调用与思考语义分组。（✅ 活跃）
- [dsh-what-changed](https://github.com/sjh9714/dsh-what-changed) ⭐2 — 会话顶栏的整会话改动审阅。列出本次会话 Agent 写过的每个文件与逐处改动，被权限拒绝的写入单独计数不算改动，数据来自 session projection 而非磁盘日志。（✅ 活跃）
- [dsh-workspace-menu](https://github.com/0imzero/dsh-workspace-menu) ⭐2 — DSH workspace/chat enhancement menu: pin, rename, open in file explorer, archive, fork, copy, new window. Settings integrated into General.（✅ 活跃）
- [visual-review](https://github.com/wang-bool/visual-review) ⭐2 — 在 DSH Web 聊天界面内联渲染粘贴/上传的图片，让纯文本模型获得视觉：云端多模态 API 优先，本机 Qwen3-VL 兜底。（✅ 活跃）
- [dsh-code-intel](https://github.com/lonelymoon87/dsh-code-intel) ⭐1 — Symbol-aware code indexing and hybrid search for DeepSeek Harness.（✅ 活跃）
- [dsh-computer-use](https://github.com/xiaoheizi1212/dsh-computer-use) ⭐1 — 模型无关的 Computer Use：隔离浏览器、Windows 原生助手与第三方桥接。（✅ 活跃）
- [dsh-doctor](https://github.com/asdf17128/dsh-doctor) ⭐1 — Find what your DeepSeek Harness (dsh) patches silently broke — dead patches, config fields dropped by whole-config replacement, unmaintained plugins. Read-only, zero deps.（✅ 活跃）
- [dsh-event-auditor](https://github.com/qing3a/dsh-event-auditor) ⭐1 — DeepSeek Harness 事件流审计面板插件：观察事件类型/分发模式/计数/最近事件，帮助插件作者理解 harness 内部（✅ 活跃）
- [dsh-humanizer](https://github.com/lynote-ai/dsh-humanizer) ⭐1 — 写作工具：去除 AI 腔并贴合个人文风。8 个确定性工具扫描文本、从样本提取文风指纹，并返回改写 brief。（🧪 实验性）
- [dsh-news-plugin](https://github.com/canghai666x/dsh-news-plugin) ⭐1 — RSS/新闻摄入插件：返回结构化的标题/链接/来源/日期/摘要，供模型排序与简报。（✅ 活跃）
- [dsh-payload-capture](https://github.com/Moeblack/dsh-payload-capture) ⭐1 — 捕捉每次上行模型 API payload，JSON 落盘，用于调试与可观测性。（✅ 活跃）
- [dsh-plugin-evaluation-standards](https://github.com/dsh-plugin-evaluation/dsh-plugin-evaluation-standards) ⭐1 — Open evaluation datasets, test cases, and metrics for DSH plugins.（✅ 活跃）
- [dsh-plugin-image-tools](https://github.com/Pasumao/dsh-plugin-image-tools) ⭐1 — DSH 图片插件：图片选择卡 + 回复内嵌图片 + 盲模型收图（✅ 活跃）
- [dsh-plugin-manager-registry](https://github.com/Jesse-njx/dsh-plugin-manager-registry) ⭐1 — @dsh-pm/registry — discover dsh plugins by merging the awesome-dsh-plugin list, GitHub dsh-plugin-topic search, and npm keyword search into one deduped, offline-tolerant registry (the discovery engine of dsh pm)（✅ 活跃）
- [dsh-plugin-quote-reply](https://github.com/yangYzc/dsh-plugin-quote-reply) ⭐1 — DSH plugin: select text in a conversation, then quote it into the composer or reply in a new window. / DeepSeek Harness 划词引用插件：选中文字一键引用回复或新窗口回复。（✅ 活跃）
- [dsh-plugin-radar](https://github.com/DshMarketPlace/dsh-plugin-radar) ⭐1 — Userscript: marks DeepSeek Harness plugins on GitHub and npm, with the install command that actually works（✅ 活跃）
- [dsh-repo-setup](https://github.com/gongyijie85/dsh-repo-setup) ⭐1 — 只读仓库体检引导工具（repo_setup_scan）：识别技术栈/测试/文档/git/数据库线索，给出插件、MCP 与卫生文件的安装建议（claude-code-setup 对应版）。（✅ 活跃）
- [dsh-routines](https://github.com/Jesse-njx/dsh-routines) ⭐1 — dsh-routines — scheduled agents for DSH: run a prompt on a cron, get the digest where you already are (file digests, chatnode delivery, unattended-safe)（✅ 活跃）
- [dsh-tool-approval](https://github.com/ilharp/dsh-tool-approval) ⭐1 — Manual approval for Deepseek Harness (aka "Manual Mode"/"Ask Mode")（✅ 活跃）
- [dsh-tps](https://github.com/Small-tailqwq/dsh-tps) ⭐1 — 只是一个 tps 插件（✅ 活跃）
- [dsh-turn-index](https://github.com/Simon314620/dsh-turn-index) ⭐1 — 回合索引侧栏：每个用户回合一条，点击跳转，滚动监听高亮。（✅ 活跃）
- [dsh-voice-webspeech](https://github.com/anweat/dsh-voice-webspeech) ⭐1 — Browser Web Speech API voice input for DSH: zero server, zero keys, zero model downloads (Edge=Azure, Chrome=Google speech).（✅ 活跃）
- [dshp](https://github.com/asdf17128/dshp) ⭐1 — Manage DeepSeek Harness profiles — list, create, clone, diff, and share a whole dsh setup as one portable file.（✅ 活跃）
- [dsh-client-auto-retry](https://github.com/Frog755/dsh-client-auto-retry)  — 回合中断自动续跑：turn/end 因 error/interrupted/max-tokens 结束时自动发送「继续」，支持宽限期、冷却、连发上限、启动扫描与设置卡片；不切换模型/provider。（✅ 活跃）
- [dsh-deepseek-balance](https://github.com/dshiq04/dsh-deepseek-balance)  — 面向deepseek harness的余额查看插件（✅ 活跃）
- [dsh-evoforge](https://github.com/deepseek-harness-evoforge/dsh-evoforge)  — Evidence-driven, cache-stable extensions for DeepSeek Harness（✅ 活跃）
- [dsh-fork-to-preset](https://github.com/bpc-oss/dsh-fork-to-preset)  — 在会话 Header 上一键把当前会话分叉到任意 agent preset：选择 preset 后创建挂载到该 preset 的新子会话，并继承源会话的已完成轮次。（✅ 活跃）
- [dsh-git-branch-switcher](https://github.com/mixin-ai/dsh-git-branch-switcher)  — 会话头部 git 分支胶囊：显示并在 Web UI 中切换工作区分支。（✅ 活跃）
- [dsh-llm-local-token](https://github.com/tianxia--/dsh-llm-local-token)  — 复用本机 Codex CLI 与 Claude Code OAuth 凭据的 DSH 模型提供方路由，无需另配 API Key。（✅ 活跃）
- [dsh-plugin](https://github.com/dsh-plugin-dev/dsh-plugin)  — Build your own coding agent with Pi dsh-plugin（✅ 活跃）
- [dsh-plugin-cost](https://github.com/yweilai77-dev/dsh-plugin-cost)  — Session cost estimate in the DSH Web composer dock (tokenUsage × configurable price table, one-click official-price refresh).（✅ 活跃）
- [dsh-precedent](https://github.com/dshplugin-me/dsh-precedent)  — Evidence-backed working memory for DeepSeek Harness: a cited ledger of what already worked in this workspace, built from the session log you already have. No index, no model, no capture step.（✅ 活跃）
- [dsh-routed-subagent](https://github.com/bpc-oss/dsh-routed-subagent)  — 从任意会话派发一个完整挂载到任意 agent preset 的一次性子代理，支持按次指定模型/provider、模型可用性预检，以及外部 CLI 引擎（codex / claude / codebuddy），支持后台任务、实时进度、终止与可续会话。（✅ 活跃）
- [dsh-session-cleaner-cli](https://github.com/ChenChen913/dsh-session-cleaner-cli)  — 深度清理 DeepSeek Harness (DSH) 工作区会话的离线 CLI：按工作区列出/删除/恢复会话，自动同步工作区账目与投影缓存。Offline session cleaner for DeepSeek Harness: list, delete (trash+restore) and prune ghost sessions across workspaces.（✅ 活跃）
- [dsh-upload](https://github.com/Ei-Ayw/dsh-upload)  — DSH Web 的上传按钮:点 📎 选本地文件,字节落盘到会话工作区 .uploads/<会话ID>/,绝对路径追加进输入框(可见可编辑),AI 用自带 fs 工具直接读取。零依赖。（✅ 活跃）

### Skills


#### 🔥 Top 10

| # | 项目 | 星数 | 说明 | 状态 |
|---|---|---|---|---|
| 1 | [memos](https://github.com/MemTensor/MemOS) | ⭐10,873 | Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings and DeepSeek Harness support. | ✅ 活跃 |
| 2 | [dsh-routing-suite](https://github.com/yjh051108/dsh-routing-suite) | ⭐6,940 | dsh-routing-suite — injector + router-standard kit: install the runtime injector first, then the task-aware reasoning-mode router preset (measured P1-P23). | ✅ 活跃 |
| 3 | [easyeda-agent](https://github.com/zhoushoujianwork/easyeda-agent) | ⭐274 | EasyEDA Pro automation: Go daemon + in-app connector + agent skill + stdio MCP server for typed schematic/PCB actions, workflow gates, and DRC. | ✅ 活跃 |
| 4 | [dsh-taskboard](https://github.com/shengsheng90/DSH-taskboard) | ⭐195 | Native local Taskboard plugin for DeepSeek Harness. SQLite-backed projects, Agent claim/review, and a native Web UI — no iframe, no second chat runtime. | ✅ 活跃 |
| 5 | [deepseek-harness-genui](https://github.com/pengyue-polaron/deepseek-harness-genui) | ⭐107 | Task-specific React apps for DeepSeek Harness with state carried into the next Agent turn | ✅ 活跃 |
| 6 | [dsh-skill-viewer](https://github.com/Fishquito7/dsh-skill-viewer) | ⭐88 | DSH Web 技能设置区：热启停、删除与新增。 | ✅ 活跃 |
| 7 | [dsh-reverse-skill](https://github.com/dhicoc/dsh-reverse-skill) | ⭐58 | Complete reverse-skill (85 SKILL.md) as a DeepSeek Harness (dsh) Cordis plugin — reverse engineering, authorized pentesting and security research skill pack. | ✅ 活跃 |
| 8 | [dsh-save-money](https://github.com/zhu168/dsh-save-money) | ⭐35 | Save-money plugin for DSH (DeepSeek Harness) — define your own "pause / resume" time windows; at pause time running long tasks are paused (not stopped) automatically, and they resume when the window ends. | ✅ 活跃 |
| 9 | [dsh-skill-picker](https://github.com/a735624258/dsh-skill-picker) | ⭐25 | DSH 实现 workbuddy 同款选择 skill 功能 | WorkBuddy-style skill picker for DeepSeek Harness: pick a skill in the composer, insert the official /skill-name gesture, and DSH loads it with your message. | ✅ 活跃 |
| 10 | [dsh-science](https://github.com/biociao/dsh-science) | ⭐24 | Claude Science-style research workbench: ReAct research-loop engine (research_* tools), versioned artifacts with provenance (artifact_* tools), and 10 science skills for genomics/pathogens/bioinformatics. | ✅ 活跃 |

#### 完整列表（44）

- [memos](https://github.com/MemTensor/MemOS) ⭐10,873 — Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings and DeepSeek Harness support.（✅ 活跃）
- [dsh-routing-suite](https://github.com/yjh051108/dsh-routing-suite) ⭐6,940 — dsh-routing-suite — injector + router-standard kit: install the runtime injector first, then the task-aware reasoning-mode router preset (measured P1-P23).（✅ 活跃）
- [easyeda-agent](https://github.com/zhoushoujianwork/easyeda-agent) ⭐274 — EasyEDA Pro automation: Go daemon + in-app connector + agent skill + stdio MCP server for typed schematic/PCB actions, workflow gates, and DRC.（✅ 活跃）
- [dsh-taskboard](https://github.com/shengsheng90/DSH-taskboard) ⭐195 — Native local Taskboard plugin for DeepSeek Harness. SQLite-backed projects, Agent claim/review, and a native Web UI — no iframe, no second chat runtime.（✅ 活跃）
- [deepseek-harness-genui](https://github.com/pengyue-polaron/deepseek-harness-genui) ⭐107 — Task-specific React apps for DeepSeek Harness with state carried into the next Agent turn（✅ 活跃）
- [dsh-skill-viewer](https://github.com/Fishquito7/dsh-skill-viewer) ⭐88 — DSH Web 技能设置区：热启停、删除与新增。（✅ 活跃）
- [dsh-reverse-skill](https://github.com/dhicoc/dsh-reverse-skill) ⭐58 — Complete reverse-skill (85 SKILL.md) as a DeepSeek Harness (dsh) Cordis plugin — reverse engineering, authorized pentesting and security research skill pack.（✅ 活跃）
- [dsh-save-money](https://github.com/zhu168/dsh-save-money) ⭐35 — Save-money plugin for DSH (DeepSeek Harness) — define your own "pause / resume" time windows; at pause time running long tasks are paused (not stopped) automatically, and they resume when the window ends.（✅ 活跃）
- [dsh-skill-picker](https://github.com/a735624258/dsh-skill-picker) ⭐25 — DSH 实现 workbuddy 同款选择 skill 功能 | WorkBuddy-style skill picker for DeepSeek Harness: pick a skill in the composer, insert the official /skill-name gesture, and DSH loads it with your message.（✅ 活跃）
- [dsh-science](https://github.com/biociao/dsh-science) ⭐24 — Claude Science-style research workbench: ReAct research-loop engine (research_* tools), versioned artifacts with provenance (artifact_* tools), and 10 science skills for genomics/pathogens/bioinformatics.（✅ 活跃）
- [dsh-media-skills](https://github.com/MJorgin/dsh-media-skills) ⭐19 — Free image reading & generation for DeepSeek Harness (rc.7 / rc.8 / v0.1.1-rc.1 / rc.2) — paste-image reading with auto vision transcription, DeepSeek-V4-Flash-Vision-Exp / GLM-4V-Flash / SenseNova / Gemini failover, Kolors + U1 Fast generation. No keys in repo.（✅ 活跃）
- [dsh-opencode-palette](https://github.com/FeatherHunter/dsh-opencode-palette) ⭐18 — 🎨 看腻了 DSH 默认皮肤？34 款 opencode 经典配色一键换上——tokyonight、dracula、gruvbox、matrix、rose-pine……即点即换，重启不丢。34 opencode themes for DeepSeek Harness, one click, persisted. More by @FeatherHunter: ⚡ dsh-prompt · 🧠 dsh-mattpocock-skills-deck（✅ 活跃）
- [dsh-directorx](https://github.com/LaplaceYoung/dsh-directorx) ⭐16 — DirectorX as a DeepSeek Harness plugin: AI video/image/audio skills, knowledge corpus, and configurable vision/image/video/audio model tools.（✅ 活跃）
- [dsh-evoresearch](https://github.com/Karbo123/DSH-EvoResearch) ⭐14 — 自进化科研工作流（✅ 活跃）
- [dsh-plugin-development](https://github.com/w2112515/dsh-plugin-development) ⭐14 — Portable Agent Skill for developing and auditing DeepSeek Harness plugins, with an optional profile-installable DSH bundle adapter.（✅ 活跃）
- [dsh_plugin_swift_cycle](https://github.com/Solismuchengxue/dsh_plugin_swift_cycle) ⭐14 — Swift Cycle governance skill adapter for DeepSeek Harness; user-invoked, version-pinned, and offline-verifiable.（✅ 活跃）
- [dsh-plugin-dev](https://github.com/omdsh-dev/dsh-plugin-dev) ⭐13 — 插件开发踩坑与做法档案（skill + 文档）：cordis 双副本、tsconfig 三件套、Windows junction、多帧 zstd 实测。（✅ 活跃）
- [dsh-claude-move](https://github.com/PerryLink/dsh-claude-move) ⭐11 — Four-source migration wizard for DeepSeek Harness: move Claude Code, Codex, OpenCode and Hermes sessions, memories, skills, instructions and slash commands into DSH (/move wizard + resumable sessions, approval-gated, idempotent).（✅ 活跃）
- [dsh-plugin-skills](https://github.com/omdsh-dev/dsh-plugin-skills) ⭐11 — 构建与测试 DSH 插件的 Agent 技能：从脚手架到发布。（✅ 活跃）
- [dsh-fail-logger](https://github.com/Areium/dsh-fail-logger) ⭐9 — DeepSeek Harness（DSH）插件：自动记录所有执行模式（原生工具 / PTC run_code / 代码内嵌工具调用）的工具失败错因，去重、计数、确定性排序后沉淀进 skill 的机器维护实录区段——让 Agent 越用越少错。（✅ 活跃）
- [dsh-godot-skill](https://github.com/akira399/dsh-godot-skill) ⭐9 — Godot Engine 4.x 全栈游戏开发技能插件。（✅ 活跃）
- [dsh-task-status](https://github.com/vlln/dsh-task-status) ⭐9 — DSH 插件：后台任务状态条（对话页任务进度 + 实时输出 tail）。官方 bundle 插件，dsh plugin --profile web add 安装（✅ 活跃）
- [dsh-codex-port](https://github.com/STARDUSTLC666/dsh-codex-port) ⭐8 — DeepSeek Harness 技能移植插件：把 ~/.codex 的 Codex 官方插件（186+ 个、583+ 技能）一键移植为 DSH 技能（codex_list/port/status），frontmatter 自动转换、幂等跳过。· Batch-port the Codex plugin family into DSH skills.（✅ 活跃）
- [dsh-book2skill](https://github.com/omdsh-dev/dsh-book2skill) ⭐4 — 书转技能插件：获取→解析→理解→生成→安装的五阶段长任务。（✅ 活跃）
- [dsh-capability-receipt](https://github.com/dongsheng123132/dsh-capability-receipt) ⭐4 — Content-addressed receipts for skills actually loaded by DeepSeek Harness（✅ 活跃）
- [dsh-remotion](https://github.com/STARDUSTLC666/dsh-remotion) ⭐4 — DSH 视频创作技能插件：注册 Remotion 官方移植技能（React 编程式视频，38 个规则文件），安装即用。· Remotion skill plugin for DeepSeek Harness.（✅ 活跃）
- [dsh-ecc](https://github.com/gongyijie85/dsh-ecc) ⭐3 — ECC（227k⭐ 操作员系统）273 个技能（95.8%）分四批移植到 DSH。（✅ 活跃）
- [dsh-find-skill](https://github.com/Moximxxx/dsh-find-skill) ⭐3 — 桥接 vercel-labs/skills 生态：LLM 驱动技能搜索、安装与管理。（✅ 活跃）
- [dsh-humanize](https://github.com/zevorn/dsh-humanize) ⭐3 — 去 AI 味写作技能：让 Agent 输出更自然。（✅ 活跃）
- [dsh-local-ai](https://github.com/PerryLink/dsh-local-ai) ⭐3 — Local-model (Ollama) integration for DeepSeek Harness: discover, pull, remove, and inspect local models, route requests to them by task type or keyword with automatic fallback to the cloud, and get a one-shot status overview via /ollama.（✅ 活跃）
- [dsh-memoryhub](https://github.com/solknight48/dsh-memoryhub) ⭐3 — MemoryHub (mh) plugin for DeepSeek Harness (dsh): auto-loads checkpoint memory on session start, adds mh_* tools and the mh skill, and a Memory tab in the web UI（✅ 活跃）
- [dsh-skillradar](https://github.com/hellosky983/dsh-skillradar) ⭐3 — 扫描会话可见技能，按与近期对话的相关度排序。（✅ 活跃）
- [dsh-web-novel-research](https://github.com/canghai666x/dsh-web-novel-research) ⭐3 — 中文网文情节查证技能：免费镜像站流程，GBK 解码与跨卷重复章节消歧。（✅ 活跃）
- [deepseek-harness-skillx](https://github.com/drowned-fish1/deepseek-harness-skillx) ⭐2 — DSH 工作流技能合集。（✅ 活跃）
- [dsh-kb-sieve](https://github.com/omdsh-dev/dsh-kb-sieve) ⭐2 — DSH knowledge-base plugin: build audit-able KB packs (references + SQLite FTS5) from md/txt/docx/pdf, deterministic retrieval (kb_query) and original-text reading (kb_read), zero-script generated skills. Apache-2.0.（✅ 活跃）
- [dsh-ponytail](https://github.com/gongyijie85/dsh-ponytail) ⭐2 — Ponytail 最懒资深工程师模式：6 个技能，改编自 DietrichGebert/ponytail。（✅ 活跃）
- [dsh-review-skills](https://github.com/ben7am1n/dsh-review-skills) ⭐2 — DSH 代码评审技能集。（✅ 活跃）
- [dsh-skill-pack-security](https://github.com/PerryLink/dsh-skill-pack-security) ⭐2 — 安全审计技能包：5 个 Agent 技能，覆盖密钥扫描、依赖审计等。（✅ 活跃）
- [dsh-skillport](https://github.com/Jesse-njx/dsh-skillport) ⭐2 — 让 Claude Code、Codex、Cursor、Gemini CLI 已有的技能在 DSH 中直接可用。（✅ 活跃）
- [mattpocock-skills-dsh](https://github.com/gongyijie85/mattpocock-skills-dsh) ⭐2 — Matt Pocock 完整发布技能集（25 个 SKILL.md：grilling、writing-for-agents、wait-what、TDD、code-review、wayfinder、ask-matt 路由等）的 DSH 移植。（✅ 活跃）
- [howto-dsh](https://github.com/dshworks/howto-dsh) ⭐1 — Verified field notes for DeepSeek Harness (dsh): traps, skills, hooks, profiles. Every claim dated against a dsh version, with source paths to re-verify. Not affiliated with DeepSeek.（✅ 活跃）
- [mattpocock-skills-dsh-zh](https://github.com/gongyijie85/mattpocock-skills-dsh-zh) ⭐1 — Matt Pocock 25 个技能正文全译中文（技术术语保留英文并附注释）。（✅ 活跃）
- [dsh-news-briefing](https://github.com/canghai666x/dsh-news-briefing)  — 新闻简报技能：多维故事评分、反标题党规则、内容优先级与中文编辑风格。（✅ 活跃）
- [mstar-workflow](https://github.com/btspoony/mstar-workflow)  — A Skill-driven Harness/Loop Engineering Workflow Agent Plugin（💤 停更）

### Workflows & Automation


#### 🔥 Top 10

| # | 项目 | 星数 | 说明 | 状态 |
|---|---|---|---|---|
| 1 | [tongflow](https://github.com/tong-io/tongflow) | ⭐902 | TongFlow — multimodal workflow studio and engine (canvas + Python plugin engine) and dsh-tongflow, the DeepSeek Harness studio plugin | ✅ 活跃 |
| 2 | [dsh-agent-team-gui](https://github.com/toolclub/dsh-agent-team-gui) | ⭐159 | Persistent multi-model workflow teams for DeepSeek Harness — dynamic lead planning, bounded DAGs, per-agent model/tools, Run Center and Token insights. | ✅ 活跃 |
| 3 | [dsh_workflow](https://github.com/omdsh-dev/dsh_workflow) | ⭐92 | 把Claude Code的UltraCode模式带给DSH，把 DSH 的一次性多 Agent 调度，升级为可生成、可保存、可治理、可观察、可恢复的 Workflow 层 | ✅ 活跃 |
| 4 | [dsh_workflow](https://github.com/icetomoyo/dsh_workflow) | ⭐92 | 把 Claude Code 的 UltraCode 模式带给 DSH：将一次性多 Agent 调度升级为可生成、可保存、可治理、可观察、可恢复的 Workflow 层。 | ✅ 活跃 |
| 5 | [dsh-plugin-agent-workflow](https://github.com/xuanyuanzhifeng/dsh-plugin-agent-workflow) | ⭐78 | DeepSeek Harness Agent Workflow | ✅ 活跃 |
| 6 | [dsh-automation](https://github.com/titanwings/dsh-automation) | ⭐70 | 让 Coding 任务按计划在全新 Agent Session 中运行，由用户或 Agent 创建和管理定时任务。 | ✅ 活跃 |
| 7 | [mstar-harness](https://github.com/btspoony/mstar-harness) | ⭐52 | 技能驱动的 Harness/Loop 工程工作流 Agent：把 Agent 循环调优作为一等工作流。 | ✅ 活跃 |
| 8 | [dsh-plans](https://github.com/Optim-Agent/dsh-plans) | ⭐42 | 从 prime-plans 移植的人机协同规划预设：调研、评审、执行。 | ✅ 活跃 |
| 9 | [dsh-auto-continue](https://github.com/HsiangNianian/dsh-auto-continue) | ⭐33 | 自动恢复中断的请求：失败分类、自适应退避重试、可配置续写消息与浏览器通知。 | ✅ 活跃 |
| 10 | [dsh-deep-research](https://github.com/omdsh-dev/dsh-deep-research) | ⭐18 | 基于官方 workflow 引擎的自适应深度研究编排器。 | ✅ 活跃 |

#### 完整列表（30）

- [tongflow](https://github.com/tong-io/tongflow) ⭐902 — TongFlow — multimodal workflow studio and engine (canvas + Python plugin engine) and dsh-tongflow, the DeepSeek Harness studio plugin（✅ 活跃）
- [dsh-agent-team-gui](https://github.com/toolclub/dsh-agent-team-gui) ⭐159 — Persistent multi-model workflow teams for DeepSeek Harness — dynamic lead planning, bounded DAGs, per-agent model/tools, Run Center and Token insights.（✅ 活跃）
- [dsh_workflow](https://github.com/omdsh-dev/dsh_workflow) ⭐92 — 把Claude Code的UltraCode模式带给DSH，把 DSH 的一次性多 Agent 调度，升级为可生成、可保存、可治理、可观察、可恢复的 Workflow 层（✅ 活跃）
- [dsh_workflow](https://github.com/icetomoyo/dsh_workflow) ⭐92 — 把 Claude Code 的 UltraCode 模式带给 DSH：将一次性多 Agent 调度升级为可生成、可保存、可治理、可观察、可恢复的 Workflow 层。（✅ 活跃）
- [dsh-plugin-agent-workflow](https://github.com/xuanyuanzhifeng/dsh-plugin-agent-workflow) ⭐78 — DeepSeek Harness Agent Workflow（✅ 活跃）
- [dsh-automation](https://github.com/titanwings/dsh-automation) ⭐70 — 让 Coding 任务按计划在全新 Agent Session 中运行，由用户或 Agent 创建和管理定时任务。（✅ 活跃）
- [mstar-harness](https://github.com/btspoony/mstar-harness) ⭐52 — 技能驱动的 Harness/Loop 工程工作流 Agent：把 Agent 循环调优作为一等工作流。（✅ 活跃）
- [dsh-plans](https://github.com/Optim-Agent/dsh-plans) ⭐42 — 从 prime-plans 移植的人机协同规划预设：调研、评审、执行。（✅ 活跃）
- [dsh-auto-continue](https://github.com/HsiangNianian/dsh-auto-continue) ⭐33 — 自动恢复中断的请求：失败分类、自适应退避重试、可配置续写消息与浏览器通知。（✅ 活跃）
- [dsh-deep-research](https://github.com/omdsh-dev/dsh-deep-research) ⭐18 — 基于官方 workflow 引擎的自适应深度研究编排器。（✅ 活跃）
- [dsh-harness-ops](https://github.com/fakechris/dsh-harness-ops) ⭐11 — 运维工具箱：官方每日快照 A/B 双槽轮换、原子切换、一键回滚、守护进程自动拉起。（✅ 活跃）
- [dsh-plannotator](https://github.com/titanwings/dsh-plannotator) ⭐10 — DSH 计划批注插件：选中计划原文、逐条批注，并把结构化反馈送回 Agent。 / A DSH plan-review plugin for anchored annotations and structured Agent feedback.（✅ 活跃）
- [dsh-deepresearch](https://github.com/havingautism/dsh-deepresearch) ⭐9 — 面向 Harness 的 DeepResearch 插件（cordis）。（🧪 实验性）
- [dsh-inspect](https://github.com/omdsh-dev/dsh-inspect) ⭐6 — 发现问题(checkup) → 修复交付(fix) → 质量复查(review) 的对抗式闭环。（✅ 活跃）
- [dsh-plugin-spur](https://github.com/HuanLinOTO/dsh-plugin-spur) ⭐6 — 聊天流中悬挂皮鞭：甩动鞭梢即向 agent 发送 go work 消息（整活）。（✅ 活跃）
- [dsh-task-dag](https://github.com/LeemanCheung/dsh-task-dag) ⭐6 — 工作流运行、子代理、状态与依赖的持久化实时 DAG 可视化。（✅ 活跃）
- [dsh-track](https://github.com/fakechris/dsh-track) ⭐6 — 嵌入式任务管理引擎：决策点协议、念头捕获墙、Linear 形 issue 存储。（✅ 活跃）
- [engineer-software](https://github.com/KirschBluteX/engineer-software) ⭐6 — 与运行时无关、证据驱动的软件工程工作流，适用于 Codex 与 DeepSeek Harness。（✅ 活跃）
- [dsh-companion](https://github.com/william-jin-cmu/dsh-companion) ⭐5 — 常驻桌面助手：全局唤起、定时自动化、快捷回复、插件市场。（💤 停更）
- [dsh-loop](https://github.com/vlln/dsh-loop) ⭐5 — DSH 插件：定时循环（/loop 命令 + loop 工具 + 活动状态条）。官方 bundle 插件，dsh plugin --profile web add 安装（✅ 活跃）
- [dsh-continual-harness](https://github.com/jasen215/dsh-continual-harness) ⭐4 — DeepSeek Harness plugin for continual self-evolution: persistent memory, periodic review-and-refine, cross-session shared knowledge, and automatic rollback — a plan→validate→apply→rollback loop driven by a model-callable harness_refine tool.（✅ 活跃）
- [dsh-doublecheck](https://github.com/PerryLink/dsh-doublecheck) ⭐4 — 工程纪律循环：编辑前需求拷问、红/绿测试证据门、对抗式交付审查。（✅ 活跃）
- [dsh-prime-agent](https://github.com/yoke233/dsh-prime-agent) ⭐4 — Prime Agent 启发的持久 RLM 控制平面，面向 DSH Code 模式。（✅ 活跃）
- [dsh-tool-time](https://github.com/omdsh-dev/dsh-tool-time) ⭐4 — DSH 时间工具插件：严格 ISO 8601 解析、IANA 时区转换、UTC 日历运算、固定时长差，零依赖（✅ 活跃）
- [dsh-agent-orchestration](https://github.com/LeslieWylie/dsh-agent-orchestration) ⭐3 — Evidence-first multi-agent workflow planning, handoff validation, and Loop Guard skills for DeepSeek Harness.（💤 停更）
- [dsh-eval](https://github.com/hccccc01333/dsh-eval) ⭐1 — Agent 评测平台：benchmark YAML、无头 dsh 运行、基于 trace 的指标、脚本评分与运行对比。（✅ 活跃）
- [dsh-governance](https://github.com/tappass/dsh-governance) ⭐1 — Agentic AI 的权威层插件：按你的策略治理每次工具调用。（✅ 活跃）
- [dsh-report-studio](https://github.com/ciceroyang/dsh-report-studio) ⭐1 — 把 DSH 会话变成可交付工作报告（日报/周报/交接/文章），带可验证凭证。（✅ 活跃）
- [dsh-trajectory-debug](https://github.com/devmom/dsh-trajectory-debug) ⭐1 — 轨迹瀑布流、确定性回放、断点、编辑重跑、fork 对比与性能分析。（✅ 活跃）
- [dsh-plugin-skill](https://github.com/dsh-io/dsh-plugin-skill)  — Agent skill (SKILL.md) for creating DeepSeek Harness (dsh) plugins: authoritative defineTool API, schema rules, project layout and workflow — works with Claude Code, Codex, Cursor, Gemini CLI, opencode（✅ 活跃）

### Agents & Multi-Agent


#### 🔥 Top 10

| # | 项目 | 星数 | 说明 | 状态 |
|---|---|---|---|---|
| 1 | [openbiliclaw](https://github.com/whiteguo233/OpenBiliClaw) | ⭐2,971 | 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin） | ✅ 活跃 |
| 2 | [dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) | ⭐746 | 面向团队的 DSH 多 Agent 扩展。 | ✅ 活跃 |
| 3 | [dsh-univer-office](https://github.com/dream-num/dsh-univer-office) | ⭐191 | Give DeepSeek Harness a real office environment.  Univer Office Plugin brings spreadsheets, docs, slides, canvases, relational tables, and more into one runtime — with connected data, validation, versioned changes, and isolated worktrees for multi-agent collaboration. | ✅ 活跃 |
| 4 | [dsh-agent-rp](https://github.com/hewzhew/dsh-agent-rp) | ⭐169 | SillyTavern 迁移与下一代 Agent 角色扮演。 | ✅ 活跃 |
| 5 | [dsh-auto-review](https://github.com/PerryLink/dsh-auto-review) | ⭐116 | Second-model AI auto-review for DeepSeek Harness approval requests: a read-only reviewer subagent returns structured allow/deny verdicts with reasons, fail-closed by default, fully auditable from the session log (approval/asked -> autoReview/verdict -> approval/decided). | ✅ 活跃 |
| 6 | [dsh-data-agent](https://github.com/omdsh-dev/dsh-data-agent) | ⭐104 | 会话级数据库连接 + 专用数据 Agent：让模型连数据库、写 SQL。 | ✅ 活跃 |
| 7 | [dsh-openbiliclaw](https://github.com/whiteguo233/dsh-openbiliclaw) | ⭐48 | OpenBiliClaw 是本地运行的跨平台个性化内容推荐 Agent，持续理解你的兴趣并主动找内容。本仓库是它的 DeepSeek Harness 插件：DSH 界面常驻第四栏（推荐/内容库/对话/画像/设置），注册 22 个 Agent Bridge 工具，让 Agent 也能读推荐、答探测、闭环学习。 | ✅ 活跃 |
| 8 | [allinluna](https://github.com/zenx0x/allinluna) | ⭐41 | 面向 Codex 与 DeepSeek Harness 的资源感知多 Agent 编排。 | ✅ 活跃 |
| 9 | [dsh-tianshu-build](https://github.com/huiliyi37/dsh-tianshu-build) | ⭐36 | DeepSeek X Tianshu  Harness build 是一款完全体开源 coding agent:在 dsh harness 基础之上带视觉、跨会话记忆、验证门、agent 路由、语义 + 图谱代码检索、文件回滚和全屏终端 UI——全部以插件组合。  它是 DeepSeek Harness(dsh)的友好 MIT fork, 它保留了上游一切皆插件的架构，并将以harness最佳形态和架构往下演进。 | ✅ 活跃 |
| 10 | [dsh-interconnect](https://github.com/Chinesezjc/dsh-interconnect) | ⭐34 | 跨实例消息/事件交接插件（interconnect 服务 + 工具）。 | ✅ 活跃 |

#### 完整列表（28）

- [openbiliclaw](https://github.com/whiteguo233/OpenBiliClaw) ⭐2,971 — 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin）（✅ 活跃）
- [dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) ⭐746 — 面向团队的 DSH 多 Agent 扩展。（✅ 活跃）
- [dsh-univer-office](https://github.com/dream-num/dsh-univer-office) ⭐191 — Give DeepSeek Harness a real office environment.  Univer Office Plugin brings spreadsheets, docs, slides, canvases, relational tables, and more into one runtime — with connected data, validation, versioned changes, and isolated worktrees for multi-agent collaboration.（✅ 活跃）
- [dsh-agent-rp](https://github.com/hewzhew/dsh-agent-rp) ⭐169 — SillyTavern 迁移与下一代 Agent 角色扮演。（✅ 活跃）
- [dsh-auto-review](https://github.com/PerryLink/dsh-auto-review) ⭐116 — Second-model AI auto-review for DeepSeek Harness approval requests: a read-only reviewer subagent returns structured allow/deny verdicts with reasons, fail-closed by default, fully auditable from the session log (approval/asked -> autoReview/verdict -> approval/decided).（✅ 活跃）
- [dsh-data-agent](https://github.com/omdsh-dev/dsh-data-agent) ⭐104 — 会话级数据库连接 + 专用数据 Agent：让模型连数据库、写 SQL。（✅ 活跃）
- [dsh-openbiliclaw](https://github.com/whiteguo233/dsh-openbiliclaw) ⭐48 — OpenBiliClaw 是本地运行的跨平台个性化内容推荐 Agent，持续理解你的兴趣并主动找内容。本仓库是它的 DeepSeek Harness 插件：DSH 界面常驻第四栏（推荐/内容库/对话/画像/设置），注册 22 个 Agent Bridge 工具，让 Agent 也能读推荐、答探测、闭环学习。（✅ 活跃）
- [allinluna](https://github.com/zenx0x/allinluna) ⭐41 — 面向 Codex 与 DeepSeek Harness 的资源感知多 Agent 编排。（✅ 活跃）
- [dsh-tianshu-build](https://github.com/huiliyi37/dsh-tianshu-build) ⭐36 — DeepSeek X Tianshu  Harness build 是一款完全体开源 coding agent:在 dsh harness 基础之上带视觉、跨会话记忆、验证门、agent 路由、语义 + 图谱代码检索、文件回滚和全屏终端 UI——全部以插件组合。  它是 DeepSeek Harness(dsh)的友好 MIT fork, 它保留了上游一切皆插件的架构，并将以harness最佳形态和架构往下演进。（✅ 活跃）
- [dsh-interconnect](https://github.com/Chinesezjc/dsh-interconnect) ⭐34 — 跨实例消息/事件交接插件（interconnect 服务 + 工具）。（✅ 活跃）
- [dsh-plugin-cc](https://github.com/cpj-dev/dsh-plugin-cc) ⭐29 — 将 DSH 桥接到 Claude Code：审查、批判、委托与会话导入。（✅ 活跃）
- [kixparadigm](https://github.com/olicesx/kixparadigm) ⭐23 — kixparadigm — AI self-orchestrated minimal paradigm (resident cognition layer) + kixpower multi-agent orchestration · one-command import into DeepSeek Harness (npm i -g) / AI 自编排最小范式（认知层常驻）× kixpower 多智能体编排 · npm 一键导入 DeepSeek Harness（✅ 活跃）
- [dsh-plugin-product-subagents](https://github.com/shaokeyibb/dsh-plugin-product-subagents) ⭐17 — 基于角色的 Codex/Claude Code/ACP 子代理提供方：可延续的子任务，带持久状态。（✅ 活跃）
- [dsh-plugin-yet-another-subagent](https://github.com/HuanLinOTO/dsh-plugin-yet-another-subagent) ⭐12 — 可配置子代理 profile 系统：单一 subagent 工具 + profile 参数，含 Web UI 设置与实时进度。（✅ 活跃）
- [dsh-sidechain](https://github.com/omdsh-dev/dsh-sidechain) ⭐10 — 侧会话：/side 持续性侧会话（Codex 风格）与 /btw 一次性侧问（Claude 风格），临时 fork 中运行。（✅ 活跃）
- [dsh-plugin-claude-bridge](https://github.com/YYTbit/dsh-plugin-claude-bridge) ⭐9 — 把 Claude Code 的记忆、技能与配置桥接到 DSH。（✅ 活跃）
- [Task Passport](https://github.com/dongsheng123132/task-passport) ⭐9 — 跨编码 Agent 环境的开放任务交接协议：交接可验证的状态而非聊天记录。（✅ 活跃）
- [dsh-background-agents](https://github.com/PerryLink/dsh-background-agents) ⭐7 — Interactive long-session background agents for DeepSeek Harness: start a durable continuable child agent, watch its progress in the Web UI sidebar, message it any time, and interrupt it - all through the official subagent seam.（✅ 活跃）
- [dsh-ha-orchestrator](https://github.com/Saktawdi/dsh-ha-orchestrator) ⭐7 — DeepSeek Harness（dsh）动态 Cordis 插件：模型高可用回退 + 五种模式子智能体编排（fanout / pipeline / supervisor / map-reduce / router）（✅ 活跃）
- [dsh-a2a](https://github.com/dpskh/dsh-a2a) ⭐6 — 面向 Harness 的 Agent2Agent 网状网络。（✅ 活跃）
- [dsh-reasoning-settings](https://github.com/JuneLearn/dsh-reasoning-settings) ⭐6 — 让 DeepSeek Harness 的第三方 API 支持低、中、高等推理强度，并可为每次子 Agent 调用选择模型｜Add Low, Medium, High, and other reasoning levels to third-party APIs, with model selection for each subagent call（✅ 活跃）
- [dsh-agent-messaging](https://github.com/happyren/dsh-agent-messaging) ⭐5 — 跨会话 Agent 互发消息：按名称寻址其他会话。（✅ 活跃）
- [dsh-crosstalk](https://github.com/Jesse-njx/dsh-crosstalk) ⭐2 — 跨会话消息：同机 DSH 会话之间可发现、互发消息并协同。（✅ 活跃）
- [dsh-slice-agent-loop](https://github.com/TT-Wang/dsh-slice-agent-loop) ⭐2 — 可替换的 Agent 循环：上下文引擎是有界切片而非不断增长的记录。（✅ 活跃）
- [dsh-subagent-tools](https://github.com/lynx-gt/dsh-subagent-tools) ⭐2 — 子代理委托的逐调用模型/provider/persona/toolFilter 覆盖，支持 @preset 引用。（✅ 活跃）
- [dsh-swarm-router](https://github.com/r600a-code/dsh-swarm-router) ⭐2 — DSH plugin: sub-agent matrix swarm — routes heterogeneous tasks to the most suitable model (OpenRouter-like + cfgpu.com/llm/square), dispatches each via in-process subagents. 32/32 benchmark green.（✅ 活跃）
- [dsh-cross-session](https://github.com/Wha1eChai/dsh-cross-session) ⭐1 — 同运行时跨会话发现与通信。（✅ 活跃）
- [dsh-supervisor](https://github.com/Wha1eChai/dsh-supervisor) ⭐1 — 同运行时跨会话发现与通信。（✅ 活跃）

### Clients (Desktop & TUI)


#### 🔥 Top 10

| # | 项目 | 星数 | 说明 | 状态 |
|---|---|---|---|---|
| 1 | [open-design](https://github.com/nexu-io/open-design) | ⭐90,033 | 🎨 The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode / Hermes & 20+ CLIs via BYOK. | ✅ 活跃 |
| 2 | [deepseek-harness-desktop (Anywhere Labs)](https://github.com/anywhere-labs/deepseek-harness-desktop) | ⭐17,280 | 为 DeepSeek Harness 生态打造的现代化桌面端体验（插件）。 | ✅ 活跃 |
| 3 | [desktop-cc-gui](https://github.com/zhukunpenglinyutong/desktop-cc-gui) | ⭐4,058 | Multi-engine AI coding desktop client (Tauri). Claude Code, Codex, Gemini, OpenCode, DeepSeek Harness and more in one GUI. | ✅ 活跃 |
| 4 | [echobird](https://github.com/edison7009/EchoBird) | ⭐3,105 | One-click install + model switch:Claude Code,Codex CLI (OpenAI), Grok Build (xAI), DeepSeek Harness, Kimi Code (Moonshot) ,Qwen Code,Aider,OpenCode,MiMo Code (Xiaomi),ZCode (Z.AI),OpenClaw,Pi,OpenScience,Vibe-Trading,Claude Desktop (3P profile),ChatGPT desktop,OpenCode Desktop, | ✅ 活跃 |
| 5 | [dsh-cc-tui](https://github.com/ccch1mneyyy/dsh-TUI) | ⭐2,680 | DSH 官方公众号收录的 TUI 补位插件：Claude Code 风，鲸鱼顶栏/实时状态/流式思考/双击 Esc 回滚/上下文进度+TPS。npm 一键装。  DSH official WeChat featured TUI plugin — Claude Code style: whale bar, live status, streaming thoughts, double-Esc rollback, context bar + TPS. npm one-click. | ✅ 活跃 |
| 6 | [dsh-desktop (DataElement)](https://github.com/dataelement/dsh-desktop) | ⭐1,511 | DeepSeek Harness 桌面应用。 | ✅ 活跃 |
| 7 | [deepseek-harness-eac](https://github.com/zouyuxuan122/Deepseek-Harness-EAC) | ⭐1,067 | DeepSeek Harness (dsh) Windows desktop client - bundled Node.js + dsh CLI, one-click launch, 10 built-in UI skins. EAC: Embracing All Creation 揽尽万象 | ✅ 活跃 |
| 8 | [deepseek-harness-desktop (hairyf)](https://github.com/hairyf/deepseek-harness-desktop) | ⭐814 | 一键桌面应用：全本地运行，核心自愈更新，零环境配置。Win/macOS/Linux。 | ✅ 活跃 |
| 9 | [deepseek-harness-desktop-app](https://github.com/vibeinging/deepseek-harness-desktop-app) | ⭐610 | DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts. | ✅ 活跃 |
| 10 | [dsh-work](https://github.com/vibeinging/dsh-work) | ⭐610 | Local-first AI workbench for DSH Plugins, combining Agent sessions, project files, data analysis, web research, MCP, and Office artifacts in an Electron desktop app. | ✅ 活跃 |

#### 完整列表（81）

- [open-design](https://github.com/nexu-io/open-design) ⭐90,033 — 🎨 The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, slides, images & video — real files, HTML/PDF/PPTX/MP4 export. 🤖 Claude Code / Codex / Cursor / DeepSeek Harness / OpenCode / Hermes & 20+ CLIs via BYOK.（✅ 活跃）
- [deepseek-harness-desktop (Anywhere Labs)](https://github.com/anywhere-labs/deepseek-harness-desktop) ⭐17,280 — 为 DeepSeek Harness 生态打造的现代化桌面端体验（插件）。（✅ 活跃）
- [desktop-cc-gui](https://github.com/zhukunpenglinyutong/desktop-cc-gui) ⭐4,058 — Multi-engine AI coding desktop client (Tauri). Claude Code, Codex, Gemini, OpenCode, DeepSeek Harness and more in one GUI.（✅ 活跃）
- [echobird](https://github.com/edison7009/EchoBird) ⭐3,105 — One-click install + model switch:Claude Code,Codex CLI (OpenAI), Grok Build (xAI), DeepSeek Harness, Kimi Code (Moonshot) ,Qwen Code,Aider,OpenCode,MiMo Code (Xiaomi),ZCode (Z.AI),OpenClaw,Pi,OpenScience,Vibe-Trading,Claude Desktop (3P profile),ChatGPT desktop,OpenCode Desktop,（✅ 活跃）
- [dsh-cc-tui](https://github.com/ccch1mneyyy/dsh-TUI) ⭐2,680 — DSH 官方公众号收录的 TUI 补位插件：Claude Code 风，鲸鱼顶栏/实时状态/流式思考/双击 Esc 回滚/上下文进度+TPS。npm 一键装。  DSH official WeChat featured TUI plugin — Claude Code style: whale bar, live status, streaming thoughts, double-Esc rollback, context bar + TPS. npm one-click.（✅ 活跃）
- [dsh-desktop (DataElement)](https://github.com/dataelement/dsh-desktop) ⭐1,511 — DeepSeek Harness 桌面应用。（✅ 活跃）
- [deepseek-harness-eac](https://github.com/zouyuxuan122/Deepseek-Harness-EAC) ⭐1,067 — DeepSeek Harness (dsh) Windows desktop client - bundled Node.js + dsh CLI, one-click launch, 10 built-in UI skins. EAC: Embracing All Creation 揽尽万象（✅ 活跃）
- [deepseek-harness-desktop (hairyf)](https://github.com/hairyf/deepseek-harness-desktop) ⭐814 — 一键桌面应用：全本地运行，核心自愈更新，零环境配置。Win/macOS/Linux。（✅ 活跃）
- [deepseek-harness-desktop-app](https://github.com/vibeinging/deepseek-harness-desktop-app) ⭐610 — DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts.（✅ 活跃）
- [dsh-work](https://github.com/vibeinging/dsh-work) ⭐610 — Local-first AI workbench for DSH Plugins, combining Agent sessions, project files, data analysis, web research, MCP, and Office artifacts in an Electron desktop app.（✅ 活跃）
- [dsh_desktop](https://github.com/myYangyunfan/dsh_desktop) ⭐521 — DeepSeek Harness (dsh) Windows desktop client - bundled Node.js + dsh CLI, one-click launch（✅ 活跃）
- [deepseek-harness-studio](https://github.com/fufankeji/deepseek-harness-studio) ⭐426 — DeepSeek Harness 零代码桌面端｜一键启动，支持 Windows 与 macOS；内置插件发现、热点插件推送、一键安装与管理、AI 智能推荐和视觉增强。（✅ 活跃）
- [ai-novel-writer](https://github.com/EthanYoQ/AI-Novel-Writer) ⭐422 — 本地优先 AI 小说创作工作台，提供 Windows/macOS 桌面版与 DeepSeek Harness 插件开发预览，支持角色、大纲、章节蓝图、审稿修稿和本地模型。（✅ 活跃）
- [dsh-dafeiyu](https://github.com/QCYTSN/dsh-dafeiyu) ⭐272 — Desktop-native BigFish companion for DeepSeek Harness — real Agent status, always on top on Windows.（✅ 活跃）
- [oh-dsh](https://github.com/hust-open-atom-club/oh-dsh) ⭐256 — 一站式社区发行版：TUI、桌面端与 Web UI 三种形态统一体验，分层安装。（✅ 活跃）
- [dsh-tianshu-tui](https://github.com/huiliyi37/dsh-tianshu-tui) ⭐226 — DSH 交互式终端 UI 插件：在官方基础上增加 TDD、证据门、视觉图像模块等工作流。（✅ 活跃）
- [dsh-launcher](https://github.com/Ruler4396/dsh-launcher) ⭐165 — 轻量 Windows 启动器：登录静默自启 + 极简 WebView2 窗口。（✅ 活跃）
- [deepseek-harness-desktop (ningbainb)](https://github.com/ningbainb/deepseek-harness-desktop) ⭐157 — 无损 Windows 桌面应用：完整 DSH Web UI、插件、皮肤与技能停靠栏。（✅ 活跃）
- [deepseek-harness-desktop (steven-kid)](https://github.com/steven-kid/deepseek-harness-desktop) ⭐157 — 极简跨平台桌面端：免配置，开箱即用。（✅ 活跃）
- [deepseek-harness-desktop (salathleizhang)](https://github.com/salathleizhang/deepseek-harness-desktop) ⭐138 — DeepSeek Harness 桌面封装。（✅ 活跃）
- [Deepseek-Harness-Desktop (ChisaAlter)](https://github.com/ChisaAlter/Deepseek-Harness-Desktop) ⭐131 — Electron 桌面壳：支持主题与背景图等多种个性化配置。（✅ 活跃）
- [dshcode](https://github.com/whitelonng/dshcode) ⭐126 — Community desktop companion for DeepSeek Harness — one-click Electron app for macOS and Windows（✅ 活跃）
- [dsh-launcher](https://github.com/MarcoG-h/DSH-Launcher) ⭐125 — 最全面的DeepSeek Harness🐋桌面启动器&第三方插件管理   | 离线部署 | 一键启动 | 插件管理 | API切换 |（✅ 活跃）
- [deepseek-harness-remote](https://github.com/liguobao/deepseek-harness-remote) ⭐124 — 基于 DeepSeek Harness 插件机制的多端远程访问方案，让桌面端与 Android 端安全连接并操作远程 Harness。（A multi-device remote access solution built on the DeepSeek Harness plugin system, enabling desktop and Android clients to securely connect to and operate a remote Harness.）（✅ 活跃）
- [dsh-mobile](https://github.com/saya-ch/dsh-mobile) ⭐79 — DeepSeek Harness 移动端适配与安全局域网访问插件，支持 Android App 和手机浏览器。（✅ 活跃）
- [DeepSeekHarnessDesktop (wess09)](https://github.com/wess09/DeepSeekHarnessDesktop) ⭐66 — DeepSeek Harness 桌面端打包。（✅ 活跃）
- [dsh-desktop (bruc3van)](https://github.com/bruc3van/dsh-desktop) ⭐66 — 第三方桌面客户端：直接加载官方 Web UI，可复用本机实例或内置 dsh 运行时。（✅ 活跃）
- [Martty](https://github.com/openma-ai/Martty) ⭐66 — 面向 DeepSeek Harness 的 Rust/ratatui Agent TUI，支持流式工具调用、子代理、持久会话和可扩展的 Cordis 客户端界面（deepseek-harness-tui 的继任者）。（✅ 活跃）
- [dsh-multica-runtime](https://github.com/multica-ai/dsh-multica-runtime) ⭐53 — 在 Multica 上支持 dsh 运行时。（✅ 活跃）
- [beauticode](https://github.com/starsstreaming/beautiCode) ⭐51 — 面向 AI 编程客户端的动态、可响应环境——视频背景、氛围场景与主题，适用于 DeepSeek Harness 与 Codex Desktop。（✅ 活跃）
- [deepseek-harness-desktop (xiincs)](https://github.com/xiincs/deepseek-harness-desktop) ⭐49 — 基于 Tauri 2 的原生桌面版：内置 Node.js 运行时，托盘常驻，自动更新。（✅ 活跃）
- [DeepSeek Harness TUI (openma-ai)](https://github.com/openma-ai/deepseek-harness-tui) ⭐46 — Rust/Ratatui 终端客户端，直接与 DSH 的 SDK JSON-RPC 协议通信。（✅ 活跃）
- [dsh-plugin-dev-skills](https://github.com/zimodzh/dsh-plugin-dev-skills) ⭐38 — An Agent Skills skill for developing DeepSeek Harness (DSH) plugins（开发 DSH 插件的 Agent Skill）——插件/服务/事件/工具/LLM 适配器/打包安装的标准。Works with Claude Code, Codex, DSH, VS Code Copilot & any compatible agent.（✅ 活跃）
- [deepseek-harness-desktop (hongfeiyucode)](https://github.com/hongfeiyucode/deepseek-harness-desktop) ⭐37 — DeepSeek Harness 桌面封装。（✅ 活跃）
- [deepseek-harness-termux](https://github.com/Vengisk/deepseek-harness-termux) ⭐37 — 在 Android/Termux 上运行 DeepSeek Harness。（✅ 活跃）
- [dsh-usage-plugin](https://github.com/feiyang-dev/dsh-usage-plugin) ⭐33 — DeepSeek Harness 用量与消耗插件（dsh-usage）—— 每次调用的 token 用量/缓存命中统计、峰谷计费、余额查询、CSV/JSON/PNG 导出，可经桌面端一键安装或命令行 dsh plugin add 安装。（✅ 活跃）
- [deepseek-harness-app (ipfred)](https://github.com/ipfred/deepseek-harness-app) ⭐29 — DeepSeek Harness 桌面应用。（✅ 活跃）
- [dsh-plugin-session-delete](https://github.com/lsz-asd/dsh-plugin-session-delete) ⭐26 — Delete DeepSeek Harness sessions from the UI: header danger button + sidebar session-row menu item (no conversation jump), risk-consent dialog with session name/id, stops running agents first, in-place list refresh without page reload. Works in web and the desktop client.（✅ 活跃）
- [dsh-tui](https://github.com/dsh-tui/dsh-tui) ⭐24 — Claude Code-style terminal UI for DeepSeek Harness agents, as an out-of-tree dsh plugin bundle（✅ 活跃）
- [dsh-mobile](https://github.com/lehhair/dsh-mobile) ⭐21 — Mobile client plugin (cordis + dsh.plugin.json).（✅ 活跃）
- [dsh-studio](https://github.com/Moresyl/dsh-studio) ⭐20 — DeepSeek Harness 原生桌面端 · Linux / macOS / Windows · Rust + Tauri（✅ 活跃）
- [deepseek-harness-desktop (cc1252)](https://github.com/cc1252/deepseek-harness-desktop) ⭐19 — 非官方 Windows Electron 封装。（✅ 活跃）
- [DeepSeek-Harness-Desktop (sleep2agi)](https://github.com/sleep2agi/DeepSeek-Harness-Desktop) ⭐19 — 社区桌面壳。（✅ 活跃）
- [deepseek-harness-fnos](https://github.com/techysy/deepseek-harness-fnos) ⭐18 — DeepSeek Harness (DeepSeek 官方 agent 浏览器 UI) fnOS 应用 — 本地常驻服务, 官方统一网关接入（✅ 活跃）
- [dsh-melody-launcher](https://github.com/rirko/dsh-melody-launcher) ⭐16 — dsh-旋律启动器：DeepSeek Harness 桌面启动器与插件管理器（✅ 活跃）
- [dshcockpit](https://github.com/Lxiayu/DshCockpit) ⭐16 — DshCockpit — DeepSeek Harness 桌面驾驶舱 (desktop cockpit)：运行时自动更新、成本控制、全局快捷问询、定时任务、会话全文检索、数据安全。自动更新 / 成本中心 / Quick Ask / 定时任务 / 会话搜索（✅ 活跃）
- [dsh-mobile-for-android](https://github.com/Hongtwenfive1226/DSH-Mobile-for-Android) ⭐12 — The Android mobile version of DeepSeek Harness that relies on Tailscale.（✅ 活跃）
- [dsh-grok-tui](https://github.com/chen-001/dsh-grok-tui) ⭐11 — 基于 grok-build 构建的 TUI。（✅ 活跃）
- [awesome-deepseek-harness-desktop (ADHD)](https://github.com/omdsh-dev/awesome-deepseek-harness-desktop) ⭐10 — ADHD — 开箱即用的 Electron 桌面封装。（✅ 活跃）
- [deepseek-harness-desktop](https://github.com/qyqy-1109/deepseek-harness-desktop) ⭐10 — DeepSeek Harness Desktop: self-contained Windows desktop shell (Electron) that auto-starts dsh web, plus a subtle Codex-flavored theme plugin.（✅ 活跃）
- [deepseek-harness-desktop (chyra-moon)](https://github.com/chyra-moon/deepseek-harness-desktop) ⭐10 — Windows 原生桌面壳：官方 Web UI 1:1 复刻，内置服务、托盘与自动恢复。（✅ 活跃）
- [deepseek-harness-tui (boxeryao)](https://github.com/boxeryao/deepseek-harness-tui) ⭐10 — 轻量快速终端插件，直连 DSH 运行时。（✅ 活跃）
- [dsh-desktop](https://github.com/foolgry/dsh-desktop) ⭐10 — Download-and-run desktop build of DeepSeek Harness — Electron shell with embedded Node, no npm required.（✅ 活跃）
- [dsh-record-replay](https://github.com/humblebanana/dsh-record-replay) ⭐10 — DeepSeek Harness record macOS desktop workflows by demonstration and turn them into agent skills (open-record-replay skill + orr_* tools)（✅ 活跃）
- [agentpocket](https://github.com/npu-chenlin/AgentPocket) ⭐9 — Android 客户端：通过 Tailscale 在手机上使用 Kimi Code / DeepSeek Harness 等编码 Agent 的 Web 服务（✅ 活跃）
- [deepseek-harness-desktop](https://github.com/baiyuscc13724-max/deepseek-harness-desktop) ⭐9 — Windows desktop app for DeepSeek Harness: installer, themes, in-app plugin marketplace, model routing, and updates.（✅ 活跃）
- [dsh-mobile-gui-agent](https://github.com/kunjinkao-os/dsh-mobile-gui-agent) ⭐9 — Android Mobile GUI Agent plugin for DeepSeek Harness with ADB control, iterative verification, approvals, and a Web mobile view（✅ 活跃）
- [deepseek-harness-desktop](https://github.com/omdsh-dev/deepseek-harness-desktop) ⭐8 — DSH 桌面应用打包器（✅ 活跃）
- [dsh-ux](https://github.com/jiangnanquan/dsh-ux) ⭐8 — DSH web UI 增强插件 + 无边框 Electron 桌面壳（✅ 活跃）
- [deepseek-harness-desktop](https://github.com/RZX00/deepseek-harness-desktop) ⭐7 — DeepSeek Harness with a Windows desktop build: an Electron shell over the dsh web profile, packaged as an installer（✅ 活跃）
- [deepseek-harness-pet](https://github.com/minybear/DeepSeek-Harness-Pet) ⭐7 — Codex-style desktop pet plugin for DeepSeek Harness（✅ 活跃）
- [deepseek-harness-tui (gxinxing)](https://github.com/gxinxing/deepseek-harness-tui) ⭐7 — 基于 Ink（终端 React）构建的终端原生交互 TUI。（✅ 活跃）
- [star-deepseek-harness-desktop](https://github.com/dabaicai001/star-deepseek-harness-desktop) ⭐7 — Star-deepseek-harness-desktop — DeepSeek Harness,一站式桌面运维台。Harness 自动规划并调用数据库 / SSH / SFTP / Docker 执行。本地优先、跨平台。本项目由自研的starhub 做的再次改进，现在改进中... 尽情期待吧，如果想使用老版本可以下载 0.6X.X 版本（✅ 活跃）
- [deepseek-harness-cli](https://github.com/Richard-Yang0130/deepseek-harness-cli) ⭐6 — Claude Code-style terminal interface for DeepSeek Harness（✅ 活跃）
- [deepseek-harness-desktop](https://github.com/HaoyueQin/deepseek-harness-desktop) ⭐6 — A desktop shell for DeepSeek Harness — the pluggable AI agent harness from DeepSeek. Wrap the official dsh web UI into a native-feeling, always-on desktop app. / 为 DeepSeek Harness（DeepSeek 开源的可插拔 AI Agent harness）打造的桌面应用壳，把官方 dsh web 界面包装成原生质感、常驻后台的桌面应用。（✅ 活跃）
- [dsh-codex-pet](https://github.com/skr311/dsh-codex-pet) ⭐6 — dsh-codex-pet · DSH 桌面宠物插件 — 导入精灵图序列帧宠物，悬浮浮层渲染 + Agent 状态联动（✅ 活跃）
- [dsh-desk-pet](https://github.com/anneheartrecord/dsh-desk-pet) ⭐5 — Always-on-top DeepSeek Harness desktop pet. Default whale, four skins, four silent states.（✅ 活跃）
- [dsh-desktop-electron](https://github.com/Void0312Aurora/dsh-desktop-electron) ⭐5 — 跨平台 Electron 桌面壳：托盘常驻独立窗口。（✅ 活跃）
- [deepseek-harness-for-android](https://github.com/standtrain/deepseek-harness-for-android) ⭐4 — 该程序是一个独立的 Capacitor Android 应用，用于管理本机 DeepSeek Harness Ubuntu 用户空间。它提供运行时安装与重置、Ubuntu 终端、可选的 Shizuku 设备 Shell 访问、设置，以及仅限回环地址的内嵌 Harness Web 界面。（✅ 活跃）
- [dsh-closerai](https://github.com/sb1733831438-maker/DSH-closerAI) ⭐4 — CloserAI - a local-first, model-agnostic, permission-transparent desktop AI workbench built on DeepSeek Harness.（✅ 活跃）
- [dsh-launcher-android](https://github.com/qawse110/dsh-launcher-android) ⭐4 — DshLauncher: single-APK Android launcher for DeepSeek Harness with embedded Node runtime（✅ 活跃）
- [dsh-tui](https://github.com/orriduck/dsh-tui) ⭐4 — A small, session-aware terminal UI for DeepSeek Harness（✅ 活跃）
- [deepseek-harness-desktop](https://github.com/Easyhoov/deepseek-harness-desktop-windows) ⭐3 — Unofficial in-process desktop app for DeepSeek Harness: the host composition boots inside the Electron main process with zero ports and an IPC bridge. Not affiliated with DeepSeek.（✅ 活跃）
- [deepseek-harness-workbench](https://github.com/xuan-ao-1/deepseek-harness-workbench) ⭐3 — DeepSeek Harness 官方架构的 Windows 桌面发行版 (Desktop distribution of the official DeepSeek Harness)（✅ 活跃）
- [dsh-vault](https://github.com/feiyang-dev/dsh-vault) ⭐3 — DeepSeek Harness 数据保险箱插件（dsh-vault）—— 自动备份、清空检测、一键恢复，保护聊天记录与工作区数据；可经桌面端一键安装或命令行 dsh plugin add 安装。（✅ 活跃）
- [dsh-pi-tui](https://github.com/lqhl/dsh-pi-tui) ⭐2 — Pi TUI 前端：流式 Markdown、思考折叠、工具卡片、斜杠命令与审批浮层。（✅ 活跃）
- [dsh-portable-launcher](https://github.com/15828148/dsh-portable-launcher) ⭐2 — One-click portable launcher for DeepSeek Harness (dsh) Web UI on Windows. Auto-installs Node.js and dsh with China mirror fallback, 3-stage progress with retries and resume, zero-download fast path when ready. No admin needed.（✅ 活跃）
- [dsh-desktop](https://github.com/xiaowei2025cqu23phy/dsh-desktop) ⭐1 — DeepSeek Harness 桌面客户端:AI 屏保、手机 PWA 遥控(扫码配对)、QQ/Telegram 机器人通道(审批/提问按钮)、模式提示词(工作助手/对话朋友)、壁纸美化等。（✅ 活跃）
- [dsh-desktop-launcher](https://github.com/becomeless/dsh-desktop-launcher)  — Windows/macOS desktop launcher for DeepSeek Harness: double-click to launch, zero console windows, auto-stop on close | 双击图标一键启动 DeepSeek Harness 的桌面启动器（Windows / macOS）（✅ 活跃）
- [dsh-quickstart](https://github.com/qzhqzh/dsh-quickstart)  — Desktop launcher for DeepSeek Harness - start dsh web with no console window and auto-open the browser. Tested on Windows; macOS/Linux in progress.（✅ 活跃）
- [dsh-start](https://github.com/zhengjy01/dsh-start)  — macOS 上 DSH Web GUI 的一键启停启动器：前台/后台启动、停止、状态、防重复启动、自动打开浏览器，并可用脚本构建程序坞版 DSH.app。（✅ 活跃）

### MCP & Integrations


#### 🔥 Top 10

| # | 项目 | 星数 | 说明 | 状态 |
|---|---|---|---|---|
| 1 | [Coding Tools MCP](https://github.com/xyTom/coding-tools-mcp) | ⭐846 | 面向编码的 MCP 工具集：让任何 AI Agent 获得编码能力。 | ✅ 活跃 |
| 2 | [memtrace-public](https://github.com/syncable-dev/memtrace-public) | ⭐459 | Structural memory for AI coding agents. Bi-temporal graph, MCP-native, zero LLM calls. Cursor · Claude Code · Codex · DeepSeek Harness · Hermes · VS Code · Windsurf. | ✅ 活跃 |
| 3 | [dsh-plugin-bridge](https://github.com/Totoro-qaq/dsh-plugin-bridge) | ⭐163 | DeepSeek Harness plugin for previewable cross-preset session migration. Fixed-schema handoffs preserve state, source-model intent, and unresolved images; the original session stays untouched. | ✅ 活跃 |
| 4 | [dsh-openpencil](https://github.com/ZSeven-W/dsh-openpencil) | ⭐135 | OpenPencil 设计预览与编辑集成。 | ✅ 活跃 |
| 5 | [dsh-super-injector](https://github.com/yjh051108/dsh-super-injector) | ⭐133 | 上下文注入增强插件（cordis）。 | ✅ 活跃 |
| 6 | [dsh-crew](https://github.com/ZSeven-W/dsh-crew) | ⭐119 | DeepSeek Harness (DSH) plugin: dispatch work to DSH agents from Claude Code / Codex — native subagent progress, in-host worker sessions with per-tier presets, and a multimodal bridge that lends the text-only harness vision and image generation. | ✅ 活跃 |
| 7 | [dsh-skill-mcp-panel](https://github.com/Fishquito7/dsh-skill-mcp-panel) | ⭐111 | DSH Web UI plugin: skill and MCP management（Web界面的skill/MCP管理工具） | ✅ 活跃 |
| 8 | [dsh-tabbit](https://github.com/Tabbit-Browser/dsh-tabbit) | ⭐96 | Tabbit Browser plugins for Deepseek Harness | ✅ 活跃 |
| 9 | [dsh-qqbot](https://github.com/tencent-connect/dsh-qqbot) | ⭐70 | 让 QQ 机器人接入 DeepSeek Harness（dsh）的官方插件 | ✅ 活跃 |
| 10 | [dsh-lark](https://github.com/omdsh-dev/dsh-lark) | ⭐41 | Lark/Feishu IM bot channel for DeepSeek Harness | 飞书 DeepSeek Harness 插件 | ✅ 活跃 |

#### 完整列表（86）

- [Coding Tools MCP](https://github.com/xyTom/coding-tools-mcp) ⭐846 — 面向编码的 MCP 工具集：让任何 AI Agent 获得编码能力。（✅ 活跃）
- [memtrace-public](https://github.com/syncable-dev/memtrace-public) ⭐459 — Structural memory for AI coding agents. Bi-temporal graph, MCP-native, zero LLM calls. Cursor · Claude Code · Codex · DeepSeek Harness · Hermes · VS Code · Windsurf.（✅ 活跃）
- [dsh-plugin-bridge](https://github.com/Totoro-qaq/dsh-plugin-bridge) ⭐163 — DeepSeek Harness plugin for previewable cross-preset session migration. Fixed-schema handoffs preserve state, source-model intent, and unresolved images; the original session stays untouched.（✅ 活跃）
- [dsh-openpencil](https://github.com/ZSeven-W/dsh-openpencil) ⭐135 — OpenPencil 设计预览与编辑集成。（✅ 活跃）
- [dsh-super-injector](https://github.com/yjh051108/dsh-super-injector) ⭐133 — 上下文注入增强插件（cordis）。（✅ 活跃）
- [dsh-crew](https://github.com/ZSeven-W/dsh-crew) ⭐119 — DeepSeek Harness (DSH) plugin: dispatch work to DSH agents from Claude Code / Codex — native subagent progress, in-host worker sessions with per-tier presets, and a multimodal bridge that lends the text-only harness vision and image generation.（✅ 活跃）
- [dsh-skill-mcp-panel](https://github.com/Fishquito7/dsh-skill-mcp-panel) ⭐111 — DSH Web UI plugin: skill and MCP management（Web界面的skill/MCP管理工具）（✅ 活跃）
- [dsh-tabbit](https://github.com/Tabbit-Browser/dsh-tabbit) ⭐96 — Tabbit Browser plugins for Deepseek Harness（✅ 活跃）
- [dsh-qqbot](https://github.com/tencent-connect/dsh-qqbot) ⭐70 — 让 QQ 机器人接入 DeepSeek Harness（dsh）的官方插件（✅ 活跃）
- [dsh-lark](https://github.com/omdsh-dev/dsh-lark) ⭐41 — Lark/Feishu IM bot channel for DeepSeek Harness | 飞书 DeepSeek Harness 插件（✅ 活跃）
- [dsh-browser](https://github.com/wqty123/dsh-browser) ⭐37 — Shared real browser plugin for DeepSeek Harness（✅ 活跃）
- [dsh-lark-bot](https://github.com/PlutoKeating/dsh-lark-bot) ⭐37 — DeepSeek Harness (dsh) 接入飞书/Lark bot，扫码即用：流式卡片、项目工作区、并行任务、多角色 Agent、跨会话通知、对话内模型/密钥管理与安全网守护（dsh 崩溃后飞书仍可自救）。A scan-to-connect bridge bot connecting DeepSeek Harness (dsh) into Feishu/Lark: streaming cards, workspaces, parallel tasks, multi-role agents, cross-session notify, in-chat model/key management, and a safety-net guardian.（✅ 活跃）
- [dsh-plugin-guide](https://github.com/PerryLink/dsh-plugin-guide) ⭐32 — Installable DSH bundle: the dsh-plugin-guide plugin-development knowledge base as an on-demand agent skill. Official docs archive (EN/ZH), Cordis primer, 114-repo community archive, 1654 archived Discussions, 20+ battle-tested pitfalls.（✅ 活跃）
- [dsh-lark-link](https://github.com/amlyczz/dsh-lark-link) ⭐30 — High-reliability Feishu/Lark bridge for DeepSeek Harness — QR one-click auth, multi-mode agents, card-based commands, zero-loss outbox, media in/out, session-log doctor, reusable DSH Web GUI（✅ 活跃）
- [deepseek-harness-docker](https://github.com/runzhliu/deepseek-harness-docker) ⭐27 — @deepseek-ai/dsh 的社区 Docker/K8s 打包，加固镜像。（✅ 活跃）
- [dsh-bottom-info-bar](https://github.com/songoao25/dsh-bottom-info-bar) ⭐26 — Bottom Info Bar — an information bar plugin for DeepSeek Harness: provider/model, live balance, peak/off-peak pricing with countdown, and real persisted per-session spend in a single line.（✅ 活跃）
- [dsh-feishu](https://github.com/PGZXB/dsh-feishu) ⭐26 — The Feishu UI for DeepSeek Harness  — a panel-driven control console: every slash command a button on the ⚙️ control-panel card, in-card approvals & questions, live streaming cards, one-QR setup. | DeepSeek Harness 的飞书 UI：面板驱动控制台——每个命令都是卡片按钮，卡内审批与提问，流式卡片，扫码一键配置。（✅ 活跃）
- [dsh-mcp-panel](https://github.com/PerryLink/dsh-mcp-panel) ⭐26 — 官方 DSH MCP 客户端的只读运行时管理面板：/mcp 命令 + 设置 Tab。（✅ 活跃）
- [deepseek-harness-vsc-extension](https://github.com/weinibuliu/deepseek-harness-vsc-extension) ⭐24 — DeepSeek Harness for VS Code as extension（💤 停更）
- [dsh-computer-use](https://github.com/ZRui-C/dsh-computer-use) ⭐24 — Text-first browser & background macOS control for DeepSeek Harness (DSH): target the right process and window without taking the user's pointer. 为 DSH 提供文本优先的电脑控制：后台操作 Chromium 与 macOS，不抢前台、不移动鼠标。（✅ 活跃）
- [dsh-ide](https://github.com/chenw2759-wq/dsh-IDE) ⭐24 — dsh-IDE 把 DeepSeek Harness（DSH）网页版升级成一站式 IDE：JupyterLab 式文件树、带语法高亮的代码编辑、多格式预览、Trae 风格红绿 diff 和内置终端，再加上「本地大脑、远程手脚」的 SSH 远程工作区，让 AI 直接在本机操控远程服务器，全程零配置文件改动。（✅ 活跃）
- [chatccc](https://github.com/wzj998/ChatCCC) ⭐22 — 飞书（Lark）或微信（WeChat）聊天控制 DeepSeek Harness / Claude Code / Cursor / Codex / CCC Agent（✅ 活跃）
- [dsh-mcp-manager](https://github.com/Js2Hou/dsh-mcp-manager) ⭐17 — 用于 DeepSeek Harness 的 MCP 可视化管理插件：在「设置 → MCP」中查看已安装/启用的 MCP 服务器，支持增删、启用/停用，并实时查看连接状态。（✅ 活跃）
- [dsh-hdc-bridge](https://github.com/1na-ko/dsh-hdc-bridge) ⭐16 — DSH 原生鸿蒙开发助手：hdc 设备闭环调试 + 设备面板（官方 client 插件形态）+ 离线官方知识层（Tier-1 随包）+ DevEco CLI 构建/签名/模拟器控制 / DSH-native HarmonyOS dev assistant: hdc device loop, live device panel, offline official knowledge, DevEco CLI build/sign/emulator（✅ 活跃）
- [dsh-movein](https://github.com/sjh9714/dsh-movein) ⭐15 — Migrate Claude Code setup into DeepSeek Harness. Import skills, commands, agents, hooks, permission rules, and MCP config. Codex and OpenCode supported.（✅ 活跃）
- [dsh-chatgpt-bridge](https://github.com/jiezeng2004-design/dsh-chatgpt-bridge) ⭐14 — MCP bridge that lets ChatGPT web create, view, continue, and control DeepSeek Harness (DSH) agent sessions.（✅ 活跃）
- [dsh-vscode](https://github.com/Lixxx1/dsh-vscode) ⭐14 — DSH Sidebar — a Claude Code/Codex-style VS Code sidebar for DeepSeek Harness. 像 Claude Code、Codex 一样，在 VS Code 侧边栏中使用 DSH。（✅ 活跃）
- [deepseek-harness-action](https://github.com/Lixiaoyiao/deepseek-harness-action) ⭐13 — 社区 GitHub Action：AI 代码审查、CI 诊断、自动修复、Issue 转 PR。（✅ 活跃）
- [dsh-git-graph](https://github.com/1841220388zzzcccxxx-star/dsh-git-graph) ⭐13 — Embedded git repository graph visualizer for the DeepSeek Harness Web GUI | 嵌入式 Git 仓库图谱可视化插件（提交历史图 / 分支过滤 / 文件 diff / VSCode 式未提交改动）（✅ 活跃）
- [deepseek-harness-acp](https://github.com/openma-ai/deepseek-harness-acp) ⭐12 — DeepSeek Harness 的 ACP 服务器实现：复用凭据与会话，将完整 DSH Agent 暴露给 ACP 客户端。（✅ 活跃）
- [dsh-search-mcp](https://github.com/gxpppp/dsh-search-mcp) ⭐12 — 用搜索 MCP 服务器（Tavily/Brave/Exa/Perplexity/DDG）替换 DSH 内置搜索。（✅ 活跃）
- [dsh-vision-proxy](https://github.com/Flyvhidbwo/dsh-vision-proxy) ⭐12 — DeepSeek Harness 插件：DeepSeek 大脑 + 自动识图。GUI 附加图片自动经 OpenAI 兼容 VLM 转译成文字后交给 DeepSeek 作答；支持百炼/智谱/OpenRouter 等任意 OpenAI 兼容端点（默认 qwen3.7-flash），无 key 自动探测本地 Ollama（图片不出本机）；安装时有一问式确认（✅ 活跃）
- [ikanban](https://github.com/isomoes/ikanban) ⭐12 — Monorepo for the iKanban browser-surface fork for DeepSeek Harness.（✅ 活跃）
- [dsh-annotate](https://github.com/BrambleXu/dsh-annotate) ⭐11 — Visual browser element annotation for DeepSeek Harness, capturing DOM, styles, accessibility data, comments, and viewport screenshots. DeepSeek Harness 浏览器元素标注插件，捕获 DOM、样式、可访问性数据、评论和视口截图。（✅ 活跃）
- [dsh-acp-for-bitfun](https://github.com/bobleer/dsh-acp-for-bitfun) ⭐10 — BitFun 与 DSH ACP 交互对接 插件（✅ 活跃）
- [dsh-better-browser](https://github.com/titanwings/dsh-better-browser) ⭐10 — DSH 真实浏览器插件：通过 Kimi WebBridge 让 Agent 操作用户已登录的浏览器，并提供 13 个 webbridge_* 工具。 / Let DSH Agents use your signed-in browser through thirteen Kimi WebBridge tools.（✅ 活跃）
- [dsh-feishu](https://github.com/xmanrui/dsh-feishu) ⭐10 — 通过扫码把飞书机器人接入DeepSeek Harness（✅ 活跃）
- [dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) ⭐10 — MCP 服务器管理器：设置页 OAuth（PKCE + 动态客户端注册）或静态 Token 认证。（✅ 活跃）
- [deepseek-acp](https://github.com/xintaofei/deepseek-acp) ⭐9 — 把 DeepSeek Harness 接成一个面向编辑器的完整编码 Agent， 通过 Agent Client Protocol（ACP）与客户端通话。（✅ 活跃）
- [dsh-harness-mcp-server](https://github.com/chushixixin/dsh-harness-mcp-server) ⭐9 — 将 DSH Agent 能力暴露为 MCP 服务器（大脑=Hermes，双手=Harness）。（✅ 活跃）
- [dsh-im-bridge](https://github.com/BiBoyang/dsh-im-bridge) ⭐9 — DSH 插件：把 DeepSeek Harness 桥接到 IM（v0.1 微信/iLink；钉钉/飞书/Telegram 预留）。turn/approval 推送 + 远程批准/注入，持久去重/收敛分段/合并窗口。（✅ 活跃）
- [dsh-lan-access](https://github.com/Leon0555/dsh-lan-access) ⭐9 — Web GUI 局域网访问：0.0.0.0 绑定 + 非安全上下文 polyfill。（✅ 活跃）
- [dsh-oauth-mcp-client](https://github.com/springbrand-lab/dsh-oauth-mcp-client) ⭐9 — OAuth 2.1 Streamable HTTP MCP 客户端插件。（✅ 活跃）
- [dsh-browser](https://github.com/xylt369/dsh-browser) ⭐8 — Browser capability for DeepSeek Harness: headed Edge/Playwright provider, SSRF-safe navigation, a11y-ref clicking, permission gate with auto-remember, gated evaluate（✅ 活跃）
- [dsh-telegram-channel](https://github.com/hi-wenw/dsh-telegram-channel) ⭐8 — Telegram 手机远程控制 DSH 实时会话：会话选择、绑定/解绑，轨迹与桌面一致。（✅ 活跃）
- [dsh-vision](https://github.com/54xkeee/dsh-vision) ⭐8 — Vision for DeepSeek Harness: Doubao Web by default (zero-cost, no API key), Antigravity IDE quota (flash/pro), any IDE CLI, Gemini — auto detail escalation, evidence memory（✅ 活跃）
- [dsh-chatnode-wechat](https://github.com/Jesse-njx/dsh-chatnode-wechat) ⭐7 — Chat with, monitor, and approve your DSH agents from WeChat — an iLink gateway + conversation node bundle for DeepSeek Harness（✅ 活跃）
- [dsh-lark-bridge](https://github.com/imetn/dsh-lark-bridge) ⭐7 — Bidirectional Lark/Feishu controller for DeepSeek Harness（✅ 活跃）
- [dsh-message-preview](https://github.com/asukasec/dsh-message-preview) ⭐7 — Right-side user-message navigator for the DeepSeek Harness Web UI.（✅ 活跃）
- [telegram](https://github.com/LoserFox/telegram) ⭐7 — Telegram Bot API 桥接插件：长轮询、per-chat 会话、HTML 格式化（✅ 活跃）
- [DSH Telegram Relay](https://github.com/congchuanling-dot/DSH-Telegram-Relay) ⭐6 — 把 Telegram 变成 DSH 远程对话渠道并接收通知。（✅ 活跃）
- [dsh-acp-plugin](https://github.com/agentic-control-plane/dsh-acp-plugin) ⭐6 — Agentic Control Plane for DeepSeek Harness — policy-check every tool call before it runs（✅ 活跃）
- [dsh-agentlink](https://github.com/hootandy321/dsh-Agentlink) ⭐6 — Caller-side bridge from Codex and other agent frameworks to DeepSeek Harness, with observable sessions, follow-up, cancellation, and human-gated approvals.（✅ 活跃）
- [dsh-mcp-lens](https://github.com/labmimors/dsh-mcp-lens) ⭐6 — DeepSeek Harness MCP tool search for large catalogs: 1,000 MCP tools behind 2 MCP-facing schemas, exact-schema calls, allow/deny controls, and a local calculator.（✅ 活跃）
- [dsh-cowork](https://github.com/Jesse-njx/dsh-cowork) ⭐5 — READ + WRITE for office documents & notebooks in DeepSeek Harness — doc_read/doc_write tools (xlsx, pdf, docx, pptx, ipynb) plus MCP server and CLI（✅ 活跃）
- [dsh-feishu-bridge](https://github.com/wz-heng/dsh-feishu-bridge) ⭐5 — Fail-closed Feishu (Lark) channel bridge for DeepSeek Harness (dsh) — chat with a bot, get agent turns back. Opt-in human-in-the-loop bash approval (Allow/Deny cards, fail-closed timeout), one-message /pair onboarding, webhook signature/timestamp/replay verification, daily latest-SDK canary. Community plugin, not DeepSeek-official.（✅ 活跃）
- [dsh-subscription-auth](https://github.com/Khellendros97/dsh-subscription-auth) ⭐5 — dsh对接openai、grok、anthropic、kimi订阅渠道（✅ 活跃）
- [dsh-talk](https://github.com/PerryLink/dsh-talk) ⭐5 — Voice-first session loop for DeepSeek Harness: a composer microphone button with browser/local speech-to-text (Web Speech, FunASR, whisper.cpp), a speak tool for text-to-speech replies (browser, edge-tts, piper), event announcements with mute, and speak-to-interrupt.（✅ 活跃）
- [dsh4vscode](https://github.com/DoggyHU/dsh4vscode) ⭐5 — 由 DSH Agent 驱动的 VS Code 聊天窗口：OpenCode 风格独立会话，模型自动路由。（✅ 活跃）
- [dsh-plugin-opencode-bridge](https://github.com/YYTbit/dsh-plugin-opencode-bridge) ⭐4 — Bridge opencode skills and config into DeepSeek Harness（✅ 活跃）
- [dsh-session-hub](https://github.com/Asaiuta/dsh-session-hub) ⭐4 — Aggregate and natively control multiple remote DeepSeek Harness (DSH) servers' sessions from one official Web UI — hub gateway + official-UI bridge. 多服务器 DSH 会话聚合与原生操控（✅ 活跃）
- [dsh-session-sync](https://github.com/PerryLink/dsh-session-sync) ⭐4 — Cross-device DeepSeek Harness session sync: a dedicated git mirror with append-only keep-both conflict resolution (fork files, never silently overwritten), /sync command and sync_* tools（✅ 活跃）
- [dsh-slack](https://github.com/STARDUSTLC666/dsh-slack) ⭐4 — DeepSeek Harness Slack 插件：slack_notify/channels/inbox/reply 四工具，Socket Mode 免公网回调收消息，收件箱队列 + 线程回复，支持自定义 slackApiUrl 对接代理网关；内置假 Slack 服务器做协议级验收测试。· Two-way Slack messaging for DeepSeek Harness agents.（✅ 活跃）
- [kimi-tide](https://github.com/tafcear/kimi-tide) ⭐4 — 月汐 — Kimi Code (Moonshot) 接入 DeepSeek Harness 的完整方案：标准 DSH 插件 + Kimi CLI 桥接维护 fork + Agent 协作闭环方法论（✅ 活跃）
- [PicGo DSH Plugin](https://github.com/PicGo/dsh-plugin) ⭐4 — PicGo 官方插件：从 DSH 上传图片/文件到图床并获取公网 URL。（✅ 活跃）
- [deepseek-harness-plugin-mcp](https://github.com/bobleer/deepseek-harness-plugin-mcp) ⭐3 — MCP server that lets any agent discover, install, and run DeepSeek Harness plugins (topic: dsh-plugin).（✅ 活跃）
- [dsh-dingtalk](https://github.com/STARDUSTLC666/dsh-dingtalk) ⭐3 — DeepSeek Harness 钉钉群机器人通知插件：dingtalk_notify/dingtalk_text 两工具，自定义机器人 webhook + HMAC 加签安全模式，手写签名实现、零运行时依赖；纯 Node 全平台。· DingTalk group-robot notifications for DeepSeek Harness agents.（✅ 活跃）
- [dsh-github](https://github.com/PerryLink/dsh-github) ⭐3 — Official-grade GitHub CI for DeepSeek Harness: composite action.yml, PR review bot with idempotent inline comments and a status-check gate, plus PR/issues tools with every write gated by human approval (Apache-2.0, dsh-plugin).（✅ 活跃）
- [dsh-mcp-manager](https://github.com/Nichts0v0/dsh-mcp-manager) ⭐3 — 在 DeepSeek Harness 设置页管理 MCP 服务器：运行时添加/编辑/启停/重连/删除，实时状态、自动重连，中英双语界面。MCP server manager for DeepSeek Harness — add, edit, enable/disable, reconnect & delete MCP servers from the web settings page, with live status and auto-reconnect.（✅ 活跃）
- [dsh-plugin-vision](https://github.com/tdf1995/dsh-plugin-vision) ⭐3 — Vision for text-only LLMs in DeepSeek Harness (DSH): describe images / OCR / VQA via free Gemini & GLM vision APIs（✅ 活跃）
- [dsh-subagent-cwd](https://github.com/lynx-gt/dsh-subagent-cwd) ⭐3 — DeepSeek Harness subagent delegation enhancement（✅ 活跃）
- [dsh-watch](https://github.com/dshworks/dsh-watch) ⭐3 — Put a watch on a stream: background listeners that wake the DeepSeek Harness agent with new matching lines — and a daemon host so a watcher runs unattended for weeks, with no task and no browser. Not affiliated with DeepSeek.（✅ 活跃）
- [shopline-ai-toolkit-dsh](https://github.com/lunw/shopline-ai-toolkit-dsh) ⭐3 — SHOPLINE AI Toolkit for DeepSeek Harness (dsh-plugin): official SHOPLINE Developer MCP bridge + SHOPLINE agent skills, mirroring the Shopify AI Toolkit architecture. dsh-plugin（✅ 活跃）
- [vscode-deepseek-harness](https://github.com/kalynnka/vscode-deepseek-harness) ⭐3 — 非官方：把 dsh 作为 VS Code 原生聊天 Agent 使用。（✅ 活跃）
- [dsh-github-integration](https://github.com/omdsh-dev/dsh-github-integration) ⭐2 — DSH 的 GitHub 集成插件。（✅ 活跃）
- [dsh-meow-cat](https://github.com/dsh-pub/dsh-meow-cat) ⭐2 — A cat runs across the bottom of the DeepSeek Harness web UI with a synthesized meow every time a conversation turn ends.（✅ 活跃）
- [dsh-plugin-acn](https://github.com/acnlabs/dsh-plugin-acn) ⭐2 — DeepSeek Harness plugin: join ACN so this agent can discover, message, and collaborate with other agents. Defaults to the China region.（✅ 活跃）
- [dsh-plugin-codex-bridge](https://github.com/YYTbit/dsh-plugin-codex-bridge) ⭐2 — Bridge codex skills and config into DeepSeek Harness（✅ 活跃）
- [dsh-plugin-pi-bridge](https://github.com/YYTbit/dsh-plugin-pi-bridge) ⭐2 — Bridge pi skills and config into DeepSeek Harness（✅ 活跃）
- [deepseek-harness-rs](https://github.com/Tokimorphling/deepseek-harness-rs) ⭐1 — DeepSeek Harness 的 Rust 移植。（🧪 实验性）
- [dsh-chrome](https://github.com/YJSoooooo/dsh-chrome) ⭐1 — Chrome 配置档桥接：通过 CDP 操控已登录的 Chrome。（✅ 活跃）
- [mcp_guard](https://github.com/dshoneys/mcp_guard) ⭐1 — 本机 MCP / Agent 口扫描、监视与审计（loopback 未鉴权 tools/list、CORS）。DeepSeek Honeys.（✅ 活跃）
- [dsh-docker](https://github.com/dshoneys/dsh-docker)  — 隔离的 DeepSeek Harness 插件安装沙箱，并对本机 MCP 口做防御性探测。（✅ 活跃）
- [dsh-wechat-bridge](https://github.com/lanbaolu/dsh-wechat-bridge)  — 个人微信桥接插件：扫码绑定后直接在微信里与本机 DeepSeek Harness Agent 对话（文字/图片/语音/文件、流式回复、会话持久化、三端通用）。（✅ 活跃）
- [opendsh](https://github.com/TheChengXi/opendsh)  — 在 VS Code 内打开 DSH Web UI，一键启停。（✅ 活跃）
- [URL Manager MCP](https://github.com/Piccolo123/url-manager-mcp)  — URL Manager 的 MCP 伴生服务器：21 个工具用于保存/搜索/分类/共享与魔法链接投递。（✅ 活跃）

### Examples & Starters


#### 🔥 Top 9

| # | 项目 | 星数 | 说明 | 状态 |
|---|---|---|---|---|
| 1 | [hello-dsh](https://github.com/pingfanfan/hello-dsh) | ⭐79 | 从零开始看懂「万物皆可插件」：零基础插件开发教程，含 22 个中文技能实例。 | ✅ 活跃 |
| 2 | [dsh-plugin-template](https://github.com/bugmaker2/dsh-plugin-template) | ⭐13 | DeepSeek Harness 插件开发模板。 | ✅ 活跃 |
| 3 | [plugin-template (omdsh-dev)](https://github.com/omdsh-dev/plugin-template) | ⭐12 | 基于原 turtle-ui 官方仓库创建的插件模板。 | ✅ 活跃 |
| 4 | [turtle-ui](https://github.com/turtle1999/turtle-ui) | ⭐8 | 官方 UI 插件参考实现。 | ✅ 活跃 |
| 5 | [dsh-plugin-template (sunshine-lang)](https://github.com/sunshine-lang/dsh-plugin-template) | ⭐6 | 可直接发布的插件骨架：bundle 格式、工具 DSL、配置与测试。 | ✅ 活跃 |
| 6 | [dsh-101](https://github.com/bill9109/dsh-101) | ⭐5 | DSH 文档阅读模式。 | ✅ 活跃 |
| 7 | [InfiniteDSH](https://github.com/vdnight89/InfiniteDSH) | ⭐3 | 诸天万界DSH：一个会话就是一本书。封面开书十九界，文学预设只写正文，规则书按关键词注入，/export-story 誊成 Markdown 小说。 | ✅ 活跃 |
| 8 | [Living-Dream-DSH](https://github.com/alllllllllli/Living-Dream-DSH) | ⭐2 | DSH 桌面配置框架：8+ MCP 服务器、免费模型渠道（CNB 代理、AMD Radeon Cloud）、Tailscale 手机远程、视觉补丁、一键安装。 | ✅ 活跃 |
| 9 | [dsh-plugin-hello](https://github.com/xu1132/dsh-plugin-hello) |  | Hello-world 风格 DSH 起步插件。 | ✅ 活跃 |

#### 完整列表（9）

- [hello-dsh](https://github.com/pingfanfan/hello-dsh) ⭐79 — 从零开始看懂「万物皆可插件」：零基础插件开发教程，含 22 个中文技能实例。（✅ 活跃）
- [dsh-plugin-template](https://github.com/bugmaker2/dsh-plugin-template) ⭐13 — DeepSeek Harness 插件开发模板。（✅ 活跃）
- [plugin-template (omdsh-dev)](https://github.com/omdsh-dev/plugin-template) ⭐12 — 基于原 turtle-ui 官方仓库创建的插件模板。（✅ 活跃）
- [turtle-ui](https://github.com/turtle1999/turtle-ui) ⭐8 — 官方 UI 插件参考实现。（✅ 活跃）
- [dsh-plugin-template (sunshine-lang)](https://github.com/sunshine-lang/dsh-plugin-template) ⭐6 — 可直接发布的插件骨架：bundle 格式、工具 DSL、配置与测试。（✅ 活跃）
- [dsh-101](https://github.com/bill9109/dsh-101) ⭐5 — DSH 文档阅读模式。（✅ 活跃）
- [InfiniteDSH](https://github.com/vdnight89/InfiniteDSH) ⭐3 — 诸天万界DSH：一个会话就是一本书。封面开书十九界，文学预设只写正文，规则书按关键词注入，/export-story 誊成 Markdown 小说。（✅ 活跃）
- [Living-Dream-DSH](https://github.com/alllllllllli/Living-Dream-DSH) ⭐2 — DSH 桌面配置框架：8+ MCP 服务器、免费模型渠道（CNB 代理、AMD Radeon Cloud）、Tailscale 手机远程、视觉补丁、一键安装。（✅ 活跃）
- [dsh-plugin-hello](https://github.com/xu1132/dsh-plugin-hello)  — Hello-world 风格 DSH 起步插件。（✅ 活跃）

### Tutorials & Learning


#### 🔥 Top 10

| # | 项目 | 星数 | 说明 | 状态 |
|---|---|---|---|---|
| 1 | [DeepSeek Harness Orange Book](https://github.com/alchaincyf/deepseek-harness-orange-book) | ⭐1,118 | 《DeepSeek Harness 橙皮书》：完整系统提示词、129 行启动清单、三份原始会话日志——官方文档没有的一手实测。PDF/EPUB/HTML 免费下载。 | ✅ 活跃 |
| 2 | [dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) | ⭐604 | 从 0 到 1 深度手册：安装/插件开发/性能调优/实测案例/同模型多 Agent 实测对比（中文 + 英文 PDF）。 | ✅ 活跃 |
| 3 | [dshfind](https://github.com/hikariming/dshfind) | ⭐200 | DSH 原理学习、插件市场与最佳实践：从 Cordis 论文逐章精读到插件自动聚合市场。 | ✅ 活跃 |
| 4 | [deepseek-harness-tutorial](https://github.com/ht426/deepseek-harness-tutorial) | ⭐182 | DeepSeek Harness 中文详细学习教程。 | ✅ 活跃 |
| 5 | [dsh-memory](https://github.com/FuRongJun-1999/dsh-memory) | ⭐66 | 白箱AGI架构探索：元认知（自我认知循环）、持续学习（知识飞轮）、世界模型（条件空间+语义时空图）、自我改进（自举纪律）、零LLM白箱管线与可审计信任护栏。 | ✅ 活跃 |
| 6 | [dsh-harness-tutorial](https://github.com/yanhua1010/dsh-harness-tutorial) | ⭐54 | DeepSeek Harness Agent 的原理与实现：从零到一实现一个 AI Agent —— 一切皆插件的中文教程（VitePress 站点 + 8 个 Demo + mini-harness 教学项目） | ✅ 活跃 |
| 7 | [deepseek-harness-handbook](https://github.com/sandbaseai/deepseek-harness-handbook) | ⭐36 | Independent, source-backed handbook for DeepSeek AI's official DeepSeek Harness (dsh): agents, plugins, security, troubleshooting, and runbooks. | ✅ 活跃 |
| 8 | [dsh-explain](https://github.com/yuezengwu/dsh-explain) | ⭐11 | 本地优先学习模式：跨会话全局学习线程、按来源讲解、ExplainContext、压缩与可诊断设置。 | ✅ 活跃 |
| 9 | [deepseek-harness-learning](https://github.com/Lucky2024-pllove/deepseek-harness-learning) | ⭐7 | 基于 deepseek-harness 仓库系统化拆解的学习网站：面向想了解 AI Agent 框架如何工作的开发者。 | ✅ 活跃 |
| 10 | [deepseek-harness-prompts](https://github.com/demouo/deepseek-harness-prompts) | ⭐6 | 不同模式下的 DeepSeek Harness 提示词集。 | ✅ 活跃 |

#### 完整列表（15）

- [DeepSeek Harness Orange Book](https://github.com/alchaincyf/deepseek-harness-orange-book) ⭐1,118 — 《DeepSeek Harness 橙皮书》：完整系统提示词、129 行启动清单、三份原始会话日志——官方文档没有的一手实测。PDF/EPUB/HTML 免费下载。（✅ 活跃）
- [dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) ⭐604 — 从 0 到 1 深度手册：安装/插件开发/性能调优/实测案例/同模型多 Agent 实测对比（中文 + 英文 PDF）。（✅ 活跃）
- [dshfind](https://github.com/hikariming/dshfind) ⭐200 — DSH 原理学习、插件市场与最佳实践：从 Cordis 论文逐章精读到插件自动聚合市场。（✅ 活跃）
- [deepseek-harness-tutorial](https://github.com/ht426/deepseek-harness-tutorial) ⭐182 — DeepSeek Harness 中文详细学习教程。（✅ 活跃）
- [dsh-memory](https://github.com/FuRongJun-1999/dsh-memory) ⭐66 — 白箱AGI架构探索：元认知（自我认知循环）、持续学习（知识飞轮）、世界模型（条件空间+语义时空图）、自我改进（自举纪律）、零LLM白箱管线与可审计信任护栏。（✅ 活跃）
- [dsh-harness-tutorial](https://github.com/yanhua1010/dsh-harness-tutorial) ⭐54 — DeepSeek Harness Agent 的原理与实现：从零到一实现一个 AI Agent —— 一切皆插件的中文教程（VitePress 站点 + 8 个 Demo + mini-harness 教学项目）（✅ 活跃）
- [deepseek-harness-handbook](https://github.com/sandbaseai/deepseek-harness-handbook) ⭐36 — Independent, source-backed handbook for DeepSeek AI's official DeepSeek Harness (dsh): agents, plugins, security, troubleshooting, and runbooks.（✅ 活跃）
- [dsh-explain](https://github.com/yuezengwu/dsh-explain) ⭐11 — 本地优先学习模式：跨会话全局学习线程、按来源讲解、ExplainContext、压缩与可诊断设置。（✅ 活跃）
- [deepseek-harness-learning](https://github.com/Lucky2024-pllove/deepseek-harness-learning) ⭐7 — 基于 deepseek-harness 仓库系统化拆解的学习网站：面向想了解 AI Agent 框架如何工作的开发者。（✅ 活跃）
- [deepseek-harness-prompts](https://github.com/demouo/deepseek-harness-prompts) ⭐6 — 不同模式下的 DeepSeek Harness 提示词集。（✅ 活跃）
- [dsh-book-deepseek-harness](https://github.com/LaplaceYoung/dsh-book-deepseek-harness) ⭐6 — 《深入理解 DeepSeek Harness：一切皆插件的 Agent 架构》——源码级架构拆解科普书：37 个章节文件、PDF、Mermaid 图。（✅ 活跃）
- [dsh-learn-everything](https://github.com/cendaifeng/dsh-learn-everything) ⭐5 — 费曼学习模式：教→复述→评判→重讲循环，渲染为富 HTML 课程卡片。（✅ 活跃）
- [gitlearnos](https://github.com/Guojiz/gitlearnos) ⭐4 — Git-native AI learning OS with a GitLearnOS-exclusive DeepSeek Harness panel, targeted practice, local RAG, and learner-owned memory.（✅ 活跃）
- [deepseek-protocol-doctor](https://github.com/Whning0513/deepseek-protocol-doctor) ⭐2 — 检查 DeepSeek 工具循环、reasoning_content、严格 schema 与捕获的 SSE，也可作为 DSH 插件。（✅ 活跃）
- [DeepSeek Harness Brain](https://github.com/AgriciDaniel/deepseek-harness-brain)  — 带来源引用的 Obsidian 知识库，包含浅显指南、架构笔记、可安装助手技能，以及 DeepSeek Harness 可移植性指南。（✅ 活跃）

### Awesome Lists & Registries


#### 🔥 Top 10

| # | 项目 | 星数 | 说明 | 状态 |
|---|---|---|---|---|
| 1 | [awesome-deepseek-integration](https://github.com/deepseek-ai/awesome-deepseek-integration) | ⭐38,897 | 官方：DeepSeek 生态集成目录 | ✅ 活跃 |
| 2 | [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | ⭐11,012 | 大型 DSH 插件精选目录（双语）。 | ✅ 活跃 |
| 3 | [awesome-deepseek-agent (official)](https://github.com/deepseek-ai/awesome-deepseek-agent) | ⭐5,966 | 官方精选：将 DeepSeek 模型集成到主流 Agent/编码助手工具的指南（AstrBot、Cherry Studio、Claude Code、Codex、DeepSeek-TUI、Reasonix 等）。 | ✅ 活跃 |
| 4 | [awesome-harness-engineering](https://github.com/walkinglabs/awesome-harness-engineering) | ⭐3,887 | Harness 工程精选（跨生态） | ✅ 活跃 |
| 5 | [awesome-dsh-plugins (Radar)](https://github.com/AdamPlatin123/awesome-dsh-plugins) | ⭐1,309 | 雷达索引仓库：自动扫描发现的所有 dsh 插件候选，带证据驱动的兼容性矩阵。 | ✅ 活跃 |
| 6 | [awesome-deepseek-harness](https://github.com/Anil-matcha/awesome-deepseek-harness) | ⭐966 | Curated guide to DeepSeek Harness (dsh) and its best community plugins | ✅ 活跃 |
| 7 | [awesome-dsh-plugin](https://github.com/Anil-matcha/awesome-dsh-plugin) | ⭐966 | A curated list of plugins for DeepSeek Harness (dsh) - DeepSeek Harness plugin ecosystem | ✅ 活跃 |
| 8 | [awesome-deepseek-coder](https://github.com/deepseek-ai/awesome-deepseek-coder) | ⭐811 | 官方：DeepSeek 编码资源 | ✅ 活跃 |
| 9 | [awesome-deepseek-harness (0xsline)](https://github.com/0xsline/awesome-deepseek-harness) | ⭐788 | DSH 生态目录：来自 dsh-external/hub 与公开 dsh-plugin 主题的插件、工具与基础设施精选。 | ✅ 活跃 |
| 10 | [awesome-dsh-plugin (bruc3van)](https://github.com/bruc3van/awesome-dsh-plugin) | ⭐261 | 用 30 秒找到适合你的 DSH 插件：不仅列仓库，还说明插件解决什么问题、适合谁、从哪开始。 | ✅ 活跃 |

#### 完整列表（82）

- [awesome-deepseek-integration](https://github.com/deepseek-ai/awesome-deepseek-integration) ⭐38,897 — 官方：DeepSeek 生态集成目录（✅ 活跃）
- [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) ⭐11,012 — 大型 DSH 插件精选目录（双语）。（✅ 活跃）
- [awesome-deepseek-agent (official)](https://github.com/deepseek-ai/awesome-deepseek-agent) ⭐5,966 — 官方精选：将 DeepSeek 模型集成到主流 Agent/编码助手工具的指南（AstrBot、Cherry Studio、Claude Code、Codex、DeepSeek-TUI、Reasonix 等）。（✅ 活跃）
- [awesome-harness-engineering](https://github.com/walkinglabs/awesome-harness-engineering) ⭐3,887 — Harness 工程精选（跨生态）（✅ 活跃）
- [awesome-dsh-plugins (Radar)](https://github.com/AdamPlatin123/awesome-dsh-plugins) ⭐1,309 — 雷达索引仓库：自动扫描发现的所有 dsh 插件候选，带证据驱动的兼容性矩阵。（✅ 活跃）
- [awesome-deepseek-harness](https://github.com/Anil-matcha/awesome-deepseek-harness) ⭐966 — Curated guide to DeepSeek Harness (dsh) and its best community plugins（✅ 活跃）
- [awesome-dsh-plugin](https://github.com/Anil-matcha/awesome-dsh-plugin) ⭐966 — A curated list of plugins for DeepSeek Harness (dsh) - DeepSeek Harness plugin ecosystem（✅ 活跃）
- [awesome-deepseek-coder](https://github.com/deepseek-ai/awesome-deepseek-coder) ⭐811 — 官方：DeepSeek 编码资源（✅ 活跃）
- [awesome-deepseek-harness (0xsline)](https://github.com/0xsline/awesome-deepseek-harness) ⭐788 — DSH 生态目录：来自 dsh-external/hub 与公开 dsh-plugin 主题的插件、工具与基础设施精选。（✅ 活跃）
- [awesome-dsh-plugin (bruc3van)](https://github.com/bruc3van/awesome-dsh-plugin) ⭐261 — 用 30 秒找到适合你的 DSH 插件：不仅列仓库，还说明插件解决什么问题、适合谁、从哪开始。（✅ 活跃）
- [Awesome-DeepSeek-Harness-Plugins](https://github.com/Zhiyuan-Fan/Awesome-DeepSeek-Harness-Plugins) ⭐240 — DeepSeek Harness 插件精选列表。（✅ 活跃）
- [awesome-deepseek-harness (libukai)](https://github.com/libukai/awesome-deepseek-harness) ⭐175 — 终极指南：快速入门、资源推荐、精选插件与实用工具。（✅ 活跃）
- [awesome-deepseek-harness (Dominic789654)](https://github.com/Dominic789654/awesome-deepseek-harness) ⭐174 — DSH 插件、技能、MCP 服务器、patch/profile 层、编排器与 UI 精选列表。（✅ 活跃）
- [notes (zhaoolee)](https://github.com/zhaoolee/notes) ⭐149 — 开源版锤子便签：一键 Docker 私有化部署、skill 调用、dsh plugin 支持、一键生成公众号格式。（✅ 活跃）
- [awesome-deepseek-harness-plugins](https://github.com/imsai-sh/awesome-deepseek-harness-plugins) ⭐145 — Curated community plugin directory and live marketplace for DeepSeek Harness.（✅ 活跃）
- [dsh-skin-market](https://github.com/kingOfSoySauce/dsh-skin-market) ⭐105 — DeepSeek Harness skin market 皮肤市场 已收录200+DSH 皮肤 完善评分系统加人工审核，有便捷的社区收录入口；有在线页面方便在线浏览，也有插件方便管理本地皮肤（✅ 活跃）
- [awesome-dsh-plugin](https://github.com/beancookie/awesome-dsh-plugin) ⭐93 — Awesome DeepSeek Harness (DSH) Plugin（✅ 活跃）
- [awesome-DSH-plugin (Alex-Yanggg)](https://github.com/Alex-Yanggg/awesome-DSH-plugin) ⭐77 — 精心整理的 DSH 插件、扩展、工具与开发资源列表。（✅ 活跃）
- [zat-dsh-engine](https://github.com/mishibeikejie/zat-dsh-engine) ⭐76 — Visual plugin marketplace for DeepSeek Harness — browse, search and install community plugins（✅ 活跃）
- [oh-my-dsh](https://github.com/like-study1/Oh-My-DSH) ⭐68 — 🐳 DeepSeek Harness 插件聚合社区 — 自动同步 dsh-plugin 生态 · 精选目录 · 每 8 小时自动维护 | Oh-My-DSH: a community-maintained catalog of DeepSeek Harness plugins, auto-synced from the dsh-plugin topic（✅ 活跃）
- [dsh-meow-memory](https://github.com/Phant0Meow/dsh-meow-memory) ⭐58 — Cross-session memory plugin for DeepSeek Harness: seven-layer SQLite store (soul/user/project/fact/lesson/topic/rules), BM25 retrieval, per-window dream consolidation. 跨会话七层长期记忆插件。（✅ 活跃）
- [plugin-registry](https://github.com/vlln/plugin-registry) ⭐57 — DSH 插件生态基建：薄控制台管理官方 repository 插件（0 patch）+ make-dsh-plugin 技能。（✅ 活跃）
- [dsh-session-manager](https://github.com/dream12347/dsh-session-manager) ⭐54 — DSH 会话管理插件：删除（回收站恢复/彻底清除）、统计、继续/暂停、打开日志目录、对话顶部抽屉、工作区分组与排序、上下文压缩阈值设置。DSH session manager: delete with trash/restore/purge, stats, continue/pause, log folder, header drawer, workspace grouping, context compaction threshold.（✅ 活跃）
- [oh-my-dsh](https://github.com/LaplaceYoung/oh-my-dsh) ⭐51 — 面向 DSH 的插件生态：700+ 插件，只通过扩展接缝注册，不修改 agent-loop 骨架。（✅ 活跃）
- [awesome-harness-engineering](https://github.com/jiji262/awesome-harness-engineering) ⭐49 — Harness 工程精选（中文）（✅ 活跃）
- [dsh-config-manager](https://github.com/xiajiajun516/dsh-config-manager) ⭐48 — DeepSeek Harness (DSH) backup & restore plugin — export, import, migrate and sync your complete DSH configuration, plugins, MCP servers, skills and workspace. One-click migration to another machine.（✅ 活跃）
- [dsh-market](https://github.com/2BingLing/dsh-market) ⭐46 — DeepSeek Harness 插件市场 · 持续收录 500+ DSH 插件：中文搜索 + 实用五维评分 + 一键安装。Web 版与 DSH 侧边栏插件双形态。Plugin marketplace for DeepSeek Harness: 500+ plugins, Chinese search, 5-dim scoring, one-click install.（✅ 活跃）
- [dsh-suite](https://github.com/whyihaveyou/dsh-suite) ⭐43 — 活体插件目录（785+ 插件，每小时刷新）：每日兼容性 CI、双语目录站与应用内插件商店。（✅ 活跃）
- [awesome-deepseek-harness-plugins](https://github.com/web-casa/Awesome-DeepSeek-Harness-Plugins) ⭐33 — DeepSeek Harness 插件精选（✅ 活跃）
- [sandbase-skills](https://github.com/sandbaseai/sandbase-skills) ⭐31 — 88 installable open-source Agent Skills for research, social intelligence, marketing, and business workflows—compatible with Codex, Claude Code, Cursor, Gemini CLI, and DeepSeek Harness.（✅ 活跃）
- [dsh-meme-hub](https://github.com/the-beating-light-of-the-nail/dsh-meme-hub) ⭐30 — 社区整活插件导航（皮肤、桌宠、小游戏），双语。（✅ 活跃）
- [dsh-plugin-marketplace](https://github.com/AwesomeHou/dsh-plugin-marketplace) ⭐27 — Plugin marketplace for DeepSeek Harness — live-syncs the GitHub dsh-plugin topic (1800+ repos) into a searchable, paginated settings tab with one-click install and agent tools (market_search / market_install).（✅ 活跃）
- [deepseek-plugin-store](https://github.com/Ericwong5021/deepseek-plugin-store) ⭐24 — DeepSeek Harness 独立社区插件商店：发现、安装并提交经过验证的插件、工具与扩展。 | Independent community plugin directory.（✅ 活跃）
- [awesome-dsh-plugins (kejixiaoliang)](https://github.com/kejixiaoliang/awesome-dsh-plugins) ⭐22 — DSH 插件精选目录：14 类 280+ 个社区插件，覆盖 MCP/Skill/TUI/多 Agent/上下文记忆/UI 皮肤。（✅ 活跃）
- [dsh-plugin-marketplace](https://github.com/YELEBAI/dsh-plugin-marketplace) ⭐20 — Verified plugin marketplace and autonomous registry for DeepSeek Harness（✅ 活跃）
- [dsh-plugin-hub](https://github.com/cclank/dsh-plugin-hub) ⭐17 — DeepSeek Harness community plugin registry with evidence-based screening（✅ 活跃）
- [dsh-plugin-hub](https://github.com/dshplugin/dsh-plugin-hub) ⭐16 — DeepSeek Harness 社区内置插件市场（dsh-plugin）— 搜索插件、下载并安装 4000+ 人工精选社区插件，每日更新、完全免费。内置在 Harness「设置 → 插件中心」，无需离开应用即可浏览、搜索、安装各类 AI 插件。（✅ 活跃）
- [deepseek-harness-awesome-top-500](https://github.com/weekend-project-space/deepseek-harness-awesome-top-500) ⭐15 — DeepSeek Harness Top 500 资源索引（✅ 活跃）
- [dsh-backup](https://github.com/xiaoyuyu6420/dsh-backup) ⭐14 — One command backs up & restores all of ~/.dsh for DeepSeek Harness: /backup, scheduled auto-backup, upgrade snapshots, session-log doctor & repair, out-of-process rescue console, credential redaction, GitHub sync. 一条命令备份/恢复 DSH 全部数据：升级快照、会话日志体检修复、起不来也能自救的救援通道、凭据脱敏。（✅ 活跃）
- [awesome-deepseek-harness (jiji262)](https://github.com/jiji262/awesome-deepseek-harness) ⭐13 — DeepSeek Harness 资源精选。（✅ 活跃）
- [awesome-dsh-plugins (white0dew)](https://github.com/white0dew/awesome-dsh-plugins) ⭐13 — DSH 插件公开目录，含安装命令。（✅ 活跃）
- [awesome-dsh-plugin (billLiao)](https://github.com/billLiao/awesome-dsh-plugin) ⭐12 — DeepSeek Harness 插件精选列表。（✅ 活跃）
- [dsh-checkpoint-rewind](https://github.com/PerryLink/dsh-checkpoint-rewind) ⭐12 — Claude Code /rewind for DeepSeek Harness — git-first workspace snapshots before every mutation, turn-boundary session forks, one-shot /rewind restore. A dsh-plugin capability seam.（✅ 活跃）
- [dsh-plugin-hub](https://github.com/helloHupc/dsh-plugin-hub) ⭐12 — DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 | https://dsh-plugin-hub.hupc.site（✅ 活跃）
- [dsh-plugin-marketplace](https://github.com/w2112515/dsh-plugin-marketplace) ⭐12 — Out-of-tree installable plugin marketplace bundle for DeepSeek Harness（✅ 活跃）
- [awesome-deepseek-harness-plugins](https://github.com/vvlife/awesome-deepseek-harness-plugins) ⭐10 — DeepSeek Harness 插件目录（✅ 活跃）
- [awesome-deepseek-harness-plugins](https://github.com/walkinglabs/awesome-deepseek-harness-plugins) ⭐9 — A curated, bilingual list of verified plugins, tools, design workflows, and learning resources for DeepSeek Harness (DSH).（✅ 活跃）
- [dsh-composer-history](https://github.com/PerryLink/dsh-composer-history) ⭐8 — Terminal-style input history for the DeepSeek Harness web composer: edge-first arrows with exact draft/caret restore, browser-local persisted history, Ctrl+R reverse search, workspace recall - and sliding-context awareness (compaction summaries in recall/search, compaction notice with one-click /compact fill).（✅ 活跃）
- [dsh-us-stocks](https://github.com/Realyujie/dsh-us-stocks) ⭐8 — US stock market data tools for DeepSeek Harness, powered by yahoo-finance2（✅ 活跃）
- [awesome-dsh-bridges](https://github.com/YYTbit/awesome-dsh-bridges) ⭐6 — DSH 桥接集成目录（✅ 活跃）
- [awesome-dsh-plugins](https://github.com/cccakeee/awesome-dsh-plugins) ⭐6 — DSH 插件列表（✅ 活跃）
- [dsh-plugins](https://github.com/Sakana-yuyu/dsh-plugins) ⭐6 — DeepSeek Harness (DSH) 插件目录：官方包 + 社区插件按 GitHub stars 排名，GitHub Pages 可访问。（✅ 活跃）
- [awesome-dsh-plugins](https://github.com/dshworks/awesome-dsh-plugins) ⭐5 — DSH 插件目录（垃圾过滤开放数据）（✅ 活跃）
- [dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) ⭐5 — DeepSeek Harness plugin market - browse, search & install dsh-plugin topic plugins (dsh 插件市场：浏览/搜索/安装插件)（✅ 活跃）
- [dsh-plugins](https://github.com/HackSing/dsh-plugins) ⭐5 — A bilingual, continuously maintained directory of plugins for DeepSeek Harness (DSH).（✅ 活跃）
- [awesome-dsh-skills](https://github.com/hackerFish/awesome-dsh-skills) ⭐4 — DSH 技能目录（✅ 活跃）
- [dsh-plugin-market](https://github.com/chnjames/dsh-plugin-market) ⭐4 — DSH 插件市场 — DeepSeek Harness 设置内一键安装社区插件，并提供公开目录站（浏览 / 复制安装命令）（✅ 活跃）
- [dsh-plugin-store](https://github.com/sandbaseai/dsh-plugin-store) ⭐4 — Native plugin marketplace for DeepSeek Harness: discover, filter, install, and manage 4,000+ community plugin packages.（✅ 活跃）
- [dsh-undo](https://github.com/LingLambda/dsh-undo) ⭐4 — Context undo/redo plugin for DeepSeek Harness (dsh): roll the model context back to the last completed step and restore it again.（✅ 活跃）
- [awesome-deepseek-harness](https://github.com/XiaomingX/awesome-deepseek-harness) ⭐3 — DeepSeek Harness 资源列表（✅ 活跃）
- [awesome-dsh-plugins](https://github.com/dongsheng123132/awesome-dsh-plugins) ⭐3 — DSH 插件精选（✅ 活跃）
- [awesome-dsh-plugins-2026](https://github.com/Herdeny/awesome-dsh-plugins-2026) ⭐3 — 2026 DSH 插件列表（✅ 活跃）
- [awesome-dsh-themes](https://github.com/dshworks/awesome-dsh-themes) ⭐3 — DSH 主题/皮肤注册表（✅ 活跃）
- [dsh-marketplace](https://github.com/ouyangyipeng/dsh-marketplace) ⭐3 — A safe, live plugin marketplace for DeepSeek Harness（✅ 活跃）
- [dsh-mask](https://github.com/PerryLink/dsh-mask) ⭐3 — PII masking middleware for DeepSeek Harness: anonymize names, phones, emails, ID cards, bank cards, keys, and addresses to placeholders before they reach the model, restore them at the display layer, keep the restore table only in memory and a controlled storage domain, never log plaintext, and expose /mask and the mask_test tool（✅ 活跃）
- [dsh-plugins](https://github.com/lwmxiaobei/dsh-plugins) ⭐3 — DeepSeek Harness 社区插件目录，自动汇总并基础校验 GitHub 插件，支持搜索、筛选、双语详情与最新版本安装命令复制。Community directory for DeepSeek Harness plugins with automated discovery, basic validation, search, filters, bilingual details, and latest version install commands.（✅ 活跃）
- [dsh-plugins-store](https://github.com/DshMarketPlace/dsh-plugins-store) ⭐3 — Browse and install DSH plugins from inside DeepSeek Harness. /store, a settings tab, and agent tools — bilingual.（✅ 活跃）
- [awesome-dsh-plugin](https://github.com/wgd753/awesome-dsh-plugin) ⭐2 — DSH 插件大集合（2000+ 链接）（✅ 活跃）
- [awesome-dsh-plugins](https://github.com/coolbat/awesome-dsh-plugins) ⭐2 — DSH 插件大目录（500+ 链接）（✅ 活跃）
- [awesome-dsh-plugins](https://github.com/jqueryscript/awesome-dsh-plugins) ⭐2 — DSH 插件列表（✅ 活跃）
- [awesome-dshoneys](https://github.com/dshoneys/awesome-dshoneys) ⭐2 — DeepSeek Honeys 认证插件目录 — 安全检测报告 + 插件需求墙 + 每周精选（✅ 活跃）
- [dshmarketplace](https://github.com/DshMarketPlace/dshmarketplace) ⭐2 — Bilingual directory of DeepSeek Harness (DSH) plugins — 3,400+ listings, sandbox-verified install commands, written detail pages, public API. Next.js on Cloudflare Workers.（✅ 活跃）
- [awesome-deepseek-harness](https://github.com/Harris1121/awesome-deepseek-harness) ⭐1 — DeepSeek Harness 资源精选（✅ 活跃）
- [awesome-deepseek-harness-plugins](https://github.com/SihanTeng/awesome-deepseek-harness-plugins) ⭐1 — DeepSeek Harness 插件精选（✅ 活跃）
- [awesome-dsh-list](https://github.com/kingselyjoe/awesome-dsh-list) ⭐1 — DSH 综合资源列表（1000+ 链接）（✅ 活跃）
- [awesome-dsh-plugins](https://github.com/oslook/awesome-dsh-plugins) ⭐1 — DSH 插件精选列表（✅ 活跃）
- [awesome-dsh-presets](https://github.com/hackerFish/awesome-dsh-presets) ⭐1 — DSH 预设目录（✅ 活跃）
- [awesome-deepseek-harness](https://github.com/Rodert/awesome-deepSeek-harness)  — DeepSeek Harness 精选资源（✅ 活跃）
- [awesome-deepseek-harness](https://github.com/awesome-deepseekharness/awesome-deepseek-harness)  — DSH 社区目录（✅ 活跃）
- [dsh-plugin-registry](https://github.com/dshplugin-app/dsh-plugin-registry)  — Discover and compare DeepSeek Harness plugins directly inside DSH.（✅ 活跃）
- [dshthemes](https://github.com/dshworks/dshthemes)  — dshthemes.com — every DeepSeek Harness theme, in its own colours. A reader of dshworks/awesome-dsh-themes.（✅ 活跃）
- [plugins](https://github.com/dsh-universe/plugins)  — DeepSeek Harness plugin & skill directory — DSH Universe official marketplace (duink.com)（✅ 活跃）

### Related Agent Harnesses


#### 🔥 Top 10

| # | 项目 | 星数 | 说明 | 状态 |
|---|---|---|---|---|
| 1 | [DeerFlow](https://github.com/bytedance/deer-flow) | ⭐80,462 | 字节跳动开源的长时间跨度 SuperAgent harness：技能、记忆、沙箱、子代理、工具与消息网关。 | ✅ 活跃 |
| 2 | [CodeWhale](https://github.com/Hmbown/CodeWhale) | ⭐40,830 | 开源、社区驱动的 Agent Harness。 | ✅ 活跃 |
| 3 | [agentmemory](https://github.com/rohitg00/agentmemory) | ⭐27,233 | 基于真实基准的 AI 编码 Agent 持久记忆（DSH agentmemory 移植的上游项目）。 | ✅ 活跃 |
| 4 | [Cordis](https://github.com/cordiverse/cordis) | ⭐6,867 | 时空可组合性元框架——DeepSeek Harness 底层的插件运行时。 | ✅ 活跃 |
| 5 | [deeptide](https://github.com/paean-ai/deeptide) | ⭐1,091 | DeepSeek 官方出品的 Swift 原生 macOS 编码 Agent。 | ✅ 活跃 |
| 6 | [sandbase-harness](https://github.com/sandbaseai/sandbase-harness) | ⭐628 | 开源 CMA 兼容的任意模型 Agent 运行时：MCP 工具、沙箱会话、审计与回放。 | ✅ 活跃 |
| 7 | [mnemon](https://github.com/mnemon-dev/mnemon) | ⭐500 | LLM 监督的 Agent 持久记忆：图召回与跨会话知识，单二进制。 | ✅ 活跃 |
| 8 | [claude-paper](https://github.com/alaliqing/claude-paper) | ⭐324 | 跨 Agent 论文研究工具包：快速摘要与深度精读，支持 Claude Code/Codex/OpenCode/DSH。 | ✅ 活跃 |
| 9 | [open-managed-agents](https://github.com/openma-ai/open-managed-agents) | ⭐243 | 开源 Claude Managed Agents API 实现与自托管 Claude Tag 风格 Agent 运行时。 | ✅ 活跃 |
| 10 | [Axern](https://github.com/cofy-x/axern) | ⭐57 | 面向 AI Agent 的开源沙箱：不可信代码执行与持久服务。 | ✅ 活跃 |

#### 完整列表（11）

- [DeerFlow](https://github.com/bytedance/deer-flow) ⭐80,462 — 字节跳动开源的长时间跨度 SuperAgent harness：技能、记忆、沙箱、子代理、工具与消息网关。（✅ 活跃）
- [CodeWhale](https://github.com/Hmbown/CodeWhale) ⭐40,830 — 开源、社区驱动的 Agent Harness。（✅ 活跃）
- [agentmemory](https://github.com/rohitg00/agentmemory) ⭐27,233 — 基于真实基准的 AI 编码 Agent 持久记忆（DSH agentmemory 移植的上游项目）。（✅ 活跃）
- [Cordis](https://github.com/cordiverse/cordis) ⭐6,867 — 时空可组合性元框架——DeepSeek Harness 底层的插件运行时。（✅ 活跃）
- [deeptide](https://github.com/paean-ai/deeptide) ⭐1,091 — DeepSeek 官方出品的 Swift 原生 macOS 编码 Agent。（✅ 活跃）
- [sandbase-harness](https://github.com/sandbaseai/sandbase-harness) ⭐628 — 开源 CMA 兼容的任意模型 Agent 运行时：MCP 工具、沙箱会话、审计与回放。（✅ 活跃）
- [mnemon](https://github.com/mnemon-dev/mnemon) ⭐500 — LLM 监督的 Agent 持久记忆：图召回与跨会话知识，单二进制。（✅ 活跃）
- [claude-paper](https://github.com/alaliqing/claude-paper) ⭐324 — 跨 Agent 论文研究工具包：快速摘要与深度精读，支持 Claude Code/Codex/OpenCode/DSH。（✅ 活跃）
- [open-managed-agents](https://github.com/openma-ai/open-managed-agents) ⭐243 — 开源 Claude Managed Agents API 实现与自托管 Claude Tag 风格 Agent 运行时。（✅ 活跃）
- [Axern](https://github.com/cofy-x/axern) ⭐57 — 面向 AI Agent 的开源沙箱：不可信代码执行与持久服务。（✅ 活跃）
- [deepseek-auto-evolving-harness](https://github.com/liuchen6667/deepseek-auto-evolving-harness) ⭐28 — 自进化 LLM Agent Harness：通过 Claude Code 与 self_evolution.md 指南进行基准驱动进化。（✅ 活跃）
<!-- AUTO:resources:END -->` 之间的资源表格由 `scripts/generate-readme.py` 产出。请编辑 JSON，不要手改表格。

---

# 质量等级

每条资源都带有一个状态标记：

| 状态 | 含义 |
|---|---|
| ✅ **活跃（Active）** | 近期有提交；仓库存在且包含代码 |
| 🧪 **实验性（Experimental）** | 非常新、API 不稳定、文档不全或验证有限 |
| 🚧 **进行中（WIP）** | 正在开发 |
| 💤 **停更（Inactive）** | 不再维护 |

所有条目均通过 GitHub API 实时核验。`dsh-external` 组织已于 2026 年中清空/重定向——多数其他注册表仍指向大量死链；本目录不收录已失效的仓库。

---

# 提交项目

欢迎提交 PR。建议包含以下信息：

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

项目应：
* 直接支持官方 `deepseek-ai/deepseek-harness`，或提供明确有用的周边工具
* 包含有意义的源代码或文档
* 避免误导性命名，并明确披露实验性状态

最简单的路径：通过[提交模板](.github/ISSUE_TEMPLATE/submit-project.yml)开 issue，或为仓库添加 `dsh-plugin` 主题标签后对 `data/` 提交 PR。

---

# 并非同一项目

⚠️ 存在使用 **DeepSeek Harness** 名称的旧项目/无关项目（例如独立的 DeepSeek API 封装）。本目录特指围绕 `deepseek-ai/deepseek-harness` 的生态。提交前请先核实目标。

---

# 路线图

## 第一阶段 — Awesome 目录 ✅
- [x] 插件 · 技能 · 工作流 · 智能体 · 客户端 · 示例 · 教程
- [x] 机器可读注册表 + schema
- [x] 自动化校验与链接检查
- [ ] 全条目 Verified 徽章铺开

## 第二阶段 — 自动化
- [ ] 每周运行 `update-metadata.py`（星数/状态刷新）
- [ ] 每周运行 `discover-github.py` → 候选评审 issue
- [ ] CI 自动部署 MkDocs

## 第三阶段 — HarnessHub
- [ ] 网站搜索与分类
- [ ] 带安装说明的资源页
- [ ] 热门/相关项目
- [ ] 一键安装命令

## 第四阶段 — CLI

```bash
dshx search browser
dshx search memory
dshx info dsh-at-file
dshx add <plugin>
```

## 第五阶段 — 桌面端
用于发现、安装、配置、运行与更新整个生态的 GUI。

---

# 贡献

DeepSeek Harness 迭代极快。如果你发现新插件、新工作流、新客户端、过期条目、失效链接或错误的兼容性信息——欢迎开 issue 或提交 PR。

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

# 免责声明

本项目为独立社区项目，**与 DeepSeek AI 无关联，亦未获其背书**。DeepSeek 与 DeepSeek Harness 均为各自所有者的商标或项目。除非特别注明，此处列出的项目均由独立作者维护。

---

## Star History

如果本目录帮你发现了有用的 DeepSeek Harness 项目，欢迎点个 Star ⭐。

**为 DeepSeek Harness 社区而生。🐋**
