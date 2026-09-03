---
title: "dsh-email"
description: "DeepSeek Harness 邮件插件：email_list/read/search/send/folders/attachment 六工具，内置 QQ/163/126/新浪/阿里/Gmail/Outlook/iCloud 八个预设，多账号、附件收发、Web 设置页配置，纯 Node 全平台。· IMAP/SMTP email tools for DeepSeek Harness agents."
keywords: "dsh-email, search, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-email

> ⭐ **6** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [STARDUSTLC666](https://github.com/STARDUSTLC666) | 更新时间 | 2026-08-18 |
| 子分类 | 🌐 网页搜索 | 能力 | coding, multi-agent, search |

## 一句话介绍

> DeepSeek Harness 邮件插件：email_list/read/search/send/folders/attachment 六工具，内置 QQ/163/126/新浪/阿里/Gmail/Outlook/iCloud 八个预设，多账号、附件收发、Web 设置页配置，纯 Node 全平台。· IMAP/SMTP email tools for DeepSeek Harness agents.

## 详细介绍

DeepSeek Harness 邮件工具插件：让 agent 能**查收件箱、读邮件、搜邮件、代发邮件、收发附件**。纯插件实现，零核心改动，安装即可用。 Email tools for DeepSeek Harness: list, read, search and send mail through standard IMAP/SMTP — with one-line presets for QQ / 163 / 126 / Sina / Aliyun / Gmail / Outlook / iCloud. 纯 Node 实现，**全平台通用**（Windows / macOS / Linux 同一份代码），不依赖 shell、无原生二进制。

## 📦 安装

```bash
dsh plugin --profile web add dsh-email
```

## 🚀 快速开始

```bash
dsh plugin --profile web remove dsh-email
```

## 📚 更多信息

**安装**

dsh plugin --profile web add dsh-email （或从 GitHub 安装：`dsh plugin --profile web add github:你的账号/dsh-email#<commit>`，随后按提示在 profile 的 `pnpm-workspace.yaml` 里授权 `prepare` 构建。） 装好后重启 `dsh web`。插件自带空配置，**不会弄崩启动**；配置前调用任何 email 工具都会返回明确的配置提示。 **配置方式有两种（任选其一）：** 1. **网页设置（推荐）**：重启后打开 **设置 → 邮件 (dsh-email)**，表单里填邮箱地址和授权码，点「保存并应用」，还带「测试连接」按钮。零 YAML、零重启。 2. **YAML**：按下面的 cordis.patch.yml 模板手写；设置页的「多账号（高级，YA

**配置**

在你 profile 的 `cordis.patch.yml` 里覆盖 `tool-email` 行（在 `$DSH_HOME/profiles/<name>/` 下），然后重启： config: provider: qq # qq | 163 | 126 | sina | aliyun | gmail | outlook | icloud user: you@qq.com password: 你的授权码 # 强烈建议改用环境变量 DSH_EMAIL_PASSWORD，见下 不需要预设？手填任意 IMAP/SMTP 服务器即可： config: user: you@corp.example password: 你的授权码 imap: { host: imap.corp.example, port: 993, secure: true } smtp: { host: smtp.corp.ex

## 🔗 链接

- [GitHub 仓库](https://github.com/STARDUSTLC666/dsh-email)
- [完整 README](https://github.com/STARDUSTLC666/dsh-email#readme)
- [返回dsh-email所在分类](../plugins.md)
