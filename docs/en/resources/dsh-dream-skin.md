---
title: "dsh-dream-skin"
description: "One-command skinning for DSH Web: 8 original themes, wallpaper (opacity/blur/gradient/URL), per-user accent, shareable theme packs, favorites and surprise-me — purely native on DSH's token system."
keywords: "dsh-dream-skin, ui, plugin, deepseek harness, dsh"
---
# dsh-dream-skin

> ⭐ **73** · ✅ active · plugin · ⬆️ +5 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 73 | Status | ✅ active |
| Author | [RevolutionLA](https://github.com/RevolutionLA) | Updated | 2026-08-21 |
| Subcategory | 🎨 Skins & themes | Capabilities | ui |

## One-liner

> One-command skinning for DSH Web: 8 original themes, wallpaper (opacity/blur/gradient/URL), per-user accent, shareable theme packs, favorites and surprise-me — purely native on DSH's token system.

## About

**为 DeepSeek Harness 换上一张克制、清透、有质感的「脸」。** 原生换肤 · 背景壁纸 · 强调色 · 主题包 —— 一条 `--dsw-*` token 生态内的优雅实现。装一次，用很久。 ---

## 📦 Install

```bash
dsh plugin --profile web add dsh-dream-skin && dsh web
```

## 🚀 Quick Start

```bash
┌────────────── dsh-dream-skin（标准 dsh-plugin / 双面插件）──────────────┐
            │  dsh.bundle   → cordis.patch.yml 插入 dream-skin 入口   (host 半边)     │
            │  dsh.client   → lib/client.js（浏览器 bundle）          (浏览器半边)     │
            └─────────────────────────────────────────────────────────────────────────┘
```

## 📚 Learn more

**🎨 预览 — Mirage 幻梦系列**

> **玩法一 · 开箱即用的优雅。** 8 套皮肤，由各皮肤的**真实 token + 专属弥散光背景**生成——所见即所得。点开可放大查看精致材质。 <table> <tr> <td align="center"><a href="docs/previews/abyss.png"></a><br/><b>abyss</b> · 沉静蓝</td> <td align="center"><a href="docs/previews/aurora.png"></a><br/><b>aurora</b> · 极光青</td> <td align="center"><a href="docs/previews/nebula.png"></a><br/><b>nebula</b> · 星云紫</td> <td align="center"><a href="docs/previews/ember.

**⚡ 一句话安装**

**复制下面这句话给你的 DSH，它自己会装好一切：** > 请帮我安装 dsh-dream-skin 换肤插件（https://github.com/RevolutionLA/dsh-dream-skin 或 npm 的 dsh-dream-skin），装完告诉我如何重启 DSH Web。 不想麻烦 Agent？命令行一条： dsh plugin --profile web add dsh-dream-skin && dsh web > 🚀 **现已发布到 npm！** 装好 DSH 后，一条命令即可安装，无需 clone。 > **致敬 [Codex-Dream-Skin](https://github.com/Fei-Away/Codex-Dream-Skin)。** 但实现路径不同：Codex 是往桌面客户端渲染进程 > 注入 CSS（CDP），而 DSH 本身是 **token 

**方式二：从 GitHub 安装（固定到已验证的提交）**

dsh plugin --profile web add 'github:RevolutionLA/dsh-dream-skin#<40位commit>' > 固定到 release 对应的 commit，之后 `main` 的新改动不会静默改变已安装代码。

**方式三：从 Release tarball 安装（离线 / 不便走 git 的环境）**

从本仓库 [Releases](https://github.com/RevolutionLA/dsh-dream-skin/releases) 下载 `dsh-dream-skin-<版本>.tgz`（内含构建好的 `lib/client.js`，安装时无需执行任何 prepare 脚本），然后： dsh plugin --profile web add ./dsh-dream-skin-<版本>.tgz

## 🔗 Links

- [GitHub Repository](https://github.com/RevolutionLA/dsh-dream-skin)
- [Full README](https://github.com/RevolutionLA/dsh-dream-skin#readme)
- [Back to the Plugins list](../plugins.md)
