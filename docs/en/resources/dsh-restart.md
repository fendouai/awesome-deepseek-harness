---
title: "dsh-restart"
description: "Restart DSH: configurable restart method (Node native / legacy PowerShell), post-restart continue prompt, optional watchdog auto-relaunch."
keywords: "dsh-restart, discovery, plugin, coding, deepseek harness, dsh"
---
# dsh-restart

> ⭐ **6** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Plugin discovery |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [anweat](https://github.com/anweat) | Updated | 2026-08-14 |

## One-liner

> Restart DSH: configurable restart method (Node native / legacy PowerShell), post-restart continue prompt, optional watchdog auto-relaunch.

## About

重启整个 DeepSeek Harness 进程的插件，用于重新加载插件与配置（profile 的 cordis 组合、settings 等）。host + client 双半，装进 profile 的 bundle 后即可用。

## ✨ Key Features

- **模型工具 `restart_harness`**：让 agent 直接安排一次进程重启（可选 `delayMs`）。
- **`/restart` 斜杠命令**：在 UI 里手动触发重启。
- **配置卡片**（设置 → 插件 → 插件配置 → 「DSH 重启」）：可视化编辑以下设置，改动即时写入 `settings.yaml`：
- **「立即重启」按钮**：先读取当前进程身份，安排重启后等待新进程恢复并自动刷新页面。只读 GET 返回 `{ pid, startedAt }`；出于安全考虑，重启 POST 仍仅接受来自环回地址（127.0.0.1 / localhost）的同源请求，经反向代理/远程访问时会被拒绝（403）。

## 📦 Install

```bash
pnpm install
node scripts/link-dsh-workspace.mjs --source <path-to-deepseek-harness>
pnpm run build
```

## 🚀 Quick Start

```bash
// profiles/<profile>/package.json
{
  "dependencies": { "dsh-restart": "..." },
  "dsh": { "profile": { "bundles": ["...", "dsh-restart"] } }
}
```

## 📚 Learn more

**安装**

1. 把包加入 profile 依赖并挂进 bundle： // profiles/<profile>/package.json { "dependencies": { "dsh-restart": "..." }, "dsh": { "profile": { "bundles": ["...", "dsh-restart"] } } } 2. 重启 DSH（`/restart` 或 `restart_harness`），刷新页面后即可看到卡片；之后通过卡片重启时会自动等待并恢复页面。

## 🔗 Links

- [GitHub Repository](https://github.com/anweat/dsh-restart)
- [Full README](https://github.com/anweat/dsh-restart#readme)
- [Back to the Plugins list](../plugins.md)
