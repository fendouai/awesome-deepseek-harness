---
title: "awesome-dsh-plugins (Radar)"
description: "雷达索引仓库：自动扫描发现的所有 dsh 插件候选，带证据驱动的兼容性矩阵。"
keywords: "awesome-dsh-plugins (Radar), registry, awesome-list, search, observability, deepseek harness, dsh"
---
# awesome-dsh-plugins (Radar)

> ⭐ **1,309** · ✅ 活跃 · 精选列表 · 近期 ⬆️ +35

| | | | |
|---|---|---|---|
| 类型 | 精选列表 | 分类 | 注册表 |
| 星数 | ⭐ 1,309 | 状态 | ✅ 活跃 |
| 作者 | [AdamPlatin123](https://github.com/AdamPlatin123) | 更新时间 | 2026-08-21 |

## 一句话介绍

> 雷达索引仓库：自动扫描发现的所有 dsh 插件候选，带证据驱动的兼容性矩阵。

## 详细介绍

**开源的 DeepSeek Harness 插件生态雷达——持续发现、运行级验证、15 分钟快照。自动生成 artifact同步在[PLUGINS-ALL.md](PLUGINS-ALL.md)中更新。** 安装前就知道哪个能用，不用自己踩坑。 --- **架构原则：目录是构建产物（Catalog is a build artifact）。** Radar Engine（开源 → engine/） ↓ 机器可读快照（data/snapshots/，每 15 分钟） ↓ 目录渲染器（聚合 · 分类 · 双语渲染） ↓ ┌─ PLUGINS-ALL.md 全量清单 ├─ 精选插件榜 / 整合包 ├─ 生态快照 / 兼容矩阵 └─ dshfind 等下游消费方

## 🚀 快速开始

```bash
Radar Engine（开源 → engine/）
     ↓
机器可读快照（data/snapshots/，每 15 分钟）
     ↓
目录渲染器（聚合 · 分类 · 双语渲染）
     ↓
┌─ PLUGINS-ALL.md 全量清单
├─ 精选插件榜 / 整合包
├─ 生态快照 / 兼容矩阵
└─ dshfind 等下游消费方
```

## 📚 更多信息

**工作原理**

> 数据截至快照 `20260903T131502Z`（2026-09-03 21:15:03 UTC+8 · 分类器 unified-v2-bridge） flowchart TB subgraph Discovery["发现（每 6 小时 · probe 每 15 分钟 巡检触发）"] A1["GitHub Search<br/>topic ×2 + keyword ×3<br/>候选 17736 · 龄 249m"] A2["本地库补全 · 去重 repo id"] A3["私有 org 仓排除<br/>35s 错峰 · 403 退避 · dshow 黑名单"] end subgraph Validation["验证（driver 20s 流式循环）"] B1{"package.json<br/>name + main/exports/dsh?"} end B1 -->|"插件 35

**3. 安装、验证和回滚**

本目录不是包管理器，也没有被本仓库验证过的统一安装命令。请以插件自身 README 的安装方式为准，并建议按以下顺序操作： 1. 阅读插件的安装、配置、权限和卸载说明。 2. 固定插件版本或 commit，不直接依赖会漂移的默认分支。 3. 先在隔离 profile 或测试环境加载，不提供生产密钥和敏感数据。 4. 执行一个最小功能任务，记录 DSH 版本、插件版本和日志。 5. 保留原配置与锁文件；失败时能移除插件并恢复环境。 若插件安装或功能本身出错，请优先在插件仓库反馈；若目录链接、分类或状态证据有误，请在本仓库提交 issue 或 PR。

## 🔗 链接

- [GitHub 仓库](https://github.com/AdamPlatin123/awesome-dsh-plugins)
- [完整 README](https://github.com/AdamPlatin123/awesome-dsh-plugins#readme)
- [返回awesome-dsh-plugins (Radar)所在分类](../awesome-lists.md)
