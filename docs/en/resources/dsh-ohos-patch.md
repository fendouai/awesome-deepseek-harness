---
title: "dsh-ohos-patch"
description: "让deepseek harness能在 ohos上跑！"
keywords: "dsh-ohos-patch, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-ohos-patch

> ⭐ **6** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [shenjackyuanjie](https://github.com/shenjackyuanjie) | Updated | 2026-08-11 |

## One-liner

> 让deepseek harness能在 ohos上跑！

## About

保存让 **dsh**（`test-shenjackyuanjie` monorepo，CLI 入口 `bin/dsh`）在 **OpenHarmony (openharmony-arm64)** 上 能完成 `pnpm install` 并正常运行所需的全部 patch 与配置。 **2026-08-11 实测结论：ohos 正常终端下 `pnpm install` 完整成功 + `bin/dsh --help` 可用（6 PASS / 0 FAIL）， 只需 1 个 patch（install-lefthook 跳过）。详见 `docs/ohos-install.md`。**

## ✨ Key Features

- 仓库内部的源文件（`packages/**`、`apps/**`、`scripts/**`、`src/**` 等）
- 源码片段、关键实现逻辑、内部模块名/结构信息
- 内部工具脚本的完整内容（如 `scripts/install-lefthook.mjs` 等）

## 🚀 Quick Start

```bash
dsh-ohos-patch/
├── README.md              # 本文件
├── docs/
│   ├── ohos-install.md         # 安装配方（实测通过）
│   └── ohos-sandbox-notes.md   # 沙箱环境实测结论与工作流
├── patches/               # 各依赖/仓库代码的 patch 文件（git format-patch / diff）
├── scripts/
│   └── ohos-install.sh         # 安装+诊断脚本（用户 shell 执行）
└── config/                # 需要落地的配置（.npmrc、pnpm-workspace 改动等）
```

## 🔗 Links

- [GitHub Repository](https://github.com/shenjackyuanjie/dsh-ohos-patch)
- [Full README](https://github.com/shenjackyuanjie/dsh-ohos-patch#readme)
- [Back to the Plugins list](../plugins.md)
