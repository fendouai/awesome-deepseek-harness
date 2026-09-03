---
title: "dsh-plugin-hub"
description: "DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 | https://dsh-plugin-hub.hupc.site"
keywords: "dsh-plugin-hub, registry, awesome-list, coding, deepseek harness, dsh"
---
# dsh-plugin-hub

> ⭐ **12** · ✅ 活跃 · 精选列表 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 精选列表 | 分类 | 注册表 |
| 星数 | ⭐ 12 | 状态 | ✅ 活跃 |
| 作者 | [helloHupc](https://github.com/helloHupc) | 更新时间 | 2026-08-21 |

## 一句话介绍

> DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 | https://dsh-plugin-hub.hupc.site

## 详细介绍

全网 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (dsh) 插件聚合检测站: 多数据源自动汇总 → 自己的逻辑去重/分类/排序 → 静态页检索,每小时刷新。 线上地址:https://dsh-plugin-hub.hupc.site

## 🚀 快速开始

```bash
# 跑一次完整 ETL(实时拉取)
python3 scripts/aggregate.py

# 只用本地缓存调试
python3 scripts/aggregate.py --offline

# 本地预览站点
mkdir -p site/data && cp data/plugins.json site/data/plugins.json
cd site && python3 -m http.server 8000
# 打开 http://localhost:8000
```

## 📚 更多信息

**本地预览站点**

mkdir -p site/data && cp data/plugins.json site/data/plugins.json cd site && python3 -m http.server 8000

## 🔗 链接

- [GitHub 仓库](https://github.com/helloHupc/dsh-plugin-hub)
- [完整 README](https://github.com/helloHupc/dsh-plugin-hub#readme)
- [返回dsh-plugin-hub所在分类](../awesome-lists.md)
