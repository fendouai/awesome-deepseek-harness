---
title: "dsh-plugin-workbench"
description: "VS Code-style workspace file explorer with editable preview for the DSH web GUI"
keywords: "dsh-plugin-workbench, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-plugin-workbench

> ⭐ **6** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [Pasumao](https://github.com/Pasumao) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, ui |

## One-liner

> VS Code-style workspace file explorer with editable preview for the DSH web GUI

## About

[**中文**](./README.md) | [English](./README.en.md) **能直接改文件的 VS Code 风格工作台**——不是只读预览：文件树 + 可编辑代码预览 （语法高亮、标签页、行号栏）+ 右键文件操作（新建 / 重命名 / 删除 / 复制 / 剪切 / 粘贴 / 在系统中打开 / 在资源管理器打开）+ 图片内联预览，每个工作区独立保存状态。 装上之后，DSH 网页就是一个轻量代码编辑器。 装完你会看到： - 左侧多出**文件树侧栏**（懒加载 + 2 秒自动刷新，每工作区独立展开状态）； - 消息里的 `@相对路径` 变成**可点击链接**，点开直接在工作台预览； - 把文件从左栏**拖进聊天区**，路径自动插入输入框。

## ✨ Key Features

- 文件树：懒加载、2 秒自动刷新、每工作区独立展开状态
- 文件图标：常见格式显示着色徽章（代码）/ emoji（图片、音视频、压缩包等），目录展开/收起区分
- 可编辑预览：透明 textarea 叠加语法高亮，`Ctrl+S`/`Cmd+S` 保存；
- **磁盘变更同步**：打开的文件被外部修改（如 agent 或其它编辑器保存）时，
- **行号栏**：编辑器左侧逻辑行号，与文本滚动锁定对齐（纯文本/高亮模式均生效）
- **图片预览**：png/jpg/gif/webp/avif/svg 等直接内联渲染（同源字节路由，20MB 上限）
- **右键菜单**（VS Code 风格）：文件/文件夹/**整列任意空白、头部**均可右键——
- **@ 在消息中引用**：文件右键「@ 在消息中引用」把 `@相对工作区路径` 插入聊天输入框；

## 📦 Install

```bash
# npm（推荐）
dsh plugin --profile web add dsh-plugin-workbench
# 或 GitHub
dsh plugin --profile web add github:Pasumao/dsh-plugin-workbench
```

## 🚀 Quick Start

```bash
git clone https://github.com/Pasumao/dsh-plugin-workbench.git
cd dsh-plugin-workbench
pnpm install
pnpm run build     # 产出 lib/index.js 与 lib/client.js
# 以 link: 方式挂载进 profile
```

## 📚 Learn more

**配置**

无需环境变量或配置文件；布局补丁全自动（插件启动时自动检测并重跑 `scripts/patch-layout.mjs`，幂等、非阻塞；0.0.15 起自动识别同一版本的两种构建产物 ——npm 构建与 DSH Desktop 内置构建；锚点与编译产物字节级耦合，DSH 升级后如失配 需更新锚点）：

**安装**

> 布局补丁锚点与 DSH 编译产物字节级耦合，DSH 升级后如失配需更新锚点；0.0.15 起 > 自动识别 npm / DSH Desktop 两种构建产物，插件启动时自动检测并重打补丁 > （详见「配置」节）。

**说明**

右键菜单的新建/重命名/删除同样经该通道（loopback 信任，与编辑器保存一致） 先经 `ctx.fs.resolve → stat`（沙箱一致的路径解析）再读取字节，20MB 上限 无需手动重跑；锚点失效时需更新 `scripts/patch-layout.mjs`（0.0.15 起锚点表分 npm / desktop-ci 两个构建变体自动探测，desktop-ci 变体存于 `scripts/layout-anchors.desktop-ci.json`）

## 🔗 Links

- [GitHub Repository](https://github.com/Pasumao/dsh-plugin-workbench)
- [Full README](https://github.com/Pasumao/dsh-plugin-workbench#readme)
- [Back to the Plugins list](../plugins.md)
