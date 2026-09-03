---
title: "dsh-diff-viewer"
description: "PiUI 风格 Web diff 查看器，替代默认 diff 视图。"
keywords: "dsh-diff-viewer, ui, plugin, git, deepseek harness, dsh"
---
# dsh-diff-viewer

> ⭐ **24** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 24 | 状态 | ✅ 活跃 |
| 作者 | [lehhair](https://github.com/lehhair) | 更新时间 | 2026-08-19 |

## 一句话介绍

> PiUI 风格 Web diff 查看器，替代默认 diff 视图。

## 详细介绍

DSH Web GUI 的 PiUI 风格 diff 查看器插件：替换 write/edit 工具调用的 diff 渲染（原 DiffBlock）。 - **unified 单栏默认**：同一 gutter 并排显示旧/新行号，无左右错位；split 双栏可选（`viewMode`） - **变更条**：新增实心绿条、删除条纹红条；行背景色带统一延伸到最宽行 - **词级高亮**：行内改动叠加绿/红标记，shiki 语法着色（`highlightLines`） - **上下文折叠**：长段未变更行折叠为"`N 行未变更`"，向上/向下/全部展开 - **窗口化渲染**：固定行高窗口化，大 diff 不挂载全部行；sticky 横向滚动条（hover 显现） - **复制 + `└ +A -R · N file(s)` 页脚** - **edit 结果默认展开**：settled 的 edit 结果卡展开即见替换 diff（write 保持默认收起） - **PTC/Code 嵌套支持**：Code Dispatch 内的 write/edit 子卡片同样接管——嵌套子调用没有 wire diff view，插件按工具自身的 `presentCall` 语义从参数推导调用时 diff（edit 的 old_string→new_string、write 的整文件新增），错误子调用保持通用错误路径

## ✨ 核心特性

- **unified 单栏默认**：同一 gutter 并排显示旧/新行号，无左右错位；split 双栏可选（`viewMode`）
- **变更条**：新增实心绿条、删除条纹红条；行背景色带统一延伸到最宽行
- **词级高亮**：行内改动叠加绿/红标记，shiki 语法着色（`highlightLines`）
- **上下文折叠**：长段未变更行折叠为"`N 行未变更`"，向上/向下/全部展开
- **窗口化渲染**：固定行高窗口化，大 diff 不挂载全部行；sticky 横向滚动条（hover 显现）
- **复制 + `└ +A -R · N file(s)` 页脚**

## 📦 安装

```bash
dsh plugin --profile web add "github:lehhair/dsh-diff-viewer"
```

## 🚀 快速开始

```bash
# 直接用 latest 资产 URL（永远是最新版）：
dsh plugin --profile web add "https://github.com/lehhair/dsh-diff-viewer/releases/latest/download/dsh-external-dsh-diff-viewer.tgz"

# 重启 dsh web 生效
dsh web
```

## 📚 更多信息

**直接安装本地目录，或 npm pack 后装 tarball：**

dsh plugin --profile web add E:\dev\dsh-diff-viewer > Windows 注意：`dsh plugin add <本地目录>` 的 `link:` 绝对路径有 junction bug（pnpm 拼错目标）。用 **tarball**（`npm pack` 后 `dsh plugin add *.tgz`）可绕过。 > 发版注意：`lib/` 已提交，源码改动必须同时重建并提交 `lib/`（CI 的 `check` 后会校验 `lib/` 与源码一致，不一致即失败）。

## 🔗 链接

- [GitHub 仓库](https://github.com/lehhair/dsh-diff-viewer)
- [完整 README](https://github.com/lehhair/dsh-diff-viewer#readme)
- [返回dsh-diff-viewer所在分类](../plugins.md)
