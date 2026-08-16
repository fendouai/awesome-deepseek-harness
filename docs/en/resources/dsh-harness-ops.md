---
title: "dsh-harness-ops"
description: "Ops toolbox: A/B dual-slot daily snapshot rotation with atomic switch and one-click rollback, plus a 10s watchdog."
keywords: "dsh-harness-ops, automation, workflow, observability, deepseek harness, dsh"
---
# dsh-harness-ops

> ⭐ 9 · ✅ active · workflow

## One-liner

Ops toolbox: A/B dual-slot daily snapshot rotation with atomic switch and one-click rollback, plus a 10s watchdog.

## About

dsh-harness-ops（本仓库） ├── skills/dsh-snapshot-ab/ AB 轮换：官方快照 A/B 双槽，旧版保底、验收后原子切换 │ └── scripts/ab.sh 主命令（status/discover/notes/prepare/verify/switch/confirm/rollback） ├── skills/dsh-web-guard/ 自愈守护：launchd/systemd 托管，端口空闲 10s 内拉起 web │ └── scripts/install.sh 跨平台安装（macOS launchd / Linux systemd） ├── skills/dsh-session-recovery/ 会话丢失诊断：0 sessions/日志损坏 → 定位 → 无损修复 → 重启 │ └── scripts/ validate-sessions / repair-session-log / check-all-sessions / repair-unknown-events ├── skills/dsh-web-doctor/ out-of

## Author
**[fakechris](https://github.com/fakechris)**

## Links

- [GitHub Repository](https://github.com/fakechris/dsh-harness-ops)
- [Full README](https://github.com/fakechris/dsh-harness-ops#readme)
- [Back to the Workflows & Automation list](../workflows.md)
