---
title: "dsh-personal-directive"
description: "个人指令插件：系统提示词注入、工具与顶部运行时开关（框架版，中性占位可替换）。"
keywords: "dsh-personal-directive, input-editing, plugin, context, deepseek harness, dsh"
---
# dsh-personal-directive

> ⭐ **0** · 🧪 实验性 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 输入与编辑 |
| 星数 | ⭐ 0 | 状态 | 🧪 实验性 |
| 作者 | [PerryLink](https://github.com/PerryLink) | 更新时间 | — |

## 一句话介绍

> 个人指令插件：系统提示词注入、工具与顶部运行时开关（框架版，中性占位可替换）。

## 详细介绍

DeepSeek Harness 的「无限一代」二次开发**框架版**：保留原版仓库的插件形态（系统提示词注入 + 工具 + 顶部运行时开关），但**不随包发布原版提示词内容**——改用中性占位指令，用户可自行替换为自己的个人指令。

## ✨ 核心特性

- GitHub：https://github.com/Minglink/dsh-infinite-gen-1
- 项目名称：dsh-infinite-gen-1 / 无限一代（Infinite Generation One）
- 原作者：Minglink

## 📦 安装

```bash
dsh plugin --profile web add github:PerryLink/dsh-personal-directive
```

## 🚀 快速开始

```bash
& "D:/deepseek-harness/node_modules/.bin/dsh.cmd" plugin --profile web add github:PerryLink/dsh-personal-directive
```

## 📚 更多信息

**从 GitHub 安装**

推荐直接从 GitHub 安装： dsh plugin --profile web add github:PerryLink/dsh-personal-directive 如果 `dsh` 没有加入 PATH，可以使用 DSH 安装目录中的命令： & "D:/deepseek-harness/node_modules/.bin/dsh.cmd" plugin --profile web add github:PerryLink/dsh-personal-directive 安装成功后，DSH 会自动： 1. 将插件加入 `~/.dsh/profiles/web/package.json` 的 dependencies。 2. 将 `dsh-personal-directive` 加入 `dsh.profile.bundles`。 3. 应用插件自带的 `cordis.patch.yml`。

**本地安装备选（git / pack）**

适合开发、修改源码或从本地备份恢复。git 安装会一并安装依赖： dsh plugin --profile <p> add github:PerryLink/dsh-personal-directive 将 `<p>` 替换为目标 profile 名（如 `web`）。 也可以先打包再从本地 tarball 安装： npm pack dsh plugin --profile <p> add ./dsh-personal-directive-0.2.0.tgz 打包安装同样会安装依赖。修改源码后需重新打包并重装，并重启 `dsh web` 才能加载新的 Host 或 Web 客户端代码。

**安全和使用范围**

本框架版**不包含原版提示词内容**：随包发布的是中性占位指令（`prompts/personal-directive.md`），运行时行为与任何"系统提示词段注入"插件相同，仅影响你自己提供的指令文本。 本项目不修改模型权重，也不绕过远端模型服务的独立安全策略、操作系统权限或 Harness 的实际工具权限。

**归属和许可证说明**

本项目明确基于以下原版项目进行二次开发： https://github.com/Minglink/dsh-infinite-gen-1 原版作者和原始项目归属应得到保留。 本仓库根目录的 `LICENSE` 是本仓库维护者为本项目新增代码和集成代码提供的 MIT 声明。它不自动替代原版项目的版权，也不代表原作者的原始提示词和原始代码已经被重新许可。 截至本项目整理时，原版仓库没有发现明确的 `LICENSE` 文件或 GitHub 许可证标识。因此，本框架版采用原版 README 指引中的第三种许可路径：**仅发布不包含原版提示词的代码框架**——`prompts/personal-directive.md` 已替换为中性占位指令，用户可自行提供自己的指令内容（原版路径见上述 GitHub 链接，请自行核对原版许可状态）。 本仓库的 MIT 声明不应被解释为原作者对原版内容的授权。如原作者

## 🔗 链接

- [GitHub 仓库](https://github.com/PerryLink/dsh-personal-directive)
- [完整 README](https://github.com/PerryLink/dsh-personal-directive#readme)
- [返回dsh-personal-directive所在分类](../plugins.md)
