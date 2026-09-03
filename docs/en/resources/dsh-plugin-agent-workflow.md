---
title: "dsh-plugin-agent-workflow"
description: "DeepSeek Harness Agent Workflow"
keywords: "dsh-plugin-agent-workflow, workflow, coding, multi-agent, deepseek harness, dsh"
---
# dsh-plugin-agent-workflow

> ⭐ **78** · ✅ active · workflow · ⬆️ +4 recently

| | | | |
|---|---|---|---|
| Type | workflow | Category | Workflows |
| Stars | ⭐ 78 | Status | ✅ active |
| Author | [xuanyuanzhifeng](https://github.com/xuanyuanzhifeng) | Updated | 2026-08-18 |

## One-liner

> DeepSeek Harness Agent Workflow

## About

`dsh-plugin-agent-workflow` 是一个可独立安装的 DeepSeek Harness Web UI 插件。它在原有“对话”和“轨迹”之外增加“工作流”标签页，以用户对话轮次为入口，把 Agent 的模型请求、模型响应和工具调用呈现为清晰的执行链路。 插件不会替换或修改 DeepSeek Harness 内置的“轨迹”功能。

## ✨ Key Features

- **按轮次浏览**：左侧固定显示当前 Session 的用户对话轮次，包括提示词摘要、开始时间、模型调用数、工具调用数和完成状态。
- **执行链路可视化**：每次模型调用依次展示请求、响应和工具调用卡片，一行内容超出可视区域时支持横向滚动。
- **完整请求检查**：请求详情分别展示真实记录的 `system`、提供方无关的 `messages[]` 和 `tools`，JSON 节点可以逐级展开或收起。
- **响应内容检查**：展示 reasoning、content、工具调用以及当次模型响应的原始记录。
- **工具执行状态**：区分运行中、完成和失败状态，并展示调用参数、执行结果、耗时和错误摘要。
- **Token 与缓存统计**：分别显示输入、未缓存输入、缓存读取、缓存写入和输出 Token，便于分析上下文复用情况。
- **大数据量浏览**：轮次列表和模型调用列表独立滚动，模型调用行使用虚拟化渲染，长链路不会挤压整个页面。

## 📦 Install

```bash
pnpm install
pnpm run typecheck
pnpm test
pnpm pack
```

## 🚀 Quick Start

```bash
dsh@0.1.0-rc.8
```

## 📚 Learn more

**安装本地 `.tgz` 包**

假设安装包位于当前目录： npx --yes @deepseek-ai/dsh@0.1.0-rc.8 plugin \ --profile web \ add ./dsh-plugin-agent-workflow-0.1.1.tgz \ --workspace-root 检查安装结果： npx --yes @deepseek-ai/dsh@0.1.0-rc.8 plugin \ --profile web \ list --depth 0 列表中出现 `dsh-plugin-agent-workflow 0.1.1` 表示安装成功。重启 Web UI 后即可看到“工作流”标签页： npx --yes @deepseek-ai/dsh@0.1.0-rc.8 web

**从 GitHub 安装**

仓库发布 `v0.1.1` 标签后，可以直接安装固定版本： npx --yes @deepseek-ai/dsh@0.1.0-rc.8 plugin \ --profile web \ add github:xuanyuanzhifeng/dsh-plugin-agent-workflow#v0.1.1 \ --workspace-root 固定 Release 标签或 commit 可以避免安装内容随分支变化。只有在信任源码的情况下，才应允许包管理器执行 Git 依赖的构建脚本。

## 🔗 Links

- [GitHub Repository](https://github.com/xuanyuanzhifeng/dsh-plugin-agent-workflow)
- [Full README](https://github.com/xuanyuanzhifeng/dsh-plugin-agent-workflow#readme)
- [Back to the Workflows & Automation list](../workflows.md)
