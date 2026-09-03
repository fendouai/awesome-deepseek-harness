---
title: "dsh-archive-viewer"
description: "DeepSeek Harness 归档会话管理插件：查看/恢复已归档会话（回到原工作区分组）+ 右上角一键关闭 dsh。MIT 许可，欢迎收录到任何插件合集，注明出处即可。"
keywords: "dsh-archive-viewer, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-archive-viewer

> ⭐ **4** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [keepermttl](https://github.com/keepermttl) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> DeepSeek Harness 归档会话管理插件：查看/恢复已归档会话（回到原工作区分组）+ 右上角一键关闭 dsh。MIT 许可，欢迎收录到任何插件合集，注明出处即可。

## About

DeepSeek Harness（DSH）Web GUI 的归档会话管理插件：**查看 / 恢复已归档会话**，外加右上角**一键关闭 dsh**。 English: [README.en.md](README.en.md) · 更新日志: [CHANGELOG.md](CHANGELOG.md)

## ✨ Key Features

- **侧边栏插件栏入口「已归档会话」**（设置按钮上方）：列出全部归档会话——标题、最后活跃时间、所属工作区、运行中/空白状态
- **关键词搜索**：输入即筛（标题 / 会话 ID / 工作区，不区分大小写）；开启「内容」模式后还会逐页扫描每段会话最近的对话（每会话扫描页数可在设置中调整，扫描进度实时显示）
- **排序 + 筛选**：按最近更新 / 名称 / 会话 ID 排序，升序/降序一键切换；标签筛选收纳在「筛选」按钮菜单内，支持多选、AND / OR 模式与标签搜索，和关键词搜索叠加
- **归档会话标签**：用户可给每个归档会话添加/删除自定义标签；标签持久化在 DSH profile 目录，由 host 半区提供本地 HTTP API 读写
- **内嵌 AI 助手**：面板底部可折叠小窗口，直接调用 DSH 标准模式（默认 `standard`，可在设置改为其他 agent preset）驱动真实 agent，帮助检索会话、添加标签、整理归档；对话中的代码块/超长文本自动折叠
- **AI 助手会话自动隐藏**：AI 助手使用的会话会自动归档为内部 helper 会话，不出现在侧边栏和归档面板；「新对话」会安全删除上一个 helper 会话，不会误删用户会话
- **AI 工作区**：AI 助手会话默认在 `E:\dsh-ai-workspace` 下创建，可在设置中修改
- **隐藏临时检索标签**：agent 检索命中后自动给会话添加隐藏标签「agent检索」并切到对应筛选；该标签不显示在会话徽章上，取消勾选后自动清除

## 📦 Install

```bash
git clone https://github.com/keepermttl/dsh-archive-viewer.git
cd dsh-archive-viewer
pnpm install
pnpm build

# 安装进 web profile（link: 指向本目录）
dsh plugin --profile web add link:$(pwd)        # POSIX
dsh plugin --profile web add link:E:\path\to\dsh-archive-viewer   # Windows
```

## 🚀 Quick Start

```bash
cd <你的 deepseek-harness 检出目录>
git apply /path/to/dsh-archive-viewer/patches/0001-workspace-unarchive-and-host-shutdown-rpcs.patch
```

## 📚 Learn more

**安装**

前置：Node.js >= 22、pnpm。 git clone https://github.com/keepermttl/dsh-archive-viewer.git cd dsh-archive-viewer pnpm install pnpm build

**安装进 web profile（link: 指向本目录）**

dsh plugin --profile web add link:$(pwd) # POSIX dsh plugin --profile web add link:E:\path\to\dsh-archive-viewer # Windows 重启 `dsh web`，浏览器 **Ctrl+F5** 硬刷新。 > 从旧版本升级后，请务必**重启 `dsh web`**：本版本 host 半区新增了标签存储与 `/api/archive-viewer/tags` 本地 API，仅刷新浏览器无法加载 host 侧变更。

**使用**

1. 侧边栏底部（设置按钮上方）点击「已归档会话」打开面板 2. 搜索框输入关键词即时过滤；点击「内容」可同时搜索对话内容（设置里可调整每会话扫描页数） 3. 工具栏选择排序方式（最近更新 / 名称 / ID）与升/降序；点击「筛选」按钮打开标签筛选菜单，可按标签多选（AND / OR）、搜索标签或开启「Agent 检索」 4. 齿轮按钮打开设置：语言、排序、排列、搜索、AI 模式、AI 模型与思考强度、标签筛选模式、介绍文本显隐、恢复默认 5. 每个会话行：**查看对话 / 恢复会话 / 下载日志 (ZIP) / 复制 ID / 标签** 6. 面板底部「AI 助手」小窗口：直接和 DSH agent 对话，让它检索会话、添加标签或整理归档；agent 可通过标签 API 操作标签；代码块/长文本会自动折叠；AI 会话自动隐藏，点「新对话」会删除上一个 AI 会话 7. 会话头部**右上

**许可与使用声明**

**MIT License**（见 [LICENSE](LICENSE)）。 欢迎任何人**使用、修改、引用、或把本项目收录进自己的插件合集**（如 dsh-web-ui 全家桶），只需：

## 🔗 Links

- [GitHub Repository](https://github.com/keepermttl/dsh-archive-viewer)
- [Full README](https://github.com/keepermttl/dsh-archive-viewer#readme)
- [Back to the Plugins list](../plugins.md)
