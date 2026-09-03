---
title: "dsh-trace-compare"
description: "Trace Compare & Live Maze for DeepSeek Harness: visualize agent exploration (main path, detours, backtracks) from session logs or live sessions"
keywords: "dsh-trace-compare, vision, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-trace-compare

> ⭐ **41** · ✅ 活跃 · 插件 · 近期 ⬆️ +7

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 41 | 状态 | ✅ 活跃 |
| 作者 | [lamost423](https://github.com/lamost423) | 更新时间 | 2026-08-21 |
| 子分类 | 👁️ 视觉工具 | 能力 | coding, multi-agent |

## 一句话介绍

> Trace Compare & Live Maze for DeepSeek Harness: visualize agent exploration (main path, detours, backtracks) from session logs or live sessions

## 详细介绍

还被收录于：[fendouai/awesome-deepseek-harness](https://github.com/fendouai/awesome-deepseek-harness)（独立介绍页）· [Zhiyuan-Fan/Awesome-DeepSeek-Harness-Plugins](https://github.com/Zhiyuan-Fan/Awesome-DeepSeek-Harness-Plugins) · [ZeroPointRepo/awesome-dsh-plugins](https://github.com/ZeroPointRepo/awesome-dsh-plugins) · [cccakeee/awesome-dsh-plugins](https://github.com/cccakeee/awesome-dsh-plugins) [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 的**执行迷宫**：把 Agent 真实的干活过程完整画出来、并分析给你看。 - **迷宫**——主干路径、失败支路、折返点落在同一根时间轴上；空闲自动折叠、密集段自动聚合成「×N」徽标（点击放大、标签逐级补齐）、进度条自带失败热力，8 小时的会话照样字字可辨： - **数据轨道**——每一步的工具调用密度、Token 脉冲（缓存背景 + 未缓存输入/推理/输出增量柱）、上下文压力曲线（70%/90% 阈值线、压缩事件「⌄−N%」标注，悬停看压缩前后真值）： - **执行分析**——失败恢复链（原样重试 / 换参数 / 换工具 / 未恢复）、工具结果矩阵、耗时分位散点。**每个结论一键点回原始命令与返回内容**： - **多会话对比**——同一任务在不同模型上的 2~5 次跑

## ✨ 核心特性

- **迷宫**——主干路径、失败支路、折返点落在同一根时间轴上；空闲自动折叠、密集段自动聚合成「×N」徽标（点击放大、标签逐级补齐）、进度条自带失败热力，8 小时的会话照样字字可辨：
- **数据轨道**——每一步的工具调用密度、Token 脉冲（缓存背景 + 未缓存输入/推理/输出增量柱）、上下文压力曲线（70%/90% 阈值线、压缩事件「⌄−N%」标注，悬停看压缩前后真值）：
- **执行分析**——失败恢复链（原样重试 / 换参数 / 换工具 / 未恢复）、工具结果矩阵、耗时分位散点。**每个结论一键点回原始命令与返回内容**：
- **多会话对比**——同一任务在不同模型上的 2~5 次跑同轴对比：轮次对齐、手动锚点、支路盘点。
- **回放**——最高 300× 重放整场执行，看它是怎么一步步走到结果的：

## 📦 安装

```bash
npm install --global @deepseek-ai/dsh@next
dsh plugin --profile web add dsh-maze
dsh web
```

## 🚀 快速开始

```bash
git clone https://github.com/lamost423/dsh-maze.git
cd dsh-maze
corepack enable && pnpm install && pnpm build
dsh plugin --profile web add .
dsh web
```

## 📚 更多信息

**安装**

**先看你的宿主是哪来的。** 宿主 `0.1.2` 把客户端包重新拆分了一次（`dsh-client-runtime` 拆成 `dsh-client-store` 等），同时换掉了会话快照的数据模型，所以两条线的插件不通用： 宿主 `0.1.2-rc.1` 与拆分出的客户端包已发到 npm（`next` 标签），所以从 v2.0.0 起 `latest` 归 `2.x`；还在老宿主上的人钉住 `1.1.0` 即可。等宿主的 `latest` 也切到 `0.1.2`，这张表就并成一行。 兼容性：`2.0.0` 对着 npm 的 `0.1.2-rc.1` 全家桶构建，类型检查与 49 个测试全绿；实机验收在 `2.0.0-alpha.2` × 上游 master `0.1.2-alpha.1` 上做过——从 npm 装包、真会话跑通、界面数字与宿主自己的统计逐项对账。`1.1.x` 已对官方

## 🔗 链接

- [GitHub 仓库](https://github.com/lamost423/dsh-trace-compare)
- [完整 README](https://github.com/lamost423/dsh-trace-compare#readme)
- [返回dsh-trace-compare所在分类](../plugins.md)
