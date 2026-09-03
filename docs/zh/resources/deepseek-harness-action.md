---
title: "deepseek-harness-action"
description: "社区 GitHub Action：AI 代码审查、CI 诊断、自动修复、Issue 转 PR。"
keywords: "deepseek-harness-action, developer, integration, coding, automation, git, deepseek harness, dsh"
---
# deepseek-harness-action

> ⭐ **13** · ✅ 活跃 · 集成 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 开发者工具 |
| 星数 | ⭐ 13 | 状态 | ✅ 活跃 |
| 作者 | [Lixiaoyiao](https://github.com/Lixiaoyiao) | 更新时间 | 2026-08-21 |
| 子分类 | 🧪 代码·测试·审查 | 能力 | coding, automation, git |

## 一句话介绍

> 社区 GitHub Action：AI 代码审查、CI 诊断、自动修复、Issue 转 PR。

## 详细介绍

[中文](README.zh-CN.md) Run DeepSeek Harness directly from GitHub pull requests, issues, failed CI jobs, and maintainer-authored automations. GitHub PR / Issue / CI → DeepSeek Harness → Review / Diagnose / Fix / Issue → PR The Action starts a credential-isolated DSH worker, validates its structured result, and lets a trusted Controller publish comments or validated changes. This is a community project, not an official DeepSeek or GitHub product. It is maintained by [@Lixiaoyiao](https://github.com/Lixiaoyiao).

## 🚀 快速开始

```bash
GitHub PR / Issue / CI  →  DeepSeek Harness  →  Review / Diagnose / Fix / Issue → PR
```

## 📚 更多信息

**Quick Start**

Run the installer from the root of the repository you want to configure: npm create deepseek-harness-action@latest Choose one of these modes: For CI or another non-interactive environment, pass the mode explicitly so the installer never waits for stdin: npm create deepseek-harness-action@latest -- --mode both For non-interactive use, omitting `--dsh-mode` keeps the compatible `controlled` default.

**Manual installation**

Add `DEEPSEEK_API_KEY` under **Settings → Secrets and variables → Actions**, then create `.github/workflows/dsh-review.yml`: name: DSH review on: pull_request_target: types: [opened, synchronize, ready_for_review, reopened] permissions: contents: read pull-requests: write jobs: review: if: github.event.pull_request.draft == false runs-on: ubuntu-latest timeout-minutes: 30 steps: - uses: actions/ch

## 🔗 链接

- [GitHub 仓库](https://github.com/Lixiaoyiao/deepseek-harness-action)
- [完整 README](https://github.com/Lixiaoyiao/deepseek-harness-action#readme)
- [返回deepseek-harness-action所在分类](../integrations.md)
