---
title: "dsh-security-audit"
description: "DSH 本机安全审计插件：配置/插件来源/会话/网络暴露面，只读脱敏风险报告"
keywords: "dsh-security-audit, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-security-audit

> ⭐ **13** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 13 | 状态 | ✅ 活跃 |
| 作者 | [omdsh-dev](https://github.com/omdsh-dev) | 更新时间 | 2026-08-21 |
| 子分类 | 🛡️ 安全与运维 | 能力 | coding |

## 一句话介绍

> DSH 本机安全审计插件：配置/插件来源/会话/网络暴露面，只读脱敏风险报告

## 详细介绍

[English](README.en.md) DSH 本机安全审计插件 —— 防御性、只读的安全审计：配置、凭据存储元数据、已安装插件来源、关键路径权限、会话文件结构与网络暴露面。输出脱敏、可复现、可定位的风险报告。 仓库：[https://github.com/omdsh-dev/dsh-security-audit](https://github.com/omdsh-dev/dsh-security-audit)（public）

## ✨ 核心特性

- **只读**：绝不修改/删除任何文件，绝不执行被审计插件的代码，绝不主动连接远程目标
- **秘密脱敏**：疑似秘密只返回类型 / 长度 / 进程内随机 HMAC fingerprint / 路径 / 行号，**完整值永不出现在 canonical 输出**（设计级保证，非截断）
- **路径围栏**：所有路径经 lstat → realpath → containment 检查；`root` 固定为进程启动时解析的 `$DSH_HOME`（或管理员声明的 allowedRoot），模型参数不能扩大读取范围
- **诚实判定**：finding / pass / `skipped` / `error` 四态；`skipped` 与 `error` 不计为 pass（coverage 降为 `incomplete`）；`capability finding` 只提示人工确认、不裁定恶意
- **预算**：
- 工具参数会记入会话日志，不要传入敏感数据

## 📦 安装

```bash
# 交互式（web）profile
dsh plugin --profile web add github:omdsh-dev/dsh-security-audit
# 一次性任务（headless）profile —— dsh run 默认使用 headless
dsh plugin --profile headless add github:omdsh-dev/dsh-security-audit
```

## 🚀 快速开始

```bash
dsh plugin --profile web add dsh-security-audit-*.tgz
```

## 📚 更多信息

**输出示例**

{"tool":"security_audit","version":1,"root":"$DSH_HOME","platform":"win32","strict":false, "verdict":"fail","riskVerdict":"fail","coverageVerdict":"complete", "summary":{"critical":0,"high":1,"medium":0,"low":0}, "findings":[{"code":"secret-in-settings","severity":"high","state":"finding", "evidence":{"path":"$DSH_HOME/.env","line":13,"secretKind":"api-key","secretLength":35, "fingerprint":"b99e18

**安装**

DSH 0.1.2-rc.1（npm）下，插件通过 `dsh plugin --profile <profile> add <source>` 安装，source 支持 GitHub 仓库或 npm pack tarball。

**从 npm pack tarball 安装**

`npm pack` 产物可直接作为 source 安装： dsh plugin --profile web add dsh-security-audit-*.tgz 包内 `dsh.bundle.patch` 会在安装后自动把插件加入 profile 的 layer stack（row id：`security-audit`）。插件缺失的 peer 依赖（`@deepseek-ai/cordis`、`@deepseek-ai/dsh-tools`、`@deepseek-ai/dsh-invariants`）由 profile 的 healed `profiles/node_modules` 回退安装提供。 > ⚠️ web 与 headless 是**不同 profile**：web 安装不会自动覆盖 headless；`dsh run` 默认使用 headless profile。Wi

**旧场景：monorepo / 本地路径安装**

monorepo 方式已标注为旧场景（本地 junction/symlink、手动编辑 profile 层、不支持 GitHub/tarball source 的旧快照）： dsh plugin --profile web add "C:/path/to/dsh-security-audit"

## 🔗 链接

- [GitHub 仓库](https://github.com/omdsh-dev/dsh-security-audit)
- [完整 README](https://github.com/omdsh-dev/dsh-security-audit#readme)
- [返回dsh-security-audit所在分类](../plugins.md)
