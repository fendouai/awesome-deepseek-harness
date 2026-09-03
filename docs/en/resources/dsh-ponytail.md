---
title: "dsh-ponytail"
description: "Ponytail lazy senior dev mode: 6 skills (ponytail, ponytail-audit, ponytail-debt, ponytail-gain, ponytail-help, ponytail-review) adapted from DietrichGebert/ponytail."
keywords: "dsh-ponytail, coding, skill, deepseek harness, dsh"
---
# dsh-ponytail

> ⭐ **2** · ✅ active · skill · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | skill | Category | Coding |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [gongyijie85](https://github.com/gongyijie85) | Updated | 2026-08-16 |

## One-liner

> Ponytail lazy senior dev mode: 6 skills (ponytail, ponytail-audit, ponytail-debt, ponytail-gain, ponytail-help, ponytail-review) adapted from DietrichGebert/ponytail.

## About

[English](README.en.md) | **简体中文** 把 [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)(~76k⭐ 的 "最懒资深工程师"代码风格)移植到 **DeepSeek Harness (DSH)** 的 Cordis 插件架构。 插件向 `ctx.skills` 注册表的 **host 层** 注册技能提供者,6 个技能随包分发 (`skills//SKILL.md`),无需任何用户配置。

## 📦 Install

```bash
# npm(包名 dsh-ponytail 已被同名项目占用,本包发布为 dsh-ponytail-skills)
dsh plugin --profile web add dsh-ponytail-skills

# GitHub
dsh plugin --profile web add github:gongyijie85/dsh-ponytail

# 本地开发
dsh plugin --profile web add D:\plugins\dsh-ponytail
```

## 📚 Learn more

**工作原理**

`skills/` 目录,从 YAML frontmatter 解析 `name`/`description` 并返回完整技能 定义,`resourceBase` 指向技能目录。

## 🔗 Links

- [GitHub Repository](https://github.com/gongyijie85/dsh-ponytail)
- [Full README](https://github.com/gongyijie85/dsh-ponytail#readme)
- [Back to the Skills list](../skills.md)
