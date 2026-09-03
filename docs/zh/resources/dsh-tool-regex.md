---
title: "dsh-tool-regex"
description: "DSH 正则工具插件：测试匹配/提取捕获组/安全替换/静态解释正则（不执行代码），零依赖，注册 regex 工具"
keywords: "dsh-tool-regex, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-tool-regex

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [omdsh-dev](https://github.com/omdsh-dev) | 更新时间 | — |
| 子分类 | 🛡️ 安全与运维 | 能力 | coding |

## 一句话介绍

> DSH 正则工具插件：测试匹配/提取捕获组/安全替换/静态解释正则（不执行代码），零依赖，注册 regex 工具

## 详细介绍

[English](README.en.md) DSH 正则工具插件 —— 测试匹配、提取捕获组、安全替换、**静态解释正则含义（不执行任何代码）**。零依赖、纯函数。

## 📦 安装

```bash
# 交互式（web）profile —— 从 GitHub 仓库安装
dsh plugin --profile web add github:omdsh-dev/dsh-tool-regex
# 一次性任务（headless）profile —— dsh run 默认使用 headless
dsh plugin --profile headless add github:omdsh-dev/dsh-tool-regex
```

## 🚀 快速开始

```bash
npm pack     # 生成 dsh-tool-regex-<version>.tgz
# 交互式（web）profile
dsh plugin --profile web add ./dsh-tool-regex-<version>.tgz
# 一次性任务（headless）profile
dsh plugin --profile headless add ./dsh-tool-regex-<version>.tgz
```

## 📚 更多信息

**示例**

regex { action: "find", pattern: "(\\w+)@(\\w+)", input: "a@b x c@d" } → [{"index":0,"match":"a@b","captures":["a","b"],"groups":null},{"index":6,"match":"c@d","captures":["c","d"],"groups":null}] regex { action: "replace", pattern: "(\\w+) (\\w+)", input: "hello world", replacement: "$2 $1" } → {"result":"world hello","replaced":1} regex { action: "explain", pattern: "\\d{4}-\\d{2}" } → [{"kind":

**一次性任务（headless）profile —— dsh run 默认使用 headless**

dsh plugin --profile headless add github:omdsh-dev/dsh-tool-regex 或使用 `npm pack` 生成的 tarball 安装： npm pack # 生成 dsh-tool-regex-<version>.tgz

**手动安装与旧版本兼容（monorepo 旧场景）**

monorepo 方式仅适用于旧场景：不支持 Profile Bundle 的旧快照或插件开发调试环境（本地 junction/symlink、手动编辑 profile 层）。

## 🔗 链接

- [GitHub 仓库](https://github.com/omdsh-dev/dsh-tool-regex)
- [完整 README](https://github.com/omdsh-dev/dsh-tool-regex#readme)
- [返回dsh-tool-regex所在分类](../plugins.md)
