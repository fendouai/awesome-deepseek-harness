---
title: "openbiliclaw"
description: "本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin）"
keywords: "openbiliclaw, research, agent, coding, multi-agent, deepseek harness, dsh"
---
# openbiliclaw

> ⭐ **2,971** · ✅ 活跃 · 智能体 · 近期 ⬆️ +20

| | | | |
|---|---|---|---|
| 类型 | 智能体 | 分类 | 研究 |
| 星数 | ⭐ 2,971 | 状态 | ✅ 活跃 |
| 作者 | [whiteguo233](https://github.com/whiteguo233) | 更新时间 | 2026-08-21 |

## 一句话介绍

> 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin）

## 详细介绍

**通用个性化内容推荐 Agent——本地运行、跨平台理解你、只为你一个人构建** *A general-purpose personalized content discovery Agent — runs on your machine, understands only you* [项目主页](https://whiteguo233.github.io/OpenBiliClaw/) | [English](README_EN.md) | 中文

## ✨ 核心特性

- 🧠 **五层灵魂画像** — 事件→偏好→觉察→洞察→灵魂，推断 MBTI、认知风格和深层需求（[详解](docs/modules/soul.md)）
- 🔮 **兴趣探针** — 基于心理学桥接主动猜测你可能喜欢的未知领域，猜对升级为正式兴趣，猜错安静退出
- 🧭 **避雷探针** — 主动确认你想避开的内容形态和风格边界，确认后才写入过滤偏好
- 🌐 **跨平台内容源** — B 站 / 小红书 / 抖音 / YouTube / X / 知乎 / Reddit / Linux.do / Bangumi / V2EX / 微博 / GitHub / 通用 Web，兴趣不再被单一平台割裂（[详解](docs/modules/discovery.md)）
- 🎯 **智能多样性** — 主题配额 + 跨平台混排 + 小源保护，告别「一刷都是 AI」
- ⚡ **「换一批」瞬间响应且默认去重** — reshuffle ~0.6s；当前卡、推荐历史和持久化已看账本三层排除，连续刷不卡顿也不靠“忽略当前”开关
- 💬 **有温度的推荐理由** — 像朋友一样解释为什么你会喜欢，而不是「因为你看过类似视频」
- 🔄 **持续学习** — 苏格拉底式对话 + 行为分析 + 反馈即时生效，越用越懂你

## 📦 安装

```bash
unzip openbiliclaw-extension-v*-firefox.zip -d openbiliclaw-firefox

# 或从源码构建
git clone https://github.com/whiteguo233/OpenBiliClaw.git
cd OpenBiliClaw/extension
npm install
npm run build:firefox          # 产出 dist-firefox/
npm run package:firefox        # 额外打成未签名 openbiliclaw-extension-v*-firefox.zip
# AMO 凭据配置后可签名成正式安装包：
# AMO_JWT_ISSUER=... AMO_JWT_SECRET=... npm run sign:firefox:only
```

## 🚀 快速开始

```bash
>   APP="/Applications/OpenBiliClaw.app"
>   xattr -dr com.apple.quarantine "$APP"
>
```

## 📚 更多信息

**📸 功能预览**

核心入口现在有五个：浏览器插件负责平台内交互和登录会话，桌面端 Web（`/web`）提供大屏推荐首页，移动端 Web（`/m`）适合手机使用，另有独立仓库的原生 Flutter 客户端（[OpenBiliClaw-mobile](https://github.com/whiteguo233/OpenBiliClaw-mobile)）覆盖 Android / iOS / Web / 桌面，以及把同一套面板搬进 DSH Web 界面的 [DSH 客户端插件](https://github.com/whiteguo233/dsh-openbiliclaw)（第四栏 + 22 个 Agent Bridge 工具）。桌面端、移动端 Web、原生客户端和 DSH 插件都只调用本地 API，Cookie 同步和平台任务仍由插件承担。 <table> <tr> <td align="center" wi

**🖥️ 桌面端 Web 预览**

启动后端后访问 `http://127.0.0.1:8420/web`（或直接 `http://127.0.0.1:8420/`，会自动跳转），即可在浏览器大屏上使用推荐首页。 <table> <tr> <td align="center" width="50%"> <br/> <b>桌面推荐首页</b><br/> <sub>惊喜推荐 Hero · 为你推荐网格 · 朋友式推荐理由</sub> </td> <td align="center" width="50%"> <br/> <b>推荐卡片网格</b><br/> <sub>封面 + 推荐理由 · 喜欢 / 不感兴趣 / 稍后 / 收藏 / 聊一聊</sub> </td> </tr> <tr> <td align="center" colspan="2"> <br/> <b>画像 + 实时看板</b><br/> <sub>侧栏 Runt

**📱 移动端 Web 预览**

<table> <tr> <td align="center" width="33%"> <br/> <b>手机推荐页</b><br/> <sub>惊喜推荐 + 池子状态 · 朋友式推荐原因</sub><br/> <sub>看看 / 喜欢 / 稍后 / 收藏 / 不感兴趣 / 聊一聊</sub> </td> <td align="center" width="33%"> <br/> <b>手机画像页</b><br/> <sub>人格素描 · 核心特质 · 深层需求 · MBTI</sub> </td> <td align="center" width="33%"> <br/> <b>手机对话页</b><br/> <sub>与插件共享主聊天历史</sub> </td> </tr> </table> > 📱 想要原生 App？独立仓库 [OpenBiliClaw-mobile](https:/

**安装与部署详情**

普通用户的正常流程是：先安装浏览器插件，再把一句话发给 AI 助手安装后端，在同一个浏览器登录内容平台；如果要在手机上使用，再打开移动端 Web。脚本、Docker 和手动部署只作为备用路径，放在下面折叠区。

## 🔗 链接

- [GitHub 仓库](https://github.com/whiteguo233/OpenBiliClaw)
- [完整 README](https://github.com/whiteguo233/OpenBiliClaw#readme)
- [返回openbiliclaw所在分类](../agents.md)
