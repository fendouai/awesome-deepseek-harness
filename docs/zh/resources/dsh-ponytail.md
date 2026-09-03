---
title: "dsh-ponytail"
description: "Ponytail 最懒资深工程师模式：6 个技能，改编自 DietrichGebert/ponytail。"
keywords: "dsh-ponytail, coding, skill, deepseek harness, dsh"
---
# dsh-ponytail

> ⭐ **2** · ✅ 活跃 · 技能 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 技能 | 分类 | 编码 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [gongyijie85](https://github.com/gongyijie85) | 更新时间 | 2026-08-16 |

## 一句话介绍

> Ponytail 最懒资深工程师模式：6 个技能，改编自 DietrichGebert/ponytail。

## 详细介绍

[English](README.en.md) | **简体中文** 把 [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)(~76k⭐ 的 "最懒资深工程师"代码风格)移植到 **DeepSeek Harness (DSH)** 的 Cordis 插件架构。 插件向 `ctx.skills` 注册表的 **host 层** 注册技能提供者,6 个技能随包分发 (`skills//SKILL.md`),无需任何用户配置。

## 📦 安装

```bash
# npm(包名 dsh-ponytail 已被同名项目占用,本包发布为 dsh-ponytail-skills)
dsh plugin --profile web add dsh-ponytail-skills

# GitHub
dsh plugin --profile web add github:gongyijie85/dsh-ponytail

# 本地开发
dsh plugin --profile web add D:\plugins\dsh-ponytail
```

## 📚 更多信息

**工作原理**

`skills/` 目录,从 YAML frontmatter 解析 `name`/`description` 并返回完整技能 定义,`resourceBase` 指向技能目录。

## 🔗 链接

- [GitHub 仓库](https://github.com/gongyijie85/dsh-ponytail)
- [完整 README](https://github.com/gongyijie85/dsh-ponytail#readme)
- [返回dsh-ponytail所在分类](../skills.md)
