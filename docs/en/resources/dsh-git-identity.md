---
title: "dsh-git-identity"
description: "DSH 插件：git 提交固定使用环境自身作者身份（优先 gh CLI 登录账号，GitHub noreply 邮箱），GIT_AUTHOR_*/GIT_COMMITTER_* 环境变量注入压过一切 git config"
keywords: "dsh-git-identity, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-git-identity

> ⭐ **7** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 7 | Status | ✅ active |
| Author | [LoserFox](https://github.com/LoserFox) | Updated | 2026-08-13 |
| Subcategory | 🧪 Code, tests & review | Capabilities | coding |

## One-liner

> DSH 插件：git 提交固定使用环境自身作者身份（优先 gh CLI 登录账号，GitHub noreply 邮箱），GIT_AUTHOR_*/GIT_COMMITTER_* 环境变量注入压过一切 git config

## About

DSH **profile bundle**（0812+ 的官方插件系统）：让 DSH 内产生的所有 git 提交使用 环境自身的作者身份。优先读取 gh CLI 的登录账号（name 取 login，email 取 GitHub noreply 地址 `+@users.noreply.github.com`），其次启动环境的 `GIT_AUTHOR_*`、`git config --global` 兜底。

## 📦 Install

```bash
# 从本仓库 checkout 安装到 profile（web / headless 等），bundle 声明自动加入组合层
dsh plugin --profile web add /path/to/dsh-git-identity
dsh plugin --profile headless add /path/to/dsh-git-identity
# 验证
dsh --profile web --dump-config | grep git-identity
```

## 🚀 Quick Start

```bash
# 在 bundle 的 patch 里给行加 config（可选；不配置则按上述优先级自动解析）
- insert:
    - id: git-identity
      name: '@loserfox/git-identity'
      config:
        name: LoserFox
        email: 57448027+LoserFox@users.noreply.github.com
```

## 📚 Learn more

**从本仓库 checkout 安装到 profile（web / headless 等），bundle 声明自动加入组合层**

dsh plugin --profile web add /path/to/dsh-git-identity dsh plugin --profile headless add /path/to/dsh-git-identity

**在 bundle 的 patch 里给行加 config（可选；不配置则按上述优先级自动解析）**

- id: git-identity name: '@loserfox/git-identity' config: name: LoserFox email: 57448027+LoserFox@users.noreply.github.com

## 🔗 Links

- [GitHub Repository](https://github.com/LoserFox/dsh-git-identity)
- [Full README](https://github.com/LoserFox/dsh-git-identity#readme)
- [Back to the Plugins list](../plugins.md)
