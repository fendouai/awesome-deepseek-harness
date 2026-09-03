---
title: "dsh-whale-musume"
description: "元气鲸鱼娘桌宠：摸头养成、工作状态联动、494 条台词与 30 项成就，支持拖拽物理、主题适配与内置设置面板；全本地、零遥测（MIT，102 项单测）。"
keywords: "dsh-whale-musume, fun, plugin, ui, deepseek harness, dsh"
---
# dsh-whale-musume

> ⭐ **48** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 娱乐与生活 |
| 星数 | ⭐ 48 | 状态 | ✅ 活跃 |
| 作者 | [Sutera-Diffusus](https://github.com/Sutera-Diffusus) | 更新时间 | — |

## 一句话介绍

> 元气鲸鱼娘桌宠：摸头养成、工作状态联动、494 条台词与 30 项成就，支持拖拽物理、主题适配与内置设置面板；全本地、零遥测（MIT，102 项单测）。

## 详细介绍

- 默认悬浮形态（200px），支持鼠标拖拽； - 拖拽时切换「被拎起来」立绘，身体随光标移动方向自然摇摆； - **拖拽惯性**：松手后按瞬时速度滑行一小段并旋转回正，撞到屏幕边缘就「抓住」边缘停住；轻放只做一次轻微回弹，位置在滑行结束后才保存； - 待机时保持稳定表情，随机出现喝咖啡、伸懒腰、吃东西等日常小动作； - 待机与工作状态之间使用「下压 → 换图 → 弹起」的动势遮断过渡，不会叠影，不会闪黑； - 在设置里关掉她之后，左下角会留一枚唤回按钮（🐋），点一下就把她叫回来，不会再「消失得找不着」。

## ✨ 核心特性

- 纯前端注入，不修改 DSH 业务 DOM；
- 所有改动可备份、可回滚；
- 资源文件带版本号，升级后强制刷新缓存；
- **立绘预加载**：首屏只预载 5 张常用姿势，其余 90+ 张在空闲时段每 120ms 取一张（优先 `requestIdleCallback`），冷启动切姿势不迟滞，预取失败完全静默；
- 核心状态机与表现层分离，便于二次开发。

## 📦 安装

```bash
dsh plugin --profile web add github:Sutera-Diffusus/dsh-whale-musume
```

## 🚀 快速开始

```bash
git clone https://github.com/Sutera-Diffusus/dsh-whale-musume.git
cd dsh-whale-musume
```

## 📚 更多信息

**安装要求**

> 脚本安装方式会修改 DSH 安装目录中的前端资源文件。虽然脚本自带备份，仍建议安装前关闭 DSH 页面，并记录当前 DSH 版本号。追求零侵入请使用组合包方式。 ---

**方式 A：组合包安装（零侵入，推荐）**

鲸鱼娘同时提供标准 DSH 组合包形态，可直接经 dsh plugin 或插件市场（如 mydsh.dev）安装： dsh plugin --profile web add github:Sutera-Diffusus/dsh-whale-musume 安装后重启 dsh web 并强制刷新页面（`Ctrl+F5`），鲸鱼娘会自动出现。此模式：

**第 2 步：确认 DSH 安装目录**

DSH 安装目录通常包含 `DeepSeekHarness-Launcher.exe` 和 `node_modules`。如果不确定，可以查看启动器配置： Get-Content "<DSH_INSTALL_DIR>\DeepSeekHarness-Launcher.cfg" 其中 `workDir` 字段指向的就是安装目录。下文统一用 `<DSH_INSTALL_DIR>` 代替该路径。

**第 3 步：执行安装脚本**

在插件目录打开 PowerShell，执行： node scripts/apply-theme.mjs --assets-only --target "<DSH_INSTALL_DIR>" node scripts/apply-theme.mjs --mascot-settings --target "<DSH_INSTALL_DIR>" 也可以通过环境变量指定安装目录： $env:DSH_INSTALL_DIR = "<DSH_INSTALL_DIR>" node scripts/apply-theme.mjs --assets-only node scripts/apply-theme.mjs --mascot-settings 脚本输出中的 `Backup:` 路径就是本次改动的备份目录，请保留到确认插件运行正常。

## 🔗 链接

- [GitHub 仓库](https://github.com/Sutera-Diffusus/dsh-whale-musume)
- [完整 README](https://github.com/Sutera-Diffusus/dsh-whale-musume#readme)
- [返回dsh-whale-musume所在分类](../plugins.md)
