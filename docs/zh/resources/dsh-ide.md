---
title: "dsh-ide"
description: "dsh-IDE 把 DeepSeek Harness（DSH）网页版升级成一站式 IDE：JupyterLab 式文件树、带语法高亮的代码编辑、多格式预览、Trae 风格红绿 diff 和内置终端，再加上「本地大脑、远程手脚」的 SSH 远程工作区，让 AI 直接在本机操控远程服务器，全程零配置文件改动。"
keywords: "dsh-ide, ide, integration, coding, deepseek harness, dsh"
---
# dsh-ide

> ⭐ **24** · ✅ 活跃 · 集成 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | IDE 与编辑器 |
| 星数 | ⭐ 24 | 状态 | ✅ 活跃 |
| 作者 | [chenw2759-wq](https://github.com/chenw2759-wq) | 更新时间 | 2026-08-17 |

## 一句话介绍

> dsh-IDE 把 DeepSeek Harness（DSH）网页版升级成一站式 IDE：JupyterLab 式文件树、带语法高亮的代码编辑、多格式预览、Trae 风格红绿 diff 和内置终端，再加上「本地大脑、远程手脚」的 SSH 远程工作区，让 AI 直接在本机操控远程服务器，全程零配置文件改动。

## 详细介绍

把 DeepSeek Harness（DSH）Web GUI 升级为**一体化开发环境**，四大核心能力： - 🖥️ **右侧边栏**：可停靠的右栏抽屉——文件树 + 预览/编辑同框；**拖 tab 拖出成浮窗，拖回右缘自动停靠**（下框 / 右栏 / 浮动 / 三栏 IDE 四态切换） - 📄 **预览**：Markdown / HTML / 图片 / CSV / Office（docx / xlsx / pptx）/ 日志等多格式直接预览 - ✏️ **编辑**：代码即时编辑（语法高亮 + 行号 + 斑马纹）+ Markdown/HTML **Word 式可视化编辑** + Office 框内富文本编辑 - 🧩 **IDE**：文件树、命令行终端、Trae 风格红绿 diff、类型颜色标签、Git 角标、监视路径——开箱即用的 JupyterLab 式工作区 同时内置 **SSH 远程工作区模式**：右上角（session log 左侧）配置 SSH 主机（密码 / 密钥，复用 `~/.dsh/dsh-ssh.json`），进入后右侧面板自动切换为远程文件树，**模型本机的 read / write / edit / glob / grep 与 bash / 终端在 SSH 模式下透明地在远程服务器执行**，LLM 与 Agent 循环仍在本机——「本地大脑、远程手脚」。

## ✨ 核心特性

- 🖥️ **右侧边栏**：可停靠的右栏抽屉——文件树 + 预览/编辑同框；**拖 tab 拖出成浮窗，拖回右缘自动停靠**（下框 / 右栏 / 浮动 / 三栏 IDE 四态切换）
- 📄 **预览**：Markdown / HTML / 图片 / CSV / Office（docx / xlsx / pptx）/ 日志等多格式直接预览
- ✏️ **编辑**：代码即时编辑（语法高亮 + 行号 + 斑马纹）+ Markdown/HTML **Word 式可视化编辑** + Office 框内富文本编辑
- 🧩 **IDE**：文件树、命令行终端、Trae 风格红绿 diff、类型颜色标签、Git 角标、监视路径——开箱即用的 JupyterLab 式工作区

## 📦 安装

```bash
# 重启 dsh
npx @deepseek-ai/dsh web
```

## 🚀 快速开始

```bash
dsh-IDE/
├── packages/
│   ├── dsh-aionui-panel/ # 右侧面板系统：文件树/预览/终端/编辑 diff/类型色标签（IDE 工作区本体）
│   ├── dsh-ssh/          # SSH 引擎：ssh2 连接池、exec/PTY/SFTP/隧道/集群（SSH 远程模式依赖）
│   └── dsh-easyssh/      # SSH 远程工作区：模式状态机、接缝门面、远程实现、Web GUI 前端
└── README.md
```

## 📚 更多信息

**2) 把三个包安装到 web profile（注意用你自己的绝对路径）**

dsh plugin --profile web add file:C:/你的路径/dsh-IDE/packages/dsh-aionui-panel dsh plugin --profile web add file:C:/你的路径/dsh-IDE/packages/dsh-ssh dsh plugin --profile web add file:C:/你的路径/dsh-IDE/packages/dsh-easyssh > 仓库品牌为 dsh-IDE；核心插件包名沿用 `dsh-easyssh`（安装标识，不随品牌改名）。 > 💡 **pnpm 构建放行（一行）**：dsh-ssh 依赖的原生库（ssh2 / cpu-features）需要构建。pnpm 10+ > 默认阻止依赖构建脚本，`dsh plugin add` 会报 > `ERR_PNPM_IGNORED_BUILDS: I

**使用**

1. 会话右上角（session log 左侧）点击 **SSH** → 填主机（别名/主机/端口/用户名/密码或密钥/远程根） → 保存并测试 → 进入 SSH 模式。 2. 右侧面板自动切换到远程文件树；直接对 Agent 说「读/改远程文件」「在服务器上执行命令」——普通工具即远程执行。 3. 路径规则：远程绝对路径直接用；相对路径以远程根 `remoteRoot`（默认 `~`）为基准；不要用 Windows 本机路径。 4. 右上角切换按钮随时回到本机模式。

## 🔗 链接

- [GitHub 仓库](https://github.com/chenw2759-wq/dsh-IDE)
- [完整 README](https://github.com/chenw2759-wq/dsh-IDE#readme)
- [返回dsh-ide所在分类](../integrations.md)
