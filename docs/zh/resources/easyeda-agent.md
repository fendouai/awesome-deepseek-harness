---
title: "easyeda-agent"
description: "EasyEDA Pro automation: Go daemon + in-app connector + agent skill + stdio MCP server for typed schematic/PCB actions, workflow gates, and DRC."
keywords: "easyeda-agent, learning, skill, mcp, coding, deepseek harness, dsh"
---
# easyeda-agent

> ⭐ **274** · ✅ 活跃 · 技能 · 近期 ⬆️ +16

| | | | |
|---|---|---|---|
| 类型 | 技能 | 分类 | 学习 |
| 星数 | ⭐ 274 | 状态 | ✅ 活跃 |
| 作者 | [zhoushoujianwork](https://github.com/zhoushoujianwork) | 更新时间 | 2026-08-21 |

## 一句话介绍

> EasyEDA Pro automation: Go daemon + in-app connector + agent skill + stdio MCP server for typed schematic/PCB actions, workflow gates, and DRC.

## 详细介绍

上游 `run-api-gateway` 证明了关键入口:代码能跑在 EasyEDA 内、访问官方 `eda` 对象。但它把「裸 JavaScript 执行」当作主工作流——强大,但对 AI agent 太脆弱。 本项目的连接器是真实可用的:daemon **固定监听单端口 `60832`(`0xEDA0`,"EDA" 写进十六进制;0.15.0 起弃用与官方 gateway 冲突的 49620)**(不外溢、被占用时自动接管旧 easyeda daemon)、连接器锁定该端口、校验握手、**自愈重连**、把一套**有类型的动作目录**分发到官方 `eda.*` API。裸 JS 仅作为需二次确认的 `debug.exec_js` 逃生口保留。 - **Skill** 描述专家工作流和护栏; - **Go CLI/daemon** 暴露稳定的 typed actions; - **EasyEDA 连接器插件** 只做到官方 `eda.*` 的桥接; - 产物、截图、DRC 结果、审计日志都是一等输出。

## ✨ 核心特性

- **社区共建 + 署名可追**:每个块带 `author`/`contributors`,**一次学习贡献、永久收益**;
- **验证门禁**:块必须跑过 `place → wire → check → DRC=0` 才入库,不是「看着对」的散文堆;
- **三维知识**:器件(可替换选择)+ 原理图链接注意 + PCB 布局电气特性,一块讲全;
- **AI 直接消费**:agent 放外设前先查块库,命中即抄,省掉一整个模块的选型与接线。

## 🚀 快速开始

```bash
curl -fsSL https://raw.githubusercontent.com/zhoushoujianwork/easyeda-agent/main/install.sh | sh
```

## 📚 更多信息

**工作原理**

动作目录已覆盖原理图、PCB、文档导航、板级绑定、产物导出、诊断。完整清单与路线图见 [docs/FEATURES.md](docs/FEATURES.md)。

**安装**

> **完整上手 & 使用注意事项见 [快速开始 →](docs/quick-start.md)** —— 四件套 > (CLI / 连接器 `.eext` / Skill / EasyEDA)的安装、版本对齐、启动 daemon、升级纪律 > 与常见卡点速查,一页讲清。下面是精简版。 easyeda-agent 是一套**四件套**,四者需**同版本、同时在位**:CLI/daemon、连接器 `.eext` 插件、`easyeda-agent` Skill、开启「允许外部交互」的 EasyEDA Pro。**升级时 三方(CLI + 连接器 + Skill)要一起升到同一版本**,否则 `easyeda daemon health` 会把 落后的连接器标成 stale。 先装 `easyeda` CLI/daemon,再装 EasyEDA 连接器 —— 两条通道任选:安装器会打印**与

**实战展示:一份需求文档 → 三页原理图正式交付**

v1.0.0 的原理图全流程真机成图(esp32Mini 固定回归用例):输入只是一份**不含 BOM/网表的 客户口吻需求文档**,agent 沿 S0–S6 自己完成选型、放置、连线、分区与门禁—— **3 页原理图 / 26 个真实 LCSC 库件 / 18 网黄金表逐脚全对 / 复用 6 个电路块 / 8 个分区框 + 7 条电路说明**,分区框、区名与电路说明全部由算法计算落位,逐页 `sch gate --strict` 通过。 P1 电源页:AMS1117 LDO(5V→3V3)分区框 + 区名 + 电路说明,全部算法计算落位。 P2 主控页:WROOM 最小系统、BOOT/RESET 按键、指示 LED 三个功能分区。 P3 USB 页:CH340 USB 串口、USB-C 接口、自动下载等四个功能分区。 > **完整实战案例:[一份需求文档 → AI 全自动画完 ESP3

**原理图自动放置:两个引擎(模板 vs 官方)**

同一个 ESP32-S3R8 最小系统块,两种放置引擎的真机对比(都 `sch check` 0 悬空导线、已连线): 两版都能用、都还有少量重叠(模板版当前还会碰标题栏右下角,官方版散件间距不均),**放置的正确性由机械门禁保证**:`sch layout-lint`(真实 bbox 查重叠)+ `sch check`/`bridge-check`(查断线/短路)。多页工程/长操作用 `--doc <page>` flag **机制性地钉住目标页**,不再靠人工切页(避免长命令落错页)。 > 官方引擎在真正调用 `autoLayout()` 前会二次核对同一页的部件姿态、sheet 与全部 connectivity（wire/bus/net marker），并在启动变异的同一个 JS action 内再锁一次 document/input；`--rewire` 还核对完整网表，输入漂移立

## 🔗 链接

- [GitHub 仓库](https://github.com/zhoushoujianwork/easyeda-agent)
- [完整 README](https://github.com/zhoushoujianwork/easyeda-agent#readme)
- [返回easyeda-agent所在分类](../skills.md)
