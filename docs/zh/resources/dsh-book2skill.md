---
title: "dsh-book2skill"
description: "书转技能插件：获取→解析→理解→生成→安装的五阶段长任务。"
keywords: "dsh-book2skill, research, plugin, workflow, deepseek harness, dsh"
---
# dsh-book2skill

> ⭐ **4** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 研究 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [omdsh-dev](https://github.com/omdsh-dev) | 更新时间 | 2026-08-19 |

## 一句话介绍

> 书转技能插件：获取→解析→理解→生成→安装的五阶段长任务。

## 详细介绍

**Author / Maintainer:** [@Zacklinkk](https://github.com/Zacklinkk) 书籍转技能（Book → Skill）：DSH 插件包，把一个 5 阶段长任务工作流带进 DeepSeek Harness—— **获取书籍 → 解析分章 → 深度阅读 → 生成 SKILL.md → 安装**，中途有 **3 个人类门控**。 确定性步骤（EPUB 解析 / PDF 提取 / OCR / 安装复制）是宿主工具；理解与生成（浅读建地图、 设计方向问题、深读核心章、撰写 SKILL.md 与自检）由 agent 执行；浏览器面板负责 5 阶段时间线 展示与门控审批。任务状态存宿主存储域，**跨会话、跨重启可恢复，可随时取消**。

## 📦 安装

```bash
# 1. 用当前 DSH rc.3 npm 运行时链接类型依赖并完整验收
npm ci
DSH_NODE_MODULES_ROOT=/path/to/dsh-rc3/node_modules npm run setup:dsh-workspace
npm run typecheck
npm test
npm run build

# 2. 打包并通过插件命令安装到目标 profile
npm pack
dsh plugin --profile web add file:/absolute/path/dsh-book2skill-0.1.2.tgz

# 3. 重启 dsh web（宿主行需要进程重启），浏览器刷新后对话区出现「书籍转技能」标签
```

## 📚 更多信息

**2. 打包并通过插件命令安装到目标 profile**

npm pack dsh plugin --profile web add file:/absolute/path/dsh-book2skill-0.1.2.tgz

## 🔗 链接

- [GitHub 仓库](https://github.com/omdsh-dev/dsh-book2skill)
- [完整 README](https://github.com/omdsh-dev/dsh-book2skill#readme)
- [返回dsh-book2skill所在分类](../skills.md)
