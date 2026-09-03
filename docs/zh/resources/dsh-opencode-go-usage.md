---
title: "dsh-opencode-go-usage"
description: "DeepSeek Harness 插件:OpenCode Go 用量与花费悬浮仪表盘(配额、逐请求成本、模型/来源分布)"
keywords: "dsh-opencode-go-usage, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-opencode-go-usage

> ⭐ **13** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 13 | 状态 | ✅ 活跃 |
| 作者 | [Xenia0922](https://github.com/Xenia0922) | 更新时间 | 2026-08-17 |
| 子分类 | 💰 费用与统计 | 能力 | coding |

## 一句话介绍

> DeepSeek Harness 插件:OpenCode Go 用量与花费悬浮仪表盘(配额、逐请求成本、模型/来源分布)

## 详细介绍

一个用于 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 的 DSH 插件。它在桌面右下角提供可拖动、可缩放的悬浮面板，用于查看 OpenCode Go 的账户级用量、配额和 DSH 会话分析。 数据在本机处理。网络请求只发往 `opencode.ai`，以及用于版本检查的 GitHub 公共 `package.json`；不会把 API key、Cookie 或用量数据发送给第三方。

## ✨ 核心特性

- 官方账户级用量：读取官网 `usage.list`，使用官方逐请求费用，支持跨设备数据。凭据通过本地配置提供。
- DSH 会话分析：按 DSH 会话、模型和日期统计 OpenCode Go 用量。
- 配额监控：显示滚动 5 小时、周、月配额、重置时间和消耗速度预测。
- 多 key 配额池：自动发现 `.credentials.yaml` 中的 `OPENCODE_GO_KEY_*`，支持切换和限流状态提示。
- 交互面板：FAB 拖动、标题栏拖动、边缘缩放、最大化、位置和大小持久化。
- 数据分析：按模型排行、费用分项、7/14/30 天趋势、最近会话和 CSV 导出。
- 中英文界面：可手动切换，也可以跟随 DSH 全局语言。
- 跨平台启动：支持 Windows、macOS、Linux 上的 Chromium 系浏览器调试端口。

## 📦 安装

```bash
git clone https://github.com/Xenia0922/dsh-opencode-go-usage.git
dsh plugin --profile my-profile add ./dsh-opencode-go-usage
dsh --profile my-profile
```

## 🚀 快速开始

```bash
~/.config/dsh-opencode-go-usage.json
```

## 📚 更多信息

**首次配置**

安装完成后，右下角会出现 OpenCode Go FAB。官方视图采用一次性手动凭据配置： 1. 在普通浏览器中打开 `opencode.ai` 的 usage 页面并确认已登录。 2. 按 `F12`（或 `Ctrl+Shift+I`）打开开发者工具；进入 **Application/应用 → Storage/存储 → Cookies → https://opencode.ai**。 3. 在 Cookie 列表中找到名称为 `auth` 的行，只复制 **Value/值** 一栏。不要复制 Cookie 名称、`auth=` 前缀、整条 `Cookie:` 请求头，也不要带引号或空格。 4. 回到 usage 页面地址栏，找到形如 `https://opencode.ai/workspace/wrk_123/usage` 的地址，只复制其中的 `wrk_123` 作为 `workspa

**官方视图显示 `NEED_CONFIG`**

这表示本机还没有官方凭据配置。请在普通浏览器中打开 `opencode.ai` 的 usage 页面，复制 `auth` Cookie 和地址栏中的 `workspaceId`，填入官方视图后点击“保存并刷新”。 主流程不会自动探测或启动调试浏览器，因此不会受已有 Edge 进程合并和调试端口失效影响。

## 🔗 链接

- [GitHub 仓库](https://github.com/Xenia0922/dsh-opencode-go-usage)
- [完整 README](https://github.com/Xenia0922/dsh-opencode-go-usage#readme)
- [返回dsh-opencode-go-usage所在分类](../plugins.md)
