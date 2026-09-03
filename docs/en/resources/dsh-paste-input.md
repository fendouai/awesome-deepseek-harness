---
title: "dsh-paste-input"
description: "WebUI file input enhancement: Ctrl+V paste, drag & drop and file picker, copied into the session workspace."
keywords: "dsh-paste-input, input-editing, plugin, files, ui, deepseek harness, dsh"
---
# dsh-paste-input

> ⭐ **9** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Input & editing |
| Stars | ⭐ 9 | Status | ✅ active |
| Author | [lhh010](https://github.com/lhh010) | Updated | 2026-08-21 |

## One-liner

> WebUI file input enhancement: Ctrl+V paste, drag & drop and file picker, copied into the session workspace.

## About

DSH WebUI 文件输入增强插件：**Ctrl+V 粘贴** + **全页面拖拽** + **选择文件/文件夹**，发送时复制进会话工作区临时附件目录，并把对话气泡里的附件文本块**折叠为文件 chip**。 派生自 [dsh-external/dsh-multimedia-webui-input](https://github.com/dsh-external/dsh-multimedia-webui-input)（MIT），在其基础上新增剪贴板粘贴输入、首次告知弹窗与气泡附件折叠。

## 📦 Install

```bash
# 方式一：git 依赖固定 tag（公开镜像，推荐；也可用 github:lhh010/dsh-paste-input）
dsh plugin --profile web add '@dsh-community/dsh-paste-input@github:lhh010/dsh-paste-input#v0.1.17'

# 方式二：本地 link
# dsh plugin --profile web add link:/path/to/dsh-paste-input
```

## 🚀 Quick Start

```bash
- insert:
    - id: dsh-paste-input
      name: '@dsh-community/dsh-paste-input'
```

## 📚 Learn more

**提示词安装（让 DSH 自己装）**

把下面这段提示词发给任意一个 DSH 会话，模型会替你完成安装： > 帮我安装 dsh-paste-input 插件（DSH 文件输入增强：粘贴/拖拽文件），步骤： > 1. 执行 `dsh plugin --profile web add '@dsh-community/dsh-paste-input@github:lhh010/dsh-paste-input#v0.1.17'`（首次可能被 pnpm 11 拦截 node-pty 构建脚本而失败） > 2. 在 `~/.dsh/profiles/web` 下执行 `pnpm approve-builds --all`（放行构建脚本） > 3. 再执行一次第 1 步的安装命令 > 4. 完成后在 `~/.dsh/profiles/web/cordis.patch.yml` 追加 - insert 插件行（id: dsh-paste-inp

**提示词安装（让 DSH 自己装）**

把下面这段提示词发给任意一个 DSH 会话，模型会替你完成安装： > 帮我安装 dsh-paste-input 插件（DSH 文件输入增强：粘贴/拖拽文件），步骤： > 1. 执行 `dsh plugin --profile web add '@dsh-community/dsh-paste-input@github:lhh010/dsh-paste-input#v0.1.17'`（首次可能被 pnpm 11 拦截 node-pty 构建脚本而失败） > 2. 在 `~/.dsh/profiles/web` 下执行 `pnpm approve-builds --all`（放行构建脚本） > 3. 再执行一次第 1 步的安装命令 > 4. 完成后在 `~/.dsh/profiles/web/cordis.patch.yml` 追加 - insert 插件行（id: dsh-paste-inp

## 🔗 Links

- [GitHub Repository](https://github.com/lhh010/dsh-paste-input)
- [Full README](https://github.com/lhh010/dsh-paste-input#readme)
- [Back to the Plugins list](../plugins.md)
