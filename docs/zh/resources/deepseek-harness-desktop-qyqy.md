---
title: "deepseek-harness-desktop"
description: "DeepSeek Harness Desktop: self-contained Windows desktop shell (Electron) that auto-starts dsh web, plus a subtle Codex-flavored theme plugin."
keywords: "deepseek-harness-desktop, desktop, client, coding, ui, deepseek harness, dsh"
---
# deepseek-harness-desktop

> ⭐ **10** · ✅ 活跃 · 客户端 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 10 | 状态 | ✅ 活跃 |
| 作者 | [qyqy-1109](https://github.com/qyqy-1109) | 更新时间 | 2026-08-17 |

## 一句话介绍

> DeepSeek Harness Desktop: self-contained Windows desktop shell (Electron) that auto-starts dsh web, plus a subtle Codex-flavored theme plugin.

## 详细介绍

把 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 变成**双击即用的 Windows 桌面应用**: - **独立窗口**承载 DSH Web GUI,不再需要手开浏览器、不再需要记命令; - **自动启动服务**:双击图标后自动拉起 `dsh web`(已有服务则直接复用),关窗口最小化到**托盘**; - **完全自包含**:安装包内置完整的 dsh CLI 和 Node 运行时(Electron 43 / Node 24),**最终用户不需要安装任何东西**; - **内置常用插件**:安装包附带 6 个插件(背景图库、Codex 风味、dshmarket、dsh-difyctl、super-injector、mode-boost),首次启动自动装进全新 profile,朋友开箱即用 - **应用图标可更换**:托盘菜单 → "应用图标" → 经典蓝色鲸鱼 / 黑色鲸鱼 / **上传自定义图片**(自动裁剪为方形并适配 7 档桌面图标尺寸,同步更新窗口、托盘和桌面快捷方式图标); - **官方鲸鱼图标** + 附赠一个**保留 DSH 原生风格、只加一点 Codex 终端质感**的主题点缀插件。 ---

## ✨ 核心特性

- **独立窗口**承载 DSH Web GUI,不再需要手开浏览器、不再需要记命令;
- **自动启动服务**:双击图标后自动拉起 `dsh web`(已有服务则直接复用),关窗口最小化到**托盘**;
- **完全自包含**:安装包内置完整的 dsh CLI 和 Node 运行时(Electron 43 / Node 24),**最终用户不需要安装任何东西**;
- **内置常用插件**:安装包附带 6 个插件(背景图库、Codex 风味、dshmarket、dsh-difyctl、super-injector、mode-boost),首次启动自动装进全新 profile,朋友开箱即用
- **应用图标可更换**:托盘菜单 → "应用图标" → 经典蓝色鲸鱼 / 黑色鲸鱼 / **上传自定义图片**(自动裁剪为方形并适配 7 档桌面图标尺寸,同步更新窗口、托盘和桌面快捷方式图标);
- **官方鲸鱼图标** + 附赠一个**保留 DSH 原生风格、只加一点 Codex 终端质感**的主题点缀插件。

## 📦 安装

```bash
git clone https://github.com/qyqy-1109/deepseek-harness-desktop.git
cd deepseek-harness-desktop
npm install
```

## 🚀 快速开始

```bash
> npm approve-scripts electron
> npm install
>
```

## 📚 更多信息

**第 1 步:拿到安装包**

从发布者处获取 `DeepSeek Harness Desktop Setup 0.1.5.exe`(约 176MB),或从 [GitHub Releases](../../releases) 下载。

**第 2 步:安装**

1. 双击安装包; 2. 若出现蓝色 **SmartScreen 提示"Windows 已保护你的电脑"** —— 因为软件未购买代码签名证书,这是正常现象: - 点击 **"更多信息"** → **"仍要运行"**; 3. 等待进度条完成(**首次安装 2~10 分钟都正常**,见下方"常见问题"); 4. 安装完成后桌面自动出现 **"DeepSeek Harness"** 快捷方式,应用会自动打开。

**常见问题(FAQ)**

**Q: 安装很慢?** 正常。安装包 154MB、解压后约 400MB,且文件数量多,杀毒软件会逐个扫描。等 2~10 分钟即可;超过 15 分钟可将安装包目录加入 Windows Defender 排除项后重试。 **Q: 打开后报 "Failed to load plugins"?** 请重新下载**最新版本**安装包(旧版本存在运行时兼容问题,已在 0.1.0+ 修复)。若仍有问题,把窗口中的完整错误文本发给开发者。 **Q: 双击没反应 / 弹出错误框?** **Q: 需要梯子吗?** 不需要。只有配置 API Key 后调用 DeepSeek 模型需要能访问 DeepSeek API(国内可直接访问)。 ---

**1. 克隆与安装依赖**

git clone https://github.com/qyqy-1109/deepseek-harness-desktop.git cd deepseek-harness-desktop npm install > 若 npm 提示 electron 的 install 脚本被拦截(npm 11 的 allow-scripts 安全机制): > > ```bash > npm approve-scripts electron > npm install > ```

## 🔗 链接

- [GitHub 仓库](https://github.com/qyqy-1109/deepseek-harness-desktop)
- [完整 README](https://github.com/qyqy-1109/deepseek-harness-desktop#readme)
- [返回deepseek-harness-desktop所在分类](../clients.md)
