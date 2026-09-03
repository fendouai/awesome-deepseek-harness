---
title: "dsh-auto-mode"
description: "Safe automatic permissions for DeepSeek Harness."
keywords: "dsh-auto-mode, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-auto-mode

> ⭐ **115** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 115 | 状态 | ✅ 活跃 |
| 作者 | [NanmiCoder](https://github.com/NanmiCoder) | 更新时间 | 2026-08-17 |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Safe automatic permissions for DeepSeek Harness.

## 详细介绍

Coding agents need broad access to build, test, and inspect a project without stopping every few steps. But DeepSeek Harness currently leaves a sharp choice: restricted modes interrupt normal development, while Full access removes approval entirely. `dsh-auto-mode` adds the missing middle ground. Routine project work runs directly inside the official `workspace-write` sandbox, only semantic risks outside that boundary are classified using the current DSH model and the direct user's instructions, genuine ambiguity asks once, and destructive access to critical paths is denied before execution.

## 📦 安装

```bash
dsh plugin --profile web add --save-exact @nanmicoder/dsh-auto-mode@latest
```

## 🚀 快速开始

```bash
dsh plugin --profile web add --save-exact @nanmicoder/dsh-auto-mode@0.1.5
```

## 📚 更多信息

**Install**

> [!NOTE] > Requires an existing [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) installation. > [!IMPORTANT] > Plugin `0.1.6` targets **DeepSeek Harness 0.1.2-alpha.2 and 0.1.2-alpha.3**. Plugin `0.1.5` belongs to the older Harness `0.1.1-rc.2` line and fails to load on both tested Alpha hosts. Keep plugin `0.1.5` pinned while staying on that RC host; Alpha users should instal

**Configuration**

No extra endpoint or API key is needed by default. Auto uses the current Session's DSH provider and model. A trusted profile may pin a dedicated route: config: classifierProvider: deepseek-official classifierModel: deepseek-v4-flash classifierTimeoutMs: 30000 classifierMaxOutputTokens: 1024 See [DESIGN.md](./DESIGN.md) for the complete decision order, threat model, Windows path handling, classifie

## 🔗 链接

- [GitHub 仓库](https://github.com/NanmiCoder/dsh-auto-mode)
- [完整 README](https://github.com/NanmiCoder/dsh-auto-mode#readme)
- [返回dsh-auto-mode所在分类](../plugins.md)
