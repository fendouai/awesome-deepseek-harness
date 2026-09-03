---
title: "dsh-auto-chess"
description: "DSH Web里的自走棋插件：人机对战或双AI对弈"
keywords: "dsh-auto-chess, search, plugin, coding, deepseek harness, dsh"
---
# dsh-auto-chess

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [omdsh-dev](https://github.com/omdsh-dev) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding |

## 一句话介绍

> DSH Web里的自走棋插件：人机对战或双AI对弈

## 详细介绍

[English](README.en.md) · **中文** 在 DSH 的会话标签栏里，藏着一张自走棋棋桌：你可以亲自执蓝方，跟 AI 来一场人机对弈；也可以退到观众席，看两个 AI 各自挑好模型，在棋盘上互相对攻。这里的每一步都不是白想的：每个回合的决策，都是一次真实的模型请求。把思考档位拉到 High 或 Max，再点开思考记录，就能围观 AI 盘算「买谁、卖谁、凑什么羁绊、金币花在升级还是刷新」，把算盘一步步打给你看。胜负落在棋盘上，思路留在记录里。 棋局状态保存在浏览器端的模块级 store 中，切标签页、切会话都不会重置对局或打断正在进行的 AI 思考。

## ✨ 核心特性

- **人机与双 AI 对局**：支持人机对战（你执蓝方）、双 AI 对战（旁观）两种模式。
- **模型可分别选择**：蓝方、红方各自从模型目录（项目自带适配器 + 用户已配置的 provider/model）中选择 AI；每侧独立设置，蓝方的 AI 设置与思考记录在界面左侧，红方的在右侧。
- **思考档位可调**：Off / High / Max 三档，蓝方、红方分别设置，控制各侧 AI 决策前的思考强度；模型不支持所选档位时自动回落其默认档位。
- **超时与 token 上限固定**：单次 AI 决策的最长等待时间（默认 300000ms）与输出 token 上限（默认 32000）由部署配置决定，界面不再提供修改入口，客户端随每次请求发送固定值。
- **提示词可分别编辑**：默认系统提示词包含完整规则、严格返回格式与一个正确案例；蓝方、红方可在各自设置区分别编辑本侧提示词，也可一键恢复默认。
- **思考过程展示**：每次 AI 决策后可在界面左右两侧的「思考记录」面板中查看该次决策的完整推理文本（蓝方在左、红方在右）；每条记录默认缩略，点击展开详情。
- **失败可重试**：AI 连续多次给出非法操作时会提示原因并显示「重试」按钮；瞬时流式传输故障在尝试预算内自动重试，不会直接让整局失败。
- **切换页面不中断对局**：棋局与战斗动画由页面内的模块级 store 驱动，切换会话、关闭会话标签都不中断 AI 思考与战斗进程；但状态只存在于页面内存中，刷新或关闭浏览器页面会重置对局。

## 📦 安装

```bash
# 从本地 checkout 安装（在插件目录内执行；先构建出 lib/）
pnpm run build
dsh plugin --profile web add /Users/yejiming/Desktop/OpenSource/dsh-auto-chess
```

## 🚀 快速开始

```bash
dsh --profile web --dump-config   # 输出中应出现 auto-chess 层
dsh web                            # 重启后会话标签栏出现「自走棋」标签
```

## 📚 更多信息

**快速安装**

DSH 的标准插件安装机制是「组合包 → profile」：插件包在 `package.json` 中声明 `dsh.bundle` 并附带 patch 文件（`cordis.patch.yml`），用 `dsh plugin` 把它安装进任意 profile：

**从本地 checkout 安装（在插件目录内执行；先构建出 lib/）**

pnpm run build dsh plugin --profile web add /Users/yejiming/Desktop/OpenSource/dsh-auto-chess 安装后验证配置层，再启动（或重启）Web 界面： dsh --profile web --dump-config # 输出中应出现 auto-chess 层 dsh web # 重启后会话标签栏出现「自走棋」标签 > 插件已安装到本机的 `web` profile（`~/.dsh/profiles/web`，`@deepseek-ai/dsh-auto-chess` 以 link 依赖加入 bundle 列表）。Web 进程需重启才会扫描到新的 dshClient 包并注入客户端标签。 移除：`dsh plugin --profile web remove @deepseek-ai/dsh-auto-ch

## 🔗 链接

- [GitHub 仓库](https://github.com/omdsh-dev/dsh-auto-chess)
- [完整 README](https://github.com/omdsh-dev/dsh-auto-chess#readme)
- [返回dsh-auto-chess所在分类](../plugins.md)
