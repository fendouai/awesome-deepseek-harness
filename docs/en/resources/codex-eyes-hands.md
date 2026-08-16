---
title: "codex-eyes-hands"
description: "专为 DeepSeek Harness 打造：把本机 Codex CLI 变成纯文本 AI agent 的眼睛和手——看图/读文件/画图/监督执行/双通道容灾"
keywords: "codex-eyes-hands, vision, plugin, coding, multi-agent, deepseek harness, dsh"
---
# codex-eyes-hands

> ⭐ 4 · ✅ active · plugin

## One-liner

专为 DeepSeek Harness 打造：把本机 Codex CLI 变成纯文本 AI agent 的眼睛和手——看图/读文件/画图/监督执行/双通道容灾

## About

Harness 的 agent 若用无视觉模型（如 DeepSeek-V4-Pro），默认在 Web 里发图片会被网关拒绝 （弹「当前模型不支持图片」），图片根本到不了 agent。 **解法**：给 `@deepseek-ai/dsh-host-apiproxy` 打一个小补丁——把图片**落地成文件**、把**绝对路径 以文本**注入 agent 消息，之后 agent 就能用本技能的 `see` 模式调 Codex 看图了。 **对话记录里还会显示图片缩略图**（配套的适配器小补丁见补丁文档）。 - 补丁说明：[patches/dsh-image-gateway.md](patches/dsh-image-gateway.md) - **一键补丁脚本**：[patches/apply-dsh-gateway-patch.js](patches/apply-dsh-gateway-patch.js) （自动备份 + 校验 + 回滚，用法见文件头部注释；改完重启 dsh web 生效）

## Author
**[651002](https://github.com/651002)**

## Links

- [GitHub Repository](https://github.com/651002/codex-eyes-hands)
- [Full README](https://github.com/651002/codex-eyes-hands#readme)
- [Back to the Plugins list](../plugins.md)
