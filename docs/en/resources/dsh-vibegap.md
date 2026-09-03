---
title: "dsh-vibegap"
description: "Vocabulary spelling cards in DSH Web that appear during running sessions, persist progress locally, and optionally share the VibeGap desktop cursor."
keywords: "dsh-vibegap, fun, plugin, ui, learning, notifications, deepseek harness, dsh"
---
# dsh-vibegap

> ⭐ **0** · 🧪 experimental · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Fun & lifestyle |
| Stars | ⭐ 0 | Status | 🧪 experimental |
| Author | [ktao732084-arch](https://github.com/ktao732084-arch) | Updated | — |

## One-liner

> Vocabulary spelling cards in DSH Web that appear during running sessions, persist progress locally, and optionally share the VibeGap desktop cursor.

## About

**AI agent 等待间隙的效率小窗** — vibe coding 的间隙(gap)里,不切屏做点有价值的小事。当 Claude Code / Codex 在跑任务时,小窗自动弹出;agent 跑完(或等你确认权限)时提醒并自动收起。第一个面板是背单词:进度全局持久,换对话、换 agent 都接着上次背。小窗是可插拔面板框架,后续会有更多"间隙面板"(消息、资讯、视频……)。

## ✨ Key Features

- **自动生命周期**:提交任务约 18 秒后弹出(快任务不打扰);agent 完成/等确认时横幅提醒,拼完当前词自动收起
- **断点续背**:一本词书一个全局游标,换对话、换 agent、重启机器都接着背;顺序/乱序(固定种子)双模式,切换不丢进度
- **多 agent**:Claude Code / Codex(官方 Hooks)、pi / dsh / WorkBuddy(适配模板见 `vibegap/adapters/`);Codex 另有日志恢复兜底
- **会话面板**:按 agent 分组显示各会话的运行中/已完成状态
- **打字模式**:qwerty-learner 式拼写,音标+发音(有道音源,可关),Tab 看答案(看过即记入错词),←→ 浏览前后词
- **错词复习 / 每日目标 / AI 新闻轮播条**(卡兹克 [AIHOT](https://aihot.virxact.com) 公开 API)
- **按需运行**:Agent 启动时自动拉起;窗口隐藏且无 Agent/交互 10 分钟后自动退出,无需手动守着 daemon
- **小细节**:跟随系统或手动切换深浅主题、运行中全局热键手动唤醒(Ctrl+Alt+W,被占自动换)、自动唤醒可关、整窗拖拽、不抢焦点

## 📦 Install

```bash
git clone https://github.com/ktao732084-arch/vibegap && cd vibegap
pip install -e .
python scripts/fetch_dicts.py        # 下载内置词书(CET6 / GRE,来自 qwerty-learner)
python vibegap/adapters/claude_code/install.py
python vibegap/adapters/codex/install.py
vibegap-ensure --toggle              # 可选:立即启动并检查悬浮窗
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add dsh-vibegap
dsh web
```

## 📚 Learn more

**Windows 安装包(推荐,不需要 Python)**

从 [Releases](https://github.com/ktao732084-arch/vibegap/releases/latest) 下载 `VibeGap-<version>-Setup.exe` 后直接安装。安装器默认接入检测到的 Claude Code / Codex， 只写当前用户目录，不请求管理员权限；不默认开机自启。 安装后无需手动保持任何终端：Agent 第一次上报事件时会自动拉起 VibeGap，窗口隐藏且 无 Agent/交互 10 分钟后自动退出。纯手动背词可从开始菜单打开 VibeGap。 当前安装包尚未做商业代码签名，Windows 可能显示“未知发布者”；可用同一 Release 中的 `SHA256SUMS.txt` 校验文件。安装包自带 CET-6 与 GRE 3000 词书，首次启动即可使用。

**源码安装(开发者)**

git clone https://github.com/ktao732084-arch/vibegap && cd vibegap pip install -e . python scripts/fetch_dicts.py # 下载内置词书(CET6 / GRE,来自 qwerty-learner) python vibegap/adapters/claude_code/install.py python vibegap/adapters/codex/install.py vibegap-ensure --toggle # 可选:立即启动并检查悬浮窗

## 🔗 Links

- [GitHub Repository](https://github.com/ktao732084-arch/vibegap)
- [Full README](https://github.com/ktao732084-arch/vibegap#readme)
- [Back to the Plugins list](../plugins.md)
