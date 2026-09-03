---
title: "dsh-git-graph"
description: "Embedded git repository graph visualizer for the DeepSeek Harness Web GUI | 嵌入式 Git 仓库图谱可视化插件（提交历史图 / 分支过滤 / 文件 diff / VSCode 式未提交改动）"
keywords: "dsh-git-graph, ide, integration, coding, git, ui, deepseek harness, dsh"
---
# dsh-git-graph

> ⭐ **13** · ✅ 活跃 · 集成 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | IDE 与编辑器 |
| 星数 | ⭐ 13 | 状态 | ✅ 活跃 |
| 作者 | [1841220388zzzcccxxx-star](https://github.com/1841220388zzzcccxxx-star) | 更新时间 | 2026-08-19 |

## 一句话介绍

> Embedded git repository graph visualizer for the DeepSeek Harness Web GUI | 嵌入式 Git 仓库图谱可视化插件（提交历史图 / 分支过滤 / 文件 diff / VSCode 式未提交改动）

## 详细介绍

🌏 中文 · [English](./README_EN.md) DeepSeek Harness（DSH）Web GUI 的嵌入式 Git 仓库图谱可视化插件。 在对话界面里直接查看、浏览、管理 git 仓库：提交历史图、分支过滤、提交详情、文件 diff、工作区状态、右键 git 操作，全部内嵌在 harness 界面中，无需离开当前对话。提交图一目了然，未提交改动像 VSCode 一样分组展示，一眼看清"改了什么、谁改的、要不要提交"。 **适合谁**：用 DeepSeek Harness / DSH 做 AI 编程、Agent 开发的开发者；想在同一个界面里同时看清提交历史、分支、工作区改动的 Git 用户；需要比命令行更直观的 Git 可视化工具的开发者与团队。

## ✨ 核心特性

- **提交历史图**：GitHub 风格提交列表，分支分组折叠、分支着色（本地与远程分支各有独立分组）
- **跟随当前对话**：打开哪个对话就显示哪个对话工作区的 git 仓库，切换对话自动跟随；非 git 仓库的对话显示空态提示
- **📂 打开文件夹（v0.11）**：不局限于当前对话工作区——点击顶栏「打开」或在空态中点「打开文件夹」，可浏览磁盘（驱动器 → 目录逐层进入，带 git 标记），选择任意文件夹（如另一个工作区的仓库 B）查看其版本管理；添加过的仓库持久保存，顶部下拉随时切换，刷新后仍可继续查看
- **分支过滤**：勾选 = 显示该分支 · 不勾 = 完全隐藏（全部不勾选则列表为空）
- **提交详情**：提交信息、文件变更列表、单文件 diff、两次提交对比（Ctrl+点击）、📜 文件历史（查看单个文件的所有历史提交）
- **未提交改动（VSCode 风格，常驻图谱顶部）**：已暂存 / 更改 / 未跟踪三组文件列表、状态徽标（A/M/D/R/U/?）、每文件 +/− 行数、点击行展开单文件 diff（语法高亮）、重命名 `旧 → 新`、未跟踪文件直接显示内容；☑ 分组开关可单独隐藏某组，面板与分组均可点击折叠；**每行可 暂存/取消暂
- **右键菜单**：复制哈希/消息、查看详情、🏷️ 打标签（可改名/删除）、🌿 从提交新建分支、🌐 打开 GitHub 提交页、复制仓库路径、在文件管理器中打开
- **远程/分支操作**：顶栏 `⬇ 拉取`（git fetch）与 `⬆ 推送`（git push 当前分支，确认后执行）；分支组头右键——本地分支可 🔄 切换 / ⬆ 推送 / 🗑️ 删除（已合并才可删，HEAD 受保护），远程分支可 ⬇ 拉取 / 复制远程分支名

## 📦 安装

```bash
pnpm install
# 然后重启 dsh web（或直接使用一键重启脚本）
```

## 🚀 快速开始

```bash
git-graph/
├── index.js          # 服务端：git API（graph/branches/workstatus/workfile/diff/...）
├── client.js         # 客户端插件：会话页「Git 图谱」标签
├── web/index.html    # 图谱界面（iframe 内独立页面）
├── package.json      # 插件清单（dsh.client.inject + bundle patch）
└── cordis.patch.yml  # profile 挂载点
```

## 🔗 链接

- [GitHub 仓库](https://github.com/1841220388zzzcccxxx-star/dsh-git-graph)
- [完整 README](https://github.com/1841220388zzzcccxxx-star/dsh-git-graph#readme)
- [返回dsh-git-graph所在分类](../integrations.md)
