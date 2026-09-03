---
title: "dsh-blue-whale-maid"
description: "DeepSeek Harness Web 的蓝鲸女仆桌宠，任务有动静时会在页面边上提醒你。"
keywords: "dsh-blue-whale-maid, search, plugin, coding, deepseek harness, dsh"
---
# dsh-blue-whale-maid

> ⭐ **6** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [yuxino](https://github.com/yuxino) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding |

## One-liner

> DeepSeek Harness Web 的蓝鲸女仆桌宠，任务有动静时会在页面边上提醒你。

## About

装好以后，她会待在 DSH Web 右下角。任务开始时跟着忙；轮到你确认、这一轮结束或者出了问题，她会换个动作，再冒个泡提醒你。 平时可以把她拖到顺手的位置。点一下，她会挥手；双击一下，她会跳起来。点旁边的余额按钮，还能看看 DeepSeek 余额、今天大概花了多少，以及当前会话用了多少钱。 她只说自己能确定的事。比如一轮结束了，她会告诉你“结束了”，不会擅自说“成功了”。

## ✨ Key Features

- API Key 由 DSH 服务端读取，不会传给浏览器；桌宠界面只访问本机接口。
- “今日约消费”根据本机当天的余额变化估算，不是官方账单。
- “本会话已用”只计算来源明确、价格已知的 DeepSeek 官方模型；最终费用以 [DeepSeek 控制台](https://platform.deepseek.com/usage) 为准。

## 📦 Install

```bash
npx @deepseek-ai/dsh plugin --profile web add github:yuxino/dsh-blue-whale-maid
```

## 🚀 Quick Start

```bash
npx @deepseek-ai/dsh web
```

## 📚 Learn more

**安装**

需要 Node.js `^22.19.0` 或 `>=24.0.0`、`pnpm`，以及可用的 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) Web profile。下面沿用 DSH 官方的无版本号命令。 npx @deepseek-ai/dsh plugin --profile web add github:yuxino/dsh-blue-whale-maid 装好后重启 DSH Web： npx @deepseek-ai/dsh web 余额与费用面板需要当前 profile 配置 `DEEPSEEK_API_KEY`；没有 Key 时，桌宠和任务提醒照常能用。

**费用说明**

<details> <summary><strong>更新与卸载</strong></summary> 更新： npx @deepseek-ai/dsh plugin --profile web update dsh-blue-whale-maid 卸载： npx @deepseek-ai/dsh plugin --profile web remove dsh-blue-whale-maid 更新或卸载后都要重启 DSH Web。 </details> <details> <summary><strong>本地开发</strong></summary> npm run build npm test npm run check 让 Web profile 直接使用当前仓库： npx @deepseek-ai/dsh plugin --profile web add . npx @deepse

## 🔗 Links

- [GitHub Repository](https://github.com/yuxino/dsh-blue-whale-maid)
- [Full README](https://github.com/yuxino/dsh-blue-whale-maid#readme)
- [Back to the Plugins list](../plugins.md)
