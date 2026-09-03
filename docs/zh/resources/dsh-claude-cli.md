---
title: "dsh-claude-cli"
description: "DeepSeek Harness LLM provider that runs your installed Claude Code CLI as the model backend — no API key."
keywords: "dsh-claude-cli, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-claude-cli

> ⭐ **6** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [katsos](https://github.com/katsos) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> DeepSeek Harness LLM provider that runs your installed Claude Code CLI as the model backend — no API key.

## 详细介绍

Use the Claude Code CLI you already have installed as a DeepSeek Harness LLM provider. No API key. The plugin runs `claude` as a subprocess and streams its output back through the harness's LLM seam, so requests authenticate as whatever `claude` is already logged in as — a login you should check your plan's [usage terms](#usage-terms) against before automating. The harness stays the agent. The CLI's own agent loop, tools, settings, memory files, and MCP servers are all switched off; what is left is the model call, driven by the harness's system prompt, history, and tools.

## 📦 安装

```bash
dsh plugin --profile web add ../dsh-claude-cli
```

## 🚀 快速开始

```bash
dsh --profile headless --patch /absolute/path/to/dsh-claude-cli/cordis.yml "your task"
```

## 📚 更多信息

**Install**

Requires a working `claude` on `PATH` ([Claude Code](https://claude.com/claude-code)), Node `^22.19 || >=24`, and a harness with `@deepseek-ai/dsh-llm`. Install it into the profile you actually run, pointing at your checkout of this repository. The package declares `dsh.bundle`, so it joins that profile's layer stack and the `anthropic-claude-cli` route is composed on every start: dsh plugin --pro

**Configuration**

`extraArgs` is passed *before* the plugin's own flags, and an entry naming one of them is rejected when the plugin loads. Both matter: the CLI keeps the last occurrence of a repeated flag, so appended arguments would otherwise win. A single `--tools default` was enough to restore the CLI's full tool set — `Bash` and `Edit` included — inside the harness's working directory. Use `extraArgs` for flag

**Usage terms**

Nothing here bypasses authentication. Requests run through the official CLI, as whatever `claude` is already logged in as, using the same documented `--print` mode Claude Code ships for non-interactive use. What this plugin adds is different in kind: it makes a subscription login the model backend for *another* agent framework. Anthropic's [Consumer Terms](https://www.anthropic.com/legal/consumer-

## 🔗 链接

- [GitHub 仓库](https://github.com/katsos/dsh-claude-cli)
- [完整 README](https://github.com/katsos/dsh-claude-cli#readme)
- [返回dsh-claude-cli所在分类](../plugins.md)
