---
title: "dsh-skin-switcher"
description: "DeepSeek Harness Web GUI 皮肤切换插件：设置界面一键切换已安装皮肤"
keywords: "dsh-skin-switcher, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-skin-switcher

> ⭐ **4** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [zhtx2024](https://github.com/zhtx2024) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, ui |

## One-liner

> DeepSeek Harness Web GUI 皮肤切换插件：设置界面一键切换已安装皮肤

## About

DeepSeek Harness Web GUI 的皮肤切换插件：在设置界面新增「皮肤」页，列出所有已安装的皮肤并提供一键切换按钮，支持一键恢复官方默认外观。

## ✨ Key Features

- **设置界面内切换**：官方设置面板新增「皮肤」页（`settings.section`），已安装皮肤自动列出，无需改代码
- **统一管理所有皮肤**：自动发现 profile 中所有 `dsh-client-ui-skin-*` 皮肤包（支持任意 npm scope，如 `@dsh-external/dsh-client-ui-skin-maid-atelier`），以及 dsh-web-ui 的 `dsh-skins` 聚合载体
- **支持皮肤中心 v2 资产引擎**（0.4.0+）：皮肤中心（`@linxin666/dsh-client-ui-skin-center` >= 0.2.x）内置的 `skins/` 与用户目录 `~/.dsh/skins`（`DSH_SKINS_HOME` 可覆盖）中的 v2 皮肤自动列出；切换写入 `~/.dsh
- **热切换，无需重启**：legacy 皮肤切换写入 `~/.dsh/cordis.patch.yml` 的 managed section（原子重写），DSH 配置监视器数秒内热重载，页面自动刷新生效
- **一键恢复默认**：「恢复默认」回到官方原版外观
- **升级不丢外观**：启动时自动把旧版活跃皮肤迁移到 v2 激活文件（存在 v2 孪生时），并解除旧版写下的皮肤中心禁用行
- **单一管理权威（仅旧版中心）**：legacy 皮肤中心（< 0.2，写 patch 的竞争者，行 id 自动从 bundle patch 发现，兼容 `ui-skin-center` 与 `web-ui-skin-center`）自动禁用；v2 中心是资产引擎，不会被禁用

## 📦 Install

```bash
dsh plugin --profile web add dsh-skin-switcher
```

## 🚀 Quick Start

```bash
# 1. 克隆本仓库
git clone https://github.com/zhtx2024/dsh-skin-switcher.git

# 2. 安装进 web profile
dsh plugin --profile web add link:<克隆路径>/dsh-skin-switcher
```

## 📚 Learn more

**2. 安装进 web profile**

dsh plugin --profile web add link:<克隆路径>/dsh-skin-switcher 然后重启 `dsh web`（或依赖热重载），打开 设置 → 皮肤。

## 🔗 Links

- [GitHub Repository](https://github.com/zhtx2024/dsh-skin-switcher)
- [Full README](https://github.com/zhtx2024/dsh-skin-switcher#readme)
- [Back to the Plugins list](../plugins.md)
