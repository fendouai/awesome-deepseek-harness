---
title: "dsh-godot-skill"
description: "Godot Engine 4.x full-stack game development skill plugin for DSH."
keywords: "dsh-godot-skill, coding, skill, deepseek harness, dsh"
---
# dsh-godot-skill

> ⭐ **9** · ✅ active · skill · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | skill | Category | Coding |
| Stars | ⭐ 9 | Status | ✅ active |
| Author | [akira399](https://github.com/akira399) | Updated | 2026-08-13 |

## One-liner

> Godot Engine 4.x full-stack game development skill plugin for DSH.

## About

Godot Engine 4.x 全栈游戏开发技能插件 for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（DSH）。 安装后，插件在激活时把仓库内自带的 **`godot-4-development`** 技能注册为运行时技能 —— 任何会话都可以通过 `skill` 工具加载它，让 AI 独立完成 Godot 游戏的规划、搭建、编码、调试、优化与导出。

## ✨ Key Features

- **核心概念**：节点 / 场景 / 资源 / 信号 / 组
- **渲染器选型**：Forward+ / Mobile / Compatibility（GL）
- **特性 → 实现速查**（20 个领域）：平台与导出、编辑器、2D/3D 图形与工具与物理、着色器、GDScript/C#/GDExtension、音频、导入、输入、导航、网络、国际化、窗口与 OS、移动端/XR、GUI、动画、文件格式、杂项（Movie Maker、无头服务器、CI）
- **完整开发工作流**：设计决策 → 项目脚手架 → 核心玩法原型 → 内容实现 → 打磨与性能 → 测试调试 → 导出发布
- **代码模板与错误排查表**：玩家移动、相机跟随、生成、HTTP、暂停、存档、ENet 联机、常见错误速查

## 📦 Install

```bash
npx -p @deepseek-ai/dsh dsh plugin --profile web add dsh-godot-skill
```

## 🚀 Quick Start

```bash
npx -p @deepseek-ai/dsh dsh plugin --profile web add git+https://github.com/akira399/dsh-godot-skill.git
```

## 📚 Learn more

**方式二：Git HTTPS 安装**

npx -p @deepseek-ai/dsh dsh plugin --profile web add git+https://github.com/akira399/dsh-godot-skill.git

**方式三：GitHub 短名安装（需要本机已配置 GitHub SSH key）**

npx -p @deepseek-ai/dsh dsh plugin --profile web add github:akira399/dsh-godot-skill 安装完成后重启 DSH（重新运行 `dsh web`）。重启后会话技能目录中即出现 `godot-4-development`。

**使用**

插件生效后，会话中会提示可用技能 `godot-4-development`。直接说： > 用 godot-4-development 技能帮我做一个 2D 平台跳跃游戏 AI 会先加载技能，再按技能内的工作流与 API 速查完成开发。

## 🔗 Links

- [GitHub Repository](https://github.com/akira399/dsh-godot-skill)
- [Full README](https://github.com/akira399/dsh-godot-skill#readme)
- [Back to the Skills list](../skills.md)
