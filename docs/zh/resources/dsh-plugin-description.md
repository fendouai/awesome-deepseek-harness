---
title: "dsh-plugin-description"
description: "mount one row in the composition and every plugin card on the Web Settings plugin list page gets a bilingual (zh/en) description; it also publishes the pluginDescriptions service so other plugins can register their own descriptions."
keywords: "dsh-plugin-description, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-description

> ⭐ **2** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [MysaDC](https://github.com/MysaDC) | 更新时间 | 2026-08-14 |

## 一句话介绍

> mount one row in the composition and every plugin card on the Web Settings plugin list page gets a bilingual (zh/en) description; it also publishes the pluginDescriptions service so other plugins can register their own descriptions.

## 详细介绍

[English](README_en.md) | 中文 看到DSH插件页茫茫多的不知内容的插件感到无从下手?本插件为你补上每一个插件的自我描述，助你轻松挑选自己需要的插件。 给 **DeepSeek Harness**用的**持久化组合插件**:在组合里挂一行,Web 设置中的 **插件列表**页每张插件卡片就都带上中英文**功能说明**,并发布 `pluginDescriptions` 服务供其他插件注册自己的说明。

## ✨ 核心特性

- **持久化**:一个组合行同时进入宿主组合(Node part)与浏览器插件名册(Client part),
- **逐卡说明**:插件列表页每张卡片展示中英文功能说明,展开卡片可看完整说明、Loader
- **搜索升级**:搜索框同时匹配插件名、条目 id 与说明文字;双语随界面语言(zh/en)自动切换。
- **可扩展**:内置 134 个模块名的字典只是默认值;任何插件都能通过 `pluginDescriptions`

## 📦 安装

```bash
npx @deepseek-ai/dsh plugin --profile web add https://github.com/MysaDC/dsh-plugin-description/releases/latest/download/dsh-plugin-description.tgz
```

## 🚀 快速开始

```bash
npx @deepseek-ai/dsh plugin --profile web add https://github.com/MysaDC/dsh-plugin-description/releases/download/v1.2.1/dsh-plugin-description-1.2.1.tgz
```

## 📚 更多信息

**安装(命令行,持久化)**

要求:可正常运行的 DeepSeek Harness Web profile(需要 pnpm,`dsh plugin` 依赖它)。 本插件是**双面 npm 包**并声明 `dsh.bundle`:`dsh plugin add` 安装后,插件管理器会把 它追加进 `dsh.profile.bundles`,启动时应用包自带的 `cordis.patch.yml` 自动插入组合行 (宿主行 + 浏览器名册),不需要手改任何组合文件。

**从 GitHub Release 安装(推荐,默认最新版)**

npx @deepseek-ai/dsh plugin --profile web add https://github.com/MysaDC/dsh-plugin-description/releases/latest/download/dsh-plugin-description.tgz 上面的命令不带版本号:`releases/latest/download` 永远指向最新 Release 的固定名安装件, 以后升级重跑同一命令即可。需要固定版本时再写具体版本号(每个 Release 都附带带版本号的 tgz): npx @deepseek-ai/dsh plugin --profile web add https://github.com/MysaDC/dsh-plugin-description/releases/download/v1.2.1/dsh-plugin-descri

**升级到最新版:重跑一次安装命令即可(pnpm 会重新解析 latest 安装件)**

npx @deepseek-ai/dsh plugin --profile web add https://github.com/MysaDC/dsh-plugin-description/releases/latest/download/dsh-plugin-description.tgz

**手动安装(不想用命令行时)**

1. 下载 Release 的 `dsh-plugin-description-v<版本>.zip`,把解压出的整个包目录放到 `<DSH_HOME>/profiles/node_modules/dsh-plugin-description/`; 2. 在 profile 的 `cordis.patch.yml` 加一行(内容同本仓库根目录的 `cordis.patch.yml`); 3. 重启 DSH。

## 🔗 链接

- [GitHub 仓库](https://github.com/MysaDC/dsh-plugin-description)
- [完整 README](https://github.com/MysaDC/dsh-plugin-description#readme)
- [返回dsh-plugin-description所在分类](../plugins.md)
