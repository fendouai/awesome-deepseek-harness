---
title: "dsh-file-claim"
description: "并行 Agent 会话的文件归属/认领系统：认领/释放、心跳过期接管、异步三路合并。"
keywords: "dsh-file-claim, developer, plugin, files, multi-agent, git, deepseek harness, dsh"
---
# dsh-file-claim

> ⭐ 3 · ✅ 活跃 · 插件

## 一句话介绍

并行 Agent 会话的文件归属/认领系统：认领/释放、心跳过期接管、异步三路合并。

## 详细介绍

When several DSH sessions run in parallel against one workspace, they have no awareness of each other: two sessions can overwrite the same file, a crashed session leaves stale state behind, and a session that wants to edit a file another session owns can only wait or guess. `dsh-file-claim` turns a proven coordination protocol into native DSH tools, lifecycle events, and a write guard — so parallel agents cooperate instead of clobbering each other. claim_files({ paths: ["README.md"] }) # "I'm ed

## 作者
**[Nwflower](https://github.com/Nwflower)**

## 链接

- [GitHub 仓库](https://github.com/Nwflower/dsh-file-claim)
- [完整 README](https://github.com/Nwflower/dsh-file-claim#readme)
- [返回dsh-file-claim所在分类](../plugins.md)
