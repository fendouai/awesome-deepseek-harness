---
title: "dsh-tool-schema"
description: "DSH JSON Schema 验证工具插件：validate/paths/explain/normalize，零网络零动态执行"
keywords: "dsh-tool-schema, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-tool-schema

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [omdsh-dev](https://github.com/omdsh-dev) | 更新时间 | — |
| 子分类 | 🧰 工具与工具包 | 能力 | coding |

## 一句话介绍

> DSH JSON Schema 验证工具插件：validate/paths/explain/normalize，零网络零动态执行

## 详细介绍

[English](README.en.md) DSH JSON Schema 验证工具插件 —— 验证数据、列出失败路径、解释 schema 约束、安全应用 default。零网络、零动态代码执行。

## ✨ 核心特性

- **零动态执行**：验证内核是纯数据遍历，不构造 `RegExp`（pattern 在独立 worker 内执行）、不 `eval`、不访问网络、不读文件
- **不支持关键字绝不静默忽略**：报告 `unsupported-keyword` schema issue；`strictSchema=true`（默认）直接失败（`valid:false` / `complete:false`），`strictSchema=false` 验证已支持子集（`valid:null` /
- **ReDoS 防线**：所有 `pattern` 校验在**可终止的 worker 线程**内共享 1,000ms 硬预算，超时 `terminate()` 并报错——灾难性回溯不能阻塞宿主进程；pattern ≤ 16 KiB、每 schema ≤ 100 个
- **原型污染防护**：所有对象访问用 `Object.hasOwn`，`__proto__` / `constructor` / `prototype` 只作为普通 JSON 键处理
- **`$ref` 安全性**：仅支持本地引用（`#` 与 `#/$defs/<token>`，RFC 6901 转义）；目标必须存在；环检测（schema-check 静态报告 `ref-cycle` + 验证期 `(schemaNode, instance)` 栈动态兜底）
- **预算**：

## 📦 安装

```bash
# 交互式（web）profile
dsh plugin --profile web add github:omdsh-dev/dsh-tool-schema
# 一次性任务（headless）profile —— dsh run 默认使用 headless
dsh plugin --profile headless add github:omdsh-dev/dsh-tool-schema
```

## 🚀 快速开始

```bash
# tarball 方式（web 为例；headless 同）
npm pack
dsh plugin --profile web add <npm pack 产物 tarball 路径>
```

## 📚 更多信息

**输出示例**

{"action":"validate","complete":true,"valid":true,"supportedSubsetValid":true, "errors":[],"schemaIssues":[],"checkedNodes":3,"truncated":false} {"action":"paths","valid":false,"paths":[{"path":"/a","keywords":["type"]}], "errorCount":1,"truncated":false} {"action":"normalize","valid":true, "appliedDefaults":[{"path":"/b","value":5}],"warnings":[]}

**一次性任务（headless）profile —— dsh run 默认使用 headless**

dsh plugin --profile headless add github:omdsh-dev/dsh-tool-schema 包内 `dsh.bundle.patch` 会在安装后自动把插件加入 profile 的 layer stack（row id：`tool-schema`）。插件缺失的 peer 依赖（`cordis`、`@deepseek-ai/dsh-tools`）由 profile 的 healed `profiles/node_modules` 回退安装提供。 > ⚠️ web 与 headless 是**不同 profile**：web 安装不会自动覆盖 headless；`dsh run` 默认使用 headless profile。Windows 路径使用正斜杠（`C:/...`）。

**手动安装与旧版本兼容**

旧场景（monorepo 集成、不支持 Profile Bundle 的旧快照或插件开发调试环境——本地 junction/symlink、手动编辑 profile 层）。

## 🔗 链接

- [GitHub 仓库](https://github.com/omdsh-dev/dsh-tool-schema)
- [完整 README](https://github.com/omdsh-dev/dsh-tool-schema#readme)
- [返回dsh-tool-schema所在分类](../plugins.md)
