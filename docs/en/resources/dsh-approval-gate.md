---
title: "dsh-approval-gate"
description: "Risk-gated approval automation for DeepSeek Harness: flash pre-classifies whether a write/command is irreversible — safe operations are auto-approved, dangerous ones are escalated to human approval (fail-safe)."
keywords: "dsh-approval-gate, developer, plugin, security, deepseek harness, dsh"
---
# dsh-approval-gate

> ⭐ **4** · ✅ active · plugin · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [moon09300731](https://github.com/moon09300731) | Updated | 2026-08-20 |
| Subcategory | 🛡️ Security & ops | Capabilities | security |

## One-liner

> Risk-gated approval automation for DeepSeek Harness: flash pre-classifies whether a write/command is irreversible — safe operations are auto-approved, dangerous ones are escalated to human approval (fail-safe).

## About

**DeepSeek Harness 自动审批门控 —— 最小人工介入，安全自动放行、危险转人工（fail-safe）。** Flash 模型预判每次沙箱越界：常规操作自动放行，硬风险操作（删除 / 凭据 / 远程 / 系统 / 批量）永远转人工确认；学习沉淀只针对你确认过的操作，并提供界面化人工审查入口。

## ✨ Key Features

- ⚡ **Flash 风险预判**：每次沙箱越界由 Flash 模型判定（`SAFE` / `RISKY:<类别>`），可回补操作自动放行
- 🛡️ **硬风险永远人工**：删除、凭据、远程/生产、系统路径、批量不可回补五类操作直接转人工，不计数、不学习
- 🎯 **确认制学习**：同一操作确认 N-1 次后自动放行；沉淀规则携带**操作指纹**，只放行你确认过的操作
- 🧠 **语义同类验证**：措辞变化但意图相同的操作，由 Flash 对照你的确认样本语义判断，不再依赖关键词
- 🔧 **配置热更新**：`allowlist.json` 修改即时生效，无需重启
- ✅ **人工审查 UI**：自动放行时输入框上方出现绿色提示；「审批」视图（轨迹右侧）展示当前会话完整放行时间线
- 📄 **文件改动对比与撤销**（v0.5.0+）：审批涉及的文件可点击查看 **unified diff**——变动行带上下 5 行上下文、多处修改按 hunk 分区并以「N unmodified lines」分隔条折叠、绿加红删灰上下文、双行号；一键「撤销此改动」投递指令让 AI 按快照恢复文件
- 🗂️ **会话级快照管理**（v0.5.0+）：快照按事件归属会话，审批视图按当前会话统计；清理支持「仅清本会话」与「清空全部」两档，避免误删其他会话未查看的 diff 记录

## 📦 Install

```bash
dsh plugin --profile web add dsh-approval-gate
```

## 🔗 Links

- [GitHub Repository](https://github.com/moon09300731/dsh-approval-gate)
- [Full README](https://github.com/moon09300731/dsh-approval-gate#readme)
- [Back to the Plugins list](../plugins.md)
