---
title: "dsh-context-doctor"
description: "Audits what actually enters every model request: token cost of AGENTS.md chains, skill catalogs and tool schemas, with duplicate/conflict detection."
keywords: "dsh-context-doctor, memory, plugin, context, observability, deepseek harness, dsh"
---
# dsh-context-doctor

> ⭐ **17** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 17 | Status | ✅ active |
| Author | [Zhenyu98](https://github.com/Zhenyu98) | Updated | 2026-08-21 |
| Subcategory | 📦 Context management | Capabilities | context, observability |

## One-liner

> Audits what actually enters every model request: token cost of AGENTS.md chains, skill catalogs and tool schemas, with duplicate/conflict detection.

## About

DSH 会话里，模型每个请求都自动携带一批注入物：层层叠加的 `AGENTS.md` 指令链、一百多个技能的目录摘要、几十个工具 schema、MCP 工具面。它们悄悄消耗输入 token，且经常出现跨文件重复段落、同名技能互相遮蔽、工具面膨胀——但平时没人量化，问题到上下文告警时才暴露。

## 📦 Install

```bash
# 1. 安装（官方 bundle 插件机制；构建产物已入库，git 源安装无需构建）
dsh plugin --profile web add "github:Zhenyu98/dsh-context-doctor#main"

# 2. 验证合成树含该条目
dsh --profile web --dump-config | grep context-doctor

# 3. 重启 dsh web，在新会话里让模型调用
context_audit
```

## 🚀 Quick Start

```bash
dsh --profile web --dump-config | grep context-doctor
# - insert:
#     - id: context-doctor
#       name: 'dsh-context-doctor'
```

## 📚 Learn more

**Quick Start**

> **宿主版本要求**：DSH `>= 0.1.0-rc.6`（含 0.1.1-rc 线；已对 0.1.1-rc.2 验证）。`@deepseek-ai/cordis` 与 `@deepseek-ai/dsh-tools` 是 peer 依赖，由宿主 profile 提供；插件不自带这两份运行时（自带会铸造第二个工具调度器，见 [#2](https://github.com/Zhenyu98/dsh-context-doctor/issues/2)）。

**使用**

模型直接调用工具： context_audit # 审计当前会话工作目录 context_audit cwd=/path/to/project context_audit includeSkillBodies=true maxSkillBodies=20 context_audit detail=developer # 摘要 + 可定位的 context-audit receipt 输出 canonical JSON（`AuditReport`）： { "tool": "context_audit", "version": 1, "cwd": "/path/to/project", "injected": { "instructions": { "files": [{ "path": "...", "bytes": 3421, "tokens": 812 }], "totalTokens"

**配置**

context-doctor: defaultCwd: /path/to/project # 浏览器面板不带 cwd 参数时的默认审计目录（缺省为进程启动目录） cacheTtlMs: 60000 # 审计结果缓存时长（毫秒）

**FAQ**

**装了之后圆环没出现？** 重启 `dsh web` 后进入已有会话的 composer；新会话在分配 `sessionId` 前不会显示会话级控件。仍没有则先确认 `dsh --profile web --dump-config` 含 context-doctor 条目，且浏览器半区构建产物存在（改过源码必须重新 `./scripts/build.sh`）。 > v0.5.0 及更早版本把控件注册到 `conversation.input.context`——那个插槽任何已发布的 DSH 都没有，控件因此被静默丢弃（[#4](https://github.com/Zhenyu98/dsh-context-doctor/issues/4)）。v0.5.2 起改用原生插槽 `conversation.input.right`，无需给 DSH 打补丁。 **没有 Web 界面（headles

## 🔗 Links

- [GitHub Repository](https://github.com/Zhenyu98/dsh-context-doctor)
- [Full README](https://github.com/Zhenyu98/dsh-context-doctor#readme)
- [Back to the Plugins list](../plugins.md)
