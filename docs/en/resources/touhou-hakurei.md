---
title: "touhou-hakurei"
description: "灵梦（Reimu）·博丽神社（东方Project）美化版皮肤：神社昼夜实景背景、灵梦立绘、画框侧边栏与输入框、纸白透明界面 — DeepSeek Harness Web GUI skin"
keywords: "touhou-hakurei, search, plugin, coding, ui, deepseek harness, dsh"
---
# touhou-hakurei

> ⭐ **18** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 18 | Status | ✅ active |
| Author | [xiake595](https://github.com/xiake595) | Updated | 2026-08-15 |
| Subcategory | 🌐 Web search | Capabilities | coding, ui |

## One-liner

> 灵梦（Reimu）·博丽神社（东方Project）美化版皮肤：神社昼夜实景背景、灵梦立绘、画框侧边栏与输入框、纸白透明界面 — DeepSeek Harness Web GUI skin

## About

DeepSeek Harness Web GUI 的东方Project 博丽神社主题皮肤：博丽神社昼夜实景背景、 灵梦左右立绘、朱红/纸白/金色的神社装饰界面。纯展示层客户端插件 —— `apply()` 设置 `data-dsh-hakurei` 作用域、按亮/暗主题切换神社背景、以独立透明层挂载灵梦 角色、装饰可折叠侧栏，并为加载/思考/工具运行状态预留稳定动画钩子。effect 销毁器 还原全部 CSS/DOM 写入；不注入服务、不发出 Cordis 事件、不触达模型请求。

## ✨ Key Features

- 博丽神社昼/夜实景对话背景（亮/暗主题自动切换；浅色模式带柔光罩缓解刺眼）
- 灵梦站姿/飞行双立绘（左侧栏联动避让、对话页移向安全边缘）
- **统一半透明面板**：侧边栏、对话头部与输入框使用同一套半透明渐变
- **主题感知文字**：浅色模式深墨文字、深色模式纸白文字，保证两种主题下可读
- 简洁无横幅：顶部缘带、悬浮横幅、底部装饰条与输入框/侧边栏画框均已移除
- 朱红、纸白、金色点缀（头像 favicon、标题字标、选中态缎带）
- 素材内嵌于 client bundle（数据 URI），激活不依赖任何临时文件/远程 URL

## 📦 Install

```bash
dsh plugin --profile web add <本目录绝对路径>
```

## 🚀 Quick Start

```bash
git clone https://github.com/xiake595/touhou-hakurei
dsh plugin --profile web add <克隆路径>
```

## 📚 Learn more

**安装**

方式一：本地路径（开发 / 已克隆仓库） dsh plugin --profile web add <本目录绝对路径> 方式二：GitHub 分发（克隆后安装） git clone https://github.com/xiake595/touhou-hakurei dsh plugin --profile web add <克隆路径> 也可以直接对 DSH 说："安装一下这个皮肤包：<仓库 URL>"。 加载即生效、卸载即复原（`wiring.id` 为 `ui-skin-hakurei`）。皮肤之间的 互斥切换由皮肤管理工具（如 dsh-skin）或 profile 的 bundles 配置管理。

## 🔗 Links

- [GitHub Repository](https://github.com/xiake595/touhou-hakurei)
- [Full README](https://github.com/xiake595/touhou-hakurei#readme)
- [Back to the Plugins list](../plugins.md)
