---
title: "dsh-web-mobile"
description: "DSH Web UI 移动端适配：窄屏好用，宽屏适用"
keywords: "dsh-web-mobile, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-web-mobile

> ⭐ **68** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 68 | 状态 | ✅ 活跃 |
| 作者 | [mexiaosqwq](https://github.com/mexiaosqwq) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding, ui |

## 一句话介绍

> DSH Web UI 移动端适配：窄屏好用，宽屏适用

## 详细介绍

从 npm 一行装： dsh plugin --profile web add dsh-web-mobile 仓库自带构建产物，无 `allowBuilds` 拦截。装完重启 `dsh web`。 本地开发： dsh plugin --profile web add link:/path/to/dsh-web-mobile

## ✨ 核心特性

- **侧栏变抽屉**：手机竖屏下侧栏收进 overlay 抽屉，会话区全宽，点会话行自动收起；屏幕左缘右滑呼出、抽屉内右滑收起
- **弹窗变浮层**：设置、文件树、预览改成底部 sheet，触屏好点
- **状态栏避让**：刘海安全区、深/浅主题、双击缩放都处理
- **输入区不打架**：权限胶囊、模型名、切换菜单在窄屏下不重叠
- **长会话不卡流量**：宿主返回的大 JSON（会话历史等）自动 gzip/brotli 压缩，手机端加载明显提速
- **平板也管**：768–1023px 触屏设备限宽居中；桌面端（鼠标指针）任何宽度都是完全 no-op，窄窗口/系统缩放也不会误启移动 UI

## 📦 安装

```bash
dsh plugin --profile web add dsh-web-mobile
```

## 🚀 快速开始

```bash
> dsh plugin --profile web rm dsh-mobile-nav      # 2.1.x 及更早的装法键名是 @dsh-external/dsh-mobile-nav，同样先 rm
> dsh plugin --profile web add dsh-web-mobile     # GitHub 直装：dsh plugin --profile web add github:mexiaosqwq/dsh-web-mobile
>
```

## 📚 更多信息

**安装**

> [DSHA](https://github.com/qiannianhuanxiang/DSHA) 用户无需单独安装：DSHA 已内置本插件，装 APK 即用。 从 npm 一行装： dsh plugin --profile web add dsh-web-mobile 仓库自带构建产物，无 `allowBuilds` 拦截。装完重启 `dsh web`。 > 包名说明：2026-08-30 起 npm 包名由 `dsh-mobile-nav` 更名为 `dsh-web-mobile`（与 GitHub 仓库名统一，旧 npm 名已整包撤下）；更早的 `@dsh-external/dsh-mobile-nav` 亦不复存在。装过旧版的用户请**先移除再装新名**（patch 行 id 随包名一起换了，新旧并存会把同一插件注册两份）： > > ```sh > dsh plugin --p

## 🔗 链接

- [GitHub 仓库](https://github.com/mexiaosqwq/dsh-web-mobile)
- [完整 README](https://github.com/mexiaosqwq/dsh-web-mobile#readme)
- [返回dsh-web-mobile所在分类](../plugins.md)
