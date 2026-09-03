---
title: "dsh-solo-thinking"
description: "Solo-style isolated brainstorm branches and Handoffs for DeepSeek Harness"
keywords: "dsh-solo-thinking, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-solo-thinking

> ⭐ **21** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 21 | 状态 | ✅ 活跃 |
| 作者 | [fredalxin](https://github.com/fredalxin) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Solo-style isolated brainstorm branches and Handoffs for DeepSeek Harness

## 详细介绍

把头脑风暴拆成一棵可操作的思考树：每个方向都是独立的 DeepSeek Harness Session，分支之间只交换 Agent 主动撰写的 Handoff。 Solo Thinking 是项目 [Solo](https://github.com/solo-agent/solo) 的一部分能力。

## ✨ 核心特性

- 默认建议模式：信息足够时自动创建 2–4 个真正独立的方向，优先 4 个，不为凑数而分裂。
- 独立 Session：每个节点拥有自己的对话、状态和生命周期，建议节点先休眠，收到第一条消息后才启动。
- 自动 Handoff：分裂继承、Current State、兄弟感知和 Return 总结均由 Agent 自动撰写，用户不需要手写。
- Workspace 继承：分支持久化挂在父 Session 所属 Workspace，不落入“未分组”。
- 输入不串线：主输入框只发给当前 Session；思考树可直接向选中的其他分支发送；只有“进入对话”会导航。
- 可回放持久化：树状态写入 DSH append-only Session 事件并通过 Projection 恢复。

## 📦 安装

```bash
dsh plugin --profile web add dsh-better-sidebar dsh-plugin-solo-thinking
```

## 🚀 快速开始

```bash
curl -fsSL https://raw.githubusercontent.com/fredalxin/dsh-solo-thinking/main/scripts/install.sh | bash
```

## 📚 更多信息

**官方 npm 单行安装（推荐，自动使用 latest）**

dsh plugin --profile web add dsh-better-sidebar dsh-plugin-solo-thinking 两个包都发布在 npm 官方 Registry；不指定版本时会自动安装各自 `latest` 标签对应的版本。安装后会由各自的 `dsh.bundle.patch` 自动挂载。Solo Thinking 将 Better Sidebar 声明为可选 peer，避免重复实例；DSH 目前不会自动挂载传递依赖，所以命令中需要把两个插件都列为 profile 的直接依赖。若 pnpm 拦截 `node-pty` 构建或新包发布时间门禁，可使用下面的 Release 安装器。 Better Sidebar 0.12.1 可能打印宿主 DSH/React peer 警告；不要为消除提示把整套 DSH 或 React 重复装进 profile。已确认 Sol

**一行安装（自动使用最新 Release）**

macOS / Linux（Windows 可在 Git Bash 或 WSL 中使用）： curl -fsSL https://raw.githubusercontent.com/fredalxin/dsh-solo-thinking/main/scripts/install.sh | bash Windows PowerShell 5.1+ / pwsh： irm https://raw.githubusercontent.com/fredalxin/dsh-solo-thinking/main/scripts/install.ps1 | iex 安装器会先为 Better Sidebar 精确放行 `node-pty` / `protobufjs` 构建并将其挂载为 profile 的直接插件，再解析最新 Solo Thinking Release、下载预构建 `.tgz` 与 `.

**不执行远程脚本：官方 CLI 单行安装（固定版本）**

仓库提交了预构建 `lib/`，因此也可以直接固定 GitHub tag 安装；macOS、Linux 和 Windows 通用，不执行插件构建脚本： dsh plugin --profile web add github:fredalxin/dsh-solo-thinking#v0.1.19 安装完成后启动或重启 DSH，再硬刷新浏览器： dsh --profile web --dump-config dsh --profile web 源码运行 DSH 时，把命令中的 `dsh` 换成 `pnpm dsh`。

**下载后离线安装**

下载 Release 中的 `dsh-plugin-solo-thinking-0.1.19.tgz` 后执行： dsh plugin --profile web add ./dsh-plugin-solo-thinking-0.1.19.tgz dsh --profile web

## 🔗 链接

- [GitHub 仓库](https://github.com/fredalxin/dsh-solo-thinking)
- [完整 README](https://github.com/fredalxin/dsh-solo-thinking#readme)
- [返回dsh-solo-thinking所在分类](../plugins.md)
