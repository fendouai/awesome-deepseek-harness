---
title: "dsh-latex-tools"
description: "♾️ Copy and export the LaTeX in DeepSeek Harness 悬停任意 LaTeX 公式即可复制 TeX 源码或导出为独立的 SVG 文件"
keywords: "dsh-latex-tools, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-latex-tools

> ⭐ **10** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 10 | Status | ✅ active |
| Author | [liuup](https://github.com/liuup) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> ♾️ Copy and export the LaTeX in DeepSeek Harness 悬停任意 LaTeX 公式即可复制 TeX 源码或导出为独立的 SVG 文件

## About

- **复制 LaTeX**：鼠标悬停公式（行内或块级），点击「复制 LaTeX」，TeX 源码即进入剪贴板。 - **导出 SVG**：点击「导出 SVG」，公式经 MathJax 渲染为**自包含的矢量图**（字形轮廓内嵌为 path，无外部字体/样式依赖），下载为 `formula-.svg`，可用于论文、PPT、网页。 - 完全离线可用：MathJax 脚本由插件自身的 host half 提供，首次导出时才按需加载，之后浏览器缓存；不依赖任何 CDN。 - 支持行内与块级公式（块级按 display 模式导出）。

## ✨ Key Features

- **复制 LaTeX**：鼠标悬停公式（行内或块级），点击「复制 LaTeX」，TeX 源码即进入剪贴板。
- **导出 SVG**：点击「导出 SVG」，公式经 MathJax 渲染为**自包含的矢量图**（字形轮廓内嵌为 path，无外部字体/样式依赖），下载为 `formula-<slug>.svg`，可用于论文、PPT、网页。
- 完全离线可用：MathJax 脚本由插件自身的 host half 提供，首次导出时才按需加载，之后浏览器缓存；不依赖任何 CDN。
- 支持行内与块级公式（块级按 display 模式导出）。

## 📦 Install

```bash
npx @deepseek-ai/dsh web
```

## 🚀 Quick Start

```bash
npx @deepseek-ai/dsh plugin --profile web add dsh-latex-tools
```

## 📚 Learn more

**安装**

要求：安装 Node.js，然后直接用官方 npm 方式运行（无需全局安装）： npx @deepseek-ai/dsh web 插件装进 profile 后随 Web UI 启动自动加载，**无需手动启用**；Settings → Plugins 列表只显示有配置项的插件，本插件没有配置项，不会出现在那里。 一键 npm 安装 npx @deepseek-ai/dsh plugin --profile web add dsh-latex-tools 安装的是预构建产物，无需本地构建、无需任何额外配置，装完重启 Web UI 即可。

**从 GitHub 安装（无需本地构建）**

npx @deepseek-ai/dsh plugin --profile web add github:liuup/dsh-latex-tools git 安装拉取的是源码，pnpm 会自动执行包内的 `prepare` 脚本完成构建。pnpm ≥10 默认拒绝运行 git 依赖的 `prepare`，**首次 `add` 会失败**——`dsh` 会打印指引：按提示把对应条目加入 profile 的 `pnpm-workspace.yaml`（`allowBuilds` 段），然后重跑上面的命令。生产使用建议 pin 提交：`github:liuup/dsh-latex-tools#<commit-sha>`。

**本地源码安装（开发/自用）**

git clone https://github.com/liuup/dsh-latex-tools.git cd dsh-latex-tools pnpm install && pnpm build # 构建出 lib/（产物已被 gitignore，必须本地构建） npx @deepseek-ai/dsh plugin --profile web add link:/absolute/path/to/dsh-latex-tools npx @deepseek-ai/dsh web # 启动 Web UI </details>

## 🔗 Links

- [GitHub Repository](https://github.com/liuup/dsh-latex-tools)
- [Full README](https://github.com/liuup/dsh-latex-tools#readme)
- [Back to the Plugins list](../plugins.md)
