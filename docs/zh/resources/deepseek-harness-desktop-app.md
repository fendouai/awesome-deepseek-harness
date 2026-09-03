---
title: "deepseek-harness-desktop-app"
description: "DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts."
keywords: "deepseek-harness-desktop-app, desktop, client, coding, search, deepseek harness, dsh"
---
# deepseek-harness-desktop-app

> ⭐ **610** · ✅ 活跃 · 客户端 · 近期 ⬆️ +4

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 610 | 状态 | ✅ 活跃 |
| 作者 | [vibeinging](https://github.com/vibeinging) | 更新时间 | 2026-08-15 |

## 一句话介绍

> DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts.

## 详细介绍

各平台直链与文件大小见[官网下载页](https://dshdesktopstation.com/#download)；首跑常见问题（Gatekeeper、SmartScreen、API Key、国内下载）见[官网 FAQ](https://dshdesktopstation.com/#faq)。

## 📦 安装

```bash
dsh plugin --profile web add @linxin666/dsh-client-ui-skin-center
```

## 🚀 快速开始

```bash
dsh plugin --profile web add -w <package>@<exact-version> --save-exact --ignore-scripts
dsh plugin --profile web remove <package>
```

## 📚 更多信息

**开始使用**

1. 从 [Releases](https://github.com/vibeinging/dsh-desktop/releases/latest) 下载适合的平台安装包。 2. 启动应用，选择一个工作目录或直接创建会话。 3. 在侧栏打开文件、Git 或终端；在输入框添加文件和文件夹。 4. 需要更多能力时，打开“设置 → 插件市场”。 模型凭据由 DSH 设置与本地环境管理。项目不会把 API Key 写入 README、截图或插件清单。

**安装更多插件**

普通用户直接使用“设置 → 插件市场”。插件市场会显示来源、版本、兼容性和权限；安装前仍应查看上游说明，市场可见不等于本项目已经审查或默认内置。 也可以使用官方 CLI 操作同一个 Profile： dsh plugin --profile web add -w <package>@<exact-version> --save-exact --ignore-scripts dsh plugin --profile web remove <package> 符合官方 DSH Bundle 与 `dshClient` 合同的插件，不需要专门为 DSH Desktop 重写。需要窗口、原生文件对话框或 Browser Workspace 的插件，则要显式使用 DSH Desktop 的窄 Host 合同；在其他宿主中缺少这些能力时应直接报告。

## 🔗 链接

- [GitHub 仓库](https://github.com/vibeinging/deepseek-harness-desktop-app)
- [完整 README](https://github.com/vibeinging/deepseek-harness-desktop-app#readme)
- [返回deepseek-harness-desktop-app所在分类](../clients.md)
