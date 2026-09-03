---
title: "dsh-agent-rp"
description: "SillyTavern migration and next-generation Agent roleplay for DSH."
keywords: "dsh-agent-rp, multi-agent, agent, ui, deepseek harness, dsh"
---
# dsh-agent-rp

> ⭐ **169** · ✅ active · agent · ⬆️ +7 recently

| | | | |
|---|---|---|---|
| Type | agent | Category | Multi-agent |
| Stars | ⭐ 169 | Status | ✅ active |
| Author | [hewzhew](https://github.com/hewzhew) | Updated | 2026-08-21 |

## One-liner

> SillyTavern migration and next-generation Agent roleplay for DSH.

## About

DSH Agent RP 是运行在 DSH 上的原生角色扮演 Runtime。角色会直接作为顶层 Agent 行动；Persona、世界、提示策略、正则包、状态和记忆都是可以独立选择、复用与组合的一等资源，而不是某张角色卡的附属设置。 Character Card、Chat Completion 预设、World Info、MVU、EJS 和 Tavern Helper 是目前优先接入的内容格式。它们让已有创作可以进入这套 Runtime，但不会反过来定义它的能力边界。

## ✨ Key Features

- 从统一的「开始游玩」入口选择角色对话或世界场景，再组合 Persona、世界、提示策略、独立正则包与开场；已知的外部资源权限会在启动前一次处理。
- 导入 PNG、JSON、CHARX 角色卡，以及 World Info、Chat Completion 预设、独立正则包和 SillyTavern JSONL 聊天记录；角色、Persona、世界、预设与正则包可以分别保存和复用。
- 连续游玩一段可回溯的故事：重新生成、续写、切换回复版本、修改输入并创建分支，同时保存明确状态与长期记忆。
- 用「故事工程」维护可编辑的大纲、伏笔、公开历史、人物私有认知、原著资料和正文分区；启用后由研究、人物、导演、分区与编辑 Worker 在正文前协作，正文后再把实际发生的事件沉淀回工程。
- 运行更复杂的社区内容：MVU、同步 EJS、世界书正则、显示正则、轻量 HTML 前端及一部分 Tavern Helper 脚本会进入各自受限的兼容环境，单项失败不会拖垮整段会话。
- 在沉浸视图与调试视图之间切换，查看实际生效的提示、世界召回、状态和运行诊断。

## 📦 Install

```bash
dsh plugin add '@hewzhew/dsh-agent-rp@next'
```

## 🚀 Quick Start

```bash
$installerPath = Join-Path $env:TEMP 'install-dsh-agent-rp.ps1'
Invoke-WebRequest 'https://raw.githubusercontent.com/hewzhew/dsh-agent-rp/main/scripts/install-windows.ps1' -OutFile $installerPath
powershell -NoProfile -ExecutionPolicy Bypass -File $installerPath -Start
```

## 📚 Learn more

**安装**

需要 Node.js 22.19+ 或 24+，以及 pnpm 11。没有 pnpm 时可以先运行 `npm install --global pnpm@11`。安装器会准备经过验证的 Agent Host，从 npm 的 `next` 标签安装或更新 Agent RP，并保留 `~/.dsh` 中已有的角色与会话；它不会静默安装全局工具。

**Android / Termux 预览**

Termux 路线面向 ARM64、Android 11 及以上设备，目标是在手机本机运行、不让电脑保持开机。旧预览已经验证过安卓原生依赖、图片解码后备模块和本地启动，但当前安装入口正在迁移。 手机安装器仍固定在旧的 DSH `0.1.0-rc.6`，尚未迁移到当前 Agent Host runner，因此不适用于当前 `main` 的完整 Agent/MVU 回合。现有安装不要为了追随桌面版本而手工覆盖 DSH 包；新的 Termux 安装与更新暂缓，等安卓原生模块和 patched runner 一起完成实机验收后再恢复下面的正式命令。 旧安装仍可运行原来已经落盘的版本，但不要重新执行旧安装器更新到当前 `main`。 若启动或导入角色卡时遇到问题，运行 `dsh-agent-rp-doctor` 即可得到一份可直接贴到 Issue 的脱敏体检结果。它只检查版本、模块和 Android

## 🔗 Links

- [GitHub Repository](https://github.com/hewzhew/dsh-agent-rp)
- [Full README](https://github.com/hewzhew/dsh-agent-rp#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
