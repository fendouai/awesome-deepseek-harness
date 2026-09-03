---
title: "dsh-codex-port"
description: "DeepSeek Harness 技能移植插件：把 ~/.codex 的 Codex 官方插件（186+ 个、583+ 技能）一键移植为 DSH 技能（codex_list/port/status），frontmatter 自动转换、幂等跳过。· Batch-port the Codex plugin family into DSH skills."
keywords: "dsh-codex-port, learning, skill, coding, deepseek harness, dsh"
---
# dsh-codex-port

> ⭐ **8** · ✅ active · skill · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | skill | Category | Learning |
| Stars | ⭐ 8 | Status | ✅ active |
| Author | [STARDUSTLC666](https://github.com/STARDUSTLC666) | Updated | 2026-08-18 |

## One-liner

> DeepSeek Harness 技能移植插件：把 ~/.codex 的 Codex 官方插件（186+ 个、583+ 技能）一键移植为 DSH 技能（codex_list/port/status），frontmatter 自动转换、幂等跳过。· Batch-port the Codex plugin family into DSH skills.

## About

把 **Codex 官方插件全家桶**一键搬进 DSH：扫描 `~/.codex` 里的解包插件与插件缓存，把它们的技能批量移植为 DSH 技能（frontmatter 自动转换、codex 专属文件剔除、名称清洗、幂等跳过）。

## 📦 Install

```bash
dsh plugin --profile web add dsh-codex-port
```

## 🚀 Quick Start

```bash
dsh plugin --profile web remove dsh-codex-port
```

## 📚 Learn more

**安装**

dsh plugin --profile web add dsh-codex-port 需要本机装有 Codex CLI（`~/.codex` 目录存在即可）。

**配置**

全部可选，默认即可用： name: 'dsh-codex-port' config: # codexHome: C:\Users\you\.codex # Codex 家目录（默认 ~/.codex） # targetDir: C:\Users\you\.dsh\skills # 目标技能目录（默认 <DSH_HOME>/skills） # overwrite: true # 覆盖同名技能（默认跳过）

**示例**

codex_list {} # 看看 Codex 里有什么 codex_list { plugin: remotion } # 只看某个插件 codex_port {} # 全部移植（同名自动跳过） codex_port { plugins: [remotion, hyperframes] } codex_port { skills: [video-best], overwrite: true } codex_status {} # 还有多少没移植 移植后 DSH 技能目录立即可用，agent 按技能描述自动触发。

**跨平台使用**

`targetDir` 不限于 DSH：指向任何支持 Agent Skills（SKILL.md）格式的 agent 技能目录，即可把 Codex 全家桶移植给它们： codex_port { targetDir: ~/.claude/skills }

## 🔗 Links

- [GitHub Repository](https://github.com/STARDUSTLC666/dsh-codex-port)
- [Full README](https://github.com/STARDUSTLC666/dsh-codex-port#readme)
- [Back to the Skills list](../skills.md)
