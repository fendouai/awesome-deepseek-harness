---
title: "oh-dsh"
description: "One-stop community distribution: TUI, desktop and Web UI in a unified experience with layered installation."
keywords: "oh-dsh, desktop, client, terminal, ui, deepseek harness, dsh"
---
# oh-dsh

> ⭐ **256** · ✅ active · client · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 256 | Status | ✅ active |
| Author | [hust-open-atom-club](https://github.com/hust-open-atom-club) | Updated | 2026-08-21 |

## One-liner

> One-stop community distribution: TUI, desktop and Web UI in a unified experience with layered installation.

## About

🖥️ 三种交互界面 使用同一个 ohdsh 命令启动 Desktop、Web 或 TUI。三端共享会话、凭据、皮肤与插件缓存，同时保留独立 Profile。 🧰 本地开发工作台 内置 Workspace、PTY 终端、浏览器、文件浏览、Side chat 与 Trajectory；面板可以折叠、固定、分屏或全屏展开。 🔍 Git Review 查看工作区改动与 commit diff，在代码行上添加 review comment，并在同一个侧边栏完成分支、提交和推送操作。 🧩 插件市场 Desktop、Web 与 TUI 都能检索、预览和安装插件，并共享同一套交易与恢复状态。目录会标明插件实际生效的界面：安装可能在所有终端都成功，但某些插件只在 Web 或 Desktop 生效、在 TUI 不生效，界面上会明确区分。 🎨 跨端皮肤 @oh-dsh/skins 为 Desktop、Web 与 TUI 提供统一主题，并针对各界面的布局和可读性分别适配。 📦 可拆分发行 按需安装完整版、Web-only 或 TUI-only。每种发行都自带固定版本的 DSH 与 Node runtime，不要求单独安装运行环境。

## 📦 Install

```bash
git submodule update --init --recursive
pnpm install
pnpm run build:dsh
pnpm run build
pnpm run stage:dsh
export PATH="$PWD/bin:$PATH"

ohdsh desktop
ohdsh web
ohdsh tui
```

## 🚀 Quick Start

```bash
make build
make tui ARGS="--lang zh"       # 只暂存并启动 TUI
make web ARGS="--port 3080"     # 只暂存并启动 Web
make desktop                     # 只暂存并启动 Desktop
```

## 📚 Learn more

**首选：命令行安装**

Linux 与 macOS 使用仓库根目录的 `install.sh` 安装最新稳定版。默认安装 TUI，并将 `ohdsh` 注册到 `~/.local/bin`；新开一个终端后即可使用： curl -fsSL \ https://raw.githubusercontent.com/hust-open-atom-club/oh-dsh/main/install.sh \ | bash 需要 Web 或 Desktop 时显式选择发行形态： curl -fsSL \ https://raw.githubusercontent.com/hust-open-atom-club/oh-dsh/main/install.sh \ | bash -s -- --surface web curl -fsSL \ https://raw.githubusercontent.com/hust-open-a

**从 GitHub Release 手动安装**

从 [GitHub Releases](https://github.com/hust-open-atom-club/oh-dsh/releases/latest) 选择需要的发行形态： 安装脚本是推荐入口；Release 资产适合需要手动选择包或离线分发的场景。

**使用**

ohdsh desktop # 启动 Oh-DSH Desktop ohdsh gui # Desktop 的启动别名 ohdsh web # 启动 Oh-DSH Web ohdsh web --port 3080 # 指定 Web 端口 ohdsh tui # 启动 Oh-DSH TUI 三端默认共同使用 `~/.ohdsh` 存放缓存、配置、会话、凭据与插件状态。 设置 `OH_DSH_HOME` 可以统一更换数据目录；运行 `ohdsh web --help` 或 `ohdsh tui --help` 可以查看界面专属选项。 内置的 `@oh-dsh/vision` 为三端提供同一个 `view_image` 工具，让用户对 Workspace 内的本地图片、HTTP(S) 图片或 image data URL 做 OCR、读图与界面诊断。图片复制、 粘贴、缩略图和提交继续由 DSH

## 🔗 Links

- [GitHub Repository](https://github.com/hust-open-atom-club/oh-dsh)
- [Full README](https://github.com/hust-open-atom-club/oh-dsh#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
