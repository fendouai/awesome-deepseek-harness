---
title: "mattpocock-skills-dsh"
description: "Matt Pocock full promoted skill set (25 SKILL.md: grilling, writing-for-agents, wait-what, TDD, code review, wayfinder, ask-matt router) ported to DSH."
keywords: "mattpocock-skills-dsh, coding, skill, deepseek harness, dsh"
---
# mattpocock-skills-dsh

> ⭐ **2** · ✅ active · skill · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | skill | Category | Coding |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [gongyijie85](https://github.com/gongyijie85) | Updated | 2026-08-16 |

## One-liner

> Matt Pocock full promoted skill set (25 SKILL.md: grilling, writing-for-agents, wait-what, TDD, code review, wayfinder, ask-matt router) ported to DSH.

## About

[English](README.en.md) | **简体中文** 为 **DeepSeek Harness (DSH)** 打造的 Matt Pocock 技能插件包:把 [mattpocock/skills](https://github.com/mattpocock/skills)(来自 [aihero.dev/skills](https://www.aihero.dev/skills) 的"真实工程师"技能集) 移植到 DSH 的 Cordis 插件架构上。 插件会向 `ctx.skills` 注册表的 **host 层** 注册一个技能提供者,因此每个 agent preset 的作用域链都会合并这些技能。技能正文随包分发 (`skills//SKILL.md`),通过 `import.meta.url` 定位——这是包的 组装事实,不需要任何用户配置。

## 📦 Install

```bash
# 方式一:全局安装 dsh,永久可用(推荐)
  npm install -g @deepseek-ai/dsh
  dsh --version

  # 方式二:不安装,所有命令用 npx 形式
  npx @deepseek-ai/dsh --version
```

## 🚀 Quick Start

```bash
npx @deepseek-ai/dsh plugin --profile web add github:gongyijie85/mattpocock-skills-dsh
```

## 📚 Learn more

**在 DeepSeek Harness 中安装与使用**

这是 DeepSeek Harness 的**插件包**。安装后会把技能注册进 host 技能注册表, 你 profile 里的每个 agent 会话都能在技能目录中看到它们,并可用 `skill` 工具加载。

**最简单:一条命令(从 GitHub 安装)**

npx @deepseek-ai/dsh plugin --profile web add github:gongyijie85/mattpocock-skills-dsh

**让 DeepSeek Harness 帮你安装**

打开 DeepSeek Harness(Web 界面),新建对话,把下面这句话发给它: 帮我安装这个链接里边的插件:https://github.com/gongyijie85/mattpocock-skills-dsh Agent 会自动完成安装(`dsh plugin add` → 重启 profile → 验证技能注册)。

**移植说明(对比上游 mattpocock/skills)**

[mattpocock/skills](https://github.com/mattpocock/skills) `6654f6b`(含 grilling 轮次 HR 分隔、wait-what `CONTEXT-MAP.md` 指引、to-tickets wide-refactor 段落)。 更新历史见 [CHANGELOG.md](CHANGELOG.md)。 `description`,可选 `whenToUse`),DSH 可直接消费,正文基本零改动。 `grill-me`、`wait-what`)映射为 DSH 的 `invocation.modelInvocable: false`, 保留原意图;其余技能模型/用户均可调用。 Claude Code 工具名改为 DSH 的 `skill` 工具;`grilling` 中的"dispatch a sub-agent"对应 DSH 

## 🔗 Links

- [GitHub Repository](https://github.com/gongyijie85/mattpocock-skills-dsh)
- [Full README](https://github.com/gongyijie85/mattpocock-skills-dsh#readme)
- [Back to the Skills list](../skills.md)
