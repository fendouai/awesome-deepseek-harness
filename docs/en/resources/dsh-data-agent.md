---
title: "dsh-data-agent"
description: "Session-scoped database connections with a dedicated data agent: let the model connect to databases and write SQL."
keywords: "dsh-data-agent, research, agent, coding, deepseek harness, dsh"
---
# dsh-data-agent

> ⭐ **104** · ✅ active · agent · ⬆️ +4 recently

| | | | |
|---|---|---|---|
| Type | agent | Category | Research |
| Stars | ⭐ 104 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | 2026-08-20 |

## One-liner

> Session-scoped database connections with a dedicated data agent: let the model connect to databases and write SQL.

## About

          专为数据分析与商业分析人打造的 DeepSeek 智能数据分析助手 自然语言提问 · 自动编写执行 SQL · 智能图表与报告 · AI 辅助业务治理 · 深度商业洞察 · 本地安全只读 [产品亮点](#产品亮点) · [快速上手](#快速上手) · [使用场景](#使用场景) · [工作台与报告](#工作台与报告产物) · [支持数据源](#支持数据源) · [安全与隐私](#安全与隐私) · [常见问题](#常见问题) · [开源协议](#开源协议)

## ✨ Key Features

- 💬 **零门槛对话即分析**：告别繁琐的 SQL 语法，直接用大白话提问（如“对比最近 30 天各渠道转化率”）。AI 会自动理解业务意图、探查库表结构、编写并执行查询、连续推演并输出清晰结论。
- 📊 **自动生成高品质图表与看板**：告别枯燥的纯文本与黑白表格。根据分析结论自动绘制折线图、柱状图、饼图、散点图或多维数据看板（Dashboard），并一键导出离线 HTML 报告方便分享汇报。
- 🧠 **深度挖掘商业洞察**：不止是罗列查询数字，还能自动比较波动趋势、定位异常原因、识别高价值客群与畅销品类，把冷冰冰的数据转化为可直接落地的业务建议。
- 🏷️ **AI 驱动的业务口径治理**：智能扫描数据库，自动为库表和字段标注通俗易懂的业务含义，支持人工审核与指标定义，确保每一次分析都基于统一、准确的业务口径。
- 🔒 **本地安全与只读保护**：原生支持只读账号与只读模式，查询分析全程在本地安全受控运行，凭据严格保密，保障企业生产数据安全无忧。
- 🖥️ **现代 Web 与高效终端双体验**：既可在直观的可视化 Web 界面中点击配置与浏览图表，也可在极客高效的命令行终端（dsh-tui）中一键唤起。

## 📦 Install

```bash
# 安装到 Web 界面（推荐）
dsh plugin --profile web add @yejiming/dsh-data-agent

# 或安装到终端命令行（dsh-tui）
dsh plugin --profile dsh-tui add @yejiming/dsh-data-agent
```

## 🚀 Quick Start

```bash
dsh --profile web
```

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-data-agent)
- [Full README](https://github.com/omdsh-dev/dsh-data-agent#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
