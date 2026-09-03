---
title: "deepseek-harness-zh_pro"
description: "Chinese enhancement plugin for DeepSeek Harness (DSH) - DSH 中文增强插件"
keywords: "deepseek-harness-zh_pro, vision, plugin, coding, deepseek harness, dsh"
---
# deepseek-harness-zh_pro

> ⭐ **14** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 14 | 状态 | ✅ 活跃 |
| 作者 | [magian1127](https://github.com/magian1127) | 更新时间 | 2026-08-21 |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Chinese enhancement plugin for DeepSeek Harness (DSH) - DSH 中文增强插件

## 详细介绍

**DeepSeek Harness 综合性增强插件** **语言 / Language:** [中文](README.md) · [English](README.en.md) 综合性增强插件：补全中文界面，并提供思考显示、会话列表、服务监控和模型请求中文化 等增强。「中文补全」只在中文界面生效；其余界面与会话增强同时支持中文和英文界面。 所有会修改模型请求的功能都是独立的显式开关，默认关闭。

## ✨ 核心特性

- DeepSeek Harness Web GUI ≥ 0.1.2-alpha.2，默认 profile 为 `web`
- Node.js `^22.19.0 || >=24.0.0`

## 📦 安装

```bash
# 官方持久通道：自然下一次启动后生效
dsh plugin --profile web add deepseek-harness-zh_pro

# 热安装：DSH 正在运行时可立即生效
npx -y deepseek-harness-zh_pro install --profile web
```

## 🚀 快速开始

```bash
pnpm install
node bin/dsh-zh.mjs install --profile web --link $PWD
```

## 📚 更多信息

**热安装：DSH 正在运行时可立即生效**

npx -y deepseek-harness-zh_pro install --profile web 本地源码联调（首次使用先安装依赖，`prepare` 会生成运行产物）： pnpm install node bin/dsh-zh.mjs install --profile web --link $PWD TypeScript 源码构建与检查： pnpm install npm run typecheck npm test npm pack --dry-run --json `src/` 是唯一手写源码；`lib/`、`bin/`、`scripts/` 和根目录验证脚本都是被 Git 忽略的构建产物， 由 `prepare`、`npm run build` 或 `prepack` 动态生成。发布前会重新编译并生成客户端经典脚本。 安装后可检查状态： npx -y deepseek-h

## 🔗 链接

- [GitHub 仓库](https://github.com/magian1127/deepseek-harness-zh_pro)
- [完整 README](https://github.com/magian1127/deepseek-harness-zh_pro#readme)
- [返回deepseek-harness-zh_pro所在分类](../plugins.md)
