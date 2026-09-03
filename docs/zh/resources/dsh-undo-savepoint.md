---
title: "dsh-undo-savepoint"
description: "DSH crash-rescue plugin: undo config & plugin-code changes, secret-safe snapshots, one-click SAFE MODE, plus offline CLI/GUI that work even when DSH won't boot."
keywords: "dsh-undo-savepoint, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-undo-savepoint

> ⭐ **134** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 134 | 状态 | ✅ 活跃 |
| 作者 | [lire1131](https://github.com/lire1131) | 更新时间 | — |

## 一句话介绍

> DSH crash-rescue plugin: undo config & plugin-code changes, secret-safe snapshots, one-click SAFE MODE, plus offline CLI/GUI that work even when DSH won't boot.

## 详细介绍

**为 [DeepSeek Harness (DSH)](https://github.com/deepseek-ai/deepseek-harness) 打造的撤销/回退系统：装插件、换皮肤、改设置，自动保存即存档；手动保存随时存档；一键撤销 / 恢复 / 回退到任意版本。DSH 启动不了时，还有局外 WebUI / GUI / CLI 兜底。** 还在为 DSH 崩溃而苦恼？还在担心小改动带来大灾难？配置与插件代码一键回滚、快照密钥脱敏、一键安全模式——DSH 挂了也能自救。

## 📦 安装

```bash
dsh plugin --profile web add github:lire1131/dsh-undo-savepoint#master
```

## 🚀 快速开始

```bash
git clone https://github.com/lire1131/dsh-undo-savepoint.git D:\dsh\plugins\dsh-undo-savepoint
```

## 📚 更多信息

**安装插件（自动前后存档，失败自动回退）**

powershell -NoProfile -ExecutionPolicy Bypass -File "tools\dsh-plugin.ps1" add <包名>

## 🔗 链接

- [GitHub 仓库](https://github.com/lire1131/dsh-undo-savepoint)
- [完整 README](https://github.com/lire1131/dsh-undo-savepoint#readme)
- [返回dsh-undo-savepoint所在分类](../plugins.md)
