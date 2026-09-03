---
title: "dsh-web-ui"
description: "DSH Web 大型插件与皮肤集合：任务看板、Git 图、侧栏、远程/移动 UI、宠物、Token 统计与主题。"
keywords: "dsh-web-ui, ui, plugin, git, observability, deepseek harness, dsh"
---
# dsh-web-ui

> ⭐ **6,622** · ✅ 活跃 · 插件 · 近期 ⬆️ +245

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 6,622 | 状态 | ✅ 活跃 |
| 作者 | [zhu1090093659](https://github.com/zhu1090093659) | 更新时间 | 2026-08-21 |
| 子分类 | 🎨 皮肤与主题 | 能力 | ui, git, observability |

## 一句话介绍

> DSH Web 大型插件与皮肤集合：任务看板、Git 图、侧栏、远程/移动 UI、宠物、Token 统计与主题。

## 详细介绍

                DeepSeek Harness（DSH）Web 的插件聚合生态包 · 一切皆插件 性能引擎 · 创意工坊 · 任务看板 · 移动端远程 · SSH 运维 · 图像理解 [是什么](#是什么) · [创意工坊](#创意工坊dsh-marketcom) · [功能插件](#功能插件) · [皮肤](#皮肤) · [快速上手](#快速上手) · [常见问题](#常见问题) · [已知限制](#已知限制) · [社区](#社区)

## 📦 安装

```bash
dsh plugin --profile web add github:zhu1090093659/dsh-web
# 等价写法：dsh plugin --profile web add git+https://github.com/zhu1090093659/dsh-web.git
```

## 🚀 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/zhu1090093659/dsh-web.git
cd dsh-web

# 2. 安装依赖并构建
pnpm install
pnpm -r build

# 3. 把全家桶链接进 web profile（推荐，先链接全部子包再注册聚合包）
node scripts/link-profile.mjs
dsh plugin --profile web add link:$(pwd)/packages/dsh-web-all

# 4. 重启 dsh web，侧边栏即可看到全部插件入口
dsh web
```

## 📚 更多信息

**三步上手（npm 安装，推荐）**

1. 安装聚合包：`dsh plugin --profile web add @linxin666/dsh-web-all@latest` 2. 重启 `dsh web`，侧边栏出现全部插件入口 3. 打开「设置 > 插件配置」按需开关插件，或在皮肤面板试穿皮肤 1. 安装聚合包：`dsh plugin --profile desktop add @linxin666/dsh-web-all@latest` 2. 验证挂载：`dsh --profile desktop --dump-config` 3. 完全退出并重新启动 DSH Desktop 客户端应用，界面即可显示全部插件与皮肤入口 > 只要皮肤就装 `@linxin666/dsh-client-ui-skin-center`。若装到了旧版本（pnpm 11 的发布年龄门禁），见下方「安装排障」。

**从 GitHub 仓库直接安装**

仓库根 `package.json` 声明 `dsh.bundle`（复用聚合包的装配清单）并依赖 npm 已发布的聚合包，整个仓库因此可以直接当成一个插件安装，无需克隆与构建，插件中心 / hub 按仓库一键安装时走的就是这条路： dsh plugin --profile web add github:zhu1090093659/dsh-web

**单独安装某个插件**

不想装全家桶时，可单独安装任意插件（npm 已发布，直接用包名）： dsh plugin --profile web add @linxin666/dsh-client-ui-task-board@latest # 任务看板 dsh plugin --profile web add @linxin666/dsh-ssh@latest # 远程连接（SSH） dsh plugin --profile web add @linxin666/dsh-tool-describe-image@latest # 图像理解工具 dsh plugin --profile web add @linxin666/dsh-pet@latest # 鲸鱼娘宠物 dsh plugin --profile web add @linxin666/dsh-liangshen@latest # 梁神模式（两阶段锚定 pre

**安装排障**

<details> <summary><strong>展开查看 pnpm 常见问题</strong></summary> <br> > pnpm 的严格（isolated）布局只把聚合包放在 profile 顶层，patch 行引用的子包会被收进嵌套目录，`dsh web` 会报 `Cannot find package '@linxin666/dsh-...'`。本包的子包已声明为 dependencies；使用严格布局时，在 profile 的 `pnpm-workspace.yaml` 加 `nodeLinker: hoisted`（或旧式 `public-hoist-pattern: ['@linxin666/*']`），再重新安装即可。 > 首次安装若提示 `ERR_PNPM_IGNORED_BUILDS`（pnpm 拒绝依赖的构建脚本），按提示把 `cloudflared` /

## 🔗 链接

- [GitHub 仓库](https://github.com/zhu1090093659/dsh-web)
- [完整 README](https://github.com/zhu1090093659/dsh-web#readme)
- [返回dsh-web-ui所在分类](../plugins.md)
