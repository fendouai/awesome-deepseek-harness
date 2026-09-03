---
title: "dsh-inspect"
description: "发现问题(checkup) → 修复交付(fix) → 质量复查(review) 的对抗式闭环。"
keywords: "dsh-inspect, workflow, coding, security, deepseek harness, dsh"
---
# dsh-inspect

> ⭐ **6** · ✅ 活跃 · 工作流 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 工作流 | 分类 | 工作流 |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [omdsh-dev](https://github.com/omdsh-dev) | 更新时间 | 2026-08-17 |

## 一句话介绍

> 发现问题(checkup) → 修复交付(fix) → 质量复查(review) 的对抗式闭环。

## 详细介绍

- **发现是怀疑，验证是定罪**：检查员/审查员一律对抗式（默认怀疑、找反例、只认可当场验证的证据）； checkup 的红队环节就是负反馈——问题声明必须经受住攻击，推不翻才成立。 - **根据数据流定向判断状态**：判断问题前先按数据流理清系统（输入 → 处理 → 存储 → 输出， 谁写谁读）；**问题 = 数据流某处状态偏离预期**，而不是静态读代码猜。 - **互相校验**：每个问题必须给出可互相校验的验证方式（重跑复现 / 日志对照 / 输入输出对照 / 双路径对照），并写明预期状态与实际观测——**无法通过系统反馈验证的，不许报**。 - **修复要证伪**：先沿数据流找到状态偏离的**源头**（不许修表面）；修复后重跑原复现， 观测输出与预期比较（反馈闭合）——问题没消失 = 根因没找对，重新分析。 - **根据数据判断直接定方案**：根因找到后，方案由数据自然决定——实现员按"找根因 → 实施 → 验证" 三步直接做（根据数据判断选择最合理的方案，不空谈不犹豫，实施保持改动最小）。 - **闭环**：checkup 的问题清单 → fix 修复任务 → review 把关（可逐条验证修复是否真消失）； 复查不通过或人的反馈重新进入 fix。三个工具可单独用，也可串起来。

## ✨ 核心特性

- **发现是怀疑，验证是定罪**：检查员/审查员一律对抗式（默认怀疑、找反例、只认可当场验证的证据）；
- **根据数据流定向判断状态**：判断问题前先按数据流理清系统（输入 → 处理 → 存储 → 输出，
- **互相校验**：每个问题必须给出可互相校验的验证方式（重跑复现 / 日志对照 / 输入输出对照 /
- **修复要证伪**：先沿数据流找到状态偏离的**源头**（不许修表面）；修复后重跑原复现，
- **根据数据判断直接定方案**：根因找到后，方案由数据自然决定——实现员按"找根因 → 实施 → 验证"
- **闭环**：checkup 的问题清单 → fix 修复任务 → review 把关（可逐条验证修复是否真消失）；

## 📦 安装

```bash
pnpm install        # 仅 typescript/@types/node（typecheck 用）
pnpm run typecheck  # tsc -b，类型从 sibling deepseek-harness checkout 解析
cd plugins/dsh-inspect && node --test   # 回归测试
```

## 🚀 快速开始

```bash
cd plugins/dsh-inspect && node --test        # 零依赖，纯 node + node:test
# 或：node --test test/（Node ≤20 支持目录参数；Node 22+ 把位置参数当 glob，请用
#     node --test 或 node --test 'test/**'，见 nodejs/node 测试运行器 glob 语义）
```

## 📚 更多信息

**安装与使用方式**

包声明了 `dsh.bundle.patch`（cordis.patch.yml），通过 `dsh plugin` 装进**任意** profile （把 `<profile>` 换成 `tui` / `headless` / `web` 或自建 profile）： dsh plugin --profile <profile> add git+https://github.com/dsh-external/dsh-inspect.git dsh --profile <profile> # 重启生效：checkup / fix / review 随 profile 注入 > 若 pnpm 把 https URL 重写成 git+ssh（本机全局 git `insteadof` 配置所致），用上面的 > `git+https://` 形式；`dsh plugin` 会提示需要 `allowBu

## 🔗 链接

- [GitHub 仓库](https://github.com/omdsh-dev/dsh-inspect)
- [完整 README](https://github.com/omdsh-dev/dsh-inspect#readme)
- [返回dsh-inspect所在分类](../workflows.md)
