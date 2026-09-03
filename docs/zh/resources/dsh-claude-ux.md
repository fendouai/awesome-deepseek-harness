---
title: "dsh-claude-ux"
description: "DSH plugin: Claude-style Chinese risk control & conversation autonomy for DeepSeek Harness web"
keywords: "dsh-claude-ux, search, plugin, coding, deepseek harness, dsh"
---
# dsh-claude-ux

> ⭐ **60** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 60 | 状态 | ✅ 活跃 |
| 作者 | [eri64](https://github.com/eri64) | 更新时间 | 2026-08-15 |
| 子分类 | 🌐 网页搜索 | 能力 | coding |

## 一句话介绍

> DSH plugin: Claude-style Chinese risk control & conversation autonomy for DeepSeek Harness web

## 详细介绍

Claude 式「区域风控 + 自主结束对话」插件 —— 适用于 DeepSeek Harness 的 web profile。 复刻 Anthropic/Claude 的两类行为，**除两个默认关闭的可选外部调用外全部本地判定**（详见 [docs/PRIVACY.md](docs/PRIVACY.md)）： - **区域风控（可反向）**：检测目标用户（时区、系统/浏览器语言、中文字体、代理、代理/中转域名黑名单、公网 IP 归属、WebRTC IP 一致性）。`regionTarget` 选 `cn` = 风控中国用户（Claude 原版行为），选 `non-cn` = **反向风控**（检测到不是中国人就风控）。命中后按惩罚阶梯处置：拒绝文案（带尝试计数）→ 达到 `refusalEndsAfter` 次数后结束会话（Chat ended 面板 + 服务端持续拒绝，重启后依然生效）→ 系统提示词注入模型级区域指令。 - **自主性**：用户持续辱骂或反复要求严重有害内容时，先警告、再主动结束对话；自伤/他伤风险消息永不触发结束（对齐 Claude 的公开限制）。辱骂结束与严重有害结束使用**独立文案**（均可在设置页自定义，空值灰字显示内置默认）。辱骂判定采用**词表秒判 + LLM 语境兜底**：强词（傻逼/fuck 等）直接判；弱词（垃圾/闭嘴等）与未命中消息由独立 LLM 请求做语境裁决（`purpose` 标记，**不进会话日志与模型上下文**；消息入队即异步预分类，近零额外延迟）。分类模型可直接从 **DSH 已配置的模型目录**下拉选择，或留空跟随会话主模型。 - **隐写通道**：系统提示词日期格式（`2026-06-30` ↔ `2026/06/30`）编码区域判定，Unicode 撇号变体（U+2019 ↔ U+02BC）编码黑名单命中。

## ✨ 核心特性

- **区域风控（可反向）**：检测目标用户（时区、系统/浏览器语言、中文字体、代理、代理/中转域名黑名单、公网 IP 归属、WebRTC IP 一致性）。`regionTarget` 选 `cn` = 风控中国用户（Claude 原版行为），选 `non-cn` = **反向风控**（检测到不是中国人就风控）。命中后按惩
- **自主性**：用户持续辱骂或反复要求严重有害内容时，先警告、再主动结束对话；自伤/他伤风险消息永不触发结束（对齐 Claude 的公开限制）。辱骂结束与严重有害结束使用**独立文案**（均可在设置页自定义，空值灰字显示内置默认）。辱骂判定采用**词表秒判 + LLM 语境兜底**：强词（傻逼/fuck 等）直接判；弱
- **隐写通道**：系统提示词日期格式（`2026-06-30` ↔ `2026/06/30`）编码区域判定，Unicode 撇号变体（U+2019 ↔ U+02BC）编码黑名单命中。

## 📦 安装

```bash
npx -y @deepseek-ai/dsh plugin --profile web add github:eri64/dsh-claude-ux
```

## 🚀 快速开始

```bash
npm test   # 运行主机（115 项）与客户端（17 项）单元测试，无需 dsh 实例
```

## 📚 更多信息

**安装（一条命令）**

npx -y @deepseek-ai/dsh plugin --profile web add github:eri64/dsh-claude-ux 包内自带注册条目（`dsh.bundle`），`dsh plugin` 安装后**自动注册**，无需手动改任何配置文件。 更新（升级到最新版）也是同一条命令。

**自定义默认配置（可选）**

内置默认值开箱即用；需要覆盖 patch 级选项（`blacklist` / `cnTimezones` / 词表等）时， 参考 [examples/cordis.patch.yml](examples/cordis.patch.yml) 修改包内 `node_modules/dsh-claude-ux/cordis.patch.yml` 后重新安装即可（设置页可改的项优先用设置页）。

**配置**

设置页可改：`enabled / regionPolicy / regionTarget / abuseEnabled / warnThreshold / endThreshold / refusalEndsAfter / warnEveryOffense / severeEndsImmediately / steganography / webRtcCheck / llmMode / llmProvider / llmModel / llmTimeoutMs / 四条文案`（保存即生效，无需重启）。其中分类模型**下拉直接列出 DSH 已配置的模型**（扫描 settings 的 providers 命名空间），留空=跟随会话主模型，「自定义…」可手填目录外的模型。 `blacklist / cnTimezones / 词表 / minSignals / showAttempts / p

## 🔗 链接

- [GitHub 仓库](https://github.com/eri64/dsh-claude-ux)
- [完整 README](https://github.com/eri64/dsh-claude-ux#readme)
- [返回dsh-claude-ux所在分类](../plugins.md)
