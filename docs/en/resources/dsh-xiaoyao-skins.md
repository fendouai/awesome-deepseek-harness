---
title: "dsh-xiaoyao-skins"
description: "夕小瑶 × DeepSeek Harness Web 皮肤合集、安装器与社区创作工具链"
keywords: "dsh-xiaoyao-skins, search, plugin, coding, deepseek harness, dsh"
---
# dsh-xiaoyao-skins

> ⭐ **23** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 23 | Status | ✅ active |
| Author | [147228](https://github.com/147228) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding |

## One-liner

> 夕小瑶 × DeepSeek Harness Web 皮肤合集、安装器与社区创作工具链

## About

一套面向真实 DeepSeek Harness Web profile 的社区皮肤合集表现层插件。每套皮肤都是一个可安装、可卸载、可测试的 DSH，不替换会话、模型、工具、沙箱或插件系统；

## 📦 Install

```bash
flowchart LR
  CLI[一行命令 xiaoyao-skin] --> Catalog[受检皮肤目录]
  Catalog --> DSH[dsh plugin add/remove]
  DSH --> Profile[真实 DSH Web profile]
  Profile --> Host[Host 端空操作入口]
  Host --> Client[Web Client 表现层]
  Client --> UI[CSS / 背景 / 字体 / 动效]
  Profile --> Core[会话 · 模型 · 工具 · 沙箱 · 其他插件]
  Client -.不接管.-> Core
```

## 🚀 Quick Start

```bash
npx --yes --package=https://github.com/147228/dsh-xiaoyao-skins/releases/latest/download/xiaoyao-skin-kit.tgz xiaoyao-skin create moon-rabbit
cd dsh-skin-moon-rabbit
pnpm install
pnpm check
```

## 📚 Learn more

**版权与使用边界**

> [!WARNING] > **独立社区项目声明：** 本项目与 DeepSeek 及 `zhu1090093659/dsh-web-ui` > 原作者不存在隶属、赞助、认证或背书关系。转载截图、发布整合包或迁入代码时，不能只保留 > 本仓库的 MIT 文件；还必须一并保留对应的素材许可与第三方声明。 完整文本与逐项来源见 [LICENSE](LICENSE)、[ASSET_LICENSE.md](ASSET_LICENSE.md) 和 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。如计划将小瑶角色或美术用于商业项目， 请先联系权利人取得单独书面授权。

**安装兼容性与排错**

如果看到 `dsh: pnpm not found on PATH`，说明使用的是旧版工具包；重新执行上面同一条 `releases/latest` 命令即可获取修复版。若自动兜底因网络或代理失败，安装器会给出与当前 Node.js 匹配的手动 `npm install -g pnpm@...` 命令。安装目标失败时不会移除当前皮肤。

## 🔗 Links

- [GitHub Repository](https://github.com/147228/dsh-xiaoyao-skins)
- [Full README](https://github.com/147228/dsh-xiaoyao-skins#readme)
- [Back to the Plugins list](../plugins.md)
