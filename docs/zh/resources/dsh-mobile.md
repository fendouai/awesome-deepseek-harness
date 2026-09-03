---
title: "dsh-mobile"
description: "Unofficial community mobile client for the DeepSeek Harness Web UI."
keywords: "dsh-mobile, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-mobile

> ⭐ **12** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 12 | 状态 | ✅ 活跃 |
| 作者 | [SimonMedy](https://github.com/SimonMedy) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding, ui |

## 一句话介绍

> Unofficial community mobile client for the DeepSeek Harness Web UI.

## 详细介绍

DSH WebUI 移动端适配插件（**PiUI 翻页器结构**）：窄屏下框架本身就是横向 scroll-snap 翻页器，两页卡片——**半开侧边栏页**（手机 `clamp(280px, 70vw, 360px)`；宽屏 560-768px 随视口涨到 `clamp(360px, 50vw, 420px)`，内容拉伸铺满整页）+ **全宽聊天页**。滑到侧边栏页后聊天卡片仍在右边露出一半（PiUI 同款 overlayWidth 效果），聊天渲染零改动。纯客户端适配，零核心改动——官方 rc.2 发行版直接可用。

## ✨ 核心特性

- **PiUI 翻页器**：≤768px 时三栏框架重排为两页横向 snap 轨道——侧边栏页半开宽（约半个视口），聊天页全宽；**滑到侧边栏页时聊天卡片在右半露出（半边信息流）**，PiUI 同款结构
- **宽度自适应**：560-768px 宽屏（横屏手机、大折叠屏、小平板）下侧边栏页从 360px 随视口涨到约半个视口（上限 420px），侧边栏壳冻结的桌面 280px 内容同步拉伸铺满页列——屏幕变宽，侧边栏内容跟着变大，不再留白
- **输入栏省位**：移动端权限选择器只留盾形图标（标签与箭头收起，紧贴 `+` 按钮），模型名**宽度自适应**（以输入栏行宽为容器查询：行内空间足够就直接显示完整模型名，行位紧张才限宽 96px），超长时**带间距的单向循环跑马灯**（双副本 + GPU transform，尾部滚出留空白再从头进入；`prefers
- **侧边栏始终完整渲染**：窄屏下控制器自动展开 AppFrame 折叠的侧边栏并保持（滑动翻页**不同步状态**）——侧边栏列的内容在聊天全屏时也完整留在 DOM 里，滑回来立即可见，**绝不"滑动才跟着渲染"**
- **同色区分**：侧边栏与信息流同色（平页，无圆角阴影）；**只有信息流是卡片**（16px 圆角 + 阴影 + 细边框），PiUI 同款视觉
- **PiUI 3D 翻页**：滚动时聊天卡片 `rotateY/scale` 跟随（`transform-origin` 偏向滑动侧），`prefers-reduced-motion` 关闭
- **吸附修正**：滑动停止后自动吸附最近整页（滑不到位自动回弹/修正），永不卡半页
- **安全区与键盘**：`viewport-fit=cover` + safe-area env() 变量 + visualViewport 驱动的 `--dshm-keyboard-inset`；`100dvh` 动态视口

## 📦 安装

```bash
dsh plugin --profile web add "https://github.com/lehhair/dsh-mobile/releases/latest/download/dsh-external-dsh-mobile.tgz"
```

## 🚀 快速开始

```bash
git clone https://github.com/lehhair/dsh-mobile.git
dsh plugin --profile web add link:E:/dev/dsh-mobile
```

## 🔗 链接

- [GitHub 仓库](https://github.com/SimonMedy/DSH-Mobile)
- [完整 README](https://github.com/SimonMedy/DSH-Mobile#readme)
- [返回dsh-mobile所在分类](../plugins.md)
