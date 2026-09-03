---
title: "dsh-mermaid"
description: "在 DSH Web 会话中把 Mermaid 代码围栏渲染为 SVG 图表 | Render Mermaid code fences as SVG diagrams in DSH Web messages"
keywords: "dsh-mermaid, search, plugin, coding, deepseek harness, dsh"
---
# dsh-mermaid

> ⭐ **11** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 11 | 状态 | ✅ 活跃 |
| 作者 | [AKS1st](https://github.com/AKS1st) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding |

## 一句话介绍

> 在 DSH Web 会话中把 Mermaid 代码围栏渲染为 SVG 图表 | Render Mermaid code fences as SVG diagrams in DSH Web messages

## 详细介绍

[English](README.en.md) 在 DSH Web 会话消息中把 ` ```mermaid ` 代码围栏渲染为 SVG 图表的独立插件，通过 `dsh plugin` 安装进 web profile。

## ✨ 核心特性

- **Host 半部**（`src/index.ts`）：注册 `webServer` 前缀路由 `/mermaid-dist`，从插件自己的 `node_modules/mermaid` 惰性提供 UMD 构建，并提供固定的 `config.json` 端点。
- **Client 半部**（`src/client/`）：监听会话 DOM，把 infostring 为 `mermaid` 的围栏渲染为 SVG：

## 📦 安装

```bash
dsh plugin --profile web add github:AKS1st/dsh-mermaid
dsh web   # 重启 web 服务使 profile 生效
```

## 🚀 快速开始

```bash
npm install
npm run build
dsh plugin --profile web add .
dsh web
```

## 📚 更多信息

**安装**

从 GitHub 仓库安装（构建在 `prepare` 脚本里自动执行）： dsh plugin --profile web add github:AKS1st/dsh-mermaid dsh web # 重启 web 服务使 profile 生效 > 若 pnpm 提示 git 依赖需要执行构建脚本（`ERR_PNPM_GIT_DEP_PREPARE_NOT_ALLOWED`）， > 按提示把包加入 profile 的 `pnpm-workspace.yaml` 的 `allowBuilds` 后重试即可。 本地开发（先构建再安装）： npm install npm run build dsh plugin --profile web add . dsh web 卸载： dsh plugin --profile web remove dsh-mermaid

**配置**

组合包默认生效以下配置： - id: mermaid name: 'dsh-mermaid' config: theme: auto maxTextSize: 50000 maxEdges: 2000 securityLevel: strict 在 profile 的 `cordis.patch.yml` 里以 `- set:` 或 `- update:` 覆盖即可。

## 🔗 链接

- [GitHub 仓库](https://github.com/AKS1st/dsh-mermaid)
- [完整 README](https://github.com/AKS1st/dsh-mermaid#readme)
- [返回dsh-mermaid所在分类](../plugins.md)
