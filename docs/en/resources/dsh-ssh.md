---
title: "dsh-ssh"
description: "SSH remote workspaces for DeepSeek Harness — run bash, file, and search tools on any remote machine."
keywords: "dsh-ssh, search, plugin, coding, deepseek harness, dsh"
---
# dsh-ssh

> ⭐ **9** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 9 | Status | ✅ active |
| Author | [dsh-ssh](https://github.com/dsh-ssh) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, search |

## One-liner

> SSH remote workspaces for DeepSeek Harness — run bash, file, and search tools on any remote machine.

## About

**SSH remote-execution plugin for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness).** Moves Bash, file tools, PTY terminals, and LSP onto a remote host over a single SSH connection — with multi-hop ProxyJump chains, SFTP upload/download, and full auth coverage. Built on [ssh2](https://github.com/mscdex/ssh2).

## 📦 Install

```bash
npm i dsh-ssh
```

## 🚀 Quick Start

```bash
- id: ssh
  name: dsh-ssh/ssh            # ctx.ssh connection owner (config above)
- id: subprocess-ssh
  name: dsh-ssh/subprocess     # ctx.subprocess remote provider
- id: fs-ssh
  name: dsh-ssh/fs             # ctx.fs remote provider (SFTP)
```

## 📚 Learn more

**Architecture: local brain, remote hands**

Your machine (deepseek-harness) Remote host ┌────────────────────────────────────┐ SSH ┌──────────────────────┐ │ agent loop (orchestration, memory) │◄──────────►│ bash / command exec │ │ LLM API calls (direct, no egress) │ exec │ filesystem (SFTP) │ │ credentials / config / sessions │ pty │ PTY terminals │ │ ctx.subprocess → dsh-ssh │ sftp │ LSP / git / builds │ │ ctx.fs → dsh-ssh │ │ │ └────────

**Quick start (cordis.yml)**

**One row mounts everything** — the shared connection owner plus both remote providers: name: dsh-ssh config: host: server.example.com # target host (required; a ~/.ssh/config alias like prod works too) port: 22 username: root # required privateKey: ~/.ssh/id_ed25519 # identity-file path, or PEM content # password: 'xxx' # password auth (mutually usable with privateKey) # agent: 'pageant' # Window

**`~/.ssh/config` hosts in the sidebar (`config.hosts`)**

The「SSH 配置主机」sidebar section is driven by the `config.hosts` endpoint: every opening **re-reads** the host machine's `~/.ssh/config` and lists its **exact Host aliases** (wildcard patterns such as `*.example.com` stay hidden), each with the resolved `user@host:port`, IdentityFile presence, and ProxyJump presence: chain), **registers it silently, and drops you straight into that host's directory br

**Picker configuration (`dsh-ssh/picker`)**

`dsh-ssh/picker` now serves only the `ctx.directoryPicker` `browse` backend (local directories keep working on Windows hosts; POSIX absolute paths go to the aggregate SSH connection). The client UI's remote connection list and remote directory browsing ride the `dsh-ssh/web` RPC channel instead.

## 🔗 Links

- [GitHub Repository](https://github.com/dsh-ssh/dsh-ssh)
- [Full README](https://github.com/dsh-ssh/dsh-ssh#readme)
- [Back to the Plugins list](../plugins.md)
