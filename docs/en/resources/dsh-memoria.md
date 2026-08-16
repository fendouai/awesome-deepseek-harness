---
title: "dsh-memoria"
description: "Vector + graph memory backend with namespace isolation, automatic observation, recall, importance handling and hot reload."
keywords: "dsh-memoria, memory, plugin, context, deepseek harness, dsh"
---
# dsh-memoria

> ⭐ 0 · 🧪 experimental · plugin

## One-liner

Vector + graph memory backend with namespace isolation, automatic observation, recall, importance handling and hot reload.

## About

memoria 记忆后端插件：把 [memoria](https://github.com/jiayan-xu/memoria)（向量 + 图记忆层）接入 DeepSeek Harness (dsh)，让 dsh agent 会话可以**记住**和**回忆**。 - 4 个工具：`memoria_observe` / `memoria_remember` / `memoria_search` / `memoria_recall` - 自动写入：每轮对话结束自动 `observe` 沉淀；用户肯定反馈（不错/很好/good/赞…）自动 `remember`（importance=5） - 配置热重载：改 `~/.dsh/settings.yaml` 的 `memoria:` section 免重启生效 - 命名空间隔离：所有读写强制落在配置的 namespace（默认 `dsh-test`），不碰其他业务数据

## Author
**[jiayan-xu](https://github.com/jiayan-xu)**

## Links

- [GitHub Repository](https://github.com/jiayan-xu/dsh-memoria)
- [Full README](https://github.com/jiayan-xu/dsh-memoria#readme)
- [Back to the Plugins list](../plugins.md)
