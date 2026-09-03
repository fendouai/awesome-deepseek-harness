---
title: "dsh-restart"
description: "Restart DSH: configurable restart method (Node native / legacy PowerShell), post-restart continue prompt, optional watchdog auto-relaunch."
keywords: "dsh-restart, discovery, plugin, coding, deepseek harness, dsh"
---
# dsh-restart

> ⭐ **6** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 插件发现 |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [anweat](https://github.com/anweat) | 更新时间 | 2026-08-14 |

## 一句话介绍

> Restart DSH: configurable restart method (Node native / legacy PowerShell), post-restart continue prompt, optional watchdog auto-relaunch.

## 详细介绍

重启整个 DeepSeek Harness 进程的插件，用于重新加载插件与配置（profile 的 cordis 组合、settings 等）。host + client 双半，装进 profile 的 bundle 后即可用。

## ✨ 核心特性

- **模型工具 `restart_harness`**：让 agent 直接安排一次进程重启（可选 `delayMs`）。
- **`/restart` 斜杠命令**：在 UI 里手动触发重启。
- **配置卡片**（设置 → 插件 → 插件配置 → 「DSH 重启」）：可视化编辑以下设置，改动即时写入 `settings.yaml`：
- **「立即重启」按钮**：先读取当前进程身份，安排重启后等待新进程恢复并自动刷新页面。只读 GET 返回 `{ pid, startedAt }`；出于安全考虑，重启 POST 仍仅接受来自环回地址（127.0.0.1 / localhost）的同源请求，经反向代理/远程访问时会被拒绝（403）。

## 📦 安装

```bash
pnpm install
node scripts/link-dsh-workspace.mjs --source <path-to-deepseek-harness>
pnpm run build
```

## 🚀 快速开始

```bash
// profiles/<profile>/package.json
{
  "dependencies": { "dsh-restart": "..." },
  "dsh": { "profile": { "bundles": ["...", "dsh-restart"] } }
}
```

## 📚 更多信息

**安装**

1. 把包加入 profile 依赖并挂进 bundle： // profiles/<profile>/package.json { "dependencies": { "dsh-restart": "..." }, "dsh": { "profile": { "bundles": ["...", "dsh-restart"] } } } 2. 重启 DSH（`/restart` 或 `restart_harness`），刷新页面后即可看到卡片；之后通过卡片重启时会自动等待并恢复页面。

## 🔗 链接

- [GitHub 仓库](https://github.com/anweat/dsh-restart)
- [完整 README](https://github.com/anweat/dsh-restart#readme)
- [返回dsh-restart所在分类](../plugins.md)
