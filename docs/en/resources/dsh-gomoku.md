---
title: "dsh-gomoku"
description: "Play Gomoku with AI inside DSH, or let two AIs battle to compare models."
keywords: "dsh-gomoku, fun, plugin, ui, deepseek harness, dsh"
---
# dsh-gomoku

> ⭐ **14** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Fun & lifestyle |
| Stars | ⭐ 14 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | 2026-08-15 |

## One-liner

> Play Gomoku with AI inside DSH, or let two AIs battle to compare models.

## About

总是让 AI 帮你写代码、做表格？这次换它陪你下棋。`@yejiming/dsh-gomoku` 是 DeepSeek Harness 的五子棋插件：在 DSH 侧边栏摆上一盘 15×15 的棋盘，让 DeepSeek 或任何你配置好的模型执子对弈。 这里没有搜索算法，也没有启发式剪枝——每一步落子都来自 LLM 纯粹的推理与判断，堪称对模型「思考能力」最直观的考验。最过瘾的当属双 AI 对战：让两个模型同台厮杀，谁的推理更缜密、更懂审时度势，一局见分晓。 想更进一步？黑、白两方的系统提示词可以分别编辑，约束 AI 落子前的思维链，亲眼看着棋力在你的「调教」下节节攀升——输赢先不论，围观棋路、偷师几手也不亏。 最贴心的是：棋盘弹窗想开就开、想关就关，对局和 AI 的思考在后台照常进行。一边用 DSH 处理正事，一边偷空落一子，摸鱼与工作两不误。

## ✨ Key Features

- **人机与双 AI 对弈**：支持执黑、执白、双 AI 对弈三种模式，15×15 无禁手规则（双三、双四、长连均合法，连成五子及以上即胜）。对弈模式与新开局按钮位于棋盘下方。
- **黑白 AI 分别设置**：黑、白两方可分别选择模型与思考档位（Off / High / Max），互不影响；模型不支持所选档位时自动回落其默认档位。
- **思考过程分侧展示**：黑、白两方的思考记录分别列在棋盘左右两侧（与各自的 AI 设置同侧），默认折叠，点击某手可展开该步的完整推理文本。
- **暂停与手动接管**：棋盘下方【新开局】按钮右侧的【暂停】按钮可随时中断 AI 思考（两者均为「图标 + 文字」的胶囊按钮：⟳ 新开局、⏸ 暂停、▶ 继续，暂停中按钮转为琥珀色高亮）；暂停期间你可为黑白双方轮流落子，没有步数限制，再次点击【继续】后 AI 恢复思考。
- **固定超时与输出上限**：单次落子的端到端超时固定为 3000000 毫秒（3000 秒）、输出 token 上限固定为 32000，随每次落子请求发送，不在界面中暴露。
- **黑白提示词分开编辑**：黑、白两方 AI 的系统提示词分别在棋盘左右两侧的面板中常驻展示、随时编辑，各自可一键恢复默认。默认提示词包含规则、术语（活二/活三/眠三/双活三/四三/防守要点等，附 JSON 示范）、强制思考流程（穷举威胁→分析候选→综合判断）与高水平 Few-shot 对弈示例（每条附返回案例）。
- **弹窗关闭不中断对局**：棋局保存在浏览器端 store 中，关闭棋盘弹窗既不会重置棋局，也不会中断正在进行的 AI 思考，可以一边使用 Harness 主功能一边对弈。
- **瞬时失败自动重试**：流式响应中断（连接断开、限流等瞬时传输故障）会在尝试预算内自动重试，不会直接让整步棋失败。

## 📦 Install

```bash
# 从 npm 安装（首次使用会初始化该 profile）
dsh plugin --profile demo add @yejiming/dsh-gomoku
```

## 🚀 Quick Start

```bash
# 从 GitHub 源码安装（仓库已提交构建产物 lib/，安装时无需构建）
dsh plugin --profile demo add github:omdsh-dev/dsh-gomoku
```

## 📚 Learn more

**快速安装**

支持三种安装方式，均**无需本地构建**（构建产物 `lib/` 已提交进仓库，且不设 `prepare`/`prepack` 脚本）。DSH 的标准插件安装机制是「组合包 → profile」：插件包在 `package.json` 中声明 `dsh.bundle` 并附带 patch 文件（`cordis.patch.yml`），用户用 `dsh plugin` 把它安装进任意 profile。

**从 tarball 安装（tarball 由 pnpm pack 生成，文件名形如 yejiming-dsh-gomok**

pnpm pack dsh plugin --profile demo add ./yejiming-dsh-gomoku-0.0.1.tgz 以上方式都直接使用仓库内提交的预构建产物（`lib/`），安装时不需要执行构建脚本——从 git 安装也无需在 profile 的 `pnpm-workspace.yaml` 里配置 `allowBuilds`。要求 dsh ≥ 0.1.0-rc.6：插件使用 `@deepseek-ai/dsh-host-webserver` 的 `webServer` 服务，更早版本的 dsh 没有该服务，插件行会一直 pending。若 pnpm 提示 peer 依赖警告，可忽略：所需服务由宿主 dsh 在运行时提供。 首次使用 `dsh plugin` 会初始化该 profile（`@deepseek-ai/dsh-base` 作为第一个组合包）；安装后先用

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-gomoku)
- [Full README](https://github.com/omdsh-dev/dsh-gomoku#readme)
- [Back to the Plugins list](../plugins.md)
