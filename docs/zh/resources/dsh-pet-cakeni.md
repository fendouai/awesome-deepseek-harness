---
title: "dsh-pet"
description: "DeepSeek Harness 桌面宠物插件 + 完整素材生成链：AI 提示词 → 绿幕视频 → 透明动画 → 可安装插件，从零到宠物全流程可复现"
keywords: "dsh-pet, fun, plugin, coding, deepseek harness, dsh"
---
# dsh-pet

> ⭐ **274** · ✅ 活跃 · 插件 · 近期 ⬆️ +41

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 娱乐与生活 |
| 星数 | ⭐ 274 | 状态 | ✅ 活跃 |
| 作者 | [PC2005-cloud](https://github.com/PC2005-cloud) | 更新时间 | 2026-08-21 |

## 一句话介绍

> DeepSeek Harness 桌面宠物插件 + 完整素材生成链：AI 提示词 → 绿幕视频 → 透明动画 → 可安装插件，从零到宠物全流程可复现

## 详细介绍

一只住在 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 里的桌面宠物：待机呼吸、随机动作（打瞌睡、玩魔方、写代码、吃火锅……97 个手绘风透明动画随时无缝衔接）、左右转向、屏幕漫游、点击 Q 弹、拖拽甩抛反弹、右键菜单点播动作、余额动画 + 头顶联想气泡——可多开同屏，能脱离浏览器住上**桌面**（透明置顶小窗），也能自己添加**全新宠物种类**（pet pack）。 这不是一个普通插件，而是**完整的三件套项目**： ① 提示词（配方） → ② 素材生成链（引擎） → ③ 插件（成品） AI 生成动画的配方 源视频 → 透明动画的管线 运行在 DSH 里的宠物 任何人 clone 本仓库，都可以**从零生成自己的桌面宠物**——换角色、换动作、换风格，全流程可复现。 ---

## ✨ 核心特性

- **纯粹的桌宠**：核心就是陪你——没有天气查询、系统监控、Agent 状态感知等花活；除了**可选的余额展示**（见下节）与**系统通知**（对话完成 / 生成失败 / 输出截断 / 权限申请 / 用户选择，窗口失焦时弹系统级通知）外没有其他业务功能。零核心改动（不碰 DSH 内核）
- **余额展示**：实时显示当前 LLM 服务商的余额/额度——DeepSeek 官方显示账户余额（¥），OpenCode Zen Go 显示 5h/周/月 三个额度窗口中最紧张的一个；每次刷新按档位播放余额动画，头顶弹出联想气泡（随宠物大小等比缩放，10 秒后自动消失）；每只宠物可独立开关（`balanceEnable
- **动画链**：每个动画（含待机）播完立即按权重选下一个（权重配置于 `config.jsonc`，默认 idle 10 / turn 5 / move 5 + 动作分类权重），首尾相接永不停止
- **多开**：可配置同时显示多个宠物，每只宠物独立的大小与位置（设置页「桌宠配置」添加/删除）
- **屏幕漫游**：朝 facing 方向行走，先检查空间、不走出屏幕
- **点击/拖拽（弹簧跟手 + 甩抛反弹 + Q 弹）**：点击有回应动画并「Q 弹」挤压回弹（贴地锚定，reduce-motion 跳过）；拖拽为过阻尼弹簧跟手，用力甩出会沿抛物线飞行、屏幕边缘反弹、落地摩擦停稳且**每次落地 Q 弹一下**（温柔放下 = 原地停住），两端同一套纯函数物理与挤压曲线（`dsh-pet/
- **右键菜单**：右键宠物弹出级联菜单——桌面端根项为「**打开网站 / 查看余额 / 回到初始位置** + **动作**」、浏览器端为「**回到初始位置** + 动作」；「打开网站」用系统默认浏览器打开 DSH 网站（等效网页里 Ctrl+点击链接）；「查看余额」立即弹余额气泡播档位动画（桌面端；浏览器端用对话框 `
- **左右朝向**：所有动画可镜像，人物可朝左/朝右

## 📦 安装

```bash
# ① 前置要求：确认 Node.js 已安装
node -v

# ② 安装 DSH 启动器与 pnpm（已装可跳过；装完请重新打开终端）
npm install -g @deepseek-ai/dsh pnpm
dsh --version   # 验证 dsh 命令可用

# ③ 安装本插件
dsh plugin --profile web add dsh-pet
```

## 🚀 快速开始

```bash
# ① clone 本仓库，进入插件目录
git clone https://github.com/PC2005-cloud/dsh-pet.git
cd dsh-pet/dsh-pet

# ② 安装依赖
npm install

# ③ 构建（tsdown → lib）
npm run prepare     # 构建完整 lib（npm install / npm publish 时会自动执行）

# ④ 安装到 DSH（file: 指向本目录，用构建好的 lib）
dsh plugin --profile web add file:D:/path/to/dsh-pet
```

## 📚 更多信息

**③ 安装本插件**

dsh plugin --profile web add dsh-pet 重启 `dsh web`，宠物出现在界面右上角（默认配置角落，可在设置页修改）。 > **兼容性**：本插件在 dsh **`0.1.1-rc.2`** 下开发并测试（`dsh --version` 可查看你的版本）。建议使用相同版本；其他版本如遇问题欢迎反馈。

**④ 安装到 DSH（file: 指向本目录，用构建好的 lib）**

dsh plugin --profile web add file:D:/path/to/dsh-pet > 注：`prepare`（npm install / npm publish 时自动执行，也可手动 `npm run prepare`）才产出**完整可安装**的 lib——除 tsdown 构建外还构建桌面共享核心（`shared-core.js`）、生成类型声明并收敛发布 `files` 清单；裸 `tsdown` 构建会缺桌面运行时与类型。

**⚙️ 配置（大小 / 位置 / 多开）**

桌宠的大小、位置、多开均可配置，两条途径： > 💡 **两条途径只是编辑入口不同，最终都是同一份用户配置**——配置能力远不止设置页那几个选项：设置页可改大小/位置/边距/显示位置/余额开关/多开，但**手动编写配置文件可以任意自由配置**（动画池、播放权重、事件动画、刷新周期……），只要**格式与包内默认配置 `config.jsonc` 一致**即可，用户配置会**整体覆盖**对应字段的默认值。

**方式二：config.jsonc（单一来源）**

插件包内 `dsh-pet/assets/config.jsonc` 的 `pets` 数组定义**默认宠物**： "pets": [ { "id": "main", "size": 462, "balanceEnabled": true, "display": "both", "position": { "corner": "top-right", "marginX": 24, "marginY": 100 } } ]

## 🔗 链接

- [GitHub 仓库](https://github.com/PC2005-cloud/dsh-pet)
- [完整 README](https://github.com/PC2005-cloud/dsh-pet#readme)
- [返回dsh-pet所在分类](../plugins.md)
