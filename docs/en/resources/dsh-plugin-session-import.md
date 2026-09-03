---
title: "dsh-plugin-session-import"
description: "DeepSeek Harness plugin: import claude-code / codex / reasonix / zcode sessions"
keywords: "dsh-plugin-session-import, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-session-import

> ⭐ **6** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [huguangyu666](https://github.com/huguangyu666) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> DeepSeek Harness plugin: import claude-code / codex / reasonix / zcode sessions

## About

DeepSeek Harness（dsh）插件：把 **claude-code / codex / reasonix / zcode** 的历史聊天记录导入为 dsh 会话（含工作区绑定与工具能力），导入后可直接续聊。

## ✨ Key Features

- **四种工具解析**：
- **会话发现**：标题 / 项目名 / 消息数 / 时间齐全，30s 缓存扫描
- **搜索**：按标题 / 项目名过滤（防抖输入）
- **批量导入**：多选会话一次导入，每个会话独立 seed + 工作区绑定
- **工具完整可用**：导入会话自动加入默认 preset scope，25+ 工具（read/edit/glob/grep/pwsh 等）与正常会话一致
- **超长会话保护**：三层保障（内容裁剪 → 消息截断 → 单条兜底），任何长度 / 任何模型窗口都不超限
- **Web UI**：侧边栏「⇩ 导入会话」按钮（明暗主题自适应），导入成功自动关闭
- **命令**：`/import <tool> <path>`（文件或目录批量）

## 📦 Install

```bash
# 装进 web profile（自动 reconcile dsh.profile.bundles）
dsh plugin --profile web add dsh-plugin-session-import
dsh web   # 重启生效
```

## 🚀 Quick Start

```bash
# 1. 安装插件包
npm i dsh-plugin-session-import

# 2. 在 profile 挂载（~/.dsh/profiles/web/cordis.patch.yml）：
# - insert:
#     - id: session-import
#       name: 'dsh-plugin-session-import'

# 3. 重启 dsh web
dsh web
```

## 🔗 Links

- [GitHub Repository](https://github.com/huguangyu666/dsh-plugin-session-import)
- [Full README](https://github.com/huguangyu666/dsh-plugin-session-import#readme)
- [Back to the Plugins list](../plugins.md)
