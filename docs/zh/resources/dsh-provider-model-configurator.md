---
title: "dsh-provider-model-configurator"
description: "DSH 模型 Pro:为 DSH WebUI 提供将 pi-ai 预设或任意已配置提供商的模型上下文、输出上限、推理档位与兼容开关一键应用到目标提供商,并集中查看、新建、编辑、复制与删除各提供商模型条目的能力。"
keywords: "dsh-provider-model-configurator, memory, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-provider-model-configurator

> ⭐ **18** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 记忆与上下文 |
| 星数 | ⭐ 18 | 状态 | ✅ 活跃 |
| 作者 | [LiangYin233](https://github.com/LiangYin233) | 更新时间 | — |
| 子分类 | 📦 上下文管理 | 能力 | coding, ui |

## 一句话介绍

> DSH 模型 Pro:为 DSH WebUI 提供将 pi-ai 预设或任意已配置提供商的模型上下文、输出上限、推理档位与兼容开关一键应用到目标提供商,并集中查看、新建、编辑、复制与删除各提供商模型条目的能力。

## 详细介绍

一个 [DeepSeek Harness (DSH)](https://github.com/deepseek-ai/dsh) **插件**:在独立设置页「模型 Pro / Model Pro」中集中**查看、新建、编辑、复制与删除**已配置提供商下的模型条目——上下文窗口、最大输出、输入模态、推理档位与推理兼容开关。还可以从内置的 `llm-pi-ai` 模型列表读取您所需要配置的模型的上下文参数、最大Token，无需自行填写、手动查询。

## ✨ 核心特性

- 选择**目标提供商**,列出其显式模型条目与配置摘要,可**编辑 / 删除**;
- **新建**:输入模型 ID,手动填写显示名、上下文窗口、最大输出、输入模态(text/image)、推理档位(档位 → wire 值,`off` 留空 = 不发送);推理档位与输入模态均支持「未设置(继承目录)」,避免把未配置的字段写成显式默认值;
- **复制填充**:「使用模型预设」打开来源选择器,从预设目录或其他提供商挑一个模型快速填充表单;
- **兼容开关 (compat)**:编辑 `thinkingFormat`(openai / deepseek / openrouter / together / zai / qwen / string-thinking / ant-ling)与 `supportsReasoningEffort`(true / fal

## 📦 安装

```bash
# 从 GitHub 安装
dsh plugin --profile web add github:LiangYin233/dsh-provider-model-configurator#v0.3.9

# 或从 GitHub tarball 安装
dsh plugin --profile web add https://github.com/LiangYin233/dsh-provider-model-configurator/archive/refs/tags/v0.3.9.tar.gz

# 或从本地打包安装
npm pack
dsh plugin --profile web add ./dsh-provider-model-configurator-0.3.9.tgz
```

## 📚 更多信息

**dsh-provider-model-configurator**

一个 [DeepSeek Harness (DSH)](https://github.com/deepseek-ai/dsh) **插件**:在独立设置页「模型 Pro / Model Pro」中集中**查看、新建、编辑、复制与删除**已配置提供商下的模型条目——上下文窗口、最大输出、输入模态、推理档位与推理兼容开关。还可以从内置的 `llm-pi-ai` 模型列表读取您所需要配置的模型的上下文参数、最大Token，无需自行填写、手动查询。

**从 GitHub 安装**

dsh plugin --profile web add github:LiangYin233/dsh-provider-model-configurator#v0.3.9

**或从 GitHub tarball 安装**

dsh plugin --profile web add https://github.com/LiangYin233/dsh-provider-model-configurator/archive/refs/tags/v0.3.9.tar.gz

**或从本地打包安装**

npm pack dsh plugin --profile web add ./dsh-provider-model-configurator-0.3.9.tgz 安装后**重启 Web 服务器并刷新页面**,打开设置 → 左侧导航「模型 Pro」(Models 页之后)。

## 🔗 链接

- [GitHub 仓库](https://github.com/LiangYin233/dsh-provider-model-configurator)
- [完整 README](https://github.com/LiangYin233/dsh-provider-model-configurator#readme)
- [返回dsh-provider-model-configurator所在分类](../plugins.md)
