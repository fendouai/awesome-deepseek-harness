---
title: "deepseek-harness-acp"
description: "DeepSeek Harness 的 ACP 服务器实现：复用凭据与会话，将完整 DSH Agent 暴露给 ACP 客户端。"
keywords: "deepseek-harness-acp, acp, integration, workflow, coding, deepseek harness, dsh"
---
# deepseek-harness-acp

> ⭐ **12** · ✅ 活跃 · 集成 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | ACP |
| 星数 | ⭐ 12 | 状态 | ✅ 活跃 |
| 作者 | [openma-ai](https://github.com/openma-ai) | 更新时间 | 2026-08-21 |

## 一句话介绍

> DeepSeek Harness 的 ACP 服务器实现：复用凭据与会话，将完整 DSH Agent 暴露给 ACP 客户端。

## 详细介绍

Both shapes share `$DSH_HOME`: the same credential store, settings, presets, and session logs as `dsh web` — conversations started in the Web UI can be listed and loaded from the editor. Other dsh surfaces can mount the transport-independent `@openma/deepseek-harness-acp/plugin` on their Base Host tree and own the transport adapter. The TUI profile uses this path: it starts a separate TUI Client process and connects ACP over that process's standard stdin/stdout; it does not start `dsh-acp` or use an in-process Client stream. The package is therefore not only a CLI wrapper. It is also the ACP surface plugin used by other dsh applications: one Host composition can expose the same sessions, tools, presets, skills, and persistence through a transport chosen by the surface.

## ✨ 核心特性

- **Streaming** — assistant text and reasoning deltas; assembled-message fallback.
- **Images** — `promptCapabilities.image` is advertised when the composition mounts `ctx.attachments` (dsh-base does). ACP `image` blocks are validated, stored wi
- **Tool calls** — ACP kinds, human titles, file locations, real diffs from fs-tool hunks, raw input/output; command output on a **display terminal** when the cli
- **Permission presets as session modes** — `read-only` / `workspace-write` / `danger-full-access`, each a named `{sandbox, approval}` pair recorded as a durable 
- **Agent composition** — when the profile mounts `agentPresets`, an uncategorized config option `id: "agent"` lists the roster (`standard` / `code` / `minimal` /
- **Live model catalog** — providers × models from the running composition (third-party providers added in the Web UI appear immediately), plus reasoning-effort s
- **Slash commands** — adapter built-ins (`/status`, `/model`) plus the harness command registry (`/compact`, `/goal`, `/permission`, `/plan`, …) executed without
- **Plans & usage** — `todo_write` snapshots as ACP plans; token accounting as `usage_update` and per-turn usage.

## 📦 安装

```bash
npm install -g @deepseek-ai/dsh
dsh web                                                    # save your API key once
dsh plugin --profile acp add @openma/deepseek-harness-acp@latest
```

## 🚀 快速开始

```bash
// Zed settings.json
{
  "agent_servers": {
    "DeepSeek Harness": { "command": "dsh", "args": ["--profile", "acp"] }
  }
}
```

## 📚 更多信息

**Configuration**

Flags win over environment variables, which win over defaults. All optional — with no flags, sessions follow your product defaults (`settings.yaml`). Subcommands: `dsh-acp login [api-key]` (interactive when omitted; input never echoes), `dsh-acp update` (self-update via npm).

**Architecture**

ACP client (Zed, …) │ ACP JSON-RPC over stdio ▼ dsh-acp ├─ src/bin.ts selects one DSH tree before Host imports evaluate ├─ src/profile-boot.ts boots the harness's own profile machinery │ (dsh-base + this bundle + $DSH_HOME layers) ├─ src/harness.ts host discovery (DSH_PATH → cwd → PATH → npm -g → bundled runtime) └─ src/bridge/ the ACP bridge (a cordis plugin) ├─ index.ts sessions, prompts, cancel

## 🔗 链接

- [GitHub 仓库](https://github.com/openma-ai/deepseek-harness-acp)
- [完整 README](https://github.com/openma-ai/deepseek-harness-acp#readme)
- [返回deepseek-harness-acp所在分类](../integrations.md)
