---
title: "dsh-prime-agent"
description: "Prime Agent 启发的持久 RLM 控制平面，面向 DSH Code 模式。"
keywords: "dsh-prime-agent, workflow, deepseek harness, dsh"
---
# dsh-prime-agent

> ⭐ **4** · ✅ 活跃 · 工作流 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 工作流 | 分类 | 工作流 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [yoke233](https://github.com/yoke233) | 更新时间 | 2026-08-21 |

## 一句话介绍

> Prime Agent 启发的持久 RLM 控制平面，面向 DSH Code 模式。

## 详细介绍

- 模型 catalog 只含 `repl`。其他 DSH 工具不直接可见：prompt assembly 把 tools 列表过滤到只剩 `repl`，并移除固定 Harness identity 与隐藏能力各自的 `tool:*` 独立提示；前者不提供操作事实，后者按外层直接工具编写，会与 Prime 路由冲突。生成 SDK 的 declaration/JSDoc 是 cell 内能力的唯一使用契约。直接调用其他工具会被 guard 拒绝，这些能力作为 cell 内预加载绑定出现；Prime preset 通过 `prime-tool-restrictions.config.deny` 明确排除重复的 `str_replace_editor`、通用 `workflow` 和 `ralph`，通用 scoped 插件仅应用该配置；保留 `read`/`write`/`edit`/`apply_patch` 及其他所需能力。`tools.*` 调用向 Realm 程序返回 canonical value；若对象结果未经转换直接成为 cell completion，则使用 DSH 官方 `result.content` 展示，避免把 `edit.before/after` 等大 DTO 展开进上下文。`agents.*`（spawn/fork/list/send/interrupt）与 `jobs.*`（list/output/kill）是 continuable child 与后台任务的薄适配。Agent 固定提示与具体对话、任务、仓库和历史错误无关。 - 路由信任 Agent 执行上下文。`repl` 要求拥有 Agent 会话:插件用可信 `exec.agent.id` 从共享 `realm-identity` 存储解析该会话稳定的不透明 Realm id,再把程序、本

## ✨ 核心特性

- 模型 catalog 只含 `repl`。其他 DSH 工具不直接可见：prompt assembly 把 tools 列表过滤到只剩 `repl`，并移除固定 Harness identity 与隐藏能力各自的 `tool:*` 独立提示；前者不提供操作事实，后者按外层直接工具编写，会与 Prime 路由冲突。生成 
- 路由信任 Agent 执行上下文。`repl` 要求拥有 Agent 会话:插件用可信 `exec.agent.id` 从共享 `realm-identity` 存储解析该会话稳定的不透明 Realm id,再把程序、本轮租约绑定与取消信号交给 host 侧的 `ctx.primeRealmRuntime.run(..
- Host 服务与官方运行时并存。`cordis.patch.yml` 只是把 `dsh-prime-agent/runtime` 作为新 row 插入,官方 `code-runtime` row 原样保留;非 Prime 会话继续使用官方 one-shot 语义,不存在 fallback。
- Realm 内的绑定经跨 run 稳定的 Proxy 与 per-run binding lease 调用:schema、审批、沙箱、日志、并发和取消仍由 DSH 执行,run 结束立即撤销授权。
- 多个 TUI 进程可共享 Prime 持久状态并同时运行不同 Session；同一 Session 的 live Realm 同时只允许一个进程持有，owner 退出后另一进程以空 namespace 接管。
- Prime 不封装搜索 provider：`tools.grep` 仍调用 DSH 正式 `grep`。提示词组装按工具名复制 schema，在 `edit`、`grep`、`write` 的原始 description 后只追加各自缺失的关键约束；`grep` 说明普通文本使用字符串，正则语法使用无 flags li

## 📦 安装

```bash
npm install
npm run check:all
dsh plugin --profile web add ./dsh-prime-agent https://github.com/yoke233/dsh-tool-monitor/archive/c3397b2cafeb725af08705d5bcaeeeb828e012ae.tar.gz
```

## 🚀 快速开始

```bash
npm pack
$primePackage = Get-ChildItem -Filter 'dsh-prime-agent-*.tgz' |
  Sort-Object LastWriteTime -Descending |
  Select-Object -First 1 -ExpandProperty FullName
dsh plugin --profile tui add $primePackage https://github.com/yoke233/dsh-tool-monitor/archive/c3397b2cafeb725af08705d5bcaeeeb828e012ae.tar.gz
```

## 📚 更多信息

**工作原理**

<p align="center">  </p> 完整身份路由、namespace 生命周期、Agent 编排与学习层边界见 [当前架构](docs/architecture.md)；固定提示、completion metadata 和 notebook renderer 的模型可见契约见 [Prime REPL Notebook 呈现规格](docs/repl-notebook-presentation.zh.md)。

**安装与启用**

npm install npm run check:all dsh plugin --profile web add ./dsh-prime-agent https://github.com/yoke233/dsh-tool-monitor/archive/c3397b2cafeb725af08705d5bcaeeeb828e012ae.tar.gz 安装命令同时加入两个独立 bundle：`dsh-prime-agent` 的 patch 仍只在官方 `code-runtime` row 旁纯插入 `dsh-prime-agent/runtime` host row；`dsh-tool-monitor` 的 patch 以兼容 Registry 替换 Host 的具体 `jobs-local` 实现并注册 `job_monitor`。Prime preset 在启动时落位到 `$DSH_

**shim 从全局 DSH 安装解析这两个运行时依赖。**

$globalNodeRoot = npm root -g $shimModules = Join-Path $shimRoot 'node_modules\@deepseek-ai' New-Item -ItemType Directory -Force -Path $shimModules | Out-Null foreach ($packageName in @('dsh-agent', 'dsh-llm')) { $junction = Join-Path $shimModules $packageName if (-not (Test-Path -LiteralPath $junction)) { $target = Join-Path $globalNodeRoot "@deepseek-ai\dsh\node_modules\@deepseek-ai\$packageName

**配置**

`stateDirectory` 必填。未配置选项时使用下列默认值。 `dsh-prime-agent/runtime` 条目接受执行预算字段（`computeMs`、`maxWallMs`、`maxOutputBytes`、`maxOldGenerationSizeMb`）；显式值逐字透传，未配置时 Worker old-generation 使用 Prime 默认 64 MiB。Realm pool 治理项默认 `maxActiveRealms: 32`、`maxIdleMs: 600000`、`maxHostCallsPerRun: 200`、`maxParallelHostCallsPerRun: 16`。条目还接受单槽 completion 保留与投影上限（`maxCompletionRetainedBytes`、`maxCompletionRetainedNodes`、`max

## 🔗 链接

- [GitHub 仓库](https://github.com/yoke233/dsh-prime-agent)
- [完整 README](https://github.com/yoke233/dsh-prime-agent#readme)
- [返回dsh-prime-agent所在分类](../workflows.md)
