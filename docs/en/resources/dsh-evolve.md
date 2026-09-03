---
title: "dsh-evolve"
description: "自进化插件：agent 在 session 内随对话给自己长出/剪掉能力 —— evolve_add 热挂载持久化 cordis 插件（下一 step 工具即可见），evolve_remove 可逆卸载，重启自动恢复"
keywords: "dsh-evolve, developer, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-evolve

> ⭐ **12** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 12 | Status | ✅ active |
| Author | [william-jin-cmu](https://github.com/william-jin-cmu) | Updated | — |
| Subcategory | 📁 Files & import | Capabilities | coding, multi-agent |

## One-liner

> 自进化插件：agent 在 session 内随对话给自己长出/剪掉能力 —— evolve_add 热挂载持久化 cordis 插件（下一 step 工具即可见），evolve_remove 可逆卸载，重启自动恢复

## About

自进化 harness 插件：**agent 在 session 内随对话给自己长出/剪掉能力**。用户的表述暴露出一个缺口（反复要查的表、天天要算的换算、老要看的端点），agent 现场写一个 cordis 插件挂载给自己——新工具在**下一个 step**就可调用；不再需要时可逆卸载；重启自动恢复。 进化不限于工具。evolution 是完整的 cordis 插件：常驻 system prompt 规则、`agent/step` / `agent/settled` 事件钩子、定时器主动唤醒 agent——**改行为、而不只是加能力**的进化，同样一次 `evolve_add` 完成（[三条非工具实录](#不止工具改行为的进化)）。 依据的机制：dsh 的工具列表每个 step 都从当前挂载的插件实时重算（无 session 级快照），cordis 4 的 fiber 具有可回滚 effect——挂载即生效，dispose 即净。

## ✨ Key Features

- **`evolve_add(name, source, description?, config?)`** — 把一段纯 ESM cordis 插件源码持久化到 evolve store（`~/.dsh/evolve/<name>.mjs` + manifest），并热挂载。同名再次调用即替换（旧 fiber 先完整卸
- **`evolve_remove(name, keepSource?)`** — 卸载 fiber（它注册的工具/监听/服务全部自动清理）、移出 manifest、删除源码。
- **`evolve_list()`** — 每个 evolution 的名称、fiber 状态、版本、用途。

## 📦 Install

```bash
scripts/build.sh                 # 见下
dsh plugin --profile web add .   # 追加为该 profile 的 bundle 层
```

## 📚 Learn more

**安装**

本插件是标准 Profile Bundle：`package.json` 的 `dsh.bundle` 指向 `cordis.patch.yml`，patch 按包名（而非绝对路径）挂载，dsh 版本升级后挂载不再失效。构建后从 checkout 安装进 profile： scripts/build.sh # 见下 dsh plugin --profile web add . # 追加为该 profile 的 bundle 层 卸载：`dsh plugin --profile web remove @dsh-external/dsh-evolve`。另一条互斥通道是 plugin-registry（`dsh registry`，读 `dsh.plugin.json` 增量清单）——同一部署二选一，不要双挂载。 构建：`scripts/build.sh`（需要 `dsh` 在 PATH，或设

## 🔗 Links

- [GitHub Repository](https://github.com/william-jin-cmu/dsh-evolve)
- [Full README](https://github.com/william-jin-cmu/dsh-evolve#readme)
- [Back to the Plugins list](../plugins.md)
