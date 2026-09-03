---
title: "dsh-deepseek-quota"
description: "DeepSeek API quota (balance) widget for the DSH web GUI: a floating bottom-right card showing remaining DeepSeek API balance."
keywords: "dsh-deepseek-quota, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-deepseek-quota

> ⭐ **4** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [yingjunnan](https://github.com/yingjunnan) | Updated | 2026-08-14 |
| Subcategory | 📊 Status & stats | Capabilities | coding |

## One-liner

> DeepSeek API quota (balance) widget for the DSH web GUI: a floating bottom-right card showing remaining DeepSeek API balance.

## About

A [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (DSH) **web GUI** plugin: shows your remaining **DeepSeek API quota (balance)** and **today's consumption** in a floating card pinned to the **bottom-right corner** of the page. ---

## ✨ Key Features

- 右下角悬浮卡片（注册在框架级 `shell.overlay` 槽位，纯叠加、不遮挡应用）。
- 显示**总余额**、可用状态、**当前对话费用**、**今日已消费**、**赠送余额**与**充值余额**。
- **当前对话费用**：宿主侧对每条 `assistant/message` 按官方价格表计价（含 2026-08-17 起峰谷定价；定价引擎移植自 [dsh-web-billing](https://github.com/bpc-oss/dsh-web-billing)，MIT），通过 `GET /api/deepse
- 余额每 60 秒自动刷新、对话费用每 5 秒刷新，也可手动刷新。
- **峰谷时段提示**：显示当前处于 DeepSeek 的**高峰**（工作日 09:00–12:00 / 14:00–18:00，北京时间）还是**空闲**时段（2026-08-17 起；**周六、周日全天空闲**），让你知道现在跑模型更贵还是更便宜；随余额每 60 秒刷新。
- **可折叠为小钱包图标**：点卡头右下角的箭头即可把卡片收成右下角的一个**小钱包图标**（点击可展开）；折叠态下钱包图标会以颜色标识当前峰谷（高峰=红、空闲=绿、常规=灰）或错误状态，颜色随余额每 60 秒刷新。
- 自动跟随应用浅色/深色主题（使用 `--dsw-*` 设计变量）。
- 明确的错误状态：未配置 Key、网络失败、接口报错等。

## 📦 Install

```bash
# 已安装 dsh CLI：
dsh plugin --profile web add dsh-deepseek-quota

# 未安装 dsh CLI（例如通过 npx 启动）：
npx @deepseek-ai/dsh plugin --profile web add dsh-deepseek-quota
```

## 🚀 Quick Start

```bash
> - insert:
>     - id: deepseek-quota
>       name: dsh-deepseek-quota
>
```

## 📚 Learn more

**中文说明**

一个给 DeepSeek Harness（DSH）**网页界面**用的插件：在页面**右下角**悬浮显示你的 **DeepSeek API 额度（余额）** 与 **今日消费**。

**未安装 dsh CLI（例如通过 npx 启动）：**

npx @deepseek-ai/dsh plugin --profile web add dsh-deepseek-quota 该包声明了 `dsh.bundle`，`dsh plugin` 会自动把它加进 profile 的 bundle 层（无需手动改配置）。之后： 1. 重启网页应用：`dsh web`（若无 dsh CLI，用 `npx @deepseek-ai/dsh web`；bundle 层在启动时读取）。 2. 打开 http://127.0.0.1:3080 并刷新页面。 3. 右下角即出现额度卡片。 > 手动方式：把包放进 profile 的 `node_modules`，并在 `~/.dsh/profiles/web/cordis.patch.yml` 中加一条： > > ```yaml > - insert: > - id: deepseek-quota > na

**配置**

插件读取的正是 harness 自己在用的那个 Key：`DEEPSEEK_API_KEY`（通过凭证服务解析；在 **设置 → 模型** 页面填写，存于 `~/.dsh/.credentials.yaml`，或在启动环境中导出）。

**本地安装测试：**

dsh plugin --profile web add . # 无 dsh CLI 时：npx @deepseek-ai/dsh plugin --profile web add . 修改 `lib/client.js` 后需重启 `dsh web`（无 dsh CLI 时用 `npx @deepseek-ai/dsh web`）以重新生成引导哈希（`rev`），再强制刷新页面。

## 🔗 Links

- [GitHub Repository](https://github.com/yingjunnan/dsh-deepseek-quota)
- [Full README](https://github.com/yingjunnan/dsh-deepseek-quota#readme)
- [Back to the Plugins list](../plugins.md)
