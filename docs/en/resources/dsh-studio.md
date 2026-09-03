---
title: "dsh-studio"
description: "DeepSeek Harness 原生桌面端 · Linux / macOS / Windows · Rust + Tauri"
keywords: "dsh-studio, desktop, client, coding, deepseek harness, dsh"
---
# dsh-studio

> ⭐ **20** · ✅ active · client

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 20 | Status | ✅ active |
| Author | [Moresyl](https://github.com/Moresyl) | Updated | — |

## One-liner

> DeepSeek Harness 原生桌面端 · Linux / macOS / Windows · Rust + Tauri

## About

**A native desktop shell for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness).** Rust + Tauri 2. It supervises the local `dsh` service, reclaims every process it spawns, and never forks the upstream project to do it. Under 4 MB per installer · [all artifacts and checksums](#install) · [简体中文](README.zh-CN.md) **One click from a registry listing to a layer in the harness's profile** — read the manifest, install through the harness's own plugin command, switch it off again without uninstalling it. ---

## 📦 Install

```bash
pnpm install
pnpm tauri dev      # run it
pnpm bundle:local   # produce unsigned installers for local verification
# The release workflow prepares src-tauri/runtime-cache/offline and merges
# src-tauri/tauri.full.conf.json to produce the Full / Offline edition.
```

## 🚀 Quick Start

```bash
pnpm lint                                          # ESLint, zero warnings
pnpm exec tsc --noEmit                             # strict TypeScript
pnpm test                                          # store and i18n behaviour
cargo test --manifest-path src-tauri/Cargo.toml --workspace
```

## 📚 Learn more

**Install**

Grab an installer from [Releases]. Every tagged version is built by CI for five targets: The Universal macOS image is the lightweight edition. Full / Offline images stay architecture-specific because their embedded Node runtime is native code. Or through a package manager. The manifests all live in [`packaging/`](packaging) and are generated from a real release, so the version and the SHA-256 in t

**FAQ**

Detailed guides: [User guide](docs/user-guide.md) · [Troubleshooting](docs/troubleshooting.md) · [Architecture](docs/architecture.md) · [Plugin and catalog development](docs/plugin-development.md) · [Plugin interoperability contract](docs/plugin-interoperability.md) · [Protocol 3 SDK](sdk/README.md) · [Current roadmap](docs/ROADMAP.md). **Does this replace the harness UI?** No. The harness is load

## 🔗 Links

- [GitHub Repository](https://github.com/Moresyl/dsh-studio)
- [Full README](https://github.com/Moresyl/dsh-studio#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
