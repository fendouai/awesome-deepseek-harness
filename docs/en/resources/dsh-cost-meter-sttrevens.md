---
title: "dsh-cost-meter"
description: "DeepSeek Harness 会话费用统计插件:本会话费用、当日费用、历史记录与官方价格同步"
keywords: "dsh-cost-meter, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-cost-meter

> ⭐ **139** · ✅ active · plugin · ⬆️ +9 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 139 | Status | ✅ active |
| Author | [Han-1413141](https://github.com/Han-1413141) | Updated | 2026-08-21 |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> DeepSeek Harness 会话费用统计插件:本会话费用、当日费用、历史记录与官方价格同步

## About

**DeepSeek Harness 会话费用统计插件(界面中英双语)** 本会话费用 · 当日费用 · OpenCode Go 订阅额度显示 · 预算与已用百分比 · 官方账户余额 · 自定义 Provider 余额查询(可配任意 HTTP 端点) · 余额三段进度条 · 历史记录 · 峰谷计价时段显示(UTC 01:00–04:00、06:00–10:00 为峰时段;2026-08-23 起周末全天按谷价,显示「周末时段——全谷价」) · 峰/谷切换前弹窗与系统通知提醒(位置/提前量/提醒类型可配) · 官方价格一键同步 · 类 Codex Token 用量热图 · 多厂商多模型价格计费(内置 90+ 模型价格目录与自动匹配) · 主流 Coding Plan 额度查询与显示(Anthropic / Z.ai / MiniMax / Kimi / OpenRouter / SiliconFlow / CommandCode / SCNet / 火山方舟 九家,含 Volcano Ark AK/SK 签名) · Plan/API 双轨计费(订阅额度与按量金额分离统计,每 1% 额度与满窗的 token/等值金额估算及日/周/月曲线) · 输入框上方额度横条(预算/Go/Coding Plan 用量一条横排显示,可开关) [English](README.en.md) | **中文** ---

## ✨ Key Features

- `{{NEWAPI_API_KEY}}` 从 DSH 凭据库或环境变量解析(**仅请求头支持占位符**,URL 需写死完整地址);
- 无限额度 token(`unlimited_quota: true`)没有 `total_available`,无法提取 `remaining`,查询会报「remaining is missing or not numeric」——请改用有限额度 token,或在中间层端点换算;
- 配置入口:设置 → 费用(额度标签)→「自定义 Provider 余额」展开配置;或直接改 `storages/cost-meter/ledger.json` 的 `config.customBalance`。

## 📦 Install

```bash
dsh plugin --profile web add dsh-cost-meter
```

## 🚀 Quick Start

```bash
irm https://raw.githubusercontent.com/Han-1413141/dsh-cost-meter/v1.7.12/install.ps1 | iex
```

## 📚 Learn more

**自定义 Provider 余额配置示例(NewApi 模板)**

自定义 Provider 余额的 `extract` 规则支持四种形式:数字常量、点路径字符串、`add`/`subtract` 多路径加减、`divide` 按 `by` 除数缩放。**`divide` 适用于 NewApi 等以 quota 整数计量的端点**(1 USD = 500000 quota,与 cc-switch 同款换算)。 以 NewApi 的 `GET /api/usage/token` 为例(响应 `{ "code": 200, "data": { "total_granted": ..., "total_used": ..., "total_available": ..., "unlimited_quota": false } }`): { "enabled": true, "display": "both", "refreshMinutes": 15, "lab

**安装**

> 需求:Node.js ≥ 20 + DeepSeek Harness(带 `dsh plugin` 命令的版本,`npm install -g @deepseek-ai/dsh`)。

**一键安装(推荐)**

**npm 包名安装**(已发布到 npm registry,始终跟随最新版本;无需 git): dsh plugin --profile web add dsh-cost-meter **PowerShell 一键脚本**(复制整行粘贴回车;自动补齐 pnpm、自动探测 git,无需克隆仓库;安装链**固定到发布 tag `v1.7.12`**,建议先下载审阅再运行): irm https://raw.githubusercontent.com/Han-1413141/dsh-cost-meter/v1.7.12/install.ps1 | iex **或直接命令行**(机器上需已有 pnpm 与 git;同样固定到 tag): dsh plugin --profile web add github:Han-1413141/dsh-cost-meter#v1.7.12 没有 git 时可

**安装排障:ERR_PNPM_MINIMUM_RELEASE_AGE_VIOLATION**

症状:`dsh plugin --profile web add` 阶段安装失败,pnpm 报 `[ERR_PNPM_MINIMUM_RELEASE_AGE_VIOLATION] N lockfile entries failed verification`。 原因:你的环境(pnpm 配置或上层安装器自带策略)启用了「最小发布年龄」供应链保护——lockfile 中**发布时间距今小于阈值**的包一律拒绝。插件引入依赖精确锁版之前的历史版本,生产依赖是浮动区间,首次安装会解析到当时最新发布版(实测 `^0.1.0-rc.6` 漂到仅发布一周左右的 rc.8),在该策略下即被拒绝。 处理: 1. **升级到含依赖精确锁版的版本**:三个运行时依赖(`@deepseek-ai/dsh-credentials`、`@deepseek-ai/dsh-home-paths`、`zod`)已全部精确

## 🔗 Links

- [GitHub Repository](https://github.com/Han-1413141/dsh-cost-meter)
- [Full README](https://github.com/Han-1413141/dsh-cost-meter#readme)
- [Back to the Plugins list](../plugins.md)
