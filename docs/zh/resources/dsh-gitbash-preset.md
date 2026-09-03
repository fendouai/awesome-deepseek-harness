---
title: "dsh-gitbash-preset"
description: "DeepSeek Harness 插件：一键安装「极简模式 (Git Bash)」agent preset —— 把 DSH 自带极简模式中的 bash 调用映射到 Git for Windows 的 bash（MSYS），让 Windows 上的极简模式真正可用。"
keywords: "dsh-gitbash-preset, vision, plugin, coding, git, multi-agent, deepseek harness, dsh"
---
# dsh-gitbash-preset

> ⭐ **136** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 136 | 状态 | ✅ 活跃 |
| 作者 | [liceses](https://github.com/liceses) | 更新时间 | 2026-08-16 |
| 子分类 | 👁️ 视觉工具 | 能力 | coding, git, multi-agent |

## 一句话介绍

> DeepSeek Harness 插件：一键安装「极简模式 (Git Bash)」agent preset —— 把 DSH 自带极简模式中的 bash 调用映射到 Git for Windows 的 bash（MSYS），让 Windows 上的极简模式真正可用。

## 详细介绍

DeepSeek Harness 插件：一键安装「极简模式 (Git Bash)」agent preset —— 把 DSH 自带极简模式中的 bash 调用映射到 Git for Windows 的 bash（MSYS），让 Windows 上的极简模式真正可用。

## ✨ 核心特性

- **幂等安装**：插件启动时把打包的预设复制到用户预设根（`${DSH_HOME:-~/.dsh}/.agent-presets/minimal-gitbash/`），已存在则跳过，`force: true` 才覆盖；
- **自动探测 bash**：`GIT_BASH` 环境变量 → 常见安装目录（ProgramFiles / ProgramFiles(x86) / LOCALAPPDATA）→ PATH 中的 `bash.exe` → 兜底 `bash`，无需硬编码路径；
- **沙箱感知门控**：MSYS 运行时无法在 Windows 受限令牌沙箱内启动（无法创建 signal pipe），因此命令仅在"完全访问"策略下执行——不绕过沙箱，受限时给出明确升级指引；
- **极简不变**：固定 persona、`str_replace_editor`、无上下文压缩，与原极简模式一致。

## 📦 安装

```bash
dsh plugin --profile web add @icelily/dsh-gitbash-preset
```

## 🚀 快速开始

```bash
npm run check   # 三个文件语法检查（插件、执行器、测试）
npm run test    # 单元测试：路径转换 / 探测优先级 / 配置校验，10 个用例
```

## 📚 更多信息

**安装**

dsh plugin --profile web add @icelily/dsh-gitbash-preset 或手动合并 `cordis.patch.yml` 到 profile patch 层。**重启 DSH 后生效**；重启后插件会自动安装预设（已存在则 no-op，不会覆盖你已有的版本）。 也可以不装插件，直接把 `agent-presets/minimal-gitbash/` 目录复制到 `~/.dsh/.agent-presets/`。

**使用**

1. Web 界面新建会话，选择 **极简模式 (Git Bash)**； 2. 二选一启用 bash： - 把会话沙箱切到**完全访问**，之后所有 bash 调用直接走 git bash； - 或保持 workspace-write，让模型在第一次调用失败后按提示用 `sandbox_permissions: "danger-full-access"` + justification 单次升级（走正常审批流程）。

**配置**

**预设配置**（`agent-presets/minimal-gitbash/agent.cordis.yml` 中 `gitbash-executor`）： **插件配置**（`cordis.patch.yml` 插入行）：

## 🔗 链接

- [GitHub 仓库](https://github.com/liceses/dsh-gitbash-preset)
- [完整 README](https://github.com/liceses/dsh-gitbash-preset#readme)
- [返回dsh-gitbash-preset所在分类](../plugins.md)
