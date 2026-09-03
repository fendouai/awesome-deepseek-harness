---
title: "dsh-computer-use"
description: "computer-use in dsh"
keywords: "dsh-computer-use, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-computer-use

> ⭐ **5** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 5 | 状态 | ✅ 活跃 |
| 作者 | [JasonWei04](https://github.com/JasonWei04) | 更新时间 | — |

## 一句话介绍

> computer-use in dsh

## 详细介绍

Model-agnostic Computer Use capability for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness): an isolated browser, a Windows native helper, provider-neutral observation, a Chrome **Cookie Bridge** for importing your logged-in sessions, and a text planner (DeepSeek) plus a third-party vision model for perception.

## ✨ 核心特性

- **License**: [MIT](LICENSE) — open source, free to use, modify, and redistribute.
- **Platform**: the `windows` provider's native helper is **Windows-only**; the `playwright` browser provider and everything else are cross-platform.
- **macOS**: not currently developed — the author has no macOS environment. **Developers are welcome to contribute a macOS version.**

## 📦 安装

```bash
dsh plugin --profile web add dsh-computer-use
npx playwright install chromium   # once, for the playwright provider
```

## 🚀 快速开始

```bash
pnpm install
pnpm build      # tsdown bundles src into lib/ + dotnet publish the native helper into lib/native/win32-x64
pnpm test       # keyless contract tests (fake/framing/transport/windows/perception) + Playwright (needs Chromium)
pnpm typecheck
```

## 📚 更多信息

**Configuration**

All options live on the `dsh-computer-use/plugin` row (`config:`), for example in your profile's `cordis.patch.yml`: name: dsh-computer-use/plugin config: provider: playwright visionProvider: xiaomi visionModel: mimo-v2.5 > You can also flip the whole capability on/off **live from the DeepSeek Harness GUI** — the plugin registers a `computer-use` settings section (Settings → `computer-use`), so `e

**Install & load**

dsh plugin --profile web add dsh-computer-use npx playwright install chromium # once, for the playwright provider The bundle's `cordis.patch.yml` mounts `ctx.computerUse` (package root) and the tool/provider plugin (`dsh-computer-use/plugin`, provider `fake`). Override `provider` in your profile patch to select `playwright` or `windows`.

## 🔗 链接

- [GitHub 仓库](https://github.com/JasonWei04/dsh-computer-use)
- [完整 README](https://github.com/JasonWei04/dsh-computer-use#readme)
- [返回dsh-computer-use所在分类](../plugins.md)
