---
title: "dsh-subagent-tools"
description: "子代理委托的逐调用模型/provider/persona/toolFilter 覆盖，支持 @preset 引用。"
keywords: "dsh-subagent-tools, multi-agent, agent, deepseek harness, dsh"
---
# dsh-subagent-tools

> ⭐ **2** · ✅ 活跃 · 智能体

| | | | |
|---|---|---|---|
| 类型 | 智能体 | 分类 | 多智能体 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [lynx-gt](https://github.com/lynx-gt) | 更新时间 | 2026-08-14 |

## 一句话介绍

> 子代理委托的逐调用模型/provider/persona/toolFilter 覆盖，支持 @preset 引用。

## 详细介绍

Enhanced subagent delegation tools for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (dsh): **per-call model / provider / persona / toolFilter overrides**, **`@preset:` persona references**, and **`provider/model` composite model ids** — shipped as a standard **bundle** that patches **no official package file**.

## 📦 安装

```bash
dsh plugin --profile web add dsh-subagent-tools          # npm
# or: dsh plugin --profile web add github:lynx-gt/dsh-subagent-tools#main
# or: dsh plugin --profile web add ./dsh-subagent-tools  # local checkout
```

## 🚀 快速开始

```bash
powershell -ExecutionPolicy Bypass -File install-preset.ps1   # Windows
# or: ./install-preset.sh                                     # POSIX
```

## 📚 更多信息

**or: ./install-preset.sh                                     **

It copies the `standard` preset into `$DSH_HOME/.agent-presets/standard-plus`, rewrites its `tool-subagent` / `tool-subagent-fork` rows to point at this package, and switches the default preset. Then **restart `dsh web` and start a NEW session** (presets are read at session creation and cannot be switched in a live session). To revert: pick `standard` again in the UI (General > Agent preset) and d

**Example**

Delegate a task to a subagent using model kimi-code/k3 with the reviewer persona: subagent(description="Review the translation", prompt="...", model="kimi-code/k3", persona="@preset:审校员")

## 🔗 链接

- [GitHub 仓库](https://github.com/lynx-gt/dsh-subagent-tools)
- [完整 README](https://github.com/lynx-gt/dsh-subagent-tools#readme)
- [返回dsh-subagent-tools所在分类](../agents.md)
