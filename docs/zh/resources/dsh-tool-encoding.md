---
title: "dsh-tool-encoding"
description: "DSH 编码/哈希工具插件：base64/base64url/url/hex 编解码、md5/sha1/sha256/sha512 哈希、UUID 生成，零依赖"
keywords: "dsh-tool-encoding, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-tool-encoding

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [omdsh-dev](https://github.com/omdsh-dev) | 更新时间 | — |
| 子分类 | 💡 生成式界面 | 能力 | coding, ui |

## 一句话介绍

> DSH 编码/哈希工具插件：base64/base64url/url/hex 编解码、md5/sha1/sha256/sha512 哈希、UUID 生成，零依赖

## 详细介绍

[English](README.en.md) DSH 编码/哈希工具插件 —— UTF-8 文本的 base64/base64url/url/hex 编解码 + 哈希 + UUID。零依赖、零进程、纯函数。

## ✨ 核心特性

- **UTF-8 完整性**：解码用 fatal 模式（`TextDecoder('utf-8', { fatal: true })`），非法字节抛 `encoding: invalid UTF-8 output`；合法 U+FFFD/控制字符不误伤（`00` NUL、`0a` 换行、`efbfbd` U+FFFD 均合
- **base64 严格校验**：无空白、`=` 仅末尾且 ≤2、长度必须为 4 的倍数、**RFC 4648 canonical unused bits**（`Zh==` 等非 canonical 编码拒绝，防多串映射同文本）
- **孤立 surrogate 统一拒绝**：所有文本输入过 `String.prototype.isWellFormed()`，避免静默替换与 URIError 行为不一致
- **字节上限**：输入 1 MB / 输出 4 MB（各 1,000,000 / 4,000,000 字节，`Buffer.byteLength`；输出上限为分配前预估 + 最终检查的保险丝）
- **哈希算法白名单**：`Object.hasOwn` 查表（md5/sha1/sha256/sha512）
- 错误统一 `encoding:` 前缀，不透传底层 `URIError`/`TypeError`

## 📦 安装

```bash
# 交互式（web）profile
dsh plugin --profile web add github:omdsh-dev/dsh-tool-encoding
# 一次性任务（headless）profile —— dsh run 默认使用 headless
dsh plugin --profile headless add github:omdsh-dev/dsh-tool-encoding
```

## 🚀 快速开始

```bash
npm pack    # 生成 dsh-tool-encoding-*.tgz
dsh plugin --profile web add ./dsh-tool-encoding-*.tgz
dsh plugin --profile headless add ./dsh-tool-encoding-*.tgz
```

## 📚 更多信息

**一次性任务（headless）profile —— dsh run 默认使用 headless**

dsh plugin --profile headless add github:omdsh-dev/dsh-tool-encoding 包内 `dsh.bundle.patch`（指向 `cordis.patch.yml`）会在安装后自动把插件加入 profile 的 layer stack；插件的 `cordis.patch.yml` 以 `- insert:` 插入 `tool-encoding` 条目。 > ⚠️ web 与 headless 是**不同 profile**：web 安装不会自动覆盖 headless；`dsh run` 默认使用 headless profile。

**npm pack tarball 安装**

npm pack # 生成 dsh-tool-encoding-*.tgz dsh plugin --profile web add ./dsh-tool-encoding-*.tgz dsh plugin --profile headless add ./dsh-tool-encoding-*.tgz

**手动安装与旧版本兼容**

仅适用于不支持 Profile Bundle 的旧快照或插件开发调试环境： 1. 放入 monorepo：`cp -r encoding ~/.dsh/source/master/packages/tools/encoding`（开发调试） 2. `apps/cli/package.json` 加 `"@deepseek-ai/dsh-tool-encoding": "workspace:^"`；`tsconfig.host.json` references 加 `{ "path": "./packages/tools/encoding" }` 3. `pnpm install && pnpm run build` 4. 在 profile 用户层 patch 插入插件（`~/.dsh/profiles/<name>/cordis.patch.yml`）： - id: tool-encod

## 🔗 链接

- [GitHub 仓库](https://github.com/omdsh-dev/dsh-tool-encoding)
- [完整 README](https://github.com/omdsh-dev/dsh-tool-encoding#readme)
- [返回dsh-tool-encoding所在分类](../plugins.md)
