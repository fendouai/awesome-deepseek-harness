---
title: "dsh-session-cleaner-cli"
description: "深度清理 DeepSeek Harness (DSH) 工作区会话的离线 CLI：按工作区列出/删除/恢复会话，自动同步工作区账目与投影缓存。Offline session cleaner for DeepSeek Harness: list, delete (trash+restore) and prune ghost sessions across workspaces."
keywords: "dsh-session-cleaner-cli, discovery, plugin, coding, deepseek harness, dsh"
---
# dsh-session-cleaner-cli

> ⭐ **0** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 插件发现 |
| 星数 | ⭐ 0 | 状态 | ✅ 活跃 |
| 作者 | [ChenChen913](https://github.com/ChenChen913) | 更新时间 | 2026-08-14 |

## 一句话介绍

> 深度清理 DeepSeek Harness (DSH) 工作区会话的离线 CLI：按工作区列出/删除/恢复会话，自动同步工作区账目与投影缓存。Offline session cleaner for DeepSeek Harness: list, delete (trash+restore) and prune ghost sessions across workspaces.

## 详细介绍

[English](README.en.md) **深度清理 DeepSeek Harness（DSH）工作区会话的离线 CLI 工具**：按工作区列出、勾选删除、回收站恢复，自动同步工作区账目与投影缓存。跨平台（Windows / macOS / Linux），零依赖。 ---

## 📦 安装

```bash
# 方式一：直接从 GitHub 用 npx 运行（无需克隆）
npx github:ChenChen913/dsh-session-cleaner-cli list

# 方式二：克隆
git clone https://github.com/ChenChen913/dsh-session-cleaner-cli.git
cd dsh-session-cleaner-cli
node dsh-session-cleaner.mjs
```

## 🚀 快速开始

```bash
~/.dsh/
  sessions/<工作区路径编码>/<会话id>/session.jsonl.zstd   ← 会话日志
  storages/workspace.json                                ← 工作区账目 + 归档集合
  storages/session_projcache.json                        ← 标题/统计投影缓存
```

## 📚 更多信息

**工作原理**

DSH 默认 JSONL 后端在磁盘上的形态： ~/.dsh/ sessions/<工作区路径编码>/<会话id>/session.jsonl.zstd ← 会话日志 storages/workspace.json ← 工作区账目 + 归档集合 storages/session_projcache.json ← 标题/统计投影缓存 删除一个会话 = 四步事务： 1. **备份**：两份账目复制到 `storages/backups/<时间戳>/` 2. **移入回收站**：日志目录 → `.dsh/trash/<时间戳>/<id>/`（`--purge` 直接删） 3. **同步账目**：从 `workspace.json` 的 `sessionIds` 与 `archivedSessionIds` 摘除该 id，盖上 `updatedAt` 4. **清理缓存**：删除 `session

## 🔗 链接

- [GitHub 仓库](https://github.com/ChenChen913/dsh-session-cleaner-cli)
- [完整 README](https://github.com/ChenChen913/dsh-session-cleaner-cli#readme)
- [返回dsh-session-cleaner-cli所在分类](../plugins.md)
