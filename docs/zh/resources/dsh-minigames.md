---
title: "dsh-minigames"
description: "DSH Web UI 右侧小游戏面板：18 款离线小游戏（恐龙跳一跳 / 俄罗斯方块 / 坦克大战 / 扫雷 / 2048 / 数独 / 吃豆人 / 跟枪练习等），可扩展游戏注册表，等待模型回复或修 bug 时的摸鱼神器"
keywords: "dsh-minigames, fun, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-minigames

> ⭐ **25** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 娱乐与生活 |
| 星数 | ⭐ 25 | 状态 | ✅ 活跃 |
| 作者 | [lhh010](https://github.com/lhh010) | 更新时间 | 2026-08-21 |

## 一句话介绍

> DSH Web UI 右侧小游戏面板：18 款离线小游戏（恐龙跳一跳 / 俄罗斯方块 / 坦克大战 / 扫雷 / 2048 / 数独 / 吃豆人 / 跟枪练习等），可扩展游戏注册表，等待模型回复或修 bug 时的摸鱼神器

## 详细介绍

DSH Web UI 浮动小游戏窗口：等待模型回复或修 bug 时的摸鱼神器。 - **折叠态**：窗口隐藏后留下一个圆形浮动 🎮 按钮（默认右下角），**可自由拖动**并记住位置， 按住拖动（位移超过 5px）松手不会打开窗口；**单击**才重新打开面板。 - **展开态**：浮动小游戏窗口，**拖动标题栏**可随意移动，松手靠近屏幕边缘自动**吸附** （左右停靠/上下贴边），位置、停靠状态与宽度均持久化，刷新后自动恢复；默认宽度 min(50vw, 640px)，可拖左缘调整 360px–80vw，面板内自由选择游戏。 - **游戏**（全部离线、零资源文件、Canvas 绘制）： 1. 🦖 **恐龙跳一跳** —— Chrome 经典小恐龙（昼夜/雨天）； 2. 🧱 **俄罗斯方块** —— 经典下落消除； 3. 🛡️ **坦克大战（带 AI）** —— 2D 坦克对战，敌军追踪 + 视线开火，共 3 波； 4. 💎 **消消乐** —— 点击消除四连通同色块，目标分过关、逐关递增； 5. 🔢 **华容道** —— 16 格数字华容道（15-puzzle），滑动方块按序排列，用时越短分越高； 6. 🐍 **贪吃蛇** —— 经典贪吃蛇，穿越边界会从对侧出现（环面地图）； 7. 🔢 **2048** —— 方向键滑动合并数字，合成 2048 即达成； 8. 💣 **扫雷** —— 左键翻开、右键标旗、双击数字自动展开周围； 9. 🃏 **记忆翻牌** —— 翻开两张配对，步数越少分越高； 10. ⚫ **五子棋 vs AI** —— 15×15，AI 会进攻也会堵你； 11. 🦘 **跳一跳** —— 按住蓄力、松开起跳，落点越准加分越多； 12. 🧱 **打砖块** —— 移动挡板反弹小球，清完进入下一关、球速递增； 13. 🔨 **打地鼠** —— 30 秒限时点

## ✨ 核心特性

- **折叠态**：窗口隐藏后留下一个圆形浮动 🎮 按钮（默认右下角），**可自由拖动**并记住位置，
- **展开态**：浮动小游戏窗口，**拖动标题栏**可随意移动，松手靠近屏幕边缘自动**吸附**
- **游戏**（全部离线、零资源文件、Canvas 绘制）：
- **预留扩展接口**：游戏注册表（`registerGame`），新增游戏只需实现一个接口。
- **体验细节**：隐藏窗口/切换标签页时自动暂停游戏、恢复时继续；每局最高分存
- **尺寸自适应**：游戏画布按面板**真实可用空间**自适应（工具条+画布+按键提示整体

## 📦 安装

```bash
dsh plugin --profile web remove @dsh-external/dsh-minigames
```

## 🚀 快速开始

```bash
pnpm install
pnpm run typecheck   # tsc --noEmit
pnpm run test        # vitest 纯逻辑单测（189 个：引擎/棋盘/世界模型/三消/华容道/贪吃蛇/2048/扫雷/翻牌/五子棋/跳一跳/打砖块/打地鼠/黑白棋/Flappy/数独/吃豆人/跟枪/注册表）
pnpm run build       # tsc 声明 + tsdown：lib/index.js（node half）+ lib/client.js（浏览器 bundle）
```

## 📚 更多信息

**方式二：本地安装**

git clone https://github.com/lhh010/dsh-minigames.git # 或直接使用本目录 cd dsh-minigames pnpm install pnpm build

**可选：确认组合配置只出现一个插件行**

dsh --profile web --dump-config | grep dsh-minigames > **安装提示**：pnpm 11 首次安装可能拦截 node-pty 等构建脚本——在 `~/.dsh/profiles/web` 下执行 `pnpm approve-builds --all` 放行后重跑安装命令；装完**硬刷新浏览器**（Ctrl/Cmd+Shift+R）。

**提示词安装（让 DSH 自己装）**

把下面这段提示词发给任意一个 DSH 会话，模型会替你完成安装： > 帮我安装 dsh-minigames 插件（DSH 浮动小游戏窗口插件），步骤： > 1. 执行 `dsh plugin --profile web add '@dsh-external/dsh-minigames@github:lhh010/dsh-minigames#v0.3.13'`（首次可能被 pnpm 11 拦截 node-pty 构建脚本而失败） > 2. 在 `~/.dsh/profiles/web` 下执行 `pnpm approve-builds --all`（放行构建脚本） > 3. 再执行一次第 1 步的安装命令 > 4. 完成后提醒我硬刷新浏览器（Ctrl/Cmd+Shift+R） > 遇到报错先查 https://github.com/lhh010/dsh-minigames README 的常

**方式二：本地安装**

git clone https://github.com/lhh010/dsh-minigames.git # 或直接使用本目录 cd dsh-minigames pnpm install pnpm build

## 🔗 链接

- [GitHub 仓库](https://github.com/lhh010/dsh-minigames)
- [完整 README](https://github.com/lhh010/dsh-minigames#readme)
- [返回dsh-minigames所在分类](../plugins.md)
