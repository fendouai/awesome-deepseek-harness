---
title: "dsh-tool-csv"
description: "DSH CSV 数据工具插件：解析/查询/统计/转换 CSV 文本（RFC 4180），零依赖状态机解析器，注册 csv 工具"
keywords: "dsh-tool-csv, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-tool-csv

> ⭐ **4** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | — |
| Subcategory | 💰 Cost & billing | Capabilities | coding |

## One-liner

> DSH CSV 数据工具插件：解析/查询/统计/转换 CSV 文本（RFC 4180），零依赖状态机解析器，注册 csv 工具

## About

[English](README.en.md) DSH CSV 数据工具插件 —— 解析、查询、过滤、统计和转换 CSV 文本。零依赖、纯函数、RFC 4180 状态机解析器。

## ✨ Key Features

- **零依赖**：不引入 csv 解析库，手写状态机（单遍扫描，O(n)）
- **纯函数**：不读文件、不写文件、不联网、不 eval
- **无注入面**：查询过滤只做字面精确匹配（`===`），不支持表达式求值
- **预算**：输入上限 256,000 字节（超限直接报错，不截断）；`timeoutMs: 2000`；`limit` 默认 100 行防输出膨胀
- 工具参数会记入会话日志，不要传入敏感数据

## 📦 Install

```bash
# 交互式（web）profile
dsh plugin --profile web add github:omdsh-dev/dsh-tool-csv
# 一次性任务（headless）profile —— dsh run 默认使用 headless
dsh plugin --profile headless add github:omdsh-dev/dsh-tool-csv
```

## 🚀 Quick Start

```bash
git clone https://github.com/omdsh-dev/dsh-tool-csv
cd dsh-tool-csv
npm install && npm pack
dsh plugin --profile web add ./deepseek-ai-dsh-tool-csv-*.tgz
dsh plugin --profile headless add ./deepseek-ai-dsh-tool-csv-*.tgz
```

## 📚 Learn more

**示例**

csv { action: "parse", csv: "name,city\nalice,nyc\nbob,la" } → [{"name":"alice","city":"nyc"},{"name":"bob","city":"la"}] csv { action: "query", csv: "name,city\nalice,nyc\nbob,la", column: "city", value: "la" } → [["name","city"],["bob","la"]] csv { action: "stats", csv: "name,city\nalice,nyc" } → {"rows":1,"columns":2,"columnNames":["name","city"],"emptyRows":0,"warnings":[]}

**一次性任务（headless）profile —— dsh run 默认使用 headless**

dsh plugin --profile headless add github:omdsh-dev/dsh-tool-csv 也可以先用 `npm pack` 打出 tarball 再安装： git clone https://github.com/omdsh-dev/dsh-tool-csv cd dsh-tool-csv npm install && npm pack dsh plugin --profile web add ./deepseek-ai-dsh-tool-csv-*.tgz dsh plugin --profile headless add ./deepseek-ai-dsh-tool-csv-*.tgz 包内 `dsh.bundle.patch` 会在安装后自动把插件加入 profile 的 layer stack（row id：`tool-csv`）。插件缺失的 

**手动安装（源码贡献 / 旧 snapshot 场景）**

仅适用于源码贡献（在 monorepo 中开发调试本插件）或仍在使用旧 snapshot 的场景（本地 junction/symlink、手动编辑 profile 层）。

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-tool-csv)
- [Full README](https://github.com/omdsh-dev/dsh-tool-csv#readme)
- [Back to the Plugins list](../plugins.md)
