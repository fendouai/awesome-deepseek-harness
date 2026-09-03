---
title: "deepseek-harness-snowsalt"
description: "Snow-salt themed skin for DeepSeek Harness."
keywords: "deepseek-harness-snowsalt, ui, plugin, deepseek harness, dsh"
---
# deepseek-harness-snowsalt

> ⭐ **28** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 28 | Status | ✅ active |
| Author | [KYZHXL](https://github.com/KYZHXL) | Updated | 2026-08-13 |
| Subcategory | 🎨 Skins & themes | Capabilities | ui |

## One-liner

> Snow-salt themed skin for DeepSeek Harness.

## About

**Everything is a Plugin.** — 基于 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 的产品化魔改版，给你开箱即用的桌面 GUI、插件市场与多供应商一键接入。

## ✨ Key Features

- 重做对话区、输入条、侧边栏与空状态欢迎页，现代圆角风格
- Electron 桌面壳：原生窗口 + 系统托盘，双击即用（或浏览器访问）

## 📦 Install

```bash
# 1. 克隆本分支
git clone -b deepseek-harness-salt https://github.com/KYZHXL/deepseek-harness-snowsalt.git
cd deepseek-harness-snowsalt

# 2. 安装依赖（国内推荐 npmmirror 镜像）
pnpm install --registry=https://registry.npmmirror.com

# 3. 构建
pnpm run build

# 4. 启动 Web UI
pnpm dsh web
# 浏览器打开 http://127.0.0.1:3080
```

## 🚀 Quick Start

```bash
deepseek-harness-master/   # 魔改源码（继承上游，含全部改造）
desktop/                   # Electron 桌面壳（原生窗口 + 托盘）
plugin-manager/            # 独立插件管理器（已集成进 Web UI）
整合包/                     # 一键启动整合包（桌面壳 + 后端）
```

## 📚 Learn more

**方式一：桌面应用（安装版）**

1. 下载 **`DeepSeek-Harness-Setup-0.1.0.exe`**（[Releases](https://github.com/KYZHXL/deepseek-harness-snowsalt/releases)） 2. 安装后，将源码仓库放在安装目录同级（或设 `DSH_BACKEND_DIR` 指向源码目录），首次启动自动拉起后端 3. 双击桌面图标即可使用

## 🔗 Links

- [GitHub Repository](https://github.com/KYZHXL/deepseek-harness-snowsalt)
- [Full README](https://github.com/KYZHXL/deepseek-harness-snowsalt#readme)
- [Back to the Plugins list](../plugins.md)
