---
title: "dsh-inspect"
description: "Adversarial checkup → fix → review loop built on the official workflow engine."
keywords: "dsh-inspect, workflow, coding, security, deepseek harness, dsh"
---
# dsh-inspect

> ⭐ 5 · ✅ active · workflow

## One-liner

Adversarial checkup → fix → review loop built on the official workflow engine.

## About

- **发现是怀疑，验证是定罪**：检查员/审查员一律对抗式（默认怀疑、找反例、只认可当场验证的证据）； checkup 的红队环节就是负反馈——问题声明必须经受住攻击，推不翻才成立。 - **根据数据流定向判断状态**：判断问题前先按数据流理清系统（输入 → 处理 → 存储 → 输出， 谁写谁读）；**问题 = 数据流某处状态偏离预期**，而不是静态读代码猜。 - **互相校验**：每个问题必须给出可互相校验的验证方式（重跑复现 / 日志对照 / 输入输出对照 / 双路径对照），并写明预期状态与实际观测——**无法通过系统反馈验证的，不许报**。 - **修复要证伪**：先沿数据流找到状态偏离的**源头**（不许修表面）；修复后重跑原复现， 观测输出与预期比较（反馈闭合）——问题没消失 = 根因没找对，重新分析。 - **根据数据判断直接定方案**：根因找到后，方案由数据自然决定——实现员按"找根因 → 实施 → 验证" 三步直接做（根据数据判断选择最合理的方案，不空谈不犹豫，实施保持改动最小）。 - **闭环**：checkup 的问题清单 → fix 修复任务 → review 

## Author
**[omdsh-dev](https://github.com/omdsh-dev)**

## Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-inspect)
- [Full README](https://github.com/omdsh-dev/dsh-inspect#readme)
- [Back to the Workflows & Automation list](../workflows.md)
