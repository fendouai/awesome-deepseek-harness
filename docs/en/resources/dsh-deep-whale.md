---
title: "dsh-deep-whale"
description: "Whale-girl skin series for DSH Web (CC BY-NC-SA 4.0)."
keywords: "dsh-deep-whale, ui, plugin, deepseek harness, dsh"
---
# dsh-deep-whale

> ⭐ **1,548** · ✅ active · plugin · ⬆️ +49 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 1,548 | Status | ✅ active |
| Author | [Small-tailqwq](https://github.com/Small-tailqwq) | Updated | 2026-08-21 |
| Subcategory | 🎨 Skins & themes | Capabilities | ui |

## One-liner

> Whale-girl skin series for DSH Web (CC BY-NC-SA 4.0).

## About

**[简体中文](README.md)** · [English](README.en.md) DeepSeek Harness Web GUI 的鲸鱼娘主题皮肤系列(独立分发仓库)。

## 📦 Install

```bash
dsh plugin --profile web add 'github:Small-tailqwq/dsh-deep-whale#path:/skin-manager' && dsh plugin --profile web add 'github:Small-tailqwq/dsh-deep-whale#path:/maid-atelier' && dsh plugin --profile web add 'github:Small-tailqwq/dsh-deep-whale#path:/orca-link'
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add 'github:Small-tailqwq/dsh-deep-whale#path:/skin-manager'; dsh plugin --profile web add 'github:Small-tailqwq/dsh-deep-whale#path:/maid-atelier'; dsh plugin --profile web add 'github:Small-tailqwq/dsh-deep-whale#path:/orca-link'
```

## 📚 Learn more

**一行安装（推荐）**

三个发行包（皮肤管理器 + 两套皮肤）直接以 GitHub 依赖安装，**无需 clone**；每个包都是仓库中的一个 `#path:` 子目录。需要 **pnpm ≥ 9**:子目录语法从 pnpm 9 开始支持，pnpm 8 会把 `path:...` 当作 commit 引用而报错。 **Linux / macOS / WSL:** dsh plugin --profile web add 'github:Small-tailqwq/dsh-deep-whale#path:/skin-manager' && dsh plugin --profile web add 'github:Small-tailqwq/dsh-deep-whale#path:/maid-atelier' && dsh plugin --profile web add 'github:Small-tailqwq/

**独立子包安装（本地开发与弱网备用）**

> 普通用户不需要使用本节：GitHub 一行安装更快（无需 clone）。本节用于本地开发、指定提交测试，或 GitHub 网络不可用时。GitHub 依赖与本地 link 针对同一包名，用哪种就执行哪种，不要混跑。 git clone --depth 1 https://github.com/Small-tailqwq/dsh-deep-whale # clone 到任意位置（浅克隆足够，跳过历史） node <clone 的绝对路径>/.agents/skills/dsh-skin-install/scripts/stage-mutual-exclusion.mjs --profile web --target maid-atelier dsh plugin --profile web add <clone 的绝对路径>/skin-manager # 常驻皮肤管理面板（推荐） dsh

**示例：只启用 maid-atelier；改为 orca-link 时把 false 移到它那行，两套皮肤只能有一套是 f**

disabled: false disabled: true disabled: false > 若 patch 文件还是 dsh 的默认模板（注释 + 一行 `[]`），请**用上面的列表整体替换 `[]` 那一行**——“注释 + `[]` + 其他条目”是非法 YAML，配置解析会失败（服务器会保留上一个可用配置继续运行，修复后并刷新即可）。 Windows 示例（正斜杠与反斜杠均可，pnpm 会自动规范化）： dsh plugin --profile web add C:/Users/<你>/code/dsh-deep-whale/skin-manager dsh plugin --profile web add C:/Users/<你>/code/dsh-deep-whale/maid-atelier

**安装后验证**

dsh plugin --profile web list # 应看到三个 @dsh-external/dsh-client-ui-skin-* 依赖 dsh --profile web --dump-config # manager 行 disabled: false；两套皮肤互斥：skins 恰一套 false > 一行安装后、**尚未重启前** `--dump-config` 的状态取决于你的 patch 层：干净环境下两套皮肤都还没有互斥行（默认启用，是正常过渡态——首次重启时 skin-manager 兜底回退并写入互斥行）；若 home 层残留过互斥行（之前装过本仓库皮肤又卸载），则直接沿用该状态。冷启动后还必须在浏览器控制台检查 client roster（仅有配置 entry 不代表浏览器包已注册）。启动页 HTML 必须引用 manager 与启用皮肤的 `/plugin

## 🔗 Links

- [GitHub Repository](https://github.com/Small-tailqwq/dsh-deep-whale)
- [Full README](https://github.com/Small-tailqwq/dsh-deep-whale#readme)
- [Back to the Plugins list](../plugins.md)
