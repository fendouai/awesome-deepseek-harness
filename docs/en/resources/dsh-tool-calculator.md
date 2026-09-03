---
title: "dsh-tool-calculator"
description: "DSH 计算器工具插件：安全的数学表达式求值器，零依赖递归下降解析器"
keywords: "dsh-tool-calculator, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-tool-calculator

> ⭐ **8** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 8 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | — |
| Subcategory | 🛡️ Security & ops | Capabilities | coding |

## One-liner

> DSH 计算器工具插件：安全的数学表达式求值器，零依赖递归下降解析器

## About

[English](README.en.md) DSH 计算器工具插件 —— 安全的数学表达式求值器。零依赖、零进程、纯函数。

## ✨ Key Features

- 词法层只识别数字字面量、白名单标识符、运算符；引号、分号、反引号、`{}` `[]` 直接报错
- 标识符按名查白名单表（15 个函数 + 2 个常量），查不到即抛 `Unknown identifier`
- 求值结果必须是有限数字，`NaN`/`Infinity`（除零、负数开方等）统一拒绝

## 📦 Install

```bash
# 交互式（web）profile
dsh plugin --profile web add github:omdsh-dev/dsh-tool-calculator
# 一次性任务（headless）profile —— dsh run 默认使用 headless
dsh plugin --profile headless add github:omdsh-dev/dsh-tool-calculator
```

## 🚀 Quick Start

```bash
git clone https://github.com/omdsh-dev/dsh-tool-calculator
cd dsh-tool-calculator
npm install && npm pack
dsh plugin --profile web add ./deepseek-ai-dsh-tool-calculator-*.tgz
dsh plugin --profile headless add ./deepseek-ai-dsh-tool-calculator-*.tgz
```

## 📚 Learn more

**一次性任务（headless）profile —— dsh run 默认使用 headless**

dsh plugin --profile headless add github:omdsh-dev/dsh-tool-calculator 也可以先用 `npm pack` 打出 tarball 再安装： git clone https://github.com/omdsh-dev/dsh-tool-calculator cd dsh-tool-calculator npm install && npm pack dsh plugin --profile web add ./deepseek-ai-dsh-tool-calculator-*.tgz dsh plugin --profile headless add ./deepseek-ai-dsh-tool-calculator-*.tgz 包内 `dsh.bundle.patch`（指向 `cordis.patch.yml`）会在安

**手动安装（源码贡献 / 旧 snapshot 场景）**

适用于源码贡献（在 monorepo 中开发调试本插件）或仍在使用旧 snapshot 的场景： 1. 放入 monorepo：`cp -r calculator ~/.dsh/source/master/packages/tools/calculator`（开发调试） 2. `apps/cli/package.json` 加 `"@deepseek-ai/dsh-tool-calculator": "workspace:^"`；`tsconfig.host.json` references 加 `{ "path": "./packages/tools/calculator" }` 3. `pnpm install && pnpm run build` 4. 在 profile 用户层 patch 插入插件（`~/.dsh/profiles/<name>/cordis.patch.yml`

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-tool-calculator)
- [Full README](https://github.com/omdsh-dev/dsh-tool-calculator#readme)
- [Back to the Plugins list](../plugins.md)
