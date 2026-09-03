---
title: "dsh-git-identity"
description: "DSH 插件：git 提交固定使用环境自身作者身份（优先 gh CLI 登录账号，GitHub noreply 邮箱），GIT_AUTHOR_*/GIT_COMMITTER_* 环境变量注入压过一切 git config"
keywords: "dsh-git-identity, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-git-identity

> ⭐ **7** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 7 | 状态 | ✅ 活跃 |
| 作者 | [LoserFox](https://github.com/LoserFox) | 更新时间 | 2026-08-13 |
| 子分类 | 🧪 代码·测试·审查 | 能力 | coding |

## 一句话介绍

> DSH 插件：git 提交固定使用环境自身作者身份（优先 gh CLI 登录账号，GitHub noreply 邮箱），GIT_AUTHOR_*/GIT_COMMITTER_* 环境变量注入压过一切 git config

## 详细介绍

DSH **profile bundle**（0812+ 的官方插件系统）：让 DSH 内产生的所有 git 提交使用 环境自身的作者身份。优先读取 gh CLI 的登录账号（name 取 login，email 取 GitHub noreply 地址 `+@users.noreply.github.com`），其次启动环境的 `GIT_AUTHOR_*`、`git config --global` 兜底。

## 📦 安装

```bash
# 从本仓库 checkout 安装到 profile（web / headless 等），bundle 声明自动加入组合层
dsh plugin --profile web add /path/to/dsh-git-identity
dsh plugin --profile headless add /path/to/dsh-git-identity
# 验证
dsh --profile web --dump-config | grep git-identity
```

## 🚀 快速开始

```bash
# 在 bundle 的 patch 里给行加 config（可选；不配置则按上述优先级自动解析）
- insert:
    - id: git-identity
      name: '@loserfox/git-identity'
      config:
        name: LoserFox
        email: 57448027+LoserFox@users.noreply.github.com
```

## 📚 更多信息

**从本仓库 checkout 安装到 profile（web / headless 等），bundle 声明自动加入组合层**

dsh plugin --profile web add /path/to/dsh-git-identity dsh plugin --profile headless add /path/to/dsh-git-identity

**在 bundle 的 patch 里给行加 config（可选；不配置则按上述优先级自动解析）**

- id: git-identity name: '@loserfox/git-identity' config: name: LoserFox email: 57448027+LoserFox@users.noreply.github.com

## 🔗 链接

- [GitHub 仓库](https://github.com/LoserFox/dsh-git-identity)
- [完整 README](https://github.com/LoserFox/dsh-git-identity#readme)
- [返回dsh-git-identity所在分类](../plugins.md)
