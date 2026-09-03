---
title: "dsh-calendar"
description: "DeepSeek Harness 日历插件：calendar_list/create/update/delete/search 五工具，CalDAV 协议支持 Google/iCloud/Nextcloud/自定义端点，RRULE 重复事件自动展开，插件级 proxyUrl 代理，配置缺失不崩启动；纯 Node 全平台。· CalDAV calendar tools for DeepSeek Harness agents."
keywords: "dsh-calendar, search, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-calendar

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [STARDUSTLC666](https://github.com/STARDUSTLC666) | Updated | 2026-08-18 |
| Subcategory | 🌐 Web search | Capabilities | coding, multi-agent, search |

## One-liner

> DeepSeek Harness 日历插件：calendar_list/create/update/delete/search 五工具，CalDAV 协议支持 Google/iCloud/Nextcloud/自定义端点，RRULE 重复事件自动展开，插件级 proxyUrl 代理，配置缺失不崩启动；纯 Node 全平台。· CalDAV calendar tools for DeepSeek Harness agents.

## About

DSH 社区插件：通过 CalDAV 读写日历事件。提供 5 个面向模型的工具（calendar_list / calendar_create / calendar_update / calendar_delete / calendar_search），支持 Google / iCloud / Nextcloud 及任意 CalDAV 服务器。本轮为 node 半身，不含设置页 UI，配置全部走 profile 的 cordis.patch.yml。

## 📦 Install

```bash
dsh plugin --profile web add dsh-calendar
```

## 🚀 Quick Start

```bash
dsh plugin --profile web remove dsh-calendar
```

## 📚 Learn more

**安装**

dsh plugin --profile web add dsh-calendar 安装后重启 dsh。插件会向 profile 插入一行 id 为 `calendar` 的配置行（见本包的 cordis.patch.yml）。默认 provider 为 custom 且未填任何凭证，此时插件照常加载，但工具在调用时会抛出中文指引错误，提示你补全配置。

**中国用户：特殊代理配置（Google / iCloud）**

Google 与 iCloud 的 CalDAV 端点在中国大陆**不可直连**，需要配合你常用的梯子/特殊代理使用。插件内置 `proxyUrl` 配置：把 CalDAV 请求路由到**你本机代理客户端的端口**，不影响其他插件，也无需改任何系统设置。 config: provider: google username: you@gmail.com calendarId: you@gmail.com password: 你的应用专用密码 proxyUrl: http://127.0.0.1:7890 # 改成你代理客户端的本地端口

**Google 示例**

name: dsh-calendar config: provider: google username: you@gmail.com calendarId: you@gmail.com # password 推荐用环境变量 DSH_CALENDAR_PASSWORD Google 的 CalDAV 集合 URL 由插件拼成：`https://apidata.googleusercontent.com/caldav/v2/<calendarId>/events`。

**iCloud 示例**

name: dsh-calendar config: provider: icloud username: you@icloud.com caldavUrl: https://caldav.icloud.com/123456789/calendars/<日历ID>/ # password 推荐用环境变量 DSH_CALENDAR_PASSWORD iCloud 需要完整日历集合 URL（含你的用户 ID 与日历 ID），在 icloud.com 的日历 CalDAV 设置里可找到具体日历地址。

## 🔗 Links

- [GitHub Repository](https://github.com/STARDUSTLC666/dsh-calendar)
- [Full README](https://github.com/STARDUSTLC666/dsh-calendar#readme)
- [Back to the Plugins list](../plugins.md)
