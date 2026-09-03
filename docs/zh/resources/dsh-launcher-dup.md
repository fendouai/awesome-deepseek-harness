---
title: "dsh-launcher"
description: "轻量 Windows 启动器：登录静默自启 + 极简 WebView2 窗口。"
keywords: "dsh-launcher, desktop, client, deepseek harness, dsh"
---
# dsh-launcher

> ⭐ **165** · ✅ 活跃 · 客户端 · 近期 ⬆️ +4

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 165 | 状态 | ✅ 活跃 |
| 作者 | [Ruler4396](https://github.com/Ruler4396) | 更新时间 | 2026-08-20 |

## 一句话介绍

> 轻量 Windows 启动器：登录静默自启 + 极简 WebView2 窗口。

## 详细介绍

一个 Windows 原生壳：双击启动 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（`dsh`）、可设置开机自启，高度重视服务生命周期与出错诊断。安装包大小仅为 **~1.4MB**，不内置 dsh；缺失的依赖（Node.js 等）按需补齐，不改动系统环境。 **克制**：本项目意在打造一个舒适的 dsh 原版体验，不添加文件面板、内置终端等额外功能，一切交给dsh的插件，由用户自行决定。仅在推出安全性更新和dsh版本更新时弹出系统通知。

## ✨ 核心特性

- 开机自启 · 独立小窗口（WebView2）· 自动拉起服务并等待就绪
- 出错弹窗带错误码，统一日志 `~/.dsh\dsh-launcher\dsh.log`
- `DshWeb.exe --diagnose` 一键导出信息脱敏诊断包
- 服务生命周期：跟随窗口 / 常驻 / 托盘驻留（见下"插件"）
- 主题跟随 · 窗口位置记忆 · dsh 延迟更新（不打断会话）

## 📦 安装

```bash
dsh plugin --profile web add dsh-launcher-lifetime
```

## 📚 更多信息

**安装**

**MSI（推荐新手）**：从 [Releases](https://github.com/Ruler4396/dsh-launcher/releases) 下载 `dsh-launcher-<版本>.msi`，双击安装（向导里可勾选开机自启）。卸载：设置 → 应用 → dsh-launcher。 **便携版 ZIP**：下载 `dsh-launcher-windows-<版本>.zip`，解压后双击 `DshWeb.exe`；删文件夹即卸载。 > 双击没反应？先运行解压目录里的 `check-prereq.cmd`，它会检测 .NET / WebView2 / Node 并给出缺失项的安装命令。

## 🔗 链接

- [GitHub 仓库](https://github.com/Ruler4396/dsh-launcher)
- [完整 README](https://github.com/Ruler4396/dsh-launcher#readme)
- [返回dsh-launcher所在分类](../clients.md)
