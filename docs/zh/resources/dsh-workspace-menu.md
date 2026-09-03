---
title: "dsh-workspace-menu"
description: "DSH workspace/chat enhancement menu: pin, rename, open in file explorer, archive, fork, copy, new window. Settings integrated into General."
keywords: "dsh-workspace-menu, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-workspace-menu

> ⭐ **2** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [0imzero](https://github.com/0imzero) | 更新时间 | — |
| 子分类 | 📁 文件与导入 | 能力 | coding |

## 一句话介绍

> DSH workspace/chat enhancement menu: pin, rename, open in file explorer, archive, fork, copy, new window. Settings integrated into General.

## 详细介绍

把 DSH 主页的工作区和会话管理补齐：双击或右键，就能置顶、重命名、打开资源管理器、归档、分叉、复制、新窗口打开。所有开关都收在通用设置里，按需开启。

## ✨ 核心特性

- **工作区操作**：置顶、重命名、在资源管理器中打开、复制路径、新建会话、从列表移除、删除工作区（含磁盘）
- **会话操作**：置顶、重命名、标记未读/已读、归档、分叉、复制会话链接、复制会话标题、在新窗口中打开、打开所在目录、删除会话（含磁盘记录）
- **跨平台**：Windows 用资源管理器，macOS 用 Finder，Linux 自动选择 `xdg-open` / `gio` / 常见文件管理器
- **设置集成**：功能开关放在 DSH 通用设置里，支持折叠，逐项开关，不用的时候不会占菜单
- **不动内置源码**：通过 DOM 事件和 React fiber 定位工作区/会话行，不修改 DSH 自带代码
- **删除与归档管理不冲突**：永久删除会话复用 `@mlgbnb/dsh-archive-manager`，本插件只负责移除工作区目录，不直接改写归档/projcache 文件

## 📦 安装

```bash
dsh plugin --profile web add dsh-external-dsh-workspace-menu-1.2.0.tgz
```

## 🚀 快速开始

```bash
npm install
npm run build
```

## 📚 更多信息

**安装**

从 Releases 下载 tgz，然后： dsh plugin --profile web add dsh-external-dsh-workspace-menu-1.2.0.tgz 本地开发： npm install npm run build

## 🔗 链接

- [GitHub 仓库](https://github.com/0imzero/dsh-workspace-menu)
- [完整 README](https://github.com/0imzero/dsh-workspace-menu#readme)
- [返回dsh-workspace-menu所在分类](../plugins.md)
