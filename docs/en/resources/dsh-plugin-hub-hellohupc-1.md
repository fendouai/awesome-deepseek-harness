---
title: "dsh-plugin-hub"
description: "DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 | https://dsh-plugin-hub.hupc.site"
keywords: "dsh-plugin-hub, registry, awesome-list, coding, deepseek harness, dsh"
---
# dsh-plugin-hub

> ⭐ **12** · ✅ active · awesome-list · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 12 | Status | ✅ active |
| Author | [helloHupc](https://github.com/helloHupc) | Updated | 2026-08-21 |

## One-liner

> DSH 插件聚合站:全网 DeepSeek Harness 插件聚合检索,多源自动去重分类,每小时刷新 | https://dsh-plugin-hub.hupc.site

## About

全网 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (dsh) 插件聚合检测站: 多数据源自动汇总 → 自己的逻辑去重/分类/排序 → 静态页检索,每小时刷新。 线上地址:https://dsh-plugin-hub.hupc.site

## 🚀 Quick Start

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

## 📚 Learn more

**本地预览站点**

mkdir -p site/data && cp data/plugins.json site/data/plugins.json cd site && python3 -m http.server 8000

## 🔗 Links

- [GitHub Repository](https://github.com/helloHupc/dsh-plugin-hub)
- [Full README](https://github.com/helloHupc/dsh-plugin-hub#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
