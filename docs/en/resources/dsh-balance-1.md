---
title: "dsh-balance"
description: "dsh余额插件. A DeepSeek Harness plugin for real-time token tracking and highly accurate session cost estimation, featuring dynamic peak/off-peak pricing support."
keywords: "dsh-balance, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-balance

> ⭐ **11** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 11 | Status | ✅ active |
| Author | [TwotwoPiggy](https://github.com/TwotwoPiggy) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> dsh余额插件. A DeepSeek Harness plugin for real-time token tracking and highly accurate session cost estimation, featuring dynamic peak/off-peak pricing support.

## About

DeepSeek 余额实时显示插件: 在 dsh Web UI 输入框**下方、命中率/输入输出 token 统计条所在的同一行**, 实时显示: - **账户余额与充足度状态指示灯**(如 `🟢 余额 ¥97.69`, 红/黄/绿三色直观反映余额充裕状况，**点击状态圆点可直接手动强刷查询最新余额**) - **本次对话的估算消耗**(如 `本会话约 ¥3.92`, 按模型、按 DeepSeek 官方单价估算) - **`?` 定价参考图标**: 悬停以 `?` 为中心优雅浮现 **DeepSeek V4 系列专属定价微卡片**（支持 `deepseek-v4-flash` 与 `deepseek-v4-pro`），点击直达官方定价页 悬停读数可查看**左右双栏毛玻璃卡片**： - **左栏【📊 账户余额】**：实时大字总额、充足度 Badge、充值与赠送金额构成、5分钟自动刷新时间戳点击指示灯强刷指引以及偏好设置快速入口。 - **右栏【⚡ 本会话消耗】**：当前会话预估总花费、按模型细分明细（如 `• deepseek-v4-flash: ¥3.92`）、换行小字体展示输入/输出与缓存命中统计（如第一行 `Token: 输入 124M · 输出 301K` 与第二行 `命中: 123M (99.3%)`）。 - **时间感知引擎**：内置 DeepSeek 谷峰计费自动切换机制（北京时间周一至周五 09:00~12:00, 14:00~18:00 为峰时 100% 计费 / 其余时段含周末全天享 5 折空闲特惠），全自动无缝同步。

## ✨ Key Features

- **账户余额与充足度状态指示灯**(如 `🟢 余额 ¥97.69`, 红/黄/绿三色直观反映余额充裕状况，**点击状态圆点可直接手动强刷查询最新余额**)
- **本次对话的估算消耗**(如 `本会话约 ¥3.92`, 按模型、按 DeepSeek 官方单价估算)
- **`?` 定价参考图标**: 悬停以 `?` 为中心优雅浮现 **DeepSeek V4 系列专属定价微卡片**（支持 `deepseek-v4-flash` 与 `deepseek-v4-pro`），点击直达官方定价页 <https://api-docs.deepseek.com/zh-cn/quick_start
- **左栏【📊 账户余额】**：实时大字总额、充足度 Badge、充值与赠送金额构成、5分钟自动刷新时间戳点击指示灯强刷指引以及偏好设置快速入口。
- **右栏【⚡ 本会话消耗】**：当前会话预估总花费、按模型细分明细（如 `• deepseek-v4-flash: ¥3.92`）、换行小字体展示输入/输出与缓存命中统计（如第一行 `Token: 输入 124M · 输出 301K` 与第二行 `命中: 123M (99.3%)`）。
- **时间感知引擎**：内置 DeepSeek 谷峰计费自动切换机制（北京时间周一至周五 09:00~12:00, 14:00~18:00 为峰时 100% 计费 / 其余时段含周末全天享 5 折空闲特惠），全自动无缝同步。

## 📦 Install

```bash
# 完整版（默认）：包含可视化设置面板、定价参考浮层等丰富功能
dsh plugin --profile web add dsh-balance

# 精简版（可选）：纯余额与会话消耗显示，去除所有弹窗与设置界面（体积仅为 1/3）
dsh plugin --profile web add dsh-balance-lite
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add <本目录绝对路径>
```

## 📚 Learn more

**方式二：让 AI 助手帮您安装**

如果您正在使用 Antigravity 等 AI 助手，直接复制以下提示词发给它： > 请帮我在当前环境中安装 `dsh-balance` 插件，将其配置写入到我的 `cordis.yml` 中并启用它。

**⚙️ 可视化设置面板说明**

在 Web 界面输入框底部的统计条最右侧，点击 **⚙️ 齿轮图标**（或在悬停卡片底部点击 **⚙️ 打开偏好设置**），即可呼出可视化配置弹窗： > **提示**：在设置弹窗中点击「**保存并生效**」，修改将立即应用到当前服务与页面，无需手动重启 `dsh web`！

**📋 提示词 1：全新安装与默认启用**

> 请帮我在当前 DeepSeek Harness 环境中安装 `dsh-balance` 插件，将其默认配置写入到我的 `cordis.patch.yml` 中并确保已启用。

**📋 提示词 4：配置独立的 Dev 测试环境与端口隔离**

> 请帮我初始化一个 DSH `dev` Profile，将本地 `dsh-balance` 插件链接进去，并将 Web 端口固定为 `3081`，以便于我和日常使用的 3080 端口环境并行测试。 ---

## 🔗 Links

- [GitHub Repository](https://github.com/TwotwoPiggy/dsh-balance)
- [Full README](https://github.com/TwotwoPiggy/dsh-balance#readme)
- [Back to the Plugins list](../plugins.md)
