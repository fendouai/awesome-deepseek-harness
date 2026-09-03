---
title: "dsh-live2d-pets"
description: "Live2D 桌宠插件 for DeepSeek Harness：Agent 状态镜像 + 互动陪伴，内置宽松许可预设模型 / Live2D pet plugin: agent state mirror + interactive companion with curated permissive-license presets"
keywords: "dsh-live2d-pets, ui, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-live2d-pets

> ⭐ **14** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 14 | 状态 | ✅ 活跃 |
| 作者 | [cyanfish-x](https://github.com/cyanfish-x) | 更新时间 | — |
| 子分类 | 💡 生成式界面 | 能力 | coding, multi-agent |

## 一句话介绍

> Live2D 桌宠插件 for DeepSeek Harness：Agent 状态镜像 + 互动陪伴，内置宽松许可预设模型 / Live2D pet plugin: agent state mirror + interactive companion with curated permissive-license presets

## 详细介绍

[English](README.en.md) | 简体中文 给 DeepSeek Harness 请了个看板娘：你思考它歪头，你完成它撒花，还能摸头！

## ✨ 核心特性

- **模型加载**：内置 5 条策展模型（Hiyori / Haru / Mao / Mark / Natori）+ 自定义条目；可用任意 `.model3.json` 的 **https / http URL**，或填写**本机绝对路径**（如 `C:/models/foo/foo.model3.json`，由插件 H
- **状态镜像**：宠物实时反映 agent 思考 / 空闲 / 出错 / 完成 / 等审批（动画 + 气泡，SSE 推送）
- **人设台词**：内置六种人设（傲娇 / 元气 / 天然呆 / 三无 / 温柔治愈 / 病娇），可在插件独有 JSONC 中自定义并热切换
- **互动陪伴**：分部位触摸反应 / 鼠标跟随（头、眼、身体看向鼠标）/ 拖动停靠，任务完成庆祝；HitArea 不足时按包围盒五矩形空间回退分档
- **桌宠配置设置面板**：DSH 设置 →「桌宠配置」，开关 / 尺寸 / 渲染帧率 / 人设 / 模型列表 / 开发者选项；标量设置写入 `~/.dsh/settings.yaml`，自定义人设与自定义模型存于 `~/.dsh/live2d-pet/` 插件私有 JSONC 文件，即时生效
- **不打扰**：默认右下角、小尺寸、可拖动、可隐藏、标签页隐藏暂停渲染、限帧渲染、低配降级静态头像

## 📦 安装

```bash
请帮我安装 dsh-live2d-pets 插件（DSH 的 Live2D 桌宠插件）：
1. 执行 dsh plugin --profile web add dsh-live2d-pets 安装
2. 执行 dsh plugin --profile web list，确认 dsh-live2d-pets 出现在已安装列表中
3. 告诉我安装结果；如果失败，请附上错误信息
```

## 🚀 快速开始

```bash
dsh plugin --profile web add dsh-live2d-pets
```

## 📚 更多信息

**方式一：复制提示词让 agent 安装（推荐）**

把下面这段提示词复制给你的 DSH agent（在 Web GUI 对话中直接粘贴即可），它会自己安装并验证： 请帮我安装 dsh-live2d-pets 插件（DSH 的 Live2D 桌宠插件）： 1. 执行 dsh plugin --profile web add dsh-live2d-pets 安装 2. 执行 dsh plugin --profile web list，确认 dsh-live2d-pets 出现在已安装列表中 3. 告诉我安装结果；如果失败，请附上错误信息

**方式二：手动安装**

在终端执行（`web` profile 首次使用时自动初始化）： dsh plugin --profile web add dsh-live2d-pets 安装后插件默认启用。启动 DSH： dsh web 浏览器打开后，右下角会出现默认宠物（尺寸 160px）。当前默认模型为 Hiyori（Live2D 官方示例模型），首次加载需联网。

## 🔗 链接

- [GitHub 仓库](https://github.com/cyanfish-x/dsh-live2d-pets)
- [完整 README](https://github.com/cyanfish-x/dsh-live2d-pets#readme)
- [返回dsh-live2d-pets所在分类](../plugins.md)
