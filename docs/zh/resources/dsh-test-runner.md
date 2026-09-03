---
title: "dsh-test-runner"
description: "结构化测试运行工具：自动识别 vitest/jest/pytest/node:test，运行并解析失败摘要。"
keywords: "dsh-test-runner, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-test-runner

> ⭐ **2** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [suimi8](https://github.com/suimi8) | 更新时间 | 2026-08-13 |
| 子分类 | 🧪 代码·测试·审查 | 能力 | coding |

## 一句话介绍

> 结构化测试运行工具：自动识别 vitest/jest/pytest/node:test，运行并解析失败摘要。

## 详细介绍

DeepSeek Harness 插件：结构化测试运行工具 **`test_run`**。 让 agent 用一次工具调用完成「改代码 → 跑测试 → 修」闭环：自动探测测试框架、执行测试、**只返回结构化摘要**（通过/失败统计 + 失败用例名称与错误信息 + 输出尾部），避免模型阅读整段原始测试输出（省 token、少一轮）。

## 📦 安装

```bash
dsh plugin --profile web add ./dsh-test-runner        # 本地目录
# 或从 GitHub（需要 prepare 脚本 + allowBuilds 放行）
dsh plugin --profile web add github:you/dsh-test-runner
```

## 🚀 快速开始

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

## 📚 更多信息

**使用示例**

模型侧直接调用： 返回结构： { "ok": false, "framework": "node", "command": "node --test", "exitCode": 1, "durationMs": 800, "summary": { "total": 6, "passed": 5, "failed": 1, "skipped": 0 }, "failures": [ { "name": "string: broken case (intentional failure)", "message": "Expected values to be strictly equal: | 'WORLD' !== 'WRLD' | ..." } ], "outputTail": "<原始输出尾部 3000 字符>" }

## 🔗 链接

- [GitHub 仓库](https://github.com/suimi8/dsh-test-runner)
- [完整 README](https://github.com/suimi8/dsh-test-runner#readme)
- [返回dsh-test-runner所在分类](../plugins.md)
