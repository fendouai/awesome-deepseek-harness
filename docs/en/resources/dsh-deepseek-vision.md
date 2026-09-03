---
title: "dsh-deepseek-vision"
description: "Vision-language gateway plugin for DeepSeek Harness - paste an image, DeepSeek sees text"
keywords: "dsh-deepseek-vision, vision, plugin, coding, multimodal, deepseek harness, dsh"
---
# dsh-deepseek-vision

> ⭐ **8** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 8 | Status | ✅ active |
| Author | [siegfly](https://github.com/siegfly) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding, multimodal |

## One-liner

> Vision-language gateway plugin for DeepSeek Harness - paste an image, DeepSeek sees text

## About

**安装：** `dsh plugin --profile web add dsh-deepseek-vision` **dsh-deepseek-vision 是给 DeepSeek Harness 的视觉语言网关插件。** 纯文本的 DeepSeek 编程模型 通过一个"网关"provider 路由获得贴图能力：目录声明支持 image 的模型（官方 `deepseek-v4-flash-vision-exp`）图片直通原生视觉端点；其余模型先由可配置的视觉模型 （默认 Qwen-VL）逐字描述成文字，再交给 DeepSeek 继续写代码。官方仓库零改动、跨机器 安装不锁官方版本。同类方案里它是**最薄的桥**：不注入 agent 工具、不经过第三方中转、 不依赖本地模型。 [English](README.en.md) | [中文](README.md)

## ✨ Key Features

- **贴图即用，不用换模型：** 注册独立路由 `deepseek-vision`（显示名 *DeepSeek + Vision*），
- **每张图只描述一次：** 按 `attachmentId` 进程内 LRU 缓存，重试、上下文压缩、后续轮次
- **会话不变量保持：** 原始图片仍持久化进 session log，历史 / 回放 / 重构不受影响。
- **官方机制安装：** bundle 声明 + `dsh plugin add`，四种 spec（npm / git / 目录 / tarball）、
- **换 VL 模型零改码：** 端点 / 模型 / 提示词 / 密钥全在设置卡片，兼容任意
- **失败语义明确：** 默认 fail-closed，稳定错误码（`AUTH` / `TIMEOUT` / `TRANSPORT` /
- **跨版本不锁死：** 发布版不锁定官方 dsh 版本。无 CLI 复刻路径（`pnpm

## 📦 Install

```bash
npm install -g @deepseek-ai/dsh        # 推荐：dsh 永久进入 PATH，之后命令直接敲
# 或（官方一行启动方式）：
npx @deepseek-ai/dsh web               # 不装全局：CLI 只在 npx 缓存里运行，不会进 PATH
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add github:siegfly/dsh-deepseek-vision#<sha>
# 没装全局、走 npx 时：
npx @deepseek-ai/dsh plugin --profile web add github:siegfly/dsh-deepseek-vision#<sha>
```

## 📚 Learn more

**工作原理**

flowchart LR User["聊天窗贴图 / read_image / 截图 / MCP / ACP"] --> Gate["deepseek-vision 路由：inputModalities = text + image"] Gate --> Persist["apiproxy prompt RPC → ImageBlock 持久化进 session log"] Persist --> Decide{"DeepSeek 目录声明该模型支持 image？"} Decide -- "是（官方视觉模型）" --> Native["yield* super.stream()：父类原生序列化图片，直通 DeepSeek 视觉端点"] Decide -- "否（纯文本 / 未列目录）" --> Bridge["ImageBridge：改写图片块（含 tool-result 嵌套）"] VL

**配置**

全部可省略（走默认值）。两个 key 都支持 credential-ref（环境变量名）。已挂载 dsh 的 `credentials` 服务时，其解析结果（即使未配置）具有权威性；只有服务缺席才直接读取启动环境。 官方 `credentials-local` 的优先级是：**进程环境变量（最高、只读）→ GUI 管理的 `.credentials.yaml` → `.env` 回退**。因此 Web Models 页写入的凭据可用，而本次进程显式 导出的 key 始终优先且不能在 GUI 内修改： `llm-vl-gateway` 也是一个 settings namespace，三个编辑入口：**设置 → 插件 → 插件配置** 的"DeepSeek + Vision（视觉语言桥接）"卡片（`vl.*` 全字段 + VL 密钥）、Web Models 页 （`deepseek.*` 子段

**使用**

1. 设置两个 key：**设置 → 插件 → 插件配置 → "DeepSeek + Vision（视觉语言桥接）"** 卡片里填 VL 密钥（写入凭据存储，不出现在任何响应/设置里）；DeepSeek key 沿用现有凭据； 2. Models 页选择 provider **DeepSeek + Vision**（会话内切换即持久化为默认）； 3. 聊天窗贴图，发消息——图片自动被描述，DeepSeek 看到的是文字。 设置卡片是本插件的**客户端面**（`dsh.client`）：以官方解耦插件的方式注册进 `settings.plugin.item` 槽位，编辑 `llm-vl-gateway.vl` 段，与官方内置卡片（终端 / Agent 循环 / 网页搜索）同机制、同交互（暂存草稿、覆盖状态显示、保存时整体写入）。

**安装**

安装走**官方 bundle 机制**：本包在 `package.json` 声明 `dsh.bundle.patch`（指向包内 `cordis.patch.yml`），`dsh plugin add` 把包链接进 profile 并把包名对账进 profile manifest 的 `dsh.profile.bundles` 层栈，loader 启动时按层挂载——**不需要手工往 `cordis.patch.yml` 加任何行**（旧版本加过的受管块会在下次安装/卸载时自动迁移移除）。 四种 spec 任选（日常推荐 git 形式，锁 commit）： dsh plugin --profile web add github:siegfly/dsh-deepseek-vision#<sha> # git（推荐），锁 commit dsh plugin --profile web add 

## 🔗 Links

- [GitHub Repository](https://github.com/siegfly/dsh-deepseek-vision)
- [Full README](https://github.com/siegfly/dsh-deepseek-vision#readme)
- [Back to the Plugins list](../plugins.md)
