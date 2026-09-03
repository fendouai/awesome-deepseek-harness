---
title: "dsh-plugin-dev-skills"
description: "An Agent Skills skill for developing DeepSeek Harness (DSH) plugins（开发 DSH 插件的 Agent Skill）——插件/服务/事件/工具/LLM 适配器/打包安装的标准。Works with Claude Code, Codex, DSH, VS Code Copilot & any compatible agent."
keywords: "dsh-plugin-dev-skills, desktop, client, coding, multi-agent, deepseek harness, dsh"
---
# dsh-plugin-dev-skills

> ⭐ **38** · ✅ active · client · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 38 | Status | ✅ active |
| Author | [zimodzh](https://github.com/zimodzh) | Updated | 2026-08-18 |

## One-liner

> An Agent Skills skill for developing DeepSeek Harness (DSH) plugins（开发 DSH 插件的 Agent Skill）——插件/服务/事件/工具/LLM 适配器/打包安装的标准。Works with Claude Code, Codex, DSH, VS Code Copilot & any compatible agent.

## About

中文 · English 一套遵循 [Agent Skills 规范](https://agentskills.io) 的技能，用于开发 [**DeepSeek Harness（DSH）**](https://github.com/deepseek-ai/deepseek-harness) 插件。 DSH 是一个插件化的 Agent Harness SDK：模型适配器、工具注册表、会话日志、甚至 agent loop 本身，全都是可以从配置里替换的 Cordis 插件。本技能把[官方文档](https://deepseek-harness.github.io/deepseek-harness/guide/quickstart)里散落在教程、参考手册与生成目录中的约定，收敛成一套可执行的标准——任何加载了它的 agent，都能用同一种方式开发 DSH 插件。

## 📦 Install

```bash
git clone https://github.com/zimodzh/dsh-plugin-dev-skills.git ~/.claude/skills/dsh-plugin-dev
```

## 🚀 Quick Start

```bash
dsh-plugin-dev/
├── SKILL.md      # 入口：frontmatter、8 条硬规则、6 个场景工作流、决策速查表、完成前检查清单
├── references/   # 12 份详细标准，按需加载；索引见 references/README.md
├── examples/     # 两个可复制、可运行的最小示例
│   ├── hello-plugin/
│   └── greet-tool/
└── evals/        # description 的触发评测集与评测方法
```

## 📚 Learn more

**安装**

技能名为 `dsh-plugin-dev`，Agent Skills 规范要求所在文件夹同名；本仓库名为 `dsh-plugin-dev-skills`。克隆时直接指定目标文件夹名即可一步到位： git clone https://github.com/zimodzh/dsh-plugin-dev-skills.git ~/.claude/skills/dsh-plugin-dev 把目标目录换成你所用 agent 的对应路径（见下表）；也可以下载 release 压缩包，解压后把文件夹改名为 `dsh-plugin-dev`。 无需构建、无需脚本依赖、无需任何配置——以上说的是技能本身。实际开发 DSH 插件则需要一个可用的 DSH 环境：Node.js、pnpm，以及示例中用到的 `dsh`。 验证：向 agent 提问"开发一个 DSH 插件 / 写一个 DSH 工具"，技能应被触发

## 🔗 Links

- [GitHub Repository](https://github.com/zimodzh/dsh-plugin-dev-skills)
- [Full README](https://github.com/zimodzh/dsh-plugin-dev-skills#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
