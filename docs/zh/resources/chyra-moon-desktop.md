---
title: "deepseek-harness-desktop (chyra-moon)"
description: "Windows 原生桌面壳：官方 Web UI 1:1 复刻，内置服务、托盘与自动恢复。"
keywords: "deepseek-harness-desktop (chyra-moon), desktop, client, deepseek harness, dsh"
---
# deepseek-harness-desktop (chyra-moon)

> ⭐ **10** · ✅ 活跃 · 客户端

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 10 | 状态 | ✅ 活跃 |
| 作者 | [chyra-moon](https://github.com/chyra-moon) | 更新时间 | 2026-08-15 |

## 一句话介绍

> Windows 原生桌面壳：官方 Web UI 1:1 复刻，内置服务、托盘与自动恢复。

## 详细介绍

把 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 官方网页版装进 Windows 桌面应用 —— **同一个界面、同一个服务器，双击即用**。

## ✨ 核心特性

- 🎯 **零配置**：不用装 Node.js、不用敲命令，装完双击就是官方界面（一比一加载官方前端，不是仿制皮肤）
- 🐳 **服务器内置**：应用自己托管官方 dsh 服务器；你已开着网页版/CLI 时自动复用，会话数据互通
- 🔄 **断线自愈**：外部服务器被关掉？应用 5 秒内自动接管重启，页面自动恢复，不会"界面还在但发不了消息"
- 🖥 **正经桌面体验**：托盘驻留、窗口记忆、单实例、崩溃自动重启、无菜单栏纯净窗口
- 🐋 **鲸鱼加载动画**：官方鲸鱼由蓝/白光点构成（肚皮、眼睛、水花三处细节一比一），呼吸式起伏

## 📦 安装

```bash
npm install && npm start      # 图标缺失时会自动生成,也可手动 npm run icon
```

## 🚀 快速开始

```bash
npm run dist                      # 打包(安装版 + 解压版 + 便携版,并自动完整性校验)
npm run verify                    # 单独跑打包完整性校验
npm run update:dsh                # 一键升级官方 dsh 并重新出包
npm run preview -- --open         # 浏览器实时预览加载动画
```

## 🔗 链接

- [GitHub 仓库](https://github.com/chyra-moon/deepseek-harness-desktop)
- [完整 README](https://github.com/chyra-moon/deepseek-harness-desktop#readme)
- [返回deepseek-harness-desktop (chyra-moon)所在分类](../clients.md)
