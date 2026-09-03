---
title: "dsh-vision-opencode"
description: "DSH plugin: Auto-convert images to text for pure-text LLMs (DeepSeek etc.) via any vision model. No need to switch your main model."
keywords: "dsh-vision-opencode, vision, plugin, coding, multimodal, deepseek harness, dsh"
---
# dsh-vision-opencode

> ⭐ **13** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 13 | Status | ✅ active |
| Author | [poiuyjie](https://github.com/poiuyjie) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding, multimodal |

## One-liner

> DSH plugin: Auto-convert images to text for pure-text LLMs (DeepSeek etc.) via any vision model. No need to switch your main model.

## About

[**中文**](https://github.com/poiuyjie/dsh-vision-opencode) ｜ [English](README.en.md)

## ✨ Key Features

- 聊天里发图 → 先交给视觉模型（如 MiMo-V2.5）转成文字，主模型照常回复，不用换模型
- 输入框右侧「识图模型」下拉，自动列出所有供应商中支持图片的模型
- 设置 → Vision 独立管理模型；`vision_read_image` 工具 / `vision-image-analysis` skill 支持 OCR、图表、截图理解
- 异常兜底：单次 60s 超时、失败重试 1 次、重试耗尽降级为占位文本，不拖垮回合

## 📦 Install

```bash
dsh plugin --profile web add -w github:poiuyjie/dsh-vision-opencode
```

## 🚀 Quick Start

```bash
curl -fsSL https://raw.githubusercontent.com/poiuyjie/dsh-vision-opencode/main/scripts/install.sh | bash
```

## 📚 Learn more

**安装**

方式一（DSH 原生，推荐）： dsh plugin --profile web add -w github:poiuyjie/dsh-vision-opencode 方式二：一键脚本（Ubuntu `install.sh` / Windows `install.ps1`）： curl -fsSL https://raw.githubusercontent.com/poiuyjie/dsh-vision-opencode/main/scripts/install.sh | bash 装完重启 `dsh`，在输入框右侧选择识图模型。 卸载：`dsh plugin --profile web remove -w dsh-vision-opencode`（或 uninstall.sh）。 > 卸载前先备份包含图片的会话——卸载后这些旧会话可能无法再发给纯文本主模型。

**配置**

编辑 `~/.dsh/settings.yaml`（也可用设置 → Vision 图形化管理）： vision-opencode: provider: '' # 识图模型供应商；空 = 未选择 model: '' # 识图模型 id；空 = 未选择 autoConvert: true # 发图自动转换开关；出问题可改 false 关掉 插件自动识别纯文本主模型并接管图片；原生多模态模型保留 DSH 原生链路，无需改模型目录。

## 🔗 Links

- [GitHub Repository](https://github.com/poiuyjie/dsh-vision-opencode)
- [Full README](https://github.com/poiuyjie/dsh-vision-opencode#readme)
- [Back to the Plugins list](../plugins.md)
