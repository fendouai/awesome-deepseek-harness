---
title: "dsh-skill-picker"
description: "DSH 实现 workbuddy 同款选择 skill 功能 | WorkBuddy-style skill picker for DeepSeek Harness: pick a skill in the composer, insert the official /skill-name gesture, and DSH loads it with your message."
keywords: "dsh-skill-picker, learning, skill, coding, deepseek harness, dsh"
---
# dsh-skill-picker

> ⭐ **25** · ✅ active · skill

| | | | |
|---|---|---|---|
| Type | skill | Category | Learning |
| Stars | ⭐ 25 | Status | ✅ active |
| Author | [a735624258](https://github.com/a735624258) | Updated | — |

## One-liner

> DSH 实现 workbuddy 同款选择 skill 功能 | WorkBuddy-style skill picker for DeepSeek Harness: pick a skill in the composer, insert the official /skill-name gesture, and DSH loads it with your message.

## About

dsh plugin --profile web add dsh-skill-picker 一条命令从 npm 装好并注入 DSH web profile，重启 `dsh web`（或刷新页面）即生效。源码方式见下文 [安装](#安装)。 DSH Web GUI 的技能选择器：在输入框（composer）工具行右侧加一个按钮，点开可以**搜索并点选已安装的技能**，选中后把官方 `/技能名` 手势插入发送框——随消息一起发出，DSH 原生机制就会自动加载该技能并执行。WorkBuddy 式"把技能写进发送框"的交互，DeepSeek Harness 复刻版。 English: A skill picker for the DSH Web GUI — a button in the composer's right tool row opens a searchable list of installed skills; picking one inserts the official `/skill-name` gesture into the draft, so DSH's native user-invocation path loads the skill with your message. 当前版本：**v0.3.2**（`/` 补全 + ⚡ 面板均支持**拼音搜索**）

## ✨ Key Features

- ⚡ 一键弹出全部技能（闪电图标，人人看得懂）
- **`/` 直接补全**：输入斜杠即列出全部技能，**模糊搜索**（技能名+描述任意匹配）+ **常用排序**（v0.2.0）
- 🔤 **拼音搜索**：技能名和描述都生成拼音索引（全拼带空格 `ji yi` / 连打 `jiyi` / 首字母 `jy`），中文技能不用记字就能搜（v0.3.0）
- 🔍 实时搜索（技能名 / 描述 / 拼音都搜）
- ⌨️ **键盘导航**：弹层内 ↑↓ 选择、Enter 插入、Esc 关闭，全程不碰鼠标（v0.2.2）
- 🧠 **最近使用置顶、常用靠前**的智能排序（WorkBuddy 同款）
- 📋 走官方宿主 skills API（与 DSH 内置 `/` 补全同一数据源，自动覆盖用户级+项目级技能）
- 🧩 插入官方 `/技能名` 手势，加载/执行走 DSH 原生机制，**零 agent 侧改动**

## 📦 Install

```bash
dsh plugin --profile web add dsh-skill-picker
```

## 🚀 Quick Start

```bash
# 方式一：GitHub 克隆 + link（推荐，无需发布 npm）
git clone https://github.com/a735624258/dsh-skill-picker.git
dsh plugin --profile web add link:/path/to/dsh-skill-picker

# 方式二：Git 依赖直装
dsh plugin --profile web add "github:a735624258/dsh-skill-picker"

# 方式三：发布到 npm 后（预构建安装，体验最佳）
dsh plugin --profile web add dsh-skill-picker
```

## 📚 Learn more

**⚡ 快速安装（npm）**

dsh plugin --profile web add dsh-skill-picker 一条命令从 npm 装好并注入 DSH web profile，重启 `dsh web`（或刷新页面）即生效。源码方式见下文 [安装](#安装)。 DSH Web GUI 的技能选择器：在输入框（composer）工具行右侧加一个按钮，点开可以**搜索并点选已安装的技能**，选中后把官方 `/技能名` 手势插入发送框——随消息一起发出，DSH 原生机制就会自动加载该技能并执行。WorkBuddy 式"把技能写进发送框"的交互，DeepSeek Harness 复刻版。 English: A skill picker for the DSH Web GUI — a button in the composer's right tool row opens a searchable list of in

**方式三：发布到 npm 后（预构建安装，体验最佳）**

dsh plugin --profile web add dsh-skill-picker > 注：已发布 npm（`npm view dsh-skill-picker` 可见 0.3.2），方式三可直接安装；未发布时请用方式一或方式二。 > 若 `dsh` 命令因 PowerShell 执行策略被拒（`File ... cannot be loaded`），用： > `powershell -ExecutionPolicy Bypass -Command "dsh plugin --profile web add link:C:\path\to\dsh-skill-picker"` **网络特例（国内/HTTPS 受限时）**： `dsh plugin --profile web add "git+ssh://git@github.com:a735624258/dsh-skill-pic

**原理**

DSH 的 [dsh-tool-skill](https://github.com/deepseek-ai/deepseek-harness) 在 `agent/pre-step` 阶段扫描用户消息中的 `/kebab-case-name` 手势（`SKILL_GESTURE` 正则），命中后把对应技能内容作为 `skill-invocation` 注入对话——即"用户消息里写 `/技能名` 就会自动加载技能"是官方既有能力，只是没有 UI。 本插件只补 UI 一层： [client] ⚡ 按钮 → fetch('/dsh-skill-picker/skills') ↓ [host] 扫描用户级 $DSH_HOME/skills + 项目级 <cwd>/.dsh/skills 等 → 技能目录（name + description） ↓ [client] 点选 → inputActions

## 🔗 Links

- [GitHub Repository](https://github.com/a735624258/dsh-skill-picker)
- [Full README](https://github.com/a735624258/dsh-skill-picker#readme)
- [Back to the Skills list](../skills.md)
