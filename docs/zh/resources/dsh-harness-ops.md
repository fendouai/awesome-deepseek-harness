---
title: "dsh-harness-ops"
description: "运维工具箱：官方每日快照 A/B 双槽轮换、原子切换、一键回滚、守护进程自动拉起。"
keywords: "dsh-harness-ops, automation, workflow, observability, deepseek harness, dsh"
---
# dsh-harness-ops

> ⭐ 9 · ✅ 活跃 · 工作流

## 一句话介绍

运维工具箱：官方每日快照 A/B 双槽轮换、原子切换、一键回滚、守护进程自动拉起。

## 详细介绍

dsh-harness-ops（本仓库） ├── skills/dsh-snapshot-ab/ AB 轮换：官方快照 A/B 双槽，旧版保底、验收后原子切换 │ └── scripts/ab.sh 主命令（status/discover/notes/prepare/verify/switch/confirm/rollback） ├── skills/dsh-web-guard/ 自愈守护：launchd/systemd 托管，端口空闲 10s 内拉起 web │ └── scripts/install.sh 跨平台安装（macOS launchd / Linux systemd） ├── skills/dsh-session-recovery/ 会话丢失诊断：0 sessions/日志损坏 → 定位 → 无损修复 → 重启 │ └── scripts/ validate-sessions / repair-session-log / check-all-sessions / repair-unknown-events ├── skills/dsh-web-doctor/ out-of

## 作者
**[fakechris](https://github.com/fakechris)**

## 链接

- [GitHub 仓库](https://github.com/fakechris/dsh-harness-ops)
- [完整 README](https://github.com/fakechris/dsh-harness-ops#readme)
- [返回dsh-harness-ops所在分类](../workflows.md)
