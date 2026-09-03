---
title: "dsh-tool-json"
description: "DSH JSON 查询工具插件：JMESPath 子集查询，零依赖递归下降解析器"
keywords: "dsh-tool-json, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-tool-json

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | — |
| Subcategory | 🧰 Toolkits | Capabilities | coding |

## One-liner

> DSH JSON 查询工具插件：JMESPath 子集查询，零依赖递归下降解析器

## About

[English](README.en.md) DSH JSON 查询工具插件 —— JMESPath-inspired 路径查询（自定义子集），零依赖递归下降解析器。

## ✨ Key Features

- `grep` 只能做字符串级搜索，容易误匹配值、key、或嵌套子对象中的同名 key
- `json` 走结构化路径，只匹配指定路径，不混淆 key 和 value

## 📦 Install

```bash
# 交互式（web）profile
dsh plugin --profile web add github:omdsh-dev/dsh-tool-json
# 一次性任务（headless）profile —— dsh run 默认使用 headless
dsh plugin --profile headless add github:omdsh-dev/dsh-tool-json
```

## 🚀 Quick Start

```bash
npm pack    # 生成 dsh-tool-json-*.tgz
dsh plugin --profile web add ./dsh-tool-json-*.tgz
dsh plugin --profile headless add ./dsh-tool-json-*.tgz
```

## 📚 Learn more

**一次性任务（headless）profile —— dsh run 默认使用 headless**

dsh plugin --profile headless add github:omdsh-dev/dsh-tool-json 包内 `dsh.bundle.patch`（指向 `cordis.patch.yml`）会在安装后自动把插件加入 profile 的 layer stack；插件的 `cordis.patch.yml` 以 `- insert:` 插入 `tool-json` 条目。 > ⚠️ web 与 headless 是**不同 profile**：web 安装不会自动覆盖 headless；`dsh run` 默认使用 headless profile。

**npm pack tarball 安装**

npm pack # 生成 dsh-tool-json-*.tgz dsh plugin --profile web add ./dsh-tool-json-*.tgz dsh plugin --profile headless add ./dsh-tool-json-*.tgz

**手动安装与旧版本兼容**

仅适用于不支持 Profile Bundle 的旧快照或插件开发调试环境： 1. 放入 monorepo：`cp -r json ~/.dsh/source/master/packages/tools/json`（开发调试） 2. `apps/cli/package.json` 加 `"@deepseek-ai/dsh-tool-json": "workspace:^"`；`tsconfig.host.json` references 加 `{ "path": "./packages/tools/json" }` 3. `pnpm install && pnpm run build` 4. 在 profile 用户层 patch 插入插件（`~/.dsh/profiles/<name>/cordis.patch.yml`）： - id: tool-json name: '@deepseek

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-tool-json)
- [Full README](https://github.com/omdsh-dev/dsh-tool-json#readme)
- [Back to the Plugins list](../plugins.md)
