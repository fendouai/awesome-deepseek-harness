---
title: "dsh-wps"
description: "WPS / Kingsoft cloud-docs integration for DSH: official SkillHub MCP, custom browser authorization, cloud-drive ops + text/sheet/presentation/PDF content under mcp__wps__*."
keywords: "dsh-wps, developer, plugin, files, mcp, deepseek harness, dsh"
---
# dsh-wps

> ⭐ **0** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 0 | Status | ✅ active |
| Author | [zhengjy01](https://github.com/zhengjy01) | Updated | — |
| Subcategory | 🛡️ Security & ops | Capabilities | files, mcp |

## One-liner

> WPS / Kingsoft cloud-docs integration for DSH: official SkillHub MCP, custom browser authorization, cloud-drive ops + text/sheet/presentation/PDF content under mcp__wps__*.

## About

WPS / 金山文档 (WPS Cloud Docs) integration for DeepSeek Harness (DSH). Talk to your **WPS cloud drive** in the DSH conversation: list / search / read / create / upload-download cloud documents, and read / write their text / spreadsheet / presentation / PDF content. It connects to the **official Kingsoft SkillHub MCP** (`https://mcp-center.wps.cn/skill_hub/mcp`) and registers its tools as `mcp__wps__*`. - Custom browser authorization (auth-guide + exchange-poll token), no standard OAuth. - Access token stored at `~/.dsh/dsh-wps.json` (mode 0600). - **558 tools** discovered dynamically from the official SkillHub (drive / wps / sheet / wpp / dbsheet / pdf / form / aippt). - Auto-registers `mcp__wps__` tools + 4 helper tools (`wps_status` / `wps_oauth_start` / `wps_test` / `wps_clear`) + a web se

## ✨ Key Features

- Custom browser authorization (auth-guide + exchange-poll token), no standard OAuth.
- Access token stored at `~/.dsh/dsh-wps.json` (mode 0600).
- **558 tools** discovered dynamically from the official SkillHub (drive / wps / sheet /
- Auto-registers `mcp__wps__<name>` tools + 4 helper tools (`wps_status` /

## 📦 Install

```bash
dsh plugin --profile web add dsh-wps
# or from Git:
# dsh plugin --profile web add github.com/zhengjy01/dsh-wps
```

## 🔗 Links

- [GitHub Repository](https://github.com/zhengjy01/dsh-wps)
- [Full README](https://github.com/zhengjy01/dsh-wps#readme)
- [Back to the Plugins list](../plugins.md)
