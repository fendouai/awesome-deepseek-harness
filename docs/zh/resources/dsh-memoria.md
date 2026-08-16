---
title: "dsh-memoria"
description: "向量 + 图记忆后端：命名空间隔离、自动观察、召回、重要性处理与热重载。"
keywords: "dsh-memoria, memory, plugin, context, deepseek harness, dsh"
---
# dsh-memoria

> ⭐ 0 · 🧪 实验性 · 插件

## 一句话介绍

向量 + 图记忆后端：命名空间隔离、自动观察、召回、重要性处理与热重载。

## 详细介绍

memoria 记忆后端插件：把 [memoria](https://github.com/jiayan-xu/memoria)（向量 + 图记忆层）接入 DeepSeek Harness (dsh)，让 dsh agent 会话可以**记住**和**回忆**。 - 4 个工具：`memoria_observe` / `memoria_remember` / `memoria_search` / `memoria_recall` - 自动写入：每轮对话结束自动 `observe` 沉淀；用户肯定反馈（不错/很好/good/赞…）自动 `remember`（importance=5） - 配置热重载：改 `~/.dsh/settings.yaml` 的 `memoria:` section 免重启生效 - 命名空间隔离：所有读写强制落在配置的 namespace（默认 `dsh-test`），不碰其他业务数据

## 作者
**[jiayan-xu](https://github.com/jiayan-xu)**

## 链接

- [GitHub 仓库](https://github.com/jiayan-xu/dsh-memoria)
- [完整 README](https://github.com/jiayan-xu/dsh-memoria#readme)
- [返回dsh-memoria所在分类](../plugins.md)
