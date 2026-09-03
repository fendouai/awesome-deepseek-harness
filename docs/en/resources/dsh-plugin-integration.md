---
title: "dsh-plugin-integration"
description: "DeepSeek Harness (DSH) 插件整合中心：动态发现、打标分类、重叠/兼容检测、一键启停与失效检测"
keywords: "dsh-plugin-integration, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-integration

> ⭐ **11** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 11 | Status | ✅ active |
| Author | [MutaLucem](https://github.com/MutaLucem) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> DeepSeek Harness (DSH) 插件整合中心：动态发现、打标分类、重叠/兼容检测、一键启停与失效检测

## About

dsh plugin --profile web add github:MutaLucem/dsh-plugin-integration

## ✨ Key Features

- **操作日志**：标题栏「操作日志」按钮展开日志面板，分「当前日志（本次启动）/ 历史日志」，按时间倒序，支持单条删除、清空当前/历史/全部，持久化到 `~/.dsh`。
- **设置窗口原生缩放**：用浏览器原生 `resize` 手柄（设置弹窗右下角）拖拽调整整个设置窗口大小，尺寸持久化到 `localStorage`；标题栏「重置窗口」一键恢复默认 800×800。

## 📦 Install

```bash
dsh plugin --profile web add github:MutaLucem/dsh-plugin-integration
# 重启 DSH 后，设置栏底部出现「插件整合」分页
```

## 🚀 Quick Start

```bash
Client --host.call('analyze')--> Host --读 package.json / cordis.patch.yml / clientModules.graph()
                                       --读 ~/.dsh/dsh-plugin-integration.json（可选覆盖）
                                       --动态解析各 bundle 补丁
                                  Host --返回分析 JSON--> Client 渲染
Client --host.call('toggle'/'switch'/'applyFix')--> Host --写 cordis.patch.yml（受保护拦截）--> 结果
```

## 📚 Learn more

**2. 架构说明**

dsh-plugin-integration/ ├── package.json # 元数据 + dsh.bundle.patch + dsh.client 声明 ├── cordis.patch.yml # bundle 补丁层（insert 一行 loader 条目） ├── config.default.json # 默认配置（知识库 + 重叠组 + 兼容规则 + 保护名单） ├── src/ │ ├── host.js # Host 半（动态形态）：动态发现 + 配置加载 + 检测 + 启停写入 + RPC + 工具 │ ├── client.js # Client 半（动态形态）：settings.section「插件整合」React UI │ ├── host.standalone.js # Host 半（独立 bundle 形态，已实测）：webServer HTTP 路由 

**3. 外部配置文件**

**默认配置**：`config.default.json`（已内置于 `src/host.js` 的 `DEFAULT_CONFIG`，两者需保持一致）。 **用户自定义**：把配置复制为 `~/.dsh/dsh-plugin-integration.json` 后编辑，无需重新编译即可增删插件元数据与规则。 { "protected": ["ui-web-ui-compat"], // 禁止停用的核心条目 "plugins": { // 按 entryId 覆盖/新增（与默认合并） "my-plugin": { "label": "我的插件", "category": "某类", "tags": ["某tag"], "stars": 123, "capability": "…", "boundary": "…" } }, "overlaps": [ /* 整体替换默认重叠组 */ ],

**5.2 形态 B：独立 bundle 安装（推荐发布用）**

`package.json` 已指向 `src/host.standalone.js` / `src/client.standalone.js`，可直接安装： dsh plugin --profile web add github:MutaLucem/dsh-plugin-integration

## 🔗 Links

- [GitHub Repository](https://github.com/MutaLucem/dsh-plugin-integration)
- [Full README](https://github.com/MutaLucem/dsh-plugin-integration#readme)
- [Back to the Plugins list](../plugins.md)
