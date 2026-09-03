---
title: "deepseek-harness-eac"
description: "DeepSeek Harness (dsh) Windows desktop client - bundled Node.js + dsh CLI, one-click launch, 10 built-in UI skins. EAC: Embracing All Creation 揽尽万象"
keywords: "deepseek-harness-eac, desktop, client, coding, ui, deepseek harness, dsh"
---
# deepseek-harness-eac

> ⭐ **1,067** · ✅ active · client · ⬆️ +56 recently

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 1,067 | Status | ✅ active |
| Author | [zouyuxuan122](https://github.com/zouyuxuan122) | Updated | 2026-08-21 |

## One-liner

> DeepSeek Harness (dsh) Windows desktop client - bundled Node.js + dsh CLI, one-click launch, 10 built-in UI skins. EAC: Embracing All Creation 揽尽万象

## About

- Windows 10/11（x64） - macOS 13+（Apple Silicon / arm64，桌面版） - 无需预装 Node.js 或任何其他运行时

## ✨ Key Features

- [为什么选择 EAC](#为什么选择-eac)
- [快速开始（安装）](#快速开始)
- [功能一览](#功能一览)
- [社区与支持](#社区与支持)
- [开发者文档](#开发者文档)
- [致谢](#致谢)

## 📦 Install

```bash
cd dsh-desktop
npm install
npm run fetch-runtime            # 内置 node.exe + npm CLI
node tauri-shell/stage-resources.mjs   # 装配打包资源（sidecar + dsh-desktop 运行树）
cd tauri-shell
npx -y @tauri-apps/cli@2 build   # release 构建 + NSIS 安装包
node make-portable.mjs           # 便携 zip（可选）→ target/release/portable/

# 开发态（热迭代）：cargo run（Rust 工具链需 RUSTUP_HOME/CARGO_HOME）
```

## 🚀 Quick Start

```bash
cd dsh-desktop
npm install
npm run fetch-runtime
# 打包（Tauri 三段链，产出入 tauri-shell/target/release/）
node ../tauri-shell/stage-resources.mjs     # 装配 staged-resources
cd ../tauri-shell
npx -y @tauri-apps/cli@2 build              # → bundle/nsis/*-setup.exe（含 sidecar 运行树）
node make-portable.mjs                      # → portable/*-portable.zip + SHA256SUMS.txt
```

## 📚 Learn more

**首次使用**

1. 双击运行，显示启动动画，随后自动加载 DeepSeek Harness Web UI（原生窗口，仅本机回环访问）。 2. 如尚未配置 API Key，在界面「设置」内完成配置即可开始使用（与命令行 dsh 完全一致）。 3. 常用入口：设置 → 皮肤（10 款内置皮肤切换）/ 插件市场 / 模型一键选择；对话区 → 终端 / 文件标签页。

## 🔗 Links

- [GitHub Repository](https://github.com/zouyuxuan122/Deepseek-Harness-EAC)
- [Full README](https://github.com/zouyuxuan122/Deepseek-Harness-EAC#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
