---
title: "dsh-meow-memory"
description: "Cross-session memory plugin for DeepSeek Harness: seven-layer SQLite store (soul/user/project/fact/lesson/topic/rules), BM25 retrieval, per-window dream consolidation. 跨会话七层长期记忆插件。"
keywords: "dsh-meow-memory, registry, awesome-list, coding, memory, deepseek harness, dsh"
---
# dsh-meow-memory

> ⭐ **58** · ✅ 活跃 · 精选列表

| | | | |
|---|---|---|---|
| 类型 | 精选列表 | 分类 | 注册表 |
| 星数 | ⭐ 58 | 状态 | ✅ 活跃 |
| 作者 | [Phant0Meow](https://github.com/Phant0Meow) | 更新时间 | — |

## 一句话介绍

> Cross-session memory plugin for DeepSeek Harness: seven-layer SQLite store (soul/user/project/fact/lesson/topic/rules), BM25 retrieval, per-window dream consolidation. 跨会话七层长期记忆插件。

## 详细介绍

为 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（DSH）打造的跨会话记忆插件。 **核心理念**：每个工作区维护一份结构化记忆数据库（`.dsh-meow/memory.db`，基于 `node:sqlite`）。 静态记忆手册（数据总览 + 工具用法 + 写作准则）以固定 section 的形式放在 **system prompt** 里—— 文本恒定，因此不会破坏 LLM provider 的 KV/上下文缓存。动态内容（soul/user 全量、设计原则、 记忆导引）作为**第一条用户消息的前缀**注入，且首轮只注入长期记忆、不做关键词命中； 从第二轮起每条用户消息做关键词命中（top-2）。模型按需用 `memory_search` / `memory_project` 深入检索。每个窗口由自己的主 agent 在空闲时（"dream"）整理记忆 （本窗口建立 + 提取过的记忆），以窗口最后一次对话时间戳冻结其知识。

## ✨ 核心特性

- **七层记忆**（`soul` = AI 自身 / `user` = 用户基本信息与偏好 / `project` = 项目信息，
- **首轮注入（长期记忆块）**：第一条用户消息前注入固定格式
- **每消息关键词命中**：从第二条用户消息起，每条真实用户消息都检索
- **当前 project 锚定**：`memory_remember/search/update/project` 带 project 参数即锚定
- **缓存友好设计**：静态 `meow-memory:guide` section（order 130，紧随各 `tool:*` 说明之后）
- **压缩后重注入**：会话被压缩（手动 `/compact` 或 token 压力自动触发）后，下一个用户
- **工具集**：`memory_remember`（写入，必填 content/project/keywords/importance 且缺失报错引导重填，
- **记忆时间戳**（`updated_at` = 最后更新时间）：dream 封存或 `memory_update` 刷新时更新。

## 📦 安装

```bash
dsh plugin --profile web add github:Phant0Meow/dsh-meow-memory
```

## 🚀 快速开始

```bash
dsh plugin --profile web remove meow-memory
```

## 📚 更多信息

**✨ 功能特性**

含 `subcategory`（overview/structure/decisions/quotes/ops/todo）/ `fact` = 原子事实 / `lesson` = 教训与纠正 / `topic` = 进行中的讨论话题，带目标句 / `rules` = 设计原则与行为准则）。 每层一张 SQLite 表，UUID 带时间前缀，id 顺序即创建顺序。 `===== 长期记忆 =====` → `【关于你】`（soul 全量）→ `【关于user】`（user 全量）→ `【设计原则】`（全局 rules 且 importance≥2，少而精的命令式准则）→ `【记忆导引】` （用法说明 + 「用户的所有 project」动态列表，供 `memory_project` 选用）。 记忆作为独立 plugin snapshot 消息放在真实 user 消息之前，不改写用户 promp

**一键安装（推荐）**

dsh plugin --profile web add github:Phant0Meow/dsh-meow-memory 一条命令装完即生效：安装时自动编译（包内含 `prepare` 脚本），自动挂载，重启 `dsh web` 后新会话自动加载插件。 > pnpm ≥10 默认会阻止安装期的构建脚本：首次 `add` 可能失败并提示 `allowBuilds`，按提示把输出的键加进 profile 的 `pnpm-workspace.yaml` 后重跑即可。

**手动安装（开发者，任意 DSH 安装，无需 npm）**

1. 把本包复制（或软链）到 profile 的 `node_modules`： ```sh mkdir -p ~/.dsh/profiles/web/node_modules ln -s /path/to/meow-memory ~/.dsh/profiles/web/node_modules/meow-memory ``` （Windows：`New-Item -ItemType Junction ...` —— NTFS junction，无需管理员权限。） 2. 把 `meow-memory` 加进 profile `package.json` 的 `dsh.profile.bundles`（同上）。 3. 重启 `dsh web`。新会话自动加载插件。

**⚙️ 配置**

所有字段均可选（profile patch 或 `cordis.patch.yml`）： name: 'meow-memory' config: enabled: true # 总开关 projectDir: '.dsh-meow' # 记忆目录（相对工作区） promptLang: 'zh' # ⚠️ 首次使用建议显式配置（见下方说明） hitTopK: 2 # 每条用户消息关键词命中的条目数上限（fact/lesson/rules/topic） reflect: true # 连续 ≥reflectTurns 轮工具调用后自动反思 reflectTurns: 7 # 触发反思所需的连续工具轮数 dream: enabled: true idleMinutes: 180 # 窗口空闲 ≥180 分钟（3 小时）允许 dream suppressWindows: # 峰时抑制时段（按下方 

## 🔗 链接

- [GitHub 仓库](https://github.com/Phant0Meow/dsh-meow-memory)
- [完整 README](https://github.com/Phant0Meow/dsh-meow-memory#readme)
- [返回dsh-meow-memory所在分类](../awesome-lists.md)
