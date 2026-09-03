---
title: "dsh-ramify"
description: "Ramify 是 DeepSeek Harness 的创意分支画布插件，用树状工作区生成、对比和迭代多个可交互方案。"
keywords: "dsh-ramify, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-ramify

> ⭐ **11** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 11 | 状态 | ✅ 活跃 |
| 作者 | [yanglongyun](https://github.com/yanglongyun) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Ramify 是 DeepSeek Harness 的创意分支画布插件，用树状工作区生成、对比和迭代多个可交互方案。

## 详细介绍

1. 点击 DSH 左侧栏的 **Ramify**，打开内置工作台。 2. 在 Ramify 原生输入框中输入需求并选择方案数量。 3. 插件立即创建项目并进入画布，同时把任务提交给当前 DSH 会话和模型。 4. Agent 通过 Ramify 工具把方案持续写入画布，节点和预览实时出现。 5. 点击节点右上角的发散按钮，输入修改要求，即可从该节点继续生成分支。 整个过程不需要复制本地地址，也不需要在 Ramify 中再次配置模型或 API Key。

## ✨ 核心特性

- **原生 DSH 插件**：使用标准插件清单、Cordis 服务和 Client UI 插槽，没有修改 Harness 源码。
- **原生 Ramify UI**：保留网站版创作票据、数量选择、画布、节点卡片和分支气泡的视觉与交互。
- **当前会话驱动**：界面提交通过 DSH 官方会话输入能力发送给当前模型。
- **即时进入画布**：首页提交后先创建项目并立即打开画布，Agent 随后向同一项目写入节点。
- **可视化分支**：从任意已完成节点继续发散，旧方案保持不变。
- 安装后自动启动本地画布，不需要单独运行 CLI。
- HTML、Markdown、SVG、图片、视频和音频作品可直接预览。
- SQLite 本地持久化，前端轻量轮询感知变更。

## 📦 安装

```bash
git clone https://github.com/yanglongyun/dsh-ramify.git
cd dsh-ramify
npm install
npm run build

dsh plugin --profile web add "$PWD"
dsh web --port 3099
```

## 🚀 快速开始

```bash
dsh plugin --profile web add @ramify/dsh-ramify
dsh web --port 3099
```

## 📚 更多信息

**从源码安装（当前推荐）**

git clone https://github.com/yanglongyun/dsh-ramify.git cd dsh-ramify npm install npm run build dsh plugin --profile web add "$PWD" dsh web --port 3099

**使用**

你可以直接从 Ramify 输入框开始，也可以在 DSH 对话中要求 Agent 使用 Ramify。例如： > 使用 Ramify 为这个 AI 搜索产品探索三个明显不同的落地页方向，做出可预览页面让我比较。 插件向模型注册以下工具：

**配置**

用户可以在 profile 的 `cordis.patch.yml` 中覆盖插件配置： name: '@ramify/dsh-ramify' config: port: 9519 dataDir: '/absolute/path/to/ramify-data' startupTimeoutMs: 5000 shutdownTimeoutMs: 3000 `dataDir` 省略时使用平台默认目录：

## 🔗 链接

- [GitHub 仓库](https://github.com/yanglongyun/ramify-dsh)
- [完整 README](https://github.com/yanglongyun/ramify-dsh#readme)
- [返回dsh-ramify所在分类](../plugins.md)
