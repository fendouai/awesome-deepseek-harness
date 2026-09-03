---
title: "dsh-gitbash-preset"
description: "DeepSeek Harness 插件：一键安装「极简模式 (Git Bash)」agent preset —— 把 DSH 自带极简模式中的 bash 调用映射到 Git for Windows 的 bash（MSYS），让 Windows 上的极简模式真正可用。"
keywords: "dsh-gitbash-preset, vision, plugin, coding, git, multi-agent, deepseek harness, dsh"
---
# dsh-gitbash-preset

> ⭐ **136** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 136 | Status | ✅ active |
| Author | [liceses](https://github.com/liceses) | Updated | 2026-08-16 |
| Subcategory | 👁️ Vision tools | Capabilities | coding, git, multi-agent |

## One-liner

> DeepSeek Harness 插件：一键安装「极简模式 (Git Bash)」agent preset —— 把 DSH 自带极简模式中的 bash 调用映射到 Git for Windows 的 bash（MSYS），让 Windows 上的极简模式真正可用。

## About

DeepSeek Harness 插件：一键安装「极简模式 (Git Bash)」agent preset —— 把 DSH 自带极简模式中的 bash 调用映射到 Git for Windows 的 bash（MSYS），让 Windows 上的极简模式真正可用。

## ✨ Key Features

- **幂等安装**：插件启动时把打包的预设复制到用户预设根（`${DSH_HOME:-~/.dsh}/.agent-presets/minimal-gitbash/`），已存在则跳过，`force: true` 才覆盖；
- **自动探测 bash**：`GIT_BASH` 环境变量 → 常见安装目录（ProgramFiles / ProgramFiles(x86) / LOCALAPPDATA）→ PATH 中的 `bash.exe` → 兜底 `bash`，无需硬编码路径；
- **沙箱感知门控**：MSYS 运行时无法在 Windows 受限令牌沙箱内启动（无法创建 signal pipe），因此命令仅在"完全访问"策略下执行——不绕过沙箱，受限时给出明确升级指引；
- **极简不变**：固定 persona、`str_replace_editor`、无上下文压缩，与原极简模式一致。

## 📦 Install

```bash
dsh plugin --profile web add @icelily/dsh-gitbash-preset
```

## 🚀 Quick Start

```bash
npm run check   # 三个文件语法检查（插件、执行器、测试）
npm run test    # 单元测试：路径转换 / 探测优先级 / 配置校验，10 个用例
```

## 📚 Learn more

**安装**

dsh plugin --profile web add @icelily/dsh-gitbash-preset 或手动合并 `cordis.patch.yml` 到 profile patch 层。**重启 DSH 后生效**；重启后插件会自动安装预设（已存在则 no-op，不会覆盖你已有的版本）。 也可以不装插件，直接把 `agent-presets/minimal-gitbash/` 目录复制到 `~/.dsh/.agent-presets/`。

**使用**

1. Web 界面新建会话，选择 **极简模式 (Git Bash)**； 2. 二选一启用 bash： - 把会话沙箱切到**完全访问**，之后所有 bash 调用直接走 git bash； - 或保持 workspace-write，让模型在第一次调用失败后按提示用 `sandbox_permissions: "danger-full-access"` + justification 单次升级（走正常审批流程）。

**配置**

**预设配置**（`agent-presets/minimal-gitbash/agent.cordis.yml` 中 `gitbash-executor`）： **插件配置**（`cordis.patch.yml` 插入行）：

## 🔗 Links

- [GitHub Repository](https://github.com/liceses/dsh-gitbash-preset)
- [Full README](https://github.com/liceses/dsh-gitbash-preset#readme)
- [Back to the Plugins list](../plugins.md)
