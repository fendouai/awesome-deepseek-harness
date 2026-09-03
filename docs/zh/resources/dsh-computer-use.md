---
title: "dsh-computer-use"
description: "Computer Use 插件：虚拟鼠标真人操作 for DeepSeek Harness（screen_observe + computer_click 等 11 个模型友好工具，跨平台 cua-driver 引擎）"
keywords: "dsh-computer-use, vision, plugin, browser, coding, deepseek harness, dsh"
---
# dsh-computer-use

> ⭐ **17** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 17 | 状态 | ✅ 活跃 |
| 作者 | [988hj7tczd-oss](https://github.com/988hj7tczd-oss) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | browser, coding |

## 一句话介绍

> Computer Use 插件：虚拟鼠标真人操作 for DeepSeek Harness（screen_observe + computer_click 等 11 个模型友好工具，跨平台 cua-driver 引擎）

## 详细介绍

**中文文档 · English documentation** - [中文文档](#中文文档) - [English Documentation](#english-documentation)

## ✨ 核心特性

- [中文文档](#中文文档)
- [English Documentation](#english-documentation)

## 📦 安装

```bash
git clone https://github.com/988hj7tczd-oss/dsh-computer-use.git
cd dsh-computer-use

# 先预演，不写入配置
./install.sh --dry-run

# 安装到用户级 patch 层
./install.sh

# 安装后重启 harness-desktop
```

## 🚀 快速开始

```bash
export DSH_HOME="/path/to/your/dsh-home"
./install.sh --dry-run
./install.sh
```

## 📚 更多信息

**方式一：使用 harness-desktop**

普通桌面用户建议先下载 [harness-desktop](https://github.com/988hj7tczd-oss/harness-desktop/releases)。它是一个开箱即用的 DeepSeek Harness 桌面客户端，支持 macOS、Windows 和 Linux。 1. 下载并启动 harness-desktop 2. 完成首启配置 3. 安装本插件 4. 重启 harness-desktop 5. 在对话中让 Agent 操作桌面

**方式二：从 GitHub 源码安装**

git clone https://github.com/988hj7tczd-oss/dsh-computer-use.git cd dsh-computer-use

**安装后重启 harness-desktop**

安装脚本只做两件事： 1. 将插件链接到 `$DSH_HOME/profiles/web/node_modules/dsh-computer-use`； 2. 在 `$DSH_HOME/cordis.patch.yml` 注册插件。 脚本使用用户级 patch 层，不修改项目代码，也不修改其他 profile 的配置。

**配置**

插件配置位于 DSH 的用户级 patch 层： config: ttlMs: 30000 maxElements: 500 allowedApps: [] cursorTheme: com.dsh.computeruse.rainbow nativeImage: auto visionProvider: deepseek-official visionModel: deepseek-v4-flash-vision-exp > 安装脚本或 bundle patch 可能覆盖代码层默认值。请以实际生成的 `$DSH_HOME/cordis.patch.yml` 为准；多步任务建议显式写入 `ttlMs`，不要依赖隐式默认值。

## 🔗 链接

- [GitHub 仓库](https://github.com/988hj7tczd-oss/dsh-computer-use)
- [完整 README](https://github.com/988hj7tczd-oss/dsh-computer-use#readme)
- [返回dsh-computer-use所在分类](../plugins.md)
