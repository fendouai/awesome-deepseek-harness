---
title: "dsh-memory-evolve"
description: "跨会话长期记忆 + 后台自我进化：五轨记忆、git 分支感知、回合内自我审查、技能自我进化。"
keywords: "dsh-memory-evolve, memory, plugin, context, automation, deepseek harness, dsh"
---
# dsh-memory-evolve

> ⭐ **211** · ✅ 活跃 · 插件 · 近期 ⬆️ +6

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 记忆与上下文 |
| 星数 | ⭐ 211 | 状态 | ✅ 活跃 |
| 作者 | [csyangwen](https://github.com/csyangwen) | 更新时间 | 2026-08-19 |
| 子分类 | 🧠 记忆系统 | 能力 | memory, context, automation |

## 一句话介绍

> 跨会话长期记忆 + 后台自我进化：五轨记忆、git 分支感知、回合内自我审查、技能自我进化。

## 详细介绍

插件包内自带 `cordis.patch.yml`（`dsh.bundle.patch` 声明），`dsh plugin add` 安装后 **host 端自动注册，无需任何手动配置**。以 web profile 为例，两步装好：

## 📦 安装

```bash
# 1. 安装到 profile（本地目录用 link:，也可用 git/registry 包地址）
dsh plugin --profile web add github:csyangwen/dsh-memory-evolve

# 2. 重启 dsh web 即生效
```

## 🚀 快速开始

```bash
- id: dsh-memory-evolve
  config:
    reviewEnabled: true      # 开启回合内记忆审查（默认关）
    reviewInterval: 10       # 每 10 个用户回合审查一次
```

## 📚 更多信息

**dsh-memory-evolve 使用场景指南**

> **一句话**：让 DSH 里的 AI 拥有跨会话的长期记忆、帮你管理待办与技能、还能拉起一群 AI 会话和外部 AI 代理协同干活——**越用越懂你，换会话不丢上下文**。 > > 本指南按真实工作流组织，每个场景讲「适合谁、能做什么、怎么用、会得到什么」。 > > 相关文档：[详细功能说明](README-详细说明.md) · [记忆同步](docs/记忆同步.md) · [更新日志](docs/CHANGELOG.md) · [English](README.en.md) ---

**快速开始（安装）**

插件包内自带 `cordis.patch.yml`（`dsh.bundle.patch` 声明），`dsh plugin add` 安装后 **host 端自动注册，无需任何手动配置**。以 web profile 为例，两步装好：

## 🔗 链接

- [GitHub 仓库](https://github.com/csyangwen/dsh-memory-evolve)
- [完整 README](https://github.com/csyangwen/dsh-memory-evolve#readme)
- [返回dsh-memory-evolve所在分类](../plugins.md)
