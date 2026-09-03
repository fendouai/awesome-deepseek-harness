---
title: "dsh-client-ui-skins"
description: "DSH Web skin plugin with built-in themes and custom image skins"
keywords: "dsh-client-ui-skins, search, plugin, coding, multimodal, ui, deepseek harness, dsh"
---
# dsh-client-ui-skins

> ⭐ **11** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 11 | Status | ✅ active |
| Author | [caoyiwei850](https://github.com/caoyiwei850) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, multimodal, ui |

## One-liner

> DSH Web skin plugin with built-in themes and custom image skins

## About

给 DeepSeek Harness (DSH) Web 界面换肤：4 套内置皮肤 + 自定义图片/视频皮肤。 自定义皮肤把整张图片（PNG / JPG / WebP）或视频（MP4 / WebM）作为界面背景， 整套配色（背景、强调色、交互高亮）自动跟随画面主色调。 主要特性： - **4 套内置皮肤**：深海蓝 / 樱粉 / 薄荷 / 琥珀，深色浅色外观都适配。 - **自定义图片壁纸**：任意 PNG / JPG / WebP，配色自动取自主图。 - **视频动态壁纸**：MP4 / WebM 循环播放，首帧取色生成配色。 - **背景遮罩滑块**：独立调节壁纸明暗，避免文字被背景图吃掉。 - **输入框不透明度滑块**：独立调节输入框背景，保证打字清晰。 - **正文加强开关**：给助手正文加一层轻磨砂底，照片高光区也不影响阅读。

## ✨ Key Features

- **4 套内置皮肤**：深海蓝 / 樱粉 / 薄荷 / 琥珀，深色浅色外观都适配。
- **自定义图片壁纸**：任意 PNG / JPG / WebP，配色自动取自主图。
- **视频动态壁纸**：MP4 / WebM 循环播放，首帧取色生成配色。
- **背景遮罩滑块**：独立调节壁纸明暗，避免文字被背景图吃掉。
- **输入框不透明度滑块**：独立调节输入框背景，保证打字清晰。
- **正文加强开关**：给助手正文加一层轻磨砂底，照片高光区也不影响阅读。

## 📦 Install

```bash
# 1. 装包
cd ~/.dsh/profiles/web && pnpm add -w ./dsh-client-ui-skins-0.1.13.tgz

# 2. 注册（编辑 ~/.dsh/profiles/web/cordis.patch.yml，追加：）
#    - insert:
#        - id: ui-skins
#          name: 'dsh-client-ui-skins'

# 3. 重启 web
launchctl kickstart -k gui/$(id -u)/com.deepseek.dsh.web
```

## 🚀 Quick Start

```bash
bash uninstall-dsh-skins.sh
```

## 🔗 Links

- [GitHub Repository](https://github.com/caoyiwei850/dsh-client-ui-skins)
- [Full README](https://github.com/caoyiwei850/dsh-client-ui-skins#readme)
- [Back to the Plugins list](../plugins.md)
