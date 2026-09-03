---
title: "dsh-web-billing"
description: "DSH Web 中英文金额 Token 计费：官方策略自动定价（含高峰/低谷），逐条消息费用台账。"
keywords: "dsh-web-billing, ui, plugin, observability, deepseek harness, dsh"
---
# dsh-web-billing

> ⭐ **10** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 10 | 状态 | ✅ 活跃 |
| 作者 | [bpc-oss](https://github.com/bpc-oss) | 更新时间 | 2026-08-21 |
| 子分类 | 📊 状态与统计 | 能力 | observability, ui |

## 一句话介绍

> DSH Web 中英文金额 Token 计费：官方策略自动定价（含高峰/低谷），逐条消息费用台账。

## 详细介绍

**简体中文** · [English](README.en.md) DeepSeek Harness（`dsh web` / 桌面版）的 **人民币 / 美元 token 计费插件**：按官方政策自动计价 （内置政策时间表，含 2026-08-17 起的**峰谷定价**），逐条消息记账，实时显示账号余额，浏览器端 展示费用（界面语言自动切换 ¥ / $）。 **一句话**：你的 AI 花销「看得见、算得清、省得下」——官方价自动跟随、本地/订阅/白嫖精细化分类、 历史一键重估、预算与余额可视。 ---

## 📦 安装

```bash
# 从 GitHub 安装（git 安装运行 prepare 构建；本包为纯 JS，无需构建，开箱即用）
dsh plugin --profile web add github:<owner>/dsh-web-billing

# 或从 npm 安装（发布后）
dsh plugin --profile web add dsh-web-billing

# 或本地开发：链接 checkout
powershell -ExecutionPolicy Bypass -File scripts/install.ps1 -Profile web
```

## 🚀 快速开始

```bash
npm run check   # 语法检查
npm test        # 定价引擎 / 余额 / 账本单元测试（node:test，无依赖）
node scripts/sync-coding-plans.mjs   # 从本机 DSH pi-ai catalog 重新生成 coding plan 价表
```

## 📚 更多信息

**📦 安装**

插件是一个标准 **DSH 组合包（bundle）**（`dsh.bundle.patch` 指向包内 `cordis.patch.yml`），按官方[打包与安装指南](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/user/develop/basic/publish.zh.md) 分发。三种安装方式：

## 🔗 链接

- [GitHub 仓库](https://github.com/bpc-oss/dsh-web-billing)
- [完整 README](https://github.com/bpc-oss/dsh-web-billing#readme)
- [返回dsh-web-billing所在分类](../plugins.md)
