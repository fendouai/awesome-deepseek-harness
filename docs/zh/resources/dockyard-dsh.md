---
title: "dockyard-dsh"
description: "A macOS-only native account-pool and provider plugin for DeepSeek Harness."
keywords: "dockyard-dsh, vision, plugin, coding, deepseek harness, dsh"
---
# dockyard-dsh

> ⭐ **73** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 73 | 状态 | ✅ 活跃 |
| 作者 | [AITabby](https://github.com/AITabby) | 更新时间 | 2026-08-17 |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> A macOS-only native account-pool and provider plugin for DeepSeek Harness.

## 详细介绍

**A native account-pool and provider plugin for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`).** [中文](#中文) · [English](#english)

## ✨ 核心特性

- 在 DSH 内使用 `/dockyard` 命令管理账号和 provider。
- 点击“登录添加账号”直接打开 provider 官方浏览器授权页，选择账号并安全导入账号池；provider 不可用时保留 CLI fallback。
- 扫描本机已有的官方登录态；扫描和新增账号是两个独立操作，已有账号不会被“新增”静默重复导入。
- 支持手动选择、sticky session、round-robin 和 failover 账号池策略。
- 读取 provider 返回的实时模型目录、推理档位、套餐和额度窗口。
- 所有命令、模型选择和 LLM 生成都读取同一个 Dockyard runtime，不维护第二套账号池或额度缓存。

## 📦 安装

```bash
# DSH 当前是 developer preview；请使用上游要求的 Node.js 版本。
# 当前上游 package.json 要求 Node 22.19+ 的 22.x，或 Node 24+。
npm install --global @deepseek-ai/dsh
npm install --global pnpm

dsh --version
pnpm --version
```

## 🚀 快速开始

```bash
dsh plugin --profile web add github:AITabby/dockyard-dsh
dsh web
```

## 📚 更多信息

**一条命令安装 Dockyard plugin**

如果已经有 Node.js，直接把下面这一行交给终端或智能体执行即可： npx -y @dockyard-dsh/install@latest 它会自动检查 DSH 和 pnpm，并把预构建的 Dockyard host/client bundle 安装到默认 `web` profile。安装完成后重启 DSH Web。

**从源码安装 Dockyard plugin / Web profile**

Dockyard DSH 作为源码 plugin 安装到已有 DSH Web profile 时，才需要先安装 DSH CLI，并确认 `dsh` 命令可用。 当前上游 DSH CLI 的 npm 安装方式：

**最简便的方式：直接安装到 DSH Web profile**

`web` 是 DSH 自带的完整 Web profile；不要新建只包含 Dockyard bundle 的空 profile，否则不会启动 Web GUI。 dsh plugin --profile web add github:AITabby/dockyard-dsh dsh web 默认访问 `http://127.0.0.1:3080`。首次启动可先检查组合配置： dsh web --dump-config 如需固定版本，建议 pin 到已验证的 commit： dsh plugin --profile web add github:AITabby/dockyard-dsh#<commit-sha> 当前发布 commit 已提交可运行的 host/client bundle，安装时不执行 `prepare`，因此 GitHub 直装不需要额外的 `allowBuilds` 配置

**需要本地修改时：克隆后安装**

git clone https://github.com/AITabby/dockyard-dsh.git cd dockyard-dsh npm install npm test # 可选：验证环境 npm run build # 修改 source 或 bundle 过期时需要 dsh plugin --profile web add . dsh web 要隔离测试、不影响默认 DSH home： DSH_HOME=/tmp/dockyard-dsh-home dsh plugin --profile web add . DSH_HOME=/tmp/dockyard-dsh-home dsh web --dump-config DSH_HOME=/tmp/dockyard-dsh-home dsh web 仓库已提交 `packages/dsh-plugin/dist/index.mj

## 🔗 链接

- [GitHub 仓库](https://github.com/AITabby/dockyard-dsh)
- [完整 README](https://github.com/AITabby/dockyard-dsh#readme)
- [返回dockyard-dsh所在分类](../plugins.md)
