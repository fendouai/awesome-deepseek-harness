---
title: "dsh-ui-progress"
description: "DSH Web UI 会话进度插件：输入框停靠区常驻会话进度条（todos 真实进度 / 实时 token 生成速率 / 中断橘红态 / 待办提醒），零核心改动"
keywords: "dsh-ui-progress, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-ui-progress

> ⭐ **8** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 8 | 状态 | ✅ 活跃 |
| 作者 | [lhh010](https://github.com/lhh010) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding, ui |

## 一句话介绍

> DSH Web UI 会话进度插件：输入框停靠区常驻会话进度条（todos 真实进度 / 实时 token 生成速率 / 中断橘红态 / 待办提醒），零核心改动

## 详细介绍

DSH Web UI 会话进度插件：为 DeepSeek Harness 的 Web GUI 的输入框停靠区提供常驻会话进度条，**零核心改动**（纯 client 插件，不触碰 agent-loop）。

## ✨ 核心特性

- **常驻会话进度条**（`conversation.input.dock`，输入框停靠区）：读取框架 `useSession` 快照渲染真实执行状态——运行中/空闲、当前在飞的工具名、当前窗口已结算的工具结果数、当前轮次。运行中左侧加载圈**旋转**，进度条 shimmer 扫光 + 品牌色光环脉冲，填充宽度缓动。**
- **中断橘红态**（v0.8.0 新增）：本会话**最近一个已结束回合被中断/停止**——手动打断、API 故障或其他意外原因——进度条切换为**橘红色**（浅橘背景 + 橘红填充/图标/百分比 + 慢速脉冲），标签显示"已中断"，优先于运行中/完成态的常规配色。只按**最近一个**回合判定：中断后继续发送并正常完成的
- **实时 token 生成速率**（v0.9.0 新增）：运行中**模型正在生成**时（有流式 partial 内容、且无待处理的人机交互），进度条在已耗时旁显示实时速率（如 `12.3 tok/s`，斜体品牌色，固定最小宽度保持进度条右侧稳定）。流式 chunk 不携带 token 计数（核心端只有回合结束后的 pr
- **待办提醒（attention）**：本会话或其后代 subagent 会话存在**等待人处理的交互**（沙箱命令审批 / 选项选择 / 计划审阅）时，进度条切换为**琥珀色警告态**（浅琥珀背景 + 琥珀填充/图标 + 慢速脉冲），文字提示来源与类型——`等待审批` / `需要选择`（本会话）、`子代理等待审批` 

## 📦 安装

```bash
# 方式一：git 依赖固定 tag（公开镜像，推荐；也可用 github:lhh010/dsh-ui-progress）
dsh plugin --profile web add '@dsh-external/dsh-ui-progress@github:lhh010/dsh-ui-progress#v0.9.11'

# 方式二：本地 link（开发）
git clone https://github.com/lhh010/dsh-ui-progress.git
cd dsh-ui-progress && pnpm install && pnpm run build
dsh plugin --profile web add link:/path/to/dsh-ui-progress
```

## 🚀 快速开始

```bash
- insert:
    - id: dsh-ui-progress
      name: '@dsh-external/dsh-ui-progress'
```

## 📚 更多信息

**提示词安装（让 DSH 自己装）**

把下面这段提示词发给任意一个 DSH 会话，模型会替你完成安装： > 帮我安装 dsh-ui-progress 插件（DSH 会话进度条：输入框常驻会话进度条/todos 真实进度/中断橘红态），步骤： > 1. 执行 `dsh plugin --profile web add '@dsh-external/dsh-ui-progress@github:lhh010/dsh-ui-progress#v0.9.11'`（首次可能被 pnpm 11 拦截 node-pty 构建脚本而失败） > 2. 在 `~/.dsh/profiles/web` 下执行 `pnpm approve-builds --all`（放行构建脚本） > 3. 再执行一次第 1 步的安装命令 > 4. 完成后提醒我硬刷新浏览器（Ctrl/Cmd+Shift+R） > 遇到报错先查 https://github.com/

**配置**

无配置键。安装后只需在配置树里插入一行： - id: dsh-ui-progress name: '@dsh-external/dsh-ui-progress'

## 🔗 链接

- [GitHub 仓库](https://github.com/lhh010/dsh-ui-progress)
- [完整 README](https://github.com/lhh010/dsh-ui-progress#readme)
- [返回dsh-ui-progress所在分类](../plugins.md)
