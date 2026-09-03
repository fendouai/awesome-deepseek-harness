---
title: "dsh-ecc"
description: "273 ECC skills (95.8% of the 227k-star operator system) ported to DSH in four batches."
keywords: "dsh-ecc, coding, skill, deepseek harness, dsh"
---
# dsh-ecc

> ⭐ **3** · ✅ active · skill · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | skill | Category | Coding |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [gongyijie85](https://github.com/gongyijie85) | Updated | 2026-08-16 |

## One-liner

> 273 ECC skills (95.8% of the 227k-star operator system) ported to DSH in four batches.

## About

[English](README.en.md) | **简体中文** 把 [affaan-m/ECC](https://github.com/affaan-m/ECC)(~227k⭐ 的"操作员系统",286 个 技能)渐进移植到 **DeepSeek Harness (DSH)** 的 Cordis 插件架构。 插件向 `ctx.skills` 注册表的 **host 层** 注册技能提供者;技能随包分发 (`skills//SKILL.md`),无需用户配置。

## 📦 Install

```bash
# npm(包名 dsh-ecc 已被同名项目占用,本包发布为 dsh-ecc-skills)
dsh plugin --profile web add dsh-ecc-skills

# GitHub
dsh plugin --profile web add github:gongyijie85/dsh-ecc

# 本地开发
dsh plugin --profile web add D:\plugins\dsh-ecc
```

## 📚 Learn more

**移植路线图(渐进)**

医疗(healthcare-*、hipaa)、家庭网络(homelab-*)、科学(scientific-* / pubmed / uspto / gget)、 金融(customer-billing / finance-billing / defi / prediction-market / evm / x402)、 设计与内容(brand-*、motion-*、liquid-glass、manim、remotion、article-writing、seo)、 网络运维(cisco-ios、netmiko、network-*、terminal-*)、供应链/物流、营销/销售、 研究与数据(pytorch、recsys、mle、clickhouse、video/audio)等 视频工作流——风格访谈 → style pack → 校验 → 应用 → EDL/FCPXML 导出, 移植上游 

**移植说明(对比上游)**

`metadata.origin: ECC`)。 `/prompt-optimize` → `prompt-optimizer`);无 `Skill tool` 引用。 文件的 7 个技能(留待后续批次)。

**工作原理 / 添加技能**

同 [mattpocock-skills-dsh](https://github.com/gongyijie85/mattpocock-skills-dsh) (host 层 `ctx.skills.registerProvider`;零运行时依赖;原生解析折叠 YAML frontmatter)。往 `skills/<kebab-name>/SKILL.md` 放文件即自动发现;验证: `npm run verify`(274/274)。

## 🔗 Links

- [GitHub Repository](https://github.com/gongyijie85/dsh-ecc)
- [Full README](https://github.com/gongyijie85/dsh-ecc#readme)
- [Back to the Skills list](../skills.md)
