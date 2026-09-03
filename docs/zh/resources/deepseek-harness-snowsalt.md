---
title: "deepseek-harness-snowsalt"
description: "雪盐主题皮肤。"
keywords: "deepseek-harness-snowsalt, ui, plugin, deepseek harness, dsh"
---
# deepseek-harness-snowsalt

> ⭐ **28** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 28 | 状态 | ✅ 活跃 |
| 作者 | [KYZHXL](https://github.com/KYZHXL) | 更新时间 | 2026-08-13 |
| 子分类 | 🎨 皮肤与主题 | 能力 | ui |

## 一句话介绍

> 雪盐主题皮肤。

## 详细介绍

**Everything is a Plugin.** — 基于 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 的产品化魔改版，给你开箱即用的桌面 GUI、插件市场与多供应商一键接入。

## ✨ 核心特性

- 重做对话区、输入条、侧边栏与空状态欢迎页，现代圆角风格
- Electron 桌面壳：原生窗口 + 系统托盘，双击即用（或浏览器访问）

## 📦 安装

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

## 🚀 快速开始

```bash
deepseek-harness-master/   # 魔改源码（继承上游，含全部改造）
desktop/                   # Electron 桌面壳（原生窗口 + 托盘）
plugin-manager/            # 独立插件管理器（已集成进 Web UI）
整合包/                     # 一键启动整合包（桌面壳 + 后端）
```

## 📚 更多信息

**方式一：桌面应用（安装版）**

1. 下载 **`DeepSeek-Harness-Setup-0.1.0.exe`**（[Releases](https://github.com/KYZHXL/deepseek-harness-snowsalt/releases)） 2. 安装后，将源码仓库放在安装目录同级（或设 `DSH_BACKEND_DIR` 指向源码目录），首次启动自动拉起后端 3. 双击桌面图标即可使用

## 🔗 链接

- [GitHub 仓库](https://github.com/KYZHXL/deepseek-harness-snowsalt)
- [完整 README](https://github.com/KYZHXL/deepseek-harness-snowsalt#readme)
- [返回deepseek-harness-snowsalt所在分类](../plugins.md)
