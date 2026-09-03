---
title: "dsh-douyin"
description: "DSH WebUI 侧栏短视频插件：原生播放器、系列导航、直链解析与精确历史回放"
keywords: "dsh-douyin, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-douyin

> ⭐ **6** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [AnacondaKC](https://github.com/AnacondaKC) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, ui |

## One-liner

> DSH WebUI 侧栏短视频插件：原生播放器、系列导航、直链解析与精确历史回放

## About

DSH WebUI 侧栏短视频插件：**原生播放器直接解析视频直链播放**。顶部可选择学姐、甜妹、COS、舞蹈等 21 个系列，支持自动连播、滚轮切换与精确历史回放。

## 📦 Install

```bash
dsh plugin --profile web add /path/to/DSH-douyin
# 重启 dsh web 后生效
```

## 🚀 Quick Start

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

## 📚 Learn more

**原理**

聚合视频源来自 `api.yujn.cn` 的分类接口。每次请求会 302 到随机 mp4 直链；插件通过 host resolver 读取 `Location`，再交给原生 `<video>` 播放。历史栈保存真实直链，因此向上滚动能回到同一段视频。

## 🔗 Links

- [GitHub Repository](https://github.com/AnacondaKC/dsh-douyin)
- [Full README](https://github.com/AnacondaKC/dsh-douyin#readme)
- [Back to the Plugins list](../plugins.md)
