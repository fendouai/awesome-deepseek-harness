---
title: "dsh-spend"
description: "Token usage and estimated spend: floating panel with per-model/day/session stats and auto-detected billing plans."
keywords: "dsh-spend, ui, plugin, observability, deepseek harness, dsh"
---
# dsh-spend

> ⭐ **7** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 7 | Status | ✅ active |
| Author | [nonewind](https://github.com/nonewind) | Updated | 2026-08-18 |
| Subcategory | 🖥️ Sidebars & panels | Capabilities | observability, ui |

## One-liner

> Token usage and estimated spend: floating panel with per-model/day/session stats and auto-detected billing plans.

## About

在 dsh Web UI 右下角显示一个**悬浮用量窗口**：实时查看 token 调用量、多维度统计与预计计费金额，**零配置**自动识别计费计划并直读订阅商真实额度/余额。

## ✨ Key Features

- 🖱️ **三级交互**：悬浮胶囊常驻 → hover 摘要预览 → 点击展开四标签页详情面板
- 📊 **多维统计**：按提供商 / 模型 / 小时 / 天 / 会话 / 工作目录 / 最近调用，含性能指标（TTFT、生成速度）
- 📈 **时间序列图表**：今日逐小时、24h/72h/7d 时间曲线、52 周活跃热力图
- 🏷️ **计费计划自动识别**：内置知识库（17 供应商 / 131 模型价格），自动区分订阅制（Code）与按量（Token）
- 🔴 **实时额度 / 余额直读**：9 家订阅商内置适配器（额度 7 + 余额 2），展示厂商接口返回的真实值，失败安全回退不崩溃
- ⚡ **DeepSeek 峰谷计价**：8/17 起按调用时刻自动按高峰/空闲价计费
- 💱 **$ / ¥ 货币切换**：实时汇率（失败回退 `usdCnyRate`，默认 7.2）
- 📂 **工作区筛选**：按项目限定全部统计口径，支持逐级下钻子目录

## 📦 Install

```bash
# 1. 安装到 web profile（pnpm 转发，支持 npm 包 / github:owner/repo / 本地路径）
dsh plugin --profile web add dsh-spend

# 2. 验证已挂载（组合配置中出现 usage-stats 行）
dsh --profile web --dump-config | grep usage-stats

# 3. 重启 dsh web（改动需要重启加载，HMR 对插件不生效）
dsh web
```

## 📚 Learn more

**供应商自动识别（零配置）**

插件内置**供应商知识库**（`lib/knowledge.js`，2026-08-14 官方文档核实）：**17 个供应商 / 131 个模型价格**。provider id 自动归一化别名：`glm`→zhipu、`kimi`→moonshot、`dashscope`→qwen、`gemini`→google、`grok`→xai、`claude`→anthropic、`copilot`→github-copilot、`minimax-cn`→minimax、`deepseek-official`→deepseek 等。日志中出现的提供商**自动匹配**知识库生成计划与价格（UI 标记"自动识别"）；显式 `plans` / `pricing` 配置始终覆盖自动识别。

**安装**

插件包声明了 `dsh.bundle` 清单，`dsh plugin add` 后由 CLI 自动挂载进 profile 层——**无需手动编辑任何配置文件**：

**配置**

`cordis.patch.yml` 中 `usage-stats` 行的 `config`（当前已写入官方价，见「价格来源」）： config: currency: USD # 服务端基准货币（费用按 USD 计算；UI 内可自由切换 $ / ¥ 展示） usdCnyRate: 7.2 # USD→CNY 固定汇率（实时汇率拉取失败时的回退值） liveRate: true # 服务端实时拉取 USD→CNY 汇率（6h 缓存）；false 时始终用固定值 pricing: # 按模型精确匹配的单价（每百万 token） - model: deepseek-v4-flash inputPerMillion: 0.14 outputPerMillion: 0.28 cacheReadPerMillion: 0.0028 cacheWritePerMillion: 0 defaultPric

## 🔗 Links

- [GitHub Repository](https://github.com/nonewind/dsh-spend)
- [Full README](https://github.com/nonewind/dsh-spend#readme)
- [Back to the Plugins list](../plugins.md)
