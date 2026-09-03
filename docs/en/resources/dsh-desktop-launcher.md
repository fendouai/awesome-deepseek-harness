---
title: "dsh-desktop-launcher"
description: "一个轻量的 dsh（DeepSeek Harness）插件：安装桌面双击启动器 —— macOS 上是带官方鲸鱼图标的 dsh.app，Linux 上是 .desktop 入口。零依赖，约 147 KB。（终端命令在独立的 dsh-launcher 包）"
keywords: "dsh-desktop-launcher, desktop, client, coding, deepseek harness, dsh"
---
# dsh-desktop-launcher

> ⭐ **1** · ✅ active · client

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [LvienOeria](https://github.com/LvienOeria) | Updated | — |

## One-liner

> 一个轻量的 dsh（DeepSeek Harness）插件：安装桌面双击启动器 —— macOS 上是带官方鲸鱼图标的 dsh.app，Linux 上是 .desktop 入口。零依赖，约 147 KB。（终端命令在独立的 dsh-launcher 包）

## About

Windows 与 macOS 的桌面启动器 for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)：**双击桌面图标 → 自动启动服务 → 弹出 Chrome 独立应用窗口**，全程没有任何命令行黑窗，关掉窗口即自动停服，再次双击无缝续聊。

## ✨ Key Features

- 🖱 **一键启动**：双击桌面图标，自动完成「启动服务 → 等待就绪 → 打开应用窗口」三步
- 🪟 **零黑窗**：对 Windows Terminal / 服务窗口做了无窗口化处理，只出现浏览器窗口
- 🔁 **断点续聊**：会话保存在本机，重启服务后对话无缝继续
- 🧹 **关窗即停**：关闭应用窗口自动结束后台服务，不留残留进程（应用窗口使用独立的浏览器配置目录，即使你平时开着 Chrome 也不受影响）
- 🔒 **防重复启动**：服务启动过程中再双击不会重复拉起第二个服务，新实例会等待复用
- 🛡️ **端口自适应**：首选端口被系统保留（Hyper-V/WSL2 排除端口段）或被占用时，自动换用备用端口，无需手动干预
- 🩺 **友好报错**：缺 Node.js / 启动失败都会弹窗提示，日志写 `%TEMP%\DSH-Server.log`
- 🌐 **双浏览器**：优先 Chrome，没有自动回退 Edge

## 📦 Install

```bash
brew tap becomeless/dsh-desktop-launcher
brew install --cask dsh-desktop-launcher
```

## 🚀 Quick Start

```bash
curl -fsSL https://cdn.jsdelivr.net/gh/becomeless/dsh-desktop-launcher@main/install-macos.sh | bash
```

## 📚 Learn more

**🚀 一键安装**

**PowerShell（推荐）：** [Net.ServicePointManager]::SecurityProtocol='Tls12'; iex ([System.Text.Encoding]::UTF8.GetString((New-Object Net.WebClient).DownloadData('https://cdn.jsdelivr.net/gh/becomeless/dsh-desktop-launcher@main/install.ps1')).TrimStart([char]0xFEFF)) **CMD：** powershell -NoProfile -ExecutionPolicy Bypass -Command "[Net.ServicePointManager]::SecurityProtocol='Tls12'; iex ([System.Text.E

**⚙️ 配置项**

编辑 `%LOCALAPPDATA%\DeepSeek-Harness-Launcher\DSH-Launcher.ps1` 顶部配置区： > macOS 版同理：编辑 `.app` 内的 `Contents/MacOS/launcher`，顶部有 `PORT`、`PORT_FALLBACK`、`TIMEOUT` 等配置。

**❓ FAQ**

**双击没反应？** 看任务栏/通知，或查看日志 `C:\Users\<你>\AppData\Local\Temp\DSH-Server.log`（上一次运行的日志保留为 `DSH-Server.log.old`）。 **启动报错弹窗？** 弹窗里会带日志尾部内容；常见原因：没装 Node、网络问题、端口被占用（端口问题新版会自动换备用端口）。 **第一次打开很慢？** 启动器每次启动都会通过 npx 检查并拉取最新版 dsh（官方目前几乎每天发版），命中新版时会重新下载全部依赖，慢属正常现象。想固定版本，可把 `DSH-Server.ps1` 里的 `npx --yes @deepseek-ai/dsh web` 改成带版本号的形式（如 `@deepseek-ai/dsh@0.1.0-rc.7`）。 **应用窗口和我日常的 Chrome 是同一个吗？** 不是：应用窗口使用安装目录下的独

## 🔗 Links

- [GitHub Repository](https://github.com/LvienOeria/dsh-desktop-launcher)
- [Full README](https://github.com/LvienOeria/dsh-desktop-launcher#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
