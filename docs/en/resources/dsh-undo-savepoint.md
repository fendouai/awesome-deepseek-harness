---
title: "dsh-undo-savepoint"
description: "DSH crash-rescue plugin: undo config & plugin-code changes, secret-safe snapshots, one-click SAFE MODE, plus offline CLI/GUI that work even when DSH won't boot."
keywords: "dsh-undo-savepoint, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-undo-savepoint

> ⭐ **134** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 134 | Status | ✅ active |
| Author | [lire1131](https://github.com/lire1131) | Updated | — |

## One-liner

> DSH crash-rescue plugin: undo config & plugin-code changes, secret-safe snapshots, one-click SAFE MODE, plus offline CLI/GUI that work even when DSH won't boot.

## About

**为 [DeepSeek Harness (DSH)](https://github.com/deepseek-ai/deepseek-harness) 打造的撤销/回退系统：装插件、换皮肤、改设置，自动保存即存档；手动保存随时存档；一键撤销 / 恢复 / 回退到任意版本。DSH 启动不了时，还有局外 WebUI / GUI / CLI 兜底。** 还在为 DSH 崩溃而苦恼？还在担心小改动带来大灾难？配置与插件代码一键回滚、快照密钥脱敏、一键安全模式——DSH 挂了也能自救。

## 📦 Install

```bash
dsh plugin --profile web add github:lire1131/dsh-undo-savepoint#master
```

## 🚀 Quick Start

```bash
git clone https://github.com/lire1131/dsh-undo-savepoint.git D:\dsh\plugins\dsh-undo-savepoint
```

## 📚 Learn more

**安装插件（自动前后存档，失败自动回退）**

powershell -NoProfile -ExecutionPolicy Bypass -File "tools\dsh-plugin.ps1" add <包名>

## 🔗 Links

- [GitHub Repository](https://github.com/lire1131/dsh-undo-savepoint)
- [Full README](https://github.com/lire1131/dsh-undo-savepoint#readme)
- [Back to the Plugins list](../plugins.md)
