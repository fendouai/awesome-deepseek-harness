---
title: "dsh-plugin-dev"
description: "插件开发踩坑与做法档案（skill + 文档）：cordis 双副本、tsconfig 三件套、Windows junction、多帧 zstd 实测。"
keywords: "dsh-plugin-dev, learning, skill, coding, deepseek harness, dsh"
---
# dsh-plugin-dev

> ⭐ **13** · ✅ 活跃 · 技能 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 技能 | 分类 | 学习 |
| 星数 | ⭐ 13 | 状态 | ✅ 活跃 |
| 作者 | [omdsh-dev](https://github.com/omdsh-dev) | 更新时间 | 2026-08-21 |

## 一句话介绍

> 插件开发踩坑与做法档案（skill + 文档）：cordis 双副本、tsconfig 三件套、Windows junction、多帧 zstd 实测。

## 详细介绍

1. 把 `skills/dsh-plugin-dev` 放进 skills 目录（或在 agent 会话中引用）； 2. 从 [SKILL.md](skills/dsh-plugin-dev/SKILL.md) 的流程与踩坑速查表入手； 3. 构建前看 [references/build-pitfalls.md](skills/dsh-plugin-dev/references/build-pitfalls.md)——第一条就是 cordis 双副本。

## 🚀 快速开始

```bash
dsh --version && readlink ~/.dsh/source/current     # 快照
node -v                                              # Node
gh --version && gh auth status                       # gh 与认证
node <mono>/node_modules/typescript/bin/tsc --version  # TS（<mono> 换成 current 真实路径）
node <mono>/node_modules/vitest/vitest.mjs --version   # Vitest
```

## 🔗 链接

- [GitHub 仓库](https://github.com/omdsh-dev/dsh-plugin-dev)
- [完整 README](https://github.com/omdsh-dev/dsh-plugin-dev#readme)
- [返回dsh-plugin-dev所在分类](../skills.md)
