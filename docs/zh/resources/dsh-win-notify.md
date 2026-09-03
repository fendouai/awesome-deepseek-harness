---
title: "dsh-win-notify"
description: "DSH 插件：代理任务完成时弹出带声音的 Windows Toast 通知，点击通知即可直接切回并前台显示 DSH 标签页"
keywords: "dsh-win-notify, notifications, plugin, coding, deepseek harness, dsh"
---
# dsh-win-notify

> ⭐ **4** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 通知 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [MuziIsabel](https://github.com/MuziIsabel) | 更新时间 | — |

## 一句话介绍

> DSH 插件：代理任务完成时弹出带声音的 Windows Toast 通知，点击通知即可直接切回并前台显示 DSH 标签页

## 详细介绍

一个 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（dsh）插件：代理任务完成时在 Windows 上弹出**带声音的 Toast 通知**。 - 通知显示应用名 **DeepSeek** 与官方鲸鱼图标 - **顶层**代理回合完成（running → idle）时通知；子代理回合保持静默 - 通知正文显示最近一条用户提示词 - 任务出错时也会通知（可配置） - **点击通知直接切换并前台显示现有 GUI 标签** —— 不产生临时浏览器标签；仅当没有存活 GUI 时才新开标签（`?session=` 深链） - 等待沙箱/权限审批时也会通知（可配置） - 代理通过 `ask_user_question` 提问等待回复时也会通知（可配置） - **聚焦感知：** GUI 页面处于前台且正显示触发事件的会话时，抑制该会话的通知 —— 你正在查看时不会被打扰 - 手动停止的任务**不算**完成 —— 不弹通知 - 仅依赖 Windows 自带的 PowerShell 5.1 —— 无额外依赖

## ✨ 核心特性

- 通知显示应用名 **DeepSeek** 与官方鲸鱼图标
- **顶层**代理回合完成（running → idle）时通知；子代理回合保持静默
- 通知正文显示最近一条用户提示词
- 任务出错时也会通知（可配置）
- **点击通知直接切换并前台显示现有 GUI 标签** —— 不产生临时浏览器标签；仅当没有存活 GUI 时才新开标签（`?session=<id>` 深链）
- 等待沙箱/权限审批时也会通知（可配置）

## 📦 安装

```bash
dsh plugin --profile web add github:MuziIsabel/dsh-win-notify
```

## 🚀 快速开始

```bash
dsh plugin --profile web remove dsh-win-notify
```

## 📚 更多信息

**安装**

dsh plugin --profile web add github:MuziIsabel/dsh-win-notify `dsh plugin` 会在 profile 目录内转发给 pnpm；bundle 会把自身合并进 profile 的 `dsh.profile.bundles` 列表。重启 profile（或让 profile 的 HMR 生效）即可激活。 > 插件适用于任意 profile —— 如需在其他 profile 收到通知，可用同样的方式添加到 `headless` 等 profile。

**配置**

bundle 会在 profile 中插入加载行 `win-notify`。在 profile 的 `cordis.patch.yml` 中覆盖其配置： config: enabled: true # 启用插件（默认 true） sound: default # default | reminder | sms | alarm | silent onError: true # 任务出错时也通知（默认 true） openOnClick: true # 点击通知打开/切换 GUI 会话（默认 true） directActivate: true # 优先投递给存活的本机回环 GUI 标签；否则走浏览器深链 baseUrl: '' # 自定义 GUI 根地址（默认自动取 webServer 端口） approval: true # 等待用户审批时通知（默认 true） approvalWait

**工作原理**

1. **身份注册（一次性、自动）。** Windows 只展示来自*已注册身份*的 toast。激活时插件会： - 向 `%LOCALAPPDATA%\DeepSeek` 编译一个微型 `DeepSeek.exe` 占位程序； - 创建指向它的开始菜单快捷方式 `DeepSeek.lnk`，图标为多尺寸 `DeepSeek.ico`（由官方 DeepSeek Harness favicon 生成）； - 通过 `IPropertyStore` P/Invoke 把 `AppUserModelID`（`DSH.WinNotify`）写入快捷方式（BurntToast 技术）。 此后通知以 **DeepSeek** 名称和鲸鱼图标显示。快捷方式是身份载体 —— 请勿删除；缺失时插件会自动重建。 2. **事件钩子。** 插件在宿主层监听 `agent/status` 事件。当某会话的代理由 

## 🔗 链接

- [GitHub 仓库](https://github.com/MuziIsabel/dsh-win-notify)
- [完整 README](https://github.com/MuziIsabel/dsh-win-notify#readme)
- [返回dsh-win-notify所在分类](../plugins.md)
