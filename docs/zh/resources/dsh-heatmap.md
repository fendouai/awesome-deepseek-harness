---
title: "dsh-heatmap"
description: "DSH Web GUI activity heatmap plugin: GitHub-style commit/token/spend heatmap in the sidebar with per-model cost estimation"
keywords: "dsh-heatmap, search, plugin, coding, git, ui, deepseek harness, dsh"
---
# dsh-heatmap

> ⭐ **4** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [283Gawin](https://github.com/283Gawin) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding, git, ui |

## 一句话介绍

> DSH Web GUI activity heatmap plugin: GitHub-style commit/token/spend heatmap in the sidebar with per-model cost estimation

## 详细介绍

DSH Web GUI 左侧栏活动热力图插件：常驻显示近 90 天的活动热力图，可在 「提交次数 / Token 用量 / 估算花费」三个维度间切换；热力图下方固定一行显示 今日所有会话消耗的 Token 总数、缓存命中率，并按每次调用实际使用的模型 自动计算花费（USD，可配汇率显示 CNY）。

## ✨ 核心特性

- **近 90 天热力图**（固定窗口）：GitHub 贡献图式网格（周一至周日 × 按周
- 维度切换：提交（所有 DSH 工作区 git 仓库，不含 merge）、Token（billed
- **统计块**（参考 Codex 个人资料页形态）：今日 Token 总量、今日缓存命中率
- 常驻侧栏：面板常驻左侧栏**底部**（工作区列表下方），自愈式挂载（React
- 设置卡片：注册在设置页「插件」分区（settings.plugin.item），支持主题
- 数据来源：host 进程经官方 SDK 读取——sessionPersistence 列出全部会话

## 📚 更多信息

**安装**

git clone https://github.com/283Gawin/dsh-heatmap cd dsh-heatmap pnpm install && pnpm build # link 安装需要构建产物（lib/） dsh plugin --profile web add link:$PWD 或从 npm 发布版安装： dsh plugin --profile web add @linxin666/dsh-client-ui-activity-heatmap 重启 dsh web 后，左侧栏即出现热力图面板。 > **设置页暴露**：DSH 宿主对配置客户端可见的 settings namespace 有一个 > 白名单（`dsh-host-apiproxy` 的 `WEB_SETTINGS_NAMESPACES`，官方包内 > hardcode）。新插件必须把它的 names

**配置**

设置页「插件 → 活动热力图」卡片可配置以下字段（等价于插件行 config）： 插件行 config 示例： - insert: - id: ui-activity-heatmap name: '@linxin666/dsh-client-ui-activity-heatmap' config: theme: green usdCnyRate: 7.2 priceOverrides: my-model: inputPerM: 0.5 outputPerM: 2 修改后重启 dsh web 生效。

## 🔗 链接

- [GitHub 仓库](https://github.com/283Gawin/dsh-heatmap)
- [完整 README](https://github.com/283Gawin/dsh-heatmap#readme)
- [返回dsh-heatmap所在分类](../plugins.md)
