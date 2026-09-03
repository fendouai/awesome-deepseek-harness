---
title: "dsh-theme-plugin"
description: "Chinese traditional colors as a DeepSeek Harness theme pack."
keywords: "dsh-theme-plugin, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-theme-plugin

> ⭐ **19** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 19 | 状态 | ✅ 活跃 |
| 作者 | [nevertoday](https://github.com/nevertoday) | 更新时间 | 2026-08-15 |
| 子分类 | 🎨 皮肤与主题 | 能力 | coding, ui |

## 一句话介绍

> Chinese traditional colors as a DeepSeek Harness theme pack.

## 详细介绍

Chinese traditional colors as a **DeepSeek Harness theme pack**. 49 anchor colors × light/dark = **98 themes**, each writing the full token vocabulary (98 tokens: 89 `--dsw-*` plus 9 `--shiki-token-*` syntax slots) and clearing WCAG AA on all 3136 contrast assertions. Twelve of the anchors are marked as a curated shortlist. 📖 [中文文档](./README.zh-CN.md) 竹青 · light（素绢）  |  朱红 · dark（熟宣）群青 · light（雪青）  |  藤黄 · dark（赭纸） One anchor per paper family, same conversation in each. The most saturated patch on screen is always the color you picked.

## ✨ 核心特性

- **Verify** — the browser console logs `registered 98/98 themes (49 light / 49 dark)`, and `dsh --profile web --dump-config` shows a `theme-zhongguo` row.
- **Update** — run the same `add` command again.
- **Uninstall** — `dsh plugin --profile web remove dsh-theme-plugin`

## 📦 安装

```bash
npx -y @deepseek-ai/dsh plugin --profile web add dsh-theme-plugin@latest
npx -y @deepseek-ai/dsh --profile web          # boot → open http://127.0.0.1:3080/
```

## 🚀 快速开始

```bash
http://127.0.0.1:3080/#theme=zhuqing-light      # 竹青 light
http://127.0.0.1:3080/#theme=qunqing-dark       # 群青 dark
```

## 📚 更多信息

**Install**

npx -y @deepseek-ai/dsh plugin --profile web add dsh-theme-plugin@latest npx -y @deepseek-ai/dsh --profile web # boot → open http://127.0.0.1:3080/ This pulls the prebuilt bundle from npm — no clone, no build step. The `web` profile is created on first boot under `~/.dsh/profiles/web`.

**Usage**

Open **Settings → Traditional Colors** and pick a theme; it applies immediately. Themes also have deep links: http://127.0.0.1:3080/#theme=zhuqing-light # 竹青 light http://127.0.0.1:3080/#theme=qunqing-dark # 群青 dark Changing the hash switches themes live. A deep link wins over your remembered pick. The remembered pick lives in `localStorage`, not in `settings.yaml`, so it does not follow you acros

## 🔗 链接

- [GitHub 仓库](https://github.com/nevertoday/dsh-theme-plugin)
- [完整 README](https://github.com/nevertoday/dsh-theme-plugin#readme)
- [返回dsh-theme-plugin所在分类](../plugins.md)
