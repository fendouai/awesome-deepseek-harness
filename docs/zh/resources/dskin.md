---
title: "dskin"
description: "卡通像素皮肤插件：原始界面不动，像素宠物散步、眨眼、跳跃。"
keywords: "dskin, ui, plugin, deepseek harness, dsh"
---
# dskin

> ⭐ **7** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 7 | 状态 | ✅ 活跃 |
| 作者 | [dancingmemory](https://github.com/dancingmemory) | 更新时间 | 2026-08-21 |
| 子分类 | 🎨 皮肤与主题 | 能力 | ui |

## 一句话介绍

> 卡通像素皮肤插件：原始界面不动，像素宠物散步、眨眼、跳跃。

## 详细介绍

- **看它们玩**：小猫在屏幕底部散步、眨眼、到边转身；两只靠近时会停下来面对面蹦跳，然后散开。 - **拖拽**：按住小猫拖到任意位置——它会在半空挣扎（摇摆 + "!" 气泡）；**拖到屏幕顶边会倒挂住**，松手也不会掉下来，抓住拉下来才回地面。 - **摸**：鼠标悬停在猫身上，它开心蹦跶并冒爱心 ♥。 - **点击**：猫跳一下。 - **切换品种**：右下角 🐾 面板——先点一只小猫选中，再点品种按钮只给那只换装；`− ＋` 可以加减小猫数量。

## ✨ 核心特性

- **看它们玩**：小猫在屏幕底部散步、眨眼、到边转身；两只靠近时会停下来面对面蹦跳，然后散开。
- **拖拽**：按住小猫拖到任意位置——它会在半空挣扎（摇摆 + "!" 气泡）；**拖到屏幕顶边会倒挂住**，松手也不会掉下来，抓住拉下来才回地面。
- **摸**：鼠标悬停在猫身上，它开心蹦跶并冒爱心 ♥。
- **点击**：猫跳一下。
- **切换品种**：右下角 🐾 面板——先点一只小猫选中，再点品种按钮只给那只换装；`− ＋` 可以加减小猫数量。

## 📦 安装

```bash
# 1. 安装插件（写入 web profile）
dsh plugin --profile web add github:dancingmemory/dskin

# 2. 若 pnpm ≥ 10 提示构建脚本被阻止，把下面内容追加到
#    ~/.dsh/profiles/web/pnpm-workspace.yaml 后重跑第 1 步
#    allowBuilds:
#      dskin: true

# 3. 重启 web 服务，插件进入加载图谱
dsh web

# 4. 验证：设置 → 插件 中应看到 dskin（ui-skin-dskin），
#    页面右下角出现 🐾 爪爪按钮，屏幕底边有小猫散步
```

## 🚀 快速开始

```bash
# GitHub 安装（推荐）
dsh plugin --profile web add github:dancingmemory/dskin

# 源码安装
git clone https://github.com/dancingmemory/dskin.git
cd dskin && pnpm install
dsh plugin --profile web add .
```

## 📚 更多信息

**🤖 一键安装（丢给 AI）/ One-Click Install (hand to your AI)**

复制下面这句话，发给你的 AI 助手（例如 opencode / Claude / 或 DSH 自带的智能体）： > **请给我的 DSH 安装 https://github.com/dancingmemory/dskin 插件，并在插件工具中显示。** AI 应该按以下步骤执行：

**源码安装**

git clone https://github.com/dancingmemory/dskin.git cd dskin && pnpm install dsh plugin --profile web add . > pnpm ≥ 10 首次安装 git 依赖可能拒绝执行构建脚本，dsh 会提示你把 > `allowBuilds: dskin: true` 写进 profile 的 `pnpm-workspace.yaml`，重跑即可。

**🚀 使用 / Usage**

dsh web # 安装后重启，让新插件行进入加载图谱 打开 `http://127.0.0.1:3080`，小猫已经在你屏幕底边等你了。 还原：`dsh plugin --profile web remove dskin` 再重启。

## 🔗 链接

- [GitHub 仓库](https://github.com/dancingmemory/dskin)
- [完整 README](https://github.com/dancingmemory/dskin#readme)
- [返回dskin所在分类](../plugins.md)
