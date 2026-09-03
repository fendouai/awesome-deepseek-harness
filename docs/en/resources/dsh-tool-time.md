---
title: "dsh-tool-time"
description: "DSH 时间工具插件：严格 ISO 8601 解析、IANA 时区转换、UTC 日历运算、固定时长差，零依赖"
keywords: "dsh-tool-time, automation, workflow, coding, deepseek harness, dsh"
---
# dsh-tool-time

> ⭐ **4** · ✅ active · workflow

| | | | |
|---|---|---|---|
| Type | workflow | Category | Automation |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | — |

## One-liner

> DSH 时间工具插件：严格 ISO 8601 解析、IANA 时区转换、UTC 日历运算、固定时长差，零依赖

## About

[English](README.en.md) DSH 时间工具插件 —— 严格 ISO 解析、IANA 时区转换、UTC 日历运算、固定时长差。零依赖、零进程、纯函数。

## ✨ Key Features

- **严格 ISO 8601 子集**：仅接受 `YYYY-MM-DD`（UTC 零点）、`YYYY-MM-DDTHH:mm:ssZ`、`YYYY-MM-DDTHH:mm:ss±HH:MM`（±14:00 内，可选 `.SSS` 毫秒）；不带时区的日期时间、RFC 2822、自然语言日期一律拒绝；`2026-02-30`
- **时区名**：IANA 名交给 `Intl.DateTimeFormat` 校验，非法即抛 `time: unknown timezone`
- **数值**：`amount` 必须是安全整数；`unit` 枚举白名单；所有字符串 ≤200 字符
- **Intl 环境固定**：`'en-CA'` + `hourCycle: 'h23'`（避免午夜 `24:00` 与本地化数字）

## 📦 Install

```bash
# 交互式（web）profile —— 从 GitHub 仓库安装
dsh plugin --profile web add github:omdsh-dev/dsh-tool-time
# 一次性任务（headless）profile —— dsh run 默认使用 headless
dsh plugin --profile headless add github:omdsh-dev/dsh-tool-time
```

## 🚀 Quick Start

```bash
npm pack     # 生成 dsh-tool-time-<version>.tgz
# 交互式（web）profile
dsh plugin --profile web add ./dsh-tool-time-<version>.tgz
# 一次性任务（headless）profile
dsh plugin --profile headless add ./dsh-tool-time-<version>.tgz
```

## 📚 Learn more

**一次性任务（headless）profile —— dsh run 默认使用 headless**

dsh plugin --profile headless add github:omdsh-dev/dsh-tool-time 或使用 `npm pack` 生成的 tarball 安装： npm pack # 生成 dsh-tool-time-<version>.tgz

**手动安装与旧版本兼容（monorepo 旧场景）**

monorepo 方式仅适用于旧场景：不支持 Profile Bundle 的旧快照或插件开发调试环境： 1. 放入 monorepo：`cp -r time ~/.dsh/source/master/packages/tools/time`（开发调试） 2. `apps/cli/package.json` 加 `"@deepseek-ai/dsh-tool-time": "workspace:^"`；`tsconfig.host.json` references 加 `{ "path": "./packages/tools/time" }` 3. `pnpm install && pnpm run build` 4. 在 profile 用户层 patch 插入插件（`~/.dsh/profiles/<name>/cordis.patch.yml`）： - id: tool-time n

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-tool-time)
- [Full README](https://github.com/omdsh-dev/dsh-tool-time#readme)
- [Back to the Workflows & Automation list](../workflows.md)
