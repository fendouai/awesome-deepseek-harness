---
title: "dsh-plugin-quota-monitor"
description: "DSH sidebar footer quota & balance monitor: DeepSeek Rage + OpenCode Go HP/MP/SP + SCNet (国家超算) Credits local estimate. 设置→插件管理可配置数据源与费率表。"
keywords: "dsh-plugin-quota-monitor, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-quota-monitor

> ⭐ **2** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [DoggyHU](https://github.com/DoggyHU) | 更新时间 | — |
| 子分类 | 🖥️ 侧边栏与面板 | 能力 | coding, ui |

## 一句话介绍

> DSH sidebar footer quota & balance monitor: DeepSeek Rage + OpenCode Go HP/MP/SP + SCNet (国家超算) Credits local estimate. 设置→插件管理可配置数据源与费率表。

## 详细介绍

DSH（DeepSeek Harness）侧边栏底部的**额度与余额监控**插件：一条怒气条 + 各服务商状态条，并在 **设置 → 插件管理 → 余额监控**里提供完整配置页。 RPG 风格的映射：**HP 血（红）= 月额度 · 魔法 MP（蓝）= 周额度 · 耐力 SP（黄）= 5h 额度 · 怒气 Rage（金）= DeepSeek 余额**。

## ✨ 核心特性

- **怒气 Rage（金，始终显示）**：DeepSeek 官方接口实时余额（`api.deepseek.com/user/balance`），显示 ¥ 剩余金额。
- **OpenCode Go**（`opencode-go`）：官方用量接口的 **月 / 周 / 5h** 三个窗口 → HP / MP / SP，显示剩余 `$` 与细条。
- **国家超算中心（scnet）**：Token Plan **Credits 剩余**（单条，绿色）。scnet **没有公开的用量查询接口**，本插件改为**本地估算**：直接读取 DSH 自己的会话日志（`$DSH_HOME/sessions/**/*.jsonl(.zstd)`，纯 Node 解压 Zstanda
- **自动识别数据源**：默认 `auto` —— 从 DSH `settings.yaml` 的 `agent-default-model.provider` 自动选择（opencode-go / scnet），也可手动指定。
- **设置页**：数据源切换、每个条目的开关、scnet 月度额度与**模型费率表**（JSON 可编辑，含 DeepSeek-V4-Flash-0731 / GLM-5 / Kimi-K3 / MiniMax-M3 / Qwen3.8-Max 等 13 个官方费率）。
- 60 秒轮询 + 切回页面即时刷新；窄侧栏折叠为圆形小徽标。

## 📦 安装

```bash
dsh plugin --profile web add dsh-plugin-quota-monitor-<version>.tgz
# 或从 npm
dsh plugin --profile web add dsh-plugin-quota-monitor
```

## 🚀 快速开始

```bash
npm pack                                   # 打 tarball
dsh plugin --profile web remove dsh-plugin-quota-monitor
dsh plugin --profile web add ./dsh-plugin-quota-monitor-<version>.tgz
```

## 🔗 链接

- [GitHub 仓库](https://github.com/DoggyHU/dsh-plugin-quota-monitor)
- [完整 README](https://github.com/DoggyHU/dsh-plugin-quota-monitor#readme)
- [返回dsh-plugin-quota-monitor所在分类](../plugins.md)
