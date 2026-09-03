---
title: "dsh-ohos-patch"
description: "让deepseek harness能在 ohos上跑！"
keywords: "dsh-ohos-patch, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-ohos-patch

> ⭐ **6** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [shenjackyuanjie](https://github.com/shenjackyuanjie) | 更新时间 | 2026-08-11 |

## 一句话介绍

> 让deepseek harness能在 ohos上跑！

## 详细介绍

保存让 **dsh**（`test-shenjackyuanjie` monorepo，CLI 入口 `bin/dsh`）在 **OpenHarmony (openharmony-arm64)** 上 能完成 `pnpm install` 并正常运行所需的全部 patch 与配置。 **2026-08-11 实测结论：ohos 正常终端下 `pnpm install` 完整成功 + `bin/dsh --help` 可用（6 PASS / 0 FAIL）， 只需 1 个 patch（install-lefthook 跳过）。详见 `docs/ohos-install.md`。**

## ✨ 核心特性

- 仓库内部的源文件（`packages/**`、`apps/**`、`scripts/**`、`src/**` 等）
- 源码片段、关键实现逻辑、内部模块名/结构信息
- 内部工具脚本的完整内容（如 `scripts/install-lefthook.mjs` 等）

## 🚀 快速开始

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

## 🔗 链接

- [GitHub 仓库](https://github.com/shenjackyuanjie/dsh-ohos-patch)
- [完整 README](https://github.com/shenjackyuanjie/dsh-ohos-patch#readme)
- [返回dsh-ohos-patch所在分类](../plugins.md)
