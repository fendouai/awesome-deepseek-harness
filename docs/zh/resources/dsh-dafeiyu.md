---
title: "dsh-dafeiyu"
description: "Desktop-native BigFish companion for DeepSeek Harness — real Agent status, always on top on Windows."
keywords: "dsh-dafeiyu, desktop, client, coding, multi-agent, deepseek harness, dsh"
---
# dsh-dafeiyu

> ⭐ **272** · ✅ 活跃 · 客户端

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 272 | 状态 | ✅ 活跃 |
| 作者 | [QCYTSN](https://github.com/QCYTSN) | 更新时间 | — |

## 一句话介绍

> Desktop-native BigFish companion for DeepSeek Harness — real Agent status, always on top on Windows.

## 详细介绍

**住在桌面上、由 DeepSeek Harness 真实工作状态驱动的 Agent 伴侣。** 入口属于 DSH，生命周期属于 DSH，显示层属于桌面。 [English](README_EN.md) · [npm](https://www.npmjs.com/package/dsh-dafeiyu) · [下载最新版本](https://github.com/QCYTSN/dsh-dafeiyu/releases) · [更新日志](CHANGELOG.md) · [更新与回退](docs/UPDATING.md) · [验收记录](docs/ACCEPTANCE.md) · DSH 大肥鱼不是一个需要单独启动的桌宠应用。它由 DSH 插件启用，跟随 DSH 一起启动和退出，并以透明、无边框、始终置顶的原生窗口显示在桌面上。即使切换到 VS Code、浏览器或文件管理器，也能知道 DSH 当前在思考、修改、测试、等待还是已经完成。

## ✨ 核心特性

- 最新版本永远以 [npm `latest`](https://www.npmjs.com/package/dsh-dafeiyu) 和 [GitHub Releases](https://github.com/QCYTSN/dsh-dafeiyu/releases) 为准（Releases 里同时提供 `.tgz` 安
- 给仓库 **Star 只是收藏，不会收到更新通知**。想第一时间知道「更新了什么」：
- 已安装用户升级：完全退出 DSH 后执行

## 📦 安装

```bash
dsh plugin --profile web update dsh-dafeiyu
```

## 🚀 快速开始

```bash
stateDiagram-v2
    [*] --> 空闲
    空闲 --> 思考: DSH 开始一轮任务
    思考 --> 工作: 搜索、读取、修改、执行或测试
    工作 --> 思考: 整理工具结果
    思考 --> 等待: 需要用户确认
    工作 --> 等待: 需要用户确认
    思考 --> 完成: 本轮任务完成
    工作 --> 完成: 本轮任务完成
    思考 --> 错误: 任务异常结束
    工作 --> 错误: 工具或任务失败
    等待 --> 思考: 用户继续任务
    错误 --> 思考: 用户重试
    完成 --> 空闲
```

## 📚 更多信息

**3. GitHub Release 备用安装方式**

进入 [GitHub Releases](https://github.com/QCYTSN/dsh-dafeiyu/releases)，下载最新的： dsh-dafeiyu-<version>.tgz 不要解压这个文件。 不解压，在 DSH 目录中直接安装下载的插件包： pnpm dsh plugin --profile web add "C:\Users\you\Downloads\dsh-dafeiyu-<version>.tgz"

**怎么使用？**

安装后不需要额外操作： 1. 启动 DSH。 2. 在 DSH 中开始一个项目任务。 3. 大肥鱼根据 DSH 的真实事件切换动作和状态卡。 4. 切换到其他窗口继续工作；大肥鱼仍然保持在桌面最上层。 5. DSH Host 真正退出后，大肥鱼自动退出。 状态卡可能显示： 大肥鱼不会监听 VS Code、浏览器或其他应用，也不会截图。只有 DSH Agent 的事件能够 改变它的工作状态。

## 🔗 链接

- [GitHub 仓库](https://github.com/QCYTSN/dsh-dafeiyu)
- [完整 README](https://github.com/QCYTSN/dsh-dafeiyu#readme)
- [返回dsh-dafeiyu所在分类](../clients.md)
