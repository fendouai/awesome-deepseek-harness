---
title: "codex-eyes-hands"
description: "专为 DeepSeek Harness 打造：把本机 Codex CLI 变成纯文本 AI agent 的眼睛和手——看图/读文件/画图/监督执行/双通道容灾"
keywords: "codex-eyes-hands, vision, plugin, coding, multi-agent, deepseek harness, dsh"
---
# codex-eyes-hands

> ⭐ **4** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [651002](https://github.com/651002) | Updated | 2026-08-15 |
| Subcategory | 👁️ Vision tools | Capabilities | coding, multi-agent |

## One-liner

> 专为 DeepSeek Harness 打造：把本机 Codex CLI 变成纯文本 AI agent 的眼睛和手——看图/读文件/画图/监督执行/双通道容灾

## About

Harness 的 agent 若用无视觉模型（如 DeepSeek-V4-Pro），默认在 Web 里发图片会被网关拒绝 （弹「当前模型不支持图片」），图片根本到不了 agent。Web 附件的白名单也只有 4 种图片， 发 zip/exe/pdf 等文件会弹「仅支持 PNG、JPG、WebP、GIF 格式的图片」。 **解法**：给 `@deepseek-ai/dsh-host-apiproxy`（网关）+ `dsh-client-ui-conversation`（客户端）打一个小补丁—— 把**图片和任意文件落地成文件**、把**绝对路径以文本**注入 agent 消息，之后 agent 就能用本技能的 `see` 模式调 Codex 看图、用 `read` 模式或 pwsh 读文件了。 **对话记录里还会显示图片缩略图**（配套的适配器小补丁见补丁文档）。 - 补丁说明：[patches/dsh-image-gateway.md](patches/dsh-image-gateway.md) - **一键补丁脚本**：[patches/apply-dsh-gateway-patch.js](patches/apply-dsh-gateway-patch.js) （自动备份 + 校验 + 回滚，用法见文件头部注释；改完重启 dsh web、刷新页面生效）

## 🚀 Quick Start

```bash
node "C:\Users\<你>\.codex\skills\codex-bridge\scripts\bridge.js" see "C:\图.png" --ask "图里写了什么"
node "C:\Users\<你>\.codex\skills\codex-bridge\scripts\bridge.js" read "C:\某压缩包.zip" "C:\某文件夹"
node "C:\Users\<你>\.codex\skills\codex-bridge\scripts\bridge.js" watch "把某文件夹里的 txt 打包成 zip，不要删原文件"
node "C:\Users\<你>\.codex\skills\codex-bridge\scripts\bridge.js" shot "屏幕上有什么"
```

## 📚 Learn more

**安装**

1. 把本仓库放到你的技能目录，最终结构： `C:\Users\<你的用户名>\.codex\skills\codex-bridge\`（含 `SKILL.md` 与 `scripts\bridge.js`） 2. 打开 `SKILL.md`，把示例命令里的 `C:\Users\Administrator\...` 换成你自己的路径。 3. （可选）配置 Claude 备用通道： - 复制 `examples/claude.config.toml.example` → `C:\Users\<你>\.codex\claude.config.toml`， 把 `base_url` 换成你的中转地址、`model` 换成中转支持的 Claude 模型。 - 同时把同名的 `[model_providers.claude]` 注册进 `~/.codex/config.toml` （`codex e

**常见问题（FAQ）**

中转上游过载或限流。先等片刻重试；用 CC Switch 换一条通道；或加 `--backup only` 强制走 Claude 备用通道。 长期不稳可考虑换一家中转（见上方「推荐中转」）。 DSH 网关对无视觉模型拦截了图片。按 [patches/dsh-image-gateway.md](patches/dsh-image-gateway.md) 打补丁， 图片就会以文件路径到达 agent。 主配置 `~/.codex/config.toml` 里没注册 claude provider（`resume` 不加载 profile）。 按 `examples/claude.config.toml.example` 末尾的注释补一段即可。 不会。备用通道密钥由脚本运行时从你本机 CC Switch 数据库读取、只注入本次进程，不落盘；仓库本身不含任何密钥。 `node "...\scrip

## 🔗 Links

- [GitHub Repository](https://github.com/651002/codex-eyes-hands)
- [Full README](https://github.com/651002/codex-eyes-hands#readme)
- [Back to the Plugins list](../plugins.md)
