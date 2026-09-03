---
title: "deepseek-harness-desktop"
description: "DSH 桌面应用打包器"
keywords: "deepseek-harness-desktop, desktop, client, coding, deepseek harness, dsh"
---
# deepseek-harness-desktop

> ⭐ **8** · ✅ 活跃 · 客户端

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 8 | 状态 | ✅ 活跃 |
| 作者 | [omdsh-dev](https://github.com/omdsh-dev) | 更新时间 | 2026-08-21 |

## 一句话介绍

> DSH 桌面应用打包器

## 详细介绍

把 [@deepseek-ai/dsh](https://www.npmjs.com/package/@deepseek-ai/dsh) 的 `--profile web` 与 `cordis.patch.yml` 打包为**独立自定义桌面**的 Go 单命令。 支持 macOS、Linux 与 Windows。

## ✨ 核心特性

- `dev [<workspace>]` — 基于工作区直接起 `dsh web` 并打开浏览器页面
- `bundle <workspace>` — 打包为平台应用。产物按输入指纹内容寻址缓存于
- `plugin add <package...>` — 代理 `dsh plugin add`：在工作区跑 `pnpm add`，

## 📦 安装

```bash
dsh-web-desktopify dev examples/custom        # 基于工作区起 dsh web 并打开浏览器
dsh-web-desktopify bundle examples/custom     # 打包当前平台的应用（基于工作区 hash 增量）
dsh-web-desktopify bundle --force examples/custom      # 忽略缓存，全新打包
dsh-web-desktopify bundle --install examples/custom    # 打包并安装到当前平台
cd examples/custom && dsh-web-desktopify plugin add @foo/bar   # 向工作区加插件（代理 dsh plugin add）
```

## 🚀 快速开始

```bash
just test        # go test ./...（并发代码用 go test -race 验证）
just install     # go install ./cmd/dsh-web-desktopify
just dep         # go mod tidy
just custom::dev     # examples/custom 起 dsh web（go tool dsh-web-desktopify dev）
just custom::bundle  # examples/custom 打包（go tool dsh-web-desktopify bundle）
```

## 📚 更多信息

**Quick Start**

go install github.com/omdsh-dev/dsh-web-desktopify/cmd/dsh-web-desktopify@latest 创建你的工作区（复制本仓库 [examples/custom](examples/custom) 即可起步）， 然后： dsh-web-desktopify dev examples/custom # 基于工作区起 dsh web 并打开浏览器 dsh-web-desktopify bundle examples/custom # 打包当前平台的应用（基于工作区 hash 增量） dsh-web-desktopify bundle --force examples/custom # 忽略缓存，全新打包 dsh-web-desktopify bundle --install examples/custom # 打包并安装到当前平台 

## 🔗 链接

- [GitHub 仓库](https://github.com/omdsh-dev/deepseek-harness-desktop)
- [完整 README](https://github.com/omdsh-dev/deepseek-harness-desktop#readme)
- [返回deepseek-harness-desktop所在分类](../clients.md)
