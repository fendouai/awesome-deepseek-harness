---
title: "dsh-super-pm"
description: "DeepSeek Harness 的产品思考助手：先明确负向边界，拆开事实与假设，经七套产品视角讨论取舍，并将确认的决策沉淀到项目记忆中。"
keywords: "dsh-super-pm, developer, plugin, context, research, workflow, deepseek harness, dsh"
---
# dsh-super-pm

> ⭐ **0** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 0 | 状态 | ✅ 活跃 |
| 作者 | [Lohaslee](https://github.com/Lohaslee) | 更新时间 | — |

## 一句话介绍

> DeepSeek Harness 的产品思考助手：先明确负向边界，拆开事实与假设，经七套产品视角讨论取舍，并将确认的决策沉淀到项目记忆中。

## 详细介绍

`dsh-super-pm` 是一个面向 **DeepSeek Harness（DSH）** 的标准插件，用于打包和分发 [Super PM](https://github.com/Lohaslee/super-pm) 产品思考 Skill。 它不是一个独立的产品管理系统，也不是简单的提示词集合，而是把 Super PM 的产品分析方法、七套产品视角、双语参考资料和工作流，以 DSH 可安装的插件形式提供给模型使用。

## ✨ 核心特性

- **负向边界优先**：先明确这次绝不能发生、明确不做和不可接受的成本，再讨论功能和方案。
- **区分事实与假设**：分开记录用户原话、事实、推断、建议和待验证假设，不用肯定语气掩盖未知。
- **动态组织产品视角**：只使用能够改变当前判断的产品维度和视角，不机械地让所有角色轮流发言。
- **支持 Lead PM**：可以指定一个产品视角负责整体方向，其他视角负责挑战、补充和识别风险。
- **适配不同产品类型**：根据问题选择需求与价值、产品系统、使用与交付、触点与形态、体验与信任等相关维度。
- **优先验证高风险假设**：先给出最低成本的验证方案，再决定是否进行外部研究、竞品检查或原型验证。
- **支持决策沉淀**：在获得明确授权后，将重要产品决定保存到项目的 `.super-pm/decisions.md`。
- **按需输出产物**：可以生成决策简报、产品报告或面向 AI coding agent 和交付团队的 PRD。

## 📦 安装

```bash
dsh plugin --profile web add github:Lohaslee/dsh-super-pm
```

## 🚀 快速开始

```bash
dsh plugin --profile web add /absolute/path/to/dsh-super-pm
```

## 📚 更多信息

**从 npm 安装**

dsh plugin --profile web add dsh-super-pm 修改服务端 profile 组合后，需要重启 `dsh web`。不要把 `/super-pm` 当成直接命令：DSH Slash Command 不会发送模型回合。请直接输入产品请求，例如 `使用 super-pm，帮我诊断这个产品的留存问题`，或直接描述产品决策、0 到 1 想法、功能定义或产品诊断问题。

## 🔗 链接

- [GitHub 仓库](https://github.com/Lohaslee/dsh-super-pm)
- [完整 README](https://github.com/Lohaslee/dsh-super-pm#readme)
- [返回dsh-super-pm所在分类](../plugins.md)
