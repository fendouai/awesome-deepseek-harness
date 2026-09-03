---
title: "dsh-memory"
description: "Two-phase long-term memory plugin for DeepSeek Harness (DSH): per-session extraction + global consolidation, always-injected summary, and memory_list/read/search/add tools."
keywords: "dsh-memory, memory, plugin, coding, search, deepseek harness, dsh"
---
# dsh-memory

> ⭐ **4** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [yan5236](https://github.com/yan5236) | Updated | — |
| Subcategory | 🧠 Memory systems | Capabilities | coding, memory, search |

## One-liner

> Two-phase long-term memory plugin for DeepSeek Harness (DSH): per-session extraction + global consolidation, always-injected summary, and memory_list/read/search/add tools.

## About

**项目定位**：个人的大型研究项目——目标用户是**对 AGI 有需要的研究人员**（白箱智能 / 可解释性 / 协议工程 / 记忆机制 / 扮演论研究者），不是面向普通用户的消费级插件。它把「智能论 v3.4」协议的理论（条件论 / 扮演论 / 信息差 / 端口架构与锚定验证）工程化为**可运行、可审计、可复现**的机制： - **白箱优先**：知识问答 **100% 白箱处理（零 LLM）**，LLM 降级为外部校验器——机制可解释、可追溯、可验证（详见「白箱智能管线」） - **协议驱动**：每项能力都是「智能论 v3.4 / 条件论 / 扮演论 / 端口架构」条款的具体工程实现，可对照协议验证 - **机制可解释**：白箱处理的每一步（条件识别 → 单元匹配 → 组合生成 → 自校验 → 固化）都有证据链可查 - **可审计**：工具调用、记忆写入、自校验判定全链路留痕；护栏宪章约束对外行为 这不是又一个"记忆插件"。灵枢（AEIS）是一套遵循「智能论 v3.4」协议的**时空记忆引擎**（端口架构 + 锚定验证 + 认知图/条件路由 + 原生神经网络），它把当前大模型范式缺失的 AGI 能力逐一给了工程实现。 ---

## ✨ Key Features

- **跨会话自我连续性**：Agent 用 `lingshu_recall/search/timeline` 记住并召回过去——对话间、会话间、甚至不同子代理间共享一份持续的"我"。
- **自演化知识飞轮**：`distill / flywheel / learn / induce` 把经验验证→归纳→联想→蒸馏为可复用模式，记忆越用越强。
- **可审计的信任**：护栏宪章 v2 ——对外部与人类使用者的行为边界成文、可执行、可审计、可终裁（[宪章全文](docs/guardrail-charter.md) 随包自带）。
- **自我认知**（大脑模式 brain）：`cognition / cognition_report / self_reliability / emotional_bias / recursive_reflect` ——能反思自己的认知状态与情绪倾向。
- **角色扮演**（v3.3 扮演论）：自我锚点（SELF 层 no_forget 不可遗忘）· 特化价值观（条件触发）· 跨会话角色记忆 · 世界认知（子知识·虚拟化世界观）· 自定义翻译（现实↔虚拟名词表）· **同源角色扮演网页（/roleplay）**——角色人设长对话不崩（100 轮测试零漂移）。
- **零运行时依赖**：手写 stdio MCP 桥，与灵枢 D-005「核心零外部依赖」哲学一致——你拿到的是一个干净、可信、可审的大脑。
- **动态 schema + 进程自愈**：工具清单运行时拉取（灵枢升级 DSH 零改动），Python 子进程崩溃自动指数退避重启。
- **工具注册竞态补注册**：启动时 python 未就绪（竞态）→ 桥重连成功后自动补注册工具（2s 轮询），不再"工具永久缺失"。

## 📦 Install

```bash
# ① 装灵枢大脑（一条命令，零外部依赖；v0.5.0 完整自包含：核心+白箱+知识库随包）
pip install aeis-0.5.0-py3-none-any.whl          # wheel 从 Releases 页下载，或 git+ 在线安装

# ② 装进 DSH 的 web profile（pnpm 协调入口，不要用裸 npm install 装进 profile）
dsh plugin --profile web add @furongjun1999/dsh-memory

# ③ 配置 cordis.yml 启用
```

## 🚀 Quick Start

```bash
- id: lingshu-memory
  name: '@furongjun1999/dsh-memory'
  config:
    dbPath: 'data/lingshu.db'
    identity: '灵枢'
    tools: 'brain'      # 'brain' 全心智 | 'core' 精选
```

## 📚 Learn more

**③ 配置 cordis.yml 启用**

name: '@furongjun1999/dsh-memory' config: dbPath: 'data/lingshu.db' identity: '灵枢' tools: 'brain' # 'brain' 全心智 | 'core' 精选 > ⚠️ **安装方式**：插件必须通过 **`dsh plugin --profile <name> add`** 装进 profile（它会用 pnpm + `autoInstallPeers: false` 正确解析 peer 依赖）。 > **不要**用 `npm install` 把插件装进 profile 的 `node_modules`——那会引入错误版本的 `@deepseek-ai` peer 包，导致插件加载失败 / 浏览器报错。 > 想自己改源码？克隆 `FuRongJun-1999/dsh-memory` 后用 `npm 

**🗺️ 功能使用教学 · 条件路由图**

**想做什么 → 找对应泳道 → 走条件边到功能**（流程图 = 认知图 = 条件路由图，**82 工具**全收录，[工具总表 → docs/灵枢MCP工具总表_v3.4.md](docs/灵枢MCP工具总表_v3.4.md)）：  > 图中每条边 = 一个使用条件：比如「问知识」走 `wisdom_chat`（白箱优先），「验证说法」走 `wisdom_verify`（互维双通道），「记住信息」走 `remember`。找不到路径时用 `service_info` 看协议实例身份。 ---

**🧭 认知图使用方法 & 工作纪律（v1.1）**

> 认知图 = 时空记忆图/条件注释图。节点**四要素**：conditions(生效) / subgraph(子内容·嵌套) / negative(不适用) / execution(如何执行)。

**📊 记忆系统使用性评分（五维标尺）**

> 视角：**使用性**（普通用户/开发者体感）——「存、找、想、准、安」五维。 > 评估基准：公开能力 + 设计者校准（2026-08-17）。灵枢分数经设计者核对（不虚高）。 （插图源文件：[memory_score.html](docs/memory_score.html)，可浏览器打开重新截图） **综合分 = min × 0.4 + mean × 0.6**（安全性是底线，短板效应显著） **灵枢各维度依据**（设计者校准，不虚高）：S=语义时空图+五层记忆+条件空间；R=三层语义检索（二元组+语义坐标+bge）+图谱遍历+因果候选生成器（条件论对自身，被拒路径→候选→验证闭环）+知识点级精确命中（卡⊃知识点嵌套子图）+歧义词多义列举（语境不确定时列全各义）；J=验证单元（P37）+递归反思+白箱校验+结构排斥+主动遗忘决策器（forget_advisor：未使用记忆归档，可逆）

## 🔗 Links

- [GitHub Repository](https://github.com/yan5236/dsh-memory)
- [Full README](https://github.com/yan5236/dsh-memory#readme)
- [Back to the Plugins list](../plugins.md)
