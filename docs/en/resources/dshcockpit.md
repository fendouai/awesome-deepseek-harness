---
title: "dshcockpit"
description: "DshCockpit — DeepSeek Harness 桌面驾驶舱 (desktop cockpit)：运行时自动更新、成本控制、全局快捷问询、定时任务、会话全文检索、数据安全。自动更新 / 成本中心 / Quick Ask / 定时任务 / 会话搜索"
keywords: "dshcockpit, desktop, client, coding, ui, deepseek harness, dsh"
---
# dshcockpit

> ⭐ **16** · ✅ active · client · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 16 | Status | ✅ active |
| Author | [Lxiayu](https://github.com/Lxiayu) | Updated | 2026-08-21 |

## One-liner

> DshCockpit — DeepSeek Harness 桌面驾驶舱 (desktop cockpit)：运行时自动更新、成本控制、全局快捷问询、定时任务、会话全文检索、数据安全。自动更新 / 成本中心 / Quick Ask / 定时任务 / 会话搜索

## About

**不是给 dsh 再套一个窗口——而是一个桌面控制平面。** DshCockpit 把 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（`dsh`）从一条终端命令变成常驻桌面的 Agent 服务：Harness 工作区保持 100% 原生，壳只在其外补齐安全更新、成本核算、后台任务、远程访问——全部通过稳定接口完成。内置运行时，无需安装 Node.js。 ---

## 📦 Install

```bash
git clone https://github.com/Lxiayu/DshCockpit.git && cd DshCockpit
npm install && npm start
```

## 🚀 Quick Start

```bash
> xattr -dr com.apple.quarantine /Applications/DshCockpit.app
>
```

## 📚 Learn more

**零侵入设计**

壳从不给上游源码打补丁，从不碰它的内部实现。所有集成只走稳定边界：HTTP/WebSocket、文件系统（会话日志）、CLI 参数（`--dump-config`、端口发现）与显式 IPC。"Harness 可以变，DshCockpit 保持有用"在这里是工程性质，不是口号。详见 [`DESIGN.md`](DESIGN.md)。

## 🔗 Links

- [GitHub Repository](https://github.com/Lxiayu/DshCockpit)
- [Full README](https://github.com/Lxiayu/DshCockpit#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
