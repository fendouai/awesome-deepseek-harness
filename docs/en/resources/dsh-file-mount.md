---
title: "dsh-file-mount"
description: "Incremental file mounting with line-range deduplication: identical file contents are never re-sent to the model."
keywords: "dsh-file-mount, memory, plugin, context, files, deepseek harness, dsh"
---
# dsh-file-mount

> ⭐ **11** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 11 | Status | ✅ active |
| Author | [acefun29](https://github.com/acefun29) | Updated | 2026-08-17 |

## One-liner

> Incremental file mounting with line-range deduplication: identical file contents are never re-sent to the model.

## About

DeepSeek Harness 插件：**文件增量挂载 + 重复读取去重**。记录每个文件哪些行范围已经进入模型上下文，重复读取只补缺失部分；文件在磁盘上变化时按行级对比只补改动的行；并提供「挂载文件」仪表盘实时展示账本。 移植自 [piwpi](https://github.com/earendil-works/pi-mono) 的 context-mount 机制。

## ✨ Key Features

- **模型侧**：读过的行范围不重复进上下文（去重 marker）；缺失/改动的正文写进本次 read 的工具结果（增量 / 重挂），纸条只记账本声明；文件改动后只补改动的行（行级 diff，日志追加只补新尾巴）；AI 自己写过的文件回头读直接免单；`file_mount_forget` 工具让模型能主动强制重读。
- **界面侧**：「挂载文件」标签页是仪表盘——打开时停在顶部，**净节省与路径搜索固定在顶栏**，文件列表单独滚动；每个文件行可展开成**文件段**列表，每段带**新鲜度色带**（绿=新鲜/黄=一般/橙=接近过期/红=已过期/灰=未知）和**过期次数**；另有**覆盖图**（色块标出已挂载行在文件中的位置）、搜索、排序
- **节省统计**：中文按 1 字 ≈ 1 token、其他按 4 字符 ≈ 1 token 估算；同时记账「省下的」和「纸条花掉的」，界面显示**净值**（为负时按 0 显示）；可选把跨会话总账落盘（`statsFile`）。

## 📦 Install

```bash
npx --yes @deepseek-ai/dsh plugin --profile web add https://github.com/acefun29/dsh-file-mount/releases/latest/download/dsh-file-mount.tgz
npx --yes @deepseek-ai/dsh --profile web
```

## 🚀 Quick Start

```bash
pnpm dsh:install
```

## 📚 Learn more

**安装**

一个包两面：`dsh.bundle.patch` 挂载宿主插件行，`dsh.client` manifest 让 Web 端扫描出浏览器半部。装进 profile 后**必须重启 harness**（刷新页面不够）。需要本机有 **pnpm**（`dsh plugin` 转调它）和 Node `^22.19 || >=24`。

**配置**

name: dsh-file-mount config: enabled: true # 总开关；关闭后所有读取原生透传 capacity: 32 # 文件身份缓存容量（挂载中文件不受淘汰影响） ttlMs: 300000 # 缓存安全阀：同 stat 内容被改的兜底重读间隔 maxPinnedFiles: 256 # 单个会话最多钉住多少个挂载文件 minSavedTokens: 16 # 去重/增量净收益低于此值则原生透传且不写账本（也不计入安全阀次数） maxFingerprintBytes: 1000000 # 超过此大小的文件不留行级底稿（改动时整本重挂） maxManagedBytes: 16777216 # 超过此大小的文件不接管，原样放行 excludeGlobs: ['**/node_modules/**'] # 这些路径永远原样放行 statsFile: ./dsh-f

**工作原理**

插件挂在 `tools/post-execute` 拦截面，按工具名分流： 1. **read**：以 canonical value（path/offset/lines/totalLines）为准确定本次窗口；经 stat 校验式缓存（mtime+size 快路径 + sha256）核实磁盘身份后三分支决策：完全覆盖 → 结果换成去重 marker（同一个文件在两次真实消息之间只发第一条去重纸条，重复去重静默合并节省）；部分覆盖 / hash 变化 → **缺失或改动的正文写进本次 read 的工具结果**（每行带 `N: ` 行号，与原生 read 对齐；`cancel` 清 inbox 最多丢掉账本纸条，下次当没挂过再发），纸条只留 head-only 账本声明；hash 变化时拿行级底稿做 diff，**只补改动的行**（没动的行号平移；中段过大时用唯一行锚点切分 LCS），没底稿

## 🔗 Links

- [GitHub Repository](https://github.com/acefun29/dsh-file-mount)
- [Full README](https://github.com/acefun29/dsh-file-mount#readme)
- [Back to the Plugins list](../plugins.md)
