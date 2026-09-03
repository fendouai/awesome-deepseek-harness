---
title: "DSH-Plugins-Marketplace"
description: "在 DSH Web GUI 中一键浏览、安装与更新全部 GitHub dsh-plugin 插件。"
keywords: "DSH-Plugins-Marketplace, discovery, plugin, ui, workflow, deepseek harness, dsh"
---
# DSH-Plugins-Marketplace

> ⭐ **132** · ✅ 活跃 · 插件 · 近期 ⬆️ +3

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 插件发现 |
| 星数 | ⭐ 132 | 状态 | ✅ 活跃 |
| 作者 | [bradeGithub](https://github.com/bradeGithub) | 更新时间 | 2026-08-21 |

## 一句话介绍

> 在 DSH Web GUI 中一键浏览、安装与更新全部 GitHub dsh-plugin 插件。

## 详细介绍

🌐 **语言 / Language:** **中文** | [English](README.en.md) 一个为 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（DSH）打造的插件市场插件：自动嗅探 GitHub 生态全部插件，在 DSH Web GUI 设置页中以卡片列表展示，支持**一键安装 / 版本检测 / 自动更新 / 已安装识别**，全程无需命令行。 --- - [✨ 核心优势](#核心优势) - [⚡ 一键安装（复制即用）](#一键安装复制即用) - [🚀 使用方法](#使用方法) - [✨ 功能特性](#功能特性) - [📦 手动安装](#手动安装) - [🔧 工作原理](#工作原理) - [数据源（registry 优先，搜索 API 兜底）](#数据源registry-优先搜索-api-兜底) - [安装流程（5 步）](#安装流程5-步) - [版本检测逻辑](#版本检测逻辑) - [已安装判定（五重，打开市场即自动比对）](#已安装判定五重打开市场即自动比对) - [📁 文件结构](#文件结构) - [📡 HTTP 接口](#http-接口) - [⚠️ 安全说明](#安全说明) - [⚖️ 免责声明](#免责声明) - [🧱 已知限制](#已知限制) - [🌱 第三方生态](#第三方生态) - [🙏 致谢](#致谢) - [🛠️ 开发与维护](#开发与维护) - [📝 更新日志](#更新日志) - [📄 许可](#许可) ---

## ✨ 核心特性

- **全量拉取**：插件列表优先从**静态索引**（`registry.json`，jsDelivr CDN 分发，GitHub Actions 每 2 小时自动生成）加载——零 API 调用、零限流，几千个插件也能秒开；索引不可用时自动回退 GitHub 搜索 API 分页拉取（缓存 10 分钟）。列表排序：**已安装
- **一键安装**：每个插件卡片带「安装」按钮，点击后自动完成：克隆仓库 → 识别类型 → 扫描所需环境变量 → 执行安装
- **自带一键安装**：本仓库内置 `install.ps1` / `install.sh`，一行命令即可安装，也可把上面的一句话直接交给 AI 执行
- **智能类型识别**：自动区分并安装以下类型的仓库：
- **用户材料介入**：当插件需要 `API_KEY` / `TOKEN` / `SECRET` 等环境变量时，**安装自动暂停**，在页面内弹窗请你提供材料（或跳过），不会盲装
- **脚本执行确认**：检测到第三方安装脚本（`install.sh` / `install.ps1`）或 npm 生命周期脚本（`prepare` / `install` / `postinstall` 等）时，先弹窗征求你的确认——拒绝即取消安装并**清理全部痕迹**
- **已安装识别**：五重判定——安装清单（`installed.json`）+ 目录启发式探测 + 包名映射扫描 + 本体 `repository` 自识别 + 缓存克隆预读，已安装的插件按钮变为不可点击的灰色「已安装」
- **中英双语**：界面与安装日志跟随 DSH 的语言设置自动切换 中文 / English（设置 → 常规 → Language）

## 📦 安装

```bash
dsh plugin --profile web install bradeGithub/DSH-Plugins-Marketplace
```

## 🚀 快速开始

```bash
dsh plugin --profile web remove bradeGithub/DSH-Plugins-Marketplace
dsh plugin --profile web install bradeGithub/DSH-Plugins-Marketplace   # 重装即更新
```

## 📚 更多信息

**⚡ 一键安装（复制即用）**

**方式一（推荐）：官方 dsh CLI**——由 Harness 官方安装机制完成安装与注册（需要 `dsh` CLI 与 `pnpm`，`dsh web` 用户通常已具备）： dsh plugin --profile web install bradeGithub/DSH-Plugins-Marketplace 卸载 / 更新同样走官方命令： dsh plugin --profile web remove bradeGithub/DSH-Plugins-Marketplace dsh plugin --profile web install bradeGithub/DSH-Plugins-Marketplace # 重装即更新 **方式二：安装脚本**（没有 dsh CLI 的环境；脚本检测到 dsh CLI 时会自动改用官方方式）： **喂给 AI 的一句话**（AI 具备命令执行能

**🚀 使用方法**

1. 重启 DSH 后打开 Web GUI，进入 **设置 → DSH插件市场** 2. 页面自动加载全部插件（已安装置顶，其余按 Star 排序），也可点击「刷新」强制重新拉取 3. 使用搜索框按名字过滤插件；分类 chips 按栏目筛选 4. 点击插件卡片上的按钮： - **安装** → 开始安装，日志实时滚动 - 需要材料时 → 页面弹出输入框，提供 API Key 等后点「提交材料并继续安装」 - **更新** → 检测到新版本时覆盖升级 - **已安装**（灰色）→ 无需操作 5. 切换到 **通用 Skills** tab 浏览 20000+ 技能，支持搜索 / 触底分页 / 一键安装 ---

**✨ 功能特性**

- `skill`（含 `SKILL.md`）→ 安装到 `~/.dsh/skills/` - agent 预设（含 `preset.yml` + `agent.cordis.yml`）→ 安装到 `~/.dsh/.agent-presets/` - cordis 插件（含 `package.json`）→ 安装依赖并注册到 web profile - 安装脚本（`install.sh` / `install.ps1`）→ 执行脚本 ---

**📦 手动安装**

> 💡 不想手动操作？用上面的 [⚡ 一键安装](#-一键安装复制即用)（一条命令或一句话交给 AI）。 本插件位于 `~/.dsh/profiles/web/node_modules/dsh-plugin-marketplace/`，并通过 `~/.dsh/profiles/web/cordis.patch.yml` 注册： - id: dsh-plugin-marketplace name: dsh-plugin-marketplace > ⚠️ **重启生效**：DSH 的 Web profile 关闭了配置热重载（`hmr` 被禁用），修改插件代码或注册条目后需要**重启 DSH**（重新运行 `dsh web` 或 `start-dsh.bat`）再刷新页面。 ---

## 🔗 链接

- [GitHub 仓库](https://github.com/bradeGithub/DSH-Plugins-Marketplace)
- [完整 README](https://github.com/bradeGithub/DSH-Plugins-Marketplace#readme)
- [返回DSH-Plugins-Marketplace所在分类](../plugins.md)
