---
title: "dsh-user-experience"
description: "Persona-driven UX walkthrough plugin for DeepSeek Harness (DSH) - scans React + TypeScript source code for UX issues, pinpoints them, and suggests fixes."
keywords: "dsh-user-experience, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-user-experience

> ⭐ **19** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 19 | Status | ✅ active |
| Author | [DietCokewithSugar](https://github.com/DietCokewithSugar) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Persona-driven UX walkthrough plugin for DeepSeek Harness (DSH) - scans React + TypeScript source code for UX issues, pinpoints them, and suggests fixes.

## About

🎉 Listed in [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin). Existing automated checks (axe, Lighthouse) can only verify absolute rules — contrast ratio, missing alt text. But UX issues are inherently **relative**: a confirmation dialog before deleting protects an occasional user but wastes the time of an operator who processes hundreds of records a day. Without knowing *who it's for*, a "UX issue" cannot be defined. This plugin makes **target user personas** the basis of every finding. If the project has no personas yet, the plugin infers a short draft from the README and routes—there is no setup command. By having AI walk through the product as those users, it surfaces experience problems **during development** and gives concrete, locatable, reviewable opti

## 📦 Install

```bash
dsh plugin --profile web add dsh-user-experience@0.4.2
```

## 🚀 Quick Start

```bash
安装失败: dsh-user-experience — nothing installable: the plugin(s) need a build step
(blocked by default, see allowBuilds) or ship no prebuilt artifacts
```

## 📚 Learn more

**Install in Harness**

In DeepSeek Harness, enter: > Install the UX plugin in DeepSeek Harness: `dsh plugin --profile web add dsh-user-experience@0.4.2` Or run the command directly: dsh plugin --profile web add dsh-user-experience@0.4.2 Name an exact version rather than `@latest`: pnpm 11 holds back releases published in the last 24 hours, so `@latest` can resolve to nothing on a fresh profile. Check the [npm version li

**Upgrading from a `github:` install**

`dsh plugin add github:DietCokewithSugar/dsh-user-experience` **no longer works**. This repository stopped committing `lib/`, so a Git checkout carries no build artifacts, and pnpm blocks the build step by default. The market reports: 安装失败: dsh-user-experience — nothing installable: the plugin(s) need a build step (blocked by default, see allowBuilds) or ship no prebuilt artifacts and the exported

**Screenshots**

The walkthrough report explains the observed behavior and user impact in plain language: Speak in plain language to start a walkthrough. If personas are missing, the plugin drafts 1–3 users and asks once before continuing: Once you confirm that a finding is real, the card provides a task Prompt you can copy to another AI. It describes the observed phenomenon rather than prescribing code changes, t

**Installation**

> ⚠️ **Security note (must read)** > > The npm tarball ships prebuilt artifacts. There is **no `prepare` / `preinstall` / `postinstall` script**, so pnpm ≥ 10 will not ask you to allowlist a build. Installation does not compile TypeScript on your machine. > > Activating the plugin still runs its code inside the Harness process. Therefore: > 1. **Only install plugins from sources you trust**; > 2. 

## 🔗 Links

- [GitHub Repository](https://github.com/DietCokewithSugar/dsh-user-experience)
- [Full README](https://github.com/DietCokewithSugar/dsh-user-experience#readme)
- [Back to the Plugins list](../plugins.md)
