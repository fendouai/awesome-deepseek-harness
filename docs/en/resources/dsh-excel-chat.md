---
title: "dsh-excel-chat"
description: "dsh-excel-chat — talk to Excel in DeepSeek Harness: create, edit, repair, and verify spreadsheets by conversation (cells, formulas, styles, filters, tables, charts); every edit is auto-validated."
keywords: "dsh-excel-chat, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-excel-chat

> ⭐ **6** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [hccccc01333](https://github.com/hccccc01333) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> dsh-excel-chat — talk to Excel in DeepSeek Harness: create, edit, repair, and verify spreadsheets by conversation (cells, formulas, styles, filters, tables, charts); every edit is auto-validated.

## About

在 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 里用自然语言 操作 Excel：说一句“给 D 列加毛利公式、表头加粗、冻结首行、加筛选”，agent 会自动 调用 `excel_operate` 完成；每次编辑后自动体检公式有没有被弄坏，也可以让它 “检查这个表哪里算错了”并自动修复。所有工作都在对话里完成，不需要记 Excel 操作。

## 📦 Install

```bash
dsh plugin --profile demo add dsh-excel-chat          # 从 npm 安装
dsh plugin --profile demo add ./bundle                # 或本地 bundle 目录
```

## 🚀 Quick Start

```bash
dsh-excel-chat-doctor                                  # npm 全局/npx 可用时
# 或 profile 内直接跑：
# ~/.dsh/profiles/demo/node_modules/.bin/dsh-excel-chat-doctor
```

## 📚 Learn more

**安装**

dsh plugin --profile demo add dsh-excel-chat # 从 npm 安装 dsh plugin --profile demo add ./bundle # 或本地 bundle 目录 装完先自检一次，确认宿主包隔离和引擎都正常： dsh-excel-chat-doctor # npm 全局/npx 可用时

**~/.dsh/profiles/demo/node_modules/.bin/dsh-excel-chat-doctor**

装完直接聊，例如： > 帮我把 report.xlsx 做成报表：D 列是毛利（收入减成本），E 列加合计， > 表头加粗填浅灰，冻结第一行，加筛选。 > 检查 sales.xlsx 里 D 列公式是不是每行都是“收入-成本”，不对的帮我修掉。 完整使用指南见 [docs/usage.md](docs/usage.md)，岗位用法（运营/产品/数分）见 [docs/roles.md](docs/roles.md)。

**给使用者：一分钟上手**

前提：已安装 DeepSeek Harness（`dsh` CLI 或桌面端）。 dsh plugin --profile demo add dsh-excel-chat # 从 npm 安装

**dsh plugin --profile demo add github:hccccc01333/dsh-excel-c**

dsh web --profile demo # 打开对话界面 然后在对话里直接说： 平台说明：公式校验/修复、读写单元格、样式、汇总、合并、邮件合并等功能跨平台； 图表创建/改参、原生透视表、图表 PNG 导出需要 Windows + 本机安装 Excel。 锁定版本：`dsh plugin --profile demo add dsh-excel-chat@0.23.0`（不写版本默认 latest）。

## 🔗 Links

- [GitHub Repository](https://github.com/hccccc01333/dsh-excel-chat)
- [Full README](https://github.com/hccccc01333/dsh-excel-chat#readme)
- [Back to the Plugins list](../plugins.md)
