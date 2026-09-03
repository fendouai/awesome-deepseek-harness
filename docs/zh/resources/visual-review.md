---
title: "visual-review"
description: "在 DSH Web 聊天界面内联渲染粘贴/上传的图片，让纯文本模型获得视觉：云端多模态 API 优先，本机 Qwen3-VL 兜底。"
keywords: "visual-review, vision, plugin, multimodal, deepseek harness, dsh"
---
# visual-review

> ⭐ **2** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [wang-bool](https://github.com/wang-bool) | 更新时间 | 2026-08-18 |
| 子分类 | 👁️ 视觉工具 | 能力 | vision, multimodal |

## 一句话介绍

> 在 DSH Web 聊天界面内联渲染粘贴/上传的图片，让纯文本模型获得视觉：云端多模态 API 优先，本机 Qwen3-VL 兜底。

## 详细介绍

为 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（DSH）Web 界面打造的**双面插件**：让聊天界面直接**显示图片**，并让模型**解读图片**。 - **图片显示**：用户粘贴 / 上传的图片（PNG / JPEG / WebP / GIF）会直接渲染在对话气泡里。 - **视觉解读**：`visual_review` 工具调用视觉多模态模型，返回图片的中文文字描述（文字、物体、人物、场景、图表等）。 - **双引擎**：云端优先（任意 OpenAI 兼容的多模态 `chat/completions` API，零本地依赖）；未配置时自动回退本机 Qwen3-VL-8B（数据不出本机）。 - **无需更换模型**：插件在发送路径上把「图片块」转换成「带附件 ID 的文本注解」，任何本身看不到图片的文本模型都能配合工作。 ---

## ✨ 核心特性

- **图片显示**：用户粘贴 / 上传的图片（PNG / JPEG / WebP / GIF）会直接渲染在对话气泡里。
- **视觉解读**：`visual_review` 工具调用视觉多模态模型，返回图片的中文文字描述（文字、物体、人物、场景、图表等）。
- **双引擎**：云端优先（任意 OpenAI 兼容的多模态 `chat/completions` API，零本地依赖）；未配置时自动回退本机 Qwen3-VL-8B（数据不出本机）。
- **无需更换模型**：插件在发送路径上把「图片块」转换成「带附件 ID 的文本注解」，任何本身看不到图片的文本模型都能配合工作。

## 📦 安装

```bash
dsh plugin --profile web add visual-review
```

## 🚀 快速开始

```bash
dsh plugin --profile web add github:wang-bool/visual-review
```

## 📚 更多信息

**架构与工作原理**

┌──────────────────────────── DSH Web 前端 ────────────────────────────┐ │ 聊天界面（React） │ │ └─ visual-review 客户端插件（lib/client.js） │ │ 注入 conversation.chat.node 渲染槽 │ │ └─ 图片块 → │ └───────────────┬─────────────────────────────────────────┬────────────┘ │ ① /api/session.prompt（图片块→注解） │ ② /vr-image 取图片字节 ┌───────────────▼─────────────────────────────────────────▼────────────┐ │ DSH Host（插件 Host 端 lib/i

**安装**

> **方式 A / B 无需依赖外部发布渠道**；插件已声明 `dsh.bundle` manifest（`cordis.patch.yml`），因此也支持官方 `dsh plugin add` 安装（**方式 C**，推荐，最简单）。

**方式 B：手动安装**

1. 将插件包放入 profile 的 `node_modules`： ```bash DSH_HOME="${DSH_HOME:-$HOME/.dsh}" PROFILE_DIR="$DSH_HOME/profiles/web" mkdir -p "$PROFILE_DIR/node_modules/visual-review" cp -r package.json lib server "$PROFILE_DIR/node_modules/visual-review/" ``` 2. 在 `$PROFILE_DIR/cordis.patch.yml` 末尾追加（参考 `install/cordis.patch.yml.example`）： ```yaml - insert: - id: visual-review name: 'visual-review' ``` 3. **重启 DS

**使用**

1. **直接体验**：在聊天框**粘贴**或**上传**一张图片 → 图片立即渲染在气泡里；模型侧自动出现附件注解，模型会自动调用 `visual_review` 并给出图片描述。 2. **分析本地文件**：让模型分析磁盘上的图片，例如“请用 `visual_review` 分析 `/path/to/photo.png`”，模型会以 `image_path` 参数调用工具。 3. **定制提问**：给模型指令时说明诉求，如“读出这张图片里的所有文字”“描述这个图表的趋势”。工具支持 `prompt` 参数，由模型按需传递。 4. **切换引擎**：调用 `visual_review_config` 修改云端配置即可；把三项都置空则回到本机引擎。

## 🔗 链接

- [GitHub 仓库](https://github.com/wang-bool/visual-review)
- [完整 README](https://github.com/wang-bool/visual-review#readme)
- [返回visual-review所在分类](../plugins.md)
