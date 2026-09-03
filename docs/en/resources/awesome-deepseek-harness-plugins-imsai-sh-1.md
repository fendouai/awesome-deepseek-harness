---
title: "awesome-deepseek-harness-plugins"
description: "Curated community plugin directory and live marketplace for DeepSeek Harness."
keywords: "awesome-deepseek-harness-plugins, registry, awesome-list, coding, deepseek harness, dsh"
---
# awesome-deepseek-harness-plugins

> ⭐ **145** · ✅ active · awesome-list · ⬆️ +16 recently

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 145 | Status | ✅ active |
| Author | [imsai-sh](https://github.com/imsai-sh) | Updated | 2026-08-21 |

## One-liner

> Curated community plugin directory and live marketplace for DeepSeek Harness.

## About

面向 [DeepSeek Harness](https://github.com/deepseek-ai/DeepSeek-Harness)（`dsh`）生态的社区插件目录，共收录 **13146** 个插件（含 PR 收录与 GitHub `dsh-plugin` topic 自动发现），目录数据更新于 2026-09-03。 **但这个项目不只是一份 awesome list。** 它还包括一个在线插件市场、一个把市场装进 `dsh` 本体的插件，以及一套免费的公开查询 API——这些应用代码开源在姊妹仓库 [dsh-1024store](https://github.com/imsai-sh/dsh-1024store)；本仓库专注目录本身：经静态校验的 PR 收录流水线与自动生成的目录 README，目录数据另有自动收集服务持续喂入。全部代码 MIT 协议，fork 之后就能部署成你自己的插件市场。 [在线网站](https://deepseek1024.com/) · [API 文档](https://github.com/imsai-sh/dsh-1024store/blob/main/web/docs/api.md) · [英文目录](catalog/README.md) · [提交插件](CONTRIBUTING.md) · [网站与 CLI 源码](https://github.com/imsai-sh/dsh-1024store) DSH插件社区

## 📦 Install

```bash
dsh plugin --profile web add dsh1024@latest
```

## 🚀 Quick Start

```bash
curl 'https://api.deepseek1024.com/v1/plugins/search?q=memory'
```

## 📚 Learn more

**安装插件并计入统计**

1024 Store 只提供 npm 安装：插件详情页展示的命令安装的是作者发布到 npm、声明 `dsh.bundle` 的包；尚未发布 npm 包的插件以浏览模式收录（有仓库链接，无安装命令）。网站优先提供开源包装 CLI；它会调用官方 DeepSeek Harness 插件命令、校验 profile 的真实安装结果，并把匿名安装结果可靠地上报到排行榜： dsh1024 plugin --profile web add <npm-package> 首次使用先一次性全局安装：`npm install -g dsh1024`。它与官方命令只差一个名字——`plugin` 之后的参数原样转发给官方 CLI，不增删、不改写、不重排，包装器只负责在结束后核对 profile 并记录一条匿名安装结果。参数不会写入遥测或本地 receipt。 monorepo 子目录插件的标识形如 `owner/r

**使用 Agent Skill 提交（推荐）**

如果你使用 Codex、Claude Code、Cursor 或其他兼容 Agent Skills 的编程助手，可以安装本仓库提供的提交 Skill： npx skills add imsai-sh/awesome-deepseek-harness-plugins --skill submit-dsh-plugin -g 安装后告诉助手： 使用 $submit-dsh-plugin 检查并提交我的 DeepSeek Harness 插件。 该 Skill 会检查插件仓库、生成唯一允许提交的目录 JSON、验证变更范围，并在获得授权后创建 PR。新增条目的非草稿 PR 通过静态审查后会自动合并；修改或删除既有条目的 PR 同样会跑静态审查，但不会自动合并，需要维护者人工审核后手动合并。合并后 CI 自动同步目录到网站数据库并刷新本 README，贡献者和维护者都不需要手工更新任何生成文件。查

## 🔗 Links

- [GitHub Repository](https://github.com/imsai-sh/awesome-deepseek-harness-plugins)
- [Full README](https://github.com/imsai-sh/awesome-deepseek-harness-plugins#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
