---
title: "dsh-smooth-stream"
description: "丝滑流式渲染：字跟着模型到达走、换行滑入、不闪，滚动归用户，尊重 prefers-reduced-motion。"
keywords: "dsh-smooth-stream, ui, plugin, deepseek harness, dsh"
---
# dsh-smooth-stream

> ⭐ **45** · ✅ 活跃 · 插件 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 45 | 状态 | ✅ 活跃 |
| 作者 | [Laplace-bit](https://github.com/Laplace-bit) | 更新时间 | 2026-08-20 |
| 子分类 | 💡 生成式界面 | 能力 | ui |

## 一句话介绍

> 丝滑流式渲染：字跟着模型到达走、换行滑入、不闪，滚动归用户，尊重 prefers-reduced-motion。

## 详细介绍

[English](README.en.md) · [项目主页](https://laplace-bit.github.io/dsh-smooth-stream/) · [工作原理与基准](https://laplace-bit.github.io/dsh-smooth-stream/how-it-works.html) · [npm](https://www.npmjs.com/package/dsh-smooth-stream) ---

## ✨ 核心特性

- **如水流般自然铺展**：告别大段文本突然“砸”在屏幕上的视觉压迫，字句如打字机般富有呼吸感地逐字涌现；
- **视线无需追赶跳动**：视口如同搭载了高精度阻尼滑轨，随文字增长平稳匀速推移，彻底终结换行时的突发踢移；
- **呼吸感与实时性的平衡**：慢速输出时从容优雅，高并发爆发时平稳追赶，无论模型吐字多快，画面始终从容自若。

## 📦 安装

```bash
pnpm dsh plugin --profile web add dsh-smooth-stream
```

## 🚀 快速开始

```bash
dsh plugin --profile web add dsh-smooth-stream
```

## 📚 更多信息

**安装与使用**

在 DeepSeek Harness 源码根目录运行： pnpm dsh plugin --profile web add dsh-smooth-stream 如果系统 `PATH` 中已有 `dsh`： dsh plugin --profile web add dsh-smooth-stream 启动界面： pnpm dsh web Host 日志中显示 `[dsh-smooth-stream] plugin loaded!` 即表示已成功加载。 卸载命令：`pnpm dsh plugin --profile web remove dsh-smooth-stream`。 ---

## 🔗 链接

- [GitHub 仓库](https://github.com/Laplace-bit/dsh-smooth-stream)
- [完整 README](https://github.com/Laplace-bit/dsh-smooth-stream#readme)
- [返回dsh-smooth-stream所在分类](../plugins.md)
