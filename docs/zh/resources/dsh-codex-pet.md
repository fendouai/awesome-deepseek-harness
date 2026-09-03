---
title: "dsh-codex-pet"
description: "将 Codex 桌宠皮肤自动迁移到 DeepSeek Harness，在 DSH Web 界面渲染功能一致的桌宠：动画、多会话对话框、设置面板，一键迁移即插即用。"
keywords: "dsh-codex-pet, search, plugin, coding, deepseek harness, dsh"
---
# dsh-codex-pet

> ⭐ **8** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 8 | 状态 | ✅ 活跃 |
| 作者 | [mengyun233](https://github.com/mengyun233) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding |

## 一句话介绍

> 将 Codex 桌宠皮肤自动迁移到 DeepSeek Harness，在 DSH Web 界面渲染功能一致的桌宠：动画、多会话对话框、设置面板，一键迁移即插即用。

## 详细介绍

DeepSeek Harness（DSH）桌面宠物插件：导入/上传 codex 风格的**精灵图序列帧宠物**，在 DSH Web GUI 以 `shell.overlay` 悬浮浮层渲染，含图库管理、基础交互与 Agent 状态联动。

## ✨ 核心特性

- **序列帧播放**：单 WebP 精灵图（格式 A），逐帧毫秒时长，行=动画（idle / running / waiting / review / failed / 移动 / 挥手 / 跳跃）。
- **悬浮浮层交互**：左下角常驻（贴着侧边栏），可拖拽（视口钳制 + 位置持久化）、点击挥手、空闲随机小动作。
- **图库管理**：设置 → 宠物图库——zip 上传 / URL 导入 / 启用 / 停用 / 删除 / 首帧预览。
- **Agent 状态联动**：订阅 DSH 会话状态——工作中→跑动（常驻）；审批/提问→等待（脉冲一次）；任务完成→得意（脉冲一次）；任务失败→沮丧（脉冲一次）。
- **深/浅主题**：全部样式走 `--dsw-*` 主题令牌，自动适配 DSH 主题。

## 📦 安装

```bash
dsh plugin --profile web add dsh-codex-pet
```

## 🚀 快速开始

```bash
git clone https://github.com/skr311/dsh-codex-pet.git
cd dsh-codex-pet
dsh plugin --profile web add ./packages/dsh-codex-pet
```

## 🔗 链接

- [GitHub 仓库](https://github.com/mengyun233/dsh-codex-pet)
- [完整 README](https://github.com/mengyun233/dsh-codex-pet#readme)
- [返回dsh-codex-pet所在分类](../plugins.md)
