---
title: "dsh-notify-windows"
description: "DSH Windows 原生通知，零依赖。"
keywords: "dsh-notify-windows, notifications, plugin, deepseek harness, dsh"
---
# dsh-notify-windows

> ⭐ **5** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 通知 |
| 星数 | ⭐ 5 | 状态 | ✅ 活跃 |
| 作者 | [SeverusZh](https://github.com/SeverusZh) | 更新时间 | 2026-08-20 |

## 一句话介绍

> DSH Windows 原生通知，零依赖。

## 详细介绍

- **任务完成提醒**：监听会话 `turn/end` 事件，任务完成 / 出错 / 输出超限时立即弹窗，标题自动使用会话标题，正文显示原因与轮次； - **权限审批提醒**：监听 `approval/asked` 事件，有操作等待你的审批时立即提醒；会话审批策略为 `never` 时自动跳过（此时没有东西在等你）； - **提问确认提醒**：Agent 调用 `ask_user_question` 向你提问时提醒；本部署下所有工具都经 `run_code` 调用，插件会扫描 `run_code` 程序源码中的 `tools.ask_user_question(` 调用并提取问题文本； - **防打扰**：默认忽略子代理（subagent）会话，只提醒主会话； - **零依赖**：通知通过 Windows PowerShell 5.1 的 WinRT Toast API 发送，自动注册 HKCU 的 AppUserModelId（无需管理员权限）； - **可诊断**：可选日志（`%TEMP%\dsh-notify\notify.log`）与 debug 事件日志。

## ✨ 核心特性

- **任务完成提醒**：监听会话 `turn/end` 事件，任务完成 / 出错 / 输出超限时立即弹窗，标题自动使用会话标题，正文显示原因与轮次；
- **权限审批提醒**：监听 `approval/asked` 事件，有操作等待你的审批时立即提醒；会话审批策略为 `never` 时自动跳过（此时没有东西在等你）；
- **提问确认提醒**：Agent 调用 `ask_user_question` 向你提问时提醒；本部署下所有工具都经 `run_code` 调用，插件会扫描 `run_code` 程序源码中的 `tools.ask_user_question(` 调用并提取问题文本；
- **防打扰**：默认忽略子代理（subagent）会话，只提醒主会话；
- **零依赖**：通知通过 Windows PowerShell 5.1 的 WinRT Toast API 发送，自动注册 HKCU 的 AppUserModelId（无需管理员权限）；
- **可诊断**：可选日志（`%TEMP%\dsh-notify\notify.log`）与 debug 事件日志。

## 📦 安装

```bash
dsh plugin --profile web add dsh-notify-windows
```

## 🚀 快速开始

```bash
dsh --profile web
```

## 📚 更多信息

**🚀 安装**

项目通过 **`dsh.bundle`** 机制安装：npm 包自带的 `cordis.patch.yml` 会在 `dsh plugin add` 后自动挂载 `dsh-notify` 入口，**不需要**再手动 `- insert:`。 dsh plugin --profile web add dsh-notify-windows 重启 DSH 并刷新浏览器后生效： dsh --profile web > 注意：不要再用 `- insert:` 手动添加 `dsh-notify`，否则启动会报 > `duplicate loader entry id: dsh-notify`。想调整配置，在 profile 的 > `cordis.patch.yml` 里按 id 覆盖即可（见下节）。

**⚙️ 配置项**

插件行 `config` 全字段可选，未填按默认值。需要调整时，在 `$DSH_HOME/profiles/web/cordis.patch.yml` 里按 id 覆盖主条目即可 （该文件被运行中的 DSH 热监视，改动立即生效，无需重启）： name: dsh-notify-windows config: enabled: true reasons: [completed, error, max-tokens] notifyOnStart: true notifyOnApproval: true log: true

## 🔗 链接

- [GitHub 仓库](https://github.com/SeverusZh/dsh-notify-windows)
- [完整 README](https://github.com/SeverusZh/dsh-notify-windows#readme)
- [返回dsh-notify-windows所在分类](../plugins.md)
