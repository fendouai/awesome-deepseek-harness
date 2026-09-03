---
title: "dsh-directorx"
description: "DirectorX as a DeepSeek Harness plugin: AI video/image/audio skills, knowledge corpus, and configurable vision/image/video/audio model tools."
keywords: "dsh-directorx, learning, skill, coding, multimodal, deepseek harness, dsh"
---
# dsh-directorx

> ⭐ **16** · ✅ 活跃 · 技能

| | | | |
|---|---|---|---|
| 类型 | 技能 | 分类 | 学习 |
| 星数 | ⭐ 16 | 状态 | ✅ 活跃 |
| 作者 | [LaplaceYoung](https://github.com/LaplaceYoung) | 更新时间 | — |

## 一句话介绍

> DirectorX as a DeepSeek Harness plugin: AI video/image/audio skills, knowledge corpus, and configurable vision/image/video/audio model tools.

## 详细介绍

**The first DeepSeek Harness-native video agent harness for end-to-end AI video production.** DirectorX 是一个运行在 **DeepSeek Harness (DSH)** 里的开源 `dsh-plugin`：让一个真正的 video agent 从需求理解、导演决策、剧本与分镜，到图像 / 视频 / 音频生成、剪辑、质检和交付，沿着同一条可审计的生产链完成工作。 这不是另一个提示词合集，也不是把聊天窗口包成视频生成器。它是 **DeepSeek Harness 的第一个 video agent harness**：让视频 agent 有状态、有工具、有知识、有确认闸门，并能把计划落成可编辑、可重渲染的成片。 **中文关键词**：DeepSeek Harness 视频 Agent、AI 视频 Agent、视频生成工作流、AI 导演、分镜画布、智能剪辑、成片质检、FFmpeg 视频管线。 **English keywords**: DeepSeek Harness video agent, AI video agent harness, AI video generation workflow, text-to-video, image-to-video, storyboard canvas, smart video editing, FFmpeg media pipeline. 一句话进入视频工作坊：DSH 负责导演、审批与编排，DirectorX 提供无限分镜板、生成、镜头拆解、粗剪、批处理和交付工具。 定位 · 自适应接入 · 能力 · 知识库 · 成片 · 安装 · 流程 · 画布 · 工具 · 对比 · FAQ · 文档 项目「临界点：看见之后」——节点是镜头，连线

## ✨ 核心特性

- 想在 DeepSeek Harness 中构建可复用 **AI video agent** 的开发者与 AI 工程团队。
- 需要从文字 brief 交付宣传片、短剧、分镜预演、产品视频或社媒短片的创作者与制作团队。
- 需要审批、成本控制、知识引用、素材连续性和可审计产物的企业视频工作流。

## 📦 安装

```bash
# 在插件目录里装进 Web 配置
dsh plugin --profile web add .

# 打开 WebUI
dsh web
```

## 🚀 快速开始

```bash
npm test          # typecheck + build + node:test
```

## 📚 更多信息

**FAQ**

<details> <summary><b>没有 API Key 能用吗？</b></summary> 能。四个能力切 <code>mock</code> 即可跑通工具链、画布和剪辑。有 Key 再回设置页填写。 </details> <details> <summary><b>支持哪些视频模型？</b></summary> Sora 2、可灵（新旧协议）、Runway、MiniMax H3、Vidu、Google Veo、豆包 Seedance。协议按官方文档接入，在 Settings → DirectorX 里按能力配置。 </details> <details> <summary><b>多镜头怎么保持同一张脸？</b></summary> <code>directorx_character_register</code> 注册锚点；生成时带参考图和身份描述。角色设定走三视图。相邻镜头

## 🔗 链接

- [GitHub 仓库](https://github.com/LaplaceYoung/dsh-directorx)
- [完整 README](https://github.com/LaplaceYoung/dsh-directorx#readme)
- [返回dsh-directorx所在分类](../skills.md)
