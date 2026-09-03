---
title: "dsh-plugin-quote-reply"
description: "DSH plugin: select text in a conversation, then quote it into the composer or reply in a new window. / DeepSeek Harness 划词引用插件：选中文字一键引用回复或新窗口回复。"
keywords: "dsh-plugin-quote-reply, input-editing, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-quote-reply

> ⭐ **1** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Input & editing |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [yangYzc](https://github.com/yangYzc) | Updated | 2026-08-14 |

## One-liner

> DSH plugin: select text in a conversation, then quote it into the composer or reply in a new window. / DeepSeek Harness 划词引用插件：选中文字一键引用回复或新窗口回复。

## About

**DeepSeek Harness (DSH) 划词引用插件** — 在会话中选中文字，一键「引用回复」或「新窗口回复」。 Select text (划词) in a DSH conversation, then quote it into the composer or reply in a new window. ---

## ✨ Key Features

- **引用回复**：把选中文字以 markdown 引用块（`> …`）插入当前输入框，直接接着打字回复。
- **新窗口回复**：自动创建并打开一个新会话，引用已预填在新会话的输入框里。

## 📦 Install

```bash
# 任意 profile（推荐 web）
dsh plugin --profile web add dsh-plugin-quote-reply
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add "github:<your-name>/dsh-plugin-quote-reply"
```

## 📚 Learn more

**从 Git 安装（备选）**

dsh plugin --profile web add "github:<your-name>/dsh-plugin-quote-reply" git 安装会触发 `prepare` 构建脚本。pnpm ≥ 10 默认拒绝执行 git 依赖的构建脚本，首次安装会失败并提示你放行——把报错里给出的包名写进 profile 的 `pnpm-workspace.yaml`： allowBuilds: dsh-plugin-quote-reply: true 然后重新执行上面的 add 命令。（放行 = 允许在安装时执行该包的代码，只放行你信任的源码。）

**使用 Usage**

1. 在会话里用鼠标选中一段文字（比如助手回答中的一句）。 2. 选中处下方出现工具条。 3. 点「引用回复」——引用进当前输入框；或点「新窗口回复」——开新会话并预填引用。 4. 打字，发送。

## 🔗 Links

- [GitHub Repository](https://github.com/yangYzc/dsh-plugin-quote-reply)
- [Full README](https://github.com/yangYzc/dsh-plugin-quote-reply#readme)
- [Back to the Plugins list](../plugins.md)
