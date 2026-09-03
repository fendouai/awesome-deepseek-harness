---
title: "dsh-paste-input"
description: "DSH WebUI 文件输入增强：Ctrl+V 粘贴、拖拽、选择文件，发送时复制进会话工作区。"
keywords: "dsh-paste-input, input-editing, plugin, files, ui, deepseek harness, dsh"
---
# dsh-paste-input

> ⭐ **9** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 输入与编辑 |
| 星数 | ⭐ 9 | 状态 | ✅ 活跃 |
| 作者 | [lhh010](https://github.com/lhh010) | 更新时间 | 2026-08-21 |

## 一句话介绍

> DSH WebUI 文件输入增强：Ctrl+V 粘贴、拖拽、选择文件，发送时复制进会话工作区。

## 详细介绍

DSH WebUI 文件输入增强插件：**Ctrl+V 粘贴** + **全页面拖拽** + **选择文件/文件夹**，发送时复制进会话工作区临时附件目录，并把对话气泡里的附件文本块**折叠为文件 chip**。 派生自 [dsh-external/dsh-multimedia-webui-input](https://github.com/dsh-external/dsh-multimedia-webui-input)（MIT），在其基础上新增剪贴板粘贴输入、首次告知弹窗与气泡附件折叠。

## 📦 安装

```bash
# 方式一：git 依赖固定 tag（公开镜像，推荐；也可用 github:lhh010/dsh-paste-input）
dsh plugin --profile web add '@dsh-community/dsh-paste-input@github:lhh010/dsh-paste-input#v0.1.17'

# 方式二：本地 link
# dsh plugin --profile web add link:/path/to/dsh-paste-input
```

## 🚀 快速开始

```bash
- insert:
    - id: dsh-paste-input
      name: '@dsh-community/dsh-paste-input'
```

## 📚 更多信息

**提示词安装（让 DSH 自己装）**

把下面这段提示词发给任意一个 DSH 会话，模型会替你完成安装： > 帮我安装 dsh-paste-input 插件（DSH 文件输入增强：粘贴/拖拽文件），步骤： > 1. 执行 `dsh plugin --profile web add '@dsh-community/dsh-paste-input@github:lhh010/dsh-paste-input#v0.1.17'`（首次可能被 pnpm 11 拦截 node-pty 构建脚本而失败） > 2. 在 `~/.dsh/profiles/web` 下执行 `pnpm approve-builds --all`（放行构建脚本） > 3. 再执行一次第 1 步的安装命令 > 4. 完成后在 `~/.dsh/profiles/web/cordis.patch.yml` 追加 - insert 插件行（id: dsh-paste-inp

**提示词安装（让 DSH 自己装）**

把下面这段提示词发给任意一个 DSH 会话，模型会替你完成安装： > 帮我安装 dsh-paste-input 插件（DSH 文件输入增强：粘贴/拖拽文件），步骤： > 1. 执行 `dsh plugin --profile web add '@dsh-community/dsh-paste-input@github:lhh010/dsh-paste-input#v0.1.17'`（首次可能被 pnpm 11 拦截 node-pty 构建脚本而失败） > 2. 在 `~/.dsh/profiles/web` 下执行 `pnpm approve-builds --all`（放行构建脚本） > 3. 再执行一次第 1 步的安装命令 > 4. 完成后在 `~/.dsh/profiles/web/cordis.patch.yml` 追加 - insert 插件行（id: dsh-paste-inp

## 🔗 链接

- [GitHub 仓库](https://github.com/lhh010/dsh-paste-input)
- [完整 README](https://github.com/lhh010/dsh-paste-input#readme)
- [返回dsh-paste-input所在分类](../plugins.md)
