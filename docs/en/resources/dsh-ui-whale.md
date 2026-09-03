---
title: "dsh-ui-whale"
description: "Hand-drawn pixel whale companion in the session title bar: blinks, wags its tail, spouts water when a turn completes."
keywords: "dsh-ui-whale, ui, plugin, deepseek harness, dsh"
---
# dsh-ui-whale

> ⭐ **29** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 29 | Status | ✅ active |
| Author | [lhh010](https://github.com/lhh010) | Updated | 2026-08-21 |
| Subcategory | 🐋 Desktop pets | Capabilities | ui |

## One-liner

> Hand-drawn pixel whale companion in the session title bar: blinks, wags its tail, spouts water when a turn completes.

## About

DSH Web UI 的常驻像素鲸鱼伙伴插件：会话标题栏（标题行右侧）常驻一只小鲸鱼，随会话快照实时反应——**零核心改动**。

## 📦 Install

```bash
# 方式一：git 依赖固定 tag（公开镜像，推荐；也可用 github:lhh010/dsh-ui-whale）
dsh plugin --profile web add '@dsh-external/dsh-ui-whale@github:lhh010/dsh-ui-whale#v0.3.12'

# 方式二：本地 link（开发）
git clone https://github.com/lhh010/dsh-ui-whale.git
cd dsh-ui-whale && pnpm install && pnpm run build
dsh plugin --profile web add link:/path/to/dsh-ui-whale
```

## 🚀 Quick Start

```bash
- insert:
    - id: dsh-ui-whale
      name: '@dsh-external/dsh-ui-whale'
```

## 📚 Learn more

**演示 Demo**

各动作 GIF：   > 完整视频：[docs/dsh-ui-whale-demo.mp4](docs/dsh-ui-whale-demo.mp4) > **你的 DSH 版本决定装哪个插件版本**（装错会崩：常见症状 `useConversation is not a function`） > - DSH **0.1.1-rc.2**（npm 最新）：装**旧版** `'@dsh-external/dsh-ui-whale@github:lhh010/dsh-ui-whale#v0.3.4'` > - DSH **0.1.2-alpha.1 / alpha.2 / alpha.3 / alpha.4 / alpha.5**：装**新版**（下方默认命令）

**提示词安装（让 DSH 自己装）**

把下面这段提示词发给任意一个 DSH 会话，模型会替你完成安装： > 帮我安装 dsh-ui-whale 插件（DSH 会话标题栏像素鲸鱼伙伴），步骤： > 1. 执行 `dsh plugin --profile web add '@dsh-external/dsh-ui-whale@github:lhh010/dsh-ui-whale#v0.3.12'`（首次可能被 pnpm 11 拦截 node-pty 构建脚本而失败） > 2. 在 `~/.dsh/profiles/web` 下执行 `pnpm approve-builds --all`（放行构建脚本） > 3. 再执行一次第 1 步的安装命令 > 4. 完成后提醒我硬刷新浏览器（Ctrl/Cmd+Shift+R） > 遇到报错先查 https://github.com/lhh010/dsh-ui-whale README 的常见问

**安装（组织内成员）**

完整步骤见 [INSTALL.md](INSTALL.md)。两条通道任选其一（互斥，勿同时用）： **官方 profile 通道**（0806 默认，配置行热重载，无需重启）： git clone https://github.com/lhh010/dsh-ui-whale.git cd dsh-ui-whale && pnpm install dsh plugin --profile web add link:/path/to/dsh-ui-whale `$DSH_HOME/profiles/web/cordis.patch.yml` 配置行： - id: dsh-ui-whale name: '@dsh-external/dsh-ui-whale' **registry 通道**（需 DSH 已集成 plugin-registry，`dsh registry` 可用；清单已满足 re

## 🔗 Links

- [GitHub Repository](https://github.com/lhh010/dsh-ui-whale)
- [Full README](https://github.com/lhh010/dsh-ui-whale#readme)
- [Back to the Plugins list](../plugins.md)
