---
title: "dsh-hdc-bridge"
description: "DSH 原生鸿蒙开发助手：hdc 设备闭环调试 + 设备面板（官方 client 插件形态）+ 离线官方知识层（Tier-1 随包）+ DevEco CLI 构建/签名/模拟器控制 / DSH-native HarmonyOS dev assistant: hdc device loop, live device panel, offline official knowledge, DevEco CLI build/sign/emulator"
keywords: "dsh-hdc-bridge, developer, integration, coding, ui, deepseek harness, dsh"
---
# dsh-hdc-bridge

> ⭐ **16** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 开发者工具 |
| 星数 | ⭐ 16 | 状态 | ✅ 活跃 |
| 作者 | [1na-ko](https://github.com/1na-ko) | 更新时间 | — |

## 一句话介绍

> DSH 原生鸿蒙开发助手：hdc 设备闭环调试 + 设备面板（官方 client 插件形态）+ 离线官方知识层（Tier-1 随包）+ DevEco CLI 构建/签名/模拟器控制 / DSH-native HarmonyOS dev assistant: hdc device loop, live device panel, offline official knowledge, DevEco CLI build/sign/emulator

## 详细介绍

[hdc_mcp](https://github.com/yushun667/hdc_mcp) 等 MCP 服务器已覆盖 hdc 能力层。本插件不重写 hdc 协议，直接复用本机 hdc 二进制（3.x），价值在 DSH 原生层： - 会话内工具卡片与 `read_image` 原生闭环 - 按调用会话解析沙箱策略（与 `pwsh` 工具同款路线），截图写入 `/.dsh-hdc/screenshots/` - 结构化的失败上报（hdc 传输层退出码不可靠，插件用输出标记 + 落盘校验兜底） - v0.7 起面板按官方 client 插件形态集成（边栏入口 + 浮动面板 + 官方主题），v0.9 补齐会话级编译、静态检查、部署与日志工具（switch_cwd / build_project / arkts_check / start_app / hdc_log）

## ✨ 核心特性

- 会话内工具卡片与 `read_image` 原生闭环
- 按调用会话解析沙箱策略（与 `pwsh` 工具同款路线），截图写入 `<workspace>/.dsh-hdc/screenshots/`
- 结构化的失败上报（hdc 传输层退出码不可靠，插件用输出标记 + 落盘校验兜底）
- v0.7 起面板按官方 client 插件形态集成（边栏入口 + 浮动面板 + 官方主题），v0.9 补齐会话级编译、静态检查、部署与日志工具（switch_cwd / build_project / arkts_check / start_app / hdc_log）

## 🚀 快速开始

```bash
{"name":"switch_cwd","arguments":{"path":"E:\\ScribePad"}}
```

## 🔗 链接

- [GitHub 仓库](https://github.com/1na-ko/dsh-hdc-bridge)
- [完整 README](https://github.com/1na-ko/dsh-hdc-bridge#readme)
- [返回dsh-hdc-bridge所在分类](../integrations.md)
