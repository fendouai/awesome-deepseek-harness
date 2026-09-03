---
title: "dsh-skin-market"
description: "DeepSeek Harness skin market 皮肤市场 已收录200+DSH 皮肤 完善评分系统加人工审核，有便捷的社区收录入口；有在线页面方便在线浏览，也有插件方便管理本地皮肤"
keywords: "dsh-skin-market, registry, awesome-list, coding, ui, deepseek harness, dsh"
---
# dsh-skin-market

> ⭐ **105** · ✅ active · awesome-list

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 105 | Status | ✅ active |
| Author | [kingOfSoySauce](https://github.com/kingOfSoySauce) | Updated | — |

## One-liner

> DeepSeek Harness skin market 皮肤市场 已收录200+DSH 皮肤 完善评分系统加人工审核，有便捷的社区收录入口；有在线页面方便在线浏览，也有插件方便管理本地皮肤

## About

[点击查看在线皮肤市场](https://kingofsoysauce.github.io/dsh-skin-market/)

## ✨ Key Features

- 2026-08-28：[fengb3/dsh-theme-aurum](https://github.com/fengb3/dsh-theme-aurum)（`1.1.0`）——鎏金 Aurum 主题
- 更多请查看[收录日志](./docs/recently-added.md)

## 📦 Install

```bash
dsh plugin --profile web add "dsh-skin-market@latest"
```

## 🚀 Quick Start

```bash
> pnpm add "github:owner/repo#<commit>&path:/subdir" --dir $env:USERPROFILE\.dsh\profiles\web
>
```

## 📚 Learn more

**方式二，提示词安装：**

<details> <summary><strong>点击展开提示词</strong></summary> 复制以下给 DSH 即可，会先检查冲突，再安装皮肤市场 请把 dsh-skin-market 插件安装到 DSH 的 web profile。不能先安装再检查，必须严格按以下顺序执行： 1. 安装前只读检查 web profile 的 package.json（dependencies 与 dsh.profile.bundles）、profile 的 cordis.patch.yml 和 $DSH_HOME/cordis.patch.yml（如有）。 2. 从当前启用的 bundles 中识别皮肤、主题或外观插件：排除 @deepseek-ai/dsh-base、@deepseek-ai/dsh-web-app 和 dsh-skin-market；读取候选 package.json 

**安装失败时，可以让 DSH 自己排查**

> 皮肤市场的安装、更新和卸载会调用 DSH 的 profile 插件管理器；当前 DSH 使用 `pnpm` 管理 profile 依赖。如果出现 `pnpm is not recognized`、`package manifest missing` 或 `allowBuilds` 相关报错，不必手动猜测 profile 状态。 > > 含子目录路径的 GitHub 目标（`github:…#commit&path:/…`）请优先用市场页一键安装。Windows 上不要把这段 spec 交给 `dsh plugin add`：cmd.exe 会在 `&` 处截断。需要手动安装时用： > > ```powershell > pnpm add "github:owner/repo#<commit>&path:/subdir" --dir $env:USERPROFILE\.dsh\profi

## 🔗 Links

- [GitHub Repository](https://github.com/kingOfSoySauce/dsh-skin-market)
- [Full README](https://github.com/kingOfSoySauce/dsh-skin-market#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
