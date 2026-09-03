---
title: "dsh-revive"
description: "DSH 一键复活：重启后给所有被打断的会话自动发送「继续」指令（/revive 命令 + revive_sessions 工具 + 浏览器一键按钮）"
keywords: "dsh-revive, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-revive

> ⭐ **4** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | — |
| Subcategory | 🧰 Toolkits | Capabilities | coding |

## One-liner

> DSH 一键复活：重启后给所有被打断的会话自动发送「继续」指令（/revive 命令 + revive_sessions 工具 + 浏览器一键按钮）

## About

**Author / Maintainer:** [@Zacklinkk](https://github.com/Zacklinkk) DSH 进程经常在跑任务时被杀死（自己杀自己、OOM、崩溃……），重启之后每个被打断的会话都要手动点开、手动发一句「继续」。这个插件把这件事变成**一键**： - 扫描全部持久化会话，识别「被打断」的（回合没跑完、消息没处理、上次回合以中止/出错/阻塞/超长收尾的）； - 按官方 GUI 同款路径冷恢复它们：从持久化日志重建会话、挂回它原来的 preset 组合、沿用上次的模型； - 给每个被打断的会话发送「继续」指令，让它们接着干活； - 子代理会话不直接复活（它们会随父会话的恢复被自动接管），正在运行的会话不动。

## ✨ Key Features

- 扫描全部持久化会话，识别「被打断」的（回合没跑完、消息没处理、上次回合以中止/出错/阻塞/超长收尾的）；
- 按官方 GUI 同款路径冷恢复它们：从持久化日志重建会话、挂回它原来的 preset 组合、沿用上次的模型；
- 给每个被打断的会话发送「继续」指令，让它们接着干活；
- 子代理会话不直接复活（它们会随父会话的恢复被自动接管），正在运行的会话不动。

## 📦 Install

```bash
# 已登录私有 npm registry 的 DSH 部署机
dsh plugin --profile web add dsh-revive@0.1.4

# 本地开发 checkout
dsh plugin --profile web add link:/path/to/dsh-revive
```

## 🚀 Quick Start

```bash
- update:
    id: revive
    config:
      resumePrompt: 继续
      autoReviveOnStartup: false
      startupDelayMs: 5000
      scanTtlMs: 120000
```

## 📚 Learn more

**配置**

在 profile 自己的 `cordis.patch.yml` 中更新插件行；不要修改安装包内的 patch： id: revive config: resumePrompt: 继续 autoReviveOnStartup: false startupDelayMs: 5000 scanTtlMs: 120000 所有键均可选：

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-revive)
- [Full README](https://github.com/omdsh-dev/dsh-revive#readme)
- [Back to the Plugins list](../plugins.md)
