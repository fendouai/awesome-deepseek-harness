---
title: "dsh-vision-tools"
description: "DeepSeek Harness 视觉能力全家桶：vision_understand 工具（OpenAI 兼容视觉 API，默认免费智谱 GLM-4V-Flash）+ 粘贴/拖拽/按钮三入口识图。"
keywords: "dsh-vision-tools, vision, plugin, multimodal, deepseek harness, dsh"
---
# dsh-vision-tools

> ⭐ **3** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [moon09300731](https://github.com/moon09300731) | 更新时间 | 2026-08-17 |
| 子分类 | 👁️ 视觉工具 | 能力 | multimodal, vision |

## 一句话介绍

> DeepSeek Harness 视觉能力全家桶：vision_understand 工具（OpenAI 兼容视觉 API，默认免费智谱 GLM-4V-Flash）+ 粘贴/拖拽/按钮三入口识图。

## 详细介绍

DeepSeek Harness（DSH）视觉能力全家桶 —— 让 DeepSeek 纯文本模型"看得见"。 - **vision_understand 工具**：调用 OpenAI 兼容视觉大模型 API 理解本地图片（描述画面、识别文字、回答问题），注册为全局工具，所有会话可用。 - **三入口识图**：`Cmd/Ctrl+V` 粘贴截图、拖图到按钮、点按钮选文件 → 图片自动落盘到 `$DSH_HOME/pasted-images/` → 输入框填入 `请识别这张图片：` → 发送后模型自动调用识图工具。 默认使用**智谱 GLM-4.6V-Flash（免费）**，支持 4 家 provider 切换。被限流时**自动降级到 GLM-4V（glm-4v-flash）**重试，免费模型高峰期也不容易失败。

## ✨ 核心特性

- **vision_understand 工具**：调用 OpenAI 兼容视觉大模型 API 理解本地图片（描述画面、识别文字、回答问题），注册为全局工具，所有会话可用。
- **三入口识图**：`Cmd/Ctrl+V` 粘贴截图、拖图到按钮、点按钮选文件 → 图片自动落盘到 `$DSH_HOME/pasted-images/` → 输入框填入 `请识别这张图片：<路径>` → 发送后模型自动调用识图工具。

## 📦 安装

```bash
# 方式一：npm 安装（推荐）
dsh plugin --profile web add dsh-vision-tools

# 方式二：GitHub 安装
dsh plugin --profile web add "github:moon09300731/dsh-vision-tools#main"
```

## 🚀 快速开始

```bash
VISION_PROVIDER=zhipu        # zhipu | dashscope | siliconflow | openai
VISION_API_KEY=你的APIKey
```

## 📚 更多信息

**方式二：GitHub 安装**

dsh plugin --profile web add "github:moon09300731/dsh-vision-tools#main" 重启 `dsh web` 后生效。

**配置（vision_understand 工具需要）**

创建 `~/.dsh/vision.env`（全局生效，推荐）： VISION_PROVIDER=zhipu # zhipu | dashscope | siliconflow | openai VISION_API_KEY=你的APIKey 可选覆盖： VISION_BASE_URL=https://open.bigmodel.cn/api/paas/v4/chat/completions VISION_MODEL=glm-4.6v-flash 限流自动降级（可选）： VISION_FALLBACK_MODEL=glm-4v-flash 工作区回退：在项目目录放 `.dsh-vision.env`（同格式），仅该项目生效。配置每次调用实时读取，改完无需重启。

**使用**

1. **粘贴**：直接 `Cmd/Ctrl+V` 粘贴剪贴板截图（捕获阶段拦截，优先于 GUI 自身附件处理） 2. **拖拽**：拖图片到输入框左侧的「📷 识图」按钮 3. **选择**：点「📷 识图」按钮选文件 发送后 agent 会自动调用 `vision_understand` 识别图片。

**技术说明**

> ⚠️ **依赖约定**：`@deepseek-ai/dsh-tools` 是 DSH 宿主运行时自带（bundle 机制提供），本插件**不声明为 dependencies**。若声明，`dsh plugin add` 触发 npm install 会在 profile 里装出第二份 dsh-tools，与宿主全局那份形成**模块双实例**，导致工具执行层 `scheduler.prepare` 崩溃（`Cannot read properties of undefined (reading 'prepare')`）。安装后建议确认 profile 的 `node_modules/@deepseek-ai/dsh-tools` 是符号链接或单实例。 - `vision_understand` 工具经 `defineTool` 注册（`@deepseek-ai/dsh-tools`） -

## 🔗 链接

- [GitHub 仓库](https://github.com/moon09300731/dsh-vision-tools)
- [完整 README](https://github.com/moon09300731/dsh-vision-tools#readme)
- [返回dsh-vision-tools所在分类](../plugins.md)
