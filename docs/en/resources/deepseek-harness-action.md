---
title: "deepseek-harness-action"
description: "Community GitHub Action: AI code review, CI diagnosis, auto-fix and issue-to-PR implementation."
keywords: "deepseek-harness-action, developer, integration, coding, automation, git, deepseek harness, dsh"
---
# deepseek-harness-action

> ⭐ **13** · ✅ active · integration · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | integration | Category | Developer tools |
| Stars | ⭐ 13 | Status | ✅ active |
| Author | [Lixiaoyiao](https://github.com/Lixiaoyiao) | Updated | 2026-08-21 |
| Subcategory | 🧪 Code, tests & review | Capabilities | coding, automation, git |

## One-liner

> Community GitHub Action: AI code review, CI diagnosis, auto-fix and issue-to-PR implementation.

## About

[中文](README.zh-CN.md) Run DeepSeek Harness directly from GitHub pull requests, issues, failed CI jobs, and maintainer-authored automations. GitHub PR / Issue / CI → DeepSeek Harness → Review / Diagnose / Fix / Issue → PR The Action starts a credential-isolated DSH worker, validates its structured result, and lets a trusted Controller publish comments or validated changes. This is a community project, not an official DeepSeek or GitHub product. It is maintained by [@Lixiaoyiao](https://github.com/Lixiaoyiao).

## 🚀 Quick Start

```bash
GitHub PR / Issue / CI  →  DeepSeek Harness  →  Review / Diagnose / Fix / Issue → PR
```

## 📚 Learn more

**Quick Start**

Run the installer from the root of the repository you want to configure: npm create deepseek-harness-action@latest Choose one of these modes: For CI or another non-interactive environment, pass the mode explicitly so the installer never waits for stdin: npm create deepseek-harness-action@latest -- --mode both For non-interactive use, omitting `--dsh-mode` keeps the compatible `controlled` default.

**Manual installation**

Add `DEEPSEEK_API_KEY` under **Settings → Secrets and variables → Actions**, then create `.github/workflows/dsh-review.yml`: name: DSH review on: pull_request_target: types: [opened, synchronize, ready_for_review, reopened] permissions: contents: read pull-requests: write jobs: review: if: github.event.pull_request.draft == false runs-on: ubuntu-latest timeout-minutes: 30 steps: - uses: actions/ch

## 🔗 Links

- [GitHub Repository](https://github.com/Lixiaoyiao/deepseek-harness-action)
- [Full README](https://github.com/Lixiaoyiao/deepseek-harness-action#readme)
- [Back to the MCP & Integrations list](../integrations.md)
