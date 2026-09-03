---
title: "dsh-plugin-session-delete"
description: "Delete DeepSeek Harness sessions from the UI: header danger button + sidebar session-row menu item (no conversation jump), risk-consent dialog with session name/id, stops running agents first, in-place list refresh without page reload. Works in web and the desktop client."
keywords: "dsh-plugin-session-delete, desktop, client, coding, multi-agent, ui, deepseek harness, dsh"
---
# dsh-plugin-session-delete

> ⭐ **26** · ✅ 活跃 · 客户端 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 26 | 状态 | ✅ 活跃 |
| 作者 | [lsz-asd](https://github.com/lsz-asd) | 更新时间 | 2026-08-14 |

## 一句话介绍

> Delete DeepSeek Harness sessions from the UI: header danger button + sidebar session-row menu item (no conversation jump), risk-consent dialog with session name/id, stops running agents first, in-place list refresh without page reload. Works in web and the desktop client.

## 详细介绍

你是否困扰于 web 端无法删除对话？是否觉得归档对话键只是隐藏对话，删除得不够彻底？是否在尝试编辑 harness 时遇到对话话历史无法同步，而损坏的对话又无法删除？这个插件可以帮你！ **在 DeepSeek Harness 界面里安全地彻底删除会话。** 在会话顶部添加垃圾桶按钮，侧栏会话行 "..." 菜单内添加"删除会话"项，点击后出现风险确认弹窗（需勾选）；确认后会删除会话日志、投影缓存与工作区记账；运行中的会话会有提示，若仍选择删除会停止运行并删除。可在web中使用，并且理论上兼容一切web套壳的客户端。 **添加agent工具让agent可以删除会话。** 工具名`workbench_session_delete`

## ✨ 核心特性

- 会话头部垃圾桶按钮
- 侧栏会话行 "..." 菜单注入"删除会话"项
- `RiskConfirmation` 风险确认：勾选"我已了解后果"后确认可用
- 删除链路：会话目录 + 投影缓存 + 工作区记账（经活动 storageDomain，内存/磁盘一致）
- `workbench_session_delete` 工具：agent 可直接删除会话

## 📦 安装

```bash
dsh plugin --profile <profile> add file:C:/path/to/dsh-plugin-session-delete
```

## 📚 更多信息

**安装**

dsh plugin --profile <profile> add file:C:/path/to/dsh-plugin-session-delete 重启 profile 生效。

**Installation**

dsh plugin --profile <profile> add file:C:/path/to/dsh-plugin-session-delete Restart the profile to apply.

## 🔗 链接

- [GitHub 仓库](https://github.com/lsz-asd/dsh-plugin-session-delete)
- [完整 README](https://github.com/lsz-asd/dsh-plugin-session-delete#readme)
- [返回dsh-plugin-session-delete所在分类](../clients.md)
