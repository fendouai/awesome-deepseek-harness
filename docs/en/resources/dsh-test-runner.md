---
title: "dsh-test-runner"
description: "Structured test runner tool: auto-detect vitest/jest/pytest/node:test, run tests and parse failure summaries for the model."
keywords: "dsh-test-runner, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-test-runner

> ⭐ **2** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [suimi8](https://github.com/suimi8) | Updated | 2026-08-13 |
| Subcategory | 🧪 Code, tests & review | Capabilities | coding |

## One-liner

> Structured test runner tool: auto-detect vitest/jest/pytest/node:test, run tests and parse failure summaries for the model.

## About

DeepSeek Harness 插件：结构化测试运行工具 **`test_run`**。 让 agent 用一次工具调用完成「改代码 → 跑测试 → 修」闭环：自动探测测试框架、执行测试、**只返回结构化摘要**（通过/失败统计 + 失败用例名称与错误信息 + 输出尾部），避免模型阅读整段原始测试输出（省 token、少一轮）。

## 📦 Install

```bash
dsh plugin --profile web add ./dsh-test-runner        # 本地目录
# 或从 GitHub（需要 prepare 脚本 + allowBuilds 放行）
dsh plugin --profile web add github:you/dsh-test-runner
```

## 🚀 Quick Start

```bash
{
  "ok": false,
  "framework": "node",
  "command": "node --test",
  "exitCode": 1,
  "durationMs": 800,
  "summary": { "total": 6, "passed": 5, "failed": 1, "skipped": 0 },
  "failures": [
    { "name": "string: broken case (intentional failure)",
      "message": "Expected values to be strictly equal: | 'WORLD' !== 'WRLD' | ..." }
  ],
  "outputTail": "<原始输出尾部 3000 字符>"
}
```

## 📚 Learn more

**使用示例**

模型侧直接调用： 返回结构： { "ok": false, "framework": "node", "command": "node --test", "exitCode": 1, "durationMs": 800, "summary": { "total": 6, "passed": 5, "failed": 1, "skipped": 0 }, "failures": [ { "name": "string: broken case (intentional failure)", "message": "Expected values to be strictly equal: | 'WORLD' !== 'WRLD' | ..." } ], "outputTail": "<原始输出尾部 3000 字符>" }

## 🔗 Links

- [GitHub Repository](https://github.com/suimi8/dsh-test-runner)
- [Full README](https://github.com/suimi8/dsh-test-runner#readme)
- [Back to the Plugins list](../plugins.md)
