---
title: "dsh-wps"
description: "WPS / 金山文档云文档集成插件：官方 SkillHub MCP，自定义浏览器授权，云盘操作 + 文字/表格/演示/PDF 内容读写，工具以 mcp__wps__* 在会话中可用。"
keywords: "dsh-wps, developer, plugin, files, mcp, deepseek harness, dsh"
---
# dsh-wps

> ⭐ **0** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 0 | 状态 | ✅ 活跃 |
| 作者 | [zhengjy01](https://github.com/zhengjy01) | 更新时间 | — |
| 子分类 | 🛡️ 安全与运维 | 能力 | files, mcp |

## 一句话介绍

> WPS / 金山文档云文档集成插件：官方 SkillHub MCP，自定义浏览器授权，云盘操作 + 文字/表格/演示/PDF 内容读写，工具以 mcp__wps__* 在会话中可用。

## 详细介绍

WPS / 金山文档 (WPS Cloud Docs) integration for DeepSeek Harness (DSH). Talk to your **WPS cloud drive** in the DSH conversation: list / search / read / create / upload-download cloud documents, and read / write their text / spreadsheet / presentation / PDF content. It connects to the **official Kingsoft SkillHub MCP** (`https://mcp-center.wps.cn/skill_hub/mcp`) and registers its tools as `mcp__wps__*`. - Custom browser authorization (auth-guide + exchange-poll token), no standard OAuth. - Access token stored at `~/.dsh/dsh-wps.json` (mode 0600). - **558 tools** discovered dynamically from the official SkillHub (drive / wps / sheet / wpp / dbsheet / pdf / form / aippt). - Auto-registers `mcp__wps__` tools + 4 helper tools (`wps_status` / `wps_oauth_start` / `wps_test` / `wps_clear`) + a web se

## ✨ 核心特性

- Custom browser authorization (auth-guide + exchange-poll token), no standard OAuth.
- Access token stored at `~/.dsh/dsh-wps.json` (mode 0600).
- **558 tools** discovered dynamically from the official SkillHub (drive / wps / sheet /
- Auto-registers `mcp__wps__<name>` tools + 4 helper tools (`wps_status` /

## 📦 安装

```bash
dsh plugin --profile web add dsh-wps
# or from Git:
# dsh plugin --profile web add github.com/zhengjy01/dsh-wps
```

## 🔗 链接

- [GitHub 仓库](https://github.com/zhengjy01/dsh-wps)
- [完整 README](https://github.com/zhengjy01/dsh-wps#readme)
- [返回dsh-wps所在分类](../plugins.md)
