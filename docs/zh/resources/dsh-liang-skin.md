---
title: "dsh-liang-skin"
description: "DeepSeek Harness 滑动变阻器皮肤"
keywords: "dsh-liang-skin, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-liang-skin

> ⭐ **148** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 148 | 状态 | ✅ 活跃 |
| 作者 | [kingOfSoySauce](https://github.com/kingOfSoySauce) | 更新时间 | — |
| 子分类 | 🎨 皮肤与主题 | 能力 | coding |

## 一句话介绍

> DeepSeek Harness 滑动变阻器皮肤

## 详细介绍

- #### 方法一， 提示词安装： &emsp;&emsp;点击展开提示词 复制以下提示词给 DSH；会先排查冲突再安装，所以较长： 请把“滑动变祖”皮肤安装到 DSH 的 web profile。必须先检查冲突，确认可以继续后再安装。 1. 安装前只读检查 web profile 的 package.json（dependencies 与 dsh.profile.bundles）、profile 的 cordis.patch.yml 和 $DSH_HOME/cordis.patch.yml（如有）。 2. 从当前启用的 bundles 中识别其他皮肤、主题或外观插件：排除 @deepseek-ai/dsh-base、@deepseek-ai/dsh-web-app、dsh-skin-market 和本次目标 dsh-client-liang-intensity-skin；读取候选 package.json 的名称、描述、dsh.client/dsh.bundle 声明，必要时再读 README。 3. 如果发现其他已启用的皮肤插件，列出它们并停在安装前，提醒我先停用；未经我确认不得修改任何 profile 文件，也不得执行安装。 4. 如果没有冲突，明确说“未检测到其他已启用的皮肤插件”，然后执行： dsh plugin --profile web add 'github:kingOfSoySauce/dsh-liang-skin' 5. 安装后读取 web profile 的 package.json，确认 dependencies 和 dsh.profile.bundles 中都有 dsh-client-liang-intensity-skin；再检查目标 package.json 的 dsh.client/dsh.bundle 声明和 liang-intensit

## ✨ 核心特性

- #### 方法一， 提示词安装：
- #### 方法二(推荐)，安装[皮肤市场](https://github.com/kingOfSoySauce/dsh-skin-market#安装皮肤市场)插件后，搜索“滑动变祖”，一键安装
- #### 方法三， 或者[命令安装](#cli-install)；运行前请关闭其他皮肤插件，避免冲突

## 📦 安装

```bash
dsh plugin --profile web add 'github:kingOfSoySauce/dsh-liang-skin'
dsh --profile web --dump-config | grep -B1 -A2 liang-intensity
```

## 🚀 快速开始

```bash
dsh plugin --profile web add ./dsh-client-liang-intensity-skin-0.1.7.tgz
```

## 📚 更多信息

**安装**

<details> <summary>&emsp;&emsp;点击展开提示词</summary> 复制以下提示词给 DSH；会先排查冲突再安装，所以较长： 请把“滑动变祖”皮肤安装到 DSH 的 web profile。必须先检查冲突，确认可以继续后再安装。 1. 安装前只读检查 web profile 的 package.json（dependencies 与 dsh.profile.bundles）、profile 的 cordis.patch.yml 和 $DSH_HOME/cordis.patch.yml（如有）。 2. 从当前启用的 bundles 中识别其他皮肤、主题或外观插件：排除 @deepseek-ai/dsh-base、@deepseek-ai/dsh-web-app、dsh-skin-market 和本次目标 dsh-client-liang-intensity-sk

**命令安装**

需要先安装 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)；当前版本已在 `0.1.0-rc.6` 上验证。安装本身可以在 DSH 运行时执行（只改动磁盘配置），重启后生效。三种方式任选其一： > 安装前请确保已关闭其他皮肤插件，避免冲突。

**方式一：从 GitHub 安装最新版（推荐）**

dsh plugin --profile web add 'github:kingOfSoySauce/dsh-liang-skin' dsh --profile web --dump-config | grep -B1 -A2 liang-intensity

**方式二：从 GitHub Release tarball 安装**

从本仓库 [Releases](https://github.com/kingOfSoySauce/dsh-liang-skin/releases) 页面下载 `dsh-client-liang-intensity-skin-0.1.7.tgz`（包内已包含构建好的 `lib/client.js`，安装时不需要执行任何 prepare 脚本），然后： dsh plugin --profile web add ./dsh-client-liang-intensity-skin-0.1.7.tgz 适合不方便走 git 的环境；相对路径按你运行命令的目录解析。

## 🔗 链接

- [GitHub 仓库](https://github.com/kingOfSoySauce/dsh-liang-skin)
- [完整 README](https://github.com/kingOfSoySauce/dsh-liang-skin#readme)
- [返回dsh-liang-skin所在分类](../plugins.md)
