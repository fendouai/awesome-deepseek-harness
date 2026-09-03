---
title: "dsh-tool-approval"
description: "Manual approval for Deepseek Harness (aka \"Manual Mode\"/\"Ask Mode\")"
keywords: "dsh-tool-approval, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-tool-approval

> ⭐ **1** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [ilharp](https://github.com/ilharp) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Manual approval for Deepseek Harness (aka "Manual Mode"/"Ask Mode")

## About

Add pre-approval to any Tool Calling, aka "Manual Mode"/"Ask Mode".

## 📦 Install

```bash
dsh plugin --profile web add dsh-tool-approval
```

## 🚀 Quick Start

```bash
- id: tool-approval
  name: dsh-tool-approval
```

## 📚 Learn more

**Default config**

name: dsh-tool-approval With the default config, every Tool Calling goes through pre-approval.

**Custom config**

name: dsh-tool-approval config: include: [fs_*, web_*] exclude: [task_output] reason: tool execution requires your approval Only tools specified in `include` get pre-approval; tools in `exclude` pass through. Wildcards are supported.

## 🔗 Links

- [GitHub Repository](https://github.com/ilharp/dsh-tool-approval)
- [Full README](https://github.com/ilharp/dsh-tool-approval#readme)
- [Back to the Plugins list](../plugins.md)
