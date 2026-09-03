---
title: "dsh-wallpaper-engine"
description: "把本机 Wallpaper Engine 的壁纸变成 DSH 网页界面的背景：Video 动态播放、Web 以 iframe 加载、Scene 壁纸提取主纹理作为静态帧；iOS 液态玻璃设置窗口（配色 / 玻璃颜色 / 透明度）、内容分级与类型过滤、自定义壁纸上传、紧凑 CD 架布局、黑胶唱片展示、隐藏 / 恢复、倍速 / 翻转与自动轮播。感谢 Jerry 维护 macOS 版。"
keywords: "dsh-wallpaper-engine, search, plugin, coding, deepseek harness, dsh"
---
# dsh-wallpaper-engine

> ⭐ **204** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 204 | 状态 | ✅ 活跃 |
| 作者 | [elysia395](https://github.com/elysia395) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding |

## 一句话介绍

> 把本机 Wallpaper Engine 的壁纸变成 DSH 网页界面的背景：Video 动态播放、Web 以 iframe 加载、Scene 壁纸提取主纹理作为静态帧；iOS 液态玻璃设置窗口（配色 / 玻璃颜色 / 透明度）、内容分级与类型过滤、自定义壁纸上传、紧凑 CD 架布局、黑胶唱片展示、隐藏 / 恢复、倍速 / 翻转与自动轮播。感谢 Jerry 维护 macOS 版。

## 详细介绍

[English](README.en.md) | [中文](README.md) 一个 DSH bundle，把你电脑上的 **Wallpaper Engine** 壁纸变成 **DSH 网页界面（`dsh web`）的背景**。 它会自动发现你本机的 Wallpaper Engine 安装，列出你的壁纸，并把*可移植*的类型渲染到 DSH 对话界面的后方，配以 **iOS 风格液态玻璃**效果：Video（`.mp4`）动态播放、Web/HTML 以 iframe 加载，**Scene（场景）由内置渲染器输出完整场景帧（对象树/纹理/粒子/shader 效果）**。v0.2 起还支持： - **壁纸选择弹窗**：缩略图网格收纳进独立弹窗，设置页不再被长列表占满； - **隐藏 / 恢复**：不想看的壁纸一键隐藏（软删除），随时恢复，不碰源文件； - **视频倍速**：0.5x – 2x 六档原生调速，即时生效、不重载； - **水平翻转**：镜像画面（视频 / 网页 / 上传图片均适用）； - **自定义壁纸**：直接上传本地 JPG / PNG / MP4 当壁纸，可选存储位置与画面适配模式； - **场景壁纸完整场景帧**（v0.6）：Scene 壁纸由纯 JS 场景渲染器完整重放（对象树/纹理/粒子/shader 效果），不再是主纹理静态帧。 - **液态玻璃设置页**（v0.3.1）：设置页升级为**一级设置页**（参照 dsh-web-ui-all 皮肤中心的设计），整页是可自定义的液态玻璃卡片 —— **配色**（6 种预设 + 自定义取色）与**玻璃透明度**（0–60%）即时生效、持久保存。 - **整个设置窗口液态玻璃化**（v0.3.2）：一键把 **DSH 原生设置窗口整体**（对话框 + 左侧导航 + General / 模型 / 插件等**全部

## ✨ 核心特性

- **壁纸选择弹窗**：缩略图网格收纳进独立弹窗，设置页不再被长列表占满；
- **隐藏 / 恢复**：不想看的壁纸一键隐藏（软删除），随时恢复，不碰源文件；
- **视频倍速**：0.5x – 2x 六档原生调速，即时生效、不重载；
- **水平翻转**：镜像画面（视频 / 网页 / 上传图片均适用）；
- **自定义壁纸**：直接上传本地 JPG / PNG / MP4 当壁纸，可选存储位置与画面适配模式；
- **场景壁纸完整场景帧**（v0.6）：Scene 壁纸由纯 JS 场景渲染器完整重放（对象树/纹理/粒子/shader 效果），不再是主纹理静态帧。

## 📦 安装

```bash
dsh plugin --profile web add dsh-plugin-wallpaper-engine
```

## 🚀 快速开始

```bash
> dsh plugin --profile web add dsh-plugin-wallpaper-engine-mac
>
```

## 📚 更多信息

**工作原理**

1. 通过读取 Steam 的 `libraryfolders.vdf` 定位 Wallpaper Engine 安装位置（所以 Steam 装在非默认盘也能用）； 2. 从 `projects/defaultprojects`、`projects/myprojects` 以及 `steamapps/workshop/content/431960/*` 枚举壁纸； 3. 在 DSH webserver 上注册同源 HTTP 路由，让浏览器端直接获取数据和流式加载媒体： - `GET /wallpaper-engine/inventory` → 壁纸 JSON 列表 - `GET /wallpaper-engine/media/<token>` → 视频 / HTML（支持 Range） - `GET /wallpaper-engine/preview/<token>` → 预览图 - `G

**普通用户（安装已发布版本，推荐）**

如果你只是想用这个插件，直接装 npm 上已发布的包即可： dsh plugin --profile web add dsh-plugin-wallpaper-engine 装完重启 `dsh web`，打开 **设置 → Wallpaper Engine** 就能用。 > **macOS 用户**：macOS 没有 Wallpaper Engine 客户端，本插件的 macOS 版（WaifuX + 散装媒体支持）由社区维护者 Jerry 维护，发布为独立 npm 包： > > ```sh > dsh plugin --profile web add dsh-plugin-wallpaper-engine-mac > ``` > > 仓库：https://github.com/ruijiaang-lab/dsh-wallpaper-engine

**安装失败排查**

`dsh plugin --profile web add ...` 会把命令转发给 **pnpm**。如果你遇到下面的错误： [ERR_PNPM_UNEXPECTED_VIRTUAL_STORE] Unexpected virtual store location dsh: pnpm failed in profile directory C:\Users\xxx\.dsh-desktop\profiles\web **这不是插件本身的问题**（换任何一个插件安装都会失败），而是该 profile 目录的 pnpm 依赖状态失效了：pnpm 在 `node_modules\.modules.yaml` 里记录了安装时的虚拟存储位置（绝对路径），一旦 profile 目录被**移动 / 复制 / 备份恢复**过，或 pnpm 版本 / `virtual-store-dir` 配置发生变化，

**2) 删除该 profile 的依赖目录（只删 node_modules 即可，配置/已装插件名不会丢）**

Remove-Item "$env:USERPROFILE\.dsh-desktop\profiles\web\node_modules" -Recurse -Force

## 🔗 链接

- [GitHub 仓库](https://github.com/elysia395/dsh-wallpaper-engine)
- [完整 README](https://github.com/elysia395/dsh-wallpaper-engine#readme)
- [返回dsh-wallpaper-engine所在分类](../plugins.md)
