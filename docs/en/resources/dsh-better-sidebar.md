---
title: "DSH Better Sidebar"
description: "Workbench-style sidebar: file viewer/editor, terminal, Git, subagents and plugin-extensible tabs."
keywords: "DSH Better Sidebar, ui, plugin, files, terminal, git, deepseek harness, dsh"
---
# DSH Better Sidebar

> ⭐ **2,552** · ✅ active · plugin · ⬆️ +116 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 2,552 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | 2026-08-21 |
| Subcategory | 💡 Generative UI | Capabilities | ui, files, terminal, git |

## One-liner

> Workbench-style sidebar: file viewer/editor, terminal, Git, subagents and plugin-extensible tabs.

## About

一个服务化的侧边栏框架，一套开箱即用的完整工作台 右侧栏 + 底部面板双工作台，并把 ctx.betterSidebar 服务开放给所有插件—— 通过 registerTab / registerFileViewer 注册新的侧边栏页面与文件预览器。 🌏 中文 · English

## ✨ Key Features

- **🗂️ 文件工作台**：资源管理器（懒加载目录树；软链接按目标类型展示——目录软链接可展开、失效链接标红）+ CodeMirror 编辑器；图片 / Markdown（含 Mermaid 图表，strict 安全渲染 + 点击放大；README 级内嵌 HTML——徽章墙 / `<details>` 折叠 / 表格内
- **🌐 内嵌浏览器**：多开网页 tab，后退 / 前进 / 刷新；内容运行在沙箱 iframe；外链默认按协议分流——HTTP 在侧边栏打开、HTTPS 走系统浏览器（设置页可分别调整）
- **💻 真实终端**：xterm.js + node-pty 真实 shell，断线重连回放；可选为模型注入 `terminal_*` 工具
- **📂 模型侧边栏打开（可选）**：全局设置开启后注入 `sidebar_open` 工具——模型可主动在侧边栏打开文件 / 文件夹（树以该目录为根）/ HTTP(S) 网页
- **🌿 文件变动**：Git 视角（真 diff / 历史 / 暂存·提交·还原 / worktree·子仓库选择）与本轮文件视角（模型读 / 写 / 编辑实时追踪，按文件分组、按类型筛选）**双视角合一**；统一 diff 渲染（改蓝配对 + 行内字符级高亮 + 语法着色 + 上下文折叠），底部可拖拽预览面板，可一键
- **🧩 后台任务页**：subagent 拓扑 + 后台任务（退出码 / 实时输出 / 强制终止）
- **💬 侧边对话(beta)**：Codex 风格的侧边线程——继承主会话完整上下文（含进行中的回合与工具调用）独立运行，不进入主会话；线程内可持续追问，一键「保存为新会话」提升为顶层会话
- **🪟 双工作台**：右侧栏 + 底部面板；拖 Tab 拆分 / 合并分栏（可跨面板），移动端自动合并全宽抽屉

## 📦 Install

```bash
dsh plugin --profile web add dsh-better-sidebar@latest   # 首次会因 pnpm 11 拦截 node-pty 构建脚本而失败（依赖已写入）
cd ~/.dsh/profiles/web && pnpm approve-builds --all      # 放行构建脚本（自动重跑安装）
dsh plugin --profile web add dsh-better-sidebar@latest   # 重跑即成功
```

## 🚀 Quick Start

```bash
帮我安装 dsh-better-sidebar 插件（DSH 侧边栏工作台），步骤：
1. 执行 dsh plugin --profile web add dsh-better-sidebar@latest（首次会被 pnpm 11 拦截 node-pty 构建脚本而失败，属正常）
2. 在 ~/.dsh/profiles/web 下执行 pnpm approve-builds --all（放行构建脚本，会自动重跑安装）
3. 再次执行 dsh plugin --profile web add dsh-better-sidebar@latest
4. 完成后提醒我硬刷新浏览器（Cmd/Ctrl+Shift+R）
遇到报错先查 https://github.com/omdsh-dev/DSH-better-sidebar README 的常见问题表。
```

## 📚 Learn more

**🚀 安装**

**前置**：已装好 DSH（`dsh web` 能正常运行），Node.js ≥ 20、pnpm ≥ 10。 **支持的 DSH 版本**： <a href="https://www.npmjs.com/package/@deepseek-ai/dsh?activeTab=versions"></a> > 📌 **正式版**：`v0.18.0` 起适配 DSH **0.1.2-rc.1+**（npm dist-tag `latest`），不再支持 0.1.0-rc.8 ~ 0.1.1-rc.2——DSH stable（≤ 0.1.1-rc.2）用户请固定安装 `dsh-better-sidebar@0.17.1`（`@latest` 已由 v0.18.0 接管）；停留在 0.1.2-alpha.x 的宿主请先升级 DSH，或继续用 `dsh-better-sidebar@alpha`（v

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/DSH-better-sidebar)
- [Full README](https://github.com/omdsh-dev/DSH-better-sidebar#readme)
- [Back to the Plugins list](../plugins.md)
