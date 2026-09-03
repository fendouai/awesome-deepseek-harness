---
title: "dsh-browser"
description: "Browser capability for DeepSeek Harness: headed Edge/Playwright provider, SSRF-safe navigation, a11y-ref clicking, permission gate with auto-remember, gated evaluate"
keywords: "dsh-browser, browser, integration, coding, deepseek harness, dsh"
---
# dsh-browser

> ⭐ **8** · ✅ 活跃 · 集成 · 近期 ⬆️ +3

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 浏览器控制 |
| 星数 | ⭐ 8 | 状态 | ✅ 活跃 |
| 作者 | [xylt369](https://github.com/xylt369) | 更新时间 | 2026-08-15 |

## 一句话介绍

> Browser capability for DeepSeek Harness: headed Edge/Playwright provider, SSRF-safe navigation, a11y-ref clicking, permission gate with auto-remember, gated evaluate

## 详细介绍

[English](README.en.md) | **中文** | [Español](README.es.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [العربية](README.ar.md) 为 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（`dsh`）提供完整的浏览器能力：导航、可读快照、点击与填表、多标签、截图，以及可接入识图模型的图像附件。 目标宿主：**dsh `0.1.0-rc.7` / `0.1.1-rc.2`**。默认驱动本机 **Microsoft Edge**（持久登录态 + 轻量反检测），并兼容 Clash / Surge 的 fake-ip DNS。 当前发布版本： 仓库与发行说明：https://github.com/xylt369/dsh-browser/releases/tag/v0.8.1 ---

## 📦 安装

```bash
dsh plugin --profile web add \
  @yeesy369/dsh-browser-playwright@0.8.1 \
  @yeesy369/dsh-tool-browser@0.7.0 \
  @yeesy369/dsh-web-permission@0.6.1
```

## 🚀 快速开始

```bash
# $DSH_HOME/settings.yaml — web-permission（热更新）
web-permission:
  defaultAction: ask
  remember: true
```

## 📚 更多信息

**安装**

1. 确认已安装 `dsh`（`dsh --version`）。未安装时执行 `npm i -g @deepseek-ai/dsh`。 2. 安装插件： dsh plugin --profile web add \ @yeesy369/dsh-browser-playwright@0.8.1 \ @yeesy369/dsh-tool-browser@0.7.0 \ @yeesy369/dsh-web-permission@0.6.1 3. 重启 `dsh web`。 4. 在对话中请求打开网页；需要登录时在弹出的 Edge 窗口中完成一次即可（状态保存在 `~/.dsh/edge-profile`）。 升级已有安装时，请使用上方带版本号的 `plugin add`，然后重启 `dsh web`。 ---

## 🔗 链接

- [GitHub 仓库](https://github.com/xylt369/dsh-browser)
- [完整 README](https://github.com/xylt369/dsh-browser#readme)
- [返回dsh-browser所在分类](../integrations.md)
