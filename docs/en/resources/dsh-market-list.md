---
title: "dsh-market"
description: "DeepSeek Harness 插件市场 · 持续收录 500+ DSH 插件：中文搜索 + 实用五维评分 + 一键安装。Web 版与 DSH 侧边栏插件双形态。Plugin marketplace for DeepSeek Harness: 500+ plugins, Chinese search, 5-dim scoring, one-click install."
keywords: "dsh-market, registry, awesome-list, coding, search, deepseek harness, dsh"
---
# dsh-market

> ⭐ **46** · ✅ active · awesome-list · ⬆️ +7 recently

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 46 | Status | ✅ active |
| Author | [2BingLing](https://github.com/2BingLing) | Updated | 2026-08-21 |

## One-liner

> DeepSeek Harness 插件市场 · 持续收录 500+ DSH 插件：中文搜索 + 实用五维评分 + 一键安装。Web 版与 DSH 侧边栏插件双形态。Plugin marketplace for DeepSeek Harness: 500+ plugins, Chinese search, 5-dim scoring, one-click install.

## About

DSH 生态增长极快，插件与技能散落在 GitHub 各处 —— **不知道哪个好用、怎么装、怎么组合成一套能干活的环境**。DSH Market 用一个平台收齐它们，并提供两种消费入口：

## ✨ Key Features

- **持续收录** — 每天自动扫描 `dsh-plugin` / `dsh` 等 GitHub topic、社区精选列表，全量收录（当前 5785 个插件 + 整合包通道）
- **实用五维评分** — 维护活跃 / 实用度 / 生态热度 / 便捷度 / 信号质量，加权几何平均融合，每个插件附「为什么推荐」解释
- **中文体验** — 所有插件自动生成中文简介与中文功能标签，中文搜索、中文筛选
- **一键安装** — 插件版确定性脚本路由：skill 型 `git clone`，cordis 型 `dsh plugin add`；失败可重试、可回滚
- **AI 安装（路由模式）** — 零 LLM 直装优先（配方缓存 / 解析命令 + 冒烟验证，75%+ 插件无需 AI），需要时交给极简协议子代理（JSON verdict 自动沉淀为配方）；安装度量本机记录（T0 命中率 / AI 参与率 / 成功率）
- **🛡 安全模式** — 确认安装时可开启：AI 安装前强制供应链扫描（危险命令 `curl|sh` / 混淆执行 / 敏感信息收集回传 / 配置篡改 / 来源存疑），发现风险即中止不安装；针对 DSH 插件供应链漏洞风险（如 QVD-2026-57410 CVSS 9.8），来源不明插件建议开启（消耗 token）
- **推荐体系** — 冷启动问卷 / 新手友好 / 猜你喜欢（个性化画像）/ 场景推荐（读会话上下文，详见 [DSH 插件版](#dsh-插件版)）
- **整合包生态** — Web「整合包」分区 + 插件端整合包 Tab（浏览 / 条目解析率校验 / 装包入口）；配套 `dsh.pack.json` 整合包协议（详见 [dsh-bundler](https://github.com/2BingLing/dsh-bundler)）

## 📦 Install

```bash
npx @deepseek-ai/dsh plugin --profile web add @dsh-market/plugin
```

## 🚀 Quick Start

```bash
├─ collector/   # 数据管道（Node + tsx）：扫描 → 检测 → 评分 → 中文化
├─ web/         # Web 站（Vite + React + TS + Fuse.js）
├─ plugin/
│  ├─ core/     # 插件核心层（纯 Node，零 DSH 依赖，可独立测试）
│  └─ ui/       # 插件 UI 层（cordis Host RPC + 浏览器 Client 面板）
├─ schema/      # 共享类型（DshPlugin / MarketData / PracticalScore）
└─ scripts/     # 工具脚本（截图 / 数据注入 / 视觉评审）
```

## 📚 Learn more

**安装插件版**

npx @deepseek-ai/dsh plugin --profile web add @dsh-market/plugin 装完**重启 harness**，侧边栏底部出现「插件市场」入口。 > **v0.4.0 起**：AI 代理安装升级为**路由模式**——先走零 LLM 直装（已装检测 → 配方缓存 → README 解析命令 + 冒烟验证），只有需要时才交给极简协议子代理；一键安装成功后自动学习配方，后续重装/换机器零 token 直装。 > **v0.4.5 起**：确认安装时可勾选 **🛡 安全模式**——对于来源不明或敏感的插件，开启后**跳过零 LLM 直装**，强制 AI 子代理在安装前做供应链扫描：检查危险命令（`curl|sh` 管道执行 / 下载执行 / base64 混淆）、敏感信息收集回传（读取 API Key / Token 并外发）、配置篡改（覆盖 s

**克隆与安装**

git clone https://github.com/2BingLing/dsh-market.git cd dsh-market npm install cp .env.example .env # 填入 GITHUB_TOKEN（必需）、DEEPSEEK_API_KEY（可选）

## 🔗 Links

- [GitHub Repository](https://github.com/2BingLing/dsh-market)
- [Full README](https://github.com/2BingLing/dsh-market#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
