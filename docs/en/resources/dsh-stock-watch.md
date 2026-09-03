---
title: "dsh-stock-watch"
description: "A股自选股实时行情盯盘插件 - DeepSeek Harness Web 右上角可折叠弹窗"
keywords: "dsh-stock-watch, search, plugin, coding, deepseek harness, dsh"
---
# dsh-stock-watch

> ⭐ **68** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 68 | Status | ✅ active |
| Author | [Awu12277](https://github.com/Awu12277) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding |

## One-liner

> A股自选股实时行情盯盘插件 - DeepSeek Harness Web 右上角可折叠弹窗

## About

已发布到 npm，一条命令安装到你的 web profile： dsh plugin --profile web add dsh-stock-watch - 本地开发安装：`dsh plugin --profile web add file:D:\projects\github\dsh-stock-watch` - 或直接通过 git：`dsh plugin --profile web add github:Awu12277/dsh-stock-watch` - 安装后**重启 `dsh web` 生效**；卸载：`dsh plugin --profile web remove dsh-stock-watch` 安装完成后，刷新页面，右上角出现「📈 自选股」药丸。

## ✨ Key Features

- **右上角可折叠弹窗**：折叠时显示自选股实时涨跌家数药丸；展开为完整列表，点击任意行进入详情
- **胶囊可拖动**：按住「📈 自选股」药丸可拖到屏幕任意位置，面板随之跟随（右边缘对齐）；展开后按住面板头部也可拖动；位置持久化到 localStorage。**拖到屏幕四边自动吸附**，贴边后胶囊变为**半球**（屏幕边缘显示涨/跌家数，如 `3↑0↓`），点击仍可展开面板
- **多分组自选股**：分组 tab 切换（分组名 + 股票数），配置存浏览器 `localStorage`（首次自动从 `~/.stocking/settings.json` 迁移）
- **A 股 + 港股 + ETF 三市场**：添加股票搜索支持 **A 股（本地全 A 池 5549 只）、港股（本地池 2791 只 + 腾讯 smartbox 补充正股）、ETF（本地池 1650 只场内基金，含沪深300ETF、恒生科技ETF、货币ETF、黄金ETF 等）**；搜索「小米」「01810」→ 港股 
- **实时行情列表**：名称 / 代码、现价、涨跌幅、分时迷你折线、目标价触发标记（买入 / 卖出 / 等待 / -），每 10s 自动刷新（带倒计时）
- **价格变动闪烁**：列表行数据刷新时，若当前价格 ≠ 上次价格，自动红/绿闪烁（涨→红、跌→绿）：**先亮 0.5s 满色、再约 0.5s 渐隐消失**（1s 总时长）；背景通过 `::before` 伪元素独立做 opacity 动画，**文字层全程保持不透明**，仅背景色淡出
- **分时视图**：全天分钟价格线（红涨绿跌）+ 黄色均价线（VWAP）+ 昨收虚线基准，时间轴按 **A 股交易时段（北京时间 09:30–11:30 / 13:00–15:00）** 标注，午间休市留白
- **K 线视图**：日 K / 周 K / 月 K 前复权蜡烛图 + 成交量柱 + **MA 均线（MA5 白 / MA10 黄 / MA20 紫 / MA60 绿，A 股配色，右上角可自定义隐藏/显示，配置存 localStorage）**，支持 **`+ / − / 重置` 按钮缩放 K 线**（位于 MA 均线配

## 📦 Install

```bash
dsh plugin --profile web add dsh-stock-watch
```

## 📚 Learn more

**安装**

已发布到 npm，一条命令安装到你的 web profile： dsh plugin --profile web add dsh-stock-watch 安装完成后，刷新页面，右上角出现「📈 自选股」药丸。

## 🔗 Links

- [GitHub Repository](https://github.com/Awu12277/dsh-stock-watch)
- [Full README](https://github.com/Awu12277/dsh-stock-watch#readme)
- [Back to the Plugins list](../plugins.md)
