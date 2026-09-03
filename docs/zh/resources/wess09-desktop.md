---
title: "DeepSeekHarnessDesktop (wess09)"
description: "DeepSeek Harness 桌面端打包。"
keywords: "DeepSeekHarnessDesktop (wess09), desktop, client, deepseek harness, dsh"
---
# DeepSeekHarnessDesktop (wess09)

> ⭐ **66** · ✅ 活跃 · 客户端

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 66 | 状态 | ✅ 活跃 |
| 作者 | [wess09](https://github.com/wess09) | 更新时间 | 2026-08-13 |

## 一句话介绍

> DeepSeek Harness 桌面端打包。

## 详细介绍

将 [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) 打包成三平台桌面应用： **Electron 桌面壳 + 内置 Node 运行时 + 完整 Harness 环境**，双击即用。

## ✨ 核心特性

- **一键启动**：双击 `DeepSeekHarness.exe` → 自动拉起后端 → 直接打开 DeepSeek Harness Web UI
- **内置 Node 24**：自包含运行时，用户无需安装 Node.js
- **完整环境**：打包了 Harness 全部依赖（链接已物化为真实文件）
- **无边框窗口**：UI 铺满窗口，右上角内嵌最小化 / 最大化 / 关闭按钮
- **单实例**：重复启动不会拉起多个后端
- **免管理员**：Windows 安装到 `%LocalAppData%\Programs\DeepSeek Harness`

## 📦 安装

```bash
node build/build-harness.js        # 克隆 → 删 packageManager → .npmrc(hoisted) → pnpm install → pnpm build
```

## 🚀 快速开始

```bash
node build/materialize3.js resources/harness   # junction/符号链接 → 真实文件
node build/trim.js                             # 删除冗余 @deepseek-ai 副本、拷贝 web 前端
```

## 📚 更多信息

**🚀 使用**

1. 双击 `DeepSeekHarnessSetup-*.exe` 安装（免管理员，自动建桌面快捷方式） 2. 双击桌面「DeepSeek Harness」图标 3. 首次使用：在 Web 界面设置 **DeepSeek API Key**

## 🔗 链接

- [GitHub 仓库](https://github.com/wess09/DeepSeekHarnessDesktop)
- [完整 README](https://github.com/wess09/DeepSeekHarnessDesktop#readme)
- [返回DeepSeekHarnessDesktop (wess09)所在分类](../clients.md)
