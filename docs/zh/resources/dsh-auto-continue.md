---
title: "dsh-auto-continue"
description: "自动恢复中断的请求：失败分类、自适应退避重试、可配置续写消息与浏览器通知。"
keywords: "dsh-auto-continue, automation, workflow, ui, deepseek harness, dsh"
---
# dsh-auto-continue

> ⭐ **33** · ✅ 活跃 · 工作流 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 工作流 | 分类 | 自动化 |
| 星数 | ⭐ 33 | 状态 | ✅ 活跃 |
| 作者 | [HsiangNianian](https://github.com/HsiangNianian) | 更新时间 | 2026-08-21 |

## 一句话介绍

> 自动恢复中断的请求：失败分类、自适应退避重试、可配置续写消息与浏览器通知。

## 详细介绍

For [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh web`): whenever a request in the web GUI gets interrupted by a **non-human cause**, the plugin simulates the user typing **“Continue”** and sends it, so the agent keeps working without manual intervention. The message enters the session log exactly like a manual prompt — the model sees it, and the interrupted work resumes. Since 0.8.0 the engine runs **inside the host process** (single instance), so it keeps watching even with every browser tab closed, and multiple open tabs can never double-send. **Smart recovery** (all configurable): - **Error classification** — transient failures (network / timeout / 5xx / 429…) are auto-resumed; permanent ones are **skipped** and notified, because retrying them never helps. A

## ✨ 核心特性

- **Error classification** — transient failures (network / timeout / 5xx / 429…) are auto-resumed; permanent ones are **skipped** and notified, because retrying t
- **Adaptive backoff** — consecutive failures wait longer each time (cooldown × factor: 20s → 40s → 80s…), capped at the max backoff, instead of hammering a broke
- **English / Chinese localization** — the settings card, built-in resume / guard / loop text, and browser notifications follow DSH's active UI language (initiall
- **Templated continue text** — `continueText` supports `{code}` `{message}` `{status}` `{tool}` `{turn}` `{errorCount}` `{sessionTitle}` `{elapsed}` placeholders
- **Idempotency guard** — before resuming, the plugin inspects the last tool call: if its result is unconfirmed (the turn died mid-tool, e.g. a `git push` that ma
- **Pause** — a global **Pause auto-continue** toggle in the settings card stops everything (live + scan) instantly; per-session pauses (e.g. via a notification b
- **Notification buttons** — notifications carry **Resume now** (send immediately, ignoring cooldown, the consecutive cap and any pause) and **Pause this session 
- **Loop guard** — watches **running** turns too. Three signals trip the guard, which cancels the turn and restarts it with a configurable loop text ("stop repeat

## 📦 安装

```bash
dsh plugin --profile web add dsh-client-auto-continue
dsh web
```

## 🚀 快速开始

```bash
dsh plugin --profile web add github:HsiangNianian/dsh-auto-continue
dsh web
```

## 📚 更多信息

**Quick Start**

DSH plugins install into a **profile** (`dsh web` → `web` profile). Install, restart `dsh web`, done. > **Use the latest DSH (recommended: 0.1.2-alpha.4 or newer).** Run `dsh --version` before installing. Plugin v0.11.1 supports the settings API used by DSH 0.1.2-alpha.2+ (including alpha.3 and alpha.4) while retaining compatibility with DSH 0.1.0-rc.7 through 0.1.1; rc.6 and earlier remain unsupp

**Verify & uninstall**

dsh --profile web --dump-config | grep auto-continue # config layer mounted In the browser console (Ctrl/Cmd+Shift+I): `[auto-continue] 已启动(文本="继续", …)` — every detection and auto-send is logged. dsh plugin --profile web remove dsh-client-auto-continue # npm / repo install

**Configuration**

Everything is configurable from the GUI — no file or console edits needed. Open **Settings → Plugins → Plugin configuration**. **Auto Continue** appears as a collapsed card alongside the other plugins; click the card or its right-hand chevron to expand the full configuration in place. Besides the fields below, the expanded card shows a live **stats panel** (today's activity with a reset button) an

## 🔗 链接

- [GitHub 仓库](https://github.com/HsiangNianian/dsh-auto-continue)
- [完整 README](https://github.com/HsiangNianian/dsh-auto-continue#readme)
- [返回dsh-auto-continue所在分类](../workflows.md)
