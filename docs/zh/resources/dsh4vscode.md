---
title: "dsh4vscode"
description: "由 DSH Agent 驱动的 VS Code 聊天窗口：OpenCode 风格独立会话，模型自动路由。"
keywords: "dsh4vscode, ide, integration, coding, deepseek harness, dsh"
---
# dsh4vscode

> ⭐ **5** · ✅ 活跃 · 集成 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | IDE 与编辑器 |
| 星数 | ⭐ 5 | 状态 | ✅ 活跃 |
| 作者 | [DoggyHU](https://github.com/DoggyHU) | 更新时间 | 2026-08-21 |

## 一句话介绍

> 由 DSH Agent 驱动的 VS Code 聊天窗口：OpenCode 风格独立会话，模型自动路由。

## 详细介绍

在 VS Code 里直接用 **DeepSeek Harness（DSH）** 的智能体。这不是一个聊天玩具——聊天面板背后是完整的 DSH agent：它可以读取、创建、修改工作区文件，运行命令，搜索网页，并行委派子任务，然后把每一步工具调用实时展示在聊天流里。

## ✨ 核心特性

- 🪟 **纯编辑器窗口形态（OpenCode 式）**：DSH Chat 是编辑器区里的独立窗口，与代码窗口平级——**每个窗口 = 一个完整的会话工作区**：自带会话 tab 栏、＋新建、🪟再开新窗口、📜历史、模型选择器、问题卡片。窗口想开几个开几个，拖到任意编辑器组分屏并行。
- 🔒 **窗口之间完全独立**：新窗口永远创建**全新的独立会话**（全新上下文），各窗口各聊各的、互不同步；同一窗口内可切换会话 tab。
- 🖥 **入口**：编辑器右上角 💬 按钮 / `Ctrl+Alt+D` / 状态栏 🐳 / 命令 `DSH: New Chat Window`——全部是"开一个独立窗口"。
- 📑 **会话历史 = 当前工作区**：窗口内 📜 按钮列出**当前工作区**（cwd）的全部历史会话，与 DSH Web UI 的会话列表同源同步（`session.list` 过滤同 cwd、隐藏空占位会话），一键切换/继续旧对话。
- ❓ **Agent 提问卡片**：agent 调用 `ask_user_question` 时弹出问题卡片（单选/多选/自定义输入），回答后 agent 继续，不再卡死。
- 🤖 **真正的 agent**：会话绑定当前工作区（`cwd`），DSH 的 `standard` preset 自带文件读写、终端、搜索、子代理等全套工具——让它"直接改文件"，它就真的改。
- 🎛 **模型选择器 = DSH Web UI 的原样镜像**（插件零自有模型逻辑）：
- 🎯 **选中内容自动附带（Claude Code 同款）**：在编辑器里选中一行/一段文字，直接在聊天里说"把这行替换成 12345"——发送时自动附带选中内容（文件路径、行号、代码块），agent 直接就能看到并改文件，不用再手动粘贴。

## 📦 安装

```bash
npm install
npm run compile
npm run package     # 生成 dsh4vscode-<version>.vsix
```

## 🚀 快速开始

```bash
npm install
npm run compile
code --extensionDevelopmentPath=<本目录>
```

## 📚 更多信息

**特性**

- 列表直接索引 `session.models`：按 provider 分组、显示名、每个模型声明的 effort 档位——DSH 加模型/加 provider 插件自动出现，无需升级插件 - 选中即调 `session.selectModel`（DSH 自己校验），effort 下拉按所选模型声明的档位重建 - **继承跟着 DSH 走**：选一次成为 DSH 部署默认值，新建对话自动继承（插件重启也不丢） - 发送时直接 prompt——DSH 用自己的 current 组装本轮，与 Web UI 同一条路径 - 编辑器右上角 💬 按钮一键开窗口；选中代码时出现 ❓（解释）和 🐛（修复）按钮 - 右键选中代码 → 「DSH: Ask About Selection」/「DSH: Debug / Fix Selection」（自动附带文件路径、行号、代码块，并打开新窗口） - 输入 `

**方式一：VSIX 安装（推荐）**

npm install npm run compile npm run package # 生成 dsh4vscode-<version>.vsix 然后在 VS Code 中：扩展面板 → `...` → **Install from VSIX**，选择生成的 `.vsix`。

## 🔗 链接

- [GitHub 仓库](https://github.com/DoggyHU/dsh4vscode)
- [完整 README](https://github.com/DoggyHU/dsh4vscode#readme)
- [返回dsh4vscode所在分类](../integrations.md)
