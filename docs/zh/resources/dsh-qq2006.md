---
title: "dsh-qq2006"
description: "DSH (DeepSeek Harness) 的 QQ2006 皮肤插件：注册 qq2006 主题、镜像 body[data-ds-skin]、全局皮肤表与完整素材"
keywords: "dsh-qq2006, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-qq2006

> ⭐ **24** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 24 | 状态 | ✅ 活跃 |
| 作者 | [LaplaceYoung](https://github.com/LaplaceYoung) | 更新时间 | — |
| 子分类 | 🎨 皮肤与主题 | 能力 | coding, ui |

## 一句话介绍

> DSH (DeepSeek Harness) 的 QQ2006 皮肤插件：注册 qq2006 主题、镜像 body[data-ds-skin]、全局皮肤表与完整素材

## 详细介绍

**把 DeepSeek Harness 的 WebUI 一键变回 2006 年的 QQ 客户端。** QQ2006 皮肤插件：注册珊瑚蓝主题、镜像 `body[data-ds-skin]`、全局皮肤表 + 完整组件级补丁，从登录窗到聊天窗口全链路还原 2006 年的那个蓝色小企鹅。可切换、可持久化、默认皮肤零污染。 聊天窗口：好友信息条 + 原版九宫格标题带 + 列表式消息 + QQ 秀右侧栏

## ✨ 核心特性

- **可切换皮肤**：设置 → 通用 → **QQ2006 皮肤**（当前 DSH 外观行仍是浅色 / 深色 / 跟随系统三个色块，插件自带开关）；偏好持久化，刷新/重启保持；随时切回默认皮肤，**零污染契约**（所有补丁锚定 `body[data-ds-skin='qq2006']`）
- **QQ2006 登录窗**：九宫格窗口框、三态按钮、记住密码/自动登录联动、连接中动态点动画
- **主面板**：用户头部（50×50 蓝描边头像 + 6 个 mini 钮）、面板栏 10 钮（27×37 原版底条格）、分组/好友行（原版行高与 hover）、右键菜单
- **聊天窗口**：标题栏 4 钮（含 65×24 原版"菜单"文字钮）、大工具栏 12 钮、小工具栏 8 钮（全部原版素材、原生尺寸）
- **原版消息形式**：列表式消息（自己绿色昵称 / 对方深蓝紫昵称 + HH:MM:SS 时间 + 黑色正文），宋体渲染
- **QQ 秀右侧栏**：对方形象 / 个人空间（真实会话统计）/ 我的形象，默认展开
- **换肤 4 预设**：经典蓝 / 粉红 / 薄荷绿 / 紫罗兰，窗口内实时切换
- **真实交互**：Alt+S 发送、右键复制、hover 操作行（复制/引用/转发）、提示音、QQ 黄色反馈 tip

## 📦 安装

```bash
dsh plugin --profile web add https://github.com/LaplaceYoung/dsh-qq2006
```

## 🚀 快速开始

```bash
git clone https://github.com/LaplaceYoung/deepseek-harness.git
cd deepseek-harness
git checkout skin/qq2006
pnpm install
pnpm run build
node --import tsx/esm apps/cli/src/bin.ts web
```

## 📚 更多信息

**方式一：npm 发行版（dsh plugin 安装）**

仓库已包含预构建产物（`lib/`），发行版用户可直接从 GitHub 安装： dsh plugin --profile web add https://github.com/LaplaceYoung/dsh-qq2006 安装后**重启 `dsh web`**，然后： 1. 打开 **设置 → 通用** 2. 找到 **QQ2006 皮肤**，点 **开启** DSH 0.1.0-rc.7+ 还会在 **设置 → 插件 → 插件配置** 里出现同名卡片。当前上游外观行（到 `dsh-v0.1.2-alpha.1`）仍然只渲染浅色 / 深色 / 跟随系统，**不会出现第 4 个色块**——这是上游硬编码，不是安装失败。0.1.2 起开关文案走第三方 UI 语言注册（中 / 英）。 启用后获得：**可见的 QQ2006 壳层**（经典蓝标题栏、侧栏、输入区、设置窗）+ 珊瑚蓝 `--dsw-

## 🔗 链接

- [GitHub 仓库](https://github.com/LaplaceYoung/dsh-qq2006)
- [完整 README](https://github.com/LaplaceYoung/dsh-qq2006#readme)
- [返回dsh-qq2006所在分类](../plugins.md)
