---
title: "awesome-dsh-presets"
description: "DSH 预设目录"
keywords: "awesome-dsh-presets, registry, awesome-list, search, deepseek harness, dsh"
---
# awesome-dsh-presets

> ⭐ **1** · ✅ 活跃 · 精选列表

| | | | |
|---|---|---|---|
| 类型 | 精选列表 | 分类 | 注册表 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [hackerFish](https://github.com/hackerFish) | 更新时间 | 2026-08-16 |

## 一句话介绍

> DSH 预设目录

## 详细介绍

**4 presets (2 derived from official shipped presets with attribution, 2 original) and 4 AGENTS.md rule packs. Every preset passes YAML/`!!js`-dialect parsing, structure checks, and package-existence validation against a real harness install.** [中文](README.zh.md) · Siblings: [dsh-lab](https://github.com/hackerFish/dsh-lab) · [awesome-dsh-skills](https://github.com/hackerFish/awesome-dsh-skills) · [dsh-video-studio](https://github.com/hackerFish/dsh-video-studio)

## ✨ 核心特性

- **Presets** (`agent.cordis.yml` + `preset.yml`): drop a directory into `~/.dsh/.agent-presets/` and pick it in new sessions (mechanism per official `@deepseek-a
- **Rules** (`rules/*.md`): append to `~/.dsh/AGENTS.md`.

## 📦 安装

```bash
git clone https://github.com/hackerFish/awesome-dsh-presets ~/dsh-presets
mkdir -p ~/.dsh/.agent-presets
cp -r ~/dsh-presets/presets/minimal-zh ~/.dsh/.agent-presets/   # pick what you need
cat ~/dsh-presets/rules/code-quality.md >> ~/.dsh/AGENTS.md
```

## 📚 更多信息

**Install**

git clone https://github.com/hackerFish/awesome-dsh-presets ~/dsh-presets mkdir -p ~/.dsh/.agent-presets cp -r ~/dsh-presets/presets/minimal-zh ~/.dsh/.agent-presets/ # pick what you need cat ~/dsh-presets/rules/code-quality.md >> ~/.dsh/AGENTS.md

## 🔗 链接

- [GitHub 仓库](https://github.com/hackerFish/awesome-dsh-presets)
- [完整 README](https://github.com/hackerFish/awesome-dsh-presets#readme)
- [返回awesome-dsh-presets所在分类](../awesome-lists.md)
