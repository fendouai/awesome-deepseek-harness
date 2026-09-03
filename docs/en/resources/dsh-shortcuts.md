---
title: "dsh-shortcuts"
description: "DeepSeek Harness WebUI 键盘快捷键插件（34 个预置功能、一键录制自定义、静默权限切换）— Fully customizable keyboard shortcuts for the DSH WebUI."
keywords: "dsh-shortcuts, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-shortcuts

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [Ricketts-Guo](https://github.com/Ricketts-Guo) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, ui |

## One-liner

> DeepSeek Harness WebUI 键盘快捷键插件（34 个预置功能、一键录制自定义、静默权限切换）— Fully customizable keyboard shortcuts for the DSH WebUI.

## About

为 [DeepSeek Harness](https://deepseek.com) 的 WebUI 提供一套**可完全自定义的键盘快捷键系统**。所有可触达的功能预注册在分组列表中，带默认键的直接生效（macOS 优先，其他平台自动改用 Ctrl），其余一键录制即可绑定。配置保存在浏览器 localStorage，刷新/重启不丢。 - **34 个预置功能**，6 个分组：会话 / 视图 / 剪贴板 / 模型 / 权限 / 系统 - **自定义绑定**：任何功能都可录制任意组合键、清除、禁用，冲突自动检测 - **快捷键速查表**（`⌘/`）：随时查看全部绑定 + 内置诊断面板 - **无留痕权限切换**：⇧Tab 直调宿主权限服务，对话流零污染 - **权限快速切换**：只读 / 工作区写入 / 完全访问（Shitft+tab） - **双部署形态**：会话级动态插件（WebUI）+ 宿主级静态插件（Desktop），行为一致 - **纯浏览器端为主**：无网络请求、不触碰业务数据；仅权限切换经宿主侧路由直写

## ✨ Key Features

- **34 个预置功能**，6 个分组：会话 / 视图 / 剪贴板 / 模型 / 权限 / 系统
- **自定义绑定**：任何功能都可录制任意组合键、清除、禁用，冲突自动检测
- **快捷键速查表**（`⌘/`）：随时查看全部绑定 + 内置诊断面板
- **无留痕权限切换**：⇧Tab 直调宿主权限服务，对话流零污染
- **权限快速切换**：只读 / 工作区写入 / 完全访问（Shitft+tab）
- **双部署形态**：会话级动态插件（WebUI）+ 宿主级静态插件（Desktop），行为一致

## 🚀 Quick Start

```bash
curl -fsSL https://raw.githubusercontent.com/Ricketts-Guo/dsh-shortcuts/main/install.sh | bash
```

## 📚 Learn more

**方式一：一键安装（推荐，一行命令）**

curl -fsSL https://raw.githubusercontent.com/Ricketts-Guo/dsh-shortcuts/main/install.sh | bash 脚本自动完成：克隆插件 → 链接到 web profile → 注册到 `package.json` → **同步 pnpm lockfile（将插件纳入 pnpm 管理，防止后续安装/更新其他插件时被清掉）**（幂等，可重复运行）。完成后**完全退出并重新打开 DeepSeek Harness**，左下角设置按钮旁出现「⌘K 快捷键」按钮即安装成功。 **更新插件**：重新运行上面同一行命令即可（`pnpm install` 会同步最新代码副本，再重启 DSH 生效）。 **手动步骤版**（脚本等价操作）： 1. `git clone https://github.com/Ricketts-Guo/d

## 🔗 Links

- [GitHub Repository](https://github.com/Ricketts-Guo/dsh-shortcuts)
- [Full README](https://github.com/Ricketts-Guo/dsh-shortcuts#readme)
- [Back to the Plugins list](../plugins.md)
