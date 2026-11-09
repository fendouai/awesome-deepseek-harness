---
title: "dsh-sensitive-guard"
description: "为 DeepSeek Harness 提供敏感信息保护：密钥、令牌、密码（含 JSON / 配置字段）在进入模型上下文前替换为 <SG_> 占位符，明文以 AES-256-GCM 加密存在本地保管库。0.5.0 接入 gitleaks 官方 221 条规则（可搜索、逐条开关）、手动录入敏感数据与持久关闭保护；点小锁或复制按钮可看真值，模型通过导出文件取用凭据。"
keywords: "dsh-sensitive-guard, memory, plugin, coding, git, deepseek harness, dsh"
---
# dsh-sensitive-guard

> ⭐ **1** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [wangxy496](https://github.com/wangxy496) | Updated | — |

## One-liner

> 为 DeepSeek Harness 提供敏感信息保护：密钥、令牌、密码（含 JSON / 配置字段）在进入模型上下文前替换为 <SG_> 占位符，明文以 AES-256-GCM 加密存在本地保管库。0.5.0 接入 gitleaks 官方 221 条规则（可搜索、逐条开关）、手动录入敏感数据与持久关闭保护；点小锁或复制按钮可看真值，模型通过导出文件取用凭据。

## About

为 DeepSeek Harness 提供敏感信息保护：密钥、令牌、密码（含 JSON / 配置字段）在进入模型上下文前替换为 <SG_> 占位符，明文以 AES-256-GCM 加密存在本地保管库。0.5.0 接入 gitleaks 官方 221 条规则（可搜索、逐条开关）、手动录入敏感数据与持久关闭保护；点小锁或复制按钮可看真值，模型通过导出文件取用凭据。

## 🔗 Links

- [GitHub Repository](https://github.com/wangxy496/dsh-sensitive-guard)
- [Full README](https://github.com/wangxy496/dsh-sensitive-guard#readme)
- [Back to the Plugins list](../plugins.md)
