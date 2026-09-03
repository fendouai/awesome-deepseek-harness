---
title: "dsh-bash-encoding"
description: "DSH bash 输出编码自动识别插件：替换 ctx.bash，自管 spawn 收集原始字节，自动检测 UTF-16LE/UTF-8/GBK 等编码并正确解码，修复 WSL/Windows 下 bash 工具的中文乱码。"
keywords: "dsh-bash-encoding, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-bash-encoding

> ⭐ **8** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 8 | 状态 | ✅ 活跃 |
| 作者 | [lhh010](https://github.com/lhh010) | 更新时间 | — |
| 子分类 | 🧰 工具与工具包 | 能力 | coding |

## 一句话介绍

> DSH bash 输出编码自动识别插件：替换 ctx.bash，自管 spawn 收集原始字节，自动检测 UTF-16LE/UTF-8/GBK 等编码并正确解码，修复 WSL/Windows 下 bash 工具的中文乱码。

## 详细介绍

DSH bash 输出**编码自动识别**插件：替换 `ctx.bash`，自管 spawn 收集**原始字节**，自动检测 UTF-16LE / UTF-8 / GBK 等编码并正确解码，修复 Windows/WSL 下 bash 工具的中文乱码。

## ✨ 核心特性

- **缝合线改名**：0.1.0 npm 线将 bash 能力从 `ctx.bash`/`@deepseek-ai/dsh-bash` 整体迁移到 `ctx.shell`/`@deepseek-ai/dsh-shell`——`dsh-tool-bash` 现在消费 `ctx.shell`（`resolve`/`run`/
- **依赖改名**：peer/devDependencies 由 `cordis`/`schemastery`/`@deepseek-ai/dsh-bash` 迁移为 `@deepseek-ai/cordis`/`@deepseek-ai/schemastery`/`@deepseek-ai/dsh-shell`（与官方
- **接入方式变化**：同一 context 只允许一个 `ctx.shell` provider。POSIX/WSL profile 下需**替换** `@deepseek-ai/dsh-bash-local`（而不是旧版的停用 `bash-sandbox`）；Windows 原生 profile 的 provider
- **验证**：DSH npm `0.1.1-rc.1` 基线 typecheck、构建、26 例单元测试（25 通过 + 1 例本机 WSL 代理警告环境噪音）与 0.1.0-rc.8 之前基线一致；运行加载验证见下节

## 📦 安装

```bash
# 在插件目录安装依赖（DSH 需要 Node ^22.19 || >=24）
cd /path/to/dsh-bash-encoding && pnpm install && pnpm build
```

## 🚀 快速开始

```bash
cd "${DSH_HOME:-$HOME/.dsh}/profiles/web"
pnpm add -w link:/path/to/dsh-bash-encoding
```

## 📚 更多信息

**Windows 原生 profile 停用说明**

在 **Windows 原生（无 WSL）profile** 下，本插件默认**停用**（`cordis.patch.yml` 注释段），原因： 需要时（POSIX/WSL profile，或显式替换 `dsh-bash-local`）按下方「安装」节接入即可——这是 profile 配置层的停用决定，不是代码弃用。

**使用环境（重点）**

本插件解决的是 **Windows + WSL 组合下的中文乱码**，典型触发条件： 当以上条件同时满足时，**每次执行 bash 命令**，`wsl.exe` 启动器都会向 stderr 输出一条 **UTF-16LE 编码**的代理警告，而 DSH 核心以 UTF-8 有损解码 → 必现乱码（见下方对比 1）。 > 附带修复的场景：任何输出非 UTF-8 字节的程序（GBK 中文工具、UTF-16 输出等）， > 以及 UTF-16LE 警告与命令自身 UTF-8 输出**混合在同一管道**的情况（最棘手，见对比 2/3）。

**在插件目录安装依赖（DSH 需要 Node ^22.19 || >=24）**

cd /path/to/dsh-bash-encoding && pnpm install && pnpm build 将插件接入 DSH web profile（与 `dsh-shell-windows` 等外部插件同样的方式）： cd "${DSH_HOME:-$HOME/.dsh}/profiles/web" pnpm add -w link:/path/to/dsh-bash-encoding

**配置**

在 profile 的 `cordis.yml`（或 `cordis.patch.yml`）中**替换** shell 条目 （`@deepseek-ai/dsh-bash-local` 被本插件替代——v0.2.0 起本插件与 `dsh-bash-local` 都注册 `ctx.shell`，同一 context 只能有一个 provider）：

## 🔗 链接

- [GitHub 仓库](https://github.com/lhh010/dsh-bash-encoding)
- [完整 README](https://github.com/lhh010/dsh-bash-encoding#readme)
- [返回dsh-bash-encoding所在分类](../plugins.md)
