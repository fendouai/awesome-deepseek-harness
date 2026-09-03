---
title: "dsh-file-upload"
description: "DeepSeek Harness (dsh) file-message plugin: Claude-style drag-and-drop / paperclip upload, content sniffing, document-to-Markdown via Microsoft MarkItDown (with built-in JS fallback), text inlining, read_document tool for agents."
keywords: "dsh-file-upload, ui, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-file-upload

> ⭐ **20** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 20 | Status | ✅ active |
| Author | [HongMing-Huang](https://github.com/HongMing-Huang) | Updated | — |
| Subcategory | ⌨️ Input enhancement | Capabilities | coding, multi-agent, ui |

## One-liner

> DeepSeek Harness (dsh) file-message plugin: Claude-style drag-and-drop / paperclip upload, content sniffing, document-to-Markdown via Microsoft MarkItDown (with built-in JS fallback), text inlining, read_document tool for agents.

## About

**File-message plugin for DeepSeek Harness (dsh).** Claude/Codex-style uploads — drag-and-drop (files and folders), paperclip picker, paste-to-attach, multi-file support; content sniffing; fully bundled document → Markdown conversion (MarkItDown engine, 20+ formats, image OCR); Codex-style `@relative/path` references; automatic image explanations for text-only models; and a `read_document` tool for agents.

## ✨ Key Features

- **Upload** — composer paperclip button plus a global drag-and-drop overlay ("release to attach"), multi-file support.
- **Attachment cards** — color-coded type badges (PDF red / DOC blue / XLS green / TXT gray / ZIP purple / JSON gold) with name and size; removable.
- **Codex-style file references** — uploaded files appear in the message as `@relative/path` references (like OpenAI Codex), never as raw content dumped into the 
- **Codex-style `@` mentions** — type `@` in the composer to pick any uploaded file by its relative path; the reference inserts as a mention.
- **Document → Markdown, fully bundled** — the MarkItDown engine ships inside the plugin (Microsoft MarkItDown TypeScript port, `markitdown-node`): PDF / DOCX / P
- **Image explanation for text-only models** — upload an image and the plugin automatically generates a **description ("讲解图片")** through a vision discovery chain,
- **`read_document` tool for agents** — line-numbered paging (`offset`/`limit`), byte-budgeted LRU cache (invalidated on file change), size pre-checks, reads thro
- **Security** — loopback-only uploads, sanitized file names, session-isolated storage (`.dsh-uploads/<sessionId>`), sha256 content dedup, bounded concurrency, TT

## 📦 Install

```bash
dsh plugin --profile web add dsh-file-upload
# restart dsh web
```

## 🚀 Quick Start

```bash
- id: file-upload
  config:
    markitdownBin: /path/to/your/markitdown   # optional; empty = bundled engine only
```

## 📚 Learn more

**Usage**

1. Click the paperclip in the composer toolbar, or drag files anywhere over the window; 2. Small text files land directly in the composer; documents appear as attachment cards and their path is sent with the message; 3. The agent reads documents with `read_document <path>` — converted to Markdown on demand, pageable with `offset`/`limit`.

**Configuration**

> All fields have sensible defaults — you can install and use the plugin > without touching any of them. Tune only what you need.

**Architecture**

src/ ├── index.ts # entry: apply + Config schema + assembly ├── detect.ts # content sniffing (never trusts extensions) ├── convert.ts # MarkItDown engine + optional CLI backend ├── vision.ts # image explanations (vision discovery chain) ├── upload.ts # upload route: loopback/session/size/dedup/TTL ├── tool.ts # read_document: ctx.fs reads + paging + LRU cache └── client/ └── index.tsx # paperclip 

## 🔗 Links

- [GitHub Repository](https://github.com/HongMing-Huang/dsh-file-upload)
- [Full README](https://github.com/HongMing-Huang/dsh-file-upload#readme)
- [Back to the Plugins list](../plugins.md)
