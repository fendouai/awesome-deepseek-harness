---
title: "dsh-plugin-interpreters"
description: "暴露 run_python/run_node 工具，通过 stdin 执行代码返回 stdout/stderr/exit。"
keywords: "dsh-plugin-interpreters, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-interpreters

> ⭐ **9** · ✅ 活跃 · 插件 · 近期 ⬆️ +3

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 9 | 状态 | ✅ 活跃 |
| 作者 | [HuanLinOTO](https://github.com/HuanLinOTO) | 更新时间 | 2026-08-19 |
| 子分类 | 🧰 工具与工具包 | 能力 | coding |

## 一句话介绍

> 暴露 run_python/run_node 工具，通过 stdin 执行代码返回 stdout/stderr/exit。

## 详细介绍

DSH 插件：暴露 `run_python` 和 `run_node` 两个模型可调用工具，通过 stdin 执行代码并返回 stdout/stderr/exit code。在设置页「插件配置」分区提供配置卡片，让用户设置 Python 和 Node.js 解释器的可执行文件路径，工具描述中会告知模型解释器位置。

## ✨ 核心特性

- **工具**：`run_python` / `run_node`，通过 `spawn(executable, ['-'])` 执行代码，代码经 stdin 传入（无命令行长度限制）
- **设置持久化**：通过 `ctx.settings` 命名空间 `interpreters` 持久化到 `$DSH_HOME/settings.yaml`
- **动态 description**：工具的 `description` 在注册时根据配置计算，包含解释器路径；设置变更时通过 `bridge.onChange()` 自动重新注册
- **配置暴露（TypertRemoteService 模式）**：DSH 的 settings RPC 域（api-proxy）只向配置客户端提供白名单命名空间（`interpreters` 不在其中），所以浏览器通过 host 内置的 typertRemote `/api` RPC 通道读写 `interpreter
- **客户端 bundle**：配置卡片通过 `settings.plugin.item` slot 注册（「插件配置」分区），卡片用 `connection.rpc.call('/api', 'interpreters/get'|'set', { args: {...} })` 读写，不依赖 `settingsScop

## 📦 安装

```bash
pnpm install          # 安装依赖（link: 指向 ~/.dsh/source/current/）
pnpm run typecheck    # tsc --noEmit
pnpm test             # vitest run
pnpm run build        # tsdown + tsc（生成 lib/index.js, lib/client.js, lib/types/*.d.ts）
```

## 🚀 快速开始

```bash
# 从 npm 安装（推荐）：
dsh plugin --profile web add @huanlin/dsh-plugin-interpreters

# 本地开发（热更新）：
dsh plugin --profile web add "link:D:/Projects/deepseek-harness/dsh-interpreters"
```

## 📚 更多信息

**配置**

默认配置（`cordis.patch.yml`）： pythonPath: 'python' # Python 可执行文件路径 nodePath: 'node' # Node.js 可执行文件路径 timeoutMs: 30000 # 执行超时（毫秒） 运行时通过设置页「插件配置」分区的卡片修改，持久化到 `$DSH_HOME/settings.yaml`。

## 🔗 链接

- [GitHub 仓库](https://github.com/HuanLinOTO/dsh-plugin-interpreters)
- [完整 README](https://github.com/HuanLinOTO/dsh-plugin-interpreters#readme)
- [返回dsh-plugin-interpreters所在分类](../plugins.md)
