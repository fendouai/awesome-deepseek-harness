---
title: "Living-Dream-DSH"
description: "DSH 桌面配置框架：8+ MCP 服务器、免费模型渠道（CNB 代理、AMD Radeon Cloud）、Tailscale 手机远程、视觉补丁、一键安装。"
keywords: "Living-Dream-DSH, learning, example, desktop, mcp, automation, deepseek harness, dsh"
---
# Living-Dream-DSH

> ⭐ **2** · ✅ 活跃 · 示例

| | | | |
|---|---|---|---|
| 类型 | 示例 | 分类 | 学习 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [alllllllllli](https://github.com/alllllllllli) | 更新时间 | 2026-08-20 |

## 一句话介绍

> DSH 桌面配置框架：8+ MCP 服务器、免费模型渠道（CNB 代理、AMD Radeon Cloud）、Tailscale 手机远程、视觉补丁、一键安装。

## 详细介绍

**Living Dream DSH — The Ultimate DeepSeek Harness Desktop Configuration** A battle-tested DSH configuration framework with 8+ MCP servers, custom plugins, free model access, mobile remote control, and more. ---

## 📦 安装

```bash
# 1. Clone repository
git clone https://github.com/alllllllllli/Living-Dream-DSH.git
cd Living-Dream-DSH

# 2. Double-click install.bat (launches GUI wizard)
#    Or run in PowerShell: .\install-gui.ps1
```

## 🚀 快速开始

```bash
# ✅ Correct way
dsh plugin --profile web add <package>@<version>

# ❌ Wrong way (will clear unlisted bundles)
cd $env:USERPROFILE\.dsh\profiles\web
pnpm add <package>
```

## 📚 更多信息

**Prerequisites (Must Install First)**

> 💡 After installing Python, run `pip install mcp markitdown zstandard` to enable all MCP servers. > The GUI installer does this automatically. > 💡 The launcher auto-detects DSH Desktop from common install paths. If it fails, set > `$env:DSH_DESKTOP_PATH = "D:\Tools\DeepSeekHarness-Desktop"` (your actual path), > or add it as a system environment variable for persistence.

**Option 1: Offline Install ⭐ Recommended**

> **No internet required during install.** Node.js, Python, Git are bundled in the package. 1. Download [`Living-Dream-DSH-v2.9.0-Offline-Setup.exe`](https://github.com/alllllllllli/Living-Dream-DSH/releases/download/v2.9.0/Living-Dream-DSH-v2.9.0-Offline-Setup.exe) (~122 MB) from Releases 2. Double-click to run — professional Inno Setup wizard launches 3. Follow the wizard: Language → License → C

**1. Install prerequisites (if not installed)**

winget install OpenJS.NodeJS.LTS # Node.js winget install Python.Python.3.13 # Python npm install -g pnpm # pnpm

**3. Copy config files to DSH directory**

Copy-Item configs\cordis.patch.yml.template $env:USERPROFILE\.dsh\profiles\web\cordis.patch.yml Copy-Item configs\package.json.template $env:USERPROFILE\.dsh\profiles\web\package.json Copy-Item configs\settings.yaml.template $env:USERPROFILE\.dsh\settings.yaml Copy-Item configs\AGENTS.md $env:USERPROFILE\.dsh\AGENTS.md Copy-Item configs\.credentials.yaml.template $env:USERPROFILE\.dsh\.credentials

## 🔗 链接

- [GitHub 仓库](https://github.com/alllllllllli/Living-Dream-DSH)
- [完整 README](https://github.com/alllllllllli/Living-Dream-DSH#readme)
- [返回Living-Dream-DSH所在分类](../examples.md)
