---
title: "dsh-group-photo"
description: "DSH 内测收官合影墙：GitHub OAuth 零权限登录 + 冻结白名单校验的拍立得合影站（含 DSH Skill 包装）"
keywords: "dsh-group-photo, fun, plugin, coding, git, deepseek harness, dsh"
---
# dsh-group-photo

> ⭐ **17** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 娱乐与生活 |
| 星数 | ⭐ 17 | 状态 | ✅ 活跃 |
| 作者 | [SenmuuuuW](https://github.com/SenmuuuuW) | 更新时间 | 2026-08-14 |

## 一句话介绍

> DSH 内测收官合影墙：GitHub OAuth 零权限登录 + 冻结白名单校验的拍立得合影站（含 DSH Skill 包装）

## 详细介绍

**收官之夜，来合影 👉 https://rio-palm-cfr-benz.trycloudflare.com/** （活动期间在线；仅 dsh-external 内测成员可入镜。地址为活动期临时隧道，永久纪念版见 [`archive/index.html`](archive/index.html)） ---

## ✨ 核心特性

- 📸 拍立得合影墙：头像卡片 + `NO.xxx` 编号 + 留言 + 入镜时间，实时更新、彩带庆祝、移动端适配
- 🔐 零权限 OAuth：授权页不申请任何 scope，登录只用于证明"你是你"
- 🧊 冻结白名单：资格名单是内测私有期的快照，组织公开化 / 成员变动均不影响
- 🔒 浏览同样上锁：合影数据接口需登录会话，未登录只能看到人数
- 📦 零依赖：纯 Node 内置模块 + 原生 HTML/CSS/JS，无构建步骤
- 🗃️ 一键导出静态纪念版（`archive/index.html`），永久保存、任意静态托管
- 🏷️ 成员卡自动展示其在 dsh-external 组织的**代表作仓库**（`works.json`，由仓库首笔 commit 作者映射）

## 🚀 快速开始

```bash
# 1. 在 GitHub 创建 OAuth App，回调地址填 http://localhost:8808/auth/callback
# 2. 环境变量注入密钥（绝不放仓库）
GH_CLIENT_ID=xxx GH_CLIENT_SECRET=xxx GH_ORG=dsh-external npm start
# 3. 打开 http://localhost:8808
```

## 📚 更多信息

**3. 配置密钥（环境变量或 config.json 二选一）**

export GH_CLIENT_ID=你的ClientID export GH_CLIENT_SECRET=你的ClientSecret export GH_ORG=dsh-external

**把拥有 read:org 权限的 classic PAT 写进 config.json 的 pat 字段（或 GH_PA**

node freeze-whitelist.js # → 生成/更新 whitelist.json，用完后立刻 revoke PAT 服务端运行时不使用 PAT；`whitelist.json` 按 mtime 热加载，重新冻结无需重启。

**隐私说明**

本仓库为**公开安全版**：`members.json` / `whitelist.json` / `works.json` / `archive/index.html` 均为**演示数据**（虚构成员）。 真实数据（内测成员名单、合影留言）由活动维护者存放在**私有数据层**（如 `SenmuuuuW/dsh-group-photo-data`），通过文件挂载或环境变量（`GH_WHITELIST_FILE` / `GH_DATA_FILE` / `GH_WORKS_FILE`）注入运行环境：

## 🔗 链接

- [GitHub 仓库](https://github.com/SenmuuuuW/dsh-group-photo)
- [完整 README](https://github.com/SenmuuuuW/dsh-group-photo#readme)
- [返回dsh-group-photo所在分类](../plugins.md)
