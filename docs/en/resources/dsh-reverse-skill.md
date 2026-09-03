---
title: "dsh-reverse-skill"
description: "Complete reverse-skill (85 SKILL.md) as a DeepSeek Harness (dsh) Cordis plugin — reverse engineering, authorized pentesting and security research skill pack."
keywords: "dsh-reverse-skill, learning, skill, coding, search, deepseek harness, dsh"
---
# dsh-reverse-skill

> ⭐ **58** · ✅ active · skill · ⬆️ +7 recently

| | | | |
|---|---|---|---|
| Type | skill | Category | Learning |
| Stars | ⭐ 58 | Status | ✅ active |
| Author | [dhicoc](https://github.com/dhicoc) | Updated | 2026-08-17 |

## One-liner

> Complete reverse-skill (85 SKILL.md) as a DeepSeek Harness (dsh) Cordis plugin — reverse engineering, authorized pentesting and security research skill pack.

## About

本仓库内容仅用于 **授权的** 逆向工程、渗透测试与安全研究。使用者须确保对目标系统拥有合法授权。一切未授权行为与本仓库无关。 ---

## 📦 Install

```bash
# 安装 peer 依赖（cordis / dsh-skill 由 dsh 运行时提供，这里用于类型与构建）
npm install
npm run build        # tsc → 生成 lib/ 与 lib/types/
```

## 🚀 Quick Start

```bash
"main": "lib/index.js",
"types": "lib/types/index.d.ts",
"peerDependencies": {
  "@deepseek-ai/cordis": "^4.0.1",
  "@deepseek-ai/dsh-skill": "^0.0.1-rc.1"
}
```

## 📚 Learn more

**安装 peer 依赖（cordis / dsh-skill 由 dsh 运行时提供，这里用于类型与构建）**

npm install npm run build # tsc → 生成 lib/ 与 lib/types/ `package.json` 中已声明： "main": "lib/index.js", "types": "lib/types/index.d.ts", "peerDependencies": { "@deepseek-ai/cordis": "^4.0.1", "@deepseek-ai/dsh-skill": "^0.0.1-rc.1" }

**从 GitHub 安装并激活（推荐）**

dsh plugin add github:dhicoc/dsh-reverse-skill 安装后 dsh 会读取 `cordis.patch.yml` 把 `reverse-skill` 这个 Cordis 插件插入当前 profile，启动时自动注册 87 个技能。若你想在 profile / package 配置里手动引用，包名是 `@dhicoc/dsh-reverse-skill`：

**dsh 配置（示例，键名可能因版本而异）**

plugins: - "@dhicoc/dsh-reverse-skill" 加载后，插件在 `apply(ctx)` 里调用 `ctx.skills.registerProvider(...)`，把 87 个技能注册进 `ctx.skills`。模型可通过 `ctx.skills` → `tool-skill` 自动调用，用户也可通过技能名手动调用（受各 SKILL.md 的 `user-invocable` 控制）。

**插件工作原理（数据驱动，零手写清单）**

`src/index.ts` 不做任何硬编码候选列表，而是： 1. 递归遍历 `skills/` 与 `CTF-Sandbox-Orchestrator/`，找到每个 `SKILL.md`； 2. 解析前导 matter（把 `metadata.user-invocable` 提升为顶层 `user-invocable`；上游文件原样打包，CRLF / BOM 在运行时归一化）； 3. 构造 `SkillCandidate`（含 `resourceBase: {kind:'directory', path}`、结果缓存）； 4. 注册一个 `SkillProvider`，`get()` 时返回完整 body。 新增/删除技能只需改目录，插件自动同步。

## 🔗 Links

- [GitHub Repository](https://github.com/dhicoc/dsh-reverse-skill)
- [Full README](https://github.com/dhicoc/dsh-reverse-skill#readme)
- [Back to the Skills list](../skills.md)
