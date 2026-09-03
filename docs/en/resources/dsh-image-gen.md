---
title: "dsh-image-gen"
description: "Generate images directly in DeepSeek Harness chats"
keywords: "dsh-image-gen, vision, plugin, coding, multimodal, deepseek harness, dsh"
---
# dsh-image-gen

> ⭐ **277** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 277 | Status | ✅ active |
| Author | [shanliuling](https://github.com/shanliuling) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding, multimodal |

## One-liner

> Generate images directly in DeepSeek Harness chats

## About

**为 DeepSeek Harness 提供完整的对话图像能力：文生图、图生图、多图参考、连续编辑、本地 ComfyUI 与画廊管理。** [English](README.en.md) | **简体中文** 💬 直接对你的 DeepSeek Harness Agent 发送以下提示词： 帮我安装生图插件，执行命令：pnpm dsh plugin --profile web add dsh-image-gen@latest （也可以手动在终端执行：pnpm dsh plugin --profile web add dsh-image-gen@latest） 安装完成后，在 DSH 设置中填入自己的 API Key 或配置本地 ComfyUI，就可以直接对 Agent 说： 帮我画一张雨夜霓虹街头的赛博朋克猫咪。 Agent 会自动完成图片生成，也可以直接基于上一张图片继续修改。 ---

## 📦 Install

```bash
帮我安装生图插件，执行命令：pnpm dsh plugin --profile web add dsh-image-gen@latest
```

## 🚀 Quick Start

```bash
帮我画一张雨夜霓虹街头的赛博朋克猫咪。
```

## 📚 Learn more

**若已将 dsh 安装为系统全局命令：**

dsh plugin --profile web add dsh-image-gen@latest <details> <summary><b>🛠️ 其他安装方式（Git 仓库直装 / 本地调试）</b></summary>

**方式 B：从 GitHub 仓库直接安装最新代码**

pnpm dsh plugin --profile web add git+https://github.com/shanliuling/dsh-image-gen.git

**方式 C：本地克隆源码开发安装**

git clone https://github.com/shanliuling/dsh-image-gen.git pnpm dsh plugin --profile web add ./dsh-image-gen </details>

**2. 配置 Provider 与工作区设置**

打开 DSH Web 页面（默认 `http://localhost:3080`）： 1. 进入 **Settings → Plugins → Image generation**。 2. 选择 Provider；云端 Provider 填写 API Key，本地 ComfyUI 填写地址并导入 API Format Workflow JSON（提示词位置使用 `{{prompt}}`，种子可选用 `{{seed}}`；图生图工作流在 LoadImage 的 `image` 输入中使用 `{{image}}`，调用时插件会自动上传源图并回填文件名，仅允许出现一次）。ComfyUI 支持导入多个命名工作流并选择当前使用的一个，Agent 也可以在调用时通过 `workflow` 参数按名称指定。 3. 可按需开启 **保存到工作区**（默认开启）并自定义子目录，点击 **保存** 即可。 <

## 🔗 Links

- [GitHub Repository](https://github.com/shanliuling/dsh-image-gen)
- [Full README](https://github.com/shanliuling/dsh-image-gen#readme)
- [Back to the Plugins list](../plugins.md)
