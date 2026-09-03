---
title: "dsh-univer-office"
description: "Give DeepSeek Harness a real office environment.  Univer Office Plugin brings spreadsheets, docs, slides, canvases, relational tables, and more into one runtime — with connected data, validation, versioned changes, and isolated worktrees for multi-agent collaboration."
keywords: "dsh-univer-office, multi-agent, agent, coding, deepseek harness, dsh"
---
# dsh-univer-office

> ⭐ **191** · ✅ active · agent

| | | | |
|---|---|---|---|
| Type | agent | Category | Multi-agent |
| Stars | ⭐ 191 | Status | ✅ active |
| Author | [dream-num](https://github.com/dream-num) | Updated | — |

## One-liner

> Give DeepSeek Harness a real office environment.  Univer Office Plugin brings spreadsheets, docs, slides, canvases, relational tables, and more into one runtime — with connected data, validation, versioned changes, and isolated worktrees for multi-agent collaboration.

## About

English · [简体中文](README.zh-CN.md) `dsh-univer-office` is the Univer office plugin for DeepSeek Harness (DSH). Tell the agent what you need and it can create or edit spreadsheets, documents, presentations, multidimensional tables, and canvases, or work with existing Excel, Word, and PowerPoint files. Every change is verified and stays in the conversation for you to preview, approve, or discard. After installation, describe the result you want in natural language. The agent handles creation, editing, and verification while you follow the work live and review the result in the conversation. Deliver spreadsheets as Excel (`.xlsx`), documents as Word (`.docx`), and presentations as PowerPoint (`.pptx`) files when needed.

## ✨ Key Features

- **Analyze and build spreadsheets** — read or create Excel data, clean fields, write formulas, apply formatting and validation, create tables, charts, pivots, fi
- **Write and lay out documents** — create paragraphs, rich text, lists, tasks, tables, images, charts, headers, footers, pagination, and page layouts.
- **Create and revise presentations** — generate a deck from an outline, redesign selected pages, edit text, shapes, images, tables, charts, and transitions, then
- **Build lightweight databases** — create Base tables, fields, records, and views with formula fields, filters, sorting, grouping, and Sheet-backed references.
- **Draw editable canvases** — create shapes, text, connectors, images, native charts, and diagrams, with connector and layout analysis.
- **Compose several content types** — one `.univer` file can contain Sheets, Docs, Slides, Bases, and Boards. Formulas and embedded content can reference other co
- **Work with Office files** — import `.xlsx`, `.csv`, `.tsv`, `.docx`, and `.pptx`, then export the edited content in the matching format.
- **Review agent changes safely** — every write starts in an isolated draft. Watch changes live, then approve or discard them instead of letting the agent overwri

## 📦 Install

```bash
dsh plugin --profile web add dsh-univer-office
```

## 🚀 Quick Start

```bash
dsh web
```

## 📚 Learn more

**Example requests**

Create a simple payroll spreadsheet with employee, base salary, bonus, deduction, gross pay, and net pay columns. Calculate the totals automatically. Create a six-slide lesson deck about bubble sort. Explain the concept, each comparison pass, pseudocode, and complexity, and check every page for layout problems. Create a formal weekly project report with an executive summary, this week's progress, 

**1. Install the plugin**

Supported DSH versions are `0.1.1-rc.2` and the `0.1.2-alpha.1` through `0.1.2-alpha.5` prereleases. If DSH is running, first press **Ctrl+C** in the terminal that started it. You can run the installation command while DSH is running, but the current DSH process will not load the new plugin automatically. Install the plugin from npm: dsh plugin --profile web add dsh-univer-office Restart DSH after

**Configuration**

The defaults are designed for local use: the service starts at port `9080`. If that port is occupied, it tries `9081`, then continues upward one port at a time. Set these plugin options when you need different values:

## 🔗 Links

- [GitHub Repository](https://github.com/dream-num/dsh-univer-office)
- [Full README](https://github.com/dream-num/dsh-univer-office#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
