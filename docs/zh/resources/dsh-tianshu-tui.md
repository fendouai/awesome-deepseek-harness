---
title: "dsh-tianshu-tui"
description: "DSH 交互式终端 UI 插件：在官方基础上增加 TDD、证据门、视觉图像模块等工作流。"
keywords: "dsh-tianshu-tui, terminal, client, workflow, deepseek harness, dsh"
---
# dsh-tianshu-tui

> ⭐ **226** · ✅ 活跃 · 客户端 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 终端 |
| 星数 | ⭐ 226 | 状态 | ✅ 活跃 |
| 作者 | [huiliyi37](https://github.com/huiliyi37) | 更新时间 | 2026-08-20 |

## 一句话介绍

> DSH 交互式终端 UI 插件：在官方基础上增加 TDD、证据门、视觉图像模块等工作流。

## 详细介绍

**dsh-tianshu-tui**（`@huiliyi37/dsh-tianshu-tui`）是官方 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 上的交互式终端 UI 插件。渲染核心为自研的 ANSI 极简引擎（由作者自己的开源项目 [天枢 Tianshu-Tui](https://github.com/huiliyi37/Tianshu-Tui) 演进而来，Apache-2.0；逐文件来源见 [SOURCE-MAP.md](SOURCE-MAP.md)），渲染轻量不打断，使用体验流畅。UI 是纯展示层：所有 agent 状态都来自会话事件流。在此之上做了 harness 工程层的个性化改造，如图像与视觉桥接、代码智能检索、记忆与跨会话召回等。

## ✨ 核心特性

- **终端内的完整会话工作区** — 实时渲染、只增滚动转录、启动时会话恢复、`/fork` 探索分支、`/rewind` 回退（会话截断 + 可选文件回退）、`/export` 导出 Markdown 转录、中轮转向（`/steer` / `Ctrl+T`）。
- **图片端到端** — 剪贴板粘贴（`Ctrl+V` / 终端菜单粘贴）、以终端图形协议内联渲染（kitty / iTerm2）、经 harness 附件服务投递、让具备视觉能力的模型真正看见——主模型不识图时自动经独立视觉模型把图片转成描述（视觉桥）。
- **完整输入面** — grok 风格 slash 下拉菜单（模糊前缀匹配、MRU 排序、ghost 预览）、`@`-路径 Tab 补全与 `@mention` 展开、bracketed paste、可选 vim 键位、外部编辑器（`Ctrl+E`）、历史搜索（`Ctrl+F`/`Ctrl+R`）——`Ctrl+.` 
- **终端内交互面** — 结构化提问面板（数字键选择、plan-review 反馈模式）、带内联 `diff` 预览的挂起审批卡片、模式循环（`Shift+Tab`：normal → plan → always-approve）、命令面板，以及 status / config / skills / tasks / 委派
- **推理过程可视化** — think 通道以实时头行流动、在滚动区折叠为紧凑行（`✻ 思考 (3.2s) · 12 行`）、`Ctrl+O` 原位展开（对标竞品：默认折叠）。
- **个性化 harness 集成** — `/doctor` 终端诊断、`/memory` 项目记忆浏览器、`/btw` 后台 agent 侧问、`/model` + `/effort` 热切换（当前会话立即生效）。
- **构造上可审计** — TUI 自身不注册任何 prompt、工具或上下文面；用户输入成为普通日志消息，所有渲染状态都派生自会话事件。
- **与 harness 协同演化** — 在 2026-08-09 基线快照之上与 harness 侧能力同步开发（250+ 提交）：图片/视觉链路、DeepSeek Spark 模型工程、会话持久化与文件快照、记忆、验证门与失败路由、代码智能、git 工具。见下一节。

## 📦 安装

```bash
pnpm dlx @deepseek-ai/dsh plugin --profile tui add @huiliyi37/dsh-tianshu-tui
```

## 🚀 快速开始

```bash
pnpm dlx @deepseek-ai/dsh --profile tui
```

## 📚 更多信息

**安装**

本包不是独立程序。须先有官方 CLI [`@deepseek-ai/dsh`](https://www.npmjs.com/package/@deepseek-ai/dsh)（npm `latest`，当前 `0.1.1-rc.2`；需 ≥ `0.1.0-rc.8`，peer 依赖对齐）。只 `npm i` 本包跑不起来。 **一键安装（推荐）**：仓库自带跨平台脚本，自动检测 Node/pnpm、经 pnpm 安装官方 CLI + 装配本插件并启动（国内网络默认走 npmmirror 镜像）：

**只安装不启动：**

bash <(curl -fsSL https://raw.githubusercontent.com/huiliyi37/dsh-tianshu-tui/main/scripts/install-tui.sh) --no-launch

**只安装不启动：**

powershell -ExecutionPolicy Bypass -File scripts\install-tui.ps1 -NoLaunch # 克隆仓库后本地跑

**更新说明**

当前 npm `latest`：[`@huiliyi37/dsh-tianshu-tui@0.1.2-rc.28`](https://www.npmjs.com/package/@huiliyi37/dsh-tianshu-tui)（[GitHub Release](https://github.com/huiliyi37/dsh-tianshu-tui/releases/tag/v0.1.2-rc.28)）。 **0.1.2-rc.28（2026-08-29）**：回应 #55 的 vim 优化——光标形态分模式（NORMAL 反色块 / insert 竖线）、历史搜索两阶段输入（编辑段可输 n/N，`Enter` 后跳转、搜索对象显式标注）、搜索命中子串高亮（含 `/scroll`）；另投递失败自动回填输入行 + README 键位表一致性守卫。 **0.1.2-rc.27（2026-

## 🔗 链接

- [GitHub 仓库](https://github.com/huiliyi37/dsh-tianshu-tui)
- [完整 README](https://github.com/huiliyi37/dsh-tianshu-tui#readme)
- [返回dsh-tianshu-tui所在分类](../clients.md)
