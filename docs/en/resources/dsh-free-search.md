---
title: "dsh-free-search"
description: "Free web search provider for DeepSeek Harness - DuckDuckGo backend, no API key needed"
keywords: "dsh-free-search, search, plugin, coding, deepseek harness, dsh"
---
# dsh-free-search

> ⭐ **38** · ✅ active · plugin · ⬆️ +8 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 38 | Status | ✅ active |
| Author | [DDDMUC](https://github.com/DDDMUC) | Updated | 2026-08-20 |
| Subcategory | 🌐 Web search | Capabilities | coding, search |

## One-liner

> Free web search provider for DeepSeek Harness - DuckDuckGo backend, no API key needed

## About

**DeepSeek Harness 免费搜索插件 —— 无需 API key，零成本，多引擎可切换。** 一个给 DeepSeek Harness (dsh) 添加多引擎搜索 provider 的插件，注册进 `ctx.web` seam。内置 `web_search` 工具自动选用，支持网页设置页切换引擎、配置 API key、一键测试所有引擎、弹出式命令切换引擎。 [中文](#中文) · [English](#english) ---

## ✨ Key Features

- **零成本** —— 多个免费引擎，无需 key、无需注册
- **多引擎可选**：DuckDuckGo（html/lite）、Bing、SearXNG（元搜索，支持自定义实例）、AnySearch、Exa、Tavily、Keenable、Perplexity、DeepSeek 官方
- **网页设置页** —— 引擎切换 + API key 配置（UI 中 key 脱敏显示"已配置"）+ 中英文切换
- **弹出式切换命令** —— 聊天框输入 `/free-search-engine`，弹出引擎选择窗口，点选即切换（等效设置页 + 保存）
- **引擎测试** —— `free_search_test` 工具让 agent 一键测试所有引擎；设置页也有"测试引擎"按钮（直测当前引擎，不走回退链，付费引擎无 key 会明确报错）
- **统一引擎回退** —— 任何引擎失败（付费/免费，缺 key/401/限流/网络）自动轮流尝试下一个引擎：首选引擎 → 其他引擎（exa/tavily/keenable 无 key 也会尝试，因为它们自带 keyless 免费额度）→ 剩余免费引擎，搜索永不直接失败；结果顶部注明实际生效的引擎（如 `Note: p
- **时间过滤** —— `advanced_search` 工具支持 `timeRange`：固定档、自定义相对值、绝对日期三种形式（详见下方逻辑说明）
- **系统提示词注入** —— agent 知道当前用哪个引擎、哪些需要 key

## 📦 Install

```bash
git clone https://github.com/DDDMUC/dsh-free-search.git
dsh plugin --profile web add /path/to/dsh-free-search
```

## 🚀 Quick Start

```bash
dsh web
```

## 📚 Learn more

**安装**

git clone https://github.com/DDDMUC/dsh-free-search.git dsh plugin --profile web add /path/to/dsh-free-search 然后重启： dsh web

**依赖说明**

插件对 `@deepseek-ai/dsh-settings` 和 `@deepseek-ai/dsh-tools` 使用 `peerDependencies`，这是刻意的：DSH 运行时必须使用安装树中的唯一实例。请通过 `dsh plugin --profile <profile> add ...` 安装插件，不要把 DSH 核心包复制进 profile 的本地 `node_modules`；重复副本会导致工具调度器失效。

**配置文件**

配置存在 `~/.dsh/settings.yaml`： free-search: provider: bing # ddg / ddg-lite / bing / searxng / anysearch / exa / tavily / keenable / perplexity / deepseek-official lang: zh # 设置页界面语言（zh / en） bingMarket: zh-CN # Bing 市场 region: cn-zh # DuckDuckGo 区域（可选） searxngInstances: # 自定义 SearXNG 实例（可选） - https://your-instance.example exaApiKey: ... # 或通过设置页填写 tavilyApiKey: ... # 或通过设置页填写 keenableApiKey: ... # 

**代理说明（国内用户）**

DuckDuckGo 等引擎可能需要代理才能访问，而 Node.js 的 `fetch` 默认不走系统代理。需要给 dsh 进程设置（Node 24+）： export NODE_USE_ENV_PROXY=1 export HTTPS_PROXY=http://127.0.0.1:7897 # 你的代理地址 export HTTP_PROXY=http://127.0.0.1:7897 Windows 用户：桌面快捷方式已内置此配置（`set NODE_USE_ENV_PROXY=1&& set HTTPS_PROXY=...`）。

## 🔗 Links

- [GitHub Repository](https://github.com/DDDMUC/dsh-free-search)
- [Full README](https://github.com/DDDMUC/dsh-free-search#readme)
- [Back to the Plugins list](../plugins.md)
