---
title: "awesome-dsh-presets"
description: "实测可用的 DeepSeek Harness 预设与规则合集：官方派生 + 原创组合，每个预设通过结构与包存在性校验（中文优先）"
keywords: "awesome-dsh-presets, registry, awesome-list, search, deepseek harness, dsh"
---
# awesome-dsh-presets

> ⭐ **1** · ✅ active · awesome-list

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [hackerFish](https://github.com/hackerFish) | Updated | 2026-08-16 |

## One-liner

> 实测可用的 DeepSeek Harness 预设与规则合集：官方派生 + 原创组合，每个预设通过结构与包存在性校验（中文优先）

## About

**4 presets (2 derived from official shipped presets with attribution, 2 original) and 4 AGENTS.md rule packs. Every preset passes YAML/`!!js`-dialect parsing, structure checks, and package-existence validation against a real harness install.** [中文](README.zh.md) · Siblings: [dsh-lab](https://github.com/hackerFish/dsh-lab) · [awesome-dsh-skills](https://github.com/hackerFish/awesome-dsh-skills) · [dsh-video-studio](https://github.com/hackerFish/dsh-video-studio)

## ✨ Key Features

- **Presets** (`agent.cordis.yml` + `preset.yml`): drop a directory into `~/.dsh/.agent-presets/` and pick it in new sessions (mechanism per official `@deepseek-a
- **Rules** (`rules/*.md`): append to `~/.dsh/AGENTS.md`.

## 📦 Install

```bash
git clone https://github.com/hackerFish/awesome-dsh-presets ~/dsh-presets
mkdir -p ~/.dsh/.agent-presets
cp -r ~/dsh-presets/presets/minimal-zh ~/.dsh/.agent-presets/   # pick what you need
cat ~/dsh-presets/rules/code-quality.md >> ~/.dsh/AGENTS.md
```

## 📚 Learn more

**Install**

git clone https://github.com/hackerFish/awesome-dsh-presets ~/dsh-presets mkdir -p ~/.dsh/.agent-presets cp -r ~/dsh-presets/presets/minimal-zh ~/.dsh/.agent-presets/ # pick what you need cat ~/dsh-presets/rules/code-quality.md >> ~/.dsh/AGENTS.md

## 🔗 Links

- [GitHub Repository](https://github.com/hackerFish/awesome-dsh-presets)
- [Full README](https://github.com/hackerFish/awesome-dsh-presets#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
