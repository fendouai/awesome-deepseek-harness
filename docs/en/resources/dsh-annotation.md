---
title: "dsh-annotation"
description: "Select text in DSH Web, annotate it and send the annotation with your message; replies cross-reference each annotation."
keywords: "dsh-annotation, input-editing, plugin, ui, deepseek harness, dsh"
---
# dsh-annotation

> ⭐ **87** · ✅ active · plugin · ⬆️ +6 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Input & editing |
| Stars | ⭐ 87 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | 2026-08-21 |

## One-liner

> Select text in DSH Web, annotate it and send the annotation with your message; replies cross-reference each annotation.

## About

**English** · [简体中文](./README.zh-CN.md) Selection-annotation plugin for DSH Web: select text → annotate → press Enter to send it along with your message; the model replies to each annotation by number. 🌐 Live Product Site — Explore dsh-annotation in DSH Select any text in an assistant reply to annotate it (the annotation body may be left empty = just mark the passage). Annotations accumulate across messages and turns. An **Annotations ×N** chip appears next to the input box — hover to view all annotations, remove them one by one. Press Enter and the annotation block goes to the model together with whatever question is in the input box. **The annotation block never shows up as text in your own message bubble** — only the question plus the chip (content visible on hover; hidden before paint,

## 📦 Install

```bash
npm install @changfenhuang/dsh-annotation
```

## 🚀 Quick Start

```bash
dsh plugin --profile web remove @omdsh-dev/dsh-annotation
dsh plugin --profile web add @changfenhuang/dsh-annotation
```

## 📚 Learn more

**Or install directly from the public GitHub source**

dsh plugin --profile web add git+https://github.com/omdsh-dev/dsh-annotation.git

**Architecture notes**

``` zh: 我批注了以下 N 处内容…\n\n1. 原文\n 批注：…\n\n请用「Annotation 1：…」…\n\n提问： en: I annotated the following N passage(s)…\n\n1. quote\n Note: …\n\nPlease respond… "Annotation 1: …"…\n\nAsk: ``` The zh delimiter is 「提问：」(ask:) rather than 「问题：」(question:) — the heading line "回答我的问题：" also contains the latter, and the bubble-hiding surgery would misfire on it; the en delimiter is `Ask:`. Hiding and reverse-pa

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-annotation)
- [Full README](https://github.com/omdsh-dev/dsh-annotation#readme)
- [Back to the Plugins list](../plugins.md)
