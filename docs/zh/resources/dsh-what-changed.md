---
title: "dsh-what-changed"
description: "会话顶栏的整会话改动审阅。列出本次会话 Agent 写过的每个文件与逐处改动，被权限拒绝的写入单独计数不算改动，数据来自 session projection 而非磁盘日志。"
keywords: "dsh-what-changed, developer, plugin, ui, deepseek harness, dsh"
---
# dsh-what-changed

> ⭐ **2** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [sjh9714](https://github.com/sjh9714) | 更新时间 | 2026-08-19 |
| 子分类 | 🧪 代码·测试·审查 | 能力 | ui |

## 一句话介绍

> 会话顶栏的整会话改动审阅。列出本次会话 Agent 写过的每个文件与逐处改动，被权限拒绝的写入单独计数不算改动，数据来自 session projection 而非磁盘日志。

## 详细介绍

**看得见 Agent 到底改了什么。一个会话里所有文件改动，一屏看完再决定要不要提交。** [English](./README.en.md) <p> </p> 真实 `dsh web` 会话，不是拼的图。顶栏上的「1 个文件 · 1 处编辑」就是这个插件，点开是这一屏。

## 📦 安装

```bash
dsh plugin --profile web add dsh-what-changed
```

## 🚀 快速开始

```bash
Failed to load plugins
bundle .../client.js loaded without registering "dsh-what-changed" via __ModuleLoader__.load
```

## 🔗 链接

- [GitHub 仓库](https://github.com/sjh9714/dsh-what-changed)
- [完整 README](https://github.com/sjh9714/dsh-what-changed#readme)
- [返回dsh-what-changed所在分类](../plugins.md)
