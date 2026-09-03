---
title: "dsh-fail-logger"
description: "DeepSeek Harness（DSH）插件：自动记录所有执行模式（原生工具 / PTC run_code / 代码内嵌工具调用）的工具失败错因，去重、计数、确定性排序后沉淀进 skill 的机器维护实录区段——让 Agent 越用越少错。"
keywords: "dsh-fail-logger, learning, skill, coding, multi-agent, deepseek harness, dsh"
---
# dsh-fail-logger

> ⭐ **9** · ✅ active · skill

| | | | |
|---|---|---|---|
| Type | skill | Category | Learning |
| Stars | ⭐ 9 | Status | ✅ active |
| Author | [Areium](https://github.com/Areium) | Updated | — |

## One-liner

> DeepSeek Harness（DSH）插件：自动记录所有执行模式（原生工具 / PTC run_code / 代码内嵌工具调用）的工具失败错因，去重、计数、确定性排序后沉淀进 skill 的机器维护实录区段——让 Agent 越用越少错。

## About

An all-mode tool failure recorder for DeepSeek Harness: whether the agent runs in **native mode** or **PTC (Code Mode)**, any tool failure is automatically written into the machine-maintained section of a skill — normalized-dedup, counted, deterministically ranked, TTL-pruned, and redacted — so the next session's model sees the most common failure causes when it loads the skill. **Fail less over time.**

## 📦 Install

```bash
# npm (recommended)
dsh plugin --profile web add dsh-fail-logger

# or pin to an exact version
dsh plugin --profile web add dsh-fail-logger@0.5.2

# or GitHub release tag (no npm registry dependency; auditability & rollback)
dsh plugin --profile web add "github:Areium/dsh-fail-logger#v0.5.2"

# or manually: merge cordis.patch.yml's insert entry into ~/.dsh/profiles/web/cordis.patch.yml
```

## 🚀 Quick Start

```bash
# 1) trigger a guaranteed failure (read on a missing file → isError=true)
dsh --profile headless "use the read tool on a file that does not exist"

# 2) verify the record landed
tail -20 ~/.dsh/skills/fail-log-guide/SKILL.md
```

## 📚 Learn more

**Config (patch entry `config:`, all optional)**

- id: dsh-fail-logger name: 'dsh-fail-logger' config: logDir: ~/.dsh/skills/fail-log-guide # target skill directory maxEntries: 10 # max rows per category maxMsg: 200 # chars kept per message marker: FAIL-LOG # section marker id ([A-Za-z0-9-]) flushMs: 300 # burst-coalescing debounce window ttlDays: 30 # drop entries with no new occurrence for N days (0 = keep forever) redact: [] # extra redaction

## 🔗 Links

- [GitHub Repository](https://github.com/Areium/dsh-fail-logger)
- [Full README](https://github.com/Areium/dsh-fail-logger#readme)
- [Back to the Skills list](../skills.md)
