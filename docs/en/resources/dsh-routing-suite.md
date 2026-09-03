---
title: "dsh-routing-suite"
description: "dsh-routing-suite — injector + router-standard kit: install the runtime injector first, then the task-aware reasoning-mode router preset (measured P1-P23)."
keywords: "dsh-routing-suite, learning, skill, coding, ui, deepseek harness, dsh"
---
# dsh-routing-suite

> ⭐ **6,940** · ✅ active · skill

| | | | |
|---|---|---|---|
| Type | skill | Category | Learning |
| Stars | ⭐ 6,940 | Status | ✅ active |
| Author | [yjh051108](https://github.com/yjh051108) | Updated | — |

## One-liner

> dsh-routing-suite — injector + router-standard kit: install the runtime injector first, then the task-aware reasoning-mode router preset (measured P1-P23).

## About

一个仓库装齐三件套：**运行时注入器**（免重启运行时管理层）+ **思维模式路由预设**（任务感知推理模式，P1-P23 实测）+ **分级任务协议**（脑暴出题 → 规格化计划 → 打卡制 → 组收官 → 终验，含红队门与审计端点）。 [中文](README.md) | [English](README.en.md)

## ✨ Key Features

- [🔬 模型注意力懈怠：观测笔记](graded/docs/STUDY.md)——长程任务里验证勤勉度衰减的真实分段数据（无协议链晚段"1 工具/0 读图" vs 协议链全程在线）+对抗机制对照
- [📊 协议 vs 无协议：实测对比](graded/docs/COMPARE.md)——同型 3D 任务三会话对比表+ASCI I 图
- [🧪 测量工具](graded/scripts/measure.mjs)——`node scripts/measure.mjs 你的会话.jsonl`：任何人可对自己会话复算上述指标（脱敏：只输出数字）
- [📁 实测数据](graded/docs/DATA.md)——三会话脱敏指标表+懈怠强度表+审计口径

## 📦 Install

```bash
dsh plugin --profile web add github:yjh051108/dsh-routing-suite
```

## 🚀 Quick Start

```bash
# 1. 拉套装（单仓库：injector/preset 内容已直接入库，无需 submodule）
git clone https://github.com/yjh051108/dsh-routing-suite.git
cd dsh-routing-suite

# 2. 一键安装（注入器装配 + 预设复制 + 布局自检 + 提示重启）
.\install.ps1
```

## 📚 Learn more

**一键安装**

dsh plugin --profile web add github:yjh051108/dsh-routing-suite > 本套装已含上述三组件（injector/preset/graded 均为仓库内普通目录，内容直接入库）； > graded 发布物：`graded/dsh-external-dsh-graded-mode-0.0.1-rc1.tgz`（或 Release 附件）。 **DSH Target**：`>=0.1.0-rc.6 <0.2.0`（已跟进 rc.8 / 0.1.1-rc.2 / 0.1.2-alpha.1） > DSH 目前处于 developer preview，官方明示会有破坏性变更（breaking changes）。 > 本仓库的版本跟进记录见 `preset/CHANGELOG.md`。

**步骤 2：安装 router 预设（每个预设目录平铺复制到 .agent-presets 下，DSH 只扫一级子目录）**

$target = Join-Path $env:USERPROFILE '.dsh\.agent-presets\router-standard' Copy-Item -Recurse .\preset\router-standard $target $target = Join-Path $env:USERPROFILE '.dsh\.agent-presets\router-spec' Copy-Item -Recurse .\preset\router-spec $target

## 🔗 Links

- [GitHub Repository](https://github.com/yjh051108/dsh-routing-suite)
- [Full README](https://github.com/yjh051108/dsh-routing-suite#readme)
- [Back to the Skills list](../skills.md)
