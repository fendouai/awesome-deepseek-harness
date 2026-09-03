---
title: "dsh-harness-ops"
description: "Ops toolbox: A/B dual-slot daily snapshot rotation with atomic switch and one-click rollback, plus a 10s watchdog."
keywords: "dsh-harness-ops, automation, workflow, observability, deepseek harness, dsh"
---
# dsh-harness-ops

> ⭐ **11** · ✅ active · workflow · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | workflow | Category | Automation |
| Stars | ⭐ 11 | Status | ✅ active |
| Author | [fakechris](https://github.com/fakechris) | Updated | 2026-08-21 |

## One-liner

> Ops toolbox: A/B dual-slot daily snapshot rotation with atomic switch and one-click rollback, plus a 10s watchdog.

## About

dsh-harness-ops（本仓库） ├── skills/dsh-snapshot-ab/ AB 轮换：官方快照 A/B 双槽，旧版保底、验收后原子切换 │ └── scripts/ab.sh 主命令（status/discover/notes/prepare/verify/switch/confirm/rollback） ├── skills/dsh-web-guard/ 自愈守护：launchd/systemd 托管，端口空闲 10s 内拉起 web │ └── scripts/install.sh 跨平台安装（macOS launchd / Linux systemd） ├── skills/dsh-session-recovery/ 会话丢失诊断：0 sessions/日志损坏 → 定位 → 无损修复 → 重启 │ └── scripts/ validate-sessions / repair-session-log / check-all-sessions / repair-unknown-events ├── skills/dsh-web-doctor/ out-of-band 医生：web/A/B 全挂时终端一键诊断→修复→拉起 │ └── scripts/ doctor.sh / doctor-tui.py / session-last-activity.mjs └── plugins/dsh-restart-recover/ 重启续接插件：agent/created 检测 interrupted → 自动注入续接 └── src/index.ts cordis 插件（监听 agent/created，零 dsh-track 依赖） **日常用得最多的入口**： - 看状态：`$AB status` - 每日分析（官方改了啥）：`$AB discove

## ✨ Key Features

- 看状态：`$AB status`
- 每日分析（官方改了啥）：`$AB discover` / `$AB notes`（官方 changelog）→ 见「场景 C′」
- 每日升级：`$AB discover → prepare → switch --yes → confirm`
- 自愈验证：`kill $(lsof -ti :3080)` → 10s 内自动拉起 → 会话自动继续（无需手动）

## 📦 Install

```bash
$AB status        # 确认 current 指向、slots 为空、phase=idle
$AB init --yes    # 新建 slot-a worktree + pnpm install + 完整构建（build:lib+build:web，约几分钟）
                  # 完成后 current -> slot-a；正在跑的服务不受影响（下次重启才走新槽）
$AB status        # slot a* 有内容，current=a，phase=idle
```

## 🚀 Quick Start

```bash
dsh web           # 启动生产。永远不需要指定 A/B —— 跑的是 current 指向的槽
```

## 📚 Learn more

**mini TUI：设计与使用（`dsh-doctor --guide` / 菜单 5）**

**为什么是 TUI**（2026-08-13 教训）：一次无人值守的 `--agent` 长跑失败——被误报带偏、超时 被杀、什么都没修成。**没有人 guide 的 doctor 长任务不靠谱**。mini TUI 是"有人看着的自愈"： LLM 自动干活，你看着它怎么想，觉得不对就打断。 **三条设计原则**： 1. **LLM 自动判断、自动修复**——已知问题确定性自动修复（无逐项确认）；0 问题自动只读验收 （输出"✅ 验收通过"+证据清单）；残留问题 LLM 自动诊断根因并修复。 2. **交互 = 看清完整 CoT + 随时打断**——完整推理链 markdown 实时渲染；**Ctrl-C 打断运行中的 agent**，输入指引后回车，agent 按指引继续（上下文跨轮携带）。 3. **只有 LLM 真正卡住/需要决策时才问用户**（缺 API key、不确定的破坏性操

**一键安装：4 个 skill 进 ~/.dsh/skills + dsh-restart-recover bundle **

git clone https://github.com/dsh-external/dsh-harness-ops.git cd dsh-harness-ops bash scripts/install.sh

**5. 设计原则（为什么这样做）**

1. **`current` 符号链接 + git worktree**：与官方 `dsh-upgrade` 同构；切换是一次原子 `ln -sfn`， 主克隆只做对象库和 worktree 宿主，从不被运行。 2. **扩展在槽外、按槽参数化**：扩展（如 dsh-track）通过 `DSH_SOURCE` / 生成的 `tsconfig.ab.json` / node_modules 符号链接指向目标槽 → 能在**切换前**就对着新快照构建测试。 3. **验收门**：install / build / 扩展测试 / web 冒烟全绿才算 prepared；验收不过不切换。 冒烟不止 HTTP 200 —— `web.smokeClientIds` 断言扩展 client 出现在 `window.__DSH_BOOT__` （20260810 把声明键 `dshClient` 改为 

## 🔗 Links

- [GitHub Repository](https://github.com/fakechris/dsh-harness-ops)
- [Full README](https://github.com/fakechris/dsh-harness-ops#readme)
- [Back to the Workflows & Automation list](../workflows.md)
