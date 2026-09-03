---
title: "dsh-event-auditor"
description: "DeepSeek Harness 事件流审计面板插件：观察事件类型/分发模式/计数/最近事件，帮助插件作者理解 harness 内部"
keywords: "dsh-event-auditor, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-event-auditor

> ⭐ **1** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [qing3a](https://github.com/qing3a) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> DeepSeek Harness 事件流审计面板插件：观察事件类型/分发模式/计数/最近事件，帮助插件作者理解 harness 内部

## 详细介绍

Harness 事件流审计面板：观察事件类型、分发模式、计数与最近事件，帮助插件作者理解 DeepSeek Harness 内部发生了什么。

## ✨ 核心特性

- 监听 22 个 harness `emit` 事件（agent 生命周期 / 会话 / 工具 / subagent / 配置）
- **v0.2**：监听 10 个 waterfall 事件（tools/execute、approval/request、fs/write-intent、llm/stream 等，观察性透传 next()）
- **v0.3**：settings 面板热改（installSettingsSection，实时开关分组无需重启）、headless dump（`DSH_EVENT_AUDIT_DUMP`）
- 按事件名与分发模式计数，环形缓冲保留最近 500 条
- `/audit` 面板（纯静态页）+ `/api/audit/events` JSON 接口（支持 `?since=` 增量）
- 分组开关（agent/session/tools/subagent/config/waterfall；config 默认关闭）

## 📦 安装

```bash
# 生产安装（npm，agent 可直接执行）
dsh plugin --profile <profile> add @qing3a/dsh-event-auditor
dsh --profile <profile>
# 打开 http://localhost:<port>/audit

# 开发模式（需 Node >= 22 + pnpm）
git clone https://github.com/qing3a/dsh-event-auditor.git
cd dsh-event-auditor && pnpm install && pnpm build
cd <path-to-deepseek-harness>
dsh plugin --profile <profile> add link:$(pwd)/dsh-event-auditor
```

## 🚀 快速开始

```bash
dsh plugin --profile <profile> remove @qing3a/dsh-event-auditor
```

## 📚 更多信息

**生产安装（npm，agent 可直接执行）**

dsh plugin --profile <profile> add @qing3a/dsh-event-auditor dsh --profile <profile>

## 🔗 链接

- [GitHub 仓库](https://github.com/qing3a/dsh-event-auditor)
- [完整 README](https://github.com/qing3a/dsh-event-auditor#readme)
- [返回dsh-event-auditor所在分类](../plugins.md)
