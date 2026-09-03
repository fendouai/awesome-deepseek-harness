---
title: "dsh-grok-tui"
description: "基于 grok-build 构建的 TUI。"
keywords: "dsh-grok-tui, terminal, client, deepseek harness, dsh"
---
# dsh-grok-tui

> ⭐ **11** · ✅ 活跃 · 客户端 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 终端 |
| 星数 | ⭐ 11 | 状态 | ✅ 活跃 |
| 作者 | [chen-001](https://github.com/chen-001) | 更新时间 | 2026-08-15 |

## 一句话介绍

> 基于 grok-build 构建的 TUI。

## 详细介绍

把 [grok-build](https://github.com/xai-org/grok-build) 的 TUI 作为 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (dsh) 的前端：界面是 grok 的，内核（提示词、工具、模型路由、会话持久化）由 dsh 提供。 Grok's TUI as a frontend for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (dsh): the interface is grok's, the engine (prompts, tools, model routing, persistence) is dsh's.

## 📦 安装

```bash
npm install -g dsh-grok-tui
grok-dsh setup        # 把 grok bridge 挂进 dsh web 的 profile（幂等，可重复执行）
                      # wire the grok bridge into the dsh web profile (idempotent)
npx @deepseek-ai/dsh web   # 启动官方 host / start the official host
grok-dsh              # 打开 TUI，直连运行中的 dsh web
                      # open the TUI, bridging to the running dsh web
```

## 🚀 快速开始

```bash
git clone https://github.com/chen-001/dsh-grok-tui.git
cd dsh-grok-tui && sh install.sh
```

## 📚 更多信息

**安装 / Installation**

前提：已安装 [dsh](https://github.com/deepseek-ai/deepseek-harness) 与 grok TUI 二进制（`curl -fsSL https://x.ai/cli/install.sh | bash`）。支持 macOS / Linux。 Prerequisites: [dsh](https://github.com/deepseek-ai/deepseek-harness) and the grok TUI binary (`curl -fsSL https://x.ai/cli/install.sh | bash`). macOS / Linux.

**方式 B：git 完整安装 / Full installer**

git clone https://github.com/chen-001/dsh-grok-tui.git cd dsh-grok-tui && sh install.sh This installer performs the same bridge hookup automatically, then builds and writes the `grok-dsh` launcher into your PATH. 两种方式安装后的行为完全一致（命令、herdr 侧栏自动配置、用量面板）。 Both paths behave identically afterwards (command, automatic herdr sidebar config, usage panels).

**使用 / Usage**

先启动官方 host（推荐），再打开 TUI： Start the official host first (recommended), then open the TUI: dsh web # 启动官方 host / start the official host grok-dsh # 打开 TUI：检测到运行中的 dsh web 则直连，否则启动本窗口独立后端 # open the TUI: bridges to a running dsh web, else starts a per-window backend grok-dsh stop # 停止所有独立后端 / stop all standalone backends grok-dsh status # 查看 host 桥 / 独立后端状态与 grok 版本 / host bridge & backend status, gro

**用量指标展示 / Usage metrics**

官方 grok 二进制即可显示 token 用量（状态栏 `18K/1.0M` context bar）。完整指标——缓存命中率、TTFT、TPS、输入/输出 token——在以下环境自动展示，**无需编译任何 grok 源码**： The stock grok binary already shows token usage (the `18K/1.0M` context bar). Full metrics — cache hit rate, TTFT, TPS, in/out tokens — appear automatically in these environments, **no grok source build needed**:

## 🔗 链接

- [GitHub 仓库](https://github.com/chen-001/dsh-grok-tui)
- [完整 README](https://github.com/chen-001/dsh-grok-tui#readme)
- [返回dsh-grok-tui所在分类](../clients.md)
