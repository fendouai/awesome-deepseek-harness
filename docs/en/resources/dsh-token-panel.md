---
title: "dsh-token-panel"
description: "A corner HUD for DeepSeek Harness that shows your session's token pressure, per-model cost, and daily/monthly usage at a glance — with an editable budget & balance that tracks spending for you. 右下角常驻的 Token 仪表盘：实时查看会话压力、按模型估算花费，预算和余额点一下就能改，每天每月用了多少都有记录。"
keywords: "dsh-token-panel, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-token-panel

> ⭐ **7** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 7 | Status | ✅ active |
| Author | [juhe291](https://github.com/juhe291) | Updated | 2026-08-17 |
| Subcategory | 🖥️ Sidebars & panels | Capabilities | coding |

## One-liner

> A corner HUD for DeepSeek Harness that shows your session's token pressure, per-model cost, and daily/monthly usage at a glance — with an editable budget & balance that tracks spending for you. 右下角常驻的 Token 仪表盘：实时查看会话压力、按模型估算花费，预算和余额点一下就能改，每天每月用了多少都有记录。

## About

**实时 Token 消耗 HUD 插件 —— 为 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 提供右下角常驻的 Token 仪表盘：实时会话压力、会话花费、历史曲线、按日/按月统计，面板跟随当前对话，可拖拽、可设默认位置。** 🌐 **中文** ｜ [**English**](README.en.md)

## 📦 Install

```bash
dsh plugin --profile web add dsh-token-panel@0.4.7
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add github:juhe291/dsh-token-panel
```

## 📚 Learn more

**从 npm 安装（推荐）**

dsh plugin --profile web add dsh-token-panel@0.4.7 npm 包直接使用打包好的 `lib/` 产物，**无需本机构建**。命令里的版本号请写**当前最新版**（发布新版本后同步更新此处，见 [发布新版本](#发布新版本)）。 > ⚠️ **为什么要写精确版本号？** 新发布的版本（不足约 24 小时）会被 DSH 的 supply-chain 年龄校验拦截，`@latest` 可能被 pnpm 解析回较早版本；显式写版本号才能保证装到最新且修好的版本。包龄超过门槛后 `@latest` 才可靠。 > ⚠️ **装到了旧版本？** 若安装后版本不是最新，改用精确版本重装（如上命令），并确认 `npm view dsh-token-panel dist-tags.latest` 显示的是最新版。

**从本地路径安装**

dsh plugin --profile web add C:\path\to\dsh-token-panel 安装完成后 **重启 profile**，刷新浏览器，右下角出现 TOKEN 胶囊。 > ⚠️ **pnpm ≥ 10 拦截 Git 构建脚本**：首次安装若提示 `ERR_PNPM_GIT_DEP_PREPARE_NOT_ALLOWED`，按提示把报错中的 `allowBuilds` 条目加入 profile 目录下的 `pnpm-workspace.yaml`，然后重跑安装命令。这是 pnpm 的安全机制（Git 依赖需要显式允许执行构建脚本），本包已自带 `prepare` 构建脚本与提交好的 `lib/` 产物，允许后即可正常安装。 > ⚠️ **从 GitHub / 本地安装需要 Node ≥ 22.5**：源码安装会执行 `prepare` 构建（pnpm 11.7 

**配置**

配置位于 profile 的 `cordis.patch.yml`（或 `settings.yaml` 的插件分节）： name: dsh-token-panel config: pollInterval: 1500 # 实时轮询间隔 (ms) priceMode: auto # auto = 8/17 前 flat 旧价、之后自动切峰谷；flat / peak-offpeak 固定模式 # 全局兜底价格（模型未在 modelPrices 中列出时使用；默认 = flash 价） pricePerMInput: 1 # 未命中输入价格 (CNY / 百万 token) pricePerMCacheRead: 0.02 # 缓存命中价格 (CNY / 百万 token) pricePerMOutput: 2 # 输出价格 (CNY / 百万 token) # 峰谷价（priceMode 切到

**工作原理**

- 聚合 `ctx.tokenMeter.measure()`（压力/表面积）+ `ctx.sessionProjections.snapshot()`（provider 实测用量/容量/构成）+ `ctx.sessionTitle.get()`（会话标题）+ `ctx.credentials.resolve('DEEPSEEK_API_KEY')`（官网余额） - 注册三条 HTTP 路由：`/plugins/dsh-token-panel/snapshot`（实时 + 按模型价表）、`/plugins/dsh-token-panel/stats`（持久化统计）、`/plugins/dsh-token-panel/balance`（官网余额，5 分钟缓存） - 用量增量按天持久化（崩溃安全：tmp + rename 原子写），并按会话 × 模型分桶累计，供成本分模型计价 - 过滤 0 t

## 🔗 Links

- [GitHub Repository](https://github.com/juhe291/dsh-token-panel)
- [Full README](https://github.com/juhe291/dsh-token-panel#readme)
- [Back to the Plugins list](../plugins.md)
