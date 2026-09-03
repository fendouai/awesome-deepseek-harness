---
title: "dsh-reasoning-effort"
description: "DSH适用的Codex风格的思考强度滑块，以及大肥鱼跑步滑块。Codex-style model and reasoning-effort slider for DeepSeek Harness"
keywords: "dsh-reasoning-effort, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-reasoning-effort

> ⭐ **97** · ✅ active · plugin · ⬆️ +5 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 97 | Status | ✅ active |
| Author | [HanaAyane](https://github.com/HanaAyane) | Updated | 2026-08-17 |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> DSH适用的Codex风格的思考强度滑块，以及大肥鱼跑步滑块。Codex-style model and reasoning-effort slider for DeepSeek Harness

## About

**把 Codex 风格的“模型 + 推理强度”控件直接带进 DeepSeek Harness。** [English](README.en.md) · [最新发行版](https://github.com/HanaAyane/dsh-reasoning-effort/releases/latest) · [反馈问题](https://github.com/HanaAyane/dsh-reasoning-effort/issues) 第一次打开插件时，你会在 DSH 输入框下方看到新的模型入口。点击后，弹层上方是推理强度滑块，档位随当前模型自动适配，下方仍然是熟悉的模型选择入口。插件默认启用，并与 DSH 的 `/model` 命令保持同步。 插件运行时界面提供简体中文和英文，并跟随 **设置 → 通用设置** 中的 DSH 语言即时切换。模型菜单、设置项、无障碍标签、知识库说明、警告和可复制 YAML 注释会统一切换，无需刷新页面。

## 📦 Install

```bash
请为 DeepSeek Harness 的 web Profile 安装 dsh-reasoning-effort 插件。

只执行下面两条命令，不要修改其他 Profile：
dsh plugin --profile web add github:HanaAyane/dsh-reasoning-effort#main
dsh --profile web --dump-config

确认输出中出现 dsh-reasoning-effort 后告诉我安装结果。
不要替我关闭或重启正在运行的 DSH；安装完成后提醒我手动重启 DSH Web Host。
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add github:HanaAyane/dsh-reasoning-effort#main
dsh --profile web --dump-config
```

## 📚 Learn more

**让 Agent 安装（推荐）**

如果当前 Agent 可以执行终端命令，把下面这段话完整发送给它： 请为 DeepSeek Harness 的 web Profile 安装 dsh-reasoning-effort 插件。 只执行下面两条命令，不要修改其他 Profile： dsh plugin --profile web add github:HanaAyane/dsh-reasoning-effort#main dsh --profile web --dump-config 确认输出中出现 dsh-reasoning-effort 后告诉我安装结果。 不要替我关闭或重启正在运行的 DSH；安装完成后提醒我手动重启 DSH Web Host。 Agent 应当返回安装结果，并明确告诉你配置中是否已经出现 `dsh-reasoning-effort`。

**手动安装**

也可以自己打开 PowerShell 执行： dsh plugin --profile web add github:HanaAyane/dsh-reasoning-effort#main dsh --profile web --dump-config `main` 当前版本为 `0.7.0`，与最新发行 Tag `v0.7.0` 一致。`#main` 始终安装最新代码（之后可能包含未发布改动）；如需固定在当前版本，可把命令中的 `#main` 改为 `#v0.7.0`。

**安装后看不到滑块**

请依次确认： 1. 安装后已经重启 DSH Web Host。 2. **设置 → 通用设置 → 推理强度滑块** 处于启用状态。 3. 当前模型在 DSH 模型目录中公开了至少两档推理强度（未声明的模型见下一条），且部署没有关闭 thinking。

## 🔗 Links

- [GitHub Repository](https://github.com/HanaAyane/dsh-reasoning-effort)
- [Full README](https://github.com/HanaAyane/dsh-reasoning-effort#readme)
- [Back to the Plugins list](../plugins.md)
