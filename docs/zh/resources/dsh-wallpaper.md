---
title: "dsh-wallpaper"
description: "Wallpaper Engine 壁纸联动插件"
keywords: "dsh-wallpaper, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-wallpaper

> ⭐ **6** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [codeMonkey-Pine](https://github.com/codeMonkey-Pine) | 更新时间 | — |

## 一句话介绍

> Wallpaper Engine 壁纸联动插件

## 详细介绍

用一张图片作为 DSH Web 界面的窗口背景，并可通过右下角小面板实时控制： - **图片透明度**（0–100%） - **面板透明度**（0–100%，越小背景图越透） - **压暗遮罩**（0–100%，提高文字可读性） - **背景模糊**（0–40px）

## ✨ 核心特性

- **图片透明度**（0–100%）
- **面板透明度**（0–100%，越小背景图越透）
- **压暗遮罩**（0–100%，提高文字可读性）
- **背景模糊**（0–40px）

## 📦 安装

```bash
dsh plugin --profile web add dsh-wallpaper     # npm 包名
# 或
dsh plugin --profile web add <owner>/dsh-wallpaper   # GitHub 仓库
```

## 🚀 快速开始

```bash
dsh --profile web
```

## 📚 更多信息

**安装**

发布到 npm 后（或直接以 GitHub 仓库 `owner/repo` 形式），一条命令装进 web profile： dsh plugin --profile web add dsh-wallpaper # npm 包名

**使用**

1. 页面右下角出现 🖼 按钮，点开面板： - 选本地图片 / 粘贴图片链接 → 应用； - 拖动滑块实时调整透明度 / 遮罩 / 模糊； - 「移除图片」或「恢复默认」关闭壁纸。 2. 配置自动保存在浏览器本地，刷新 / 重开浏览器仍生效（换浏览器需重新设置）。

## 🔗 链接

- [GitHub 仓库](https://github.com/codeMonkey-Pine/dsh-wallpaper)
- [完整 README](https://github.com/codeMonkey-Pine/dsh-wallpaper#readme)
- [返回dsh-wallpaper所在分类](../plugins.md)
