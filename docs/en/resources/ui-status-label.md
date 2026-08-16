---
title: "ui-status-label"
description: "Customize the whale's 'Deep diving' status label into anything you want."
keywords: "ui-status-label, ui, plugin, deepseek harness, dsh"
---
# ui-status-label

> ⭐ 32 · ✅ active · plugin

## One-liner

Customize the whale's 'Deep diving' status label into anything you want.

## About

把你的鲸鱼娘思考时的 deep diving 自定义成任意你想要的样子。 为 **dsh Web** 聊天视图提供可配置的运行中轮次状态文案：General 设置区的一行文本输入，插件把聊天视图运行状态栏的文案替换为你输入的文字（支持 DOM 注入和上游 `conversationStatus` 服务两条路径，见[兼容性](#兼容性)）。插件注册持久的 `ui-status-label` settings 命名空间（默认 `小难梁在0721`）；在设置行输入新文字后，聊天视图在轮次运行期间（等待首 token、工具执行、流式输出）显示的状态文案随之更新。选择持久化在 `$DSH_HOME/settings.yaml`，跟随同一个用户 home 跨越 Web 端口。

## Author
**[alingalingling](https://github.com/alingalingling)**

## Links

- [GitHub Repository](https://github.com/alingalingling/ui-status-label)
- [Full README](https://github.com/alingalingling/ui-status-label#readme)
- [Back to the Plugins list](../plugins.md)
