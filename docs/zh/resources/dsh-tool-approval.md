---
title: "dsh-tool-approval"
description: "Manual approval for Deepseek Harness (aka \"Manual Mode\"/\"Ask Mode\")"
keywords: "dsh-tool-approval, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-tool-approval

> ⭐ **1** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [ilharp](https://github.com/ilharp) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Manual approval for Deepseek Harness (aka "Manual Mode"/"Ask Mode")

## 详细介绍

Add pre-approval to any Tool Calling, aka "Manual Mode"/"Ask Mode".

## 📦 安装

```bash
dsh plugin --profile web add dsh-tool-approval
```

## 🚀 快速开始

```bash
- id: tool-approval
  name: dsh-tool-approval
```

## 📚 更多信息

**Default config**

name: dsh-tool-approval With the default config, every Tool Calling goes through pre-approval.

**Custom config**

name: dsh-tool-approval config: include: [fs_*, web_*] exclude: [task_output] reason: tool execution requires your approval Only tools specified in `include` get pre-approval; tools in `exclude` pass through. Wildcards are supported.

## 🔗 链接

- [GitHub 仓库](https://github.com/ilharp/dsh-tool-approval)
- [完整 README](https://github.com/ilharp/dsh-tool-approval#readme)
- [返回dsh-tool-approval所在分类](../plugins.md)
