---
title: "dsh-douyin"
description: "DSH WebUI 侧栏短视频插件：原生播放器、系列导航、直链解析与精确历史回放"
keywords: "dsh-douyin, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-douyin

> ⭐ **6** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [AnacondaKC](https://github.com/AnacondaKC) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding, ui |

## 一句话介绍

> DSH WebUI 侧栏短视频插件：原生播放器、系列导航、直链解析与精确历史回放

## 详细介绍

DSH WebUI 侧栏短视频插件：**原生播放器直接解析视频直链播放**。顶部可选择学姐、甜妹、COS、舞蹈等 21 个系列，支持自动连播、滚轮切换与精确历史回放。

## 📦 安装

```bash
dsh plugin --profile web add /path/to/DSH-douyin
# 重启 dsh web 后生效
```

## 🚀 快速开始

```bash
type SourceKind = 'feed' | 'direct' | 'web'

interface VideoSource {
  id: string          // 稳定 id（自定义源 custom-<timestamp>）
  name: string
  kind: SourceKind    // 播放方式，见下
  url: string
  custom?: boolean    // 用户添加的源
}
```

## 📚 更多信息

**原理**

聚合视频源来自 `api.yujn.cn` 的分类接口。每次请求会 302 到随机 mp4 直链；插件通过 host resolver 读取 `Location`，再交给原生 `<video>` 播放。历史栈保存真实直链，因此向上滚动能回到同一段视频。

## 🔗 链接

- [GitHub 仓库](https://github.com/AnacondaKC/dsh-douyin)
- [完整 README](https://github.com/AnacondaKC/dsh-douyin#readme)
- [返回dsh-douyin所在分类](../plugins.md)
