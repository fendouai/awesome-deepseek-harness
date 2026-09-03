---
title: "dsh-whale-galgame"
description: "工作推gal两不误~面向DeepSeek Harness的跨会话事件感知Galgame引擎与界面插件，支持鲸鱼娘/GPT/Claude/Grok/Gemini/Kimi多位模型娘角色"
keywords: "dsh-whale-galgame, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-whale-galgame

> ⭐ **19** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 19 | 状态 | ✅ 活跃 |
| 作者 | [JAdpp](https://github.com/JAdpp) | 更新时间 | — |
| 子分类 | 🐋 桌面宠物 | 能力 | coding |

## 一句话介绍

> 工作推gal两不误~面向DeepSeek Harness的跨会话事件感知Galgame引擎与界面插件，支持鲸鱼娘/GPT/Claude/Grok/Gemini/Kimi多位模型娘角色

## 详细介绍

**简体中文** · [English](README.en.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

## ✨ 核心特性

- 显示角色与回复模型分开选择：角色可以跟随工作区模型或手动固定；回复模型可以使用默认的 `deepseek-v4-flash`、跟随工作区，或从 DSH 模型目录中选择。
- 六个角色的好感度、等级、角色设定、聊天记录、回复选项、已消费任务记忆、自定义立绘、CG 图鉴和背景彼此分离，但都在工作区之间全局共享；当前角色、token 结算余额和插件偏好也会连续保留。
- 小剧场支线剧情，不仅支持 1v1 互动，还能触发角色间的主题日常短剧、工作复盘吐槽与里程碑剧情回放。
- 每轮提供亲近、普通、疏离三种倾向的回复，显示顺序随机；也可以直接输入内容。
- 切换角色时会同步切换对应的内置背景；鲸鱼娘默认仍使用深海宫殿，新的海边书房可在“背景图”中选作替代。用户上传背景或保存的 CG 会覆盖角色默认背景，直到恢复内置选项。
- 背景、角色立绘、对话历史、CG 图鉴和桌宠均可从界面管理。点击桌宠会打开 `galgame` 标签页。

## 📚 更多信息

**安装**

需要已安装 DeepSeek Harness，并能运行 `dsh` 的 Web profile。 ~~~sh dsh plugin --profile web add dsh-whale-galgame ~~~ 安装完成后，先停止正在运行的 Web profile，再重新启动： ~~~sh dsh --profile web ~~~ 如果源码安装提供的是 `pnpm dsh`，保留相同参数即可。

**从 GitHub 安装（跟随 main 分支）**

只有想跟最新提交、而不是 npm 发布版时才需要这条路径： ~~~sh dsh plugin --profile web add github:JAdpp/dsh-whale-galgame#main ~~~ git 安装会当场执行本仓库的 `prepare` 构建脚本，pnpm 默认拦截。首次运行会报 `ERR_PNPM_GIT_DEP_PREPARE_NOT_ALLOWED` 并打印一个键，把它写进 profile 的 `pnpm-workspace.yaml`： ~~~yaml allowBuilds: 'dsh-whale-galgame@https://codeload.github.com/JAdpp/dsh-whale-galgame/tar.gz/<commit>': true ~~~ 该键钉死了具体 commit，每次跟进新提交都要按 pnpm 新打印的值更新。**从 n

**使用与设置**

在 Galgame 顶栏可以切换“角色来源”和“实际对话”，也可以上传背景或当前角色的立绘。背景和立绘支持 PNG、JPEG、WebP、AVIF，浏览器端单个文件上限为 12 MB。 在“设置 → 插件 → 鲸鱼娘”中可以启停插件、单独显示或隐藏桌宠、设置默认角色和默认回复模型。关闭“显示桌宠”后，仍可从会话顶部的 `galgame` 页签进入并重新开启；关闭“启用插件”会暂停 Galgame 对话和好感度结算，但不会删除已有数据。

## 🔗 链接

- [GitHub 仓库](https://github.com/JAdpp/dsh-whale-galgame)
- [完整 README](https://github.com/JAdpp/dsh-whale-galgame#readme)
- [返回dsh-whale-galgame所在分类](../plugins.md)
