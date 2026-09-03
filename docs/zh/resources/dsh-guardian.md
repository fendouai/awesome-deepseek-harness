---
title: "dsh-guardian"
description: "Agent 安全护栏：拦截并审计所有工具调用，命中敏感操作就要求人工确认。"
keywords: "dsh-guardian, security, plugin, deepseek harness, dsh"
---
# dsh-guardian

> ⭐ **4** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 安全 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [cdxiaodong](https://github.com/cdxiaodong) | 更新时间 | 2026-08-21 |

## 一句话介绍

> Agent 安全护栏：拦截并审计所有工具调用，命中敏感操作就要求人工确认。

## 详细介绍

LLM Agent（Claude Code / DeepSeek Harness）能自主执行 shell、读写文件、发网络请求。一旦被**提示注入**、**工具投毒**或**模型误判**带偏，可能在你不知情时 `rm -rf`、读取 `.ssh/id_rsa`、把密钥外泄到远程。本插件是一道**运行时安全网**： Agent 想执行工具 → guardian/check 前置审查 → 命中规则 → 拦截 / 人工批准 → 才放行

## ✨ 核心特性

- **路径沙箱**（`guardian/path`）：realpath 解析 + 白名单根目录 + 编码变体解码 + 空字节截断检测——比纯正则可靠
- **风险评分引擎**（`risk.ts`）：多信号并集概率式加权成 0~1 分，按阈值分级处置（deny/block/warn/allow）

## 📦 安装

```bash
dsh plugin --profile web add github:cdxiaodong/dsh-guardian
```

## 🚀 快速开始

```bash
npm ci && npm test     # 19/19 通过
```

## 🔗 链接

- [GitHub 仓库](https://github.com/cdxiaodong/dsh-guardian)
- [完整 README](https://github.com/cdxiaodong/dsh-guardian#readme)
- [返回dsh-guardian所在分类](../plugins.md)
