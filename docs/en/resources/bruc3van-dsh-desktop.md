---
title: "dsh-desktop (bruc3van)"
description: "Third-party desktop client loading the official Web UI: reuses a running official instance or a bundled dsh runtime."
keywords: "dsh-desktop (bruc3van), desktop, client, deepseek harness, dsh"
---
# dsh-desktop (bruc3van)

> ⭐ **66** · ✅ active · client · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 66 | Status | ✅ active |
| Author | [bruc3van](https://github.com/bruc3van) | Updated | 2026-08-21 |

## One-liner

> Third-party desktop client loading the official Web UI: reuses a running official instance or a bundled dsh runtime.

## About

**一款主打安全且更尊重开发者的第三方 DSH 桌面客户端。官方 Web UI ，长任务常驻托盘，支持通知推送；内置安全市场，600+精选插件支持先审查、再安装。** DSH Desktop 是一个独立的 DeepSeek Harness（`dsh`）Electron 客户端。窗口里呈现的是官方 Web UI 本体——不是仿制版，官方产品什么样，窗口里就是什么样；而真正的工程投入都在窗口之外：关闭窗口任务照跑、托盘常驻随点随开、Agent 跑在经过治理的执行环境里、插件安装走「先审查、再安装」的内置市场、连接与更新链路逐层加固。 发布安装包内置固定版本的官方 `@deepseek-ai/dsh` 运行时；普通用户无需另外安装 Node.js、pnpm 或 `dsh` CLI。桌面外壳、安装包、连接增强与发布签名均由本项目独立负责，不属于官方运行时的一部分。桌面客户端与官方 `dsh` 使用各自独立的版本号；应用的连接设置页会同时显示两个版本号，便于排查兼容问题。

## ✨ Key Features

- **长任务常驻桌面。** 关闭窗口不等于中断任务：应用驻留在托盘 / 菜单栏，Harness 服务继续在后台运行，随点随开；本地服务意外退出有受控重启，系统唤醒或长时间后台导致页面异常时会在确认服务可达后自动恢复。终端窗口和浏览器标签页给不了这层保障。
- **Agent 执行环境经过工程治理。** Agent 本质是在你电脑上执行命令的进程，它的环境值得被认真对待：优先复用你正在跑的实例与 PATH 上的 `dsh`，Agent 跑在你自己的完整 shell 环境里；内置运行时下没装过这些工具的用户也能执行 `node`、`dsh` 和 `pnpm`；`ELECTRON
- **安全是身份，不是特性列表里的一条。** 一个能读写你文件的应用，值得用最保守的方式分发：客户端只用公开的 `dsh web` 接口，不碰官方仓库内部；窗口开沙箱、关 Node 集成、导航锁在官方源站；打包后更新源与数据目录禁止被环境变量劫持；应用内更新下载后先校验 SHA-256 再安装；本机可信 Web UI 放
- **安全市场：先审查、再安装。** 随安装包发布的内置市场默认关闭、开启后才联网；市场目录来自数据来源仓库的每日自动采集 + 人工精选，「安全安装」不替你执行任何命令，而是把审查提示词交给 Agent 先读代码、确认干净后再用官方命令安装。详见[内置安全市场](#内置安全市场)。
- **官方发版，当天就能用上。** 窗口加载的是官方 Web UI 本体，不是仿制版。官方界面加功能、改交互，官方文档、教程和快捷键全部对得上，不会出现「教程里有的界面你找不到」；官方一发版，你升级自己已有的 dsh（或等应用内更新推送内置运行时），桌面端零改动、零等待。
- **双击就能用，不用懂命令行。** 安装包自带官方运行时，不需要安装 Node.js、pnpm，也不需要敲任何命令；首次启动填一个 API Key 就能开始对话。对小白用户来说这就是全部；懂命令行的话，智能模式、固定地址这些进阶玩法也都在手边。

## 📦 Install

```bash
git clone https://github.com/bruc3van/dsh-desktop.git
cd dsh-desktop
pnpm install
pnpm run dev
```

## 🚀 Quick Start

```bash
xattr -dr com.apple.quarantine "/Applications/DSH Desktop.app"
```

## 📚 Learn more

**为什么值得使用**

先说清楚我们为什么这样做。Harness 的使用形态正在从「对话」变成「委派长任务」，而长任务的痛点全在窗口之外：任务跑着的时候不敢关标签页、关掉终端服务就停、Agent 的执行环境里找不到 `node` 和你 shell 里配好的工具、一个有文件读写权限的进程更新链路却裸奔。界面本身反而是最不需要重做的部分——官方 Web UI 一直在快速演进，用户要的正是它原封不动。 因此本项目把界面完整交还给官方，**把全部工程投入放在窗口之外：常驻与长任务、Agent 执行环境、内置安全市场、安全加固、连接与更新。** 这样做的好处是天然成立的： 这些落到产品上：

**下载安装**

从 [GitHub Releases](https://github.com/bruc3van/dsh-desktop/releases) 下载适合当前系统的安装包并启动即可。发布版内置官方 `dsh` 运行时，不依赖开发环境，也不会在首次启动时执行 npm 安装。 当前安装包尚未经过正式的开发者签名认证，首次打开时系统可能会弹出提示，按下方说明操作一次即可正常使用。

## 🔗 Links

- [GitHub Repository](https://github.com/bruc3van/dsh-desktop)
- [Full README](https://github.com/bruc3van/dsh-desktop#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
