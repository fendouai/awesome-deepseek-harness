---
title: "dsh-milestone"
description: "Git 风格里程碑时间线：悬停查看元数据，点击跳转任意消息。"
keywords: "dsh-milestone, ui, plugin, deepseek harness, dsh"
---
# dsh-milestone

> ⭐ **18** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 18 | 状态 | ✅ 活跃 |
| 作者 | [SnowCrescenter-tech](https://github.com/SnowCrescenter-tech) | 更新时间 | 2026-08-14 |
| 子分类 | 🧭 导航与跳转 | 能力 | ui |

## 一句话介绍

> Git 风格里程碑时间线：悬停查看元数据，点击跳转任意消息。

## 详细介绍

**DeepSeek Harness 的会话里程碑导航条** 像 Git 提交图一样，一眼定位每一次提问，一键跳转到任何位置。 ---

## ✨ 核心特性

- **键盘导航**：`↑↓` 移动 · `Enter` 跳转 · `Home/End` 首尾，全程不用鼠标。
- **turn 分组折叠**：长轮次折成一条，汇总圆点带可见 ×N 徽标，一眼知道藏着几条。
- **复制与 fork**：一键复制提问全文 / 从此处分支。
- **聚焦模式**：淡化 / 折叠思考与工具调用，强度可调、自由搭配。
- **折叠工具栏**：功能键默认收起，常用键可钉到折叠外；搜索 / 列表等浮层点击外部自动关闭。
- **个性化**：强调色 / 圆点大小 / 距侧边距离 / 左右位置即调即存；中文 / English 一键切换。

## 📦 安装

```bash
# 从 npm 安装（推荐）
dsh plugin --profile demo add dsh-milestone

# 或从 GitHub 源码安装
dsh plugin --profile demo add "github:SnowCrescenter-tech/dsh-milestone#main"

# 启动 Web UI
npx @deepseek-ai/dsh web    # → http://127.0.0.1:3080
```

## 🚀 快速开始

```bash
┌──────────────────────────────────────────┐
│ 第 3 / 5 条 · 第 2 轮         ☆ 复制 ✂    │  ← 序号 + 轮次 + 收藏/复制/fork
│ 帮我优化这段代码的性能                     │  ← 消息预览（前 80 字）
│ 5 分钟前 · 用时 1m30s · 首字 1.2s · 12.4 tok/s │  ← 时间 · 耗时 · TTFT · 吞吐
│ v4 · continue · 1280 / 2560 tok           │  ← 模型 · 用途 · token 用量
└──────────────────────────────────────────┘
```

## 📚 更多信息

**工作原理**

双半边浏览器插件（空 node half + `shell.overlay` slot 挂载的 client half），零侵入： shell.overlay (root scope) └─ milestone.rail (session scope, 自声明子槽) └─ useSession 读取会话快照 → 圆点列表 + 悬停 + 跳转

## 🔗 链接

- [GitHub 仓库](https://github.com/SnowCrescenter-tech/dsh-milestone)
- [完整 README](https://github.com/SnowCrescenter-tech/dsh-milestone#readme)
- [返回dsh-milestone所在分类](../plugins.md)
