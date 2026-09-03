---
title: "dsh-ui-appearance"
description: "Appearance customization plugin for DeepSeek Harness: theme color palette, background image, opacity/blur, glass effect"
keywords: "dsh-ui-appearance, ui, plugin, coding, multimodal, deepseek harness, dsh"
---
# dsh-ui-appearance

> ⭐ **10** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 10 | Status | ✅ active |
| Author | [TQSY114514](https://github.com/TQSY114514) | Updated | 2026-08-21 |
| Subcategory | 🎨 Skins & themes | Capabilities | coding, multimodal, ui |

## One-liner

> Appearance customization plugin for DeepSeek Harness: theme color palette, background image, opacity/blur, glass effect

## About

[English](README.en.md) · 中文 DeepSeek Harness 生态中首个支持多维度 UI 参数深度自定义的外观插件 —— 不局限于固定预设，支持面板/输入框/代码块透明度微调、毛玻璃强度、壁纸/视频背景及色板智能衍生；WebUI 与 DSH Desktop 均可使用。

## 📦 Install

```bash
dsh plugin --profile <name> add dsh-ui-appearance
```

## 🚀 Quick Start

```bash
powershell -ExecutionPolicy Bypass -Command "Invoke-WebRequest 'https://raw.githubusercontent.com/TQSY114514/dsh-ui-appearance/main/install.ps1' -OutFile install.ps1; .\install.ps1"
```

## 📚 Learn more

**方式三：源码安装（已验证端到端）**

git clone https://github.com/TQSY114514/dsh-ui-appearance.git dsh plugin --profile <name> add file:<克隆到的本地路径> 卸载：`dsh plugin --profile <name> remove dsh-ui-appearance`（脚本安装则删除 profile `node_modules` 下的 junction 与 `package.json` 中对应的 `dependencies`/`bundles` 条目）。 **更新**：新版本发布后，重新执行 `add` 命令或安装脚本即可升级到最新版。 > **DSH Desktop 用户**：Desktop 的 profile 与 Web 版相互独立——三种方式都可用，但要把插件装进 Desktop 实际激活的 profile（默认名为 

**使用**

1. 打开 WebUI,进入侧栏「设置」→「通用」 2. 在「外观」行下方找到「个性化外观」,点击展开 3. 点预设快速换肤 → 用取色器或 HEX 微调 6 个颜色角色 → 上传或拖入壁纸/视频 → 拖动氛围与界面滑块 4. 完成。所有调整实时生效,无需刷新、无需保存 设置面板内容一览:

## 🔗 Links

- [GitHub Repository](https://github.com/TQSY114514/dsh-ui-appearance)
- [Full README](https://github.com/TQSY114514/dsh-ui-appearance#readme)
- [Back to the Plugins list](../plugins.md)
