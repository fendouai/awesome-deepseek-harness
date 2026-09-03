---
title: "dsh-desktop-pet"
description: "DeepSeek Harness 桌面宠物:鲸鱼实时反应 agent 状态(思考冒泡/工作中工具/出错),API 余额渲染为圆形海平面,点击触发跳跃或 40% 转体跳水,带随机台词。"
keywords: "dsh-desktop-pet, ui, plugin, deepseek harness, dsh"
---
# dsh-desktop-pet

> ⭐ **5** · 🧪 实验性 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 5 | 状态 | 🧪 实验性 |
| 作者 | [FenyxHuang](https://github.com/FenyxHuang) | 更新时间 | — |
| 子分类 | 💡 生成式界面 | 能力 | ui |

## 一句话介绍

> DeepSeek Harness 桌面宠物:鲸鱼实时反应 agent 状态(思考冒泡/工作中工具/出错),API 余额渲染为圆形海平面,点击触发跳跃或 40% 转体跳水,带随机台词。

## 详细介绍

A desktop pet for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness): the official whale mark lives in the shell overlay, floats in a circular sea whose level mirrors your DeepSeek API balance, and reacts to your agent's every move.

## ✨ 核心特性

- **Live agent status** — the whale rests, thinks, works, or cries (`❗`) exactly as your agent does, with a status pill that shows the phase, the current tool, an
- **Balance as sea level** — the circular sea around the whale fills to `balance / balanceScale` (¥100 = full by default), the surface is a scrolling wave with a 
- **Interactive** — click to pet it: a springy jump most of the time, or a rare (40%) charged dive with a 360° spin that lands with a big splash, a high rebound, 
- **Zero runtime dependencies** — the bundle ships prebuilt; all `@deepseek-ai/*` services come from the harness itself, so installing needs no build step and no 

## 📦 安装

```bash
# GitHub direct install (prebuilt artifacts, no build authorization needed)
dsh plugin --profile web add github:FenyxHuang/dsh-desktop-pet

# or from a local checkout
dsh plugin --profile web add link:/path/to/dsh-desktop-pet

# or as a tarball
pnpm pack
dsh plugin --profile web add ./dsh-desktop-pet-0.1.0.tgz
```

## 🚀 快速开始

```bash
- update:
    - id: pet-status
      config:
        balanceScale: 500
        balanceRefetchMs: 60000
```

## 📚 更多信息

**Configuration**

The bundle applies the `cordis.patch.yml` layer, which mounts two rows: The host row reads your DeepSeek API key through the harness's normal credentials (`DEEPSEEK_API_KEY`) and refetches `https://api.deepseek.com/user/balance` at most every 15 seconds. Override any key in your own profile's `cordis.patch.yml`: - id: pet-status config: balanceScale: 500 balanceRefetchMs: 60000

## 🔗 链接

- [GitHub 仓库](https://github.com/FenyxHuang/dsh-desktop-pet)
- [完整 README](https://github.com/FenyxHuang/dsh-desktop-pet#readme)
- [返回dsh-desktop-pet所在分类](../plugins.md)
