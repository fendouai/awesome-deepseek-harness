---
title: "dsh-tps"
description: "只是一个 tps 插件"
keywords: "dsh-tps, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-tps

> ⭐ **1** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [Small-tailqwq](https://github.com/Small-tailqwq) | Updated | — |

## One-liner

> 只是一个 tps 插件

## About

DSH Web 实时 TPS 徽标：在 "Deep diving…" 状态行内显示实时 tokens-per-second，跟随运行行自然显隐。 English: [README.en.md](README.en.md)

## ✨ Key Features

- **内置 DeepSeek 分词器的实时 TPS**：滚动 5 秒窗口采样流式输出，token 数按 DeepSeek-V3 BPE 分词器**精确**计数——完整预分词（Split ×3 + 字节映射）与 merge 贪心合并，与官方 `tokenizers` 库对 tokenizer.json 的输出逐 token
- **跟随显隐，零适配**：徽标渲染在 "Deep diving… 7分25秒" 行内，turn 结束、提问/审批面板接管时随行一起消失——无需为待办条、队列条或提问面板编写任何隐藏逻辑
- **不重复原生功能**：窗口级平均值（AVG/TTFT/token 总数）是内置 StatsLine 的职责，本插件刻意只做瞬时速率
- **悬停淡出**：停留 2 秒淡出并变为可穿透（`pointer-events: none`）；隐藏期间光标在徽标上或其附近（外扩 8px）则保持隐藏，移开后经 3 秒宽限期才恢复（期间回到附近则取消恢复），光标停驻不会循环触发
- **纯前端**：所有读数派生自会话快照，无 store、无事件监听、无网络调用

## 📦 Install

```bash
cd <dsh>
dsh plugin --profile web add github:Small-tailqwq/dsh-tps
```

## 🚀 Quick Start

```bash
"dependencies": {
  "dsh-tps": "github:Small-tailqwq/dsh-tps"
}
```

## 📚 Learn more

**第 1 步：安装插件**

cd <dsh> dsh plugin --profile web add github:Small-tailqwq/dsh-tps 本包声明了 `dsh.bundle`（patch 指向仓库内 `cordis.yml`），`dsh plugin` 会**自动**把它追加进 profile 的 `dsh.profile.bundles`，无需手写任何 insert。从 git 安装时若 pnpm 拦截构建，按提示把包加入 profile 的 `pnpm-workspace.yaml` `allowBuilds` 后重试。 **手动安装**（无 `dsh plugin` 命令时）：编辑 `~/.dsh/profiles/web/package.json`： "dependencies": { "dsh-tps": "github:Small-tailqwq/dsh-tps" } （本地路径可

## 🔗 Links

- [GitHub Repository](https://github.com/Small-tailqwq/dsh-tps)
- [Full README](https://github.com/Small-tailqwq/dsh-tps#readme)
- [Back to the Plugins list](../plugins.md)
