---
title: "dsh-cyber-particle"
description: "为 DeepSeek Harness Web 界面添加动态粒子网络背景 | Particle-network background plugin for DeepSeek Harness web"
keywords: "dsh-cyber-particle, search, plugin, coding, deepseek harness, dsh"
---
# dsh-cyber-particle

> ⭐ **12** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 12 | Status | ✅ active |
| Author | [AKS1st](https://github.com/AKS1st) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding |

## One-liner

> 为 DeepSeek Harness Web 界面添加动态粒子网络背景 | Particle-network background plugin for DeepSeek Harness web

## About

[English](./README.en.md) | 中文 为 DeepSeek Harness Web 界面提供动态粒子网络背景：灰白散点从屏幕边缘随机飞入、直线穿过界面、离开后从新的边缘再次进入；彼此距离小于阈值的粒子自动连线，形成不断变化的网状结构。 渲染在界面全屏覆盖层上，`pointer-events` 穿透，不影响鼠标/键盘交互，也不改动任何界面配色。无 npm 运行时依赖。 内置「设置 → 粒子背景」页：可实时调节粒子数量、半径、线条粗细、连线距离、移动速度，用调色板改粒子/线条颜色，一键重置为默认；调整即时生效并持久化到浏览器 `localStorage`，刷新页面或重启后自动恢复。设置页文案跟随 DSH 语言设置（中文 / English）。

## 📦 Install

```bash
dsh plugin --profile web add github:AKS1st/dsh-cyber-particle
dsh web   # 重启 web 服务使 profile 生效
```

## 🚀 Quick Start

```bash
git clone https://github.com/AKS1st/dsh-cyber-particle.git
dsh plugin --profile web add /path/to/dsh-cyber-particle
dsh web
```

## 📚 Learn more

**安装**

从 GitHub 仓库安装（纯 JS，零构建，即装即用）： dsh plugin --profile web add github:AKS1st/dsh-cyber-particle dsh web # 重启 web 服务使 profile 生效 本地安装（clone 后直接指向仓库目录）： git clone https://github.com/AKS1st/dsh-cyber-particle.git dsh plugin --profile web add /path/to/dsh-cyber-particle dsh web

## 🔗 Links

- [GitHub Repository](https://github.com/AKS1st/dsh-cyber-particle)
- [Full README](https://github.com/AKS1st/dsh-cyber-particle#readme)
- [Back to the Plugins list](../plugins.md)
