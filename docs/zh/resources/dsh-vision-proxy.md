---
title: "dsh-vision-proxy"
description: "DeepSeek Harness 插件：DeepSeek 大脑 + 自动识图。GUI 附加图片自动经 OpenAI 兼容 VLM 转译成文字后交给 DeepSeek 作答；支持百炼/智谱/OpenRouter 等任意 OpenAI 兼容端点（默认 qwen3.7-flash），无 key 自动探测本地 Ollama（图片不出本机）；安装时有一问式确认"
keywords: "dsh-vision-proxy, developer, integration, coding, deepseek harness, dsh"
---
# dsh-vision-proxy

> ⭐ **12** · ✅ 活跃 · 集成 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 开发者工具 |
| 星数 | ⭐ 12 | 状态 | ✅ 活跃 |
| 作者 | [Flyvhidbwo](https://github.com/Flyvhidbwo) | 更新时间 | 2026-08-20 |

## 一句话介绍

> DeepSeek Harness 插件：DeepSeek 大脑 + 自动识图。GUI 附加图片自动经 OpenAI 兼容 VLM 转译成文字后交给 DeepSeek 作答；支持百炼/智谱/OpenRouter 等任意 OpenAI 兼容端点（默认 qwen3.7-flash），无 key 自动探测本地 Ollama（图片不出本机）；安装时有一问式确认

## 详细介绍

[English](README.en-US.md) | [简体中文](README.md) **保持 DeepSeek 作为对话大脑，图片照样直接发。** 为 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 打造：GUI 附加图片自动转译，纯文本 DeepSeek 也能识图。 =22.19" />

## ✨ 核心特性

- **绝不卡死**。匿名端点强制 20 秒超时上限（免费档挂起也拖不住整轮对话）；匿名端点遇到 HTTP 429 **立即失败**（不做无意义的 Retry-After 等待）；刚失败（429/超时）的端点进入 60 秒冷却并被跳过。
- **多模型、多厂商**。任何 OpenAI 兼容 VLM 端点都行——百炼/Qwen、QwenCloud 国际站、智谱、OpenRouter、本地 Ollama、或你自己的端点。每条 `fallbackModels` 都可以带**各自独立的** `baseURL`/`model`，一个安装即可串联多家。
- **零配置本地路径**。`autoLocalOllama`（默认开）启动时探测 `http://localhost:11434`，检测到 Ollama 就自动加入降级链——图片不出本机，免 key 免注册。
- **快速且明确的失败**。没有 key 也没有本地 Ollama 时，转译在几秒内失败并给出可操作指引（配置 `VISION_API_KEY` / `DASHSCOPE_API_KEY` 或安装 Ollama）——绝不静默卡住。
- **有 key 自动提速**。导出 `VISION_API_KEY` / `DASHSCOPE_API_KEY` 后自动走你配置的付费端点（默认百炼 `qwen3.7-flash`——快、便宜、不限速；百炼/QwenCloud/智谱/OpenRouter 或任意 OpenAI 兼容端点均可）；没有 key 的条目会被*
- **安装时一问式确认**。`postinstall` 询问你是否有 VLM API key。非交互环境自动跳过，安装永不卡死。启动时打印 PRIVACY NOTICE 标明当前使用的端点。
- **降级链 + 错误分类**。`rate_limit` / `quota` / `auth` / `region` / `model_not_found` / `context_too_large` / `http` 分类给出可操作提示。
- **内容哈希缓存**。转译结果按图片字节的 SHA-256 缓存（进程内，上限 200）——同一张图每个进程最多转译一次，重新附加或换对话也命中。

## 📦 安装

```bash
dsh plugin --profile web add dsh-vision-proxy
```

## 🚀 快速开始

```bash
# 写在 profile 的 pnpm-workspace.yaml 里
allowBuilds:
  dsh-vision-proxy: true
  sharp: true
```

## 📚 更多信息

**配置**

bundle 已自带合理的默认配置（见上方策略说明），一般无需改动。要覆盖时，请在 profile 中写 **id 定向覆盖**，不要用 `insert`（见下方警告）：

**$DSH_HOME/profiles/web/cordis.patch.yml —— 用户层覆盖示例**

name: 'dsh-vision-proxy' config: baseURL: https://dashscope.aliyuncs.com/compatible-mode/v1 apiKey: 'sk-…' # 或留空读环境变量（Windows 下直写这里最可靠） model: qwen3.7-flash maxTokens: 4096 timeoutMs: 120000 # 匿名端点无论如何都会被强制 20s 上限 maxImagePixels: 4000000 marker: '[图片转译]' autoLocalOllama: true fallbackModels: [] # 可自行添加 {model, baseURL, apiKey?, anonymous?, timeoutMs?} > ⚠️ **不要写成 `- insert: [{id: dsh-vision-proxy,

**安装后验证**

dsh --profile web --dump-config | grep -A3 dsh-vision-proxy # 应恰好一个条目（注意：会明文打印配置，含 key） 1. 重启 `dsh web` → 模型选择器出现 **DeepSeek + 自动识图**。 2. 向对话粘贴图片 → 应看到 `[图片转译]` 标记后 DeepSeek 作答。 3. 没有 key 也没有本地 Ollama 时，回合应在**数秒内快速失败**并给出指引消息——这就是预期的防卡死行为。

## 🔗 链接

- [GitHub 仓库](https://github.com/Flyvhidbwo/dsh-vision-proxy)
- [完整 README](https://github.com/Flyvhidbwo/dsh-vision-proxy#readme)
- [返回dsh-vision-proxy所在分类](../integrations.md)
