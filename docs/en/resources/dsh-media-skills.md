---
title: "dsh-media-skills"
description: "Free image reading & generation for DeepSeek Harness (rc.7 / rc.8 / v0.1.1-rc.1 / rc.2) — paste-image reading with auto vision transcription, DeepSeek-V4-Flash-Vision-Exp / GLM-4V-Flash / SenseNova / Gemini failover, Kolors + U1 Fast generation. No keys in repo."
keywords: "dsh-media-skills, learning, skill, coding, multimodal, deepseek harness, dsh"
---
# dsh-media-skills

> ⭐ **19** · ✅ active · skill

| | | | |
|---|---|---|---|
| Type | skill | Category | Learning |
| Stars | ⭐ 19 | Status | ✅ active |
| Author | [MJorgin](https://github.com/MJorgin) | Updated | — |

## One-liner

> Free image reading & generation for DeepSeek Harness (rc.7 / rc.8 / v0.1.1-rc.1 / rc.2) — paste-image reading with auto vision transcription, DeepSeek-V4-Flash-Vision-Exp / GLM-4V-Flash / SenseNova / Gemini failover, Kolors + U1 Fast generation. No keys in repo.

## About

DeepSeek Harness is brilliant at reasoning — but a text-only model can't see the image you just dragged into the chat. This bundle fixes that with **two free skills**, a **free vision model route**, and a **vision engine failover chain**: - 📎 **Paste to read** — paste, drag, or pick an image in any session; the free vision model turns it into text your current model understands. *(Powered by the DeepSeek Harness core auto-description path — see [docs/HARNESS_PATCH_EN.md](docs/HARNESS_PATCH_EN.md); this bundle contributes the vision model route and the skill it relies on.)* - 👁️ **`vision-review`** — analyze images and screenshots, catch UI visual bugs, detect watermarks, turn images into text. - 🎨 **`media-tools`** — generate illustrations, avatars, backgrounds and banners with a free, wat

## ✨ Key Features

- 📎 **Paste to read** — paste, drag, or pick an image in any session; the free vision model turns it into text your current model understands. *(Powered by the De
- 👁️ **`vision-review`** — analyze images and screenshots, catch UI visual bugs, detect watermarks, turn images into text.
- 🎨 **`media-tools`** — generate illustrations, avatars, backgrounds and banners with a free, watermark-free model.
- 🔀 **Engine failover** — GLM-4V-Flash (free) → **DeepSeek-V4-Flash-Vision-Exp** (same key as your agent, higher quality) → SiliconFlow Qwen3-VL → SenseNova → Goo

## 📦 Install

```bash
dsh plugin --profile <name> add github:MJorgin/dsh-media-skills
```

## 🚀 Quick Start

```bash
# ~/.dsh/.credentials.yaml (chmod 600)
   GLM_API_KEY: <your key>
```

## 📚 Learn more

**⚡ Quick start**

dsh plugin --profile <name> add github:MJorgin/dsh-media-skills 1. **Keys**: - **v0.1.1-rc.1+**: zero extra keys — paste reading and the vision route run on your agent's existing `DEEPSEEK_API_KEY` (DeepSeek-V4-Flash-Vision-Exp). - **rc.7 / rc.8** (or to add the free engines): Zhipu — [open.bigmodel.cn](https://open.bigmodel.cn) → **API Keys** (`glm-4v-flash` is free); SiliconFlow — [siliconflow.c

**🚀 Usage**

Three ways to read images: Descriptions follow your message language (Chinese message → Chinese description; English message → English description; no text → Chinese). Also just say:

**❓ FAQ**

**Does paste-image reading require a DeepSeek Harness core patch?** The auto-describe pipeline lives in the Harness **core** (`api-proxy` image-admission logic; see [docs/HARNESS_PATCH_EN.md](docs/HARNESS_PATCH_EN.md)). This bundle ships the **model route + skills**: the vision model works on any DSH build, but paste-image reading requires a Harness build with that core support — see FAQ Q1 in [do

**🎁 Examples**

Sample material to try instantly — 6 AI-generated images with their prompts, plus a purpose-built vision test card (title, buttons, bar-chart values) for checking reading accuracy:  → [examples/README.md](examples/README.md)

## 🔗 Links

- [GitHub Repository](https://github.com/MJorgin/dsh-media-skills)
- [Full README](https://github.com/MJorgin/dsh-media-skills#readme)
- [Back to the Skills list](../skills.md)
