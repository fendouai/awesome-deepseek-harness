---
title: "dsh-git-identity"
description: "DSH 插件：git 提交固定使用环境自身作者身份（优先 gh CLI 登录账号，GitHub noreply 邮箱），GIT_AUTHOR_*/GIT_COMMITTER_* 环境变量注入压过一切 git config"
keywords: "dsh-git-identity, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-git-identity

> ⭐ 7 · ✅ 活跃 · 插件

## 一句话介绍

DSH 插件：git 提交固定使用环境自身作者身份（优先 gh CLI 登录账号，GitHub noreply 邮箱），GIT_AUTHOR_*/GIT_COMMITTER_* 环境变量注入压过一切 git config

## 详细介绍

DSH **profile bundle**（0812+ 的官方插件系统）：让 DSH 内产生的所有 git 提交使用 环境自身的作者身份。优先读取 gh CLI 的登录账号（name 取 login，email 取 GitHub noreply 地址 `<id>+<login>@users.noreply.github.com`），其次启动环境的 `GIT_AUTHOR_*`、`git config --global` 兜底。

## 作者
**[LoserFox](https://github.com/LoserFox)**

## 链接

- [GitHub 仓库](https://github.com/LoserFox/dsh-git-identity)
- [完整 README](https://github.com/LoserFox/dsh-git-identity#readme)
- [返回dsh-git-identity所在分类](../plugins.md)
