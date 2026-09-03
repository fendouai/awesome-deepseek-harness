---
title: "kimi-tide"
description: "月汐 — Kimi Code (Moonshot) 接入 DeepSeek Harness 的完整方案：标准 DSH 插件 + Kimi CLI 桥接维护 fork + Agent 协作闭环方法论"
keywords: "kimi-tide, ide, integration, coding, multi-agent, deepseek harness, dsh"
---
# kimi-tide

> ⭐ **4** · ✅ 活跃 · 集成 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | IDE 与编辑器 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [tafcear](https://github.com/tafcear) | 更新时间 | 2026-08-21 |

## 一句话介绍

> 月汐 — Kimi Code (Moonshot) 接入 DeepSeek Harness 的完整方案：标准 DSH 插件 + Kimi CLI 桥接维护 fork + Agent 协作闭环方法论

## 详细介绍

**场景一：贴了张截图，模型说看不了** - 以前：手动切到能看图的模型 → 贴图 → 问完 → 记得切回来。 - 装后：直接贴。带图的消息自动交给能看图的模型，下一条纯文字消息自动回到默认模型。 **场景二：切完模型，忘了切回来** - 以前：为一张图切到贵的模型，之后整场会话都在烧贵的额度。 - 装后：月汐按「每一步」决策，一会话不绑死——图处理完，下一条消息就回到你的默认模型。 **场景三：额度总比预期烧得快** - 以前：所有消息——包括「你好」和「帮我看下这句翻译」——都走最贵的模型。 - 装后：选「省钱」预设（一套配好的「默认模型 + 规则」方案），闲聊、翻译、日常杂活自动走便宜模型，代码和图才动用贵的模型；面板实时显示套餐余额（Kimi/GLM 等带套餐的模型，无套餐的置灰不显示）。 ---

## ✨ 核心特性

- 以前：手动切到能看图的模型 → 贴图 → 问完 → 记得切回来。
- 装后：直接贴。带图的消息自动交给能看图的模型，下一条纯文字消息自动回到默认模型。
- 以前：为一张图切到贵的模型，之后整场会话都在烧贵的额度。
- 装后：月汐按「每一步」决策，一会话不绑死——图处理完，下一条消息就回到你的默认模型。
- 以前：所有消息——包括「你好」和「帮我看下这句翻译」——都走最贵的模型。
- 装后：选「省钱」预设（一套配好的「默认模型 + 规则」方案），闲聊、翻译、日常杂活自动走便宜模型，代码和图才动用贵的模型；面板实时显示套餐余额（Kimi/GLM 等带套餐的模型，无套餐的置灰不显示）。

## 📦 安装

```bash
cd packages/dsh-kimi-tide
npm install && npm run build && npm pack
dsh plugin --profile web add ./dsh-kimi-tide-<version>.tgz
```

## 🚀 快速开始

```bash
cd packages/dsh-kimi-tide
npm install
npm run typecheck   # tsc --noEmit
npm test            # vitest
npm run build       # tsc 宿主 + esbuild 浏览器
```

## 📚 更多信息

**3. 安装插件**

cd packages/dsh-kimi-tide npm install && npm run build && npm pack dsh plugin --profile web add ./dsh-kimi-tide-<version>.tgz

## 🔗 链接

- [GitHub 仓库](https://github.com/tafcear/kimi-tide)
- [完整 README](https://github.com/tafcear/kimi-tide#readme)
- [返回kimi-tide所在分类](../integrations.md)
