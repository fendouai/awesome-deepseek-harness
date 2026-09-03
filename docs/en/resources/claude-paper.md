---
title: "claude-paper"
description: "Cross-agent research paper toolkit for Claude Code, Codex, OpenCode and DeepSeek Harness: quick summaries and deep dives."
keywords: "claude-paper, harness, related, research, search, deepseek harness, dsh"
---
# claude-paper

> ⭐ **324** · ✅ active · related · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | related | Category | Harness |
| Stars | ⭐ 324 | Status | ✅ active |
| Author | [alaliqing](https://github.com/alaliqing) | Updated | 2026-08-14 |

## One-liner

> Cross-agent research paper toolkit for Claude Code, Codex, OpenCode and DeepSeek Harness: quick summaries and deep dives.

## About

**Transform research papers into comprehensive learning environments** [English](README.md) | [中文](README.zh-CN.md) A research-paper learning plugin for **Claude Code, Codex, OpenCode, and DeepSeek Harness**. It preserves the same study workflow, generated materials, code demonstrations, and interactive web viewer across supported agents. Library View - Browse and search your paper collection Reading View - Study papers with rich formatting and math support

## ✨ Key Features

- **Automatic PDF parsing** - Extract title, authors, abstract, links, and complete paper text
- **Context-safe previews** - Save complete text to `paper.txt` while keeping a 50k preview in metadata
- **Code repository detection** - Automatically finds GitHub, arXiv, CodeOcean links
- **Quick paper summaries** - Screen a paper with a concise 300–500 word overview before a deep study
- **Adaptive learning materials** - Generates README, summary, insights, Q&A based on paper complexity
- **Code demonstrations** - Clean implementations with Jupyter notebooks and original code integration
- **Interactive web viewer** - Nuxt.js interface with math equation support (KaTeX)
- **Intelligent assessment** - Difficulty levels and paper type detection for adaptive content generation

## 🚀 Quick Start

```bash
npx --yes @zlzliqing/claude-paper@latest install
```

## 📚 Learn more

**Install all supported agents**

Install Claude Code, Codex, OpenCode, and DeepSeek Harness with one command—no repository clone required: npx --yes @zlzliqing/claude-paper@latest install The default `all` target covers all four agents. For Claude Code, the installer uses the official Claude CLI to register the package-local marketplace and install or update the user-scoped plugin. For the other agents, it installs the shared Ski

**Keep upgrading only the agents selected during installation**

npx --yes @zlzliqing/claude-paper@latest upgrade --target codex,opencode The default upgrade target is `all`. If the existing installation only targets selected agents, pass the same `--target` list during upgrade so no additional agent integrations are added. The npm package copies its packaged plugin runtime to the user data directory, installs the generated compatibility Skills in `~/.agents/sk

## 🔗 Links

- [GitHub Repository](https://github.com/alaliqing/claude-paper)
- [Full README](https://github.com/alaliqing/claude-paper#readme)
- [Back to the Related Agent Harnesses list](../related.md)
