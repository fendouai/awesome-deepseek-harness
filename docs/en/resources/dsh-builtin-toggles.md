---
title: "dsh-builtin-toggles"
description: "Human-readable catalog of official DSH Web built-ins with safe GUI toggles."
keywords: "dsh-builtin-toggles, ui, plugin, deepseek harness, dsh"
---
# dsh-builtin-toggles

> ⭐ **7** · ✅ active · plugin · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 7 | Status | ✅ active |
| Author | [Starfie1d1272](https://github.com/Starfie1d1272) | Updated | 2026-08-19 |

## One-liner

> Human-readable catalog of official DSH Web built-ins with safe GUI toggles.

## About

DeepSeek Harness Web 的 evidence-backed 内置 capability Inspector；9 个经过审阅的 UI controls 只是极窄、fail-closed 的附加能力。 本插件位于 **设置 → 插件 → 内置插件**。它显示由 Host 生成的 capability inspection：审阅事实、profile override、可持久化性、兼容性和 mutation eligibility 均由服务端计算。检查结果按 composition scope 区分：Host/profile 组合与按会话挂载的 Agent 预设组合即使使用相同 id（如 `tool-bash`）也不会互相误判为重复。 截图环境：published `@deepseek-ai/dsh@0.1.0-rc.6`、内置 `standard` Agent 预设、本插件当前版本；数据未伪造。Host 不公开稳定 runtime release identity，因此 Compatibility 如实显示 `unverified / 运行时身份不可用`。（另两张真实截图保存在 `docs/assets/`：`builtin-toggles-anomalies.png` 展示干净 rc.6 + 内置 `standard` Agent 预设下仅异常项为 0，`builtin-toggles-agent-preset-scope.png` 展示 26 个按会话挂载的 Agent 预设组合条目。）

## ✨ Key Features

- **Capability Inspector / Doctor**：检查当前 Web Loader 的所有 capability，包括 external、未审阅和异常条目；逐项展示运行状态、profile override 三态、Agent 预设 ownership、composition scope（Host 组合 
- **筛选与诊断**：按 ID/包名、类别、管理平面、组合范围、策略、验证、运行状态及异常筛选；可复制不含本地路径和配置内容的脱敏诊断报告。复制成功/失败反馈显示在按钮旁。
- **Composition-scope 建模**：duplicate 检查使用 Loader 的公开 `Entry.id`（含 tree-owner 链）。Host 与内置 `standard` Agent 预设中合法的同 ID 各自归属不同 composition scope，不产生 `duplicate_runti
- **Agent 预设平面**：`tool-*` / `plan-mode` 等按会话由 Agent 预设组装，单独标注，绝不误认为 profile override。
- **9 个 reviewed UI controls**：仅 `ui-deliverables`、`ui-jobs`、`ui-goal`、`ui-message-feedback`、`ui-model-selection`、`ui-agent-preset`、`ui-skill`、`ui-subagent`、`ui-t
- **Fail-closed**：核心服务、Agent 能力、第三方与未知条目一律锁定；没有 generic plugin manager、marketplace 或安装/更新生命周期。
- **Inspection API v1**：`GET /api/builtin-toggles/v1/inspection` 是稳定、无本地化文案的机器接口，提供 inventory、审阅基线、配置三态、compatibility 和 eligibility。详见 [Inspection API v1](docs/in

## 📦 Install

```bash
dsh plugin --profile web add dsh-builtin-toggles
dsh web
```

## 🚀 Quick Start

```bash
npx @deepseek-ai/dsh plugin --profile web add dsh-builtin-toggles
npx @deepseek-ai/dsh web
```

## 📚 Learn more

**安装**

前置：已初始化的 DSH `web` profile。后续公开 DSH 版本可能仍可安装或运行，但除非经过明确 review，不自动成为 supported/reviewed baseline。 已安装 `dsh` CLI： dsh plugin --profile web add dsh-builtin-toggles dsh web 使用 npx（无需全局安装 `dsh`）： npx @deepseek-ai/dsh plugin --profile web add dsh-builtin-toggles npx @deepseek-ai/dsh web 安装后重启 DSH web/gateway，使启动时读取 bundle 层。

## 🔗 Links

- [GitHub Repository](https://github.com/Starfie1d1272/dsh-builtin-toggles)
- [Full README](https://github.com/Starfie1d1272/dsh-builtin-toggles#readme)
- [Back to the Plugins list](../plugins.md)
