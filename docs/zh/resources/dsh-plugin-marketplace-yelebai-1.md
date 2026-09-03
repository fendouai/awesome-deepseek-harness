---
title: "dsh-plugin-marketplace"
description: "Verified plugin marketplace and autonomous registry for DeepSeek Harness"
keywords: "dsh-plugin-marketplace, registry, awesome-list, coding, deepseek harness, dsh"
---
# dsh-plugin-marketplace

> ⭐ **20** · ✅ 活跃 · 精选列表 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 精选列表 | 分类 | 注册表 |
| 星数 | ⭐ 20 | 状态 | ✅ 活跃 |
| 作者 | [YELEBAI](https://github.com/YELEBAI) | 更新时间 | 2026-08-21 |

## 一句话介绍

> Verified plugin marketplace and autonomous registry for DeepSeek Harness

## 详细介绍

**经过验证的 DSH 插件市场，以及自主维护的中心 Registry。** **简体中文** · [English](./README.en.md) · [更新日志](./CHANGELOG.md)

## 📦 安装

```bash
dsh plugin --profile web add github:YELEBAI/dsh-plugin-marketplace#v0.9.4
```

## 🚀 快速开始

```bash
dsh plugin --profile web add D:/path/to/dsh_Market
```

## 📚 更多信息

**1. 安装**

dsh plugin --profile web add github:YELEBAI/dsh-plugin-marketplace#v0.9.4 本地开发安装： dsh plugin --profile web add D:/path/to/dsh_Market

**安装模式**

自动安装始终使用 Registry 验证过的精确 GitHub commit 或精确 npm 版本，不会把可变的 `main`、`latest` 或 Release 下载地址直接交给包管理器。

**手动命令安装**

在 **管理与诊断 → 手动命令安装** 中可以粘贴： dsh plugin --profile web add github:owner/repo#ref 也可以只填写 `github:owner/repo#ref`。输入内容不会交给 Shell；市场只接受当前 Profile 的 单条 GitHub 安装命令，并拒绝额外参数、管道、多命令和危险 ref。tag、分支或省略的 ref 会先解析为精确 commit，随后验证 `package.json`、bundle patch 和冲突。安装过程禁用生命周期 脚本；未安装的包会加入 Profile 的 bundle 层，已安装的同名包则按该精确来源更新。

**引导安装 Agent**

仍处于引导安装的插件会显示 **Agent 安装**；已安装插件存在引导型更新时，会显示 **Agent 更新**。 Agent 任务会固定以下上下文： 每个引导任务的第一步都会加载插件内置的 `install-dsh-plugin` Skill。Skill 优先选择最快的 安全路径：已有完整运行产物时使用精确 commit 并禁用脚本；缺少产物时在临时目录隔离构建； Release tarball 无可信摘要、包身份不一致、Bundle/入口缺失或出现冲突时直接停止。内置的只读 检查器会同时核验 Git HEAD、包名、版本、Bundle patch、Host/Client 入口、生命周期脚本及当前 Profile 的 Bundle ID/Cordis 服务冲突。 Agent 会先只读检查精确 commit。执行安装、构建、`prepare`、`postinstall` 等第三方代码前，

## 🔗 链接

- [GitHub 仓库](https://github.com/YELEBAI/dsh-plugin-marketplace)
- [完整 README](https://github.com/YELEBAI/dsh-plugin-marketplace#readme)
- [返回dsh-plugin-marketplace所在分类](../awesome-lists.md)
