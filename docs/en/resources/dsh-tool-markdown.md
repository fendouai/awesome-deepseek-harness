---
title: "dsh-tool-markdown"
description: "DSH Markdown 工具插件：HTML↔Markdown 转换、GFM 表格规范化、目录生成，零依赖轻量解析器，注册 markdown 工具"
keywords: "dsh-tool-markdown, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-tool-markdown

> ⭐ **4** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | — |
| Subcategory | 🧰 Toolkits | Capabilities | coding |

## One-liner

> DSH Markdown 工具插件：HTML↔Markdown 转换、GFM 表格规范化、目录生成，零依赖轻量解析器，注册 markdown 工具

## About

[English](README.en.md) DSH Markdown 工具插件 —— HTML↔Markdown 转换、GFM 表格规范化、目录生成。零依赖、纯函数、手写轻量解析器。

## ✨ Key Features

- **零依赖**：手写递归下降 HTML 解析器（不引入 cheerio/jsdom——净增数十 MB 且是攻击面）
- **零执行面**：不 eval、不 new Function、不加载远程资源、不解析 CSS 布局
- **内容剥离**：script/style/iframe/object/noscript 内容整体剥离（安全 + 噪音）
- **md2html 白名单**：只输出 `p h1-h6 ul ol li blockquote pre code a img strong em br hr table thead tbody tr th td`；文本一律 HTML 转义——markdown 内嵌 `<script>` 只会显示为文本
- **链接 scheme 白名单**：`http/https/mailto`；`javascript:`/`data:` 链接降级为纯文本
- **资源上限**：嵌套深度 64 层报错（防栈溢出）；输入 `maxBytes` 默认 256KB、硬顶 1MB（超限报错不截断）

## 📦 Install

```bash
# 交互式（web）profile
dsh plugin --profile web add github:omdsh-dev/dsh-tool-markdown
# 一次性任务（headless）profile —— dsh run 默认使用 headless
dsh plugin --profile headless add github:omdsh-dev/dsh-tool-markdown
```

## 🚀 Quick Start

```bash
npm pack    # 生成 dsh-tool-markdown-*.tgz
dsh plugin --profile web add ./dsh-tool-markdown-*.tgz
dsh plugin --profile headless add ./dsh-tool-markdown-*.tgz
```

## 📚 Learn more

**示例**

markdown { action: "html2md", html: "<h1>标题</h1><p>你好 <b>世界</b></p>" } → # 标题\n\n你好 **世界** markdown { action: "md2html", markdown: "[x](javascript:alert(1))" } → <p>x</p> ← javascript: 链接降级为纯文本 markdown { action: "table", text: "a|b\n1|2" } → | a | b |\n| --- | --- |\n| 1 | 2 | markdown { action: "toc", markdown: "# 标题一\n## 小节" } → - [标题一](#标题一)\n - [小节](#小节)

**一次性任务（headless）profile —— dsh run 默认使用 headless**

dsh plugin --profile headless add github:omdsh-dev/dsh-tool-markdown 包内 `dsh.bundle.patch` 会在安装后自动把插件加入 profile 的 layer stack（row id：`tool-markdown`）。 > ⚠️ web 与 headless 是**不同 profile**：web 安装不会自动覆盖 headless；`dsh run` 默认使用 headless profile。

**npm pack tarball 安装**

npm pack # 生成 dsh-tool-markdown-*.tgz dsh plugin --profile web add ./dsh-tool-markdown-*.tgz dsh plugin --profile headless add ./dsh-tool-markdown-*.tgz

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-tool-markdown)
- [Full README](https://github.com/omdsh-dev/dsh-tool-markdown#readme)
- [Back to the Plugins list](../plugins.md)
