---
title: "dsh-sticky-note"
description: "左下角便签：随手记点子/感想/TODO，实时保存到归档目录，清单+悬浮归档"
keywords: "dsh-sticky-note, input-editing, plugin, coding, deepseek harness, dsh"
---
# dsh-sticky-note

> ⭐ **11** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 输入与编辑 |
| 星数 | ⭐ 11 | 状态 | ✅ 活跃 |
| 作者 | [Meredith2328](https://github.com/Meredith2328) | 更新时间 | 2026-08-19 |

## 一句话介绍

> 左下角便签：随手记点子/感想/TODO，实时保存到归档目录，清单+悬浮归档

## 详细介绍

- 📝 **随手记**：编辑框工具栏上的便签按钮，点击弹出便签面板 - 💾 **自动保存**：按设定间隔（10 秒 / 1 分钟 / 5 分钟）自动落盘，`Ctrl+S` 立即保存 - 🏷️ **三分类**：点子 / 感想 / TODO，快捷键 `Ctrl+Shift+1/2/3` 切换 - 📤 **一键发送**：便签内容直接发给当前对话（或追加到输入框） - 📋 **历史便签**：分组清单 + 展开收起，双击查看、单击预备发送，归档分组可一键恢复 - ✏️ **可编辑**：历史便签可二次编辑保存；外部编辑器改动后查看视图自动刷新 - 📌 **选择保留**：标记保留的便签不会被自动清除（针形图标） - 🧹 **自动清除**：按最后修改时间计龄，超期未保留的先移入「已清除」回收站（保留 30 天），Host 定时触发 - 🖥️ **Markdown**：编辑 ↔ 实时预览（`Ctrl+Shift+V`），支持表格 / 任务列表 / 删除线 / 图片 - 🌓 **深色模式**：全部配色跟随 DSW 主题变量，深浅自动切换 - ⌨️ **快捷键**：`Esc` 层层退出、`Tab/Shift+Tab` 缩进、`Ctrl+Shift+X` 删除线、`Ctrl+Shift+T` 任务项、`Ctrl+T` 表格骨架等 - ⚙️ **可配置**：存储路径、保存间隔、清除周期、默认类别、发送方式

## ✨ 核心特性

- 📝 **随手记**：编辑框工具栏上的便签按钮，点击弹出便签面板
- 💾 **自动保存**：按设定间隔（10 秒 / 1 分钟 / 5 分钟）自动落盘，`Ctrl+S` 立即保存
- 🏷️ **三分类**：点子 / 感想 / TODO，快捷键 `Ctrl+Shift+1/2/3` 切换
- 📤 **一键发送**：便签内容直接发给当前对话（或追加到输入框）
- 📋 **历史便签**：分组清单 + 展开收起，双击查看、单击预备发送，归档分组可一键恢复
- ✏️ **可编辑**：历史便签可二次编辑保存；外部编辑器改动后查看视图自动刷新
- 📌 **选择保留**：标记保留的便签不会被自动清除（针形图标）
- 🧹 **自动清除**：按最后修改时间计龄，超期未保留的先移入「已清除」回收站（保留 30 天），Host 定时触发

## 📦 安装

```bash
dsh plugin --profile web add dsh-sticky-note
```

## 🚀 快速开始

```bash
dsh plugin --profile web add file:/path/to/dsh-sticky-note
```

## 📚 更多信息

**📦 安装**

dsh plugin --profile web add dsh-sticky-note 或本地目录： dsh plugin --profile web add file:/path/to/dsh-sticky-note 安装后重启 DSH（Web 或 Desktop）。 **版本要求**：需要 DSH `0.1.0-rc.7` 及以上（设置卡片注册适配 keyed slot 强校验），已验证兼容至 `0.1.1-rc.2`；旧版 DSH 请使用 v0.2.1。v0.2.3 起 peerDependencies 范围放宽以覆盖 `0.1.1` 预发布系列（运行时本就兼容）。

## 🔗 链接

- [GitHub 仓库](https://github.com/Meredith2328/dsh-sticky-note)
- [完整 README](https://github.com/Meredith2328/dsh-sticky-note#readme)
- [返回dsh-sticky-note所在分类](../plugins.md)
