---
title: "dsh-recall-plugin"
description: "DSH 消息撤回插件：回到发送该消息时的状态 DSH Message Recall Plugin: Return to the state when the message was sent"
keywords: "dsh-recall-plugin, memory, plugin, coding, context, deepseek harness, dsh"
---
# dsh-recall-plugin

> ⭐ **24** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 24 | Status | ✅ active |
| Author | [limbo947](https://github.com/limbo947) | Updated | 2026-08-20 |
| Subcategory | 🧠 Memory systems | Capabilities | coding, context |

## One-liner

> DSH 消息撤回插件：回到发送该消息时的状态 DSH Message Recall Plugin: Return to the state when the message was sent

## About

--- **在任意一条你发过的消息下方**，**点「↶ 撤回」**，**工作区文件和对话历史一起回到那条消息发出之前的状态** --- [更新日志](CHANGELOG.md)

## ✨ Key Features

- **文件 + 对话，整段回退**：撤回的不只是聊天记录，agent 改过的文件也一并回到原样。
- **不碰你项目自己的 git**：快照存在独立的影子 git 仓库里，你的分支、暂存区、未提交改动统统不受影响；`.git`、`node_modules` 自动排除。
- **项目目录保持干净**：快照始终存在 `$DSH_HOME` 下，不会往项目里塞任何东西；与会话的沙箱权限无关（workspace-write / read-only 会话照常快照与回退），仅当 home 本身不可写（如指到只读盘）才降级到项目内 `.dsh-recall-snapshots`（降级时页面会提示），h
- **字节级保真**（2.1.1+）：快照与回退不受项目 `.gitattributes` 的 EOL 转换影响——LF/CRLF 换行、`$Id$`、二进制内容原样往返（影子仓库固化 `info/attributes` 关闭全部属性驱动转换）。
- **可以反复后悔**：撤回一次后还能再撤到更早；撤回时被覆盖的文件也一直找得回来。快照默认每工作区保留 500 条（超限自动清最旧，上限可调或关闭），会话被彻底删除后其快照随之清理。
- **先看清单再动手**：点撤回先弹出将变更的文件清单（修改 / 恢复 / 删除），确认后才执行，不会稀里糊涂覆盖。
- **运行中防护**（2.0+）：目标工作区的 agent 正在运行时拒绝预览与撤回，避免确认期间文件又被 agent 改动；预览之后若该消息又有了新快照，执行前强制重新预览（时效校验）。
- **回退失败自动救援**（2.1+）：执行撤回前先自动打一份「回退前」安全快照；回退中途失败时自动恢复到回退前状态，救援也失败则给出可直接复制执行的手动恢复命令——任何路径都不留半回退现场。

## 📦 Install

```bash
dsh plugin --profile web add dsh-recall-plugin
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add github:limbo947/dsh-recall-plugin
```

## 📚 Learn more

**安装**

前置：git CLI（未装时撤回按钮不出现，页面顶部会提示安装 git，不影响 DSH 运行）；Windows 上 PowerShell 5.1 / 7 均可，Linux/macOS 需 bash + git；DSH 0.1.1-rc.x（依赖版本见 `peerDependencies`）。 dsh plugin --profile web add dsh-recall-plugin dsh plugin --profile web add github:limbo947/dsh-recall-plugin dsh plugin --profile web remove dsh-recall-plugin

**使用**

1. 鼠标悬停任意**插件启用后发送**的用户消息（含 agent 运行中插入的转向指令消息），复制按钮左侧出现「↶ 撤回」。 2. 点击 → 确认面板展示将变更的文件清单（修改 / 恢复 / 删除）。 3. 点「确认回退」→ 文件恢复到该消息发送前的状态；视图切到新会话（该消息及之后的对话移除），原会话归档、随时可找回。

**配置项**

全部配置可在「**设置 → 插件配置 → 撤回插件**」卡片可视化修改（保存即热生效，无需重启），也可在 profile 的 `cordis.patch.yml` 按 `id: recall` 重述 insert 行改写；env 变量仅覆盖 gc 两项且优先级最高（设了 env 的字段在卡片里锁定）。 设置卡片另提供「恢复默认」（一键重置全部字段）与「最近错误」查看/清空。

**工作原理**

每条用户消息发送时（agent 动文件之前），工作区被快照进一个独立的影子 git 仓库；撤回时先打「回退前」安全快照、再用 `git archive` 恢复文件、通过 DSH 官方 `sessions.fork` 机制把会话切到该消息之前。二进制与换行符安全，全程不触碰项目自身的 git 状态。 ```powershell git --git-dir="<store>\git\.git" tag -l git --git-dir="<store>\git\.git" ls-tree -r --name-only snap-<消息ID> ```

## 🔗 Links

- [GitHub Repository](https://github.com/limbo947/dsh-recall-plugin)
- [Full README](https://github.com/limbo947/dsh-recall-plugin#readme)
- [Back to the Plugins list](../plugins.md)
