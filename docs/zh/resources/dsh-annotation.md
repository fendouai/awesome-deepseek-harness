---
title: "dsh-annotation"
description: "DSH Web 选中批注：选文字→批注→随消息发送，回复按批注逐条对照。"
keywords: "dsh-annotation, input-editing, plugin, ui, deepseek harness, dsh"
---
# dsh-annotation

> ⭐ **87** · ✅ 活跃 · 插件 · 近期 ⬆️ +6

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 输入与编辑 |
| 星数 | ⭐ 87 | 状态 | ✅ 活跃 |
| 作者 | [omdsh-dev](https://github.com/omdsh-dev) | 更新时间 | 2026-08-21 |

## 一句话介绍

> DSH Web 选中批注：选文字→批注→随消息发送，回复按批注逐条对照。

## 详细介绍

**English** · [简体中文](./README.zh-CN.md) Selection-annotation plugin for DSH Web: select text → annotate → press Enter to send it along with your message; the model replies to each annotation by number. 🌐 Live Product Site — Explore dsh-annotation in DSH Select any text in an assistant reply to annotate it (the annotation body may be left empty = just mark the passage). Annotations accumulate across messages and turns. An **Annotations ×N** chip appears next to the input box — hover to view all annotations, remove them one by one. Press Enter and the annotation block goes to the model together with whatever question is in the input box. **The annotation block never shows up as text in your own message bubble** — only the question plus the chip (content visible on hover; hidden before paint,

## 📦 安装

```bash
npm install @changfenhuang/dsh-annotation
```

## 🚀 快速开始

```bash
dsh plugin --profile web remove @omdsh-dev/dsh-annotation
dsh plugin --profile web add @changfenhuang/dsh-annotation
```

## 📚 更多信息

**Or install directly from the public GitHub source**

dsh plugin --profile web add git+https://github.com/omdsh-dev/dsh-annotation.git

**Architecture notes**

``` zh: 我批注了以下 N 处内容…\n\n1. 原文\n 批注：…\n\n请用「Annotation 1：…」…\n\n提问： en: I annotated the following N passage(s)…\n\n1. quote\n Note: …\n\nPlease respond… "Annotation 1: …"…\n\nAsk: ``` The zh delimiter is 「提问：」(ask:) rather than 「问题：」(question:) — the heading line "回答我的问题：" also contains the latter, and the bubble-hiding surgery would misfire on it; the en delimiter is `Ask:`. Hiding and reverse-pa

## 🔗 链接

- [GitHub 仓库](https://github.com/omdsh-dev/dsh-annotation)
- [完整 README](https://github.com/omdsh-dev/dsh-annotation#readme)
- [返回dsh-annotation所在分类](../plugins.md)
