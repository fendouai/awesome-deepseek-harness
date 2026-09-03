---
title: "dsh-mcp-manager"
description: "用于 DeepSeek Harness 的 MCP 可视化管理插件：在「设置 → MCP」中查看已安装/启用的 MCP 服务器，支持增删、启用/停用，并实时查看连接状态。"
keywords: "dsh-mcp-manager, mcp, integration, coding, deepseek harness, dsh"
---
# dsh-mcp-manager

> ⭐ **17** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | MCP |
| 星数 | ⭐ 17 | 状态 | ✅ 活跃 |
| 作者 | [Js2Hou](https://github.com/Js2Hou) | 更新时间 | — |

## 一句话介绍

> 用于 DeepSeek Harness 的 MCP 可视化管理插件：在「设置 → MCP」中查看已安装/启用的 MCP 服务器，支持增删、启用/停用，并实时查看连接状态。

## 详细介绍

MCP 可视化管理器：装没装、连没连，一目了然 查看列表 新增删除 启用停用 连接状态 连接测试 中英双语 DeepSeek Harness DSH Desktop 设置 → MCP 一站管理 DeepSeek Harness 里的所有 MCP 服务器， 无需再手改 cordis.patch.yml —— 所有修改即改即生效（HMR 热应用）。 🌏 中文 · English

## ✨ 核心特性

- **📋 服务器列表**：列出所有已安装/启用的 MCP 服务器（`@deepseek-ai/dsh-mcp-client` 实例）——`serverName`、传输方式（`stdio` / `streamable-http`）、URL / 命令、启用状态、加载阶段、已注册工具数
- **➕ 新增 / ➖ 删除**：表单添加 MCP 服务器（stdio 与 streamable-http，支持 env / headers / args / 超时 / failOnStartupError），带格式与重名校验；一键删除
- **🔌 启用 / 停用**：随时切换，工具随之热连接 / 热断开
- **📶 连接状态**：每台服务器实时状态胶囊（Connected · N tools / Failed / Loading / Disabled）+ 独立 **Test** 探测（`initialize` + `tools/list`，报告延迟与工具数）
- **✏️ 编辑**：在被编辑卡片原位展开表单，保存即应用
- **🌏 多语言**：界面文案跟随 DSH 语言（zh / en）实时切换
- **💾 持久化**：所有修改写入 profile 的 `cordis.patch.yml`，重启后保留；页面底部显示文件路径

## 📦 安装

```bash
dsh plugin --profile web add @js2hou/dsh-mcp-manager
```

## 🚀 快速开始

```bash
dsh plugin --profile web add github:Js2Hou/dsh-mcp-manager
```

## 📚 更多信息

**🚀 安装**

插件已收录至 **[dsh-market](https://github.com/dsh-market/dsh-market)** 与 **[dsh-plugin-marketplace](https://github.com/AwesomeHou/dsh-plugin-marketplace)**。 **前置**：DSH 已装好（`dsh web` 能正常运行）。

**方式一 · AI Agent 安装**

> 告诉 Agent：「请安装 dsh-mcp-manager 插件，插件仓库是 https://github.com/Js2Hou/dsh-mcp-manager」

**方式三 · dsh 命令安装**

dsh plugin --profile web add @js2hou/dsh-mcp-manager 也可 **GitHub 源安装**（构建产物 `lib/` 已入库，无需本地构建）： dsh plugin --profile web add github:Js2Hou/dsh-mcp-manager <details> <summary><b>脚本安装</b>（一键脚本安装：自动处理新版放行与残留清理，幂等）</summary> **macOS / Linux**（Windows 装了 Git Bash 或 WSL 也可）： curl -fsSL https://raw.githubusercontent.com/Js2Hou/dsh-mcp-manager/main/scripts/install.sh | bash **Windows（PowerShell 5.1+ / pws

**② 安装并自动挂载（npm 包；本地 checkout 请用 link: 绝对路径）**

npx -y --package @deepseek-ai/dsh dsh plugin --profile web add @js2hou/dsh-mcp-manager **Windows（PowerShell）**： cd ~\.dsh\profiles\web

## 🔗 链接

- [GitHub 仓库](https://github.com/Js2Hou/dsh-mcp-manager)
- [完整 README](https://github.com/Js2Hou/dsh-mcp-manager#readme)
- [返回dsh-mcp-manager所在分类](../integrations.md)
