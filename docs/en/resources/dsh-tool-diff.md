---
title: "dsh-tool-diff"
description: "DSH Diff 工具插件：文本/JSON/CSV/Markdown 结构化比较与 unified diff，零依赖只读，注册 diff 工具"
keywords: "dsh-tool-diff, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-tool-diff

> ⭐ **4** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | — |
| Subcategory | 🧪 Code, tests & review | Capabilities | coding |

## One-liner

> DSH Diff 工具插件：文本/JSON/CSV/Markdown 结构化比较与 unified diff，零依赖只读，注册 diff 工具

## About

[English](README.en.md) DSH Diff 文本差异工具插件 —— 文本 / JSON / CSV / Markdown 结构化比较与 unified diff 生成。零依赖、纯函数、只读。

## ✨ Key Features

- **零依赖**：Myers 行级 diff、RFC 4180 解析器、JSON 递归比较全部手写
- **只读**：不读文件、不写文件、不联网、不调 git；`patch` action 只在内存中生成并校验补丁，绝不落盘
- **预算**：
- 工具参数会记入会话日志，不要传入敏感数据

## 📦 Install

```bash
# 交互式（web）profile
dsh plugin --profile web add github:omdsh-dev/dsh-tool-diff
# 一次性任务（headless）profile —— dsh run 默认使用 headless
dsh plugin --profile headless add github:omdsh-dev/dsh-tool-diff
```

## 🚀 Quick Start

```bash
git clone https://github.com/omdsh-dev/dsh-tool-diff
cd dsh-tool-diff
npm install && npm pack
dsh plugin --profile web add ./deepseek-ai-dsh-tool-diff-*.tgz
dsh plugin --profile headless add ./deepseek-ai-dsh-tool-diff-*.tgz
```

## 📚 Learn more

**输出示例**

{"kind":"json","equal":false,"beforeBytes":42,"afterBytes":58,"changes":[ {"op":"replace","path":"$.tags[1]","before":"b","after":"c"}, {"op":"add","path":"$.user.email","after":"b@x.com"}, {"op":"replace","path":"$.user.name","before":"Alice","after":"Bob"}], "summary":{"added":1,"removed":0,"replaced":2,"moved":0}}

**一次性任务（headless）profile —— dsh run 默认使用 headless**

dsh plugin --profile headless add github:omdsh-dev/dsh-tool-diff 也可以先用 `npm pack` 打出 tarball 再安装： git clone https://github.com/omdsh-dev/dsh-tool-diff cd dsh-tool-diff npm install && npm pack dsh plugin --profile web add ./deepseek-ai-dsh-tool-diff-*.tgz dsh plugin --profile headless add ./deepseek-ai-dsh-tool-diff-*.tgz 包内 `dsh.bundle.patch` 会在安装后自动把插件加入 profile 的 layer stack（row id：`tool-diff`）。

**手动安装（源码贡献 / 旧 snapshot 场景）**

仅适用于源码贡献（在 monorepo 中开发调试本插件）或仍在使用旧 snapshot 的场景（本地 junction/symlink、手动编辑 profile 层）。

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-tool-diff)
- [Full README](https://github.com/omdsh-dev/dsh-tool-diff#readme)
- [Back to the Plugins list](../plugins.md)
