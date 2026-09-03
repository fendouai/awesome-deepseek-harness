---
title: "dsh-files"
description: "DeepSeek Harness dual-face plugin: session-isolated file upload with colorful composer cards + read_document tool (text/PDF/DOCX/XLSX) with content sniffing and LRU caching"
keywords: "dsh-files, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-files

> ⭐ **28** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 28 | Status | ✅ active |
| Author | [taxueseek](https://github.com/taxueseek) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> DeepSeek Harness dual-face plugin: session-isolated file upload with colorful composer cards + read_document tool (text/PDF/DOCX/XLSX) with content sniffing and LRU caching

## About

One package, one line of cordis config. A composer paperclip for uploads, a document-reading tool for the model, and native image support that hands JPEG/PNG/WebP/GIF to any vision-capable model. DeepSeek Harness dual-face plugin. Three capabilities: - **Upload** — paperclip button, folder button, and drag-and-drop anywhere; `@` file candidates; local session-isolated storage with TTL sweep and sha256 dedup. Files are written under `/.dsh-filess//` so the agent's fs backend can always resolve them. - **Native images** — JPEG/PNG/WebP/GIF uploads are handed to the harness core attachment pipeline (`ctx.attachments` → base64 `image_url`), so any model that declares an `image` input modality actually sees the picture, rendered through the stock native image rail. - **Document reading** — the 

## ✨ Key Features

- **Upload** — paperclip button, folder button, and drag-and-drop anywhere; `@` file candidates; local session-isolated storage with TTL sweep and sha256 dedup. F
- **Native images** — JPEG/PNG/WebP/GIF uploads are handed to the harness core attachment pipeline (`ctx.attachments` → base64 `image_url`), so any model that dec
- **Document reading** — the `read_document` tool reads text / PDF / DOCX / XLSX with content sniffing, encoding fallback, paged reads, per-sheet XLSX access, an 

## 📦 Install

```bash
dsh plugin --profile web add git+https://github.com/taxueseek/dsh-files.git
# restart dsh web
```

## 🚀 Quick Start

```bash
pnpm install
pnpm test          # upload / parse / cache regression
pnpm build         # esbuild client bundle
npx tsc --noEmit   # type check
```

## 📚 Learn more

**Install**

Script install (checks dsh/pnpm, then installs via the git channel): curl -fsSL https://raw.githubusercontent.com/taxueseek/dsh-files/main/install.sh | sh

**Configuration**

name: 'dsh-files' config: maxFileBytes: 25165824 # per-document read byte cap readLimit: 800 # default lines per call (cheap pagination) sheetRowLimit: 200 # rows kept per worksheet maxSheets: 5 # sheets read per workbook cacheEntries: 16 # parse-cache entry count cacheMaxBytes: 67108864 # parse-cache byte budget maxOutputChars: 24000 # per-call window budget (text full; xlsx 3/4; pdf/docx 1/2; tr

## 🔗 Links

- [GitHub Repository](https://github.com/taxueseek/dsh-files)
- [Full README](https://github.com/taxueseek/dsh-files#readme)
- [Back to the Plugins list](../plugins.md)
