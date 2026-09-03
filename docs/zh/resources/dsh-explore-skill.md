---
title: "deepseek-harness-skillx"
description: "DSH 工作流技能合集。"
keywords: "deepseek-harness-skillx, learning, skill, workflow, deepseek harness, dsh"
---
# deepseek-harness-skillx

> ⭐ **2** · ✅ 活跃 · 技能

| | | | |
|---|---|---|---|
| 类型 | 技能 | 分类 | 学习 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [drowned-fish1](https://github.com/drowned-fish1) | 更新时间 | 2026-08-13 |

## 一句话介绍

> DSH 工作流技能合集。

## 详细介绍

skillx 是一个面向 AI Agent 的安全元 Skill，也是可直接安装的 DeepSeek Harness 插件。它指导 Agent 在本地能力不够时，搜索、比较、审查并临时采用外部 Skill，而不是看到 README 就执行安装命令。

## ✨ 核心特性

- 判断当前任务是否需要外部 Skill
- 优先检查当前项目和本地已安装 Skills
- 生成结构化能力请求
- 按渠道优先级搜索外部候选 Skill，并给出具体搜索方法
- 以只读方式获取候选 Skill 内容，记录版本标识保证可追溯
- 评估候选 Skill 的匹配度，多候选时横向比较
- 识别安全和信任风险，包括提示注入信号
- 在存在风险时请求用户确认

## 📦 安装

```bash
dsh plugin --profile web add github:drowned-fish1/deepseek-harness-skillx
dsh --profile web
```

## 🚀 快速开始

```bash
/skillx 帮我找一个适合当前任务的外部 Skill，采用前先说明匹配度和风险。
```

## 🔗 链接

- [GitHub 仓库](https://github.com/drowned-fish1/deepseek-harness-skillx)
- [完整 README](https://github.com/drowned-fish1/deepseek-harness-skillx#readme)
- [返回deepseek-harness-skillx所在分类](../skills.md)
