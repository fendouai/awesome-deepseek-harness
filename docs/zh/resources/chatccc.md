---
title: "chatccc"
description: "飞书（Lark）或微信（WeChat）聊天控制 DeepSeek Harness / Claude Code / Cursor / Codex / CCC Agent"
keywords: "chatccc, channel, integration, coding, multi-agent, deepseek harness, dsh"
---
# chatccc

> ⭐ **22** · ✅ 活跃 · 集成 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 渠道 |
| 星数 | ⭐ 22 | 状态 | ✅ 活跃 |
| 作者 | [wzj998](https://github.com/wzj998) | 更新时间 | 2026-08-21 |

## 一句话介绍

> 飞书（Lark）或微信（WeChat）聊天控制 DeepSeek Harness / Claude Code / Cursor / Codex / CCC Agent

## 详细介绍

**用飞书或微信聊天控制 Claude Code / Cursor / Codex / CCC Agent / DeepSeek Harness。** ChatCCC 把本地 AI 编程工具接入即时通讯软件。你可以在手机上发消息，让 Claude Code、Cursor Agent、Codex、内置 CCC Agent 或 DeepSeek Harness 继续写代码、查问题、跑命令；不用一直守在电脑前。 飞书是推荐入口：直接私聊机器人即可持续使用同一个专属会话，需要并行任务时再用 `/new` 创建独立会话群；卡片能流式更新，体验完整。微信 iLink 更适合快速试用或临时使用：扫码即可接入，但只能走私聊文本模式。     ---

## ✨ 核心特性

- **手机上也能用 AI 编程工具**：在飞书或微信发消息，就像在终端给 Agent 下指令。
- **飞书体验更完整**：私聊可持续对话，`/new` 创建的一群一会话支持多任务并行，CardKit 卡片可流式更新。
- **微信接入更轻**：不用创建飞书应用，启动后扫码即可在微信私聊里使用。
- **多 Agent 切换**：`/new` 使用默认 Agent，也可以用 `/new claude`、`/new cursor`、`/new codex`、`/new ccc`、`/new dsh` 指定工具。
- **群里能跑 git**：`/git status`、`/git pull`、`/git log` 会在当前会话工作目录执行，并把输出发回聊天窗口。

## 📦 安装

```bash
npm install -g chatccc
chatccc
```

## 🚀 快速开始

```bash
git clone https://github.com/wzj998/ChatCCC.git
cd ChatCCC
npm install
npm run dev
```

## 📚 更多信息

**Windows 一键安装（零依赖起步）**

如果你的电脑没有装任何东西，**复制下面全部内容，打开 PowerShell 粘贴，回车**。脚本会自动检测并安装所有缺失的依赖，最后启动 ChatCCC。全程只需确认一次 UAC 弹窗。

**--- 辅助函数：安装完程序后刷新 PATH，让当前窗口立即可用 ---**

function Refresh-Path { $env:Path = [System.Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [System.Environment]::GetEnvironmentVariable('Path','User') }

**--- 辅助函数：判断一个命令是否已安装 ---**

function Test-Cmd($name) { return [bool](Get-Command $name -ErrorAction SilentlyContinue) }

**其他安装方式**

npm install -g chatccc chatccc 要求 Node.js >= 20。安装完成后，在任意目录执行 `chatccc` 即可启动。配置、日志和状态文件会保存在用户目录的 `.chatccc` 下： 旧版本留在仓库或包目录下的 `config.json`、`logs/`、`state/` 会在首次启动时自动迁移到用户目录。 每次直接运行 `chatccc` 时，无论是否已经完成配置，ChatCCC 默认都会用系统默认浏览器打开本地 Web UI（默认 `http://localhost:18080/`，修改 `config.port` 后跟随实际端口）。可在首次配置向导或管理页的 **Web UI** 设置中关闭；关闭后从下一次直接启动起生效。由 `/restart`、`/update` 或 Web UI 发起的内部重启始终不会重复打开浏览器。Linux 服务器没有 

## 🔗 链接

- [GitHub 仓库](https://github.com/wzj998/ChatCCC)
- [完整 README](https://github.com/wzj998/ChatCCC#readme)
- [返回chatccc所在分类](../integrations.md)
