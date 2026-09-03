---
title: "dsh-eval-harness"
description: "DSH 插件评测工具：YAML 用例驱动真实 agent 回归评测 + baseline 对比 PASS/WARN/FAIL 门禁｜Regression eval harness for DeepSeek Harness plugins"
keywords: "dsh-eval-harness, vision, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-eval-harness

> ⭐ **12** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 12 | 状态 | ✅ 活跃 |
| 作者 | [BiBoyang](https://github.com/BiBoyang) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding, multi-agent |

## 一句话介绍

> DSH 插件评测工具：YAML 用例驱动真实 agent 回归评测 + baseline 对比 PASS/WARN/FAIL 门禁｜Regression eval harness for DeepSeek Harness plugins

## 详细介绍

DSH 插件/skill 作者的回归评测门禁：写 yaml 用例 → headless 驱动真实 agent 跑 → 解析 session trace 断言 → 对比 baseline 出 PASS/WARN/FAIL 报告与 CI 退出码。

## 📦 安装

```bash
dsh plugin --profile headless add dsh-eval-harness
# 或从 GitHub 源码安装：
# dsh plugin --profile headless add github:boyang/dsh-eval-harness

# 验证挂载
dsh --profile headless --dump-config | grep dsh-eval-harness
```

## 🚀 快速开始

```bash
OVERALL=FAIL
EXIT_CODE=1
STRICT=false
REGRESSIONS=1
NEW_FAILURES=0
IMPROVEMENTS=0
ADDED=0
REMOVED=0
TOKEN_REGRESSIONS=0
SKIPPED_LINE_INCREASES=0
FLAKY=0
TOOL_ERROR_RECOVERIES=0
REPEATED_ERROR_SIGNATURES=0
BASELINE_FLAKY=0
UNRELIABLE=0
REASON regression: echo-hello pass -> fail
REGRESSION echo-hello: pass -> fail
```

## 📚 更多信息

**安装**

已发布到 npm（[`dsh-eval-harness`](https://www.npmjs.com/package/dsh-eval-harness)）： dsh plugin --profile headless add dsh-eval-harness

**judge 使用与校准（工作流）**

`output_judge` 是唯一的非确定性断言——judge 本身是个会犯错的 LLM，它的漏判会直接 变成门禁的假绿。所以 judge 断言的生命周期比结构断言多两步： 1. **写 rubric**：写出「必须/不许」的可判定标准，避免主观词（「回答要好」这类只会 放大抖动）。能落成 `output_contains` / `output_matches` 的期望不要用 judge。 2. **攒标注集**：从已有报告的 `finalText` 里抽真实输出，每条亲手标 PASS/FAIL 存成 JSONL（格式与示例见 `examples/judge-labels.example.jsonl`）。通过的、失败的样本 都要有——缺了 fail 样本就验证不了「judge 会不会抓失败」。 3. **校准**：`eval_judge_validate` 跑标注集，TPR / TNR 

**session trace 说明**

评测依赖 DSH 落盘的会话 trace（默认 `$DSH_HOME/sessions/<cwd编码>/<session-id>/session.jsonl[.zstd]`， 每行一帧信封 `{ type, seq, time, data }`）。`eval_run` 不污染环境变量，而是为每条用例生成一个 `--patch` overlay （`<output_dir>/eval-overlay-<序号>-<用例名>.patch.yml`），按 row id 整体替换 base bundle 的 `session-persistence-jsonl` 配置：把 `root` 切到该用例的隔离目录 （`<session_root>/<序号>-<用例名>`，`session_root` 默认 `<output_dir>/.sessions`；序号是加载序， 因为 slug 化不是唯一键，如 

## 🔗 链接

- [GitHub 仓库](https://github.com/BiBoyang/dsh-eval-harness)
- [完整 README](https://github.com/BiBoyang/dsh-eval-harness#readme)
- [返回dsh-eval-harness所在分类](../plugins.md)
