---
title: "dsh-sensitive-guard"
description: "为 DeepSeek Harness 提供敏感信息保护：密钥、令牌、密码（含 JSON / 配置字段）在进入模型上下文前替换为 <SG_> 占位符，明文以 AES-256-GCM 加密存在本地保管库。0.5.0 接入 gitleaks 官方 221 条规则（可搜索、逐条开关）、手动录入敏感数据与持久关闭保护；点小锁或复制按钮可看真值，模型通过导出文件取用凭据。"
keywords: "dsh-sensitive-guard, memory, plugin, coding, git, deepseek harness, dsh"
---
# dsh-sensitive-guard

> ⭐ **1** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 记忆与上下文 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [wangxy496](https://github.com/wangxy496) | 更新时间 | — |

## 一句话介绍

> 为 DeepSeek Harness 提供敏感信息保护：密钥、令牌、密码（含 JSON / 配置字段）在进入模型上下文前替换为 <SG_> 占位符，明文以 AES-256-GCM 加密存在本地保管库。0.5.0 接入 gitleaks 官方 221 条规则（可搜索、逐条开关）、手动录入敏感数据与持久关闭保护；点小锁或复制按钮可看真值，模型通过导出文件取用凭据。

## 详细介绍

为 DeepSeek Harness 提供敏感信息保护：密钥、令牌、密码（含 JSON / 配置字段）在进入模型上下文前替换为 <SG_> 占位符，明文以 AES-256-GCM 加密存在本地保管库。0.5.0 接入 gitleaks 官方 221 条规则（可搜索、逐条开关）、手动录入敏感数据与持久关闭保护；点小锁或复制按钮可看真值，模型通过导出文件取用凭据。

## 🔗 链接

- [GitHub 仓库](https://github.com/wangxy496/dsh-sensitive-guard)
- [完整 README](https://github.com/wangxy496/dsh-sensitive-guard#readme)
- [返回dsh-sensitive-guard所在分类](../plugins.md)
