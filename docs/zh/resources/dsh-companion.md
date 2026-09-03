---
title: "dsh-companion"
description: "DeepSeek Companion — DeepSeek Harness 官方伴侣插件：对话导出/交接摘要/成本优化/全局检索 + 执行轨迹分析、Prompt 工程工作台、多模型竞技场、任务编排、安全与审计（E–J 九大模块，Cordis 插件化）。"
keywords: "dsh-companion, search, plugin, coding, deepseek harness, dsh"
---
# dsh-companion

> ⭐ **4** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [beijingwahw](https://github.com/beijingwahw) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding |

## 一句话介绍

> DeepSeek Companion — DeepSeek Harness 官方伴侣插件：对话导出/交接摘要/成本优化/全局检索 + 执行轨迹分析、Prompt 工程工作台、多模型竞技场、任务编排、安全与审计（E–J 九大模块，Cordis 插件化）。

## 详细介绍

[English](README.en.md) | 中文 **DeepSeek Harness 官方伴侣插件** —— 基于 Cordis 框架与 Harness Plugin SDK 构建，为 DeepSeek Harness 平台提供对话智能导出、上下文交接摘要、API 成本优化、全局对话检索、本地语义检索、对话知识资产与跨会话知识合成七大能力。 - 开发语言：TypeScript（`strict: true`，ESM） - 运行框架：DeepSeek Harness（Cordis ≥ 4.0，一切皆插件） - API 直连：DeepSeek 官方 API（`https://api.deepseek.com`） - 数据安全：所有用户数据仅存于 Harness 插件沙箱本地，API Key 以 AES-256-GCM 加密落盘 ---

## ✨ 核心特性

- 开发语言：TypeScript（`strict: true`，ESM）
- 运行框架：DeepSeek Harness（Cordis ≥ 4.0，一切皆插件）
- API 直连：DeepSeek 官方 API（`https://api.deepseek.com`）
- 数据安全：所有用户数据仅存于 Harness 插件沙箱本地，API Key 以 AES-256-GCM 加密落盘

## 📦 安装

```bash
dsh plugin add beijingwahw/dsh-companion --profile web
```

## 🚀 快速开始

```bash
dsh web
```

## 📚 更多信息

**一键安装**

dsh plugin add beijingwahw/dsh-companion --profile web 启动后插件面板自动加载： dsh web > 常用进阶命令：升级 `dsh plugin upgrade dsh-companion --profile web`；卸载 `dsh plugin remove dsh-companion --profile web`；本地路径安装 `dsh plugin add ./dsh-companion --profile web`。更多方式见「开发期热更新」后附。 ---

**从源码构建安装（贡献者 / 离线场景）**

git clone https://github.com/beijingwahw/dsh-companion.git cd dsh-companion pnpm install pnpm run build dsh plugin add . --profile web ---

**配置 DeepSeek API Key（模块 C 前置）**

1. 打开插件设置页的「开发者模式」总开关。 2. 在「API Key 管理」输入框粘贴你的 DeepSeek API Key 并保存。 - Key 通过 AES-256-GCM 加密后存入 Harness 插件沙箱的 `companion` 存储域； - 任何接口响应、日志、事件中均不会出现 Key 明文（`/cost/state` 仅返回 `apiKeyConfigured` 布尔）。 3. 可选：点击「测试连接」验证 Key 有效性（对应 `/cost/test-call`）。

**配置参考**

根配置（`cordis.patch.yml` 可覆盖任意字段）： 停用单个模块：将对应开关置为 `false`（配置层），或在 `manifest.json` 的模块声明中关闭。模块之间零耦合，停用一个不影响其余模块。 ---

## 🔗 链接

- [GitHub 仓库](https://github.com/beijingwahw/dsh-companion)
- [完整 README](https://github.com/beijingwahw/dsh-companion#readme)
- [返回dsh-companion所在分类](../plugins.md)
