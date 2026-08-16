---
title: "dsh-ohos-patch"
description: "让deepseek harness能在 ohos上跑！"
keywords: "dsh-ohos-patch, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-ohos-patch

> ⭐ 5 · ✅ 活跃 · 插件

## 一句话介绍

让deepseek harness能在 ohos上跑！

## 详细介绍

保存让 **dsh**（`test-shenjackyuanjie` monorepo，CLI 入口 `bin/dsh`）在 **OpenHarmony (openharmony-arm64)** 上 能完成 `pnpm install` 并正常运行所需的全部 patch 与配置。 **2026-08-11 实测结论：ohos 正常终端下 `pnpm install` 完整成功 + `bin/dsh --help` 可用（6 PASS / 0 FAIL）， 只需 1 个 patch（install-lefthook 跳过）。详见 `docs/ohos-install.md`。**

## 作者
**[shenjackyuanjie](https://github.com/shenjackyuanjie)**

## 链接

- [GitHub 仓库](https://github.com/shenjackyuanjie/dsh-ohos-patch)
- [完整 README](https://github.com/shenjackyuanjie/dsh-ohos-patch#readme)
- [返回dsh-ohos-patch所在分类](../plugins.md)
