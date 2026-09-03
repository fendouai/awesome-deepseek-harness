---
title: "deepseek-harness-studio"
description: "DeepSeek Harness 零代码桌面端｜一键启动，支持 Windows 与 macOS；内置插件发现、热点插件推送、一键安装与管理、AI 智能推荐和视觉增强。"
keywords: "deepseek-harness-studio, desktop, client, coding, deepseek harness, dsh"
---
# deepseek-harness-studio

> ⭐ **426** · ✅ active · client · ⬆️ +29 recently

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 426 | Status | ✅ active |
| Author | [fufankeji](https://github.com/fufankeji) | Updated | 2026-08-21 |

## One-liner

> DeepSeek Harness 零代码桌面端｜一键启动，支持 Windows 与 macOS；内置插件发现、热点插件推送、一键安装与管理、AI 智能推荐和视觉增强。

## About

DeepSeek Harness Studio 使用 Electron 承载 DeepSeek Harness 的 Web 工作区，并由桌面主进程启动和管理本地 `dsh web` 服务。这个仓库提供完整源码开发环境，使用者可以从 GitHub 克隆或下载代码，在本地安装依赖、编辑源码、启动桌面应用并继续开发。 桌面安装包只通过本仓库的 GitHub Releases 发布，不使用第三方下载站。目前已经提供经过真实 Electron 验收的 macOS arm64 预览 ZIP 和 Windows x64 预览安装程序；需要继续开发时，仍可获取完整源码并在本地启动。

## 📦 Install

```bash
git clone https://github.com/fufankeji/deepseek-harness-studio.git
cd deepseek-harness-studio
```

## 🚀 Quick Start

```bash
pnpm install
```

## 📚 Learn more

**插件中心：在线安装、启停与移除**

<p align="center">  <br><sub>真实 Desktop 界面：插件头像、公开目录、已安装区域、“安装”按钮与三点管理入口。</sub> </p> 选定插件后进入 **插件中心**，可以用短包名、完整 npm 包名或明确 GitHub 仓库查找发布到 npm 公共 Registry 的插件与 Skill Pack。`dsh-plugin` 只是发现信号；GitHub 也只用于映射已发布 npm 包，Studio 不会直接安装仓库源码。确定版本仍须通过 Bundle、完整性和运行兼容校验。

**Preset 广场已上线：一键安装完整工作方式**

插件通常解决“让 Agent 多一个工具”，Skill 解决“教 Agent 按什么方法做”，而 **Agent Preset** 解决的是更完整的问题：把角色、工作规则、Skills、Plugin/MCP 与 Harness 标准工具组合成一套可以反复使用的工作方式。用户不需要逐项理解和手工配置，安装一个 Preset 后，就能直接用对应角色创建新会话。 当前源码已经提供与“插件中心”“插件发现”平级的 **Preset 广场**，并完成发现、详情、安全安装、已安装管理、用于新会话、删除与重新安装的桌面端闭环。 <p align="center">  <br><sub>真实 Desktop 界面：Preset 广场、赋范官方内置目录、搜索与排序，以及安装、查看详情和用于新会话入口。</sub> </p> > **使用路径：** 发现 Preset → 查看能力组成与前置条件 → 一键安装

**安装与启动**

安装工作区依赖： pnpm install 构建所需模块并启动桌面开发环境： pnpm run dev:desktop 开发启动器会在相关源码或构建输入变化时重新构建；需要强制完整重建时运行： pnpm run dev:desktop:rebuild

## 🔗 Links

- [GitHub Repository](https://github.com/fufankeji/deepseek-harness-studio)
- [Full README](https://github.com/fufankeji/deepseek-harness-studio#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
