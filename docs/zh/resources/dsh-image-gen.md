---
title: "dsh-image-gen"
description: "Generate images directly in DeepSeek Harness chats"
keywords: "dsh-image-gen, vision, plugin, coding, multimodal, deepseek harness, dsh"
---
# dsh-image-gen

> ⭐ **277** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 277 | 状态 | ✅ 活跃 |
| 作者 | [shanliuling](https://github.com/shanliuling) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding, multimodal |

## 一句话介绍

> Generate images directly in DeepSeek Harness chats

## 详细介绍

**为 DeepSeek Harness 提供完整的对话图像能力：文生图、图生图、多图参考、连续编辑、本地 ComfyUI 与画廊管理。** [English](README.en.md) | **简体中文** 💬 直接对你的 DeepSeek Harness Agent 发送以下提示词： 帮我安装生图插件，执行命令：pnpm dsh plugin --profile web add dsh-image-gen@latest （也可以手动在终端执行：pnpm dsh plugin --profile web add dsh-image-gen@latest） 安装完成后，在 DSH 设置中填入自己的 API Key 或配置本地 ComfyUI，就可以直接对 Agent 说： 帮我画一张雨夜霓虹街头的赛博朋克猫咪。 Agent 会自动完成图片生成，也可以直接基于上一张图片继续修改。 ---

## 📦 安装

```bash
帮我安装生图插件，执行命令：pnpm dsh plugin --profile web add dsh-image-gen@latest
```

## 🚀 快速开始

```bash
帮我画一张雨夜霓虹街头的赛博朋克猫咪。
```

## 📚 更多信息

**若已将 dsh 安装为系统全局命令：**

dsh plugin --profile web add dsh-image-gen@latest <details> <summary><b>🛠️ 其他安装方式（Git 仓库直装 / 本地调试）</b></summary>

**方式 B：从 GitHub 仓库直接安装最新代码**

pnpm dsh plugin --profile web add git+https://github.com/shanliuling/dsh-image-gen.git

**方式 C：本地克隆源码开发安装**

git clone https://github.com/shanliuling/dsh-image-gen.git pnpm dsh plugin --profile web add ./dsh-image-gen </details>

**2. 配置 Provider 与工作区设置**

打开 DSH Web 页面（默认 `http://localhost:3080`）： 1. 进入 **Settings → Plugins → Image generation**。 2. 选择 Provider；云端 Provider 填写 API Key，本地 ComfyUI 填写地址并导入 API Format Workflow JSON（提示词位置使用 `{{prompt}}`，种子可选用 `{{seed}}`；图生图工作流在 LoadImage 的 `image` 输入中使用 `{{image}}`，调用时插件会自动上传源图并回填文件名，仅允许出现一次）。ComfyUI 支持导入多个命名工作流并选择当前使用的一个，Agent 也可以在调用时通过 `workflow` 参数按名称指定。 3. 可按需开启 **保存到工作区**（默认开启）并自定义子目录，点击 **保存** 即可。 <

## 🔗 链接

- [GitHub 仓库](https://github.com/shanliuling/dsh-image-gen)
- [完整 README](https://github.com/shanliuling/dsh-image-gen#readme)
- [返回dsh-image-gen所在分类](../plugins.md)
