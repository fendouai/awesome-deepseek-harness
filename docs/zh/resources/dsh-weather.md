---
title: "dsh-weather"
description: "天气工具：Open-Meteo 当前天气与多日预报，免费免密钥。"
keywords: "dsh-weather, developer, plugin, search, deepseek harness, dsh"
---
# dsh-weather

> ⭐ **7** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 7 | 状态 | ✅ 活跃 |
| 作者 | [sunshine-lang](https://github.com/sunshine-lang) | 更新时间 | 2026-08-14 |
| 子分类 | 🧰 工具与工具包 | 能力 | search |

## 一句话介绍

> 天气工具：Open-Meteo 当前天气与多日预报，免费免密钥。

## 详细介绍

[English](README.en.md) | 中文 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 天气工具：查询任意城市或地点的实时天气与多日预报，数据来自 [Open-Meteo](https://open-meteo.com/)——免费、无需 API key、无需注册。

## ✨ 核心特性

- `get_weather` 工具：实时温度、体感温度、湿度、风速与天气状况。
- 可选多日预报（最多 7 天）：每日最高/最低温度与天气状况。
- 支持摄氏 / 华氏温度单位。
- 无需 API key；数据来源：[Open-Meteo](https://open-meteo.com/)。

## 📦 安装

```bash
dsh plugin --profile web add "github:sunshine-lang/dsh-weather"
```

## 🚀 快速开始

```bash
dsh plugin --profile web add dsh-weather
```

## 📚 更多信息

**从 GitHub 安装**

dsh plugin --profile web add "github:sunshine-lang/dsh-weather" 然后重启 `dsh --profile web`。`lib/` 已预构建并提交，安装无需构建权限。

**从本地源码安装（开发）**

dsh plugin --profile web add ./dsh-weather > 注意：pnpm 对 `link:` 方式的本地依赖不会自动安装其依赖，需要手动添加到 profile（通过 registry 或 GitHub 安装则会自动处理）： > > ```sh > dsh plugin --profile web add @deepseek-ai/dsh-tools @deepseek-ai/cordis @deepseek-ai/schemastery > ```

**使用方法**

启动 Web UI 后，向模型提问，例如： > 上海现在天气怎么样？ > > 查一下东京的天气，用华氏度，并给出 3 天预报。 模型会调用 `get_weather`：参数 `location`（必填），可选 `units`（`celsius` | `fahrenheit`）和 `days`（1–7）。

**配置**

可通过 `cordis.patch.yml` 或 profile 的 patch 层覆盖任意配置项： - id: dsh-weather config: defaultUnits: fahrenheit timeoutMs: 15000 maxForecastDays: 5 配置无效时插件加载会直接失败，并给出可操作的错误信息。

## 🔗 链接

- [GitHub 仓库](https://github.com/sunshine-lang/dsh-weather)
- [完整 README](https://github.com/sunshine-lang/dsh-weather#readme)
- [返回dsh-weather所在分类](../plugins.md)
